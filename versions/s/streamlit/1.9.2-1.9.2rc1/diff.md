# Comparing `tmp/streamlit-1.9.2.tar.gz` & `tmp/streamlit-1.9.2rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "streamlit-1.9.2.tar", last modified: Fri May 27 18:22:08 2022, max compression
+gzip compressed data, was "streamlit-1.9.2rc1.tar", last modified: Fri May 27 18:06:21 2022, max compression
```

## Comparing `streamlit-1.9.2.tar` & `streamlit-1.9.2rc1.tar`

### file list

```diff
@@ -1,392 +1,392 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:08.027270 streamlit-1.9.2/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      108 2022-05-27 18:08:01.000000 streamlit-1.9.2/MANIFEST.in
--rw-r--r--   0 circleci  (3434) circleci  (3434)      526 2022-05-27 18:22:08.027270 streamlit-1.9.2/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1797 2022-05-27 18:08:01.000000 streamlit-1.9.2/Pipfile
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.919269 streamlit-1.9.2/bin/
--rw-r--r--   0 circleci  (3434) circleci  (3434)       33 2022-05-27 18:08:01.000000 streamlit-1.9.2/bin/streamlit.cmd
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2022-05-27 18:22:08.027270 streamlit-1.9.2/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3201 2022-05-27 18:14:28.000000 streamlit-1.9.2/setup.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.927269 streamlit-1.9.2/streamlit/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    15616 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      841 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/__main__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    24711 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/app_session.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4062 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/beta_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12575 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/bootstrap.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.927269 streamlit-1.9.2/streamlit/caching/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1560 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/caching/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3426 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/caching/cache_errors.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11558 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/caching/cache_utils.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12558 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/caching/hashing.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16779 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/caching/memo_decorator.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9718 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/caching/singleton_decorator.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2229 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/case_converters.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9854 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/cli.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2255 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/code_util.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.927269 streamlit-1.9.2/streamlit/commands/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/commands/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9725 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/commands/page_config.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.927269 streamlit-1.9.2/streamlit/components/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/components/__init__.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.927269 streamlit-1.9.2/streamlit/components/v1/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      979 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/components/v1/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10869 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/components/v1/component_arrow.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    15672 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/components/v1/components.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    34098 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/config.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10503 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/config_option.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3898 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/config_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8600 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/credentials.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5951 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/cursor.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    28766 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/delta_generator.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      779 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/development.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3806 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/echo.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.939269 streamlit-1.9.2/streamlit/elements/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2963 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/alert.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12704 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/arrow.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12724 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/arrow_altair.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6374 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/arrow_vega_lite.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1237 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/balloons.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3542 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/bokeh_chart.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13754 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/button.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7898 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/camera_input.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5268 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/checkbox.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6244 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/color_picker.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16974 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/dataframe_selector.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4213 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/deck_gl_json_chart.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4607 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/doc_string.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2446 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/empty.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8968 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/exception.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    14542 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/file_uploader.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9356 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/form.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4080 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/graphviz_chart.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4084 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/iframe.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12942 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/image.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2779 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/json.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9229 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/layouts.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12021 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/legacy_altair.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16727 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/legacy_data_frame.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6286 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/legacy_vega_lite.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.939269 streamlit-1.9.2/streamlit/elements/lib/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/lib/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3350 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/lib/dicttools.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6251 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/map.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9438 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/markdown.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8922 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/media.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7358 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/metric.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8602 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/multiselect.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11530 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/number_input.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6671 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/plotly_chart.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2386 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/progress.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5661 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/pyplot.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6840 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/radio.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9098 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/select_slider.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6756 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/selectbox.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    20262 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/slider.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1198 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/snow.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1395 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/text.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12862 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/text_widgets.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13643 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/time_widgets.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2650 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/utils.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9232 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/elements/write.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1722 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/env_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1507 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/error_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3295 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/errors.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5848 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/file_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2321 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/folder_black_list.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8766 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/forward_msg_cache.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5510 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/forward_msg_queue.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5200 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/git_util.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.939269 streamlit-1.9.2/streamlit/hello/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/hello/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8798 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/hello/demos.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2935 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/hello/hello.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11090 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/in_memory_file_manager.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3591 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/js_number.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.939269 streamlit-1.9.2/streamlit/legacy_caching/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      830 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/legacy_caching/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    25025 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/legacy_caching/caching.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    35383 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/legacy_caching/hashing.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3801 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/logger.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5563 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/magic.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2372 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/metrics_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2960 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/net_util.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.951269 streamlit-1.9.2/streamlit/proto/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3854 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Alert_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3282 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/ArrowNamedDataSet_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4173 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/ArrowVegaLiteChart_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4916 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Arrow_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2435 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Audio_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6014 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/BackMsg_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1993 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Balloons_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11785 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Block_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2922 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/BokehChart_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4602 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Button_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3785 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/CameraInput_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5048 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Checkbox_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2819 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/ClientState_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5138 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/ColorPicker_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12039 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Common_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    14749 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Components_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    32146 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/DataFrame_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6369 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/DateInput_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3010 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/DeckGlJsonChart_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5385 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Delta_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3764 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/DocString_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4738 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/DownloadButton_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    40666 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Element_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1476 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Empty_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3782 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Exception_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1944 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Favicon_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5185 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/FileUploader_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16133 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/ForwardMsg_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5383 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/GitInfo_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3012 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/GraphVizChart_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4633 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/IFrame_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4509 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Image_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2334 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Json_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2846 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Markdown_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5997 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Metric_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5537 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/MultiSelect_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3210 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/NamedDataSet_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    21092 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/NewSession_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9283 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/NumberInput_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9326 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/PageConfig_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1978 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/PageInfo_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5230 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/PlotlyChart_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1941 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Progress_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5394 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Radio_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1760 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/RootContainer_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5488 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Selectbox_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4305 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/SessionEvent_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2499 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/SessionState_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9129 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Slider_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1884 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Snow_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1941 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Spinner_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6391 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/TextArea_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7810 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/TextInput_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1896 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Text_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5090 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/TimeInput_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4048 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/VegaLiteChart_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3953 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/Video_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12593 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/WidgetStates_pb2.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      634 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/proto/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    45888 2022-05-27 18:14:38.000000 streamlit-1.9.2/streamlit/proto/openmetrics_data_model_pb2.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.951269 streamlit-1.9.2/streamlit/scriptrunner/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1034 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/scriptrunner/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6786 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/scriptrunner/script_requests.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5312 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/scriptrunner/script_run_context.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    22274 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/scriptrunner/script_runner.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8523 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/secrets.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.951269 streamlit-1.9.2/streamlit/server/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/server/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10180 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/server/routes.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    28573 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/server/server.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5619 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/server/server_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6192 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/server/upload_file_request_handler.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3734 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/session_data.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1225 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/source_util.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.955270 streamlit-1.9.2/streamlit/state/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1254 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/state/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4287 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/state/safe_session_state.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    24504 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/state/session_state.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4800 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/state/session_state_proxy.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10075 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/state/widgets.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.955270 streamlit-1.9.2/streamlit/static/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6730 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/asset-manifest.json
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.955270 streamlit-1.9.2/streamlit/static/assets/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    20638 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/assets/streamlit.css
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1019 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/favicon.png
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5374 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/index.html
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.915269 streamlit-1.9.2/streamlit/static/static/
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.955270 streamlit-1.9.2/streamlit/static/static/css/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    24409 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/css/5.71be5c0a.chunk.css
--rw-r--r--   0 circleci  (3434) circleci  (3434)    33703 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/css/7.f5138d60.chunk.css
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3661 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/css/main.b46f6fce.chunk.css
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.995270 streamlit-1.9.2/streamlit/static/static/js/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    19618 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/0.82d9d691.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)  1106924 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/1.41cbec15.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      941 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/1.41cbec15.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7727 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/10.62d2acd1.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/10.62d2acd1.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4869 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/11.5dd372e4.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    66190 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/12.75ba938f.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2550 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/13.640099b2.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    28968 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/14.dec27756.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1303 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/15.bb36f352.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/15.bb36f352.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)    14835 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/16.e0ff5a83.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/16.e0ff5a83.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)    86183 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/17.55bdd533.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7527 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/18.417e7db5.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/18.417e7db5.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8023 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/19.a97d3788.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    78469 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/2.dbd55c92.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12856 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/20.14a753ba.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/20.14a753ba.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)    14638 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/21.81da819e.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/21.81da819e.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)  3681397 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/22.4e054289.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1672 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/22.4e054289.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1710 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/23.e332c265.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/23.e332c265.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8296 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/24.9cf6cd9f.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    21569 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/25.7a23db90.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8783 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/26.6c854743.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/26.6c854743.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6399 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/27.bb14fa54.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/27.bb14fa54.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      570 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/28.55fc8575.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/28.55fc8575.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1141 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/29.e5d8f8cc.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/29.e5d8f8cc.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7675 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/30.a6f46ad4.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/30.a6f46ad4.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      630 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/31.0f4d42f4.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/31.0f4d42f4.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1363 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/32.ec76442a.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/32.ec76442a.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1021 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/33.c16196fe.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/33.c16196fe.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6517 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/34.194522d6.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/34.194522d6.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      935 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/35.fae54e30.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/35.fae54e30.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      620 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/36.1b75579f.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/36.1b75579f.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)    15871 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/37.5ab35022.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1924 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/38.04f3f7d8.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3609 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/39.4da3a545.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      817 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/40.6f9ef4f3.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/40.6f9ef4f3.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)    18009 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/41.95bd87e1.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1954 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/42.810f434c.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6031 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/43.b19a8746.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2536 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/44.a6ccee7a.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)  7752101 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/5.26b8f29c.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6571 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/5.26b8f29c.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)  2881259 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/6.7ec31925.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      487 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/6.7ec31925.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)  2963976 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/7.85ba4e86.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2011 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/7.85ba4e86.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)   155909 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/8.d6b4540e.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)       85 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/8.d6b4540e.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)  2386447 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/9.568f55f3.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)   605474 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/main.970d3503.chunk.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1231 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/main.970d3503.chunk.js.LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4334 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/js/runtime-main.9ba163f1.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:08.015270 streamlit-1.9.2/streamlit/static/static/media/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    28076 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_AMS-Regular.73ea273a.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    63632 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_AMS-Regular.853be924.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    33516 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_AMS-Regular.d562e886.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12368 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Bold.7489a2fb.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6912 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Bold.a1abf90d.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7716 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Bold.d757c535.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12344 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Regular.7e873d38.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6908 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Regular.d6484fce.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7656 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Regular.db074fa2.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13296 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Bold.354501ba.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    19584 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Bold.4c761b37.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11348 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Bold.931d67ea.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11316 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Regular.172d3529.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13208 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Regular.6fdf0ac5.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    19572 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Regular.ed305b54.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    29912 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Bold.0c3b8929.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    25324 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Bold.39890742.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    51336 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Bold.8169508b.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16780 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-BoldItalic.20f389c4.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    19412 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-BoldItalic.428978dc.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    32968 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-BoldItalic.828abcb2.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    33580 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Italic.fa675e5e.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    19676 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Italic.fd947498.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16988 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Italic.fe2176f7.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    30772 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Regular.4f35fbcc.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    53580 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Regular.9eba1d77.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    26272 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Regular.f650f111.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    18668 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-BoldItalic.3f07ed67.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    31196 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-BoldItalic.bf2d440b.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16400 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-BoldItalic.dcbcbd93.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16440 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-Italic.6d3d25f4.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    31308 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-Italic.8a5f9363.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    18748 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-Italic.96759856.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    24504 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Bold.5b49f499.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12216 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Bold.95591a92.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    14408 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Bold.b9cd458a.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12028 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Italic.7d393d38.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    14112 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Italic.8d593cfa.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    22364 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Italic.b257a18c.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12316 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Regular.02271ec5.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    19436 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Regular.2f7bc363.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10344 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Regular.cd5e231e.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10588 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Script-Regular.073b3402.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9644 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Script-Regular.c81d1b2a.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16648 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Script-Regular.fc9ba524.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6496 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size1-Regular.0108e89c.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12228 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size1-Regular.6de7d4b5.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5468 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size1-Regular.6eec866c.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5208 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size2-Regular.2960900c.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6188 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size2-Regular.3a99e70a.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11508 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size2-Regular.57f5c183.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4420 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size3-Regular.7947224e.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7588 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size3-Regular.8d6b6822.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3624 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size3-Regular.e1951519.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10364 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size4-Regular.4ad7c7e8.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5980 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size4-Regular.aeffd802.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4928 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size4-Regular.e418bf25.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16028 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Typewriter-Regular.4c6b94fd.woff
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13568 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Typewriter-Regular.c295e7f7.woff2
--rw-r--r--   0 circleci  (3434) circleci  (3434)    27556 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/KaTeX_Typewriter-Regular.c5c02d76.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   191568 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-Bold.52ac8f30.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   155288 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-BoldItalic.05b61807.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   161376 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-Italic.454577c2.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   192740 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-Regular.70cc7ff2.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   191792 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-SemiBold.4d4c53c0.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   155568 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-SemiBoldItalic.2f5470bc.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   267388 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-Bold.12e6acd2.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    94132 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-BoldItalic.7c4f9b00.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    94816 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-Italic.3c01996d.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   269108 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-Regular.efa76f83.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   268280 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-SemiBold.43cc81b4.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    94512 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-SemiBoldItalic.c30987e2.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   229740 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-Bold.bada4fe1.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   172748 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-BoldItalic.9f9b1eb2.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   169568 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-Italic.90931d6a.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   226812 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-Regular.6f22301c.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   229596 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-SemiBold.b27cb117.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)   172816 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-SemiBoldItalic.1266f2c1.ttf
--rw-r--r--   0 circleci  (3434) circleci  (3434)    73528 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/flake-0.beded754.png
--rw-r--r--   0 circleci  (3434) circleci  (3434)    86179 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/flake-1.8077dc15.png
--rw-r--r--   0 circleci  (3434) circleci  (3434)    92182 2022-05-27 18:21:57.000000 streamlit-1.9.2/streamlit/static/static/media/flake-2.e3f07d06.png
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.915269 streamlit-1.9.2/streamlit/static/vendor/
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:08.019270 streamlit-1.9.2/streamlit/static/vendor/bokeh/
--rw-r--r--   0 circleci  (3434) circleci  (3434)   799179 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-2.4.1.min.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    88828 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-api-2.4.1.min.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)   185643 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-gl-2.4.1.min.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)  1756732 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-mathjax-2.4.1.min.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)   292438 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-tables-2.4.1.min.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)   251390 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-widgets-2.4.1.min.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:08.027270 streamlit-1.9.2/streamlit/static/vendor/viz/
--rw-r--r--   0 circleci  (3434) circleci  (3434)  7055772 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/viz/viz-1.8.0.min.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1063 2022-05-27 18:14:49.000000 streamlit-1.9.2/streamlit/static/vendor/viz/viz.js-LICENSE.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5322 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/stats.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3525 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/string_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1566 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/temporary_directory.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10575 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/type_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10904 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/uploaded_file_manager.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2259 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/url_util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4040 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/util.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3147 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/version.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:08.027270 streamlit-1.9.2/streamlit/watcher/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      815 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/watcher/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13598 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/watcher/event_based_path_watcher.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7372 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/watcher/local_sources_watcher.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5665 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/watcher/path_watcher.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3552 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/watcher/polling_path_watcher.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5106 2022-05-27 18:08:01.000000 streamlit-1.9.2/streamlit/watcher/util.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:22:07.927269 streamlit-1.9.2/streamlit.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      526 2022-05-27 18:22:06.000000 streamlit-1.9.2/streamlit.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)    15730 2022-05-27 18:22:06.000000 streamlit-1.9.2/streamlit.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-05-27 18:22:06.000000 streamlit-1.9.2/streamlit.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       50 2022-05-27 18:22:06.000000 streamlit-1.9.2/streamlit.egg-info/entry_points.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-05-27 18:14:46.000000 streamlit-1.9.2/streamlit.egg-info/not-zip-safe
--rw-r--r--   0 circleci  (3434) circleci  (3434)      331 2022-05-27 18:22:06.000000 streamlit-1.9.2/streamlit.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       10 2022-05-27 18:22:06.000000 streamlit-1.9.2/streamlit.egg-info/top_level.txt
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.098960 streamlit-1.9.2rc1/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      108 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/MANIFEST.in
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      529 2022-05-27 18:06:21.098960 streamlit-1.9.2rc1/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1797 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/Pipfile
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.026959 streamlit-1.9.2rc1/bin/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       33 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/bin/streamlit.cmd
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2022-05-27 18:06:21.098960 streamlit-1.9.2rc1/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3204 2022-05-27 17:58:46.000000 streamlit-1.9.2rc1/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.030959 streamlit-1.9.2rc1/streamlit/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    15616 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      841 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/__main__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    24711 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/app_session.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4062 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/beta_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12575 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/bootstrap.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.034959 streamlit-1.9.2rc1/streamlit/caching/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1560 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/caching/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3426 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/caching/cache_errors.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11558 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/caching/cache_utils.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12558 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/caching/hashing.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16779 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/caching/memo_decorator.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9718 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/caching/singleton_decorator.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2229 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/case_converters.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9854 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/cli.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2255 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/code_util.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.034959 streamlit-1.9.2rc1/streamlit/commands/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/commands/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9725 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/commands/page_config.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.034959 streamlit-1.9.2rc1/streamlit/components/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/components/__init__.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.034959 streamlit-1.9.2rc1/streamlit/components/v1/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      979 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/components/v1/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10869 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/components/v1/component_arrow.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    15672 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/components/v1/components.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    34098 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/config.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10503 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/config_option.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3898 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/config_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8600 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/credentials.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5951 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/cursor.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    28766 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/delta_generator.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      779 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/development.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3806 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/echo.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.038959 streamlit-1.9.2rc1/streamlit/elements/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2963 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/alert.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12704 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/arrow.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12724 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/arrow_altair.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6374 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/arrow_vega_lite.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1237 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/balloons.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3542 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/bokeh_chart.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13754 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/button.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7898 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/camera_input.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5268 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/checkbox.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6244 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/color_picker.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16974 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/dataframe_selector.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4213 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/deck_gl_json_chart.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4607 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/doc_string.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2446 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/empty.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8968 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/exception.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    14542 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/file_uploader.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9356 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/form.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4080 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/graphviz_chart.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4084 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/iframe.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12942 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/image.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2779 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/json.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9229 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/layouts.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12021 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/legacy_altair.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16727 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/legacy_data_frame.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6286 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/legacy_vega_lite.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.038959 streamlit-1.9.2rc1/streamlit/elements/lib/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/lib/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3350 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/lib/dicttools.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6251 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/map.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9438 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/markdown.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8922 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/media.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7358 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/metric.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8602 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/multiselect.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11530 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/number_input.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6671 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/plotly_chart.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2386 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/progress.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5661 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/pyplot.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6840 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/radio.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9098 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/select_slider.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6756 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/selectbox.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    20262 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/slider.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1198 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/snow.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1395 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/text.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12862 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/text_widgets.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13643 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/time_widgets.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2650 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/utils.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9232 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/elements/write.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1722 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/env_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1507 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/error_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3295 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/errors.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5848 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/file_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2321 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/folder_black_list.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8766 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/forward_msg_cache.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5510 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/forward_msg_queue.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5200 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/git_util.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.038959 streamlit-1.9.2rc1/streamlit/hello/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/hello/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8798 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/hello/demos.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2935 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/hello/hello.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11090 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/in_memory_file_manager.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3591 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/js_number.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.038959 streamlit-1.9.2rc1/streamlit/legacy_caching/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      830 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/legacy_caching/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    25025 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/legacy_caching/caching.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    35383 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/legacy_caching/hashing.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3801 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/logger.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5563 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/magic.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2372 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/metrics_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2960 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/net_util.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.046959 streamlit-1.9.2rc1/streamlit/proto/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3854 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Alert_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3282 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/ArrowNamedDataSet_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4173 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/ArrowVegaLiteChart_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4916 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Arrow_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2435 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Audio_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6014 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/BackMsg_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1993 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Balloons_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11785 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Block_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2922 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/BokehChart_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4602 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Button_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3785 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/CameraInput_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5048 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Checkbox_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2819 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/ClientState_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5138 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/ColorPicker_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12039 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Common_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    14749 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Components_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    32146 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/DataFrame_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6369 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/DateInput_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3010 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/DeckGlJsonChart_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5385 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Delta_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3764 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/DocString_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4738 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/DownloadButton_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    40666 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Element_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1476 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Empty_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3782 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Exception_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1944 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Favicon_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5185 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/FileUploader_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16133 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/ForwardMsg_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5383 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/GitInfo_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3012 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/GraphVizChart_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4633 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/IFrame_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4509 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Image_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2334 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Json_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2846 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Markdown_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5997 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Metric_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5537 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/MultiSelect_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3210 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/NamedDataSet_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    21092 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/NewSession_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9283 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/NumberInput_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9326 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/PageConfig_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1978 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/PageInfo_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5230 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/PlotlyChart_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1941 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Progress_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5394 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Radio_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1760 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/RootContainer_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5488 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Selectbox_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4305 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/SessionEvent_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2499 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/SessionState_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9129 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Slider_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1884 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Snow_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1941 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Spinner_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6391 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/TextArea_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7810 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/TextInput_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1896 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Text_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5090 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/TimeInput_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4048 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/VegaLiteChart_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3953 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/Video_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12593 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/WidgetStates_pb2.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      634 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/proto/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    45888 2022-05-27 17:58:57.000000 streamlit-1.9.2rc1/streamlit/proto/openmetrics_data_model_pb2.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.046959 streamlit-1.9.2rc1/streamlit/scriptrunner/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1034 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/scriptrunner/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6786 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/scriptrunner/script_requests.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5312 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/scriptrunner/script_run_context.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    22274 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/scriptrunner/script_runner.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8523 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/secrets.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.046959 streamlit-1.9.2rc1/streamlit/server/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      582 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/server/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10180 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/server/routes.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    28573 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/server/server.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5619 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/server/server_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6192 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/server/upload_file_request_handler.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3734 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/session_data.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1225 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/source_util.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.050959 streamlit-1.9.2rc1/streamlit/state/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1254 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/state/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4287 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/state/safe_session_state.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    24504 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/state/session_state.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4800 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/state/session_state_proxy.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10075 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/state/widgets.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.050959 streamlit-1.9.2rc1/streamlit/static/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6730 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/asset-manifest.json
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.050959 streamlit-1.9.2rc1/streamlit/static/assets/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    20638 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/assets/streamlit.css
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1019 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/favicon.png
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5374 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/index.html
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.026959 streamlit-1.9.2rc1/streamlit/static/static/
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.050959 streamlit-1.9.2rc1/streamlit/static/static/css/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    24409 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/css/5.71be5c0a.chunk.css
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    33703 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/css/7.f5138d60.chunk.css
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3661 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/css/main.b46f6fce.chunk.css
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.074960 streamlit-1.9.2rc1/streamlit/static/static/js/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    19618 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/0.82d9d691.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  1106924 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/1.41cbec15.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      941 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/1.41cbec15.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7727 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/10.62d2acd1.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/10.62d2acd1.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4869 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/11.5dd372e4.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    66190 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/12.75ba938f.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2550 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/13.640099b2.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    28968 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/14.dec27756.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1303 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/15.bb36f352.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/15.bb36f352.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    14835 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/16.e0ff5a83.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/16.e0ff5a83.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    86183 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/17.55bdd533.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7527 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/18.417e7db5.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/18.417e7db5.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8023 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/19.a97d3788.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    78469 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/2.dbd55c92.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12856 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/20.14a753ba.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/20.14a753ba.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    14638 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/21.81da819e.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/21.81da819e.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  3681397 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/22.4e054289.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1672 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/22.4e054289.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1710 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/23.e332c265.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/23.e332c265.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8296 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/24.9cf6cd9f.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    21569 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/25.7a23db90.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8783 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/26.6c854743.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/26.6c854743.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6399 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/27.bb14fa54.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/27.bb14fa54.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      570 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/28.55fc8575.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/28.55fc8575.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1141 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/29.e5d8f8cc.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/29.e5d8f8cc.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7675 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/30.a6f46ad4.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/30.a6f46ad4.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      630 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/31.0f4d42f4.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/31.0f4d42f4.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1363 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/32.ec76442a.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/32.ec76442a.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1021 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/33.c16196fe.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/33.c16196fe.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6517 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/34.194522d6.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/34.194522d6.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      935 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/35.fae54e30.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/35.fae54e30.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      620 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/36.1b75579f.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/36.1b75579f.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    15871 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/37.5ab35022.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1924 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/38.04f3f7d8.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3609 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/39.4da3a545.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      817 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/40.6f9ef4f3.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      615 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/40.6f9ef4f3.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    18009 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/41.95bd87e1.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1954 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/42.810f434c.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6031 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/43.b19a8746.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2536 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/44.a6ccee7a.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  7752101 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/5.26b8f29c.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6571 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/5.26b8f29c.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  2881259 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/6.7ec31925.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      487 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/6.7ec31925.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  2963976 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/7.85ba4e86.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2011 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/7.85ba4e86.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   155909 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/8.d6b4540e.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       85 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/8.d6b4540e.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  2386447 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/9.568f55f3.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   605474 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/main.970d3503.chunk.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1231 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/main.970d3503.chunk.js.LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4334 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/js/runtime-main.9ba163f1.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.090960 streamlit-1.9.2rc1/streamlit/static/static/media/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    28076 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_AMS-Regular.73ea273a.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    63632 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_AMS-Regular.853be924.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    33516 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_AMS-Regular.d562e886.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12368 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Bold.7489a2fb.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6912 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Bold.a1abf90d.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7716 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Bold.d757c535.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12344 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Regular.7e873d38.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6908 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Regular.d6484fce.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7656 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Regular.db074fa2.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13296 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Bold.354501ba.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    19584 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Bold.4c761b37.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11348 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Bold.931d67ea.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11316 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Regular.172d3529.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13208 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Regular.6fdf0ac5.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    19572 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Regular.ed305b54.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    29912 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Bold.0c3b8929.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    25324 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Bold.39890742.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    51336 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Bold.8169508b.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16780 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-BoldItalic.20f389c4.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    19412 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-BoldItalic.428978dc.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    32968 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-BoldItalic.828abcb2.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    33580 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Italic.fa675e5e.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    19676 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Italic.fd947498.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16988 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Italic.fe2176f7.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    30772 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Regular.4f35fbcc.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    53580 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Regular.9eba1d77.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    26272 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Regular.f650f111.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    18668 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-BoldItalic.3f07ed67.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    31196 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-BoldItalic.bf2d440b.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16400 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-BoldItalic.dcbcbd93.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16440 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-Italic.6d3d25f4.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    31308 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-Italic.8a5f9363.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    18748 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-Italic.96759856.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    24504 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Bold.5b49f499.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12216 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Bold.95591a92.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    14408 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Bold.b9cd458a.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12028 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Italic.7d393d38.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    14112 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Italic.8d593cfa.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    22364 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Italic.b257a18c.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12316 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Regular.02271ec5.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    19436 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Regular.2f7bc363.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10344 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Regular.cd5e231e.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10588 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Script-Regular.073b3402.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9644 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Script-Regular.c81d1b2a.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16648 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Script-Regular.fc9ba524.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6496 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size1-Regular.0108e89c.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12228 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size1-Regular.6de7d4b5.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5468 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size1-Regular.6eec866c.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5208 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size2-Regular.2960900c.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6188 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size2-Regular.3a99e70a.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11508 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size2-Regular.57f5c183.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4420 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size3-Regular.7947224e.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7588 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size3-Regular.8d6b6822.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3624 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size3-Regular.e1951519.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10364 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size4-Regular.4ad7c7e8.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5980 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size4-Regular.aeffd802.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4928 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size4-Regular.e418bf25.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16028 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Typewriter-Regular.4c6b94fd.woff
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13568 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Typewriter-Regular.c295e7f7.woff2
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    27556 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Typewriter-Regular.c5c02d76.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   191568 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-Bold.52ac8f30.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   155288 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-BoldItalic.05b61807.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   161376 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-Italic.454577c2.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   192740 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-Regular.70cc7ff2.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   191792 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-SemiBold.4d4c53c0.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   155568 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-SemiBoldItalic.2f5470bc.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   267388 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-Bold.12e6acd2.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    94132 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-BoldItalic.7c4f9b00.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    94816 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-Italic.3c01996d.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   269108 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-Regular.efa76f83.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   268280 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-SemiBold.43cc81b4.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    94512 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-SemiBoldItalic.c30987e2.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   229740 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-Bold.bada4fe1.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   172748 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-BoldItalic.9f9b1eb2.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   169568 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-Italic.90931d6a.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   226812 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-Regular.6f22301c.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   229596 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-SemiBold.b27cb117.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   172816 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-SemiBoldItalic.1266f2c1.ttf
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    73528 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/flake-0.beded754.png
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    86179 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/flake-1.8077dc15.png
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    92182 2022-05-27 18:06:10.000000 streamlit-1.9.2rc1/streamlit/static/static/media/flake-2.e3f07d06.png
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.026959 streamlit-1.9.2rc1/streamlit/static/vendor/
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.094961 streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   799179 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-2.4.1.min.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    88828 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-api-2.4.1.min.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   185643 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-gl-2.4.1.min.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  1756732 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-mathjax-2.4.1.min.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   292438 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-tables-2.4.1.min.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   251390 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-widgets-2.4.1.min.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.098960 streamlit-1.9.2rc1/streamlit/static/vendor/viz/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)  7055772 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/viz/viz-1.8.0.min.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1063 2022-05-27 17:59:09.000000 streamlit-1.9.2rc1/streamlit/static/vendor/viz/viz.js-LICENSE.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5322 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/stats.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3525 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/string_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1566 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/temporary_directory.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10575 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/type_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10904 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/uploaded_file_manager.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2259 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/url_util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4040 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/util.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3147 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/version.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.098960 streamlit-1.9.2rc1/streamlit/watcher/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      815 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/watcher/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13598 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/watcher/event_based_path_watcher.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7372 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/watcher/local_sources_watcher.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5665 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/watcher/path_watcher.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3552 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/watcher/polling_path_watcher.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5106 2022-05-27 17:54:24.000000 streamlit-1.9.2rc1/streamlit/watcher/util.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-05-27 18:06:21.030959 streamlit-1.9.2rc1/streamlit.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      529 2022-05-27 18:06:19.000000 streamlit-1.9.2rc1/streamlit.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    15730 2022-05-27 18:06:19.000000 streamlit-1.9.2rc1/streamlit.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-05-27 18:06:19.000000 streamlit-1.9.2rc1/streamlit.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       50 2022-05-27 18:06:19.000000 streamlit-1.9.2rc1/streamlit.egg-info/entry_points.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-05-27 17:59:05.000000 streamlit-1.9.2rc1/streamlit.egg-info/not-zip-safe
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      331 2022-05-27 18:06:19.000000 streamlit-1.9.2rc1/streamlit.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       10 2022-05-27 18:06:19.000000 streamlit-1.9.2rc1/streamlit.egg-info/top_level.txt
```

### Comparing `streamlit-1.9.2/PKG-INFO` & `streamlit-1.9.2rc1/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: streamlit
-Version: 1.9.2
+Version: 1.9.2rc1
 Summary: The fastest way to build data apps in Python
 Home-page: https://streamlit.io
 Author: Streamlit Inc
 Author-email: hello@streamlit.io
 License: Apache 2
 Project-URL: Source, https://github.com/streamlit/streamlit
 Description: Streamlit's open-source app framework is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours! All in pure Python. All for free.
```

### Comparing `streamlit-1.9.2/Pipfile` & `streamlit-1.9.2rc1/Pipfile`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/setup.py` & `streamlit-1.9.2rc1/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -30,15 +30,15 @@
         from pipenv.utils import convert_deps_to_pip
 except:
     exit_msg = (
         "pipenv is required to package Streamlit. Please install pipenv and try again."
     )
     sys.exit(exit_msg)
 
-VERSION = "1.9.2"  # PEP-440
+VERSION = "1.9.2rc1"  # PEP-440
 
 NAME = "streamlit"
 
 DESCRIPTION = "The fastest way to build data apps in Python"
 
 LONG_DESCRIPTION = (
     "Streamlit's open-source app framework is the easiest way "
```

### Comparing `streamlit-1.9.2/streamlit/__init__.py` & `streamlit-1.9.2rc1/streamlit/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/__main__.py` & `streamlit-1.9.2rc1/streamlit/__main__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/app_session.py` & `streamlit-1.9.2rc1/streamlit/app_session.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/beta_util.py` & `streamlit-1.9.2rc1/streamlit/beta_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/bootstrap.py` & `streamlit-1.9.2rc1/streamlit/bootstrap.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/caching/__init__.py` & `streamlit-1.9.2rc1/streamlit/caching/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/caching/cache_errors.py` & `streamlit-1.9.2rc1/streamlit/caching/cache_errors.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/caching/cache_utils.py` & `streamlit-1.9.2rc1/streamlit/caching/cache_utils.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/caching/hashing.py` & `streamlit-1.9.2rc1/streamlit/caching/hashing.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/caching/memo_decorator.py` & `streamlit-1.9.2rc1/streamlit/caching/memo_decorator.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/caching/singleton_decorator.py` & `streamlit-1.9.2rc1/streamlit/caching/singleton_decorator.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/case_converters.py` & `streamlit-1.9.2rc1/streamlit/case_converters.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/cli.py` & `streamlit-1.9.2rc1/streamlit/cli.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/code_util.py` & `streamlit-1.9.2rc1/streamlit/code_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/commands/__init__.py` & `streamlit-1.9.2rc1/streamlit/commands/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/commands/page_config.py` & `streamlit-1.9.2rc1/streamlit/commands/page_config.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/components/__init__.py` & `streamlit-1.9.2rc1/streamlit/components/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/components/v1/__init__.py` & `streamlit-1.9.2rc1/streamlit/components/v1/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/components/v1/component_arrow.py` & `streamlit-1.9.2rc1/streamlit/components/v1/component_arrow.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/components/v1/components.py` & `streamlit-1.9.2rc1/streamlit/components/v1/components.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/config.py` & `streamlit-1.9.2rc1/streamlit/config.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/config_option.py` & `streamlit-1.9.2rc1/streamlit/config_option.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/config_util.py` & `streamlit-1.9.2rc1/streamlit/config_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/credentials.py` & `streamlit-1.9.2rc1/streamlit/credentials.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/cursor.py` & `streamlit-1.9.2rc1/streamlit/cursor.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/delta_generator.py` & `streamlit-1.9.2rc1/streamlit/delta_generator.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/development.py` & `streamlit-1.9.2rc1/streamlit/development.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/echo.py` & `streamlit-1.9.2rc1/streamlit/echo.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/__init__.py` & `streamlit-1.9.2rc1/streamlit/elements/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/alert.py` & `streamlit-1.9.2rc1/streamlit/elements/alert.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/arrow.py` & `streamlit-1.9.2rc1/streamlit/elements/arrow.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/arrow_altair.py` & `streamlit-1.9.2rc1/streamlit/elements/arrow_altair.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/arrow_vega_lite.py` & `streamlit-1.9.2rc1/streamlit/elements/arrow_vega_lite.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/balloons.py` & `streamlit-1.9.2rc1/streamlit/elements/balloons.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/bokeh_chart.py` & `streamlit-1.9.2rc1/streamlit/elements/bokeh_chart.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/button.py` & `streamlit-1.9.2rc1/streamlit/elements/button.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/camera_input.py` & `streamlit-1.9.2rc1/streamlit/elements/camera_input.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/checkbox.py` & `streamlit-1.9.2rc1/streamlit/elements/checkbox.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/color_picker.py` & `streamlit-1.9.2rc1/streamlit/elements/color_picker.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/dataframe_selector.py` & `streamlit-1.9.2rc1/streamlit/elements/dataframe_selector.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/deck_gl_json_chart.py` & `streamlit-1.9.2rc1/streamlit/elements/deck_gl_json_chart.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/doc_string.py` & `streamlit-1.9.2rc1/streamlit/elements/doc_string.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/empty.py` & `streamlit-1.9.2rc1/streamlit/elements/empty.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/exception.py` & `streamlit-1.9.2rc1/streamlit/elements/exception.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/file_uploader.py` & `streamlit-1.9.2rc1/streamlit/elements/file_uploader.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/form.py` & `streamlit-1.9.2rc1/streamlit/elements/form.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/graphviz_chart.py` & `streamlit-1.9.2rc1/streamlit/elements/graphviz_chart.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/iframe.py` & `streamlit-1.9.2rc1/streamlit/elements/iframe.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/image.py` & `streamlit-1.9.2rc1/streamlit/elements/image.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/json.py` & `streamlit-1.9.2rc1/streamlit/elements/json.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/layouts.py` & `streamlit-1.9.2rc1/streamlit/elements/layouts.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/legacy_altair.py` & `streamlit-1.9.2rc1/streamlit/elements/legacy_altair.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/legacy_data_frame.py` & `streamlit-1.9.2rc1/streamlit/elements/legacy_data_frame.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/legacy_vega_lite.py` & `streamlit-1.9.2rc1/streamlit/elements/legacy_vega_lite.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/lib/__init__.py` & `streamlit-1.9.2rc1/streamlit/elements/lib/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/lib/dicttools.py` & `streamlit-1.9.2rc1/streamlit/elements/lib/dicttools.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/map.py` & `streamlit-1.9.2rc1/streamlit/elements/map.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/markdown.py` & `streamlit-1.9.2rc1/streamlit/elements/markdown.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/media.py` & `streamlit-1.9.2rc1/streamlit/elements/media.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/metric.py` & `streamlit-1.9.2rc1/streamlit/elements/metric.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/multiselect.py` & `streamlit-1.9.2rc1/streamlit/elements/multiselect.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/number_input.py` & `streamlit-1.9.2rc1/streamlit/elements/number_input.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/plotly_chart.py` & `streamlit-1.9.2rc1/streamlit/elements/plotly_chart.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/progress.py` & `streamlit-1.9.2rc1/streamlit/elements/progress.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/pyplot.py` & `streamlit-1.9.2rc1/streamlit/elements/pyplot.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/radio.py` & `streamlit-1.9.2rc1/streamlit/elements/radio.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/select_slider.py` & `streamlit-1.9.2rc1/streamlit/elements/select_slider.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/selectbox.py` & `streamlit-1.9.2rc1/streamlit/elements/selectbox.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/slider.py` & `streamlit-1.9.2rc1/streamlit/elements/slider.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/snow.py` & `streamlit-1.9.2rc1/streamlit/elements/snow.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/text.py` & `streamlit-1.9.2rc1/streamlit/elements/text.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/text_widgets.py` & `streamlit-1.9.2rc1/streamlit/elements/text_widgets.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/time_widgets.py` & `streamlit-1.9.2rc1/streamlit/elements/time_widgets.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/utils.py` & `streamlit-1.9.2rc1/streamlit/elements/utils.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/elements/write.py` & `streamlit-1.9.2rc1/streamlit/elements/write.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/env_util.py` & `streamlit-1.9.2rc1/streamlit/env_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/error_util.py` & `streamlit-1.9.2rc1/streamlit/error_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/errors.py` & `streamlit-1.9.2rc1/streamlit/errors.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/file_util.py` & `streamlit-1.9.2rc1/streamlit/file_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/folder_black_list.py` & `streamlit-1.9.2rc1/streamlit/folder_black_list.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/forward_msg_cache.py` & `streamlit-1.9.2rc1/streamlit/forward_msg_cache.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/forward_msg_queue.py` & `streamlit-1.9.2rc1/streamlit/forward_msg_queue.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/git_util.py` & `streamlit-1.9.2rc1/streamlit/git_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/hello/__init__.py` & `streamlit-1.9.2rc1/streamlit/hello/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/hello/demos.py` & `streamlit-1.9.2rc1/streamlit/hello/demos.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/hello/hello.py` & `streamlit-1.9.2rc1/streamlit/hello/hello.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/in_memory_file_manager.py` & `streamlit-1.9.2rc1/streamlit/in_memory_file_manager.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/js_number.py` & `streamlit-1.9.2rc1/streamlit/js_number.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/legacy_caching/__init__.py` & `streamlit-1.9.2rc1/streamlit/legacy_caching/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/legacy_caching/caching.py` & `streamlit-1.9.2rc1/streamlit/legacy_caching/caching.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/legacy_caching/hashing.py` & `streamlit-1.9.2rc1/streamlit/legacy_caching/hashing.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/logger.py` & `streamlit-1.9.2rc1/streamlit/logger.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/magic.py` & `streamlit-1.9.2rc1/streamlit/magic.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/metrics_util.py` & `streamlit-1.9.2rc1/streamlit/metrics_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/net_util.py` & `streamlit-1.9.2rc1/streamlit/net_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Alert_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Alert_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/ArrowNamedDataSet_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/ArrowNamedDataSet_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/ArrowVegaLiteChart_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/ArrowVegaLiteChart_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Arrow_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Arrow_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Audio_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Audio_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/BackMsg_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/BackMsg_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Balloons_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Balloons_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Block_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Block_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/BokehChart_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/BokehChart_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Button_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Button_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/CameraInput_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/CameraInput_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Checkbox_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Checkbox_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/ClientState_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/ClientState_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/ColorPicker_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/ColorPicker_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Common_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Common_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Components_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Components_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/DataFrame_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/DataFrame_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/DateInput_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/DateInput_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/DeckGlJsonChart_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/DeckGlJsonChart_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Delta_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Delta_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/DocString_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/DocString_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/DownloadButton_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/DownloadButton_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Element_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Element_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Empty_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Empty_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Exception_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Exception_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Favicon_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Favicon_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/FileUploader_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/FileUploader_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/ForwardMsg_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/ForwardMsg_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/GitInfo_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/GitInfo_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/GraphVizChart_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/GraphVizChart_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/IFrame_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/IFrame_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Image_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Image_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Json_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Json_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Markdown_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Markdown_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Metric_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Metric_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/MultiSelect_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/MultiSelect_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/NamedDataSet_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/NamedDataSet_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/NewSession_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/NewSession_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/NumberInput_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/NumberInput_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/PageConfig_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/PageConfig_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/PageInfo_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/PageInfo_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/PlotlyChart_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/PlotlyChart_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Progress_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Progress_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Radio_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Radio_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/RootContainer_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/RootContainer_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Selectbox_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Selectbox_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/SessionEvent_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/SessionEvent_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/SessionState_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/SessionState_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Slider_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Slider_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Snow_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Snow_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Spinner_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Spinner_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/TextArea_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/TextArea_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/TextInput_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/TextInput_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Text_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Text_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/TimeInput_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/TimeInput_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/VegaLiteChart_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/VegaLiteChart_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/Video_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/Video_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/WidgetStates_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/WidgetStates_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/__init__.py` & `streamlit-1.9.2rc1/streamlit/proto/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/proto/openmetrics_data_model_pb2.py` & `streamlit-1.9.2rc1/streamlit/proto/openmetrics_data_model_pb2.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/scriptrunner/__init__.py` & `streamlit-1.9.2rc1/streamlit/scriptrunner/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/scriptrunner/script_requests.py` & `streamlit-1.9.2rc1/streamlit/scriptrunner/script_requests.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/scriptrunner/script_run_context.py` & `streamlit-1.9.2rc1/streamlit/scriptrunner/script_run_context.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/scriptrunner/script_runner.py` & `streamlit-1.9.2rc1/streamlit/scriptrunner/script_runner.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/secrets.py` & `streamlit-1.9.2rc1/streamlit/secrets.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/server/__init__.py` & `streamlit-1.9.2rc1/streamlit/server/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/server/routes.py` & `streamlit-1.9.2rc1/streamlit/server/routes.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/server/server.py` & `streamlit-1.9.2rc1/streamlit/server/server.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/server/server_util.py` & `streamlit-1.9.2rc1/streamlit/server/server_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/server/upload_file_request_handler.py` & `streamlit-1.9.2rc1/streamlit/server/upload_file_request_handler.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/session_data.py` & `streamlit-1.9.2rc1/streamlit/session_data.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/source_util.py` & `streamlit-1.9.2rc1/streamlit/source_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/state/__init__.py` & `streamlit-1.9.2rc1/streamlit/state/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/state/safe_session_state.py` & `streamlit-1.9.2rc1/streamlit/state/safe_session_state.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/state/session_state.py` & `streamlit-1.9.2rc1/streamlit/state/session_state.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/state/session_state_proxy.py` & `streamlit-1.9.2rc1/streamlit/state/session_state_proxy.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/state/widgets.py` & `streamlit-1.9.2rc1/streamlit/state/widgets.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/asset-manifest.json` & `streamlit-1.9.2rc1/streamlit/static/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/assets/streamlit.css` & `streamlit-1.9.2rc1/streamlit/static/assets/streamlit.css`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/favicon.png` & `streamlit-1.9.2rc1/streamlit/static/favicon.png`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/index.html` & `streamlit-1.9.2rc1/streamlit/static/index.html`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/css/5.71be5c0a.chunk.css` & `streamlit-1.9.2rc1/streamlit/static/static/css/5.71be5c0a.chunk.css`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/css/7.f5138d60.chunk.css` & `streamlit-1.9.2rc1/streamlit/static/static/css/7.f5138d60.chunk.css`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/css/main.b46f6fce.chunk.css` & `streamlit-1.9.2rc1/streamlit/static/static/css/main.b46f6fce.chunk.css`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/0.82d9d691.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/0.82d9d691.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/1.41cbec15.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/1.41cbec15.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/1.41cbec15.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/1.41cbec15.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/10.62d2acd1.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/10.62d2acd1.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/10.62d2acd1.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/10.62d2acd1.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/11.5dd372e4.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/11.5dd372e4.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/12.75ba938f.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/12.75ba938f.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/13.640099b2.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/13.640099b2.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/14.dec27756.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/14.dec27756.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/15.bb36f352.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/15.bb36f352.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/15.bb36f352.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/15.bb36f352.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/16.e0ff5a83.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/16.e0ff5a83.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/16.e0ff5a83.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/16.e0ff5a83.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/17.55bdd533.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/17.55bdd533.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/18.417e7db5.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/18.417e7db5.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/18.417e7db5.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/18.417e7db5.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/19.a97d3788.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/19.a97d3788.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/2.dbd55c92.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/2.dbd55c92.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/20.14a753ba.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/20.14a753ba.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/20.14a753ba.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/20.14a753ba.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/21.81da819e.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/21.81da819e.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/21.81da819e.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/21.81da819e.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/22.4e054289.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/22.4e054289.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/22.4e054289.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/22.4e054289.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/23.e332c265.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/23.e332c265.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/23.e332c265.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/23.e332c265.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/24.9cf6cd9f.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/24.9cf6cd9f.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/25.7a23db90.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/25.7a23db90.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/26.6c854743.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/26.6c854743.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/26.6c854743.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/26.6c854743.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/27.bb14fa54.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/27.bb14fa54.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/27.bb14fa54.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/27.bb14fa54.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/28.55fc8575.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/28.55fc8575.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/28.55fc8575.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/28.55fc8575.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/29.e5d8f8cc.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/29.e5d8f8cc.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/29.e5d8f8cc.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/29.e5d8f8cc.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/30.a6f46ad4.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/30.a6f46ad4.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/30.a6f46ad4.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/30.a6f46ad4.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/31.0f4d42f4.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/31.0f4d42f4.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/31.0f4d42f4.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/31.0f4d42f4.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/32.ec76442a.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/32.ec76442a.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/32.ec76442a.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/32.ec76442a.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/33.c16196fe.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/33.c16196fe.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/33.c16196fe.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/33.c16196fe.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/34.194522d6.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/34.194522d6.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/34.194522d6.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/34.194522d6.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/35.fae54e30.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/35.fae54e30.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/35.fae54e30.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/35.fae54e30.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/36.1b75579f.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/36.1b75579f.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/36.1b75579f.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/36.1b75579f.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/37.5ab35022.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/37.5ab35022.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/38.04f3f7d8.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/38.04f3f7d8.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/39.4da3a545.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/39.4da3a545.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/40.6f9ef4f3.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/40.6f9ef4f3.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/40.6f9ef4f3.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/40.6f9ef4f3.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/41.95bd87e1.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/41.95bd87e1.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/42.810f434c.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/42.810f434c.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/43.b19a8746.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/43.b19a8746.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/44.a6ccee7a.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/44.a6ccee7a.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/5.26b8f29c.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/5.26b8f29c.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/5.26b8f29c.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/5.26b8f29c.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/6.7ec31925.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/6.7ec31925.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/7.85ba4e86.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/7.85ba4e86.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/7.85ba4e86.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/7.85ba4e86.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/8.d6b4540e.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/8.d6b4540e.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/9.568f55f3.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/9.568f55f3.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/main.970d3503.chunk.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/main.970d3503.chunk.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/main.970d3503.chunk.js.LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/static/js/main.970d3503.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/js/runtime-main.9ba163f1.js` & `streamlit-1.9.2rc1/streamlit/static/static/js/runtime-main.9ba163f1.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_AMS-Regular.73ea273a.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_AMS-Regular.73ea273a.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_AMS-Regular.853be924.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_AMS-Regular.853be924.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_AMS-Regular.d562e886.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_AMS-Regular.d562e886.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Bold.7489a2fb.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Bold.7489a2fb.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Bold.a1abf90d.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Bold.a1abf90d.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Bold.d757c535.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Bold.d757c535.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Regular.7e873d38.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Regular.7e873d38.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Regular.d6484fce.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Regular.d6484fce.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Caligraphic-Regular.db074fa2.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Caligraphic-Regular.db074fa2.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Bold.354501ba.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Bold.354501ba.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Bold.4c761b37.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Bold.4c761b37.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Bold.931d67ea.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Bold.931d67ea.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Regular.172d3529.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Regular.172d3529.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Regular.6fdf0ac5.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Regular.6fdf0ac5.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Fraktur-Regular.ed305b54.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Fraktur-Regular.ed305b54.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Bold.0c3b8929.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Bold.0c3b8929.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Bold.39890742.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Bold.39890742.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Bold.8169508b.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Bold.8169508b.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-BoldItalic.20f389c4.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-BoldItalic.20f389c4.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-BoldItalic.428978dc.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-BoldItalic.428978dc.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-BoldItalic.828abcb2.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-BoldItalic.828abcb2.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Italic.fa675e5e.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Italic.fa675e5e.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Italic.fd947498.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Italic.fd947498.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Italic.fe2176f7.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Italic.fe2176f7.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Regular.4f35fbcc.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Regular.4f35fbcc.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Regular.9eba1d77.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Regular.9eba1d77.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Main-Regular.f650f111.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Main-Regular.f650f111.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-BoldItalic.3f07ed67.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-BoldItalic.3f07ed67.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-BoldItalic.bf2d440b.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-BoldItalic.bf2d440b.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-BoldItalic.dcbcbd93.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-BoldItalic.dcbcbd93.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-Italic.6d3d25f4.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-Italic.6d3d25f4.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-Italic.8a5f9363.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-Italic.8a5f9363.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Math-Italic.96759856.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Math-Italic.96759856.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Bold.5b49f499.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Bold.5b49f499.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Bold.95591a92.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Bold.95591a92.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Bold.b9cd458a.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Bold.b9cd458a.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Italic.7d393d38.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Italic.7d393d38.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Italic.8d593cfa.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Italic.8d593cfa.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Italic.b257a18c.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Italic.b257a18c.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Regular.02271ec5.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Regular.02271ec5.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Regular.2f7bc363.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Regular.2f7bc363.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_SansSerif-Regular.cd5e231e.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_SansSerif-Regular.cd5e231e.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Script-Regular.073b3402.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Script-Regular.073b3402.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Script-Regular.c81d1b2a.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Script-Regular.c81d1b2a.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Script-Regular.fc9ba524.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Script-Regular.fc9ba524.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size1-Regular.0108e89c.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size1-Regular.0108e89c.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size1-Regular.6de7d4b5.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size1-Regular.6de7d4b5.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size1-Regular.6eec866c.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size1-Regular.6eec866c.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size2-Regular.2960900c.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size2-Regular.2960900c.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size2-Regular.3a99e70a.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size2-Regular.3a99e70a.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size2-Regular.57f5c183.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size2-Regular.57f5c183.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size3-Regular.7947224e.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size3-Regular.7947224e.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size3-Regular.8d6b6822.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size3-Regular.8d6b6822.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size3-Regular.e1951519.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size3-Regular.e1951519.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size4-Regular.4ad7c7e8.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size4-Regular.4ad7c7e8.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size4-Regular.aeffd802.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size4-Regular.aeffd802.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Size4-Regular.e418bf25.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Size4-Regular.e418bf25.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Typewriter-Regular.4c6b94fd.woff` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Typewriter-Regular.4c6b94fd.woff`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Typewriter-Regular.c295e7f7.woff2` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Typewriter-Regular.c295e7f7.woff2`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/KaTeX_Typewriter-Regular.c5c02d76.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/KaTeX_Typewriter-Regular.c5c02d76.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-Bold.52ac8f30.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-Bold.52ac8f30.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-BoldItalic.05b61807.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-BoldItalic.05b61807.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-Italic.454577c2.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-Italic.454577c2.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-Regular.70cc7ff2.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-Regular.70cc7ff2.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-SemiBold.4d4c53c0.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-SemiBold.4d4c53c0.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceCodePro-SemiBoldItalic.2f5470bc.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceCodePro-SemiBoldItalic.2f5470bc.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-Bold.12e6acd2.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-Bold.12e6acd2.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-BoldItalic.7c4f9b00.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-BoldItalic.7c4f9b00.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-Italic.3c01996d.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-Italic.3c01996d.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-Regular.efa76f83.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-Regular.efa76f83.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-SemiBold.43cc81b4.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-SemiBold.43cc81b4.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSansPro-SemiBoldItalic.c30987e2.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSansPro-SemiBoldItalic.c30987e2.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-Bold.bada4fe1.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-Bold.bada4fe1.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-BoldItalic.9f9b1eb2.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-BoldItalic.9f9b1eb2.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-Italic.90931d6a.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-Italic.90931d6a.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-Regular.6f22301c.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-Regular.6f22301c.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-SemiBold.b27cb117.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-SemiBold.b27cb117.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/SourceSerifPro-SemiBoldItalic.1266f2c1.ttf` & `streamlit-1.9.2rc1/streamlit/static/static/media/SourceSerifPro-SemiBoldItalic.1266f2c1.ttf`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/flake-0.beded754.png` & `streamlit-1.9.2rc1/streamlit/static/static/media/flake-0.beded754.png`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/flake-1.8077dc15.png` & `streamlit-1.9.2rc1/streamlit/static/static/media/flake-1.8077dc15.png`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/static/media/flake-2.e3f07d06.png` & `streamlit-1.9.2rc1/streamlit/static/static/media/flake-2.e3f07d06.png`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-2.4.1.min.js` & `streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-api-2.4.1.min.js` & `streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-api-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-gl-2.4.1.min.js` & `streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-gl-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-mathjax-2.4.1.min.js` & `streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-mathjax-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-tables-2.4.1.min.js` & `streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-tables-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/bokeh/bokeh-widgets-2.4.1.min.js` & `streamlit-1.9.2rc1/streamlit/static/vendor/bokeh/bokeh-widgets-2.4.1.min.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/viz/viz-1.8.0.min.js` & `streamlit-1.9.2rc1/streamlit/static/vendor/viz/viz-1.8.0.min.js`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/static/vendor/viz/viz.js-LICENSE.txt` & `streamlit-1.9.2rc1/streamlit/static/vendor/viz/viz.js-LICENSE.txt`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/stats.py` & `streamlit-1.9.2rc1/streamlit/stats.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/string_util.py` & `streamlit-1.9.2rc1/streamlit/string_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/temporary_directory.py` & `streamlit-1.9.2rc1/streamlit/temporary_directory.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/type_util.py` & `streamlit-1.9.2rc1/streamlit/type_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/uploaded_file_manager.py` & `streamlit-1.9.2rc1/streamlit/uploaded_file_manager.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/url_util.py` & `streamlit-1.9.2rc1/streamlit/url_util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/util.py` & `streamlit-1.9.2rc1/streamlit/util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/version.py` & `streamlit-1.9.2rc1/streamlit/version.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/watcher/__init__.py` & `streamlit-1.9.2rc1/streamlit/watcher/__init__.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/watcher/event_based_path_watcher.py` & `streamlit-1.9.2rc1/streamlit/watcher/event_based_path_watcher.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/watcher/local_sources_watcher.py` & `streamlit-1.9.2rc1/streamlit/watcher/local_sources_watcher.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/watcher/path_watcher.py` & `streamlit-1.9.2rc1/streamlit/watcher/path_watcher.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/watcher/polling_path_watcher.py` & `streamlit-1.9.2rc1/streamlit/watcher/polling_path_watcher.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit/watcher/util.py` & `streamlit-1.9.2rc1/streamlit/watcher/util.py`

 * *Files identical despite different names*

### Comparing `streamlit-1.9.2/streamlit.egg-info/PKG-INFO` & `streamlit-1.9.2rc1/streamlit.egg-info/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: streamlit
-Version: 1.9.2
+Version: 1.9.2rc1
 Summary: The fastest way to build data apps in Python
 Home-page: https://streamlit.io
 Author: Streamlit Inc
 Author-email: hello@streamlit.io
 License: Apache 2
 Project-URL: Source, https://github.com/streamlit/streamlit
 Description: Streamlit's open-source app framework is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours! All in pure Python. All for free.
```

### Comparing `streamlit-1.9.2/streamlit.egg-info/SOURCES.txt` & `streamlit-1.9.2rc1/streamlit.egg-info/SOURCES.txt`

 * *Files identical despite different names*

