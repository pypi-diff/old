# Comparing `tmp/nisystemlink_clients-1.0.2.tar.gz` & `tmp/nisystemlink_clients-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nisystemlink_clients-1.0.2.tar", max compression
+gzip compressed data, was "nisystemlink_clients-1.1.0.tar", max compression
```

## Comparing `nisystemlink_clients-1.0.2.tar` & `nisystemlink_clients-1.1.0.tar`

### file list

```diff
@@ -1,82 +1,87 @@
--rw-r--r--   0        0        0     1071 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/LICENSE
--rw-r--r--   0        0        0     2335 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/README.rst
--rw-r--r--   0        0        0       15 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/__init__.py
--rw-r--r--   0        0        0       15 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/__init__.py
--rw-r--r--   0        0        0      360 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/__init__.py
--rw-r--r--   0        0        0      835 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_api_error.py
--rw-r--r--   0        0        0     2501 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_api_exception.py
--rw-r--r--   0        0        0      654 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_cloud_http_configuration.py
--rw-r--r--   0        0        0     4791 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_http_configuration.py
--rw-r--r--   0        0        0     7128 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_http_configuration_manager.py
--rw-r--r--   0        0        0       39 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/__init__.py
--rw-r--r--   0        0        0     1223 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_classproperty_support.py
--rw-r--r--   0        0        0    10921 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_http_client.py
--rw-r--r--   0        0        0     2955 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_http_configuration_file.py
--rw-r--r--   0        0        0     2482 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_path_constants.py
--rw-r--r--   0        0        0     2048 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_timestamp_utilities.py
--rw-r--r--   0        0        0    10778 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_winpaths.py
--rw-r--r--   0        0        0     3764 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_winpaths.pyi
--rw-r--r--   0        0        0      772 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_jupyter_http_configuration.py
--rw-r--r--   0        0        0       15 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/__init__.py
--rw-r--r--   0        0        0     2982 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/_base_client.py
--rw-r--r--   0        0        0      444 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/_json_model.py
--rw-r--r--   0        0        0     1586 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/_methods.py
--rw-r--r--   0        0        0      615 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/_with_paging.py
--rw-r--r--   0        0        0       64 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/__init__.py
--rw-r--r--   0        0        0     9828 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/_data_frame_client.py
--rw-r--r--   0        0        0     1267 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/__init__.py
--rw-r--r--   0        0        0     1098 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_api_info.py
--rw-r--r--   0        0        0      537 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_append_table_data_request.py
--rw-r--r--   0        0        0      625 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_column.py
--rw-r--r--   0        0        0      645 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_column_type.py
--rw-r--r--   0        0        0      809 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_create_table_request.py
--rw-r--r--   0        0        0     3065 2023-03-08 15:13:32.657848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_data_frame.py
--rw-r--r--   0        0        0      599 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_data_type.py
--rw-r--r--   0        0        0      553 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py
--rw-r--r--   0        0        0     1940 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_modify_table_request.py
--rw-r--r--   0        0        0      653 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py
--rw-r--r--   0        0        0     1821 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_modify_tables_request.py
--rw-r--r--   0        0        0      627 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_order_by.py
--rw-r--r--   0        0        0      388 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_paged_table_rows.py
--rw-r--r--   0        0        0      329 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_paged_tables.py
--rw-r--r--   0        0        0     2448 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_query_decimated_data_request.py
--rw-r--r--   0        0        0     2122 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_query_table_data_base.py
--rw-r--r--   0        0        0     1168 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_query_table_data_request.py
--rw-r--r--   0        0        0     3454 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_query_tables_request.py
--rw-r--r--   0        0        0     1195 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_table_metadata.py
--rw-r--r--   0        0        0      279 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_table_rows.py
--rw-r--r--   0        0        0      830 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/__init__.py
--rw-r--r--   0        0        0     3849 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_async_tag_query_result_collection.py
--rw-r--r--   0        0        0    13155 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_buffered_tag_writer.py
--rw-r--r--   0        0        0       39 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/__init__.py
--rw-r--r--   0        0        0      489 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_itime_stamper.py
--rw-r--r--   0        0        0     5787 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_manual_reset_timer.py
--rw-r--r--   0        0        0     3938 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py
--rw-r--r--   0        0        0     3053 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py
--rw-r--r--   0        0        0     1065 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_system_time_stamper.py
--rw-r--r--   0        0        0     2048 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_data_type.py
--rw-r--r--   0        0        0       39 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/__init__.py
--rw-r--r--   0        0        0     2591 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py
--rw-r--r--   0        0        0     2336 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py
--rw-r--r--   0        0        0     2498 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py
--rw-r--r--   0        0        0    15418 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_tag_selection.py
--rw-r--r--   0        0        0     9988 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_tag_subscription.py
--rw-r--r--   0        0        0     4577 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_temporary_tag_selection.py
--rw-r--r--   0        0        0     9900 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_itag_reader.py
--rw-r--r--   0        0        0     9391 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_itag_writer.py
--rw-r--r--   0        0        0      744 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_retention_type.py
--rw-r--r--   0        0        0    11515 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_data.py
--rw-r--r--   0        0        0     5856 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_data_update.py
--rw-r--r--   0        0        0    33150 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_manager.py
--rw-r--r--   0        0        0     1699 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_path_utilities.py
--rw-r--r--   0        0        0     2733 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_query_result_collection.py
--rw-r--r--   0        0        0    30845 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_selection.py
--rw-r--r--   0        0        0     8684 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_subscription.py
--rw-r--r--   0        0        0     1347 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_update_fields.py
--rw-r--r--   0        0        0     3800 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_value_reader.py
--rw-r--r--   0        0        0     2753 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_value_writer.py
--rw-r--r--   0        0        0     4423 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_with_aggregates.py
--rw-r--r--   0        0        0        0 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/py.typed
--rw-r--r--   0        0        0      960 2023-03-08 15:13:32.661848 nisystemlink_clients-1.0.2/nisystemlink/stubs/events.pyi
--rw-r--r--   0        0        0     2596 2023-03-08 15:13:52.790104 nisystemlink_clients-1.0.2/pyproject.toml
--rw-r--r--   0        0        0     3773 1970-01-01 00:00:00.000000 nisystemlink_clients-1.0.2/PKG-INFO
+-rw-r--r--   0        0        0     1071 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/LICENSE
+-rw-r--r--   0        0        0     2335 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/README.rst
+-rw-r--r--   0        0        0       15 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/__init__.py
+-rw-r--r--   0        0        0       15 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/__init__.py
+-rw-r--r--   0        0        0      360 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/__init__.py
+-rw-r--r--   0        0        0      835 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_api_error.py
+-rw-r--r--   0        0        0     2501 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_api_exception.py
+-rw-r--r--   0        0        0      654 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_cloud_http_configuration.py
+-rw-r--r--   0        0        0     4791 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_http_configuration.py
+-rw-r--r--   0        0        0     7128 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_http_configuration_manager.py
+-rw-r--r--   0        0        0       39 2023-04-06 20:25:59.372917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/__init__.py
+-rw-r--r--   0        0        0     1223 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_classproperty_support.py
+-rw-r--r--   0        0        0    10921 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_http_client.py
+-rw-r--r--   0        0        0     2955 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_http_configuration_file.py
+-rw-r--r--   0        0        0     2482 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_path_constants.py
+-rw-r--r--   0        0        0     2048 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_timestamp_utilities.py
+-rw-r--r--   0        0        0    10778 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_winpaths.py
+-rw-r--r--   0        0        0     3764 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_winpaths.pyi
+-rw-r--r--   0        0        0      772 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_jupyter_http_configuration.py
+-rw-r--r--   0        0        0       15 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/__init__.py
+-rw-r--r--   0        0        0     2982 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/_base_client.py
+-rw-r--r--   0        0        0      444 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/_json_model.py
+-rw-r--r--   0        0        0     1968 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/_methods.py
+-rw-r--r--   0        0        0      615 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/_with_paging.py
+-rw-r--r--   0        0        0       66 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/helpers/__init__.py
+-rw-r--r--   0        0        0      981 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/core/helpers/_iterator_file_like.py
+-rw-r--r--   0        0        0       64 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/__init__.py
+-rw-r--r--   0        0        0    10781 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/_data_frame_client.py
+-rw-r--r--   0        0        0     1365 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/__init__.py
+-rw-r--r--   0        0        0     1093 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_api_info.py
+-rw-r--r--   0        0        0      537 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_append_table_data_request.py
+-rw-r--r--   0        0        0      625 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_column.py
+-rw-r--r--   0        0        0     1367 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_column_filter.py
+-rw-r--r--   0        0        0      364 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_column_order_by.py
+-rw-r--r--   0        0        0      645 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_column_type.py
+-rw-r--r--   0        0        0      809 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_create_table_request.py
+-rw-r--r--   0        0        0     3065 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_data_frame.py
+-rw-r--r--   0        0        0      599 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_data_type.py
+-rw-r--r--   0        0        0      553 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py
+-rw-r--r--   0        0        0     1553 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_export_table_data_request.py
+-rw-r--r--   0        0        0     1940 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_modify_table_request.py
+-rw-r--r--   0        0        0      653 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py
+-rw-r--r--   0        0        0     1821 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_modify_tables_request.py
+-rw-r--r--   0        0        0      627 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_order_by.py
+-rw-r--r--   0        0        0      388 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_paged_table_rows.py
+-rw-r--r--   0        0        0      329 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_paged_tables.py
+-rw-r--r--   0        0        0     2448 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_query_decimated_data_request.py
+-rw-r--r--   0        0        0      894 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_query_table_data_base.py
+-rw-r--r--   0        0        0      877 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_query_table_data_request.py
+-rw-r--r--   0        0        0     3454 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_query_tables_request.py
+-rw-r--r--   0        0        0     1195 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_table_metadata.py
+-rw-r--r--   0        0        0      279 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_table_rows.py
+-rw-r--r--   0        0        0      830 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/__init__.py
+-rw-r--r--   0        0        0     3849 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_async_tag_query_result_collection.py
+-rw-r--r--   0        0        0    13155 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_buffered_tag_writer.py
+-rw-r--r--   0        0        0       39 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/__init__.py
+-rw-r--r--   0        0        0      489 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_itime_stamper.py
+-rw-r--r--   0        0        0     5787 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_manual_reset_timer.py
+-rw-r--r--   0        0        0     3938 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py
+-rw-r--r--   0        0        0     3053 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py
+-rw-r--r--   0        0        0     1065 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_system_time_stamper.py
+-rw-r--r--   0        0        0     2048 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_data_type.py
+-rw-r--r--   0        0        0       39 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/__init__.py
+-rw-r--r--   0        0        0     2591 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py
+-rw-r--r--   0        0        0     2336 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py
+-rw-r--r--   0        0        0     2498 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py
+-rw-r--r--   0        0        0    15418 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_tag_selection.py
+-rw-r--r--   0        0        0     9988 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_tag_subscription.py
+-rw-r--r--   0        0        0     4577 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_temporary_tag_selection.py
+-rw-r--r--   0        0        0     9900 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_itag_reader.py
+-rw-r--r--   0        0        0     9391 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_itag_writer.py
+-rw-r--r--   0        0        0      744 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_retention_type.py
+-rw-r--r--   0        0        0    11515 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_data.py
+-rw-r--r--   0        0        0     5856 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_data_update.py
+-rw-r--r--   0        0        0    33150 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_manager.py
+-rw-r--r--   0        0        0     1699 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_path_utilities.py
+-rw-r--r--   0        0        0     2733 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_query_result_collection.py
+-rw-r--r--   0        0        0    30845 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_selection.py
+-rw-r--r--   0        0        0     8684 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_subscription.py
+-rw-r--r--   0        0        0     1347 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_update_fields.py
+-rw-r--r--   0        0        0     3800 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_value_reader.py
+-rw-r--r--   0        0        0     2753 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_value_writer.py
+-rw-r--r--   0        0        0     4423 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_with_aggregates.py
+-rw-r--r--   0        0        0        0 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/py.typed
+-rw-r--r--   0        0        0      960 2023-04-06 20:25:59.380917 nisystemlink_clients-1.1.0/nisystemlink/stubs/events.pyi
+-rw-r--r--   0        0        0     2594 2023-04-06 20:26:28.851364 nisystemlink_clients-1.1.0/pyproject.toml
+-rw-r--r--   0        0        0     3773 1970-01-01 00:00:00.000000 nisystemlink_clients-1.1.0/PKG-INFO
```

### Comparing `nisystemlink_clients-1.0.2/LICENSE` & `nisystemlink_clients-1.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/README.rst` & `nisystemlink_clients-1.1.0/README.rst`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_api_error.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_api_error.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_api_exception.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_api_exception.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_cloud_http_configuration.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_cloud_http_configuration.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_http_configuration.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_http_configuration.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_http_configuration_manager.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_http_configuration_manager.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_classproperty_support.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_classproperty_support.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_http_client.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_http_client.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_http_configuration_file.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_http_configuration_file.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_path_constants.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_path_constants.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_timestamp_utilities.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_timestamp_utilities.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_winpaths.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_winpaths.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_internal/_winpaths.pyi` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_internal/_winpaths.pyi`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_jupyter_http_configuration.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_jupyter_http_configuration.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/_base_client.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/_base_client.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/_methods.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/_methods.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,12 +1,18 @@
 """Wrappers around uplink HTTP decorators with proper type annotations."""
 
 from typing import Any, Callable, Optional, Sequence, Tuple, TypeVar, Union
 
-from uplink import Body, commands, json, returns
+from uplink import (
+    Body,
+    commands,
+    json,
+    response_handler as uplink_response_handler,
+    returns,
+)
 
 F = TypeVar("F", bound=Callable[..., Any])
 
 
 def get(path: str, args: Optional[Sequence[Any]] = None) -> Callable[[F], F]:
     """Annotation for a GET request."""
 
@@ -46,7 +52,18 @@
 def delete(path: str, args: Optional[Sequence[Any]] = None) -> Callable[[F], F]:
     """Annotation for a DELETE request."""
 
     def decorator(func: F) -> F:
         return commands.delete(path, args=args)(func)  # type: ignore
 
     return decorator
+
+
+def response_handler(
+    handler: Any, requires_consumer: Optional[bool] = False
+) -> Callable[[F], F]:
+    """Annotation for creating custom response handlers."""
+
+    def decorator(func: F) -> F:
+        return uplink_response_handler(handler, requires_consumer)(func)  # type: ignore
+
+    return decorator
```

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/core/_uplink/_with_paging.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/core/_uplink/_with_paging.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/_data_frame_client.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/_data_frame_client.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,14 +1,22 @@
 """Implementation of DataFrameClient."""
 
 from typing import List, Optional
 
 from nisystemlink.clients import core
 from nisystemlink.clients.core._uplink._base_client import BaseClient
-from nisystemlink.clients.core._uplink._methods import delete, get, patch, post
+from nisystemlink.clients.core._uplink._methods import (
+    delete,
+    get,
+    patch,
+    post,
+    response_handler,
+)
+from nisystemlink.clients.core.helpers import IteratorFileLike
+from requests.models import Response
 from uplink import Body, Field, Path, Query
 
 from . import models
 
 
 class DataFrameClient(BaseClient):
     def __init__(self, configuration: Optional[core.HttpConfiguration] = None):
@@ -17,30 +25,30 @@
         Args:
             configuration: Defines the web server to connect to and information about
                 how to connect. If not provided, an instance of
                 :class:`JupyterHttpConfiguration <nisystemlink.clients.core.JupyterHttpConfiguration>`
                 is used.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service.
+            ApiException: if unable to communicate with the DataFrame Service.
         """
         if configuration is None:
             configuration = core.JupyterHttpConfiguration()
 
         super().__init__(configuration, "/nidataframe/v1/")
 
     @get("")
     def api_info(self) -> models.ApiInfo:
         """Get information about available API operations.
 
         Returns:
             Information about available API operations.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service.
+            ApiException: if unable to communicate with the DataFrame Service.
         """
         ...
 
     @get(
         "tables",
         args=[
             Query("take"),
@@ -70,15 +78,15 @@
             continuation_token: The token used to paginate results.
             workspace: List of workspace IDs to filter by.
 
         Returns:
             The list of tables with a continuation token.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @post("tables", return_key="id")
     def create_table(self, table: models.CreateTableRequest) -> str:
         """Create a new table with the provided metadata and column definitions.
@@ -86,15 +94,15 @@
         Args:
             table: The request to create the table.
 
         Returns:
             The ID of the newly created table.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @post("query-tables")
     def query_tables(self, query: models.QueryTablesRequest) -> models.PagedTables:
         """Queries available tables on the SystemLink DataFrame service and returns their metadata.
@@ -102,77 +110,77 @@
         Args:
             query: The request to query tables.
 
         Returns:
             The list of tables with a continuation token.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @get("tables/{id}")
     def get_table_metadata(self, id: str) -> models.TableMetadata:
         """Retrieves the metadata and column information for a single table identified by its ID.
 
         Args:
-            id (str): Unique ID of a DataFrame table.
+            id (str): Unique ID of a data table.
 
         Returns:
             The metadata for the table.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @patch("tables/{id}", args=[Path, Body])
     def modify_table(self, id: str, update: models.ModifyTableRequest) -> None:
         """Modify properties of a table or its columns.
 
         Args:
-            id: Unique ID of a DataFrame table.
+            id: Unique ID of a data table.
             update: The metadata to update.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @delete("tables/{id}")
     def delete_table(self, id: str) -> None:
         """Deletes a table.
 
         Args:
-            id (str): Unique ID of a DataFrame table.
+            id (str): Unique ID of a data table.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @post("delete-tables", args=[Field("ids")])
     def delete_tables(
         self, ids: List[str]
     ) -> Optional[models.DeleteTablesPartialSuccess]:
         """Deletes multiple tables.
 
         Args:
-            ids (List[str]): List of unique IDs of DataFrame tables.
+            ids (List[str]): List of unique IDs of data tables.
 
         Returns:
             A partial success if any tables failed to delete, or None if all
             tables were deleted successfully.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @post("modify-tables")
     def modify_tables(
         self, updates: models.ModifyTablesRequest
@@ -183,15 +191,15 @@
             updates: The table modifications to apply.
 
         Returns:
             A partial success if any tables failed to be modified, or None if all
             tables were modified successfully.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @get(
         "tables/{id}/data",
         args=[
@@ -211,78 +219,101 @@
         order_by_descending: Optional[bool] = None,
         take: Optional[int] = None,
         continuation_token: Optional[str] = None,
     ) -> models.PagedTableRows:
         """Reads raw data from the table identified by its ID.
 
         Args:
-            id: Unique ID of a DataFrame table.
+            id: Unique ID of a data table.
             columns: Columns to include in the response. Data will be returned in the same order as
                 the columns. If not specified, all columns are returned.
             order_by: List of columns to sort by. Multiple columns may be specified to order rows
                 that have the same value for prior columns. The columns used for ordering do not
                 need to be included in the columns list, in which case they are not returned. If
                 not specified, then the order in which results are returned is undefined.
             order_by_descending: Whether to sort descending instead of ascending. Defaults to false.
             take: Limits the returned list to the specified number of results. Defaults to 500.
             continuation_token: The token used to paginate results.
 
         Returns:
             The table data and total number of rows with a continuation token.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @post("tables/{id}/data", args=[Path, Body])
     def append_table_data(self, id: str, data: models.AppendTableDataRequest) -> None:
         """Appends one or more rows of data to the table identified by its ID.
 
         Args:
-            id: Unique ID of a DataFrame table.
+            id: Unique ID of a data table.
             data: The rows of data to append and any additional options.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @post("tables/{id}/query-data", args=[Path, Body])
     def query_table_data(
         self, id: str, query: models.QueryTableDataRequest
     ) -> models.PagedTableRows:
         """Reads rows of data that match a filter from the table identified by its ID.
 
         Args:
-            id: Unique ID of a DataFrame table.
+            id: Unique ID of a data table.
             query: The filtering and sorting to apply when reading data.
 
         Returns:
             The table data and total number of rows with a continuation token.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
 
     @post("tables/{id}/query-decimated-data", args=[Path, Body])
     def query_decimated_data(
         self, id: str, query: models.QueryDecimatedDataRequest
     ) -> models.TableRows:
         """Reads decimated rows of data from the table identified by its ID.
 
         Args:
-            id: Unique ID of a DataFrame table.
+            id: Unique ID of a data table.
             query: The filtering and decimation options to apply when reading data.
 
         Returns:
             The decimated table data.
 
         Raises:
-            ApiException: if unable to communicate with the Data Frame service
+            ApiException: if unable to communicate with the DataFrame Service
+                or provided an invalid argument.
+        """
+        ...
+
+    def _iter_content_filelike_wrapper(response: Response) -> IteratorFileLike:
+        return IteratorFileLike(response.iter_content(chunk_size=4096))
+
+    @response_handler(_iter_content_filelike_wrapper)
+    @post("tables/{id}/export-data", args=[Path, Body])
+    def export_table_data(
+        self, id: str, query: models.ExportTableDataRequest
+    ) -> IteratorFileLike:
+        """Exports rows of data that match a filter from the table identified by its ID.
+
+        Args:
+            id: Unique ID of a data table.
+            query: The filtering, sorting, and export format to apply when exporting data.
+
+        Returns:
+            A file-like object for reading the exported data.
+
+        Raises:
+            ApiException: if unable to communicate with the DataFrame Service
                 or provided an invalid argument.
         """
         ...
```

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/__init__.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/__init__.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,28 +1,30 @@
 from ._append_table_data_request import AppendTableDataRequest
 from ._api_info import ApiInfo, Operation, OperationsV1
 from ._create_table_request import CreateTableRequest
 from ._column import Column
+from ._column_filter import FilterOperation, ColumnFilter
+from ._column_order_by import ColumnOrderBy
 from ._column_type import ColumnType
 from ._data_frame import DataFrame
 from ._data_type import DataType
 from ._delete_tables_partial_success import DeleteTablesPartialSuccess
+from ._export_table_data_request import ExportTableDataRequest, ExportFormat
 from ._modify_tables_partial_success import ModifyTablesPartialSuccess
 from ._modify_table_request import ColumnMetadataPatch, ModifyTableRequest
 from ._modify_tables_request import ModifyTablesRequest, TableMetadataModification
 from ._order_by import OrderBy
 from ._paged_tables import PagedTables
 from ._paged_table_rows import PagedTableRows
 from ._query_decimated_data_request import (
     DecimationMethod,
     DecimationOptions,
     QueryDecimatedDataRequest,
 )
-from ._query_table_data_base import ColumnFilter, FilterOperation
-from ._query_table_data_request import ColumnOrderBy, QueryTableDataRequest
+from ._query_table_data_request import QueryTableDataRequest
 from ._query_tables_request import QueryTablesRequest
 from ._table_metadata import TableMetadata
 from ._table_rows import TableRows
 
 # Alias to provide backwards compatibility for misnamed class, fixed in 1.0.2
 TableMetdataModification = TableMetadataModification
```

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_api_info.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_api_info.py`

 * *Files 1% similar despite different names*

```diff
@@ -11,15 +11,15 @@
     """The version of the available operation."""
 
 
 class OperationsV1(JsonModel):
     """The operations available in the routes provided by the v1 HTTP API."""
 
     create_tables: Operation
-    """The ability to create new DataFrame tables."""
+    """The ability to create new data tables."""
 
     delete_tables: Operation
     """The ability to delete tables and all of their data."""
 
     modify_metadata: Operation
     """The ability to modify metadata for tables."""
```

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_append_table_data_request.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_append_table_data_request.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_column.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_column.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_column_type.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_column_type.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_create_table_request.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_create_table_request.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_data_frame.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_data_frame.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_data_type.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_data_type.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_modify_table_request.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_modify_table_request.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_modify_tables_request.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_modify_tables_request.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_order_by.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_order_by.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_query_decimated_data_request.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_query_decimated_data_request.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_query_table_data_request.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_query_table_data_request.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,25 +1,15 @@
 from typing import List, Optional
 
-from nisystemlink.clients.core._uplink._json_model import JsonModel
 from nisystemlink.clients.core._uplink._with_paging import WithPaging
 
+from ._column_order_by import ColumnOrderBy
 from ._query_table_data_base import QueryTableDataBase
 
 
-class ColumnOrderBy(JsonModel):
-    """Specifies a column to order by and the ordering direction."""
-
-    column: str
-    """The name of the column to order by."""
-
-    descending: Optional[bool] = None
-    """Whether the ordering should be in descending order."""
-
-
 class QueryTableDataRequest(QueryTableDataBase, WithPaging):
     """Contains the filtering and sorting options to use when querying table data."""
 
     order_by: Optional[List[ColumnOrderBy]] = None
     """A list of columns to order the results by. Multiple columns may be
     specified to order rows that have the same value for prior columns. The
     columns used for sorting do not need to be included in the columns list, in
```

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_query_tables_request.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_query_tables_request.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/dataframe/models/_table_metadata.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/dataframe/models/_table_metadata.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/__init__.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/__init__.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_async_tag_query_result_collection.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_async_tag_query_result_collection.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_buffered_tag_writer.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_buffered_tag_writer.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_manual_reset_timer.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_manual_reset_timer.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_core/_system_time_stamper.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_core/_system_time_stamper.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_data_type.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_data_type.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_tag_selection.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_tag_selection.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_http_tag_subscription.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_http_tag_subscription.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_http/_temporary_tag_selection.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_http/_temporary_tag_selection.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_itag_reader.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_itag_reader.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_itag_writer.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_itag_writer.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_retention_type.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_retention_type.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_data.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_data.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_data_update.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_data_update.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_manager.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_manager.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_path_utilities.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_path_utilities.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_query_result_collection.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_query_result_collection.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_selection.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_selection.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_subscription.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_subscription.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_update_fields.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_update_fields.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_value_reader.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_value_reader.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_value_writer.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_value_writer.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/clients/tag/_tag_with_aggregates.py` & `nisystemlink_clients-1.1.0/nisystemlink/clients/tag/_tag_with_aggregates.py`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/nisystemlink/stubs/events.pyi` & `nisystemlink_clients-1.1.0/nisystemlink/stubs/events.pyi`

 * *Files identical despite different names*

### Comparing `nisystemlink_clients-1.0.2/pyproject.toml` & `nisystemlink_clients-1.1.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "nisystemlink-clients"
-version = "1.0.2"
+version = "1.1.0"
 description = "NI-SystemLink Python API"
 authors = ["National Instruments"]
 maintainers = [
     "Carson Moore <carson.moore@ni.com>",
     "Paul Spangler <paul.spangler@ni.com>",
     "Cameron Waterman <cameron.waterman@ni.com>",
 ]
@@ -25,15 +25,15 @@
     "Programming Language :: Python :: 3.10",
     "Programming Language :: Python :: Implementation :: CPython",
     "Topic :: Scientific/Engineering",
     "Topic :: System :: Hardware",
 ]
 
 [tool.poetry.dependencies]
-python   = "^3.8"
+python = "^3.8"
 aenum    = "^3.1.11"
 Events   = "^0.4"
 httpx    = "^0.23.0"
 requests = "^2.28.1"
 uplink   = "^0.9.7"
 pydantic = "^1.10.2"
```

### Comparing `nisystemlink_clients-1.0.2/PKG-INFO` & `nisystemlink_clients-1.1.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nisystemlink-clients
-Version: 1.0.2
+Version: 1.1.0
 Summary: NI-SystemLink Python API
 License: MIT
 Keywords: nisystemlink,systemlink
 Author: National Instruments
 Maintainer: Carson Moore
 Maintainer-email: carson.moore@ni.com
 Requires-Python: >=3.8,<4.0
```

