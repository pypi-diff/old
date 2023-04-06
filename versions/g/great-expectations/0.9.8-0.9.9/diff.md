# Comparing `tmp/great_expectations-0.9.8.tar.gz` & `tmp/great_expectations-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/great_expectations-0.9.8.tar", last modified: Fri Apr  3 22:14:39 2020, max compression
+gzip compressed data, was "dist/great_expectations-0.9.9.tar", last modified: Tue Apr  7 22:35:27 2020, max compression
```

## Comparing `great_expectations-0.9.8.tar` & `great_expectations-0.9.9.tar`

### file list

```diff
@@ -1,549 +1,551 @@
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/
--rw-rw-r--   0 travis    (2000) travis    (2000)      277 2020-04-03 22:12:05.000000 great_expectations-0.9.8/MANIFEST.in
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/examples/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/examples/integrations/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/examples/integrations/airflow/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/examples/integrations/airflow/hooks/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1909 2020-04-03 22:12:05.000000 great_expectations-0.9.8/examples/integrations/airflow/hooks/s3_csv_hook.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/examples/integrations/airflow/hooks/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      609 2020-04-03 22:12:05.000000 great_expectations-0.9.8/examples/integrations/airflow/hooks/db_hook.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/examples/integrations/airflow/operators/
--rw-rw-r--   0 travis    (2000) travis    (2000)     7268 2020-04-03 22:12:05.000000 great_expectations-0.9.8/examples/integrations/airflow/operators/expectation_operator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/examples/integrations/airflow/operators/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/examples/integrations/airflow/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/examples/integrations/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    68611 2020-04-03 22:12:05.000000 great_expectations-0.9.8/versioneer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      359 2020-04-03 22:12:05.000000 great_expectations-0.9.8/requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     1136 2020-04-03 22:14:39.000000 great_expectations-0.9.8/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)    14424 2020-04-03 22:12:05.000000 great_expectations-0.9.8/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)      570 2020-04-03 22:12:05.000000 great_expectations-0.9.8/requirements-dev.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)        3 2020-04-03 22:12:05.000000 great_expectations-0.9.8/runtime.txt
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)    20398 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/util.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/dataset/
--rw-rw-r--   0 travis    (2000) travis    (2000)    21173 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/dataset/util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    61870 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/dataset/pandas_dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    45964 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/dataset/sqlalchemy_dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    38483 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/dataset/sparkdf_dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   183846 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/dataset/dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      544 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/dataset/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/validator/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4402 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/validator/validator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/validator/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/types/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1831 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/types/expectations.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      607 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/types/configurations.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1558 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/types/base.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      656 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/types/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2815 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/util.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/types/
--rw-rw-r--   0 travis    (2000) travis    (2000)    12829 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/types/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      126 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/exceptions.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/view/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/view/static/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/view/static/styles/
--rw-rw-r--   0 travis    (2000) travis    (2000)      699 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/styles/data_docs_custom_styles_template.css
--rw-rw-r--   0 travis    (2000) travis    (2000)     2545 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/styles/data_docs_default_styles.css
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/
--rw-rw-r--   0 travis    (2000) travis    (2000)    58656 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-MediumItalic.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    58764 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Italic.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    53216 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Bold.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    58520 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-LightItalic.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    54588 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Light.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    58752 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBoldItalic.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    54956 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Medium.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    57068 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-BoldItalic.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    54836 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBold.otf
--rw-rw-r--   0 travis    (2000) travis    (2000)    55152 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Regular.otf
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/
--rw-rw-r--   0 travis    (2000) travis    (2000)    39235 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/logo-long-vector.svg
--rw-rw-r--   0 travis    (2000) travis    (2000)    20317 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/iterative-dev-loop.png
--rw-rw-r--   0 travis    (2000) travis    (2000)  2563400 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/glossary_scroller.gif
--rw-rw-r--   0 travis    (2000) travis    (2000)   812992 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/validation_failed_unexpected_values.gif
--rw-rw-r--   0 travis    (2000) travis    (2000)     6310 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/short-logo.png
--rw-rw-r--   0 travis    (2000) travis    (2000)    39138 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/short-logo-vector.svg
--rw-rw-r--   0 travis    (2000) travis    (2000)     9306 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/logo-long.png
--rw-rw-r--   0 travis    (2000) travis    (2000)     1150 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/static/images/favicon.ico
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/view/templates/
--rw-rw-r--   0 travis    (2000) travis    (2000)      415 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/section.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     2365 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/page_action_card.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     2678 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/edit_expectations_instructions_modal.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      318 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/value_list.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)       63 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/string_template.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      593 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/js_script_imports.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     1684 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/header.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     2839 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/collapse.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      927 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/component.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     1912 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/top_navbar.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     1599 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/index_page.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      885 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/ge_info.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      939 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/text.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     1036 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/cta_footer.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      712 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/graph.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      503 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/content_block_container.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)       49 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/markdown.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      667 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/favicon.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      278 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/sidebar.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     1677 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/page.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     1440 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/table_of_contents.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)      875 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/bullet_list.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)    16458 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/carousel_modal.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     1464 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/table.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)     2024 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/templates/content_block_header.j2
--rw-rw-r--   0 travis    (2000) travis    (2000)    12321 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/view.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      138 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/view/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       48 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/renderer/
--rw-rw-r--   0 travis    (2000) travis    (2000)    27966 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/column_section_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12335 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/other_section_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27520 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/page_renderer.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4846 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/profiling_overview_table_content_block.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      628 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/bullet_list_content_block.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2654 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/exception_list_content_block.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11512 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/content_block.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    65166 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/expectation_string.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    15884 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/validation_results_table_content_block.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      476 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/content_block/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14326 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/site_index_page_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27378 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/site_builder.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1849 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/call_to_action_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4935 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/renderer.py
--rwxrwxr-x   0 travis    (2000) travis    (2000)     9828 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/notebook_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      553 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3826 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/render/renderer/slack_renderer.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/data_asset/
--rw-rw-r--   0 travis    (2000) travis    (2000)     7155 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_asset/util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27791 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_asset/file_data_asset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10206 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_asset/evaluation_parameters.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       76 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_asset/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    59797 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_asset/data_asset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      497 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/_version.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/init_notebooks/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/init_notebooks/sql/
--rw-rw-r--   0 travis    (2000) travis    (2000)     7741 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/init_notebooks/sql/validation_playground.ipynb
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/init_notebooks/spark/
--rw-rw-r--   0 travis    (2000) travis    (2000)     7597 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/init_notebooks/spark/validation_playground.ipynb
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/init_notebooks/pandas/
--rw-rw-r--   0 travis    (2000) travis    (2000)     7459 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/init_notebooks/pandas/validation_playground.ipynb
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/datasource/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1162 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/util.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/datasource/generator/
--rw-rw-r--   0 travis    (2000) travis    (2000)     8669 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/table_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12507 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/s3_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9363 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/subdir_reader_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4813 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/query_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4760 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/manual_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1755 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/databricks_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8230 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/batch_kwargs_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      432 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9334 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/generator/glob_reader_generator.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/datasource/types/
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/types/reader_methods.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5436 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/types/batch_kwargs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       28 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/types/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8462 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/sparkdf_datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9206 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/sqlalchemy_datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11799 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/pandas_datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12009 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      189 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/datasource/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/profile/
--rw-rw-r--   0 travis    (2000) travis    (2000)    11273 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/profile/basic_dataset_profiler.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1316 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/profile/columns_exist.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13393 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/profile/sample_expectations_dataset_profiler.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8335 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/profile/multi_batch_validation_meta_analysis.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      569 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/profile/metrics_utils.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2856 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/profile/base.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      105 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/profile/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8474 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/exceptions.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/data_context/
--rw-rw-r--   0 travis    (2000) travis    (2000)     8478 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5489 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/templates.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/data_context/types/
--rw-rw-r--   0 travis    (2000) travis    (2000)     7839 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/types/resource_identifiers.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        9 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/types/base_resource_identifiers.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8046 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/types/base.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/types/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/data_context/store/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2200 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/expectations_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11205 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/html_site_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2375 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/validations_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3241 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3072 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/store_backend.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2552 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/database_store_backend.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3123 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/metric_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1228 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    19548 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/store/tuple_store_backend.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    75195 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/data_context.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      118 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/data_context/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/expectation_suite.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/validation_operators/
--rw-rw-r--   0 travis    (2000) travis    (2000)      902 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/validation_operators/util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    21318 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/validation_operators/validation_operators.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10149 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/validation_operators/actions.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      808 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/validation_operators/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/cli/
--rw-rw-r--   0 travis    (2000) travis    (2000)     3013 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/init_messages.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1753 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5683 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/init.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1443 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/project.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2316 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/docs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1821 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/cli.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9120 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/suite.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8436 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/validation_operator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1158 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/tap_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    57063 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/datasource.py
--rwxrwxr-x   0 travis    (2000) travis    (2000)       27 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2881 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/tap.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      732 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/cli/cli_logging.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/core/
--rw-rw-r--   0 travis    (2000) travis    (2000)      611 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/core/util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      721 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/core/id_dict.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6845 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/core/metric.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1041 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/core/data_context_key.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    36111 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/core/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      891 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/core/batch.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      313 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations/jupyter_ux/
--rw-rw-r--   0 travis    (2000) travis    (2000)    75137 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/jupyter_ux/expectation_explorer.py
--rwxrwxr-x   0 travis    (2000) travis    (2000)    11805 2020-04-03 22:12:05.000000 great_expectations-0.9.8/great_expectations/jupyter_ux/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      278 2020-04-03 22:14:39.000000 great_expectations-0.9.8/setup.cfg
--rw-rw-r--   0 travis    (2000) travis    (2000)    11357 2020-04-03 22:12:05.000000 great_expectations-0.9.8/LICENSE
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations.egg-info/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1136 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations.egg-info/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations.egg-info/dependency_links.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       34 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations.egg-info/top_level.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)    24684 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations.egg-info/SOURCES.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      463 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations.egg-info/requires.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       68 2020-04-03 22:14:39.000000 great_expectations-0.9.8/great_expectations.egg-info/entry_points.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     1959 2020-04-03 22:12:05.000000 great_expectations-0.9.8/setup.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_plugins/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1113 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_plugins/fake_configs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      185 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_plugins/fake_actions.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_plugins/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/dataset/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1837 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/test_dataset_legacy.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    37358 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/test_dataset_util_legacy.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      304 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/test_dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1935 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/test_util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      669 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/test_sparkdfdataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8308 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/test_sqlalchemydataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    23909 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/dataset/test_pandas_dataset.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_dataset_implementations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     5479 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_dataset_implementations/test_dataset_implementations.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_dataset_implementations/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13303 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_dataset_implementations/test_dataset_implementations.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/render/
--rw-rw-r--   0 travis    (2000) travis    (2000)     7955 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_data_documentation_site_builder.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/render/fixtures/
--rw-rw-r--   0 travis    (2000) travis    (2000)    11751 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/fixtures/SampleExpectationsDatasetProfiler_evrs.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    49037 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_evrs_with_exception.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    51876 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_evrs.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     9982 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_expectations.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    10064 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_expectations_with_distribution.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3767 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_styled_string_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    15205 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_render.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    25664 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_render_ValidationResultsTableContentBlockRenderer.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/render/output/
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/output/.gitkeep
--rw-rw-r--   0 travis    (2000) travis    (2000)     3314 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_render_BulletListContentBlock.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3777 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    17844 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_page_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    19923 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_default_jinja_view.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1864 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2700 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_SlackRenderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4054 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_render_ExceptionListContentBlockRenderer.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/render/renderer/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/render/renderer/content_block/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1513 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/renderer/content_block/test_expectation_string_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/renderer/content_block/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/renderer/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    69395 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/renderer/test_notebook_renderer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    49257 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/render/test_column_section_renderer.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_asset/
--rw-rw-r--   0 travis    (2000) travis    (2000)    18695 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_expectation_decorators.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8726 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_filedata_asset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13178 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_filedata_asset_expectations.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3349 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_data_asset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33477 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_data_asset_internals.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      518 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_data_asset_citations.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6367 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_parameter_substitution.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5196 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_asset/test_data_asset_util.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    20654 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_great_expectations.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/datasource/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/datasource/generator/
--rw-rw-r--   0 travis    (2000) travis    (2000)     6018 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/test_subdir_reader_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6494 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/test_s3_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1867 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/test_manual_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      362 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/test_batch_kwargs_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4852 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/test_table_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3191 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/test_query_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10149 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/generator/test_glob_reader_generator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      191 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/test_sqlalchemy_datasource_workarounds.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2306 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/test_batch_kwargs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10302 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/test_sqlalchemy_datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12936 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/test_sparkdf_datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6593 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/test_batch_generators.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      682 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/conftest.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13153 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/datasource/test_pandas_datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6111 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_configs.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_sets/
--rw-rw-r--   0 travis    (2000) travis    (2000)       80 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/toy_data_incomplete.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)     8704 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/test_partitions.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      126 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/invalid_json_file.json
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/null_file.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)    76128 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_base.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)    94208 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/titanic.db
--rw-rw-r--   0 travis    (2000) travis    (2000)       68 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/same_column_names.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)       23 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/unicode.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)   101861 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/Titanic_multi_sheet.xlsx
--rw-rw-r--   0 travis    (2000) travis    (2000)      100 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/toy_data_complete.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)    70366 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/Titanic.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)     1351 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/test_json_data_file.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    95990 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/Titanic.pkl
--rw-rw-r--   0 travis    (2000) travis    (2000)    51876 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/expected_evrs_BasicDatasetProfiler_on_titanic.json
--rw-rw-r--   0 travis    (2000) travis    (2000)       62 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/strf_test.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)     1688 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/nested_test_json_data_file.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    11751 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/expected_evrs_SampleExpectationsDatasetProfiler_on_titanic.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2202 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/expected_cli_results_custom.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     6275 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/expected_cli_results_default.json
--rw-rw-r--   0 travis    (2000) travis    (2000)       11 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/white_space.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)    76045 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_test.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)     4934 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/titanic_expected_data_asset_validate_results.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    65691 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/fixed_distributional_test_dataset.csv
--rw-rw-r--   0 travis    (2000) travis    (2000)     1557 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/titanic_expectations.json
--rwxrwxr-x   0 travis    (2000) travis    (2000)     3688 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/broken_excel_file.xls
--rw-rw-r--   0 travis    (2000) travis    (2000)       34 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/json_test2_against_schema.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    34948 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/Titanic.parquet
--rw-rw-r--   0 travis    (2000) travis    (2000)      195 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/test_partition_serialized_infinity_bins.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      115 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/sample_schema.json
--rw-rw-r--   0 travis    (2000) travis    (2000)       38 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/json_test1_against_schema.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     7705 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/titanic_expected_data_asset_validate_results_with_exceptions.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    85069 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_base.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1660 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/titanic_parameterized_expectations.json
--rw-rw-r--   0 travis    (2000) travis    (2000)   141917 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/fixed_distributional_test_dataset.json
--rw-rw-r--   0 travis    (2000) travis    (2000)       35 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/titanic_evaluation_parameters.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      246 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/titanic_custom_expectations.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    85178 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_test.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    12279 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_sets/test_partitions_definition_fixture.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_definitions/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4204 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_median_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1834 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_proportion_of_unique_values_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     5740 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_mean_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     4350 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_min_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2933 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_contain_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     5304 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_be_in_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2948 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_equal_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3530 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_stdev_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3127 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_sum_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    83561 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_quantile_values_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1824 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_unique_value_count_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3044 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_most_common_value_to_be_in_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     4115 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_max_to_be_between.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_definitions/multicolumn_map_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     3086 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/multicolumn_map_expectations/expect_multicolumn_values_to_be_unique.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4764 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3267 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_null.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1465 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_json_schema.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2657 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex_list.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3997 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_strftime_format.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3689 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3992 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     4811 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2818 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_null.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    13126 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_of_type.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2249 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_equal.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1709 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex_list.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2460 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_decreasing.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    12797 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2433 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_increasing.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     8702 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_type_list.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3623 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_in_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     3411 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_unique.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_definitions/column_pair_map_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     3454 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_equal.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2012 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_in_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2386 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_A_to_be_greater_than_B.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1641 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_columns_to_match_ordered_list_test_set.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1899 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_row_count_to_equal.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2327 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_column_count_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      533 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_this_test_to_be_suppressed.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1110 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_column_to_exist.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2261 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_row_count_to_be_between.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2020 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_column_count_to_equal.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     7014 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/test_expectations.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)    57692 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than.json
--rw-rw-r--   0 travis    (2000) travis    (2000)   105938 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/test_expect_column_bootstrapped_ks_test_p_value_to_be_greater_than.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    10564 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/expect_column_chisquare_test_p_value_to_be_greater_than.json
--rw-rw-r--   0 travis    (2000) travis    (2000)   126107 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/expect_column_kl_divergence_to_be_less_than.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/profile/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2940 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/profile/test_multi_batch_validation_meta_analysis.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    17402 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/profile/test_SampleExpectationsDatasetProfiler.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    17932 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/profile/test_profile.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/profile/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1633 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_autoinspect.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      632 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/build_index_page.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/contexts/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     5155 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/uncommitted/
--rw-rw-r--   0 travis    (2000) travis    (2000)      991 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/uncommitted/config_variables.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)       90 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/.gitignore
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/invalid_config_version/
--rw-rw-r--   0 travis    (2000) travis    (2000)      970 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/invalid_config_version/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1836 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/cluster-paintings.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      191 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)    66315 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/elements-by-episode.csv
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2413 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/index.html
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/bob-ross/
--rw-rw-r--   0 travis    (2000) travis    (2000)   146908 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/bob-ross/
--rw-rw-r--   0 travis    (2000) travis    (2000)   360054 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.html
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/index.html
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/bob-ross/
--rw-rw-r--   0 travis    (2000) travis    (2000)   146908 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/bob-ross/
--rw-rw-r--   0 travis    (2000) travis    (2000)   233898 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.json
--rw-rw-r--   0 travis    (2000) travis    (2000)       12 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/.gitignore
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/sql/
--rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/sql/create_expectations.ipynb
--rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/sql/validation_playground.ipynb
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/spark/
--rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/spark/create_expectations.ipynb
--rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/spark/validation_playground.ipynb
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/pandas/
--rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/pandas/create_expectations.ipynb
--rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/pandas/validation_playground.ipynb
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/
--rw-rw-r--   0 travis    (2000) travis    (2000)    97613 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/warning.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    97626 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      684 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/quarantine.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      684 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/failure.json
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/bad_yml/
--rw-rw-r--   0 travis    (2000) travis    (2000)       57 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/bad_yml/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/invalid_top_level_key/
--rw-rw-r--   0 travis    (2000) travis    (2000)      547 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/invalid_top_level_key/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/invalid_top_level_value_type/
--rw-rw-r--   0 travis    (2000) travis    (2000)      281 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/invalid_top_level_value_type/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/old_config_version/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1022 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/old_config_version/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/version_zero/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2476 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/version_zero/great_expectations.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/fixtures/missing_top_level_key/
--rw-rw-r--   0 travis    (2000) travis    (2000)      217 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/fixtures/missing_top_level_key/great_expectations.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)     4568 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_configuration_storage.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2190 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_data_context_resource_identifiers.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2788 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_data_context_config_errors.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    41731 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_data_context.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1134 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_data_context_utils.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/data_context/store/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4359 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/store/test_html_site_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6635 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/store/test_validations_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8697 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/store/test_store_backends.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6622 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/store/test_evaluation_parameter_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2039 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/store/test_expectations_store.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/store/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3195 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_data_context_store_configs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      931 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_data_context_on_teams.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5017 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/test_data_context_config_variables.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3641 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/data_context/conftest.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/cli/
--rw-rw-r--   0 travis    (2000) travis    (2000)    38336 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_suite.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3359 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_docs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1981 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_project.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22534 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_init_pandas.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14055 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_datasource_pandas.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3016 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/utils.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18676 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_datasource_sqlite.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5061 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_cli.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8758 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_validation_operator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6306 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_init_missing_libraries.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9661 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_taps_pandas.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      118 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    19249 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_init_sqlite.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7804 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/cli/test_init.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6207 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_ge_utils.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/core/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1098 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/core/test_serialization.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9779 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/core/test_expectation_suite.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3820 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/core/test_evaluation_parameters.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2938 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/core/test_expectation_configuration.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/core/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1207 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/core/test_expectation_kwargs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    64653 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/conftest.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_fixtures/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2040 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/great_expectations_basic_without_config_variables_filepath.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)     3520 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/distributional_expectations_partition_fixtures.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       20 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/config_variables.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)     2466 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/great_expectations_basic.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/dummy.sql
--rw-rw-r--   0 travis    (2000) travis    (2000)     1026 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/custom_pandas_dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      695 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/custom_sqlalchemy_dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1747 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/custom_sparkdf_dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2797 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/fixed_distribution_data.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/
--rw-rw-r--   0 travis    (2000) travis    (2000)    13931 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/expectation_suite_3.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    48940 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/evr_suite_3.json
--rw-rw-r--   0 travis    (2000) travis    (2000)    52125 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/expectations_suite_2.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      924 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/expectations_suite_1.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2556 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/evr_suite_1.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     5452 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/great_expectations_site_builder.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/test_fixtures/expectation_suites/
--rw-rw-r--   0 travis    (2000) travis    (2000)      886 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/expectation_suites/parameterized_expectation_suite_fixture.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     2186 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/great_expectations_basic_with_variables.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)     2009 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_fixtures/great_expectations_titanic.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)    27757 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/test_utils.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/actions/
--rw-rw-r--   0 travis    (2000) travis    (2000)     4522 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/actions/test_validation_operators_in_data_context.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5396 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/actions/test_core_actions.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/actions/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2952 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/actions/conftest.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5212 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/actions/test_store_metric_action.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7255 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/actions/test_validation_operators.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-03 22:14:39.000000 great_expectations-0.9.8/tests/jupyter_ux/
--rw-rw-r--   0 travis    (2000) travis    (2000)     5278 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/jupyter_ux/test_jupyter_ux.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-03 22:12:05.000000 great_expectations-0.9.8/tests/jupyter_ux/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      277 2020-04-07 22:32:57.000000 great_expectations-0.9.9/MANIFEST.in
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/examples/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/examples/integrations/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/examples/integrations/airflow/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/examples/integrations/airflow/hooks/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1909 2020-04-07 22:32:58.000000 great_expectations-0.9.9/examples/integrations/airflow/hooks/s3_csv_hook.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/examples/integrations/airflow/hooks/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      609 2020-04-07 22:32:58.000000 great_expectations-0.9.9/examples/integrations/airflow/hooks/db_hook.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/examples/integrations/airflow/operators/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7268 2020-04-07 22:32:58.000000 great_expectations-0.9.9/examples/integrations/airflow/operators/expectation_operator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/examples/integrations/airflow/operators/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/examples/integrations/airflow/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/examples/integrations/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    68611 2020-04-07 22:32:58.000000 great_expectations-0.9.9/versioneer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      359 2020-04-07 22:32:58.000000 great_expectations-0.9.9/requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1136 2020-04-07 22:35:27.000000 great_expectations-0.9.9/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14424 2020-04-07 22:32:57.000000 great_expectations-0.9.9/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)      570 2020-04-07 22:32:58.000000 great_expectations-0.9.9/requirements-dev.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        3 2020-04-07 22:32:58.000000 great_expectations-0.9.9/runtime.txt
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20398 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/util.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/dataset/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21173 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/dataset/util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    61870 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/dataset/pandas_dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    45964 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/dataset/sqlalchemy_dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    38483 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/dataset/sparkdf_dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   183846 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/dataset/dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      544 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/dataset/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/validator/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4402 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/validator/validator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/validator/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/types/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1831 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/types/expectations.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      607 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/types/configurations.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1558 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/types/base.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      656 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/types/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2815 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/util.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/types/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12829 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/types/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      126 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/exceptions.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/view/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/view/static/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/view/static/styles/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      699 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/styles/data_docs_custom_styles_template.css
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2545 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/styles/data_docs_default_styles.css
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    58656 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-MediumItalic.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    58764 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Italic.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    53216 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Bold.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    58520 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-LightItalic.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    54588 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Light.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    58752 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBoldItalic.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    54956 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Medium.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    57068 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-BoldItalic.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    54836 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBold.otf
+-rw-rw-r--   0 travis    (2000) travis    (2000)    55152 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Regular.otf
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    39235 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/logo-long-vector.svg
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20317 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/iterative-dev-loop.png
+-rw-rw-r--   0 travis    (2000) travis    (2000)  2563400 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/glossary_scroller.gif
+-rw-rw-r--   0 travis    (2000) travis    (2000)   812992 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/validation_failed_unexpected_values.gif
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6310 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/short-logo.png
+-rw-rw-r--   0 travis    (2000) travis    (2000)    39138 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/short-logo-vector.svg
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9306 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/logo-long.png
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1150 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/static/images/favicon.ico
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/view/templates/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      415 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/section.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2461 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/page_action_card.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2678 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/edit_expectations_instructions_modal.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      318 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/value_list.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)       63 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/string_template.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      593 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/js_script_imports.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1684 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/header.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2839 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/collapse.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      927 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/component.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1912 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/top_navbar.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1689 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/index_page.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      885 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/ge_info.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      939 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/text.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1036 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/cta_footer.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      712 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/graph.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      503 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/content_block_container.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)       49 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/markdown.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      667 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/favicon.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      512 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/sidebar.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1940 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/page.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1440 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/table_of_contents.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)      875 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/bullet_list.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16460 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/carousel_modal.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1464 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/table.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2024 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/templates/content_block_header.j2
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12321 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/view.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      138 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/view/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       48 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/renderer/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27966 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/column_section_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12335 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/other_section_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27520 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/page_renderer.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4846 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/profiling_overview_table_content_block.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      628 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/bullet_list_content_block.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2654 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/exception_list_content_block.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11512 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/content_block.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    65166 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/expectation_string.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    15884 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/validation_results_table_content_block.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      476 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/content_block/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14326 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/site_index_page_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27916 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/site_builder.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1843 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/call_to_action_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4935 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/renderer.py
+-rwxrwxr-x   0 travis    (2000) travis    (2000)     9828 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/notebook_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      553 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3826 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/render/renderer/slack_renderer.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/data_asset/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7155 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_asset/util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27791 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_asset/file_data_asset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10206 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_asset/evaluation_parameters.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       76 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_asset/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    52769 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_asset/data_asset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      497 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/_version.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/init_notebooks/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/init_notebooks/sql/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7741 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/init_notebooks/sql/validation_playground.ipynb
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/init_notebooks/spark/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7597 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/init_notebooks/spark/validation_playground.ipynb
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/init_notebooks/pandas/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7459 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/init_notebooks/pandas/validation_playground.ipynb
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/datasource/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1162 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/util.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/datasource/generator/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8669 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/table_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12507 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/s3_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9363 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/subdir_reader_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4813 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/query_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4760 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/manual_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1755 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/databricks_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8230 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/batch_kwargs_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      432 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9334 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/generator/glob_reader_generator.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/datasource/types/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/types/reader_methods.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5436 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/types/batch_kwargs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       28 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/types/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8462 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/sparkdf_datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9206 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/sqlalchemy_datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11799 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/pandas_datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12009 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      189 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/datasource/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/profile/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11273 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/profile/basic_dataset_profiler.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1316 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/profile/columns_exist.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13393 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/profile/sample_expectations_dataset_profiler.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8335 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/profile/multi_batch_validation_meta_analysis.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      569 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/profile/metrics_utils.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2856 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/profile/base.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      105 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/profile/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8474 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/exceptions.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/data_context/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8478 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5544 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/templates.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/data_context/types/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7839 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/types/resource_identifiers.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        9 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/types/base_resource_identifiers.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8046 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/types/base.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/types/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/data_context/store/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2200 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/expectations_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11205 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/html_site_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2375 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/validations_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3241 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3072 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/store_backend.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2552 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/database_store_backend.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3123 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/metric_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1228 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    19548 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/store/tuple_store_backend.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    75570 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/data_context.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      118 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/data_context/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/expectation_suite.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/validation_operators/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      902 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/validation_operators/util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21526 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/validation_operators/validation_operators.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10360 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/validation_operators/actions.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      808 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/validation_operators/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/cli/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3013 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/init_messages.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1753 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5683 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/init.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1443 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/project.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2316 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/docs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1821 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/cli.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9120 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/suite.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9094 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/validation_operator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1158 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/tap_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    57063 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/datasource.py
+-rwxrwxr-x   0 travis    (2000) travis    (2000)       27 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2881 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/tap.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      732 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/cli/cli_logging.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/core/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      611 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/core/util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      721 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/core/id_dict.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6845 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/core/metric.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1041 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/core/data_context_key.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    46548 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/core/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      891 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/core/batch.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      313 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations/jupyter_ux/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    75137 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/jupyter_ux/expectation_explorer.py
+-rwxrwxr-x   0 travis    (2000) travis    (2000)    12872 2020-04-07 22:32:58.000000 great_expectations-0.9.9/great_expectations/jupyter_ux/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      278 2020-04-07 22:35:27.000000 great_expectations-0.9.9/setup.cfg
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11357 2020-04-07 22:32:57.000000 great_expectations-0.9.9/LICENSE
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1136 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       34 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations.egg-info/top_level.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24829 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      463 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       68 2020-04-07 22:35:27.000000 great_expectations-0.9.9/great_expectations.egg-info/entry_points.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1959 2020-04-07 22:32:58.000000 great_expectations-0.9.9/setup.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_plugins/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1113 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_plugins/fake_configs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      185 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_plugins/fake_actions.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_plugins/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/dataset/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1837 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/test_dataset_legacy.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    37358 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/test_dataset_util_legacy.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      304 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/test_dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1935 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/test_util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      669 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/test_sparkdfdataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8308 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/test_sqlalchemydataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    23909 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/dataset/test_pandas_dataset.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_dataset_implementations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5479 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_dataset_implementations/test_dataset_implementations.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_dataset_implementations/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13303 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_dataset_implementations/test_dataset_implementations.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/render/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13617 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_data_documentation_site_builder.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/render/fixtures/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11751 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/fixtures/SampleExpectationsDatasetProfiler_evrs.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    49037 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_evrs_with_exception.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    51876 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_evrs.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9982 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_expectations.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10064 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_expectations_with_distribution.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3767 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_styled_string_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    15205 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_render.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    25664 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_render_ValidationResultsTableContentBlockRenderer.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/render/output/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/output/.gitkeep
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3314 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_render_BulletListContentBlock.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3777 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    17844 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_page_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    19923 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_default_jinja_view.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1864 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2700 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_SlackRenderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4054 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_render_ExceptionListContentBlockRenderer.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/render/renderer/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/render/renderer/content_block/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1513 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/renderer/content_block/test_expectation_string_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/renderer/content_block/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/renderer/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    69395 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/renderer/test_notebook_renderer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    49257 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/render/test_column_section_renderer.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_asset/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18695 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_expectation_decorators.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8726 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_filedata_asset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13178 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_filedata_asset_expectations.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3349 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_data_asset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33489 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_data_asset_internals.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      518 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_data_asset_citations.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6367 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_parameter_substitution.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5196 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_asset/test_data_asset_util.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20654 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_great_expectations.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/datasource/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/datasource/generator/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6018 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/test_subdir_reader_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6494 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/test_s3_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1867 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/test_manual_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      362 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/test_batch_kwargs_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4852 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/test_table_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3191 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/test_query_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10149 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/generator/test_glob_reader_generator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      191 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/test_sqlalchemy_datasource_workarounds.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2306 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/test_batch_kwargs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10302 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/test_sqlalchemy_datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12936 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/test_sparkdf_datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6593 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/test_batch_generators.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      682 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/conftest.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13153 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/datasource/test_pandas_datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6111 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_configs.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_sets/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       80 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/toy_data_incomplete.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8704 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/test_partitions.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      126 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/invalid_json_file.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/null_file.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)    76128 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_base.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)    94208 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/titanic.db
+-rw-rw-r--   0 travis    (2000) travis    (2000)       68 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/same_column_names.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)       23 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/unicode.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)   101861 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/Titanic_multi_sheet.xlsx
+-rw-rw-r--   0 travis    (2000) travis    (2000)      100 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/toy_data_complete.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)    70366 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/Titanic.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1351 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/test_json_data_file.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    95990 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/Titanic.pkl
+-rw-rw-r--   0 travis    (2000) travis    (2000)    51876 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/expected_evrs_BasicDatasetProfiler_on_titanic.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)       62 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/strf_test.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1688 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/nested_test_json_data_file.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11751 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/expected_evrs_SampleExpectationsDatasetProfiler_on_titanic.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2202 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/expected_cli_results_custom.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6275 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/expected_cli_results_default.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)       11 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/white_space.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)    76045 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_test.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4934 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/titanic_expected_data_asset_validate_results.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    65691 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/fixed_distributional_test_dataset.csv
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1557 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/titanic_expectations.json
+-rwxrwxr-x   0 travis    (2000) travis    (2000)     3688 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/broken_excel_file.xls
+-rw-rw-r--   0 travis    (2000) travis    (2000)       34 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/json_test2_against_schema.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34948 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/Titanic.parquet
+-rw-rw-r--   0 travis    (2000) travis    (2000)      195 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/test_partition_serialized_infinity_bins.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      115 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/sample_schema.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)       38 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/json_test1_against_schema.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7705 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/titanic_expected_data_asset_validate_results_with_exceptions.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    85069 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_base.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1660 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/titanic_parameterized_expectations.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)   141917 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/fixed_distributional_test_dataset.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)       35 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/titanic_evaluation_parameters.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      246 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/titanic_custom_expectations.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    85178 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_test.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12279 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_sets/test_partitions_definition_fixture.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_definitions/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4204 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_median_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1834 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_proportion_of_unique_values_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5740 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_mean_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4350 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_min_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2933 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_contain_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5304 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_be_in_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2948 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_equal_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3530 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_stdev_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3127 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_sum_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    83561 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_quantile_values_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1824 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_unique_value_count_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3044 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_most_common_value_to_be_in_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4115 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_max_to_be_between.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_definitions/multicolumn_map_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3086 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/multicolumn_map_expectations/expect_multicolumn_values_to_be_unique.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4764 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3267 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_null.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1465 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_json_schema.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2657 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex_list.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3997 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_strftime_format.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3689 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3992 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4811 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2818 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_null.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13126 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_of_type.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2249 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_equal.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1709 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex_list.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2460 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_decreasing.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12797 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2433 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_increasing.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8702 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_type_list.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3623 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_in_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3411 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_unique.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_definitions/column_pair_map_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3454 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_equal.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2012 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_in_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2386 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_A_to_be_greater_than_B.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1641 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_columns_to_match_ordered_list_test_set.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1899 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_row_count_to_equal.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2327 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_column_count_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      533 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_this_test_to_be_suppressed.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1110 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_column_to_exist.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2261 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_row_count_to_be_between.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2020 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_column_count_to_equal.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7014 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/test_expectations.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    57692 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)   105938 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/test_expect_column_bootstrapped_ks_test_p_value_to_be_greater_than.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10564 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/expect_column_chisquare_test_p_value_to_be_greater_than.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)   126107 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/expect_column_kl_divergence_to_be_less_than.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/profile/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2940 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/profile/test_multi_batch_validation_meta_analysis.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    17402 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/profile/test_SampleExpectationsDatasetProfiler.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    17932 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/profile/test_profile.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/profile/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1633 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_autoinspect.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      632 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/build_index_page.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/contexts/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5155 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/uncommitted/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      991 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/uncommitted/config_variables.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)       90 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/.gitignore
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/invalid_config_version/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      970 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/invalid_config_version/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1836 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/cluster-paintings.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      191 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)    66315 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/elements-by-episode.csv
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2413 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/index.html
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/bob-ross/
+-rw-rw-r--   0 travis    (2000) travis    (2000)   146908 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/bob-ross/
+-rw-rw-r--   0 travis    (2000) travis    (2000)   360054 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.html
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/index.html
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/bob-ross/
+-rw-rw-r--   0 travis    (2000) travis    (2000)   146908 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/bob-ross/
+-rw-rw-r--   0 travis    (2000) travis    (2000)   233898 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)       12 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/.gitignore
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/sql/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/sql/create_expectations.ipynb
+-rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/sql/validation_playground.ipynb
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/spark/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/spark/create_expectations.ipynb
+-rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/spark/validation_playground.ipynb
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/pandas/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/pandas/create_expectations.ipynb
+-rw-rw-r--   0 travis    (2000) travis    (2000)       42 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/notebooks/pandas/validation_playground.ipynb
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    97613 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/warning.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    97626 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      684 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/quarantine.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      684 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/failure.json
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/bad_yml/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       57 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/bad_yml/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/invalid_top_level_key/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      547 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/invalid_top_level_key/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/invalid_top_level_value_type/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      281 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/invalid_top_level_value_type/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/old_config_version/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1022 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/old_config_version/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/version_zero/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2476 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/version_zero/great_expectations.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/fixtures/missing_top_level_key/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      217 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/fixtures/missing_top_level_key/great_expectations.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4568 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_configuration_storage.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2190 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_data_context_resource_identifiers.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2788 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_data_context_config_errors.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41732 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_data_context.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1134 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_data_context_utils.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/data_context/store/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4359 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/store/test_html_site_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6635 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/store/test_validations_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8697 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/store/test_store_backends.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6622 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/store/test_evaluation_parameter_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2039 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/store/test_expectations_store.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/store/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3195 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_data_context_store_configs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      931 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_data_context_on_teams.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5017 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/test_data_context_config_variables.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3641 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/data_context/conftest.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/cli/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    38336 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_suite.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3359 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_docs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1981 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_project.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22534 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_init_pandas.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14055 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_datasource_pandas.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3016 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/utils.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18676 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_datasource_sqlite.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5061 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_cli.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8758 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_validation_operator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6306 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_init_missing_libraries.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9661 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_taps_pandas.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      118 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    19249 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_init_sqlite.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7804 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/cli/test_init.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6207 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_ge_utils.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/core/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7988 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/core/test_expectation_suite_crud_methods.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1098 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/core/test_serialization.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9779 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/core/test_expectation_suite.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3820 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/core/test_evaluation_parameters.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2938 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/core/test_expectation_configuration.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/core/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1207 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/core/test_expectation_kwargs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    64653 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/conftest.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_fixtures/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2040 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/great_expectations_basic_without_config_variables_filepath.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3520 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/distributional_expectations_partition_fixtures.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       20 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/config_variables.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2468 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/great_expectations_basic.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/dummy.sql
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1026 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/custom_pandas_dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      695 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/custom_sqlalchemy_dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1747 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/custom_sparkdf_dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2797 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/fixed_distribution_data.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13931 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/expectation_suite_3.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    48940 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/evr_suite_3.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)    52125 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/expectations_suite_2.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      924 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/expectations_suite_1.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2556 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/evr_suite_1.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5482 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/great_expectations_site_builder.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/test_fixtures/expectation_suites/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      791 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/expectation_suites/parameterized_expression_expectation_suite_fixture.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      890 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/expectation_suites/parameterized_expectation_suite_fixture.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2186 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/great_expectations_basic_with_variables.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2009 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_fixtures/great_expectations_titanic.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27757 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/test_utils.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/actions/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6263 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/actions/test_validation_operators_in_data_context.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5396 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/actions/test_core_actions.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/actions/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2952 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/actions/conftest.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5212 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/actions/test_store_metric_action.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7255 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/actions/test_validation_operators.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-04-07 22:35:27.000000 great_expectations-0.9.9/tests/jupyter_ux/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5857 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/jupyter_ux/test_jupyter_ux.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-04-07 22:32:58.000000 great_expectations-0.9.9/tests/jupyter_ux/__init__.py
```

### Comparing `great_expectations-0.9.8/examples/integrations/airflow/hooks/s3_csv_hook.py` & `great_expectations-0.9.9/examples/integrations/airflow/hooks/s3_csv_hook.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/examples/integrations/airflow/hooks/db_hook.py` & `great_expectations-0.9.9/examples/integrations/airflow/hooks/db_hook.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/examples/integrations/airflow/operators/expectation_operator.py` & `great_expectations-0.9.9/examples/integrations/airflow/operators/expectation_operator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/versioneer.py` & `great_expectations-0.9.9/versioneer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/PKG-INFO` & `great_expectations-0.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: great_expectations
-Version: 0.9.8
+Version: 0.9.9
 Summary: Always know what to expect from your data.
 Home-page: https://github.com/great-expectations/great_expectations
 Author: The Great Expectations Team
 Author-email: team@greatexpectations.io
 License: Apache-2.0
 Description: Always know what to expect from your data. (See https://github.com/great-expectations/great_expectations for full description).
 Keywords: data science testing pipeline data quality dataquality validation datavalidation
```

### Comparing `great_expectations-0.9.8/README.md` & `great_expectations-0.9.9/README.md`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/requirements-dev.txt` & `great_expectations-0.9.9/requirements-dev.txt`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/util.py` & `great_expectations-0.9.9/great_expectations/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/dataset/util.py` & `great_expectations-0.9.9/great_expectations/dataset/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/dataset/pandas_dataset.py` & `great_expectations-0.9.9/great_expectations/dataset/pandas_dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/dataset/sqlalchemy_dataset.py` & `great_expectations-0.9.9/great_expectations/dataset/sqlalchemy_dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/dataset/sparkdf_dataset.py` & `great_expectations-0.9.9/great_expectations/dataset/sparkdf_dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/dataset/dataset.py` & `great_expectations-0.9.9/great_expectations/dataset/dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/dataset/__init__.py` & `great_expectations-0.9.9/great_expectations/dataset/__init__.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/validator/validator.py` & `great_expectations-0.9.9/great_expectations/validator/validator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/types/expectations.py` & `great_expectations-0.9.9/great_expectations/types/expectations.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/types/configurations.py` & `great_expectations-0.9.9/great_expectations/types/configurations.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/types/base.py` & `great_expectations-0.9.9/great_expectations/types/base.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/types/__init__.py` & `great_expectations-0.9.9/great_expectations/types/__init__.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/util.py` & `great_expectations-0.9.9/great_expectations/render/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/types/__init__.py` & `great_expectations-0.9.9/great_expectations/render/types/__init__.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/styles/data_docs_custom_styles_template.css` & `great_expectations-0.9.9/great_expectations/render/view/static/styles/data_docs_custom_styles_template.css`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/styles/data_docs_default_styles.css` & `great_expectations-0.9.9/great_expectations/render/view/static/styles/data_docs_default_styles.css`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-MediumItalic.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-MediumItalic.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Italic.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Italic.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Bold.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Bold.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-LightItalic.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-LightItalic.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Light.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Light.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBoldItalic.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBoldItalic.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Medium.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Medium.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-BoldItalic.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-BoldItalic.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBold.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-SemiBold.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Regular.otf` & `great_expectations-0.9.9/great_expectations/render/view/static/fonts/HKGrotesk/HKGrotesk-Regular.otf`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/logo-long-vector.svg` & `great_expectations-0.9.9/great_expectations/render/view/static/images/logo-long-vector.svg`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/iterative-dev-loop.png` & `great_expectations-0.9.9/great_expectations/render/view/static/images/iterative-dev-loop.png`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/glossary_scroller.gif` & `great_expectations-0.9.9/great_expectations/render/view/static/images/glossary_scroller.gif`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/validation_failed_unexpected_values.gif` & `great_expectations-0.9.9/great_expectations/render/view/static/images/validation_failed_unexpected_values.gif`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/short-logo.png` & `great_expectations-0.9.9/great_expectations/render/view/static/images/short-logo.png`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/short-logo-vector.svg` & `great_expectations-0.9.9/great_expectations/render/view/static/images/short-logo-vector.svg`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/logo-long.png` & `great_expectations-0.9.9/great_expectations/render/view/static/images/logo-long.png`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/static/images/favicon.ico` & `great_expectations-0.9.9/great_expectations/render/view/static/images/favicon.ico`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/page_action_card.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/page_action_card.j2`

 * *Files 8% similar despite different names*

```diff
@@ -38,27 +38,28 @@
             <label class="btn btn-primary" onclick="hideSucceededValidations()">
               <input type="radio" name="options" id="option2" autocomplete="off"> Failed Only
             </label>
           </div>
         </div>
       </div>
     {% endif %}
+    {% if show_how_to_buttons | default(True) %}
+      {% if renderer_type in ["ValidationResultsPageRenderer", "ExpectationSuitePageRenderer"] %}
+        <div class="mb-2">
+          <div class="d-flex justify-content-center">
+            <button type="button" class="btn btn-warning" data-toggle="modal" data-target=".ge-expectation-editing-instructions-modal">
+              <i class="fas fa-edit"></i> How to Edit This Suite
+            </button>
+          </div>
+        </div>
+      {% endif %}
 
-    {% if renderer_type in ["ValidationResultsPageRenderer", "ExpectationSuitePageRenderer"] %}
       <div class="mb-2">
         <div class="d-flex justify-content-center">
-          <button type="button" class="btn btn-warning" data-toggle="modal" data-target=".ge-expectation-editing-instructions-modal">
-            <i class="fas fa-edit"></i> How to Edit This Suite
+          <button type="button" class="btn btn-info" data-toggle="modal" data-target=".ge-walkthrough-modal">
+            Show Walkthrough
           </button>
         </div>
       </div>
     {% endif %}
-
-    <div class="mb-2">
-      <div class="d-flex justify-content-center">
-        <button type="button" class="btn btn-info" data-toggle="modal" data-target=".ge-walkthrough-modal">
-          Show Walkthrough
-        </button>
-      </div>
-    </div>
   </div>
 </div>
```

#### html2text {}

```diff
@@ -1,10 +1,11 @@
 Actions
 {% if renderer_type in ["ValidationResultsPageRenderer",
 "SiteIndexPageRenderer"] %}
 Validation Filter:
  # Show All   o Failed Only
-{% endif %} {% if renderer_type in ["ValidationResultsPageRenderer",
-"ExpectationSuitePageRenderer"] %}
+{% endif %} {% if show_how_to_buttons | default(True) %} {% if renderer_type in
+["ValidationResultsPageRenderer", "ExpectationSuitePageRenderer"] %}
   How to Edit This Suite
 {% endif %}
  Show Walkthrough
+{% endif %}
```

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/edit_expectations_instructions_modal.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/edit_expectations_instructions_modal.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/js_script_imports.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/js_script_imports.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/header.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/header.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/collapse.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/collapse.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/component.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/component.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/top_navbar.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/top_navbar.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/index_page.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/index_page.j2`

 * *Files 7% similar despite different names*

```diff
@@ -19,27 +19,30 @@
   </head>
 
   <body
           data-spy="scroll"
           data-target="#navigation"
           data-offset="50"
   >
-    {% include 'carousel_modal.j2' %}
 
-    <script>
-      try {
-        if (localStorage.getItem('ge-walkthrough-modal-dismissed') !== 'true') {
+    {% if show_how_to_buttons | default(True) %}
+      {% include 'carousel_modal.j2' %}
+
+      <script>
+        try {
+          if (localStorage.getItem('ge-walkthrough-modal-dismissed') !== 'true') {
+            $(".ge-walkthrough-modal").modal();
+          }
+        }
+        catch(error) {
           $(".ge-walkthrough-modal").modal();
+          console.log(error);
         }
-      }
-      catch(error) {
-        $(".ge-walkthrough-modal").modal();
-        console.log(error);
-      }
-    </script>
+      </script>
+    {% endif %}
 
     {% include 'top_navbar.j2' %}
     <div class="container-fluid pt-4 pb-4 pl-5 pr-5">
       <div class="row">
         {% include 'sidebar.j2' %}
         <div class="col-md-10 col-lg-10 col-xs-12 pl-md-4 pr-md-3">
           {% for section in sections %}
```

#### html2text {}

```diff
@@ -1,10 +1,10 @@
 
 {# {# Remove this when not debugging: #} {#
  #}
  {% include 'js_script_imports.j2' %} {% include 'favicon.j2' %}
-{% include 'carousel_modal.j2' %}
- {% include 'top_navbar.j2' %}
+{% if show_how_to_buttons | default(True) %} {% include 'carousel_modal.j2' %}
+ {% endif %} {% include 'top_navbar.j2' %}
 {% include 'sidebar.j2' %}
 {% for section in sections %} {% set section_loop = loop -%} {% include
 'section.j2' %} {% endfor %}
 {% if cta_footer %} {% include 'cta_footer.j2' %} {% endif %}
```

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/ge_info.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/ge_info.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/text.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/text.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/cta_footer.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/cta_footer.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/graph.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/graph.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/favicon.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/favicon.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/table_of_contents.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/table_of_contents.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/bullet_list.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/bullet_list.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/carousel_modal.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/carousel_modal.j2`

 * *Files 0% similar despite different names*

```diff
@@ -216,15 +216,15 @@
 
                 <div class="card walkthrough-card bg-dark text-white walkthrough-5">
                 <div class="card-header"><h4>Validation results save you time.</h4></div>
                 <div class="card-body">
                   <div class="image-sizer text-center">
                       <img src="{{ static_images_dir + "validation_failed_unexpected_values.gif" }}" class="img-fluid rounded-sm mx-auto">
                   </div>
-                  <p>This is an example of what a single failed Expectation looks like in Data Docs. Note the failure includes unexpected values from your data. This helps you debug pipeines faster.</p>
+                  <p>This is an example of what a single failed Expectation looks like in Data Docs. Note the failure includes unexpected values from your data. This helps you debug pipelines faster.</p>
                 </div>
                 <div class="card-footer walkthrough-links">
                   <div class="container">
                     <div class="row">
                       <div class="col-sm">
                         <a href="#" class="next-link btn btn-secondary float-left" onclick="go_to_slide(4)">Back</a>
                       </div>
@@ -324,8 +324,8 @@
     $('.walkthrough-' + slide_number).show();
   }
   function hide_cards() {
     $('.walkthrough-card').hide();
   }
   hide_cards();
   go_to_slide(1);
-</script>
+</script>
```

#### html2text {}

```diff
@@ -71,15 +71,15 @@
 Back
 4 of 7
 Next
 *** Validation results save you time. ***
 gif" }}" class="img-fluid rounded-sm mx-auto">
 This is an example of what a single failed Expectation looks like in Data Docs.
 Note the failure includes unexpected values from your data. This helps you
-debug pipeines faster.
+debug pipelines faster.
 Back
 5 of 7
 Next
 *** Great Expectations provides a large library of expectations. ***
 gif" }}" class="img-fluid rounded-sm mx-auto">
 Nearly_50_built_in_expectations allow you to express how you understand your
 data, and you can add custom expectations if you need a new one.
@@ -91,7 +91,8 @@
 Note this is not a production suite and was generated using only a small sample
 of your data.
 When you are ready, press the How to Edit button to kick off the iterative dev
 loop.
 Back
 7 of 7
  Done
+
```

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/table.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/table.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/templates/content_block_header.j2` & `great_expectations-0.9.9/great_expectations/render/view/templates/content_block_header.j2`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/view/view.py` & `great_expectations-0.9.9/great_expectations/render/view/view.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/column_section_renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/column_section_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/other_section_renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/other_section_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/page_renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/page_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/content_block/profiling_overview_table_content_block.py` & `great_expectations-0.9.9/great_expectations/render/renderer/content_block/profiling_overview_table_content_block.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/content_block/bullet_list_content_block.py` & `great_expectations-0.9.9/great_expectations/render/renderer/content_block/bullet_list_content_block.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/content_block/exception_list_content_block.py` & `great_expectations-0.9.9/great_expectations/render/renderer/content_block/exception_list_content_block.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/content_block/content_block.py` & `great_expectations-0.9.9/great_expectations/render/renderer/content_block/content_block.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/content_block/expectation_string.py` & `great_expectations-0.9.9/great_expectations/render/renderer/content_block/expectation_string.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/content_block/validation_results_table_content_block.py` & `great_expectations-0.9.9/great_expectations/render/renderer/content_block/validation_results_table_content_block.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/site_index_page_renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/site_index_page_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/site_builder.py` & `great_expectations-0.9.9/great_expectations/render/renderer/site_builder.py`

 * *Files 6% similar despite different names*

```diff
@@ -92,20 +92,22 @@
     """
 
     def __init__(self,
                  data_context,
                  store_backend,
                  site_name=None,
                  site_index_builder=None,
+                 show_how_to_buttons=True,
                  site_section_builders=None,
                  runtime_environment=None
                  ):
         self.site_name = site_name
         self.data_context = data_context
         self.store_backend = store_backend
+        self.show_how_to_buttons = show_how_to_buttons
 
         # set custom_styles_directory if present
         custom_styles_directory = None
         plugins_directory = data_context.plugins_directory
         if plugins_directory and os.path.isdir(os.path.join(plugins_directory, "custom_data_docs", "styles")):
             custom_styles_directory = os.path.join(plugins_directory, "custom_data_docs", "styles")
 
@@ -124,14 +126,15 @@
         module_name = site_index_builder.get('module_name') or 'great_expectations.render.renderer.site_builder'
         class_name = site_index_builder.get('class_name') or 'DefaultSiteIndexBuilder'
         self.site_index_builder = instantiate_class_from_config(
             config=site_index_builder,
             runtime_environment={
                 "data_context": data_context,
                 "custom_styles_directory": custom_styles_directory,
+                "show_how_to_buttons": self.show_how_to_buttons,
                 "target_store": self.target_store,
                 "site_name": self.site_name
             },
             config_defaults={
                 "name": "site_index_builder",
                 "module_name": module_name,
                 "class_name": class_name
@@ -179,15 +182,16 @@
         for site_section_name, site_section_config in site_section_builders.items():
             module_name = site_section_config.get('module_name') or 'great_expectations.render.renderer.site_builder'
             self.site_section_builders[site_section_name] = instantiate_class_from_config(
                 config=site_section_config,
                 runtime_environment={
                     "data_context": data_context,
                     "target_store": self.target_store,
-                    "custom_styles_directory": custom_styles_directory
+                    "custom_styles_directory": custom_styles_directory,
+                    "show_how_to_buttons": self.show_how_to_buttons,
                 },
                 config_defaults={
                     "name": site_section_name,
                     "module_name": module_name
                 }
             )
             if not self.site_section_builders[site_section_name]:
@@ -236,24 +240,26 @@
     def __init__(
             self,
             name,
             data_context,
             target_store,
             source_store_name,
             custom_styles_directory=None,
+            show_how_to_buttons=True,
             run_id_filter=None,
             validation_results_limit=None,
             renderer=None,
             view=None,
     ):
         self.name = name
         self.source_store = data_context.stores[source_store_name]
         self.target_store = target_store
         self.run_id_filter = run_id_filter
         self.validation_results_limit = validation_results_limit
+        self.show_how_to_buttons = show_how_to_buttons
 
         if renderer is None:
             raise exceptions.InvalidConfigError(
                 "SiteSectionBuilder requires a renderer configuration with a class_name key."
             )
         module_name = renderer.get('module_name') or 'great_expectations.render.renderer'
         self.renderer_class = instantiate_class_from_config(
@@ -331,15 +337,18 @@
                             expectation_suite_name,
                             resource_key.batch_identifier
                         )
                     )
 
             try:
                 rendered_content = self.renderer_class.render(resource)
-                viewable_content = self.view_class.render(rendered_content)
+                viewable_content = self.view_class.render(
+                    rendered_content,
+                    show_how_to_buttons=self.show_how_to_buttons
+                )
             except Exception as e:
                 exception_message = f'''\
 An unexpected Exception occurred during data docs rendering.  Because of this error, certain parts of data docs will \
 not be rendered properly and/or may not appear altogether.  Please use the trace, included in this message, to \
 diagnose and repair the underlying issue.  Detailed information follows:  
                 '''
                 exception_traceback = traceback.format_exc()
@@ -372,26 +381,26 @@
     def __init__(
             self,
             name,
             site_name,
             data_context,
             target_store,
             custom_styles_directory=None,
-            show_cta_footer=True,
+            show_how_to_buttons=True,
             validation_results_limit=None,
             renderer=None,
             view=None,
     ):
         # NOTE: This method is almost identical to DefaultSiteSectionBuilder
         self.name = name
         self.site_name = site_name
         self.data_context = data_context
         self.target_store = target_store
-        self.show_cta_footer = show_cta_footer
         self.validation_results_limit = validation_results_limit
+        self.show_how_to_buttons = show_how_to_buttons
 
         if renderer is None:
             renderer = {
                 "module_name": "great_expectations.render.renderer",
                 "class_name": "SiteIndexPageRenderer",
             }
         module_name = renderer.get('module_name') or 'great_expectations.render.renderer'
@@ -570,15 +579,15 @@
         validation_result_keys = sorted(validation_result_keys, key=lambda x: x.run_id, reverse=True)
         if self.validation_results_limit:
             validation_result_keys = validation_result_keys[:self.validation_results_limit]
 
         index_links_dict = OrderedDict()
         index_links_dict["site_name"] = self.site_name
 
-        if self.show_cta_footer:
+        if self.show_how_to_buttons:
             index_links_dict["cta_object"] = self.get_calls_to_action()
 
         for expectation_suite_key in expectation_suite_keys:
             self.add_resource_info_to_index_links_dict(
                 index_links_dict=index_links_dict,
                 expectation_suite_name=expectation_suite_key.expectation_suite_name,
                 section_name="expectations"
@@ -626,15 +635,18 @@
                 )
             except Exception as e:
                 error_msg = "Validation result not found: {0:s} - skipping".format(str(validation_result_key.to_tuple()))
                 logger.warning(error_msg)
 
         try:
             rendered_content = self.renderer_class.render(index_links_dict)
-            viewable_content = self.view_class.render(rendered_content)
+            viewable_content = self.view_class.render(
+                rendered_content,
+                show_how_to_buttons=self.show_how_to_buttons
+            )
         except Exception as e:
             exception_message = f'''\
 An unexpected Exception occurred during data docs rendering.  Because of this error, certain parts of data docs will \
 not be rendered properly and/or may not appear altogether.  Please use the trace, included in this message, to \
 diagnose and repair the underlying issue.  Detailed information follows:  
             '''
             exception_traceback = traceback.format_exc()
```

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/call_to_action_renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/call_to_action_renderer.py`

 * *Files 4% similar despite different names*

```diff
@@ -17,46 +17,46 @@
             ],
             "attributes": {
                 "id": "ge-cta-footer",
                 "role": "alert"
             }
         }
     }
-    
+
     @classmethod
     def render(cls, cta_object):
         """
         :param cta_object: dict
             {
                 "header": # optional, can be a string or string template
                 "buttons": # list of CallToActionButtons
             }
         :return: dict
             {
                 "header": # optional, can be a string or string template
                 "buttons": # list of CallToActionButtons
             }
         """
-        
+
         if not cta_object.get("header"):
             cta_object["header"] = cls._document_defaults.get("header")
-        
+
         cta_object["styling"] = cls._document_defaults.get("styling")
         cta_object["tooltip_icon"] = {
             "template": "$icon",
             "params": {
                 "icon": ""
             },
             "tooltip": {
-                "content": "To disable this footer, set the show_cta_footer flag in your project config to false."
+                "content": "To disable this footer, set the show_how_to_buttons flag in your project's data_docs_sites config to false."
             },
             "styling": {
                 "params": {
                     "icon": {
                         "tag": "i",
                         "classes": ["m-1", "fas", "fa-question-circle"],
                     }
                 }
             }
         }
-        
+
         return cta_object
```

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/notebook_renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/notebook_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/__init__.py` & `great_expectations-0.9.9/great_expectations/render/renderer/__init__.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/render/renderer/slack_renderer.py` & `great_expectations-0.9.9/great_expectations/render/renderer/slack_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_asset/util.py` & `great_expectations-0.9.9/great_expectations/data_asset/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_asset/file_data_asset.py` & `great_expectations-0.9.9/great_expectations/data_asset/file_data_asset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_asset/evaluation_parameters.py` & `great_expectations-0.9.9/great_expectations/data_asset/evaluation_parameters.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_asset/data_asset.py` & `great_expectations-0.9.9/great_expectations/data_asset/data_asset.py`

 * *Files 4% similar despite different names*

```diff
@@ -334,15 +334,25 @@
         self._expectation_suite.data_asset_type = self._data_asset_type
         self.default_expectation_args = {
             "include_config": True,
             "catch_exceptions": False,
             "result_format": 'BASIC',
         }
 
+    def append_expectation(self, expectation_config):
+        """This method is a thin wrapper for ExpectationSuite.append_expectation"""
+        self._expectation_suite.append_expectation(expectation_config)
+
     def _append_expectation(self, expectation_config):
+        """This method
+        
+        This method should become a thin wrapper for ExpectationSuite.append_expectation
+
+        Included for backwards compatibility.
+        """
         """Appends an expectation to `DataAsset._expectation_suite` and drops existing expectations of the same type.
 
            If `expectation_config` is a column expectation, this drops existing expectations that are specific to \
            that column and only if it is the same expectation type as `expectation_config`. Otherwise, if it's not a \
            column expectation, this drops existing expectations of the same type as `expectation config`. \
            After expectations of the same type are dropped, `expectation_config` is appended to \
            `DataAsset._expectation_suite`.
@@ -380,247 +390,91 @@
             )]
         else:
             self._expectation_suite.expectations = [f for f in filter(
                 lambda exp: exp.expectation_type != expectation_type,
                 self._expectation_suite.expectations
             )]
 
-        self._expectation_suite.expectations.append(expectation_config)
+        self._expectation_suite.append_expectation(expectation_config)
 
     def _copy_and_clean_up_expectation(self,
-                                       expectation,
-                                       discard_result_format_kwargs=True,
-                                       discard_include_config_kwargs=True,
-                                       discard_catch_exceptions_kwargs=True,
-                                       ):
-        """Returns copy of `expectation` without `success_on_last_run` and other specified key-value pairs removed
-
-          Returns a copy of specified expectation will not have `success_on_last_run` key-value. The other key-value \
-          pairs will be removed by default but will remain in the copy if specified.
-
-          Args:
-              expectation (json): \
-                  The expectation to copy and clean.
-              discard_result_format_kwargs (boolean): \
-                  if True, will remove the kwarg `output_format` key-value pair from the copied expectation.
-              discard_include_config_kwargs (boolean):
-                  if True, will remove the kwarg `include_config` key-value pair from the copied expectation.
-              discard_catch_exceptions_kwargs (boolean):
-                  if True, will remove the kwarg `catch_exceptions` key-value pair from the copied expectation.
-
-          Returns:
-              A copy of the provided expectation with `success_on_last_run` and other specified key-value pairs removed
-        """
-        new_expectation = copy.deepcopy(expectation)
-
-        if "success_on_last_run" in new_expectation:
-            del new_expectation["success_on_last_run"]
-
-        if discard_result_format_kwargs:
-            if "result_format" in new_expectation.kwargs:
-                del new_expectation.kwargs["result_format"]
-                # discards["result_format"] += 1
-
-        if discard_include_config_kwargs:
-            if "include_config" in new_expectation.kwargs:
-                del new_expectation.kwargs["include_config"]
-                # discards["include_config"] += 1
-
-        if discard_catch_exceptions_kwargs:
-            if "catch_exceptions" in new_expectation.kwargs:
-                del new_expectation.kwargs["catch_exceptions"]
-                # discards["catch_exceptions"] += 1
+        expectation,
+        discard_result_format_kwargs=True,
+        discard_include_config_kwargs=True,
+        discard_catch_exceptions_kwargs=True,
+    ):
+        """This method is a thin wrapper for ExpectationSuite._copy_and_clean_up_expectation"""
+        return self._expectation_suite._copy_and_clean_up_expectation(
+            expectation=expectation,
+            discard_result_format_kwargs=discard_result_format_kwargs,
+            discard_include_config_kwargs=discard_include_config_kwargs,
+            discard_catch_exceptions_kwargs=discard_catch_exceptions_kwargs,
+        )
 
-        return new_expectation
 
-    def _copy_and_clean_up_expectations_from_indexes(
-        self,
+    def _copy_and_clean_up_expectations_from_indexes(self,
         match_indexes,
         discard_result_format_kwargs=True,
         discard_include_config_kwargs=True,
         discard_catch_exceptions_kwargs=True,
     ):
-        """Copies and cleans all expectations provided by their index in DataAsset._expectation_suite.expectations.
-
-           Applies the _copy_and_clean_up_expectation method to multiple expectations, provided by their index in \
-           `DataAsset,_expectation_suite.expectations`. Returns a list of the copied and cleaned expectations.
-
-           Args:
-               match_indexes (List): \
-                   Index numbers of the expectations from `expectation_config.expectations` to be copied and cleaned.
-               discard_result_format_kwargs (boolean): \
-                   if True, will remove the kwarg `output_format` key-value pair from the copied expectation.
-               discard_include_config_kwargs (boolean):
-                   if True, will remove the kwarg `include_config` key-value pair from the copied expectation.
-               discard_catch_exceptions_kwargs (boolean):
-                   if True, will remove the kwarg `catch_exceptions` key-value pair from the copied expectation.
-
-           Returns:
-               A list of the copied expectations with `success_on_last_run` and other specified \
-               key-value pairs removed.
-
-           See also:
-               _copy_and_clean_expectation
-        """
-        rval = []
-        for i in match_indexes:
-            rval.append(
-                self._copy_and_clean_up_expectation(
-                    self._expectation_suite.expectations[i],
-                    discard_result_format_kwargs,
-                    discard_include_config_kwargs,
-                    discard_catch_exceptions_kwargs,
-                )
-            )
-
-        return rval
+        """This method is a thin wrapper for ExpectationSuite._copy_and_clean_up_expectations_from_indexes"""
+        return self._expectation_suite._copy_and_clean_up_expectations_from_indexes(
+            match_indexes=match_indexes,
+            discard_result_format_kwargs=discard_result_format_kwargs,
+            discard_include_config_kwargs=discard_include_config_kwargs,
+            discard_catch_exceptions_kwargs=discard_catch_exceptions_kwargs,
+        )
 
     def find_expectation_indexes(self,
-                                 expectation_type=None,
-                                 column=None,
-                                 expectation_kwargs=None
-                                 ):
-        """Find matching expectations within _expectation_config.
-        Args:
-            expectation_type=None                : The name of the expectation type to be matched.
-            column=None                          : The name of the column to be matched.
-            expectation_kwargs=None              : A dictionary of kwargs to match against.
-
-        Returns:
-            A list of indexes for matching expectation objects.
-            If there are no matches, the list will be empty.
-        """
-        if expectation_kwargs is None:
-            expectation_kwargs = {}
-
-        if "column" in expectation_kwargs and column is not None and column is not expectation_kwargs["column"]:
-            raise ValueError("Conflicting column names in remove_expectation: %s and %s" % (
-                column, expectation_kwargs["column"]))
-
-        if column is not None:
-            expectation_kwargs["column"] = column
-
-        match_indexes = []
-        for i, exp in enumerate(self._expectation_suite.expectations):
-            if expectation_type is None or (expectation_type == exp.expectation_type):
-                # if column == None or ('column' not in exp['kwargs']) or
-                # (exp['kwargs']['column'] == column) or (exp['kwargs']['column']==:
-                match = True
-
-                for k, v in expectation_kwargs.items():
-                    if k in exp['kwargs'] and exp['kwargs'][k] == v:
-                        continue
-                    else:
-                        match = False
-
-                if match:
-                    match_indexes.append(i)
-
-        return match_indexes
-
-    def find_expectations(self,
-                          expectation_type=None,
-                          column=None,
-                          expectation_kwargs=None,
-                          discard_result_format_kwargs=True,
-                          discard_include_config_kwargs=True,
-                          discard_catch_exceptions_kwargs=True,
-                          ):
-        """Find matching expectations within _expectation_config.
-        Args:
-            expectation_type=None                : The name of the expectation type to be matched.
-            column=None                          : The name of the column to be matched.
-            expectation_kwargs=None              : A dictionary of kwargs to match against.
-            discard_result_format_kwargs=True    : In returned expectation object(s), \
-            suppress the `result_format` parameter.
-            discard_include_config_kwargs=True  : In returned expectation object(s), \
-            suppress the `include_config` parameter.
-            discard_catch_exceptions_kwargs=True : In returned expectation object(s), \
-            suppress the `catch_exceptions` parameter.
-
-        Returns:
-            A list of matching expectation objects.
-            If there are no matches, the list will be empty.
-        """
-
-        match_indexes = self.find_expectation_indexes(
-            expectation_type,
-            column,
-            expectation_kwargs,
+        expectation_type=None,
+        column=None,
+        expectation_kwargs=None
+    ):
+        """This method is a thin wrapper for ExpectationSuite.find_expectation_indexes"""
+        return self._expectation_suite.find_expectation_indexes(
+            expectation_type=expectation_type,
+            column=column,
+            expectation_kwargs=expectation_kwargs,
         )
 
-        return self._copy_and_clean_up_expectations_from_indexes(
-            match_indexes,
-            discard_result_format_kwargs,
-            discard_include_config_kwargs,
-            discard_catch_exceptions_kwargs,
+    def find_expectations(self,
+        expectation_type=None,
+        column=None,
+        expectation_kwargs=None,
+        discard_result_format_kwargs=True,
+        discard_include_config_kwargs=True,
+        discard_catch_exceptions_kwargs=True,
+    ):
+        """This method is a thin wrapper for ExpectationSuite.find_expectations()"""
+        return self._expectation_suite.find_expectations(
+            expectation_type=expectation_type,
+            column=column,
+            expectation_kwargs=expectation_kwargs,
+            discard_result_format_kwargs=discard_result_format_kwargs,
+            discard_include_config_kwargs=discard_include_config_kwargs,
+            discard_catch_exceptions_kwargs=discard_catch_exceptions_kwargs,
         )
 
     def remove_expectation(self,
                            expectation_type=None,
                            column=None,
                            expectation_kwargs=None,
                            remove_multiple_matches=False,
                            dry_run=False,
                            ):
-        """Remove matching expectation(s) from _expectation_config.
-        Args:
-            expectation_type=None                : The name of the expectation type to be matched.
-            column=None                          : The name of the column to be matched.
-            expectation_kwargs=None              : A dictionary of kwargs to match against.
-            remove_multiple_matches=False        : Match multiple expectations
-            dry_run=False                        : Return a list of matching expectations without removing
-
-        Returns:
-            None, unless dry_run=True.
-            If dry_run=True and remove_multiple_matches=False then return the expectation that *would be* removed.
-            If dry_run=True and remove_multiple_matches=True then return a list of expectations that *would be* removed.
-
-        Note:
-            If remove_expectation doesn't find any matches, it raises a ValueError.
-            If remove_expectation finds more than one matches and remove_multiple_matches!=True, it raises a ValueError.
-            If dry_run=True, then `remove_expectation` acts as a thin layer to find_expectations, with the default \
-            values for discard_result_format_kwargs, discard_include_config_kwargs, and discard_catch_exceptions_kwargs
-        """
-
-        match_indexes = self.find_expectation_indexes(
-            expectation_type,
-            column,
-            expectation_kwargs,
+        """This method is a thin wrapper for ExpectationSuite.remove()"""
+        return self._expectation_suite.remove_expectation(
+            expectation_type=expectation_type,
+            column=column,
+            expectation_kwargs=expectation_kwargs,
+            remove_multiple_matches=remove_multiple_matches,
+            dry_run=dry_run,
         )
 
-        if len(match_indexes) == 0:
-            raise ValueError('No matching expectation found.')
-
-        elif len(match_indexes) > 1:
-            if not remove_multiple_matches:
-                raise ValueError(
-                    'Multiple expectations matched arguments. No expectations removed.')
-            else:
-
-                if not dry_run:
-                    self._expectation_suite.expectations = [i for j, i in enumerate(
-                        self._expectation_suite.expectations) if j not in match_indexes]
-                else:
-                    return self._copy_and_clean_up_expectations_from_indexes(match_indexes)
-
-        else:  # Exactly one match
-            expectation = self._copy_and_clean_up_expectation(
-                self._expectation_suite.expectations[match_indexes[0]]
-            )
-
-            if not dry_run:
-                del self._expectation_suite.expectations[match_indexes[0]]
-
-            else:
-                if remove_multiple_matches:
-                    return [expectation]
-                else:
-                    return expectation
-
     def set_config_value(self, key, value):
         self._config[key] = value
 
     def get_config_value(self, key):
         return self._config[key]
 
     @property
```

### Comparing `great_expectations-0.9.8/great_expectations/init_notebooks/sql/validation_playground.ipynb` & `great_expectations-0.9.9/great_expectations/init_notebooks/sql/validation_playground.ipynb`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/init_notebooks/spark/validation_playground.ipynb` & `great_expectations-0.9.9/great_expectations/init_notebooks/spark/validation_playground.ipynb`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/init_notebooks/pandas/validation_playground.ipynb` & `great_expectations-0.9.9/great_expectations/init_notebooks/pandas/validation_playground.ipynb`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/util.py` & `great_expectations-0.9.9/great_expectations/datasource/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/table_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/table_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/s3_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/s3_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/subdir_reader_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/subdir_reader_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/query_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/query_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/manual_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/manual_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/databricks_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/databricks_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/batch_kwargs_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/batch_kwargs_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/generator/glob_reader_generator.py` & `great_expectations-0.9.9/great_expectations/datasource/generator/glob_reader_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/types/batch_kwargs.py` & `great_expectations-0.9.9/great_expectations/datasource/types/batch_kwargs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/sparkdf_datasource.py` & `great_expectations-0.9.9/great_expectations/datasource/sparkdf_datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/sqlalchemy_datasource.py` & `great_expectations-0.9.9/great_expectations/datasource/sqlalchemy_datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/pandas_datasource.py` & `great_expectations-0.9.9/great_expectations/datasource/pandas_datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/datasource/datasource.py` & `great_expectations-0.9.9/great_expectations/datasource/datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/profile/basic_dataset_profiler.py` & `great_expectations-0.9.9/great_expectations/profile/basic_dataset_profiler.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/profile/columns_exist.py` & `great_expectations-0.9.9/great_expectations/profile/columns_exist.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/profile/sample_expectations_dataset_profiler.py` & `great_expectations-0.9.9/great_expectations/profile/sample_expectations_dataset_profiler.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/profile/multi_batch_validation_meta_analysis.py` & `great_expectations-0.9.9/great_expectations/profile/multi_batch_validation_meta_analysis.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/profile/metrics_utils.py` & `great_expectations-0.9.9/great_expectations/profile/metrics_utils.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/profile/base.py` & `great_expectations-0.9.9/great_expectations/profile/base.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/exceptions.py` & `great_expectations-0.9.9/great_expectations/exceptions.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/util.py` & `great_expectations-0.9.9/great_expectations/data_context/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/templates.py` & `great_expectations-0.9.9/great_expectations/data_context/templates.py`

 * *Files 2% similar despite different names*

```diff
@@ -104,16 +104,17 @@
 data_docs_sites:
   # Data Docs make it simple to visualize data quality in your project. These
   # include Expectations, Validations & Profiles. The are built for all
   # Datasources from JSON artifacts in the local repo including validations &
   # profiles from the uncommitted directory. Read more at https://docs.greatexpectations.io/en/latest/features/data_docs.html
   local_site:
     class_name: SiteBuilder
+    # set to false to hide how-to buttons in Data Docs
+    show_how_to_buttons: true
     store_backend:
         class_name: TupleFilesystemStoreBackend
         base_directory: uncommitted/data_docs/local_site/
     site_index_builder:
         class_name: DefaultSiteIndexBuilder
-        show_cta_footer: True
 """
 
 PROJECT_TEMPLATE = PROJECT_HELP_COMMENT + PROJECT_OPTIONAL_CONFIG_COMMENT
```

### Comparing `great_expectations-0.9.8/great_expectations/data_context/types/resource_identifiers.py` & `great_expectations-0.9.9/great_expectations/data_context/types/resource_identifiers.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/types/base.py` & `great_expectations-0.9.9/great_expectations/data_context/types/base.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/expectations_store.py` & `great_expectations-0.9.9/great_expectations/data_context/store/expectations_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/html_site_store.py` & `great_expectations-0.9.9/great_expectations/data_context/store/html_site_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/validations_store.py` & `great_expectations-0.9.9/great_expectations/data_context/store/validations_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/store.py` & `great_expectations-0.9.9/great_expectations/data_context/store/store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/store_backend.py` & `great_expectations-0.9.9/great_expectations/data_context/store/store_backend.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/database_store_backend.py` & `great_expectations-0.9.9/great_expectations/data_context/store/database_store_backend.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/metric_store.py` & `great_expectations-0.9.9/great_expectations/data_context/store/metric_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/__init__.py` & `great_expectations-0.9.9/great_expectations/data_context/store/__init__.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/store/tuple_store_backend.py` & `great_expectations-0.9.9/great_expectations/data_context/store/tuple_store_backend.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/data_context/data_context.py` & `great_expectations-0.9.9/great_expectations/data_context/data_context.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 import warnings
 import webbrowser
 
 from marshmallow import ValidationError
 from ruamel.yaml import YAML, YAMLError
 from six import string_types
 
-from great_expectations.util import verify_dynamic_loading_support
+import great_expectations.exceptions as ge_exceptions
 from great_expectations.core import (
     ExpectationSuite,
     get_metric_kwargs_id,
 )
 from great_expectations.core.id_dict import BatchKwargs
 from great_expectations.core.metric import ValidationMetricIdentifier
 from great_expectations.core.util import nested_update
@@ -30,18 +30,15 @@
     file_relative_path,
     substitute_config_variable,
 )
 from great_expectations.dataset import Dataset
 from great_expectations.profile.basic_dataset_profiler import (
     BasicDatasetProfiler,
 )
-
-import great_expectations.exceptions as ge_exceptions
-
-from ..validator.validator import Validator
+from great_expectations.util import verify_dynamic_loading_support
 from .templates import (
     CONFIG_VARIABLES_INTRO,
     CONFIG_VARIABLES_TEMPLATE,
     PROJECT_TEMPLATE,
 )
 from .types.resource_identifiers import (
     ExpectationSuiteIdentifier,
@@ -49,14 +46,15 @@
 )
 from .util import (
     instantiate_class_from_config,
     load_class,
     safe_mmkdir,
     substitute_all_config_variables,
 )
+from ..validator.validator import Validator
 
 try:
     from urllib.parse import urlparse
 except ImportError:
     from urlparse import urlparse
 
 try:
@@ -531,14 +529,15 @@
         return validator.get_dataset()
 
     def run_validation_operator(
             self,
             validation_operator_name,
             assets_to_validate,
             run_id=None,
+            evaluation_parameters=None,
             **kwargs
     ):
         """
         Run a validation operator to validate data assets and to perform the business logic around
         validation that the operator implements.
 
         Args:
@@ -551,20 +550,27 @@
 
         Returns:
             ValidationOperatorResult
         """
         if run_id is None:
             run_id = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S.%fZ")
             logger.info("Setting run_id to: {}".format(run_id))
-
-        return self.validation_operators[validation_operator_name].run(
-            assets_to_validate=assets_to_validate,
-            run_id=run_id,
-            **kwargs
-        )
+        if evaluation_parameters is None:
+            return self.validation_operators[validation_operator_name].run(
+                assets_to_validate=assets_to_validate,
+                run_id=run_id,
+                **kwargs
+            )
+        else:
+            return self.validation_operators[validation_operator_name].run(
+                assets_to_validate=assets_to_validate,
+                run_id=run_id,
+                evaluation_parameters=evaluation_parameters,
+                **kwargs
+            )
 
     def list_validation_operator_names(self):
         if not self.validation_operators:
             return []
         return list(self.validation_operators.keys())
 
     def add_datasource(self, name, initialize=True, **kwargs):
```

### Comparing `great_expectations-0.9.8/great_expectations/validation_operators/util.py` & `great_expectations-0.9.9/great_expectations/validation_operators/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/validation_operators/validation_operators.py` & `great_expectations-0.9.9/great_expectations/validation_operators/validation_operators.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,15 +23,15 @@
     The base class of all validation operators.
 
     It defines the signature of the public run method - this is the only
     contract re operators' API. Everything else is up to the implementors
     of validation operator classes that will be the descendants of this base class.
     """
 
-    def run(self, assets_to_validate, run_id):
+    def run(self, assets_to_validate, run_id, evaluation_parameters=None):
         raise NotImplementedError
 
 
 class ActionListValidationOperator(ValidationOperator):
     """
     ActionListValidationOperator is a validation operator
     that validates each batch in the list that is passed to its run
@@ -120,15 +120,15 @@
                 expectation_suite_name=item[1]
             )
         else:
             batch = item
 
         return batch
 
-    def run(self, assets_to_validate, run_id):
+    def run(self, assets_to_validate, run_id, evaluation_parameters=None):
         result_object = {
             "success": None,
             "details": {}
         }
 
         for item in assets_to_validate:
             batch = self._build_batch_from_item(item)
@@ -137,17 +137,19 @@
             )
             # validation_result_id = ValidationResultIdentifier(
             #     batch_identifier=BatchIdentifier(batch.batch_id),
             #     expectation_suite_identifier=expectation_suite_identifier,
             #     run_id=run_id,
             # )
             result_object["details"][expectation_suite_identifier] = {}
-            batch_validation_result = batch.validate(run_id=run_id, result_format="SUMMARY")
+            batch_validation_result = batch.validate(run_id=run_id, result_format="SUMMARY",
+                                                     evaluation_parameters=evaluation_parameters)
             result_object["details"][expectation_suite_identifier]["validation_result"] = batch_validation_result
-            batch_actions_results = self._run_actions(batch, expectation_suite_identifier, batch._expectation_suite, batch_validation_result, run_id)
+            batch_actions_results = self._run_actions(batch, expectation_suite_identifier, batch._expectation_suite,
+                                                      batch_validation_result, run_id)
             result_object["details"][expectation_suite_identifier]["actions_results"] = batch_actions_results
 
         result_object["success"] = all([val["validation_result"].success for val in result_object["details"].values()])
 
         return result_object
 
     def _run_actions(self, batch, expectation_suite_identifier, expectation_suite, batch_validation_result, run_id):
```

### Comparing `great_expectations-0.9.8/great_expectations/validation_operators/actions.py` & `great_expectations-0.9.9/great_expectations/validation_operators/actions.py`

 * *Files 2% similar despite different names*

```diff
@@ -242,27 +242,30 @@
 class UpdateDataDocsAction(ValidationAction):
     """
     UpdateDataDocsAction is a namespace-aware validation action that
     notifies the site builders of all the data docs sites of the data context
     that a validation result should be added to the data docs.
     """
 
-    def __init__(self, data_context):
+    def __init__(self, data_context, target_site_names=None):
         """
         :param data_context: data context
+        :param target_site_names: *optional* List of site names for building data docs
         """
         super(UpdateDataDocsAction, self).__init__(data_context)
+        self._target_site_names = target_site_names
 
     def _run(self, validation_result_suite, validation_result_suite_identifier, data_asset):
         logger.debug("UpdateDataDocsAction.run")
 
         if validation_result_suite is None:
             return
 
         if not isinstance(validation_result_suite_identifier, ValidationResultIdentifier):
             raise TypeError("validation_result_id must be of type ValidationResultIdentifier, not {0}".format(
                 type(validation_result_suite_identifier)
             ))
 
         self.data_context.build_data_docs(
+            site_names=self._target_site_names,
             resource_identifiers=[validation_result_suite_identifier]
         )
```

### Comparing `great_expectations-0.9.8/great_expectations/validation_operators/__init__.py` & `great_expectations-0.9.9/great_expectations/validation_operators/__init__.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/init_messages.py` & `great_expectations-0.9.9/great_expectations/cli/init_messages.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/util.py` & `great_expectations-0.9.9/great_expectations/cli/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/init.py` & `great_expectations-0.9.9/great_expectations/cli/init.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/project.py` & `great_expectations-0.9.9/great_expectations/cli/project.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/docs.py` & `great_expectations-0.9.9/great_expectations/cli/docs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/cli.py` & `great_expectations-0.9.9/great_expectations/cli/cli.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/suite.py` & `great_expectations-0.9.9/great_expectations/cli/suite.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/validation_operator.py` & `great_expectations-0.9.9/great_expectations/cli/validation_operator.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import json
 import sys
+from datetime import datetime
 
 import click
-from datetime import datetime
+
 from great_expectations import DataContext
 from great_expectations import exceptions as ge_exceptions
 from great_expectations.cli.datasource import (
     get_batch_kwargs,
     select_datasource,
 )
 from great_expectations.cli.util import (
@@ -190,18 +191,34 @@
             for expectation_suite_name in entry["expectation_suite_names"]:
                 batch = context.get_batch(entry["batch_kwargs"], expectation_suite_name)
                 batches_to_validate.append(batch)
 
         if run_id is None:
             run_id = datetime.utcnow().strftime("%Y%m%dT%H%M%S.%fZ")
 
-        results = context.run_validation_operator(
-            validation_operator_name,
-            assets_to_validate=[batch],
-            run_id=run_id)
+        if suite is None:
+            results = context.run_validation_operator(
+                validation_operator_name,
+                assets_to_validate=batches_to_validate,
+                run_id=run_id
+            )
+        else:
+            if suite.evaluation_parameters is None:
+                results = context.run_validation_operator(
+                    validation_operator_name,
+                    assets_to_validate=batches_to_validate,
+                    run_id=run_id
+                )
+            else:
+                results = context.run_validation_operator(
+                    validation_operator_name,
+                    assets_to_validate=batches_to_validate,
+                    run_id=run_id,
+                    evaluation_parameters=suite.evaluation_parameters
+                )
 
     except (
         ge_exceptions.DataContextError,
         IOError,
         SQLAlchemyError,
     ) as e:
         cli_message("<red>{}</red>".format(e))
@@ -253,8 +270,8 @@
 
     for batch in valdiation_config["batches"]:
         if "batch_kwargs" not in batch:
             return "Each batch must have a BatchKwargs dictionary in batch_kwargs attribute"
         if "expectation_suite_names" not in batch:
             return "Each batch must have a list of expectation suite names in expectation_suite_names attribute"
 
-    return None
+    return None
```

### Comparing `great_expectations-0.9.8/great_expectations/cli/tap_template.py` & `great_expectations-0.9.9/great_expectations/cli/tap_template.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/datasource.py` & `great_expectations-0.9.9/great_expectations/cli/datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/tap.py` & `great_expectations-0.9.9/great_expectations/cli/tap.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/cli/cli_logging.py` & `great_expectations-0.9.9/great_expectations/cli/cli_logging.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/core/util.py` & `great_expectations-0.9.9/great_expectations/core/util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/core/id_dict.py` & `great_expectations-0.9.9/great_expectations/core/id_dict.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/core/metric.py` & `great_expectations-0.9.9/great_expectations/core/metric.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/core/data_context_key.py` & `great_expectations-0.9.9/great_expectations/core/data_context_key.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/core/__init__.py` & `great_expectations-0.9.9/great_expectations/core/__init__.py`

 * *Files 22% similar despite different names*

```diff
@@ -588,14 +588,262 @@
         return citations_with_bk
 
     @staticmethod
     def _sort_citations(citations):
         return sorted(citations, key=lambda x: x["citation_date"])
 
 
+    def _copy_and_clean_up_expectation(self,
+        expectation,
+        discard_result_format_kwargs=True,
+        discard_include_config_kwargs=True,
+        discard_catch_exceptions_kwargs=True,
+    ):
+        """Returns copy of `expectation` without `success_on_last_run` and other specified key-value pairs removed
+
+          Returns a copy of specified expectation will not have `success_on_last_run` key-value. The other key-value \
+          pairs will be removed by default but will remain in the copy if specified.
+
+          Args:
+              expectation (json): \
+                  The expectation to copy and clean.
+              discard_result_format_kwargs (boolean): \
+                  if True, will remove the kwarg `output_format` key-value pair from the copied expectation.
+              discard_include_config_kwargs (boolean):
+                  if True, will remove the kwarg `include_config` key-value pair from the copied expectation.
+              discard_catch_exceptions_kwargs (boolean):
+                  if True, will remove the kwarg `catch_exceptions` key-value pair from the copied expectation.
+
+          Returns:
+              A copy of the provided expectation with `success_on_last_run` and other specified key-value pairs removed
+
+          Note: 
+              This method may move to ExpectationConfiguration, minus the "copy" part.
+        """
+        new_expectation = deepcopy(expectation)
+
+        if "success_on_last_run" in new_expectation:
+            del new_expectation["success_on_last_run"]
+
+        if discard_result_format_kwargs:
+            if "result_format" in new_expectation.kwargs:
+                del new_expectation.kwargs["result_format"]
+                # discards["result_format"] += 1
+
+        if discard_include_config_kwargs:
+            if "include_config" in new_expectation.kwargs:
+                del new_expectation.kwargs["include_config"]
+                # discards["include_config"] += 1
+
+        if discard_catch_exceptions_kwargs:
+            if "catch_exceptions" in new_expectation.kwargs:
+                del new_expectation.kwargs["catch_exceptions"]
+                # discards["catch_exceptions"] += 1
+
+        return new_expectation
+
+    def _copy_and_clean_up_expectations_from_indexes(
+        self,
+        match_indexes,
+        discard_result_format_kwargs=True,
+        discard_include_config_kwargs=True,
+        discard_catch_exceptions_kwargs=True,
+    ):
+        """Copies and cleans all expectations provided by their index in DataAsset._expectation_suite.expectations.
+
+           Applies the _copy_and_clean_up_expectation method to multiple expectations, provided by their index in \
+           `DataAsset,_expectation_suite.expectations`. Returns a list of the copied and cleaned expectations.
+
+           Args:
+               match_indexes (List): \
+                   Index numbers of the expectations from `expectation_config.expectations` to be copied and cleaned.
+               discard_result_format_kwargs (boolean): \
+                   if True, will remove the kwarg `output_format` key-value pair from the copied expectation.
+               discard_include_config_kwargs (boolean):
+                   if True, will remove the kwarg `include_config` key-value pair from the copied expectation.
+               discard_catch_exceptions_kwargs (boolean):
+                   if True, will remove the kwarg `catch_exceptions` key-value pair from the copied expectation.
+
+           Returns:
+               A list of the copied expectations with `success_on_last_run` and other specified \
+               key-value pairs removed.
+
+           See also:
+               _copy_and_clean_expectation
+        """
+        rval = []
+        for i in match_indexes:
+            rval.append(
+                self._copy_and_clean_up_expectation(
+                    self.expectations[i],
+                    discard_result_format_kwargs,
+                    discard_include_config_kwargs,
+                    discard_catch_exceptions_kwargs,
+                )
+            )
+
+        return rval
+
+    ### CRUD methods ###
+
+    def append_expectation(self, expectation_config):
+        """Appends an expectation.
+
+           Args:
+               expectation_config (ExpectationConfiguration): \
+                   The expectation to be added to the list.
+
+           Notes:
+               May want to add type-checking in the future.
+        """
+        self.expectations.append(expectation_config)
+
+    def find_expectation_indexes(self,
+        expectation_type=None,
+        column=None,
+        expectation_kwargs=None
+    ):
+        """Find matching expectations and return their indexes.
+        Args:
+            expectation_type=None                : The name of the expectation type to be matched.
+            column=None                          : The name of the column to be matched.
+            expectation_kwargs=None              : A dictionary of kwargs to match against.
+
+        Returns:
+            A list of indexes for matching expectation objects.
+            If there are no matches, the list will be empty.
+        """
+        if expectation_kwargs is None:
+            expectation_kwargs = {}
+
+        if "column" in expectation_kwargs and column is not None and column is not expectation_kwargs["column"]:
+            raise ValueError("Conflicting column names in find_expectation_indexes: %s and %s" % (
+                column, expectation_kwargs["column"]))
+
+        if column is not None:
+            expectation_kwargs["column"] = column
+
+        match_indexes = []
+        for i, exp in enumerate(self.expectations):
+            if expectation_type is None or (expectation_type == exp.expectation_type):
+                # if column == None or ('column' not in exp['kwargs']) or
+                # (exp['kwargs']['column'] == column) or (exp['kwargs']['column']==:
+                match = True
+
+                for k, v in expectation_kwargs.items():
+                    if k in exp['kwargs'] and exp['kwargs'][k] == v:
+                        continue
+                    else:
+                        match = False
+
+                if match:
+                    match_indexes.append(i)
+
+        return match_indexes
+
+    def find_expectations(self,
+        expectation_type=None,
+        column=None,
+        expectation_kwargs=None,
+        discard_result_format_kwargs=True,
+        discard_include_config_kwargs=True,
+        discard_catch_exceptions_kwargs=True,
+    ):
+        """Find matching expectations and return them.
+        Args:
+            expectation_type=None                : The name of the expectation type to be matched.
+            column=None                          : The name of the column to be matched.
+            expectation_kwargs=None              : A dictionary of kwargs to match against.
+            discard_result_format_kwargs=True    : In returned expectation object(s), \
+            suppress the `result_format` parameter.
+            discard_include_config_kwargs=True  : In returned expectation object(s), \
+            suppress the `include_config` parameter.
+            discard_catch_exceptions_kwargs=True : In returned expectation object(s), \
+            suppress the `catch_exceptions` parameter.
+
+        Returns:
+            A list of matching expectation objects.
+            If there are no matches, the list will be empty.
+        """
+
+        match_indexes = self.find_expectation_indexes(
+            expectation_type,
+            column,
+            expectation_kwargs,
+        )
+
+        return self._copy_and_clean_up_expectations_from_indexes(
+            match_indexes,
+            discard_result_format_kwargs,
+            discard_include_config_kwargs,
+            discard_catch_exceptions_kwargs,
+        )
+
+    def remove_expectation(self,
+        expectation_type=None,
+        column=None,
+        expectation_kwargs=None,
+        remove_multiple_matches=False,
+        dry_run=False,
+    ):
+        """Remove matching expectation(s).
+        Args:
+            expectation_type=None                : The name of the expectation type to be matched.
+            column=None                          : The name of the column to be matched.
+            expectation_kwargs=None              : A dictionary of kwargs to match against.
+            remove_multiple_matches=False        : Match multiple expectations
+            dry_run=False                        : Return a list of matching expectations without removing
+
+        Returns:
+            None, unless dry_run=True.
+            If dry_run=True and remove_multiple_matches=False then return the expectation that *would be* removed.
+            If dry_run=True and remove_multiple_matches=True then return a list of expectations that *would be* removed.
+
+        Note:
+            If remove_expectation doesn't find any matches, it raises a ValueError.
+            If remove_expectation finds more than one matches and remove_multiple_matches!=True, it raises a ValueError.
+            If dry_run=True, then `remove_expectation` acts as a thin layer to find_expectations, with the default \
+            values for discard_result_format_kwargs, discard_include_config_kwargs, and discard_catch_exceptions_kwargs
+        """
+
+        match_indexes = self.find_expectation_indexes(
+            expectation_type,
+            column,
+            expectation_kwargs,
+        )
+
+        if len(match_indexes) == 0:
+            raise ValueError('No matching expectation found.')
+
+        elif len(match_indexes) > 1:
+            if not remove_multiple_matches:
+                raise ValueError(
+                    'Multiple expectations matched arguments. No expectations removed.')
+            else:
+
+                if not dry_run:
+                    self.expectations = [i for j, i in enumerate(
+                        self.expectations) if j not in match_indexes]
+                else:
+                    return self._copy_and_clean_up_expectations_from_indexes(match_indexes)
+
+        else:  # Exactly one match
+            expectation = self._copy_and_clean_up_expectation(
+                self.expectations[match_indexes[0]]
+            )
+
+            if not dry_run:
+                del self.expectations[match_indexes[0]]
+
+            else:
+                if remove_multiple_matches:
+                    return [expectation]
+                else:
+                    return expectation
+
 class ExpectationSuiteSchema(Schema):
     expectation_suite_name = fields.Str()
     expectations = fields.List(fields.Nested(ExpectationConfigurationSchema))
     evaluation_parameters = fields.Dict(allow_none=True)
     data_asset_type = fields.Str(allow_none=True)
     meta = fields.Dict()
```

### Comparing `great_expectations-0.9.8/great_expectations/core/batch.py` & `great_expectations-0.9.9/great_expectations/core/batch.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/jupyter_ux/expectation_explorer.py` & `great_expectations-0.9.9/great_expectations/jupyter_ux/expectation_explorer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations/jupyter_ux/__init__.py` & `great_expectations-0.9.9/great_expectations/jupyter_ux/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -5,16 +5,19 @@
 import sys
 
 from datetime import datetime
 
 import tzlocal
 from IPython.core.display import display, HTML
 
-from great_expectations.render.renderer import ProfilingResultsColumnSectionRenderer, \
-    ExpectationSuiteColumnSectionRenderer
+from great_expectations.render.renderer import (
+    ExpectationSuiteColumnSectionRenderer,
+    ProfilingResultsColumnSectionRenderer,
+    ValidationResultsColumnSectionRenderer,
+)
 from great_expectations.render.types import RenderedSectionContent
 from great_expectations.render.view import DefaultJinjaSectionView
 
 
 def set_data_source(context, data_source_type=None):
     """
     TODO: Needs a docstring and tests.
@@ -75,15 +78,15 @@
         else:
             data_source_name = configured_datasources[0]
             display(HTML("Will be using this {0:s} data source from your project's great_expectations.yml: <b>{1:s}</b>".format(data_source_type, data_source_name)))
 
     return data_source_name
 
 
-def setup_notebook_logging(logger=None):
+def setup_notebook_logging(logger=None, log_level=logging.INFO):
     """Set up the provided logger for the GE default logging configuration.
 
     Args:
         logger - the logger to configure
     """
 
     def posix2local(timestamp, tz=tzlocal.get_localzone()):
@@ -107,16 +110,16 @@
         logger = logging.getLogger("great_expectations")
 
     chandler = logging.StreamHandler(stream=sys.stdout)
     chandler.setLevel(logging.DEBUG)
     # chandler.setFormatter(Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%dT%H:%M:%S%z"))
     chandler.setFormatter(Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%dT%H:%M:%S%z"))
     logger.addHandler(chandler)
-    logger.setLevel(logging.INFO)
-    logger.info("Great Expectations logging enabled at INFO level by JupyterUX module.")
+    logger.setLevel(log_level)
+    logger.info("Great Expectations logging enabled at %s level by JupyterUX module." % (log_level,) )
     #
     # # Filter warnings
     # import warnings
     # warnings.filterwarnings('ignore')
 
 
 def show_available_data_asset_names(context, data_source_name=None):
@@ -232,14 +235,29 @@
     transform:translate(-50%,-50%) rotate(45deg);
     background-color:#222222;
     box-shadow:0 1px 8px rgba(0,0,0,0.5);
 }
 </style>
 """
 
+def _render_for_jupyter(
+    view,
+    include_styling,
+    return_without_displaying,
+):
+    if include_styling:
+        html_to_display = bootstrap_link_element+cooltip_style_element+view
+    else:
+        html_to_display = view
+
+    if return_without_displaying:
+        return html_to_display
+    else:
+        display(HTML(html_to_display))
+
 
 def display_column_expectations_as_section(
     expectation_suite,
     column,
     include_styling=True,
     return_without_displaying=False,
 ):
@@ -257,60 +275,85 @@
     column_expectation_list = [ e for e in expectation_suite.expectations if "column" in e.kwargs and e.kwargs["column"] == column ]
 
     #TODO: Handle the case where zero evrs match the column name
 
     document = ExpectationSuiteColumnSectionRenderer().render(column_expectation_list).to_json_dict()
     view = DefaultJinjaSectionView().render({"section": document, "section_loop": 1})
 
-    if include_styling:
-        html_to_display = bootstrap_link_element+cooltip_style_element+view
-    else:
-        html_to_display = view
+    return _render_for_jupyter(
+        view,
+        include_styling,
+        return_without_displaying,
+    )
 
-    if return_without_displaying:
-        return html_to_display
-    else:
-        display(HTML(html_to_display))
 
+def display_profiled_column_evrs_as_section(
+    evrs,
+    column,
+    include_styling=True,
+    return_without_displaying=False,
+):
+    """This is a utility function to render all of the EVRs in an ExpectationSuite with the same column name as an HTML block.
+
+    By default, the HTML block is rendered using ExpectationSuiteColumnSectionRenderer and the view is rendered using DefaultJinjaSectionView.
+    Therefore, it should look exactly the same as the default renderer for build_docs.
+
+    Example usage:
+    display_column_evrs_as_section(exp, "my_column")
+
+    WARNING: This method is experimental.
+    """
+
+    #TODO: replace this with a generic utility function, preferably a method on an ExpectationSuite class
+    column_evr_list = [ e for e in evrs.results if "column" in e.expectation_config.kwargs and e.expectation_config.kwargs["column"] == column ]
+
+    #TODO: Handle the case where zero evrs match the column name
+
+    document = ProfilingResultsColumnSectionRenderer().render(column_evr_list).to_json_dict()
+    view = DefaultJinjaSectionView().render(
+        {
+            "section": document,
+            "section_loop": {"index": 1},
+        }
+    )
+
+    return _render_for_jupyter(
+        view,
+        include_styling,
+        return_without_displaying,
+    )
+
+def display_column_evrs_as_section(
+    evrs,
+    column,
+    include_styling=True,
+    return_without_displaying=False,
+):
+    """
+    Display validation results for a single column as a section.
+
+    WARNING: This method is experimental.
+    """
+
+    #TODO: replace this with a generic utility function, preferably a method on an ExpectationSuite class
+    column_evr_list = [ e for e in evrs.results if "column" in e.expectation_config.kwargs and e.expectation_config.kwargs["column"] == column ]
+
+    #TODO: Handle the case where zero evrs match the column name
 
-# def display_column_evrs_as_section(
-#     evrs,
-#     column,
-#     include_styling=True,
-#     return_without_displaying=False,
-# ):
-#     """This is a utility function to render all of the EVRs in an ExpectationSuite with the same column name as an HTML block.
-#
-#     By default, the HTML block is rendered using ExpectationSuiteColumnSectionRenderer and the view is rendered using DefaultJinjaSectionView.
-#     Therefore, it should look exactly the same as the default renderer for build_docs.
-#
-#     Example usage:
-#     display_column_evrs_as_section(exp, "my_column")
-#     """
-#
-#     #TODO: replace this with a generic utility function, preferably a method on an ExpectationSuite class
-#     column_evr_list = [ e for e in evrs.results if "column" in e.expectation_config.kwargs and e.expectation_config.kwargs["column"] == column ]
-#
-#     #TODO: Handle the case where zero evrs match the column name
-#
-#     document = ProfilingResultsColumnSectionRenderer().render(column_evr_list)
-#     view = DefaultJinjaSectionView().render(
-#         {
-#             "section": document,
-#             "section_loop": {"index": 1},
-#         }
-#     )
-#
-#     if include_styling:
-#         html_to_display = bootstrap_link_element+cooltip_style_element+view
-#     else:
-#         html_to_display = view
-#
-#     if return_without_displaying:
-#         return html_to_display
-#     else:
-#         display(HTML(html_to_display))
+    document = ValidationResultsColumnSectionRenderer().render(column_evr_list).to_json_dict()
+    view = DefaultJinjaSectionView().render(
+        {
+            "section": document,
+            "section_loop": {"index": 1},
+        }
+    )
+
+    return _render_for_jupyter(
+        view,
+        include_styling,
+        return_without_displaying,
+    )
 
 
 # When importing the jupyter_ux module, we set up a preferred logging configuration
 logger = logging.getLogger("great_expectations")
 setup_notebook_logging(logger)
```

### Comparing `great_expectations-0.9.8/LICENSE` & `great_expectations-0.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/great_expectations.egg-info/PKG-INFO` & `great_expectations-0.9.9/great_expectations.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: great-expectations
-Version: 0.9.8
+Version: 0.9.9
 Summary: Always know what to expect from your data.
 Home-page: https://github.com/great-expectations/great_expectations
 Author: The Great Expectations Team
 Author-email: team@greatexpectations.io
 License: Apache-2.0
 Description: Always know what to expect from your data. (See https://github.com/great-expectations/great_expectations for full description).
 Keywords: data science testing pipeline data quality dataquality validation datavalidation
```

### Comparing `great_expectations-0.9.8/great_expectations.egg-info/SOURCES.txt` & `great_expectations-0.9.9/great_expectations.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -209,14 +209,15 @@
 tests/cli/test_validation_operator.py
 tests/cli/utils.py
 tests/core/__init__.py
 tests/core/test_evaluation_parameters.py
 tests/core/test_expectation_configuration.py
 tests/core/test_expectation_kwargs.py
 tests/core/test_expectation_suite.py
+tests/core/test_expectation_suite_crud_methods.py
 tests/core/test_serialization.py
 tests/data_asset/__init__.py
 tests/data_asset/test_data_asset.py
 tests/data_asset/test_data_asset_citations.py
 tests/data_asset/test_data_asset_internals.py
 tests/data_asset/test_data_asset_util.py
 tests/data_asset/test_expectation_decorators.py
@@ -383,14 +384,15 @@
 tests/test_fixtures/fixed_distribution_data.py
 tests/test_fixtures/great_expectations_basic.yml
 tests/test_fixtures/great_expectations_basic_with_variables.yml
 tests/test_fixtures/great_expectations_basic_without_config_variables_filepath.yml
 tests/test_fixtures/great_expectations_site_builder.yml
 tests/test_fixtures/great_expectations_titanic.yml
 tests/test_fixtures/expectation_suites/parameterized_expectation_suite_fixture.json
+tests/test_fixtures/expectation_suites/parameterized_expression_expectation_suite_fixture.json
 tests/test_fixtures/rendering_fixtures/evr_suite_1.json
 tests/test_fixtures/rendering_fixtures/evr_suite_3.json
 tests/test_fixtures/rendering_fixtures/expectation_suite_3.json
 tests/test_fixtures/rendering_fixtures/expectations_suite_1.json
 tests/test_fixtures/rendering_fixtures/expectations_suite_2.json
 tests/test_plugins/__init__.py
 tests/test_plugins/fake_actions.py
```

### Comparing `great_expectations-0.9.8/setup.py` & `great_expectations-0.9.9/setup.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_plugins/fake_configs.py` & `great_expectations-0.9.9/tests/test_plugins/fake_configs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/dataset/test_dataset_legacy.py` & `great_expectations-0.9.9/tests/dataset/test_dataset_legacy.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/dataset/test_dataset_util_legacy.py` & `great_expectations-0.9.9/tests/dataset/test_dataset_util_legacy.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/dataset/test_util.py` & `great_expectations-0.9.9/tests/dataset/test_util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/dataset/test_sparkdfdataset.py` & `great_expectations-0.9.9/tests/dataset/test_sparkdfdataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/dataset/test_sqlalchemydataset.py` & `great_expectations-0.9.9/tests/dataset/test_sqlalchemydataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/dataset/test_pandas_dataset.py` & `great_expectations-0.9.9/tests/dataset/test_pandas_dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_dataset_implementations/test_dataset_implementations.py` & `great_expectations-0.9.9/tests/test_dataset_implementations/test_dataset_implementations.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_dataset_implementations/test_dataset_implementations.json` & `great_expectations-0.9.9/tests/test_dataset_implementations/test_dataset_implementations.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/fixtures/SampleExpectationsDatasetProfiler_evrs.json` & `great_expectations-0.9.9/tests/render/fixtures/SampleExpectationsDatasetProfiler_evrs.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_evrs_with_exception.json` & `great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_evrs_with_exception.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_evrs.json` & `great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_evrs.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_expectations.json` & `great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_expectations.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/fixtures/BasicDatasetProfiler_expectations_with_distribution.json` & `great_expectations-0.9.9/tests/render/fixtures/BasicDatasetProfiler_expectations_with_distribution.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_styled_string_template.py` & `great_expectations-0.9.9/tests/render/test_styled_string_template.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_render.py` & `great_expectations-0.9.9/tests/render/test_render.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_render_ValidationResultsTableContentBlockRenderer.py` & `great_expectations-0.9.9/tests/render/test_render_ValidationResultsTableContentBlockRenderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_render_BulletListContentBlock.py` & `great_expectations-0.9.9/tests/render/test_render_BulletListContentBlock.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_renderer.py` & `great_expectations-0.9.9/tests/render/test_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_page_renderer.py` & `great_expectations-0.9.9/tests/render/test_page_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_default_jinja_view.py` & `great_expectations-0.9.9/tests/render/test_default_jinja_view.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_util.py` & `great_expectations-0.9.9/tests/render/test_util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_SlackRenderer.py` & `great_expectations-0.9.9/tests/render/test_SlackRenderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_render_ExceptionListContentBlockRenderer.py` & `great_expectations-0.9.9/tests/render/test_render_ExceptionListContentBlockRenderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/renderer/content_block/test_expectation_string_renderer.py` & `great_expectations-0.9.9/tests/render/renderer/content_block/test_expectation_string_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/renderer/test_notebook_renderer.py` & `great_expectations-0.9.9/tests/render/renderer/test_notebook_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/render/test_column_section_renderer.py` & `great_expectations-0.9.9/tests/render/test_column_section_renderer.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_asset/test_expectation_decorators.py` & `great_expectations-0.9.9/tests/data_asset/test_expectation_decorators.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_asset/test_filedata_asset.py` & `great_expectations-0.9.9/tests/data_asset/test_filedata_asset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_asset/test_filedata_asset_expectations.py` & `great_expectations-0.9.9/tests/data_asset/test_filedata_asset_expectations.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_asset/test_data_asset.py` & `great_expectations-0.9.9/tests/data_asset/test_data_asset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_asset/test_data_asset_internals.py` & `great_expectations-0.9.9/tests/data_asset/test_data_asset_internals.py`

 * *Files 1% similar despite different names*

```diff
@@ -678,15 +678,15 @@
     ]
 
     assert my_df.find_expectations("expect_column_to_exist") == exp1
 
     with pytest.raises(ValueError) as exc:
         my_df.find_expectations("expect_column_to_exist", "x", {"column": "y"})
 
-    assert 'Conflicting column names in remove_expectation:' in str(exc.value)
+    assert 'Conflicting column names in find_expectation_indexes:' in str(exc.value)
 
     exp1 = [
         ExpectationConfiguration(
                 expectation_type="expect_column_to_exist",
                 kwargs={"column": "x"}
         ),
         ExpectationConfiguration(
@@ -763,15 +763,15 @@
     assert my_df.remove_expectation("expect_column_to_exist", remove_multiple_matches=True, dry_run=True) == \
         exp1
 
     with pytest.raises(ValueError) as exc:
         my_df.remove_expectation("expect_column_to_exist", "x", {
                                  "column": "y"}, dry_run=True)
 
-    assert 'Conflicting column names in remove_expectation' in str(exc.value)
+    assert 'Conflicting column names in find_expectation_indexes' in str(exc.value)
 
     exp1 = [
         ExpectationConfiguration(
             expectation_type="expect_column_to_exist",
             kwargs={"column": "x"}
         ),
         ExpectationConfiguration(
```

### Comparing `great_expectations-0.9.8/tests/data_asset/test_data_asset_citations.py` & `great_expectations-0.9.9/tests/data_asset/test_data_asset_citations.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_asset/test_parameter_substitution.py` & `great_expectations-0.9.9/tests/data_asset/test_parameter_substitution.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_asset/test_data_asset_util.py` & `great_expectations-0.9.9/tests/data_asset/test_data_asset_util.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_great_expectations.py` & `great_expectations-0.9.9/tests/test_great_expectations.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/generator/test_subdir_reader_generator.py` & `great_expectations-0.9.9/tests/datasource/generator/test_subdir_reader_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/generator/test_s3_generator.py` & `great_expectations-0.9.9/tests/datasource/generator/test_s3_generator.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import pytest
-from moto import mock_s3
 
 import logging
 import pandas as pd
 import boto3
+from moto import mock_s3
 
 from great_expectations.datasource.generator.s3_generator import S3GlobReaderBatchKwargsGenerator
 from great_expectations.exceptions import BatchKwargsError
 
 
 @pytest.fixture(scope="module")
 def mock_s3_bucket():
```

### Comparing `great_expectations-0.9.8/tests/datasource/generator/test_manual_generator.py` & `great_expectations-0.9.9/tests/datasource/generator/test_manual_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/generator/test_table_generator.py` & `great_expectations-0.9.9/tests/datasource/generator/test_table_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/generator/test_query_generator.py` & `great_expectations-0.9.9/tests/datasource/generator/test_query_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/generator/test_glob_reader_generator.py` & `great_expectations-0.9.9/tests/datasource/generator/test_glob_reader_generator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/test_batch_kwargs.py` & `great_expectations-0.9.9/tests/datasource/test_batch_kwargs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/test_sqlalchemy_datasource.py` & `great_expectations-0.9.9/tests/datasource/test_sqlalchemy_datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/test_sparkdf_datasource.py` & `great_expectations-0.9.9/tests/datasource/test_sparkdf_datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/test_batch_generators.py` & `great_expectations-0.9.9/tests/datasource/test_batch_generators.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/conftest.py` & `great_expectations-0.9.9/tests/datasource/conftest.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/datasource/test_pandas_datasource.py` & `great_expectations-0.9.9/tests/datasource/test_pandas_datasource.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_configs.py` & `great_expectations-0.9.9/tests/test_configs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/test_partitions.json` & `great_expectations-0.9.9/tests/test_sets/test_partitions.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_base.csv` & `great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_base.csv`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/titanic.db` & `great_expectations-0.9.9/tests/test_sets/titanic.db`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/Titanic_multi_sheet.xlsx` & `great_expectations-0.9.9/tests/test_sets/Titanic_multi_sheet.xlsx`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/Titanic.csv` & `great_expectations-0.9.9/tests/test_sets/Titanic.csv`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/test_json_data_file.json` & `great_expectations-0.9.9/tests/test_sets/test_json_data_file.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/Titanic.pkl` & `great_expectations-0.9.9/tests/test_sets/Titanic.pkl`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/expected_evrs_BasicDatasetProfiler_on_titanic.json` & `great_expectations-0.9.9/tests/test_sets/expected_evrs_BasicDatasetProfiler_on_titanic.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/nested_test_json_data_file.json` & `great_expectations-0.9.9/tests/test_sets/nested_test_json_data_file.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/expected_evrs_SampleExpectationsDatasetProfiler_on_titanic.json` & `great_expectations-0.9.9/tests/test_sets/expected_evrs_SampleExpectationsDatasetProfiler_on_titanic.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/expected_cli_results_custom.json` & `great_expectations-0.9.9/tests/test_sets/expected_cli_results_custom.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/expected_cli_results_default.json` & `great_expectations-0.9.9/tests/test_sets/expected_cli_results_default.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_test.csv` & `great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_test.csv`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/titanic_expected_data_asset_validate_results.json` & `great_expectations-0.9.9/tests/test_sets/titanic_expected_data_asset_validate_results.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/fixed_distributional_test_dataset.csv` & `great_expectations-0.9.9/tests/test_sets/fixed_distributional_test_dataset.csv`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/titanic_expectations.json` & `great_expectations-0.9.9/tests/test_sets/titanic_expectations.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/broken_excel_file.xls` & `great_expectations-0.9.9/tests/test_sets/broken_excel_file.xls`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/Titanic.parquet` & `great_expectations-0.9.9/tests/test_sets/Titanic.parquet`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/titanic_expected_data_asset_validate_results_with_exceptions.json` & `great_expectations-0.9.9/tests/test_sets/titanic_expected_data_asset_validate_results_with_exceptions.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_base.json` & `great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_base.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/titanic_parameterized_expectations.json` & `great_expectations-0.9.9/tests/test_sets/titanic_parameterized_expectations.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/fixed_distributional_test_dataset.json` & `great_expectations-0.9.9/tests/test_sets/fixed_distributional_test_dataset.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/distributional_expectations_data_test.json` & `great_expectations-0.9.9/tests/test_sets/distributional_expectations_data_test.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_sets/test_partitions_definition_fixture.json` & `great_expectations-0.9.9/tests/test_sets/test_partitions_definition_fixture.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_median_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_median_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_proportion_of_unique_values_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_proportion_of_unique_values_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_mean_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_mean_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_min_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_min_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_contain_set.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_contain_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_be_in_set.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_be_in_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_equal_set.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_distinct_values_to_equal_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_stdev_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_stdev_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_sum_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_sum_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_quantile_values_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_quantile_values_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_unique_value_count_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_unique_value_count_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_most_common_value_to_be_in_set.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_most_common_value_to_be_in_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_aggregate_expectations/expect_column_max_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_aggregate_expectations/expect_column_max_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/multicolumn_map_expectations/expect_multicolumn_values_to_be_unique.json` & `great_expectations-0.9.9/tests/test_definitions/multicolumn_map_expectations/expect_multicolumn_values_to_be_unique.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_null.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_null.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_json_schema.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_json_schema.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex_list.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_regex_list.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_match_strftime_format.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_match_strftime_format.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_set.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_null.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_null.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_of_type.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_of_type.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_equal.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_value_lengths_to_equal.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex_list.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_match_regex_list.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_decreasing.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_decreasing.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_increasing.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_increasing.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_type_list.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_in_type_list.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_in_set.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_not_be_in_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_map_expectations/expect_column_values_to_be_unique.json` & `great_expectations-0.9.9/tests/test_definitions/column_map_expectations/expect_column_values_to_be_unique.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_equal.json` & `great_expectations-0.9.9/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_equal.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_in_set.json` & `great_expectations-0.9.9/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_to_be_in_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_A_to_be_greater_than_B.json` & `great_expectations-0.9.9/tests/test_definitions/column_pair_map_expectations/expect_column_pair_values_A_to_be_greater_than_B.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_columns_to_match_ordered_list_test_set.json` & `great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_columns_to_match_ordered_list_test_set.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_row_count_to_equal.json` & `great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_row_count_to_equal.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_column_count_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_column_count_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_this_test_to_be_suppressed.json` & `great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_this_test_to_be_suppressed.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_column_to_exist.json` & `great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_column_to_exist.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_row_count_to_be_between.json` & `great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_row_count_to_be_between.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/other_expectations/expect_table_column_count_to_equal.json` & `great_expectations-0.9.9/tests/test_definitions/other_expectations/expect_table_column_count_to_equal.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/test_expectations.py` & `great_expectations-0.9.9/tests/test_definitions/test_expectations.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than.json` & `great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/test_expect_column_bootstrapped_ks_test_p_value_to_be_greater_than.json` & `great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/test_expect_column_bootstrapped_ks_test_p_value_to_be_greater_than.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/expect_column_chisquare_test_p_value_to_be_greater_than.json` & `great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/expect_column_chisquare_test_p_value_to_be_greater_than.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_definitions/column_distributional_expectations/expect_column_kl_divergence_to_be_less_than.json` & `great_expectations-0.9.9/tests/test_definitions/column_distributional_expectations/expect_column_kl_divergence_to_be_less_than.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/profile/test_multi_batch_validation_meta_analysis.py` & `great_expectations-0.9.9/tests/profile/test_multi_batch_validation_meta_analysis.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/profile/test_SampleExpectationsDatasetProfiler.py` & `great_expectations-0.9.9/tests/profile/test_SampleExpectationsDatasetProfiler.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/profile/test_profile.py` & `great_expectations-0.9.9/tests/profile/test_profile.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_autoinspect.py` & `great_expectations-0.9.9/tests/test_autoinspect.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/build_index_page.py` & `great_expectations-0.9.9/tests/build_index_page.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/great_expectations.yml` & `great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/great_expectations.yml`

 * *Files 4% similar despite different names*

```diff
@@ -21,15 +21,15 @@
       default:
         class_name: TableBatchKwargsGenerator
 
 # This config file supports variable substitution which enables: 1) keeping
 # secrets out of source control & 2) environment-based configuration changes
 # such as staging vs prod.
 #
-# When GE encounters substitution syntax (like `my_key: ${my_value}` or 
+# When GE encounters substitution syntax (like `my_key: ${my_value}` or
 # `my_key: $my_value`) in the config file it will attempt to replace the value
 # of `my_key` with the value from an environment variable `my_value` or a
 # corresponding key read from the file specified using
 # `config_variables_file_path`. Environment variables take precedence.
 #
 # If the substitution value comes from the config variables file, it can be a
 # simple (non-nested) value or a nested value such as a dictionary. If it comes
@@ -68,15 +68,15 @@
           renderer:
             module_name: great_expectations.render.renderer.slack_renderer
             class_name: SlackRenderer
 stores:
 # Stores are configurable places to store things like Expectations, Validations
 # Data Docs, and more. These are for advanced users only - most users can simply
 # leave this section alone.
-# 
+#
 # Three stores are required: expectations, validations, and
 # evaluation_parameters, and must exist with a valid store entry. Additional
 # stores can be configured for uses such as data_docs, validation_operators, etc.
   expectations_store:
     class_name: ExpectationsStore
     store_backend:
       class_name: TupleFilesystemStoreBackend
@@ -97,13 +97,13 @@
 data_docs_sites:
   # Data Docs make it simple to visualize data quality in your project. These
   # include Expectations, Validations & Profiles. The are built for all
   # Datasources from JSON artifacts in the local repo including validations &
   # profiles from the uncommitted directory. Read more at https://docs.greatexpectations.io/en/latest/features/data_docs.html
   local_site:
     class_name: SiteBuilder
+    show_how_to_buttons: true
     store_backend:
       class_name: TupleFilesystemStoreBackend
       base_directory: uncommitted/data_docs/local_site/
     site_index_builder:
       class_name: DefaultSiteIndexBuilder
-      show_cta_footer: true
```

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/uncommitted/config_variables.yml` & `great_expectations-0.9.9/tests/data_context/fixtures/contexts/incomplete_uncommitted/great_expectations/uncommitted/config_variables.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/invalid_config_version/great_expectations.yml` & `great_expectations-0.9.9/tests/data_context/fixtures/invalid_config_version/great_expectations.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/cluster-paintings.py` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/cluster-paintings.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/elements-by-episode.csv` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/data/bob-ross/elements-by-episode.csv`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/great_expectations.yml` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/great_expectations.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/team_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.html` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.html`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/documentation/local_site/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.html`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.json` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/uncommitted/validations/profiling/data__dir/default/bob-ross/BasicDatasetProfiler.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/warning.json` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/warning.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.json` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/BasicDatasetProfiler.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/quarantine.json` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/quarantine.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/failure.json` & `great_expectations-0.9.9/tests/data_context/fixtures/post_init_project_v0.8.0_A/great_expectations/expectations/data__dir/default/bob-ross/failure.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/invalid_top_level_key/great_expectations.yml` & `great_expectations-0.9.9/tests/data_context/fixtures/invalid_top_level_key/great_expectations.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/old_config_version/great_expectations.yml` & `great_expectations-0.9.9/tests/data_context/fixtures/old_config_version/great_expectations.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/fixtures/version_zero/great_expectations.yml` & `great_expectations-0.9.9/tests/data_context/fixtures/version_zero/great_expectations.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/test_configuration_storage.py` & `great_expectations-0.9.9/tests/data_context/test_configuration_storage.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/test_data_context_resource_identifiers.py` & `great_expectations-0.9.9/tests/data_context/test_data_context_resource_identifiers.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/test_data_context_config_errors.py` & `great_expectations-0.9.9/tests/data_context/test_data_context_config_errors.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/test_data_context.py` & `great_expectations-0.9.9/tests/data_context/test_data_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -170,14 +170,15 @@
             "metric_kwargs_id": {
                 "column=patient_nbr": ["expect_column_unique_value_count_to_be_between.result.observed_value"]
             }
         }],
         'source_patient_data.default': ["expect_table_row_count_to_equal.result.observed_value"]
     }
 
+
 def test_list_datasources(data_context):
     datasources = data_context.list_datasources()
 
     assert OrderedDict(datasources) == OrderedDict([
         {
             'name': 'mydatasource',
             'class_name': 'PandasDatasource'
```

### Comparing `great_expectations-0.9.8/tests/data_context/test_data_context_utils.py` & `great_expectations-0.9.9/tests/data_context/test_data_context_utils.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/store/test_html_site_store.py` & `great_expectations-0.9.9/tests/data_context/store/test_html_site_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/store/test_validations_store.py` & `great_expectations-0.9.9/tests/data_context/store/test_validations_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/store/test_store_backends.py` & `great_expectations-0.9.9/tests/data_context/store/test_store_backends.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/store/test_evaluation_parameter_store.py` & `great_expectations-0.9.9/tests/data_context/store/test_evaluation_parameter_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/store/test_expectations_store.py` & `great_expectations-0.9.9/tests/data_context/store/test_expectations_store.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/test_data_context_store_configs.py` & `great_expectations-0.9.9/tests/data_context/test_data_context_store_configs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/test_data_context_on_teams.py` & `great_expectations-0.9.9/tests/data_context/test_data_context_on_teams.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/test_data_context_config_variables.py` & `great_expectations-0.9.9/tests/data_context/test_data_context_config_variables.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/data_context/conftest.py` & `great_expectations-0.9.9/tests/data_context/conftest.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_suite.py` & `great_expectations-0.9.9/tests/cli/test_suite.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_docs.py` & `great_expectations-0.9.9/tests/cli/test_docs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_project.py` & `great_expectations-0.9.9/tests/cli/test_project.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_init_pandas.py` & `great_expectations-0.9.9/tests/cli/test_init_pandas.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_datasource_pandas.py` & `great_expectations-0.9.9/tests/cli/test_datasource_pandas.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/utils.py` & `great_expectations-0.9.9/tests/cli/utils.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_datasource_sqlite.py` & `great_expectations-0.9.9/tests/cli/test_datasource_sqlite.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_cli.py` & `great_expectations-0.9.9/tests/cli/test_cli.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_validation_operator.py` & `great_expectations-0.9.9/tests/cli/test_validation_operator.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_init_missing_libraries.py` & `great_expectations-0.9.9/tests/cli/test_init_missing_libraries.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_taps_pandas.py` & `great_expectations-0.9.9/tests/cli/test_taps_pandas.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_init_sqlite.py` & `great_expectations-0.9.9/tests/cli/test_init_sqlite.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/cli/test_init.py` & `great_expectations-0.9.9/tests/cli/test_init.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_ge_utils.py` & `great_expectations-0.9.9/tests/test_ge_utils.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/core/test_serialization.py` & `great_expectations-0.9.9/tests/core/test_serialization.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/core/test_expectation_suite.py` & `great_expectations-0.9.9/tests/core/test_expectation_suite.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/core/test_evaluation_parameters.py` & `great_expectations-0.9.9/tests/core/test_evaluation_parameters.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/core/test_expectation_configuration.py` & `great_expectations-0.9.9/tests/core/test_expectation_configuration.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/core/test_expectation_kwargs.py` & `great_expectations-0.9.9/tests/core/test_expectation_kwargs.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/conftest.py` & `great_expectations-0.9.9/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/great_expectations_basic_without_config_variables_filepath.yml` & `great_expectations-0.9.9/tests/test_fixtures/great_expectations_basic_without_config_variables_filepath.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/distributional_expectations_partition_fixtures.py` & `great_expectations-0.9.9/tests/test_fixtures/distributional_expectations_partition_fixtures.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/great_expectations_basic.yml` & `great_expectations-0.9.9/tests/test_fixtures/great_expectations_basic.yml`

 * *Files 2% similar despite different names*

```diff
@@ -26,20 +26,20 @@
 evaluation_parameter_store_name: evaluation_parameter_store
 expectations_store_name: expectations_store
 validations_store_name: validations_store
 
 data_docs_sites:
   local_site:
     class_name: SiteBuilder
+    show_how_to_buttons: true
     store_backend:
       class_name: TupleFilesystemStoreBackend
       base_directory: uncommitted/data_docs/local_site/
     site_index_builder:
       class_name: DefaultSiteIndexBuilder
-      show_cta_footer: true
 
 stores:
   expectations_store:
     class_name: ExpectationsStore
     store_backend:
       class_name: TupleFilesystemStoreBackend
       base_directory: expectations/
```

### Comparing `great_expectations-0.9.8/tests/test_fixtures/custom_pandas_dataset.py` & `great_expectations-0.9.9/tests/test_fixtures/custom_pandas_dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/custom_sqlalchemy_dataset.py` & `great_expectations-0.9.9/tests/test_fixtures/custom_sqlalchemy_dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/custom_sparkdf_dataset.py` & `great_expectations-0.9.9/tests/test_fixtures/custom_sparkdf_dataset.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/fixed_distribution_data.py` & `great_expectations-0.9.9/tests/test_fixtures/fixed_distribution_data.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/expectation_suite_3.json` & `great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/expectation_suite_3.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/evr_suite_3.json` & `great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/evr_suite_3.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/expectations_suite_2.json` & `great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/expectations_suite_2.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/expectations_suite_1.json` & `great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/expectations_suite_1.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/rendering_fixtures/evr_suite_1.json` & `great_expectations-0.9.9/tests/test_fixtures/rendering_fixtures/evr_suite_1.json`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/great_expectations_site_builder.yml` & `great_expectations-0.9.9/tests/test_fixtures/great_expectations_site_builder.yml`

 * *Files 2% similar despite different names*

```diff
@@ -110,14 +110,15 @@
   # "team_site" is meant to support the "shared source of truth for a team" use case.
   # By default only the expectations section is enabled.
   #  Users have to configure the profiling and the validations sections (and the corresponding validations_store and validations_store attributes based on the team's decisions where these are stored (a local filesystem or S3).
   # Reach out on Slack (https://greatexpectations.io/slack>) if you would like to discuss the best way to configure a team site.
 
     module_name: great_expectations.render.renderer.site_builder
     class_name: SiteBuilder
+    show_how_to_buttons: true
     target_store_name: team_site_html_store
 
     site_index_builder:
       class_name: DefaultSiteIndexBuilder
 
     site_section_builders:
       expectations:
```

### Comparing `great_expectations-0.9.8/tests/test_fixtures/expectation_suites/parameterized_expectation_suite_fixture.json` & `great_expectations-0.9.9/tests/test_fixtures/expectation_suites/parameterized_expectation_suite_fixture.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.984375%*

 * *Differences: {"'expectations'": "{1: {'kwargs': {replace: OrderedDict([('min_value', "*

 * *                   "OrderedDict([('$PARAMETER', "*

 * *                   "'urn:great_expectations:validations:source_patient_data.default:expect_table_row_count_to_equal.result.observed_value')]))])}}}"}*

```diff
@@ -9,15 +9,15 @@
                     "$PARAMETER": "urn:great_expectations:validations:source_diabetes_data.default:expect_column_unique_value_count_to_be_between.result.observed_value:column=patient_nbr"
                 }
             }
         },
         {
             "expectation_type": "expect_column_unique_value_count_to_be_between",
             "kwargs": {
-                "value": {
+                "min_value": {
                     "$PARAMETER": "urn:great_expectations:validations:source_patient_data.default:expect_table_row_count_to_equal.result.observed_value"
                 }
             }
         }
     ],
     "meta": {
         "great_expectations.__version__": "0.9.4"
```

### Comparing `great_expectations-0.9.8/tests/test_fixtures/great_expectations_basic_with_variables.yml` & `great_expectations-0.9.9/tests/test_fixtures/great_expectations_basic_with_variables.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_fixtures/great_expectations_titanic.yml` & `great_expectations-0.9.9/tests/test_fixtures/great_expectations_titanic.yml`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/test_utils.py` & `great_expectations-0.9.9/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/actions/test_validation_operators_in_data_context.py` & `great_expectations-0.9.9/tests/actions/test_validation_operators_in_data_context.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,38 +1,48 @@
 import pytest
-import os
-import shutil
-
-import pandas as pd
+import json
 
 from great_expectations.data_context import (
     BaseDataContext,
-    DataContext,
 )
-from great_expectations.util import (
-    gen_directory_tree_str
+from great_expectations.core import (
+    expectationSuiteSchema,
+)
+
+from great_expectations.data_context.util import (
+    file_relative_path,
 )
 
 
+@pytest.fixture()
+def parameterized_expectation_suite():
+    fixture_path = file_relative_path(
+        __file__,
+        "../test_fixtures/expectation_suites/parameterized_expression_expectation_suite_fixture.json",
+    )
+    with open(fixture_path, "r",) as suite:
+        return expectationSuiteSchema.load(json.load(suite))
+
+
 @pytest.fixture
 def validation_operators_data_context(basic_data_context_config_for_validation_operator, filesystem_csv_4):
     data_context = BaseDataContext(
         basic_data_context_config_for_validation_operator
     )
 
     data_context.add_datasource("my_datasource",
                                 class_name="PandasDatasource",
                                 generators={
                                     "subdir_reader": {
                                         "class_name": "SubdirReaderBatchKwargsGenerator",
                                         "base_directory": str(filesystem_csv_4)
                                     }
                                 })
-
     data_context.create_expectation_suite("f1.foo")
+
     df = data_context.get_batch(batch_kwargs=data_context.build_batch_kwargs("my_datasource",
                                                                              "subdir_reader", "f1"),
                                 expectation_suite_name="f1.foo")
     df.expect_column_values_to_be_between(column="x", min_value=1, max_value=9)
     failure_expectations = df.get_expectation_suite(discard_failed_expectations=False)
 
     df.expect_column_values_to_not_be_null(column="y")
@@ -40,28 +50,62 @@
 
     data_context.save_expectation_suite(failure_expectations, expectation_suite_name="f1.failure")
     data_context.save_expectation_suite(warning_expectations, expectation_suite_name="f1.warning")
 
     return data_context
 
 
+def test_validation_operator_evaluation_parameters(validation_operators_data_context, parameterized_expectation_suite):
+    validation_operators_data_context.save_expectation_suite(parameterized_expectation_suite, "param_suite")
+    res = validation_operators_data_context.run_validation_operator(
+        "store_val_res_and_extract_eval_params",
+        assets_to_validate=[
+            (
+                validation_operators_data_context.build_batch_kwargs("my_datasource", "subdir_reader", "f1"),
+                "param_suite"
+            )
+        ],
+        evaluation_parameters={
+            "urn:great_expectations:validations:source_patient_data.default:expect_table_row_count_to_equal.result"
+            ".observed_value": 3
+        }
+    )
+    assert res["success"] is True
+
+    res = validation_operators_data_context.run_validation_operator(
+        "store_val_res_and_extract_eval_params",
+        assets_to_validate=[
+            (
+                validation_operators_data_context.build_batch_kwargs("my_datasource", "subdir_reader", "f1"),
+                "param_suite"
+            )
+        ],
+        evaluation_parameters={
+            "urn:great_expectations:validations:source_patient_data.default:expect_table_row_count_to_equal.result"
+            ".observed_value": 10
+        }
+    )
+    assert res["success"] is False
+
+
 def test_action_list_operator(validation_operators_data_context):
     data_context = validation_operators_data_context
     validator_batch_kwargs = data_context.build_batch_kwargs("my_datasource", "subdir_reader", "f1")
 
     batch = data_context.get_batch(expectation_suite_name="f1.failure",
                                    batch_kwargs=validator_batch_kwargs
                                    )
 
     assert data_context.stores["validation_result_store"].list_keys() == []
     # We want to demonstrate running the validation operator with both a pre-built batch (DataAsset) and with
     # a tuple of parameters for get_batch
     operator_result = data_context.run_validation_operator(
         assets_to_validate=[batch, (validator_batch_kwargs, "f1.warning")],
         run_id="test-100",
+        evaluation_parameters={},
         validation_operator_name="store_val_res_and_extract_eval_params",
     )
     # results = data_context.run_validation_operator(my_ge_df)
 
     validation_result_store_keys = data_context.stores["validation_result_store"].list_keys()
     print(validation_result_store_keys)
     assert len(validation_result_store_keys) == 2
```

### Comparing `great_expectations-0.9.8/tests/actions/test_core_actions.py` & `great_expectations-0.9.9/tests/actions/test_core_actions.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/actions/conftest.py` & `great_expectations-0.9.9/tests/actions/conftest.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/actions/test_store_metric_action.py` & `great_expectations-0.9.9/tests/actions/test_store_metric_action.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/actions/test_validation_operators.py` & `great_expectations-0.9.9/tests/actions/test_validation_operators.py`

 * *Files identical despite different names*

### Comparing `great_expectations-0.9.8/tests/jupyter_ux/test_jupyter_ux.py` & `great_expectations-0.9.9/tests/jupyter_ux/test_jupyter_ux.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,21 +1,23 @@
 import logging
+import pytest
 
 import great_expectations as ge
 import great_expectations.jupyter_ux as jux
 
 
 def test_styling_elements_exist():
     assert "<link" in jux.bootstrap_link_element
     assert "bootstrap" in jux.bootstrap_link_element
 
     assert jux.cooltip_style_element[:23] == '<style type="text/css">'
     assert ".cooltip" in jux.cooltip_style_element
 
 
+
 def test_display_column_expectations_as_section(basic_expectation_suite):
     html_to_display = jux.display_column_expectations_as_section(
         basic_expectation_suite,
         "naturals",
         include_styling=False,
         return_without_displaying=True
     )
@@ -147,14 +149,32 @@
             </li>
 </ul>
 </div>
     </div>
 </div>
 """.replace(" ", "").replace("\t", "").replace("\n", "")
 
+@pytest.mark.smoketest
+def test_display_profiled_column_evrs_as_section(titanic_profiled_evrs_1):
+    section_html = jux.display_profiled_column_evrs_as_section(
+        titanic_profiled_evrs_1,
+        "SexCode",
+        include_styling=False,
+        return_without_displaying=True
+    )
+
+@pytest.mark.smoketest
+def test_display_column_evrs_as_section(titanic_profiled_evrs_1):
+    section_html = jux.display_column_evrs_as_section(
+        titanic_profiled_evrs_1,
+        "SexCode",
+        include_styling=False,
+        return_without_displaying=True
+    )
+
 
 def test_configure_logging(caplog):
     # First, ensure we set the root logger to close-to-jupyter settings (only show warnings)
     caplog.set_level(logging.WARNING)
     caplog.set_level(logging.WARNING, logger="great_expectations")
 
     root = logging.getLogger()  # root logger
```

