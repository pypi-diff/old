# Comparing `tmp/rime_sdk-2.0.0rc3.tar.gz` & `tmp/rime_sdk-2.0.0rc4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rime_sdk-2.0.0rc3.tar", last modified: Thu Apr  6 17:13:04 2023, max compression
+gzip compressed data, was "rime_sdk-2.0.0rc4.tar", last modified: Fri Apr  7 09:08:18 2023, max compression
```

## Comparing `rime_sdk-2.0.0rc3.tar` & `rime_sdk-2.0.0rc4.tar`

### file list

```diff
@@ -1,483 +1,475 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:04.013193 rime_sdk-2.0.0rc3/
--rw-r--r--   0 runner    (1001) docker     (123)      566 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    27362 2023-04-06 17:13:04.013193 rime_sdk-2.0.0rc3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    27071 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:03.969194 rime_sdk-2.0.0rc3/rime_sdk/
--rw-r--r--   0 runner    (1001) docker     (123)     1162 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    57754 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/client.py
--rw-r--r--   0 runner    (1001) docker     (123)    12058 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/data_collector.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:03.969194 rime_sdk-2.0.0rc3/rime_sdk/data_format_check/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/data_format_check/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3468 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/data_format_check/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      965 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/data_format_check/data_format_checker.py
--rw-r--r--   0 runner    (1001) docker     (123)     8402 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/data_format_check/nlp_checker.py
--rw-r--r--   0 runner    (1001) docker     (123)     7743 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/data_format_check/tabular_checker.py
--rw-r--r--   0 runner    (1001) docker     (123)      883 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/detection_event.py
--rw-r--r--   0 runner    (1001) docker     (123)    20899 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/firewall.py
--rw-r--r--   0 runner    (1001) docker     (123)     4908 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/image_builder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:03.969194 rime_sdk-2.0.0rc3/rime_sdk/internal/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    28283 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/config_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1001 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      667 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/decorators.py
--rw-r--r--   0 runner    (1001) docker     (123)     9368 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/file_upload.py
--rw-r--r--   0 runner    (1001) docker     (123)     1976 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/rest_error_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)     1762 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/security_config_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     8222 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/swagger_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     5111 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/swagger_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/test_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2690 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/throttle_queue.py
--rw-r--r--   0 runner    (1001) docker     (123)     2689 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/internal/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    16763 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/job.py
--rw-r--r--   0 runner    (1001) docker     (123)     5026 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)    55004 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/project.py
--rw-r--r--   0 runner    (1001) docker     (123)    23677 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:03.969194 rime_sdk-2.0.0rc3/rime_sdk/swagger/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:03.969194 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/
--rw-r--r--   0 runner    (1001) docker     (123)    45999 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:03.973194 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/
--rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22707 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/agent_manager_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    25158 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/data_collector_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    11141 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/detection_api.py
--rw-r--r--   0 runner    (1001) docker     (123)     9413 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/feature_flag_api.py
--rw-r--r--   0 runner    (1001) docker     (123)     8961 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/file_scanning_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    18073 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/file_upload_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    21473 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/firewall_service_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    20482 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/image_registry_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    26851 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/integration_service_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    37092 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/job_reader_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    17641 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/model_card_service_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    13568 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/model_testing_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    29422 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/monitor_service_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    19707 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/notification_setting_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    55786 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/project_service_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    57282 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/registry_service_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    50274 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/results_reader_api.py
--rw-r--r--   0 runner    (1001) docker     (123)     4053 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/rime_info_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    40148 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/user_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    41732 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/workspace_service_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    25142 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     8249 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:04.013193 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/
--rw-r--r--   0 runner    (1001) docker     (123)    44148 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4291 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/artifact_identifier_category_test_identifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     6632 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/artifact_identifier_subset_test_metric_identifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     5446 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/artifact_identifier_test_case_metric_identifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     3515 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_agent_request_aws_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3545 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_agent_request_gcp_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2514 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_agent_request_local_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5800 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_firewall_request_scheduled_ct_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     3325 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/custom_image_pull_secret.py
--rw-r--r--   0 runner    (1001) docker     (123)     7353 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/custommonitors_name_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4359 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_data_stream_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_info_params_feature_intersection.py
--rw-r--r--   0 runner    (1001) docker     (123)     6318 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_info_params_ranking_info.py
--rw-r--r--   0 runner    (1001) docker     (123)    13463 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_profiling_column_type_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     8043 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_profiling_feature_relationship_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     4888 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/datacollector_datapoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     5711 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/datacollector_datapoint_row.py
--rw-r--r--   0 runner    (1001) docker     (123)     4877 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/dataset_ct_info.py
--rw-r--r--   0 runner    (1001) docker     (123)    10661 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/dataset_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     6481 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/dataset_id_prediction_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     3373 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/datastream_project_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)    16223 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_detection_event.py
--rw-r--r--   0 runner    (1001) docker     (123)     4236 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_event_detail.py
--rw-r--r--   0 runner    (1001) docker     (123)     2691 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_event_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4393 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_metric_degradation_event_details.py
--rw-r--r--   0 runner    (1001) docker     (123)     4168 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_resolution.py
--rw-r--r--   0 runner    (1001) docker     (123)     7708 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_security_event_details.py
--rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/difference_from_target_difference.py
--rw-r--r--   0 runner    (1001) docker     (123)     2682 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/difference_from_target_target.py
--rw-r--r--   0 runner    (1001) docker     (123)     2633 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/digest_config_digest_frequency.py
--rw-r--r--   0 runner    (1001) docker     (123)     5237 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_file_scan_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_huggingface_model_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     4314 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_model_file_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     3356 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_pytorch_model_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     4207 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_security_report.py
--rw-r--r--   0 runner    (1001) docker     (123)     5708 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_security_report_import_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     4907 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_custom_loader_location.py
--rw-r--r--   0 runner    (1001) docker     (123)     3370 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_data_collector_location.py
--rw-r--r--   0 runner    (1001) docker     (123)     5023 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_data_location.py
--rw-r--r--   0 runner    (1001) docker     (123)     3952 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_delta_lake_location.py
--rw-r--r--   0 runner    (1001) docker     (123)     9945 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_firewall.py
--rw-r--r--   0 runner    (1001) docker     (123)     5038 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_firewall_firewall_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     3112 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_latest_run_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     5417 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_location_args.py
--rw-r--r--   0 runner    (1001) docker     (123)     4110 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_location_params.py
--rw-r--r--   0 runner    (1001) docker     (123)     9145 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_scheduled_ct_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     5121 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_test_category_severity.py
--rw-r--r--   0 runner    (1001) docker     (123)     4385 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/googlerpc_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     2784 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/image_reference_reference_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     6713 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     3366 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_integration_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2742 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_integration_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2771 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_variable_sensitivity.py
--rw-r--r--   0 runner    (1001) docker     (123)     4425 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integrations_integration_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4757 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_agents_request_list_agents_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     4389 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_datasets_request_datasets_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     3996 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_images_request_pip_library_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5970 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_aggregated_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     5065 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metric_without_subsets.py
--rw-r--r--   0 runner    (1001) docker     (123)     5013 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     4533 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     3596 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_models_request_model_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     6512 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_monitors_request_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4805 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_notifications_request_list_notifications_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     4336 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_prediction_sets_request_prediction_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     3685 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_summary_tests_request_list_summary_tests_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     5691 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_test_cases_request_list_test_cases_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_package_requirement.py
--rw-r--r--   0 runner    (1001) docker     (123)     2648 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_package_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     3956 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_pip_library.py
--rw-r--r--   0 runner    (1001) docker     (123)     4471 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_pip_requirement.py
--rw-r--r--   0 runner    (1001) docker     (123)     2637 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_role_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4355 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_hugging_face_model_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     4011 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_model_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     3069 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_model_path_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     3486 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/modelcards_model_card_model_card_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4105 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_aggregation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2708 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_aggregation_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2478 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_anomaly_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     6225 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_artifact_identifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     4088 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_difference_from_target.py
--rw-r--r--   0 runner    (1001) docker     (123)     3481 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_excluded_transforms.py
--rw-r--r--   0 runner    (1001) docker     (123)     4926 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_metric_degradation_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    13353 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2628 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_monitor_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4474 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_threshold.py
--rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_threshold_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     3483 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     2691 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitoring_config_alert_level.py
--rw-r--r--   0 runner    (1001) docker     (123)     3950 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitors_monitor_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     5565 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_digest_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_job_action_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3238 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_monitoring_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     9362 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_notification.py
--rw-r--r--   0 runner    (1001) docker     (123)     2737 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_notification_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_object_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_webhook_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5023 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notifsettings_notification_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)    13574 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/object_containing_the_updates_only_the_fields_specified_in_the_mask_will_be_used_by_the_backend_note_the_id_field_is_necessary_to_find_the_given_notification_setting_.py
--rw-r--r--   0 runner    (1001) docker     (123)     4304 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/predictions_model_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     2526 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_add_users_to_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)    10989 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_create_project_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_create_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2510 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_delete_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_get_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3153 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_get_project_url_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_get_workspace_roles_for_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     7232 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_id_uuid_dataset_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     6538 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_id_uuid_model_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_list_projects_request_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     5284 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_list_projects_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5701 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_list_users_of_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3702 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_owner_details.py
--rw-r--r--   0 runner    (1001) docker     (123)    15287 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_project.py
--rw-r--r--   0 runner    (1001) docker     (123)     4134 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_project_with_owner_details.py
--rw-r--r--   0 runner    (1001) docker     (123)     2542 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_remove_user_from_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_update_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2534 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_update_user_of_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4343 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_update_workspace_roles_for_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/projects_project_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     2678 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/protobuf_any.py
--rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/protobuf_null_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     7602 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_feature_cause.py
--rw-r--r--   0 runner    (1001) docker     (123)     5071 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_rca_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     2665 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_rca_role.py
--rw-r--r--   0 runner    (1001) docker     (123)     6639 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_test_case_cause.py
--rw-r--r--   0 runner    (1001) docker     (123)     4262 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_test_case_id.py
--rw-r--r--   0 runner    (1001) docker     (123)     4187 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/registry_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     2651 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/registry_validity_status.py
--rw-r--r--   0 runner    (1001) docker     (123)    10401 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/registryprediction_prediction.py
--rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rename_test_run_id_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4909 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/resetpassword_user_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_actor_role.py
--rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_add_users_to_workspace_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6182 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_agent.py
--rw-r--r--   0 runner    (1001) docker     (123)     2708 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_agent_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     8431 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_api_token_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     3920 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_archived_job_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2482 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_cancel_job_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6122 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_category_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)    13329 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_category_test_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_config_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4300 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_configure_integration_request_integration_variable.py
--rw-r--r--   0 runner    (1001) docker     (123)     3468 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_configure_integration_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3352 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_continuous_test_job_progress.py
--rw-r--r--   0 runner    (1001) docker     (123)     4960 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_continuous_test_run_progress.py
--rw-r--r--   0 runner    (1001) docker     (123)     5675 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_agent_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_agent_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4796 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_api_token_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_api_token_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_custom_monitor_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     7022 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_firewall_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_firewall_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6713 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_image_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3805 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_image_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3346 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_integration_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3444 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_integration_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3334 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_model_card_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     7105 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_notification_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3140 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_notification_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5640 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_user_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3175 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_user_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5974 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_workspace_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3315 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_workspace_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3157 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_workspace_tag_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_deactivate_agent_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_agent_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_custom_monitor_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_dataset_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2502 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_firewall_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_image_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2514 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_integration_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3334 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_model_card_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_model_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_prediction_set_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_uploaded_file_url_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_workspace_tag_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2526 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_ensure_image_existence_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3093 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_fail_job_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4563 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_failing_row.py
--rw-r--r--   0 runner    (1001) docker     (123)     6295 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_failing_rows_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     9196 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_feature_flags.py
--rw-r--r--   0 runner    (1001) docker     (123)     3307 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_feature_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     3197 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_finalize_cancellation_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3093 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_float_list.py
--rw-r--r--   0 runner    (1001) docker     (123)     3123 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_agent_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3320 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_datapoints_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6026 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_dataset_file_upload_url_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3194 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_dataset_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4078 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_enabled_feature_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3594 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_feature_flag_jwt_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3359 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_feature_flags_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3228 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_firewall_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3144 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_image_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3420 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_integration_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_job_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3357 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_latest_logs_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3328 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_limit_status_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_model_card_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6238 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_model_directory_upload_urls_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_model_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6680 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_monitor_result_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3344 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_prediction_set_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_predictions_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3251 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_project_id_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     8444 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_rime_info_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3255 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_test_run_id_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3073 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_url_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3110 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_user_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3247 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_workspace_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2482 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_heartbeat_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4331 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_image_reference.py
--rw-r--r--   0 runner    (1001) docker     (123)     3071 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_int_list.py
--rw-r--r--   0 runner    (1001) docker     (123)     4002 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_integration_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     4659 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     5091 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_data_continuous_incremental_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     4737 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_data_stress_test.py
--rw-r--r--   0 runner    (1001) docker     (123)    14707 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_view.py
--rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_license_feature.py
--rw-r--r--   0 runner    (1001) docker     (123)     2689 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_license_limit.py
--rw-r--r--   0 runner    (1001) docker     (123)     5402 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_limit_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     2635 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_limit_status_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     4931 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_agents_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4958 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_api_tokens_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3246 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_current_user_roles_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4798 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_datasets_response.py
--rw-r--r--   0 runner    (1001) docker     (123)    10142 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_request_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     5327 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4543 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_enabled_features_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4926 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_file_scan_results_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5810 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_images_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     4033 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_images_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5145 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_request_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6133 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_request_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     4867 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4645 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_metric_identifiers_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3394 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_model_cards_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4759 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_models_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4974 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_monitors_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5518 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_notifications_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4996 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_prediction_sets_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3298 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_uploaded_file_urls_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5721 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_users_of_workspace_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_users_request_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     4690 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_users_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3546 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspace_integrations_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4006 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspace_tags_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_request_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     4867 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3818 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_long_description_tab.py
--rw-r--r--   0 runner    (1001) docker     (123)    13065 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_managed_image.py
--rw-r--r--   0 runner    (1001) docker     (123)     2747 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_managed_image_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     3863 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_model_card.py
--rw-r--r--   0 runner    (1001) docker     (123)     2978 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_model_task.py
--rw-r--r--   0 runner    (1001) docker     (123)     4022 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_model_with_owner_details.py
--rw-r--r--   0 runner    (1001) docker     (123)     4097 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_monitor_data_point.py
--rw-r--r--   0 runner    (1001) docker     (123)     3660 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_named_double.py
--rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_order.py
--rw-r--r--   0 runner    (1001) docker     (123)     4160 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_parent_role_subject_role_pair.py
--rw-r--r--   0 runner    (1001) docker     (123)     3378 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_data_stream_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_dataset_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3283 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_internal_agent_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3219 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_model_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_prediction_set_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2538 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_remove_user_from_workspace_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_reset_password_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_resolve_detection_event_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2651 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_ri_email_recipient.py
--rw-r--r--   0 runner    (1001) docker     (123)     2625 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_ri_plan.py
--rw-r--r--   0 runner    (1001) docker     (123)     3089 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_safe_url.py
--rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_send_ri_email_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2617 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_severity.py
--rw-r--r--   0 runner    (1001) docker     (123)     5025 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_severity_counts.py
--rw-r--r--   0 runner    (1001) docker     (123)     3794 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_sort_spec.py
--rw-r--r--   0 runner    (1001) docker     (123)     6945 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3189 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4941 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3157 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_stress_test_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3353 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_store_datapoints_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4401 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_store_predictions_request_prediction.py
--rw-r--r--   0 runner    (1001) docker     (123)     2510 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_store_predictions_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3071 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_str_list.py
--rw-r--r--   0 runner    (1001) docker     (123)     3252 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_stress_test_job_progress.py
--rw-r--r--   0 runner    (1001) docker     (123)     2669 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_subject_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     3097 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_suggestion.py
--rw-r--r--   0 runner    (1001) docker     (123)     3817 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_sync_image_tag_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4411 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_table_column.py
--rw-r--r--   0 runner    (1001) docker     (123)     2731 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_table_column_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4861 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_tag.py
--rw-r--r--   0 runner    (1001) docker     (123)     2837 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_termination_reason.py
--rw-r--r--   0 runner    (1001) docker     (123)     5817 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_case_monitor_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_case_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     9623 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     3386 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_metric_category.py
--rw-r--r--   0 runner    (1001) docker     (123)     4774 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_run_progress.py
--rw-r--r--   0 runner    (1001) docker     (123)     2771 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_task_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     2615 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     3874 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_time_interval.py
--rw-r--r--   0 runner    (1001) docker     (123)     2594 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_token_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_build_info_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3252 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_firewall_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3444 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_integration_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3290 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_model_card_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3218 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_monitor_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3388 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_notification_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_user_of_workspace_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2486 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_user_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_workspace_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_workspace_tag_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_upsert_feature_flags_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3109 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_upsert_job_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4838 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_detail_with_role.py
--rw-r--r--   0 runner    (1001) docker     (123)     5298 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_role.py
--rw-r--r--   0 runner    (1001) docker     (123)     3849 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_with_role.py
--rw-r--r--   0 runner    (1001) docker     (123)     6778 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_write_mask.py
--rw-r--r--   0 runner    (1001) docker     (123)     3069 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_uuid.py
--rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_validate_test_config_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6396 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_workspace.py
--rw-r--r--   0 runner    (1001) docker     (123)     5953 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_workspace_write_mask.py
--rw-r--r--   0 runner    (1001) docker     (123)     2798 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/riskscore_risk_category_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4704 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/riskscore_risk_score.py
--rw-r--r--   0 runner    (1001) docker     (123)     4059 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/role_users_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4194 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/role_workspace_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4061 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image.py
--rw-r--r--   0 runner    (1001) docker     (123)     4364 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     4760 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_resource_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     7052 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_run_time_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     6653 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemadatacollector_prediction.py
--rw-r--r--   0 runner    (1001) docker     (123)     5016 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemaintegration_integration_variable.py
--rw-r--r--   0 runner    (1001) docker     (123)     4014 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemamonitor_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5273 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemanotification_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4119 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/security_event_details_flagged_datapoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     2753 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/security_event_details_security_event_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2766 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/statedb_job_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_datapoints_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_latest_logs_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_predictions_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5709 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stresstests_project_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     5968 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/test_run_metrics_category_summary_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     4334 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/test_run_metrics_model_perf_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/test_run_progress_test_batch_progress.py
--rw-r--r--   0 runner    (1001) docker     (123)     4150 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_annotated_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     6568 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_connection_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     4005 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_custom_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     5146 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_collector_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     3258 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_file_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     4489 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_info.py
--rw-r--r--   0 runner    (1001) docker     (123)    20224 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_info_params.py
--rw-r--r--   0 runner    (1001) docker     (123)     5355 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_loading_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     6379 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_profiling.py
--rw-r--r--   0 runner    (1001) docker     (123)     6132 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_delta_lake_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     5568 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_hugging_face_data_info.py
--rw-r--r--   0 runner    (1001) docker     (123)    12772 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_model_profiling.py
--rw-r--r--   0 runner    (1001) docker     (123)     4106 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_pred_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     3290 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_prediction_params.py
--rw-r--r--   0 runner    (1001) docker     (123)     4241 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_profiling_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4172 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_single_data_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     4743 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_category.py
--rw-r--r--   0 runner    (1001) docker     (123)     3326 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_category_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     7551 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_run_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4407 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_run_incremental_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2727 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_sensitivity.py
--rw-r--r--   0 runner    (1001) docker     (123)     6530 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_suite_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3399 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_batch_result_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3501 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_feature_result_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3604 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_config_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_run_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5643 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_batch_results_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5753 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_feature_results_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5798 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_summary_tests_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5516 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_cases_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     5493 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_runs_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_rename_test_run_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6466 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_result_summary_counts.py
--rw-r--r--   0 runner    (1001) docker     (123)    15407 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     6896 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result_display.py
--rw-r--r--   0 runner    (1001) docker     (123)    12899 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_case.py
--rw-r--r--   0 runner    (1001) docker     (123)     5267 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_case_display.py
--rw-r--r--   0 runner    (1001) docker     (123)    13618 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     4626 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result_display.py
--rw-r--r--   0 runner    (1001) docker     (123)    15131 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_detail.py
--rw-r--r--   0 runner    (1001) docker     (123)    11706 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)    13955 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/the_updates_to_the_monitor_.py
--rw-r--r--   0 runner    (1001) docker     (123)     6335 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask.py
--rw-r--r--   0 runner    (1001) docker     (123)     4356 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     4500 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data_continuous_incremental_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     4221 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data_stress_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/user_favorite_projects.py
--rw-r--r--   0 runner    (1001) docker     (123)     3373 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/user_private_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     2597 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/user_role.py
--rw-r--r--   0 runner    (1001) docker     (123)     7807 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/user_user_detail.py
--rw-r--r--   0 runner    (1001) docker     (123)     3778 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/users_user_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4103 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4159 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body1.py
--rw-r--r--   0 runner    (1001) docker     (123)     7487 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1betaintegrationsintegration_id_uuid_integration.py
--rw-r--r--   0 runner    (1001) docker     (123)     4289 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1betamodelcardsmodel_card_model_card_id_uuid_model_card.py
--rw-r--r--   0 runner    (1001) docker     (123)    11007 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1firewallfirewall_firewall_id_uuid_firewall.py
--rw-r--r--   0 runner    (1001) docker     (123)     4359 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1projectsproject_id_uuidroleusersuser_user_id_uuid_user.py
--rw-r--r--   0 runner    (1001) docker     (123)     8161 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1usersuser_id_uuid_user.py
--rw-r--r--   0 runner    (1001) docker     (123)     7242 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1workspaceworkspace_workspace_id_uuid_workspace.py
--rw-r--r--   0 runner    (1001) docker     (123)     4217 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/workspace_id_uuid_users_body.py
--rw-r--r--   0 runner    (1001) docker     (123)     4496 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/workspace_workspace_workspace_id_uuid_body.py
--rw-r--r--   0 runner    (1001) docker     (123)    13026 2023-04-06 17:12:59.000000 rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/rest.py
--rw-r--r--   0 runner    (1001) docker     (123)     5209 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/test_batch.py
--rw-r--r--   0 runner    (1001) docker     (123)    14716 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/rime_sdk/test_run.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:13:03.969194 rime_sdk-2.0.0rc3/rime_sdk.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    27362 2023-04-06 17:13:03.000000 rime_sdk-2.0.0rc3/rime_sdk.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    31846 2023-04-06 17:13:03.000000 rime_sdk-2.0.0rc3/rime_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 17:13:03.000000 rime_sdk-2.0.0rc3/rime_sdk.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-04-06 17:13:03.000000 rime_sdk-2.0.0rc3/rime_sdk.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      154 2023-04-06 17:13:03.000000 rime_sdk-2.0.0rc3/rime_sdk.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 17:13:03.000000 rime_sdk-2.0.0rc3/rime_sdk.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 17:13:04.013193 rime_sdk-2.0.0rc3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1330 2023-04-06 17:12:21.000000 rime_sdk-2.0.0rc3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.163589 rime_sdk-2.0.0rc4/
+-rw-r--r--   0 runner    (1001) docker     (123)      566 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    27362 2023-04-07 09:08:18.163589 rime_sdk-2.0.0rc4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    27071 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.119589 rime_sdk-2.0.0rc4/rime_sdk/
+-rw-r--r--   0 runner    (1001) docker     (123)     1162 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57754 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12058 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/data_collector.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.123589 rime_sdk-2.0.0rc4/rime_sdk/data_format_check/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/data_format_check/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3468 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/data_format_check/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/data_format_check/data_format_checker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8402 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/data_format_check/nlp_checker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7743 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/data_format_check/tabular_checker.py
+-rw-r--r--   0 runner    (1001) docker     (123)      883 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/detection_event.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20899 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/firewall.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4908 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/image_builder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.123589 rime_sdk-2.0.0rc4/rime_sdk/internal/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28283 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/config_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1001 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      667 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9368 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/file_upload.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1976 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/rest_error_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1762 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/security_config_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8222 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/swagger_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5111 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/swagger_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/test_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2690 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/throttle_queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2689 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/internal/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16763 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/job.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5026 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55004 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/project.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23861 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.123589 rime_sdk-2.0.0rc4/rime_sdk/swagger/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.123589 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/
+-rw-r--r--   0 runner    (1001) docker     (123)    45026 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.127589 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22707 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/agent_manager_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25158 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/data_collector_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11141 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/detection_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9413 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/feature_flag_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8961 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/file_scanning_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18073 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/file_upload_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21473 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/firewall_service_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20482 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/image_registry_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26851 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/integration_service_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26953 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/job_reader_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17641 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/model_card_service_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13568 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/model_testing_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29422 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/monitor_service_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19707 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/notification_setting_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55786 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/project_service_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57282 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/registry_service_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50274 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/results_reader_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4053 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/rime_info_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40148 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/user_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41732 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/workspace_service_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25142 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8249 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.163589 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/
+-rw-r--r--   0 runner    (1001) docker     (123)    43175 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4291 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/artifact_identifier_category_test_identifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6632 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/artifact_identifier_subset_test_metric_identifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5446 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/artifact_identifier_test_case_metric_identifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3515 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_agent_request_aws_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3545 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_agent_request_gcp_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2514 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_agent_request_local_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5800 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_firewall_request_scheduled_ct_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3325 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/custom_image_pull_secret.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7353 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/custommonitors_name_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4359 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_data_stream_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_info_params_feature_intersection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6318 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_info_params_ranking_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13463 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_profiling_column_type_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8043 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_profiling_feature_relationship_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4888 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/datacollector_datapoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5711 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/datacollector_datapoint_row.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4877 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/dataset_ct_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10661 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/dataset_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6481 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/dataset_id_prediction_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3373 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/datastream_project_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16223 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_detection_event.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4236 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_event_detail.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2691 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_event_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4393 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_metric_degradation_event_details.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4168 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_resolution.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7708 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_security_event_details.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/difference_from_target_difference.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2682 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/difference_from_target_target.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2633 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/digest_config_digest_frequency.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5237 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_file_scan_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_huggingface_model_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4314 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_model_file_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3356 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_pytorch_model_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4207 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_security_report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5708 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_security_report_import_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4907 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_custom_loader_location.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3370 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_data_collector_location.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5023 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_data_location.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3952 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_delta_lake_location.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9945 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_firewall.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5038 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_firewall_firewall_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3112 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_latest_run_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5417 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_location_args.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4110 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_location_params.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9145 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_scheduled_ct_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5121 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_test_category_severity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4385 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/googlerpc_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2784 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/image_reference_reference_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7422 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration_level.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3366 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2878 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2771 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_variable_sensitivity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4425 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integrations_integration_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/job_data_continuous_incremental_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4673 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/job_data_stress_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4757 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_agents_request_list_agents_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4389 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_datasets_request_datasets_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3996 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_images_request_pip_library_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5970 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_aggregated_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5065 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metric_without_subsets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5013 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4533 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3596 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_models_request_model_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6512 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_monitors_request_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4805 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_notifications_request_list_notifications_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4336 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_prediction_sets_request_prediction_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3685 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_summary_tests_request_list_summary_tests_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5691 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_test_cases_request_list_test_cases_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_package_requirement.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2648 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_package_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3956 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_pip_library.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4471 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_pip_requirement.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2637 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_role_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4355 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_hugging_face_model_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4011 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_model_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3069 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_model_path_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3486 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/modelcards_model_card_model_card_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4105 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_aggregation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2708 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_aggregation_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2478 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_anomaly_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6225 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_artifact_identifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4088 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_difference_from_target.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3481 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_excluded_transforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4926 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_metric_degradation_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13353 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2628 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_monitor_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4474 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_threshold.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_threshold_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3483 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2691 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitoring_config_alert_level.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3950 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitors_monitor_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5565 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_digest_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_job_action_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3238 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_monitoring_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9362 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_notification.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2737 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_notification_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_object_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_webhook_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5023 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notifsettings_notification_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13574 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/object_containing_the_updates_only_the_fields_specified_in_the_mask_will_be_used_by_the_backend_note_the_id_field_is_necessary_to_find_the_given_notification_setting_.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4304 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/predictions_model_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2526 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_add_users_to_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10989 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_create_project_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_create_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2510 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_delete_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_get_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3153 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_get_project_url_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_get_workspace_roles_for_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7232 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_id_uuid_dataset_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6538 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_id_uuid_model_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_list_projects_request_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5284 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_list_projects_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5701 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_list_users_of_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3702 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_owner_details.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15287 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4134 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_project_with_owner_details.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2542 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_remove_user_from_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_update_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2534 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_update_user_of_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4343 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_update_workspace_roles_for_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/projects_project_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2678 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/protobuf_any.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/protobuf_null_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7602 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_feature_cause.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5071 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_rca_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2665 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_rca_role.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6639 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_test_case_cause.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4262 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_test_case_id.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4187 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/registry_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2651 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/registry_validity_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10401 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/registryprediction_prediction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rename_test_run_id_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4909 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/resetpassword_user_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_actor_role.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_add_users_to_workspace_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6182 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_agent.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2708 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_agent_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8431 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_api_token_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3920 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_archived_job_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2482 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_cancel_job_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6122 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_category_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13329 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_category_test_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_config_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4300 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_configure_integration_request_integration_variable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3468 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_configure_integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3352 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_continuous_test_job_progress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4960 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_continuous_test_run_progress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5675 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_agent_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_agent_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4796 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_api_token_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_api_token_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_custom_monitor_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7022 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_firewall_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_firewall_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6713 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_image_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3805 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_image_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3346 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_integration_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3444 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3334 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_model_card_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7105 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_notification_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3140 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_notification_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5640 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_user_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3175 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_user_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5974 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_workspace_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3315 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_workspace_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3157 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_workspace_tag_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_deactivate_agent_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_agent_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_custom_monitor_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_dataset_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2502 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_firewall_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_image_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2514 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3334 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_model_card_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_model_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2522 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_prediction_set_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_uploaded_file_url_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_workspace_tag_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2526 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_ensure_image_existence_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4563 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_failing_row.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6295 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_failing_rows_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9196 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_feature_flags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3307 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_feature_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3093 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_float_list.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3123 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_agent_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3320 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_datapoints_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6026 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_dataset_file_upload_url_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3194 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_dataset_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4078 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_enabled_feature_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3594 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_feature_flag_jwt_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3359 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_feature_flags_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3228 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_firewall_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3144 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_image_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3420 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_job_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3357 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_latest_logs_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3328 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_limit_status_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_model_card_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6238 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_model_directory_upload_urls_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3171 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_model_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6680 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_monitor_result_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3344 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_prediction_set_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_predictions_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3251 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_project_id_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8444 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_rime_info_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3255 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_test_run_id_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3073 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_url_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3110 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_user_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3247 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_workspace_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2482 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_heartbeat_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4331 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_image_reference.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3071 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_int_list.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4002 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_integration_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4635 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14707 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_view.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_license_feature.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2689 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_license_limit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5402 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_limit_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2635 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_limit_status_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4931 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_agents_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4958 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_api_tokens_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3246 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_current_user_roles_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4798 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_datasets_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10142 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_request_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5327 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4543 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_enabled_features_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4926 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_file_scan_results_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5810 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_images_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4033 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_images_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5145 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_request_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5027 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4645 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_metric_identifiers_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3394 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_model_cards_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4759 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_models_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4974 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_monitors_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5518 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_notifications_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4996 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_prediction_sets_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3298 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_uploaded_file_urls_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5721 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_users_of_workspace_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_users_request_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4690 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_users_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3546 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspace_integrations_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4006 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspace_tags_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_request_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4867 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3818 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_long_description_tab.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13065 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_managed_image.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2747 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_managed_image_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3863 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_model_card.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2978 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_model_task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4022 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_model_with_owner_details.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4097 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_monitor_data_point.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3660 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_named_double.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_order.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4160 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_parent_role_subject_role_pair.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3378 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_data_stream_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_dataset_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3283 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_internal_agent_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3219 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_model_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_prediction_set_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2538 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_remove_user_from_workspace_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_reset_password_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_resolve_detection_event_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2651 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_ri_email_recipient.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2625 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_ri_plan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3089 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_safe_url.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_send_ri_email_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2617 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_severity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5025 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_severity_counts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3794 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_sort_spec.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6945 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3189 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4941 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3157 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_stress_test_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3353 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_store_datapoints_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4401 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_store_predictions_request_prediction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2510 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_store_predictions_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3071 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_str_list.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3252 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_stress_test_job_progress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2669 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_subject_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3097 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_suggestion.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3817 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_sync_image_tag_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4411 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_table_column.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2731 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_table_column_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4861 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_tag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2837 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_termination_reason.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5817 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_case_monitor_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_case_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9623 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3386 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_metric_category.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4774 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_run_progress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2771 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_task_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2615 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3874 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_time_interval.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2594 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_token_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_build_info_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3252 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_firewall_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3444 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_integration_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3290 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_model_card_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3218 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_monitor_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3388 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_notification_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2530 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_user_of_workspace_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2486 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_user_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_workspace_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_workspace_tag_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_upsert_feature_flags_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4838 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_detail_with_role.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5298 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_role.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3849 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_with_role.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6778 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_write_mask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3069 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_uuid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2518 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_validate_test_config_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6396 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_workspace.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5953 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_workspace_write_mask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2798 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/riskscore_risk_category_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4704 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/riskscore_risk_score.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4059 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/role_users_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4194 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/role_workspace_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4061 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4364 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4760 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_resource_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7052 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_run_time_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6653 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemadatacollector_prediction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5016 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemaintegration_integration_variable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4014 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemamonitor_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5273 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemanotification_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4119 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/security_event_details_flagged_datapoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2753 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/security_event_details_security_event_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2766 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/statedb_job_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_datapoints_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_latest_logs_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_predictions_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5709 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stresstests_project_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5968 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/test_run_metrics_category_summary_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4334 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/test_run_metrics_model_perf_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/test_run_progress_test_batch_progress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4150 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_annotated_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6568 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_connection_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9300 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_custom_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5146 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_collector_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3258 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_file_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4489 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20224 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_info_params.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5355 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_loading_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6379 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_profiling.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6132 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_delta_lake_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5568 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_hugging_face_data_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12772 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_model_profiling.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4106 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_pred_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3290 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_prediction_params.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4241 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_profiling_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4172 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_single_data_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4743 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_category.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3326 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_category_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7638 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_run_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4407 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_run_incremental_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2727 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_sensitivity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6530 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_suite_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3399 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_batch_result_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3501 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_feature_result_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3604 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_config_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_run_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5643 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_batch_results_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5753 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_feature_results_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5798 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_summary_tests_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5516 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_cases_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5493 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_runs_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_rename_test_run_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6466 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_result_summary_counts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15407 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6896 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result_display.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12899 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_case.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5267 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_case_display.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13618 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4626 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result_display.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15131 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_detail.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11706 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13955 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/the_updates_to_the_monitor_.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_favorite_projects.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3373 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_private_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2597 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_role.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7807 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_user_detail.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3778 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/users_user_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4103 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4159 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8292 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1betaintegrationsintegration_id_uuid_integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4289 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1betamodelcardsmodel_card_model_card_id_uuid_model_card.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11007 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1firewallfirewall_firewall_id_uuid_firewall.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4359 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1projectsproject_id_uuidroleusersuser_user_id_uuid_user.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8161 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1usersuser_id_uuid_user.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7242 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1workspaceworkspace_workspace_id_uuid_workspace.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4217 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/workspace_id_uuid_users_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4496 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/workspace_workspace_workspace_id_uuid_body.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13026 2023-04-07 09:08:13.000000 rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/rest.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5209 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/test_batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14716 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/rime_sdk/test_run.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:08:18.119589 rime_sdk-2.0.0rc4/rime_sdk.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    27362 2023-04-07 09:08:18.000000 rime_sdk-2.0.0rc4/rime_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    31206 2023-04-07 09:08:18.000000 rime_sdk-2.0.0rc4/rime_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:08:18.000000 rime_sdk-2.0.0rc4/rime_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-04-07 09:08:18.000000 rime_sdk-2.0.0rc4/rime_sdk.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-04-07 09:08:18.000000 rime_sdk-2.0.0rc4/rime_sdk.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 09:08:18.000000 rime_sdk-2.0.0rc4/rime_sdk.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 09:08:18.163589 rime_sdk-2.0.0rc4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1330 2023-04-07 09:07:25.000000 rime_sdk-2.0.0rc4/setup.py
```

### Comparing `rime_sdk-2.0.0rc3/LICENSE` & `rime_sdk-2.0.0rc4/LICENSE`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/PKG-INFO` & `rime_sdk-2.0.0rc4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rime_sdk
-Version: 2.0.0rc3
+Version: 2.0.0rc4
 Summary: Package to programmatically access a RIME deployment
 Home-page: UNKNOWN
 License: OSI Approved :: Apache Software License
 Platform: UNKNOWN
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `rime_sdk-2.0.0rc3/README.md` & `rime_sdk-2.0.0rc4/README.md`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/__init__.py` & `rime_sdk-2.0.0rc4/rime_sdk/__init__.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/client.py` & `rime_sdk-2.0.0rc4/rime_sdk/client.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/data_collector.py` & `rime_sdk-2.0.0rc4/rime_sdk/data_collector.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/data_format_check/cli.py` & `rime_sdk-2.0.0rc4/rime_sdk/data_format_check/cli.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/data_format_check/data_format_checker.py` & `rime_sdk-2.0.0rc4/rime_sdk/data_format_check/data_format_checker.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/data_format_check/nlp_checker.py` & `rime_sdk-2.0.0rc4/rime_sdk/data_format_check/nlp_checker.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/data_format_check/tabular_checker.py` & `rime_sdk-2.0.0rc4/rime_sdk/data_format_check/tabular_checker.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/detection_event.py` & `rime_sdk-2.0.0rc4/rime_sdk/detection_event.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/firewall.py` & `rime_sdk-2.0.0rc4/rime_sdk/firewall.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/image_builder.py` & `rime_sdk-2.0.0rc4/rime_sdk/image_builder.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/config_parser.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/config_parser.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/constants.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/constants.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/decorators.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/decorators.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/file_upload.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/file_upload.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/rest_error_handler.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/rest_error_handler.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/security_config_parser.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/security_config_parser.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/swagger_parser.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/swagger_parser.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/swagger_utils.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/swagger_utils.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/test_helpers.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/test_helpers.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/throttle_queue.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/throttle_queue.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/internal/utils.py` & `rime_sdk-2.0.0rc4/rime_sdk/internal/utils.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/job.py` & `rime_sdk-2.0.0rc4/rime_sdk/job.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/monitor.py` & `rime_sdk-2.0.0rc4/rime_sdk/monitor.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/project.py` & `rime_sdk-2.0.0rc4/rime_sdk/project.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/registry.py` & `rime_sdk-2.0.0rc4/rime_sdk/registry.py`

 * *Files 2% similar despite different names*

```diff
@@ -464,17 +464,20 @@
                 f"Received dataset_id={dataset_id}"
                 f" and dataset_name={dataset_name}."
             )
         elif dataset_name is None and dataset_id is None:
             raise ValueError("Must provide either dataset_id or dataset_name")
         api = swagger_client.RegistryServiceApi(self._api_client)
         with RESTErrorHandler():
-            res: RimeGetDatasetResponse = api.registry_service_get_dataset(
-                dataset_id=dataset_id, dataset_name=dataset_name
-            )
+            if dataset_id:
+                res: RimeGetDatasetResponse = api.registry_service_get_dataset(
+                    dataset_id=dataset_id
+                )
+            else:
+                res = api.registry_service_get_dataset(dataset_name=dataset_name)
         return res.dataset.to_dict()
 
     def has_dataset(
         self, dataset_id: Optional[str] = None, dataset_name: Optional[str] = None
     ) -> bool:
         """Return a boolean on whether the dataset is present.
 
@@ -501,17 +504,18 @@
                 f" and dataset_name={dataset_name}."
             )
         elif dataset_name is None and dataset_id is None:
             raise ValueError("Must provide either dataset_id or dataset_name")
         api = swagger_client.RegistryServiceApi(self._api_client)
         with RESTErrorHandler():
             try:
-                api.registry_service_get_dataset(
-                    dataset_id=dataset_id, dataset_name=dataset_name
-                )
+                if dataset_id:
+                    api.registry_service_get_dataset(dataset_id=dataset_id)
+                else:
+                    api.registry_service_get_dataset(dataset_name=dataset_name)
             except ApiException as e:
                 if e.status == HTTPStatus.NOT_FOUND:
                     return False
                 else:
                     raise e
         return True
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/__init__.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -84,18 +84,21 @@
 from rime_sdk.swagger.swagger_client.models.firewall_location_args import FirewallLocationArgs
 from rime_sdk.swagger.swagger_client.models.firewall_location_params import FirewallLocationParams
 from rime_sdk.swagger.swagger_client.models.firewall_scheduled_ct_info import FirewallScheduledCTInfo
 from rime_sdk.swagger.swagger_client.models.firewall_test_category_severity import FirewallTestCategorySeverity
 from rime_sdk.swagger.swagger_client.models.googlerpc_status import GooglerpcStatus
 from rime_sdk.swagger.swagger_client.models.image_reference_reference_type import ImageReferenceReferenceType
 from rime_sdk.swagger.swagger_client.models.integration_integration import IntegrationIntegration
+from rime_sdk.swagger.swagger_client.models.integration_integration_level import IntegrationIntegrationLevel
 from rime_sdk.swagger.swagger_client.models.integration_integration_schema import IntegrationIntegrationSchema
 from rime_sdk.swagger.swagger_client.models.integration_integration_type import IntegrationIntegrationType
 from rime_sdk.swagger.swagger_client.models.integration_variable_sensitivity import IntegrationVariableSensitivity
 from rime_sdk.swagger.swagger_client.models.integrations_integration_id_uuid_body import IntegrationsIntegrationIdUuidBody
+from rime_sdk.swagger.swagger_client.models.job_data_continuous_incremental_test import JobDataContinuousIncrementalTest
+from rime_sdk.swagger.swagger_client.models.job_data_stress_test import JobDataStressTest
 from rime_sdk.swagger.swagger_client.models.list_agents_request_list_agents_query import ListAgentsRequestListAgentsQuery
 from rime_sdk.swagger.swagger_client.models.list_datasets_request_datasets_query import ListDatasetsRequestDatasetsQuery
 from rime_sdk.swagger.swagger_client.models.list_images_request_pip_library_filter import ListImagesRequestPipLibraryFilter
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_aggregated_metric import ListMetricIdentifiersResponseAggregatedMetric
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_feature_metric_without_subsets import ListMetricIdentifiersResponseFeatureMetricWithoutSubsets
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_feature_metrics import ListMetricIdentifiersResponseFeatureMetrics
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_subset_metric import ListMetricIdentifiersResponseSubsetMetric
@@ -214,20 +217,18 @@
 from rime_sdk.swagger.swagger_client.models.rime_delete_integration_response import RimeDeleteIntegrationResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_model_card_response import RimeDeleteModelCardResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_model_response import RimeDeleteModelResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_prediction_set_response import RimeDeletePredictionSetResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_uploaded_file_url_response import RimeDeleteUploadedFileURLResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_workspace_tag_response import RimeDeleteWorkspaceTagResponse
 from rime_sdk.swagger.swagger_client.models.rime_ensure_image_existence_response import RimeEnsureImageExistenceResponse
-from rime_sdk.swagger.swagger_client.models.rime_fail_job_response import RimeFailJobResponse
 from rime_sdk.swagger.swagger_client.models.rime_failing_row import RimeFailingRow
 from rime_sdk.swagger.swagger_client.models.rime_failing_rows_result import RimeFailingRowsResult
 from rime_sdk.swagger.swagger_client.models.rime_feature_flags import RimeFeatureFlags
 from rime_sdk.swagger.swagger_client.models.rime_feature_type import RimeFeatureType
-from rime_sdk.swagger.swagger_client.models.rime_finalize_cancellation_response import RimeFinalizeCancellationResponse
 from rime_sdk.swagger.swagger_client.models.rime_float_list import RimeFloatList
 from rime_sdk.swagger.swagger_client.models.rime_get_agent_response import RimeGetAgentResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_datapoints_response import RimeGetDatapointsResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_dataset_file_upload_url_response import RimeGetDatasetFileUploadURLResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_dataset_response import RimeGetDatasetResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_enabled_feature_response import RimeGetEnabledFeatureResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_feature_flag_jwt_response import RimeGetFeatureFlagJwtResponse
@@ -251,16 +252,14 @@
 from rime_sdk.swagger.swagger_client.models.rime_get_user_response import RimeGetUserResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_workspace_response import RimeGetWorkspaceResponse
 from rime_sdk.swagger.swagger_client.models.rime_heartbeat_response import RimeHeartbeatResponse
 from rime_sdk.swagger.swagger_client.models.rime_image_reference import RimeImageReference
 from rime_sdk.swagger.swagger_client.models.rime_int_list import RimeIntList
 from rime_sdk.swagger.swagger_client.models.rime_integration_info import RimeIntegrationInfo
 from rime_sdk.swagger.swagger_client.models.rime_job_data import RimeJobData
-from rime_sdk.swagger.swagger_client.models.rime_job_data_continuous_incremental_test import RimeJobDataContinuousIncrementalTest
-from rime_sdk.swagger.swagger_client.models.rime_job_data_stress_test import RimeJobDataStressTest
 from rime_sdk.swagger.swagger_client.models.rime_job_metadata import RimeJobMetadata
 from rime_sdk.swagger.swagger_client.models.rime_job_type import RimeJobType
 from rime_sdk.swagger.swagger_client.models.rime_job_view import RimeJobView
 from rime_sdk.swagger.swagger_client.models.rime_license_feature import RimeLicenseFeature
 from rime_sdk.swagger.swagger_client.models.rime_license_limit import RimeLicenseLimit
 from rime_sdk.swagger.swagger_client.models.rime_limit_status import RimeLimitStatus
 from rime_sdk.swagger.swagger_client.models.rime_limit_status_status import RimeLimitStatusStatus
@@ -272,16 +271,14 @@
 from rime_sdk.swagger.swagger_client.models.rime_list_detection_events_response import RimeListDetectionEventsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_enabled_features_response import RimeListEnabledFeaturesResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_file_scan_results_response import RimeListFileScanResultsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_images_request import RimeListImagesRequest
 from rime_sdk.swagger.swagger_client.models.rime_list_images_response import RimeListImagesResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_jobs_for_project_request_query import RimeListJobsForProjectRequestQuery
 from rime_sdk.swagger.swagger_client.models.rime_list_jobs_for_project_response import RimeListJobsForProjectResponse
-from rime_sdk.swagger.swagger_client.models.rime_list_jobs_request_query import RimeListJobsRequestQuery
-from rime_sdk.swagger.swagger_client.models.rime_list_jobs_response import RimeListJobsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_metric_identifiers_response import RimeListMetricIdentifiersResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_model_cards_response import RimeListModelCardsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_models_response import RimeListModelsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_monitors_response import RimeListMonitorsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_notifications_response import RimeListNotificationsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_prediction_sets_response import RimeListPredictionSetsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_uploaded_file_urls_response import RimeListUploadedFileURLsResponse
@@ -351,15 +348,14 @@
 from rime_sdk.swagger.swagger_client.models.rime_update_monitor_response import RimeUpdateMonitorResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_notification_response import RimeUpdateNotificationResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_user_of_workspace_response import RimeUpdateUserOfWorkspaceResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_user_response import RimeUpdateUserResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_workspace_response import RimeUpdateWorkspaceResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_workspace_tag_response import RimeUpdateWorkspaceTagResponse
 from rime_sdk.swagger.swagger_client.models.rime_upsert_feature_flags_response import RimeUpsertFeatureFlagsResponse
-from rime_sdk.swagger.swagger_client.models.rime_upsert_job_response import RimeUpsertJobResponse
 from rime_sdk.swagger.swagger_client.models.rime_user_detail_with_role import RimeUserDetailWithRole
 from rime_sdk.swagger.swagger_client.models.rime_user_role import RimeUserRole
 from rime_sdk.swagger.swagger_client.models.rime_user_with_role import RimeUserWithRole
 from rime_sdk.swagger.swagger_client.models.rime_user_write_mask import RimeUserWriteMask
 from rime_sdk.swagger.swagger_client.models.rime_validate_test_config_response import RimeValidateTestConfigResponse
 from rime_sdk.swagger.swagger_client.models.rime_workspace import RimeWorkspace
 from rime_sdk.swagger.swagger_client.models.rime_workspace_write_mask import RimeWorkspaceWriteMask
@@ -423,18 +419,14 @@
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_case import TestrunresultTestCase
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_case_display import TestrunresultTestCaseDisplay
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_feature_result import TestrunresultTestFeatureResult
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_feature_result_display import TestrunresultTestFeatureResultDisplay
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_run_detail import TestrunresultTestRunDetail
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_run_metrics import TestrunresultTestRunMetrics
 from rime_sdk.swagger.swagger_client.models.the_updates_to_the_monitor_ import TheUpdatesToTheMonitor_
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask import UpsertJobRequestWriteMask
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask_job_data import UpsertJobRequestWriteMaskJobData
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask_job_data_continuous_incremental_test import UpsertJobRequestWriteMaskJobDataContinuousIncrementalTest
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask_job_data_stress_test import UpsertJobRequestWriteMaskJobDataStressTest
 from rime_sdk.swagger.swagger_client.models.user_favorite_projects import UserFavoriteProjects
 from rime_sdk.swagger.swagger_client.models.user_private_info import UserPrivateInfo
 from rime_sdk.swagger.swagger_client.models.user_role import UserRole
 from rime_sdk.swagger.swagger_client.models.user_user_detail import UserUserDetail
 from rime_sdk.swagger.swagger_client.models.users_user_id_uuid_body import UsersUserIdUuidBody
 from rime_sdk.swagger.swagger_client.models.users_user_user_id_uuid_body import UsersUserUserIdUuidBody
 from rime_sdk.swagger.swagger_client.models.users_user_user_id_uuid_body1 import UsersUserUserIdUuidBody1
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/__init__.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/__init__.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/agent_manager_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/agent_manager_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/data_collector_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/data_collector_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/detection_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/detection_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/feature_flag_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/feature_flag_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/file_scanning_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/file_scanning_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/file_upload_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/file_upload_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/firewall_service_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/firewall_service_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/image_registry_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/image_registry_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/integration_service_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/integration_service_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/job_reader_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/job_reader_api.py`

 * *Files 13% similar despite different names*

```diff
@@ -412,127 +412,14 @@
             auth_settings=auth_settings,
             async_req=params.get('async_req'),
             _return_http_data_only=params.get('_return_http_data_only'),
             _preload_content=params.get('_preload_content', True),
             _request_timeout=params.get('_request_timeout'),
             collection_formats=collection_formats)
 
-    def job_reader_list_jobs(self, **kwargs):  # noqa: E501
-        """ListJobs  # noqa: E501
-
-        Returns a paginated list of all jobs. The list can be filtered by job type and status.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this      # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers)     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['jobs'])     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```  # noqa: E501
-        This method makes a synchronous HTTP request by default. To make an
-        asynchronous HTTP request, please pass async_req=True
-        >>> thread = api.job_reader_list_jobs(async_req=True)
-        >>> result = thread.get()
-
-        :param async_req bool
-        :param list[str] first_page_query_selected_statuses: Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.   - JOB_STATUS_PENDING: Resources have been created for the job but the job has not started yet.  - JOB_STATUS_FAILED: Blanket status for user or system-related job failure. Check the Termination Reason for details.  - JOB_STATUS_REQUESTED: The job descriptor exists but has no resources allocated. Jobs that remain in this status without moving to the PENDING status are at risk of entering the FAILED status.  - JOB_STATUS_CANCELLED: Job has been cancelled. Cancelled jobs cannot be recovered.
-        :param list[str] first_page_query_selected_types: Specifies a set of types. The query only returns jobs with types in the specified set. Specify no types to return all results.
-        :param str first_page_query_object_id: Specifies an object ID. The query only returns results matching the specified object ID. Object IDs vary by job type. For example, stress test jobs have a project ID and continuous incremental test jobs have a firewall ID.
-        :param str page_token: Specifies a page of the list returned by a ListJobs query. The ListJobs query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageQuery field.
-        :param str page_size: The maximum number of Job objects to return in a single page.
-        :param str view: Specifies how much information about each job to retrieve. The default behavior is the Basic view.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view.
-        :return: RimeListJobsResponse
-                 If the method is called asynchronously,
-                 returns the request thread.
-        """
-        kwargs['_return_http_data_only'] = True
-        if kwargs.get('async_req'):
-            return self.job_reader_list_jobs_with_http_info(**kwargs)  # noqa: E501
-        else:
-            (data) = self.job_reader_list_jobs_with_http_info(**kwargs)  # noqa: E501
-            return data
-
-    def job_reader_list_jobs_with_http_info(self, **kwargs):  # noqa: E501
-        """ListJobs  # noqa: E501
-
-        Returns a paginated list of all jobs. The list can be filtered by job type and status.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this      # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers)     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['jobs'])     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```  # noqa: E501
-        This method makes a synchronous HTTP request by default. To make an
-        asynchronous HTTP request, please pass async_req=True
-        >>> thread = api.job_reader_list_jobs_with_http_info(async_req=True)
-        >>> result = thread.get()
-
-        :param async_req bool
-        :param list[str] first_page_query_selected_statuses: Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.   - JOB_STATUS_PENDING: Resources have been created for the job but the job has not started yet.  - JOB_STATUS_FAILED: Blanket status for user or system-related job failure. Check the Termination Reason for details.  - JOB_STATUS_REQUESTED: The job descriptor exists but has no resources allocated. Jobs that remain in this status without moving to the PENDING status are at risk of entering the FAILED status.  - JOB_STATUS_CANCELLED: Job has been cancelled. Cancelled jobs cannot be recovered.
-        :param list[str] first_page_query_selected_types: Specifies a set of types. The query only returns jobs with types in the specified set. Specify no types to return all results.
-        :param str first_page_query_object_id: Specifies an object ID. The query only returns results matching the specified object ID. Object IDs vary by job type. For example, stress test jobs have a project ID and continuous incremental test jobs have a firewall ID.
-        :param str page_token: Specifies a page of the list returned by a ListJobs query. The ListJobs query returns a pageToken when there is more than one page of results. Specify either this field or the firstPageQuery field.
-        :param str page_size: The maximum number of Job objects to return in a single page.
-        :param str view: Specifies how much information about each job to retrieve. The default behavior is the Basic view.   - JOB_VIEW_BASIC: Server responses only include basic information about the job, including type, status, and some job data.  - JOB_VIEW_FULL: Server responses include all available information about the job, including progress. Has greater performance requirements than the Basic view.
-        :return: RimeListJobsResponse
-                 If the method is called asynchronously,
-                 returns the request thread.
-        """
-
-        all_params = ['first_page_query_selected_statuses', 'first_page_query_selected_types', 'first_page_query_object_id', 'page_token', 'page_size', 'view']  # noqa: E501
-        all_params.append('async_req')
-        all_params.append('_return_http_data_only')
-        all_params.append('_preload_content')
-        all_params.append('_request_timeout')
-
-        params = locals()
-        for key, val in six.iteritems(params['kwargs']):
-            if key not in all_params:
-                raise TypeError(
-                    "Got an unexpected keyword argument '%s'"
-                    " to method job_reader_list_jobs" % key
-                )
-            params[key] = val
-        del params['kwargs']
-
-        collection_formats = {}
-
-        path_params = {}
-
-        query_params = []
-        if 'first_page_query_selected_statuses' in params:
-            query_params.append(('firstPageQuery.selectedStatuses', params['first_page_query_selected_statuses']))  # noqa: E501
-            collection_formats['firstPageQuery.selectedStatuses'] = 'multi'  # noqa: E501
-        if 'first_page_query_selected_types' in params:
-            query_params.append(('firstPageQuery.selectedTypes', params['first_page_query_selected_types']))  # noqa: E501
-            collection_formats['firstPageQuery.selectedTypes'] = 'multi'  # noqa: E501
-        if 'first_page_query_object_id' in params:
-            query_params.append(('firstPageQuery.objectId', params['first_page_query_object_id']))  # noqa: E501
-        if 'page_token' in params:
-            query_params.append(('pageToken', params['page_token']))  # noqa: E501
-        if 'page_size' in params:
-            query_params.append(('pageSize', params['page_size']))  # noqa: E501
-        if 'view' in params:
-            query_params.append(('view', params['view']))  # noqa: E501
-
-        header_params = {}
-
-        form_params = []
-        local_var_files = {}
-
-        body_params = None
-        # HTTP header `Accept`
-        header_params['Accept'] = self.api_client.select_header_accept(
-            ['application/json'])  # noqa: E501
-
-        # Authentication setting
-        auth_settings = ['rime-api-key']  # noqa: E501
-
-        return self.api_client.call_api(
-            '/v1-beta/jobs', 'GET',
-            path_params,
-            query_params,
-            header_params,
-            body=body_params,
-            post_params=form_params,
-            files=local_var_files,
-            response_type='RimeListJobsResponse',  # noqa: E501
-            auth_settings=auth_settings,
-            async_req=params.get('async_req'),
-            _return_http_data_only=params.get('_return_http_data_only'),
-            _preload_content=params.get('_preload_content', True),
-            _request_timeout=params.get('_request_timeout'),
-            collection_formats=collection_formats)
-
     def job_reader_list_jobs_for_project(self, project_id_uuid, **kwargs):  # noqa: E501
         """ListJobsForProject  # noqa: E501
 
         Returns a paginated list of jobs for a given project. The list can be filtered by job type and status.  #### Python pagination example:  ```python all_objects = [] # Required for authentication to all methods in the API. headers = {\"rime-api-key\": \"INSERT_API_TOKEN\"} page_token = \"\" # Initialize query parameters in a dictionary params = {\"INSERT_QUERY_PARAMETER\": \"INSERT_QUERY_VALUE\"} # Make requests until all results have been returned. while True:     # If the page_token from a previous response is not empty, we need to specify this      # token as a parameter to the next request in order to return the next page.     if page_token != \"\":         params = {\"page_token\": page_token}     res = requests.get(\"INSERT_METHOD_URI\", params=params, headers=headers)     if res.status_code != 200 :         raise ValueError(res)     res_json = res.json()     all_objects.extend(res_json['jobs'])     page_token = res_json['nextPageToken']     # If all results have been returned, res_json['hasMore'] is false.     if not res_json[\"hasMore\"]:         break ```  # noqa: E501
         This method makes a synchronous HTTP request by default. To make an
         asynchronous HTTP request, please pass async_req=True
         >>> thread = api.job_reader_list_jobs_for_project(project_id_uuid, async_req=True)
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/model_card_service_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/model_card_service_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/model_testing_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/model_testing_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/monitor_service_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/monitor_service_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/notification_setting_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/notification_setting_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/project_service_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/project_service_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/registry_service_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/registry_service_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/results_reader_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/results_reader_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/rime_info_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/rime_info_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/user_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/user_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api/workspace_service_api.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api/workspace_service_api.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/api_client.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/api_client.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/configuration.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/configuration.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/__init__.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -59,18 +59,21 @@
 from rime_sdk.swagger.swagger_client.models.firewall_location_args import FirewallLocationArgs
 from rime_sdk.swagger.swagger_client.models.firewall_location_params import FirewallLocationParams
 from rime_sdk.swagger.swagger_client.models.firewall_scheduled_ct_info import FirewallScheduledCTInfo
 from rime_sdk.swagger.swagger_client.models.firewall_test_category_severity import FirewallTestCategorySeverity
 from rime_sdk.swagger.swagger_client.models.googlerpc_status import GooglerpcStatus
 from rime_sdk.swagger.swagger_client.models.image_reference_reference_type import ImageReferenceReferenceType
 from rime_sdk.swagger.swagger_client.models.integration_integration import IntegrationIntegration
+from rime_sdk.swagger.swagger_client.models.integration_integration_level import IntegrationIntegrationLevel
 from rime_sdk.swagger.swagger_client.models.integration_integration_schema import IntegrationIntegrationSchema
 from rime_sdk.swagger.swagger_client.models.integration_integration_type import IntegrationIntegrationType
 from rime_sdk.swagger.swagger_client.models.integration_variable_sensitivity import IntegrationVariableSensitivity
 from rime_sdk.swagger.swagger_client.models.integrations_integration_id_uuid_body import IntegrationsIntegrationIdUuidBody
+from rime_sdk.swagger.swagger_client.models.job_data_continuous_incremental_test import JobDataContinuousIncrementalTest
+from rime_sdk.swagger.swagger_client.models.job_data_stress_test import JobDataStressTest
 from rime_sdk.swagger.swagger_client.models.list_agents_request_list_agents_query import ListAgentsRequestListAgentsQuery
 from rime_sdk.swagger.swagger_client.models.list_datasets_request_datasets_query import ListDatasetsRequestDatasetsQuery
 from rime_sdk.swagger.swagger_client.models.list_images_request_pip_library_filter import ListImagesRequestPipLibraryFilter
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_aggregated_metric import ListMetricIdentifiersResponseAggregatedMetric
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_feature_metric_without_subsets import ListMetricIdentifiersResponseFeatureMetricWithoutSubsets
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_feature_metrics import ListMetricIdentifiersResponseFeatureMetrics
 from rime_sdk.swagger.swagger_client.models.list_metric_identifiers_response_subset_metric import ListMetricIdentifiersResponseSubsetMetric
@@ -189,20 +192,18 @@
 from rime_sdk.swagger.swagger_client.models.rime_delete_integration_response import RimeDeleteIntegrationResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_model_card_response import RimeDeleteModelCardResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_model_response import RimeDeleteModelResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_prediction_set_response import RimeDeletePredictionSetResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_uploaded_file_url_response import RimeDeleteUploadedFileURLResponse
 from rime_sdk.swagger.swagger_client.models.rime_delete_workspace_tag_response import RimeDeleteWorkspaceTagResponse
 from rime_sdk.swagger.swagger_client.models.rime_ensure_image_existence_response import RimeEnsureImageExistenceResponse
-from rime_sdk.swagger.swagger_client.models.rime_fail_job_response import RimeFailJobResponse
 from rime_sdk.swagger.swagger_client.models.rime_failing_row import RimeFailingRow
 from rime_sdk.swagger.swagger_client.models.rime_failing_rows_result import RimeFailingRowsResult
 from rime_sdk.swagger.swagger_client.models.rime_feature_flags import RimeFeatureFlags
 from rime_sdk.swagger.swagger_client.models.rime_feature_type import RimeFeatureType
-from rime_sdk.swagger.swagger_client.models.rime_finalize_cancellation_response import RimeFinalizeCancellationResponse
 from rime_sdk.swagger.swagger_client.models.rime_float_list import RimeFloatList
 from rime_sdk.swagger.swagger_client.models.rime_get_agent_response import RimeGetAgentResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_datapoints_response import RimeGetDatapointsResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_dataset_file_upload_url_response import RimeGetDatasetFileUploadURLResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_dataset_response import RimeGetDatasetResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_enabled_feature_response import RimeGetEnabledFeatureResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_feature_flag_jwt_response import RimeGetFeatureFlagJwtResponse
@@ -226,16 +227,14 @@
 from rime_sdk.swagger.swagger_client.models.rime_get_user_response import RimeGetUserResponse
 from rime_sdk.swagger.swagger_client.models.rime_get_workspace_response import RimeGetWorkspaceResponse
 from rime_sdk.swagger.swagger_client.models.rime_heartbeat_response import RimeHeartbeatResponse
 from rime_sdk.swagger.swagger_client.models.rime_image_reference import RimeImageReference
 from rime_sdk.swagger.swagger_client.models.rime_int_list import RimeIntList
 from rime_sdk.swagger.swagger_client.models.rime_integration_info import RimeIntegrationInfo
 from rime_sdk.swagger.swagger_client.models.rime_job_data import RimeJobData
-from rime_sdk.swagger.swagger_client.models.rime_job_data_continuous_incremental_test import RimeJobDataContinuousIncrementalTest
-from rime_sdk.swagger.swagger_client.models.rime_job_data_stress_test import RimeJobDataStressTest
 from rime_sdk.swagger.swagger_client.models.rime_job_metadata import RimeJobMetadata
 from rime_sdk.swagger.swagger_client.models.rime_job_type import RimeJobType
 from rime_sdk.swagger.swagger_client.models.rime_job_view import RimeJobView
 from rime_sdk.swagger.swagger_client.models.rime_license_feature import RimeLicenseFeature
 from rime_sdk.swagger.swagger_client.models.rime_license_limit import RimeLicenseLimit
 from rime_sdk.swagger.swagger_client.models.rime_limit_status import RimeLimitStatus
 from rime_sdk.swagger.swagger_client.models.rime_limit_status_status import RimeLimitStatusStatus
@@ -247,16 +246,14 @@
 from rime_sdk.swagger.swagger_client.models.rime_list_detection_events_response import RimeListDetectionEventsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_enabled_features_response import RimeListEnabledFeaturesResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_file_scan_results_response import RimeListFileScanResultsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_images_request import RimeListImagesRequest
 from rime_sdk.swagger.swagger_client.models.rime_list_images_response import RimeListImagesResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_jobs_for_project_request_query import RimeListJobsForProjectRequestQuery
 from rime_sdk.swagger.swagger_client.models.rime_list_jobs_for_project_response import RimeListJobsForProjectResponse
-from rime_sdk.swagger.swagger_client.models.rime_list_jobs_request_query import RimeListJobsRequestQuery
-from rime_sdk.swagger.swagger_client.models.rime_list_jobs_response import RimeListJobsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_metric_identifiers_response import RimeListMetricIdentifiersResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_model_cards_response import RimeListModelCardsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_models_response import RimeListModelsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_monitors_response import RimeListMonitorsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_notifications_response import RimeListNotificationsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_prediction_sets_response import RimeListPredictionSetsResponse
 from rime_sdk.swagger.swagger_client.models.rime_list_uploaded_file_urls_response import RimeListUploadedFileURLsResponse
@@ -326,15 +323,14 @@
 from rime_sdk.swagger.swagger_client.models.rime_update_monitor_response import RimeUpdateMonitorResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_notification_response import RimeUpdateNotificationResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_user_of_workspace_response import RimeUpdateUserOfWorkspaceResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_user_response import RimeUpdateUserResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_workspace_response import RimeUpdateWorkspaceResponse
 from rime_sdk.swagger.swagger_client.models.rime_update_workspace_tag_response import RimeUpdateWorkspaceTagResponse
 from rime_sdk.swagger.swagger_client.models.rime_upsert_feature_flags_response import RimeUpsertFeatureFlagsResponse
-from rime_sdk.swagger.swagger_client.models.rime_upsert_job_response import RimeUpsertJobResponse
 from rime_sdk.swagger.swagger_client.models.rime_user_detail_with_role import RimeUserDetailWithRole
 from rime_sdk.swagger.swagger_client.models.rime_user_role import RimeUserRole
 from rime_sdk.swagger.swagger_client.models.rime_user_with_role import RimeUserWithRole
 from rime_sdk.swagger.swagger_client.models.rime_user_write_mask import RimeUserWriteMask
 from rime_sdk.swagger.swagger_client.models.rime_validate_test_config_response import RimeValidateTestConfigResponse
 from rime_sdk.swagger.swagger_client.models.rime_workspace import RimeWorkspace
 from rime_sdk.swagger.swagger_client.models.rime_workspace_write_mask import RimeWorkspaceWriteMask
@@ -398,18 +394,14 @@
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_case import TestrunresultTestCase
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_case_display import TestrunresultTestCaseDisplay
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_feature_result import TestrunresultTestFeatureResult
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_feature_result_display import TestrunresultTestFeatureResultDisplay
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_run_detail import TestrunresultTestRunDetail
 from rime_sdk.swagger.swagger_client.models.testrunresult_test_run_metrics import TestrunresultTestRunMetrics
 from rime_sdk.swagger.swagger_client.models.the_updates_to_the_monitor_ import TheUpdatesToTheMonitor_
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask import UpsertJobRequestWriteMask
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask_job_data import UpsertJobRequestWriteMaskJobData
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask_job_data_continuous_incremental_test import UpsertJobRequestWriteMaskJobDataContinuousIncrementalTest
-from rime_sdk.swagger.swagger_client.models.upsert_job_request_write_mask_job_data_stress_test import UpsertJobRequestWriteMaskJobDataStressTest
 from rime_sdk.swagger.swagger_client.models.user_favorite_projects import UserFavoriteProjects
 from rime_sdk.swagger.swagger_client.models.user_private_info import UserPrivateInfo
 from rime_sdk.swagger.swagger_client.models.user_role import UserRole
 from rime_sdk.swagger.swagger_client.models.user_user_detail import UserUserDetail
 from rime_sdk.swagger.swagger_client.models.users_user_id_uuid_body import UsersUserIdUuidBody
 from rime_sdk.swagger.swagger_client.models.users_user_user_id_uuid_body import UsersUserUserIdUuidBody
 from rime_sdk.swagger.swagger_client.models.users_user_user_id_uuid_body1 import UsersUserUserIdUuidBody1
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/artifact_identifier_category_test_identifier.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/artifact_identifier_category_test_identifier.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/artifact_identifier_subset_test_metric_identifier.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/artifact_identifier_subset_test_metric_identifier.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/artifact_identifier_test_case_metric_identifier.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/artifact_identifier_test_case_metric_identifier.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_agent_request_aws_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_agent_request_aws_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_agent_request_gcp_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_agent_request_gcp_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_agent_request_local_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_agent_request_local_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/create_firewall_request_scheduled_ct_parameters.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/create_firewall_request_scheduled_ct_parameters.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/custom_image_pull_secret.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/custom_image_pull_secret.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/custommonitors_name_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/custommonitors_name_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_data_stream_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_data_stream_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_info_params_feature_intersection.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_info_params_feature_intersection.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_info_params_ranking_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_info_params_ranking_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_profiling_column_type_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_profiling_column_type_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/data_profiling_feature_relationship_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/data_profiling_feature_relationship_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/datacollector_datapoint.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/datacollector_datapoint.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/datacollector_datapoint_row.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/datacollector_datapoint_row.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/dataset_ct_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/dataset_ct_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/dataset_dataset.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/dataset_dataset.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/dataset_id_prediction_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/dataset_id_prediction_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/datastream_project_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/datastream_project_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_detection_event.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_detection_event.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_event_detail.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_event_detail.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_event_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_event_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_metric_degradation_event_details.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_metric_degradation_event_details.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_resolution.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_resolution.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/detection_security_event_details.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/detection_security_event_details.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/difference_from_target_difference.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/difference_from_target_difference.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/difference_from_target_target.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/difference_from_target_target.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/digest_config_digest_frequency.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/digest_config_digest_frequency.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_file_scan_result.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_file_scan_result.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_huggingface_model_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_huggingface_model_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_model_file_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_model_file_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_pytorch_model_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_pytorch_model_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_security_report.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_security_report.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/filescanning_security_report_import_result.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/filescanning_security_report_import_result.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_custom_loader_location.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_custom_loader_location.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_data_collector_location.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_data_collector_location.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_data_location.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_data_location.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_delta_lake_location.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_delta_lake_location.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_firewall.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_firewall.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_firewall_firewall_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_firewall_firewall_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_latest_run_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_latest_run_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_location_args.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_location_args.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_location_params.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_location_params.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_scheduled_ct_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_scheduled_ct_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/firewall_test_category_severity.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/firewall_test_category_severity.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/googlerpc_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/googlerpc_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/image_reference_reference_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/image_reference_reference_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_integration.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration.py`

 * *Files 3% similar despite different names*

```diff
@@ -29,47 +29,52 @@
     """
     swagger_types = {
         'id': 'RimeUUID',
         'workspace_id': 'RimeUUID',
         'creation_time': 'datetime',
         'name': 'str',
         'type': 'IntegrationIntegrationType',
-        'schema': 'IntegrationIntegrationSchema'
+        'schema': 'IntegrationIntegrationSchema',
+        'level': 'IntegrationIntegrationLevel'
     }
 
     attribute_map = {
         'id': 'id',
         'workspace_id': 'workspaceId',
         'creation_time': 'creationTime',
         'name': 'name',
         'type': 'type',
-        'schema': 'schema'
+        'schema': 'schema',
+        'level': 'level'
     }
 
-    def __init__(self, id=None, workspace_id=None, creation_time=None, name=None, type=None, schema=None):  # noqa: E501
+    def __init__(self, id=None, workspace_id=None, creation_time=None, name=None, type=None, schema=None, level=None):  # noqa: E501
         """IntegrationIntegration - a model defined in Swagger"""  # noqa: E501
         self._id = None
         self._workspace_id = None
         self._creation_time = None
         self._name = None
         self._type = None
         self._schema = None
+        self._level = None
         self.discriminator = None
         if id is not None:
             self.id = id
         if workspace_id is not None:
             self.workspace_id = workspace_id
         if creation_time is not None:
             self.creation_time = creation_time
         if name is not None:
             self.name = name
         if type is not None:
             self.type = type
         if schema is not None:
             self.schema = schema
+        if level is not None:
+            self.level = level
 
     @property
     def id(self):
         """Gets the id of this IntegrationIntegration.  # noqa: E501
 
 
         :return: The id of this IntegrationIntegration.  # noqa: E501
@@ -189,14 +194,35 @@
 
         :param schema: The schema of this IntegrationIntegration.  # noqa: E501
         :type: IntegrationIntegrationSchema
         """
 
         self._schema = schema
 
+    @property
+    def level(self):
+        """Gets the level of this IntegrationIntegration.  # noqa: E501
+
+
+        :return: The level of this IntegrationIntegration.  # noqa: E501
+        :rtype: IntegrationIntegrationLevel
+        """
+        return self._level
+
+    @level.setter
+    def level(self, level):
+        """Sets the level of this IntegrationIntegration.
+
+
+        :param level: The level of this IntegrationIntegration.  # noqa: E501
+        :type: IntegrationIntegrationLevel
+        """
+
+        self._level = level
+
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
             if isinstance(value, list):
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_integration_schema.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration_schema.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_integration_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration_type.py`

 * *Files 8% similar despite different names*

```diff
@@ -23,15 +23,17 @@
 
     """
     allowed enum values
     """
     UNSPECIFIED = "INTEGRATION_TYPE_UNSPECIFIED"
     CUSTOM = "INTEGRATION_TYPE_CUSTOM"
     DATABRICKS = "INTEGRATION_TYPE_DATABRICKS"
-    S3 = "INTEGRATION_TYPE_S3"
+    AWS_S3_ACCESS_KEY = "INTEGRATION_TYPE_AWS_S3_ACCESS_KEY"
+    AWS_S3_ROLE_ARN = "INTEGRATION_TYPE_AWS_S3_ROLE_ARN"
+    HUGGINGFACE = "INTEGRATION_TYPE_HUGGINGFACE"
     GCS = "INTEGRATION_TYPE_GCS"
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integration_variable_sensitivity.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_variable_sensitivity.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/integrations_integration_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integrations_integration_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_agents_request_list_agents_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_agents_request_list_agents_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_datasets_request_datasets_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_datasets_request_datasets_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_images_request_pip_library_filter.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_images_request_pip_library_filter.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_aggregated_metric.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_aggregated_metric.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metric_without_subsets.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metric_without_subsets.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metrics.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metrics.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metric.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metric.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metrics.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metrics.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_models_request_model_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_models_request_model_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_monitors_request_filter.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_monitors_request_filter.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_notifications_request_list_notifications_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_notifications_request_list_notifications_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_prediction_sets_request_prediction_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_prediction_sets_request_prediction_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_summary_tests_request_list_summary_tests_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_summary_tests_request_list_summary_tests_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/list_test_cases_request_list_test_cases_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/list_test_cases_request_list_test_cases_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_package_requirement.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_package_requirement.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_package_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_package_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_pip_library.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_pip_library.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_pip_requirement.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_pip_requirement.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/managed_image_role_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/managed_image_role_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_hugging_face_model_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_hugging_face_model_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_model.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_model.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_model_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_model_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/model_model_path_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/model_model_path_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/modelcards_model_card_model_card_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/modelcards_model_card_model_card_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_aggregation.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_aggregation.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_aggregation_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_aggregation_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_anomaly_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_anomaly_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_artifact_identifier.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_artifact_identifier.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_difference_from_target.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_difference_from_target.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_excluded_transforms.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_excluded_transforms.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_metric_degradation_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_metric_degradation_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_monitor.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_monitor.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_monitor_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_monitor_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_threshold.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_threshold.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_threshold_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_threshold_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitor_transform.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitor_transform.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitoring_config_alert_level.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitoring_config_alert_level.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/monitors_monitor_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/monitors_monitor_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_digest_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_digest_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_job_action_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_job_action_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_monitoring_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_monitoring_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_notification.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_notification.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_notification_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_notification_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_object_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_object_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notification_webhook_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notification_webhook_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/notifsettings_notification_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/notifsettings_notification_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/object_containing_the_updates_only_the_fields_specified_in_the_mask_will_be_used_by_the_backend_note_the_id_field_is_necessary_to_find_the_given_notification_setting_.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/object_containing_the_updates_only_the_fields_specified_in_the_mask_will_be_used_by_the_backend_note_the_id_field_is_necessary_to_find_the_given_notification_setting_.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/predictions_model_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/predictions_model_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_add_users_to_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_add_users_to_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_create_project_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_create_project_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_create_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_create_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_delete_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_delete_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_get_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_get_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_get_project_url_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_get_project_url_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_get_workspace_roles_for_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_get_workspace_roles_for_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_id_uuid_dataset_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_id_uuid_dataset_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_id_uuid_model_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_id_uuid_model_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_list_projects_request_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_list_projects_request_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_list_projects_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_list_projects_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_list_users_of_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_list_users_of_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_owner_details.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_owner_details.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_project.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_project.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_project_with_owner_details.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_project_with_owner_details.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_remove_user_from_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_remove_user_from_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_update_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_update_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_update_user_of_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_update_user_of_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/project_update_workspace_roles_for_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/project_update_workspace_roles_for_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/projects_project_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/projects_project_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/protobuf_any.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/protobuf_any.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/protobuf_null_value.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/protobuf_null_value.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_feature_cause.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_feature_cause.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_rca_result.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_rca_result.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_rca_role.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_rca_role.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_test_case_cause.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_test_case_cause.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rca_test_case_id.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rca_test_case_id.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/registry_metadata.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/registry_metadata.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/registry_validity_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/registry_validity_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/registryprediction_prediction.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/registryprediction_prediction.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rename_test_run_id_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rename_test_run_id_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/resetpassword_user_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/resetpassword_user_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_actor_role.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_actor_role.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_add_users_to_workspace_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_add_users_to_workspace_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_agent.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_agent.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_agent_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_agent_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_api_token_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_api_token_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_archived_job_logs.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_archived_job_logs.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_cancel_job_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_cancel_job_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_category_metric.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_category_metric.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_category_test_result.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_category_test_result.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_config_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_config_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_configure_integration_request_integration_variable.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_configure_integration_request_integration_variable.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_configure_integration_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_configure_integration_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_continuous_test_job_progress.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_continuous_test_job_progress.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_continuous_test_run_progress.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_continuous_test_run_progress.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_agent_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_agent_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_agent_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_agent_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_api_token_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_api_token_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_api_token_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_api_token_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_custom_monitor_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_custom_monitor_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_firewall_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_firewall_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_firewall_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_firewall_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_image_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_image_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_image_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_image_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_integration_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_integration_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_integration_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_integration_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_model_card_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_model_card_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_notification_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_notification_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_notification_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_notification_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_user_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_user_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_user_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_user_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_workspace_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_workspace_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_workspace_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_workspace_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_create_workspace_tag_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_create_workspace_tag_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_deactivate_agent_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_deactivate_agent_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_agent_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_agent_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_custom_monitor_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_custom_monitor_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_dataset_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_dataset_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_firewall_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_firewall_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_image_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_image_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_integration_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_integration_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_model_card_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_model_card_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_model_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_model_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_prediction_set_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_prediction_set_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_uploaded_file_url_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_uploaded_file_url_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_delete_workspace_tag_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_delete_workspace_tag_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_ensure_image_existence_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_ensure_image_existence_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_fail_job_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_job_response.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeFailJobResponse(object):
+class RimeGetJobResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
@@ -32,36 +32,36 @@
     }
 
     attribute_map = {
         'job': 'job'
     }
 
     def __init__(self, job=None):  # noqa: E501
-        """RimeFailJobResponse - a model defined in Swagger"""  # noqa: E501
+        """RimeGetJobResponse - a model defined in Swagger"""  # noqa: E501
         self._job = None
         self.discriminator = None
         if job is not None:
             self.job = job
 
     @property
     def job(self):
-        """Gets the job of this RimeFailJobResponse.  # noqa: E501
+        """Gets the job of this RimeGetJobResponse.  # noqa: E501
 
 
-        :return: The job of this RimeFailJobResponse.  # noqa: E501
+        :return: The job of this RimeGetJobResponse.  # noqa: E501
         :rtype: RimeJobMetadata
         """
         return self._job
 
     @job.setter
     def job(self, job):
-        """Sets the job of this RimeFailJobResponse.
+        """Sets the job of this RimeGetJobResponse.
 
 
-        :param job: The job of this RimeFailJobResponse.  # noqa: E501
+        :param job: The job of this RimeGetJobResponse.  # noqa: E501
         :type: RimeJobMetadata
         """
 
         self._job = job
 
     def to_dict(self):
         """Returns the model properties as a dict"""
@@ -80,15 +80,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeFailJobResponse, dict):
+        if issubclass(RimeGetJobResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -96,15 +96,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeFailJobResponse):
+        if not isinstance(other, RimeGetJobResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_failing_row.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_failing_row.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_failing_rows_result.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_failing_rows_result.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_feature_flags.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_feature_flags.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_feature_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_feature_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_finalize_cancellation_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_build_info_response.py`

 * *Files 12% similar despite different names*

```diff
@@ -11,61 +11,35 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeFinalizeCancellationResponse(object):
+class RimeUpdateBuildInfoResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'job': 'RimeJobMetadata'
     }
 
     attribute_map = {
-        'job': 'job'
     }
 
-    def __init__(self, job=None):  # noqa: E501
-        """RimeFinalizeCancellationResponse - a model defined in Swagger"""  # noqa: E501
-        self._job = None
+    def __init__(self):  # noqa: E501
+        """RimeUpdateBuildInfoResponse - a model defined in Swagger"""  # noqa: E501
         self.discriminator = None
-        if job is not None:
-            self.job = job
-
-    @property
-    def job(self):
-        """Gets the job of this RimeFinalizeCancellationResponse.  # noqa: E501
-
-
-        :return: The job of this RimeFinalizeCancellationResponse.  # noqa: E501
-        :rtype: RimeJobMetadata
-        """
-        return self._job
-
-    @job.setter
-    def job(self, job):
-        """Sets the job of this RimeFinalizeCancellationResponse.
-
-
-        :param job: The job of this RimeFinalizeCancellationResponse.  # noqa: E501
-        :type: RimeJobMetadata
-        """
-
-        self._job = job
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -80,15 +54,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeFinalizeCancellationResponse, dict):
+        if issubclass(RimeUpdateBuildInfoResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -96,15 +70,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeFinalizeCancellationResponse):
+        if not isinstance(other, RimeUpdateBuildInfoResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_float_list.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_float_list.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_agent_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_agent_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_datapoints_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_datapoints_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_dataset_file_upload_url_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_dataset_file_upload_url_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_dataset_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_dataset_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_enabled_feature_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_enabled_feature_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_feature_flag_jwt_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_feature_flag_jwt_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_feature_flags_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_feature_flags_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_firewall_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_firewall_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_image_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_image_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_integration_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_integration_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_job_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_user_response.py`

 * *Files 10% similar despite different names*

```diff
@@ -11,61 +11,61 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeGetJobResponse(object):
+class RimeGetUserResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'job': 'RimeJobMetadata'
+        'user': 'UserUserDetail'
     }
 
     attribute_map = {
-        'job': 'job'
+        'user': 'user'
     }
 
-    def __init__(self, job=None):  # noqa: E501
-        """RimeGetJobResponse - a model defined in Swagger"""  # noqa: E501
-        self._job = None
+    def __init__(self, user=None):  # noqa: E501
+        """RimeGetUserResponse - a model defined in Swagger"""  # noqa: E501
+        self._user = None
         self.discriminator = None
-        if job is not None:
-            self.job = job
+        if user is not None:
+            self.user = user
 
     @property
-    def job(self):
-        """Gets the job of this RimeGetJobResponse.  # noqa: E501
+    def user(self):
+        """Gets the user of this RimeGetUserResponse.  # noqa: E501
 
 
-        :return: The job of this RimeGetJobResponse.  # noqa: E501
-        :rtype: RimeJobMetadata
+        :return: The user of this RimeGetUserResponse.  # noqa: E501
+        :rtype: UserUserDetail
         """
-        return self._job
+        return self._user
 
-    @job.setter
-    def job(self, job):
-        """Sets the job of this RimeGetJobResponse.
+    @user.setter
+    def user(self, user):
+        """Sets the user of this RimeGetUserResponse.
 
 
-        :param job: The job of this RimeGetJobResponse.  # noqa: E501
-        :type: RimeJobMetadata
+        :param user: The user of this RimeGetUserResponse.  # noqa: E501
+        :type: UserUserDetail
         """
 
-        self._job = job
+        self._user = user
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -80,15 +80,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeGetJobResponse, dict):
+        if issubclass(RimeGetUserResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -96,15 +96,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeGetJobResponse):
+        if not isinstance(other, RimeGetUserResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_latest_logs_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_latest_logs_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_limit_status_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_limit_status_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_model_card_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_model_card_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_model_directory_upload_urls_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_model_directory_upload_urls_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_model_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_model_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_monitor_result_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_monitor_result_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_prediction_set_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_prediction_set_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_predictions_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_predictions_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_project_id_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_project_id_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_rime_info_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_rime_info_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_test_run_id_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_test_run_id_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_url_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_url_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_user_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_uuid.py`

 * *Files 13% similar despite different names*

```diff
@@ -11,61 +11,63 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeGetUserResponse(object):
+class RimeUUID(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'user': 'UserUserDetail'
+        'uuid': 'str'
     }
 
     attribute_map = {
-        'user': 'user'
+        'uuid': 'uuid'
     }
 
-    def __init__(self, user=None):  # noqa: E501
-        """RimeGetUserResponse - a model defined in Swagger"""  # noqa: E501
-        self._user = None
+    def __init__(self, uuid=None):  # noqa: E501
+        """RimeUUID - a model defined in Swagger"""  # noqa: E501
+        self._uuid = None
         self.discriminator = None
-        if user is not None:
-            self.user = user
+        if uuid is not None:
+            self.uuid = uuid
 
     @property
-    def user(self):
-        """Gets the user of this RimeGetUserResponse.  # noqa: E501
+    def uuid(self):
+        """Gets the uuid of this RimeUUID.  # noqa: E501
 
+        Unique object ID.  # noqa: E501
 
-        :return: The user of this RimeGetUserResponse.  # noqa: E501
-        :rtype: UserUserDetail
+        :return: The uuid of this RimeUUID.  # noqa: E501
+        :rtype: str
         """
-        return self._user
+        return self._uuid
 
-    @user.setter
-    def user(self, user):
-        """Sets the user of this RimeGetUserResponse.
+    @uuid.setter
+    def uuid(self, uuid):
+        """Sets the uuid of this RimeUUID.
 
+        Unique object ID.  # noqa: E501
 
-        :param user: The user of this RimeGetUserResponse.  # noqa: E501
-        :type: UserUserDetail
+        :param uuid: The uuid of this RimeUUID.  # noqa: E501
+        :type: str
         """
 
-        self._user = user
+        self._uuid = uuid
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -80,15 +82,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeGetUserResponse, dict):
+        if issubclass(RimeUUID, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -96,15 +98,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeGetUserResponse):
+        if not isinstance(other, RimeUUID):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_get_workspace_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_get_workspace_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_heartbeat_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_heartbeat_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_image_reference.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_image_reference.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_int_list.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_int_list.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_integration_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_integration_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_data.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_data.py`

 * *Files 14% similar despite different names*

```diff
@@ -24,16 +24,16 @@
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'stress': 'RimeJobDataStressTest',
-        'continuous_inc': 'RimeJobDataContinuousIncrementalTest',
+        'stress': 'JobDataStressTest',
+        'continuous_inc': 'JobDataContinuousIncrementalTest',
         'file_scan': 'object'
     }
 
     attribute_map = {
         'stress': 'stress',
         'continuous_inc': 'continuousInc',
         'file_scan': 'fileScan'
@@ -54,46 +54,46 @@
 
     @property
     def stress(self):
         """Gets the stress of this RimeJobData.  # noqa: E501
 
 
         :return: The stress of this RimeJobData.  # noqa: E501
-        :rtype: RimeJobDataStressTest
+        :rtype: JobDataStressTest
         """
         return self._stress
 
     @stress.setter
     def stress(self, stress):
         """Sets the stress of this RimeJobData.
 
 
         :param stress: The stress of this RimeJobData.  # noqa: E501
-        :type: RimeJobDataStressTest
+        :type: JobDataStressTest
         """
 
         self._stress = stress
 
     @property
     def continuous_inc(self):
         """Gets the continuous_inc of this RimeJobData.  # noqa: E501
 
 
         :return: The continuous_inc of this RimeJobData.  # noqa: E501
-        :rtype: RimeJobDataContinuousIncrementalTest
+        :rtype: JobDataContinuousIncrementalTest
         """
         return self._continuous_inc
 
     @continuous_inc.setter
     def continuous_inc(self, continuous_inc):
         """Sets the continuous_inc of this RimeJobData.
 
 
         :param continuous_inc: The continuous_inc of this RimeJobData.  # noqa: E501
-        :type: RimeJobDataContinuousIncrementalTest
+        :type: JobDataContinuousIncrementalTest
         """
 
         self._continuous_inc = continuous_inc
 
     @property
     def file_scan(self):
         """Gets the file_scan of this RimeJobData.  # noqa: E501
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_data_continuous_incremental_test.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/job_data_continuous_incremental_test.py`

 * *Files 5% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeJobDataContinuousIncrementalTest(object):
+class JobDataContinuousIncrementalTest(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
@@ -36,84 +36,84 @@
     attribute_map = {
         'firewall_id': 'firewallId',
         'ct_test_run_ids': 'ctTestRunIds',
         'progress': 'progress'
     }
 
     def __init__(self, firewall_id=None, ct_test_run_ids=None, progress=None):  # noqa: E501
-        """RimeJobDataContinuousIncrementalTest - a model defined in Swagger"""  # noqa: E501
+        """JobDataContinuousIncrementalTest - a model defined in Swagger"""  # noqa: E501
         self._firewall_id = None
         self._ct_test_run_ids = None
         self._progress = None
         self.discriminator = None
         if firewall_id is not None:
             self.firewall_id = firewall_id
         if ct_test_run_ids is not None:
             self.ct_test_run_ids = ct_test_run_ids
         if progress is not None:
             self.progress = progress
 
     @property
     def firewall_id(self):
-        """Gets the firewall_id of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        """Gets the firewall_id of this JobDataContinuousIncrementalTest.  # noqa: E501
 
 
-        :return: The firewall_id of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        :return: The firewall_id of this JobDataContinuousIncrementalTest.  # noqa: E501
         :rtype: str
         """
         return self._firewall_id
 
     @firewall_id.setter
     def firewall_id(self, firewall_id):
-        """Sets the firewall_id of this RimeJobDataContinuousIncrementalTest.
+        """Sets the firewall_id of this JobDataContinuousIncrementalTest.
 
 
-        :param firewall_id: The firewall_id of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        :param firewall_id: The firewall_id of this JobDataContinuousIncrementalTest.  # noqa: E501
         :type: str
         """
 
         self._firewall_id = firewall_id
 
     @property
     def ct_test_run_ids(self):
-        """Gets the ct_test_run_ids of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        """Gets the ct_test_run_ids of this JobDataContinuousIncrementalTest.  # noqa: E501
 
 
-        :return: The ct_test_run_ids of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        :return: The ct_test_run_ids of this JobDataContinuousIncrementalTest.  # noqa: E501
         :rtype: list[str]
         """
         return self._ct_test_run_ids
 
     @ct_test_run_ids.setter
     def ct_test_run_ids(self, ct_test_run_ids):
-        """Sets the ct_test_run_ids of this RimeJobDataContinuousIncrementalTest.
+        """Sets the ct_test_run_ids of this JobDataContinuousIncrementalTest.
 
 
-        :param ct_test_run_ids: The ct_test_run_ids of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        :param ct_test_run_ids: The ct_test_run_ids of this JobDataContinuousIncrementalTest.  # noqa: E501
         :type: list[str]
         """
 
         self._ct_test_run_ids = ct_test_run_ids
 
     @property
     def progress(self):
-        """Gets the progress of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        """Gets the progress of this JobDataContinuousIncrementalTest.  # noqa: E501
 
 
-        :return: The progress of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        :return: The progress of this JobDataContinuousIncrementalTest.  # noqa: E501
         :rtype: RimeContinuousTestJobProgress
         """
         return self._progress
 
     @progress.setter
     def progress(self, progress):
-        """Sets the progress of this RimeJobDataContinuousIncrementalTest.
+        """Sets the progress of this JobDataContinuousIncrementalTest.
 
 
-        :param progress: The progress of this RimeJobDataContinuousIncrementalTest.  # noqa: E501
+        :param progress: The progress of this JobDataContinuousIncrementalTest.  # noqa: E501
         :type: RimeContinuousTestJobProgress
         """
 
         self._progress = progress
 
     def to_dict(self):
         """Returns the model properties as a dict"""
@@ -132,15 +132,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeJobDataContinuousIncrementalTest, dict):
+        if issubclass(JobDataContinuousIncrementalTest, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -148,15 +148,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeJobDataContinuousIncrementalTest):
+        if not isinstance(other, JobDataContinuousIncrementalTest):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_data_stress_test.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_models_response.py`

 * *Files 22% similar despite different names*

```diff
@@ -11,113 +11,113 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeJobDataStressTest(object):
+class RimeListModelsResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'project_id': 'RimeUUID',
-        'test_run_id': 'str',
-        'progress': 'RimeStressTestJobProgress'
+        'models': 'list[RimeModelWithOwnerDetails]',
+        'next_page_token': 'str',
+        'has_more': 'bool'
     }
 
     attribute_map = {
-        'project_id': 'projectId',
-        'test_run_id': 'testRunId',
-        'progress': 'progress'
+        'models': 'models',
+        'next_page_token': 'nextPageToken',
+        'has_more': 'hasMore'
     }
 
-    def __init__(self, project_id=None, test_run_id=None, progress=None):  # noqa: E501
-        """RimeJobDataStressTest - a model defined in Swagger"""  # noqa: E501
-        self._project_id = None
-        self._test_run_id = None
-        self._progress = None
+    def __init__(self, models=None, next_page_token=None, has_more=None):  # noqa: E501
+        """RimeListModelsResponse - a model defined in Swagger"""  # noqa: E501
+        self._models = None
+        self._next_page_token = None
+        self._has_more = None
         self.discriminator = None
-        if project_id is not None:
-            self.project_id = project_id
-        if test_run_id is not None:
-            self.test_run_id = test_run_id
-        if progress is not None:
-            self.progress = progress
+        if models is not None:
+            self.models = models
+        if next_page_token is not None:
+            self.next_page_token = next_page_token
+        if has_more is not None:
+            self.has_more = has_more
 
     @property
-    def project_id(self):
-        """Gets the project_id of this RimeJobDataStressTest.  # noqa: E501
+    def models(self):
+        """Gets the models of this RimeListModelsResponse.  # noqa: E501
 
 
-        :return: The project_id of this RimeJobDataStressTest.  # noqa: E501
-        :rtype: RimeUUID
+        :return: The models of this RimeListModelsResponse.  # noqa: E501
+        :rtype: list[RimeModelWithOwnerDetails]
         """
-        return self._project_id
+        return self._models
 
-    @project_id.setter
-    def project_id(self, project_id):
-        """Sets the project_id of this RimeJobDataStressTest.
+    @models.setter
+    def models(self, models):
+        """Sets the models of this RimeListModelsResponse.
 
 
-        :param project_id: The project_id of this RimeJobDataStressTest.  # noqa: E501
-        :type: RimeUUID
+        :param models: The models of this RimeListModelsResponse.  # noqa: E501
+        :type: list[RimeModelWithOwnerDetails]
         """
 
-        self._project_id = project_id
+        self._models = models
 
     @property
-    def test_run_id(self):
-        """Gets the test_run_id of this RimeJobDataStressTest.  # noqa: E501
+    def next_page_token(self):
+        """Gets the next_page_token of this RimeListModelsResponse.  # noqa: E501
 
 
-        :return: The test_run_id of this RimeJobDataStressTest.  # noqa: E501
+        :return: The next_page_token of this RimeListModelsResponse.  # noqa: E501
         :rtype: str
         """
-        return self._test_run_id
+        return self._next_page_token
 
-    @test_run_id.setter
-    def test_run_id(self, test_run_id):
-        """Sets the test_run_id of this RimeJobDataStressTest.
+    @next_page_token.setter
+    def next_page_token(self, next_page_token):
+        """Sets the next_page_token of this RimeListModelsResponse.
 
 
-        :param test_run_id: The test_run_id of this RimeJobDataStressTest.  # noqa: E501
+        :param next_page_token: The next_page_token of this RimeListModelsResponse.  # noqa: E501
         :type: str
         """
 
-        self._test_run_id = test_run_id
+        self._next_page_token = next_page_token
 
     @property
-    def progress(self):
-        """Gets the progress of this RimeJobDataStressTest.  # noqa: E501
+    def has_more(self):
+        """Gets the has_more of this RimeListModelsResponse.  # noqa: E501
 
 
-        :return: The progress of this RimeJobDataStressTest.  # noqa: E501
-        :rtype: RimeStressTestJobProgress
+        :return: The has_more of this RimeListModelsResponse.  # noqa: E501
+        :rtype: bool
         """
-        return self._progress
+        return self._has_more
 
-    @progress.setter
-    def progress(self, progress):
-        """Sets the progress of this RimeJobDataStressTest.
+    @has_more.setter
+    def has_more(self, has_more):
+        """Sets the has_more of this RimeListModelsResponse.
 
 
-        :param progress: The progress of this RimeJobDataStressTest.  # noqa: E501
-        :type: RimeStressTestJobProgress
+        :param has_more: The has_more of this RimeListModelsResponse.  # noqa: E501
+        :type: bool
         """
 
-        self._progress = progress
+        self._has_more = has_more
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -132,15 +132,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeJobDataStressTest, dict):
+        if issubclass(RimeListModelsResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -148,15 +148,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeJobDataStressTest):
+        if not isinstance(other, RimeListModelsResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_metadata.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_metadata.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_job_view.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_job_view.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_license_feature.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_license_feature.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_license_limit.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_license_limit.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_limit_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_limit_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_limit_status_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_limit_status_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_agents_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_agents_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_api_tokens_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_api_tokens_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_current_user_roles_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_current_user_roles_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_datasets_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_datasets_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_request_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_request_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_detection_events_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_enabled_features_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_enabled_features_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_file_scan_results_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_file_scan_results_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_images_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_images_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_images_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_images_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_request_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_request_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_request_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_workspace.py`

 * *Files 26% similar despite different names*

```diff
@@ -11,119 +11,171 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeListJobsRequestQuery(object):
+class RimeWorkspace(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'selected_statuses': 'list[StatedbJobStatus]',
-        'selected_types': 'list[RimeJobType]',
-        'object_id': 'str'
+        'name': 'str',
+        'agent_ids': 'list[RimeUUID]',
+        'default_agent_id': 'RimeUUID',
+        'workspace_id': 'RimeUUID',
+        'description': 'str'
     }
 
     attribute_map = {
-        'selected_statuses': 'selectedStatuses',
-        'selected_types': 'selectedTypes',
-        'object_id': 'objectId'
+        'name': 'name',
+        'agent_ids': 'agentIds',
+        'default_agent_id': 'defaultAgentId',
+        'workspace_id': 'workspaceId',
+        'description': 'description'
     }
 
-    def __init__(self, selected_statuses=None, selected_types=None, object_id=None):  # noqa: E501
-        """RimeListJobsRequestQuery - a model defined in Swagger"""  # noqa: E501
-        self._selected_statuses = None
-        self._selected_types = None
-        self._object_id = None
+    def __init__(self, name=None, agent_ids=None, default_agent_id=None, workspace_id=None, description=None):  # noqa: E501
+        """RimeWorkspace - a model defined in Swagger"""  # noqa: E501
+        self._name = None
+        self._agent_ids = None
+        self._default_agent_id = None
+        self._workspace_id = None
+        self._description = None
         self.discriminator = None
-        if selected_statuses is not None:
-            self.selected_statuses = selected_statuses
-        if selected_types is not None:
-            self.selected_types = selected_types
-        if object_id is not None:
-            self.object_id = object_id
+        if name is not None:
+            self.name = name
+        if agent_ids is not None:
+            self.agent_ids = agent_ids
+        if default_agent_id is not None:
+            self.default_agent_id = default_agent_id
+        if workspace_id is not None:
+            self.workspace_id = workspace_id
+        if description is not None:
+            self.description = description
 
     @property
-    def selected_statuses(self):
-        """Gets the selected_statuses of this RimeListJobsRequestQuery.  # noqa: E501
+    def name(self):
+        """Gets the name of this RimeWorkspace.  # noqa: E501
 
-        Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.  # noqa: E501
+        Name of the Workspace.  # noqa: E501
 
-        :return: The selected_statuses of this RimeListJobsRequestQuery.  # noqa: E501
-        :rtype: list[StatedbJobStatus]
+        :return: The name of this RimeWorkspace.  # noqa: E501
+        :rtype: str
+        """
+        return self._name
+
+    @name.setter
+    def name(self, name):
+        """Sets the name of this RimeWorkspace.
+
+        Name of the Workspace.  # noqa: E501
+
+        :param name: The name of this RimeWorkspace.  # noqa: E501
+        :type: str
+        """
+
+        self._name = name
+
+    @property
+    def agent_ids(self):
+        """Gets the agent_ids of this RimeWorkspace.  # noqa: E501
+
+        List of Agent IDs that can be used by the Workspace.  # noqa: E501
+
+        :return: The agent_ids of this RimeWorkspace.  # noqa: E501
+        :rtype: list[RimeUUID]
+        """
+        return self._agent_ids
+
+    @agent_ids.setter
+    def agent_ids(self, agent_ids):
+        """Sets the agent_ids of this RimeWorkspace.
+
+        List of Agent IDs that can be used by the Workspace.  # noqa: E501
+
+        :param agent_ids: The agent_ids of this RimeWorkspace.  # noqa: E501
+        :type: list[RimeUUID]
+        """
+
+        self._agent_ids = agent_ids
+
+    @property
+    def default_agent_id(self):
+        """Gets the default_agent_id of this RimeWorkspace.  # noqa: E501
+
+
+        :return: The default_agent_id of this RimeWorkspace.  # noqa: E501
+        :rtype: RimeUUID
         """
-        return self._selected_statuses
+        return self._default_agent_id
 
-    @selected_statuses.setter
-    def selected_statuses(self, selected_statuses):
-        """Sets the selected_statuses of this RimeListJobsRequestQuery.
+    @default_agent_id.setter
+    def default_agent_id(self, default_agent_id):
+        """Sets the default_agent_id of this RimeWorkspace.
 
-        Specifies a set of statuses. The query only returns results with a status in the specified set. Specify no statuses to return all results.  # noqa: E501
 
-        :param selected_statuses: The selected_statuses of this RimeListJobsRequestQuery.  # noqa: E501
-        :type: list[StatedbJobStatus]
+        :param default_agent_id: The default_agent_id of this RimeWorkspace.  # noqa: E501
+        :type: RimeUUID
         """
 
-        self._selected_statuses = selected_statuses
+        self._default_agent_id = default_agent_id
 
     @property
-    def selected_types(self):
-        """Gets the selected_types of this RimeListJobsRequestQuery.  # noqa: E501
+    def workspace_id(self):
+        """Gets the workspace_id of this RimeWorkspace.  # noqa: E501
 
-        Specifies a set of types. The query only returns jobs with types in the specified set. Specify no types to return all results.  # noqa: E501
 
-        :return: The selected_types of this RimeListJobsRequestQuery.  # noqa: E501
-        :rtype: list[RimeJobType]
+        :return: The workspace_id of this RimeWorkspace.  # noqa: E501
+        :rtype: RimeUUID
         """
-        return self._selected_types
+        return self._workspace_id
 
-    @selected_types.setter
-    def selected_types(self, selected_types):
-        """Sets the selected_types of this RimeListJobsRequestQuery.
+    @workspace_id.setter
+    def workspace_id(self, workspace_id):
+        """Sets the workspace_id of this RimeWorkspace.
 
-        Specifies a set of types. The query only returns jobs with types in the specified set. Specify no types to return all results.  # noqa: E501
 
-        :param selected_types: The selected_types of this RimeListJobsRequestQuery.  # noqa: E501
-        :type: list[RimeJobType]
+        :param workspace_id: The workspace_id of this RimeWorkspace.  # noqa: E501
+        :type: RimeUUID
         """
 
-        self._selected_types = selected_types
+        self._workspace_id = workspace_id
 
     @property
-    def object_id(self):
-        """Gets the object_id of this RimeListJobsRequestQuery.  # noqa: E501
+    def description(self):
+        """Gets the description of this RimeWorkspace.  # noqa: E501
 
-        Specifies an object ID. The query only returns results matching the specified object ID. Object IDs vary by job type. For example, stress test jobs have a project ID and continuous incremental test jobs have a firewall ID.  # noqa: E501
+        Description of the Workspace.  # noqa: E501
 
-        :return: The object_id of this RimeListJobsRequestQuery.  # noqa: E501
+        :return: The description of this RimeWorkspace.  # noqa: E501
         :rtype: str
         """
-        return self._object_id
+        return self._description
 
-    @object_id.setter
-    def object_id(self, object_id):
-        """Sets the object_id of this RimeListJobsRequestQuery.
+    @description.setter
+    def description(self, description):
+        """Sets the description of this RimeWorkspace.
 
-        Specifies an object ID. The query only returns results matching the specified object ID. Object IDs vary by job type. For example, stress test jobs have a project ID and continuous incremental test jobs have a firewall ID.  # noqa: E501
+        Description of the Workspace.  # noqa: E501
 
-        :param object_id: The object_id of this RimeListJobsRequestQuery.  # noqa: E501
+        :param description: The description of this RimeWorkspace.  # noqa: E501
         :type: str
         """
 
-        self._object_id = object_id
+        self._description = description
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -138,15 +190,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeListJobsRequestQuery, dict):
+        if issubclass(RimeWorkspace, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -154,15 +206,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeListJobsRequestQuery):
+        if not isinstance(other, RimeWorkspace):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_jobs_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_users_response.py`

 * *Files 10% similar despite different names*

```diff
@@ -11,111 +11,109 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeListJobsResponse(object):
+class RimeListUsersResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'jobs': 'list[RimeJobMetadata]',
+        'users': 'list[UserUserDetail]',
         'next_page_token': 'str',
         'has_more': 'bool'
     }
 
     attribute_map = {
-        'jobs': 'jobs',
+        'users': 'users',
         'next_page_token': 'nextPageToken',
         'has_more': 'hasMore'
     }
 
-    def __init__(self, jobs=None, next_page_token=None, has_more=None):  # noqa: E501
-        """RimeListJobsResponse - a model defined in Swagger"""  # noqa: E501
-        self._jobs = None
+    def __init__(self, users=None, next_page_token=None, has_more=None):  # noqa: E501
+        """RimeListUsersResponse - a model defined in Swagger"""  # noqa: E501
+        self._users = None
         self._next_page_token = None
         self._has_more = None
         self.discriminator = None
-        if jobs is not None:
-            self.jobs = jobs
+        if users is not None:
+            self.users = users
         if next_page_token is not None:
             self.next_page_token = next_page_token
         if has_more is not None:
             self.has_more = has_more
 
     @property
-    def jobs(self):
-        """Gets the jobs of this RimeListJobsResponse.  # noqa: E501
+    def users(self):
+        """Gets the users of this RimeListUsersResponse.  # noqa: E501
 
 
-        :return: The jobs of this RimeListJobsResponse.  # noqa: E501
-        :rtype: list[RimeJobMetadata]
+        :return: The users of this RimeListUsersResponse.  # noqa: E501
+        :rtype: list[UserUserDetail]
         """
-        return self._jobs
+        return self._users
 
-    @jobs.setter
-    def jobs(self, jobs):
-        """Sets the jobs of this RimeListJobsResponse.
+    @users.setter
+    def users(self, users):
+        """Sets the users of this RimeListUsersResponse.
 
 
-        :param jobs: The jobs of this RimeListJobsResponse.  # noqa: E501
-        :type: list[RimeJobMetadata]
+        :param users: The users of this RimeListUsersResponse.  # noqa: E501
+        :type: list[UserUserDetail]
         """
 
-        self._jobs = jobs
+        self._users = users
 
     @property
     def next_page_token(self):
-        """Gets the next_page_token of this RimeListJobsResponse.  # noqa: E501
+        """Gets the next_page_token of this RimeListUsersResponse.  # noqa: E501
 
-        Use this page token in your next ListJobs call to access the next page of results.  # noqa: E501
 
-        :return: The next_page_token of this RimeListJobsResponse.  # noqa: E501
+        :return: The next_page_token of this RimeListUsersResponse.  # noqa: E501
         :rtype: str
         """
         return self._next_page_token
 
     @next_page_token.setter
     def next_page_token(self, next_page_token):
-        """Sets the next_page_token of this RimeListJobsResponse.
+        """Sets the next_page_token of this RimeListUsersResponse.
 
-        Use this page token in your next ListJobs call to access the next page of results.  # noqa: E501
 
-        :param next_page_token: The next_page_token of this RimeListJobsResponse.  # noqa: E501
+        :param next_page_token: The next_page_token of this RimeListUsersResponse.  # noqa: E501
         :type: str
         """
 
         self._next_page_token = next_page_token
 
     @property
     def has_more(self):
-        """Gets the has_more of this RimeListJobsResponse.  # noqa: E501
+        """Gets the has_more of this RimeListUsersResponse.  # noqa: E501
 
 
-        :return: The has_more of this RimeListJobsResponse.  # noqa: E501
+        :return: The has_more of this RimeListUsersResponse.  # noqa: E501
         :rtype: bool
         """
         return self._has_more
 
     @has_more.setter
     def has_more(self, has_more):
-        """Sets the has_more of this RimeListJobsResponse.
+        """Sets the has_more of this RimeListUsersResponse.
 
 
-        :param has_more: The has_more of this RimeListJobsResponse.  # noqa: E501
+        :param has_more: The has_more of this RimeListUsersResponse.  # noqa: E501
         :type: bool
         """
 
         self._has_more = has_more
 
     def to_dict(self):
         """Returns the model properties as a dict"""
@@ -134,15 +132,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeListJobsResponse, dict):
+        if issubclass(RimeListUsersResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -150,15 +148,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeListJobsResponse):
+        if not isinstance(other, RimeListUsersResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_metric_identifiers_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_metric_identifiers_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_model_cards_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_model_cards_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_models_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_response.py`

 * *Files 19% similar despite different names*

```diff
@@ -11,109 +11,109 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeListModelsResponse(object):
+class RimeListWorkspacesResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'models': 'list[RimeModelWithOwnerDetails]',
+        'workspaces': 'list[RimeWorkspace]',
         'next_page_token': 'str',
         'has_more': 'bool'
     }
 
     attribute_map = {
-        'models': 'models',
+        'workspaces': 'workspaces',
         'next_page_token': 'nextPageToken',
         'has_more': 'hasMore'
     }
 
-    def __init__(self, models=None, next_page_token=None, has_more=None):  # noqa: E501
-        """RimeListModelsResponse - a model defined in Swagger"""  # noqa: E501
-        self._models = None
+    def __init__(self, workspaces=None, next_page_token=None, has_more=None):  # noqa: E501
+        """RimeListWorkspacesResponse - a model defined in Swagger"""  # noqa: E501
+        self._workspaces = None
         self._next_page_token = None
         self._has_more = None
         self.discriminator = None
-        if models is not None:
-            self.models = models
+        if workspaces is not None:
+            self.workspaces = workspaces
         if next_page_token is not None:
             self.next_page_token = next_page_token
         if has_more is not None:
             self.has_more = has_more
 
     @property
-    def models(self):
-        """Gets the models of this RimeListModelsResponse.  # noqa: E501
+    def workspaces(self):
+        """Gets the workspaces of this RimeListWorkspacesResponse.  # noqa: E501
 
 
-        :return: The models of this RimeListModelsResponse.  # noqa: E501
-        :rtype: list[RimeModelWithOwnerDetails]
+        :return: The workspaces of this RimeListWorkspacesResponse.  # noqa: E501
+        :rtype: list[RimeWorkspace]
         """
-        return self._models
+        return self._workspaces
 
-    @models.setter
-    def models(self, models):
-        """Sets the models of this RimeListModelsResponse.
+    @workspaces.setter
+    def workspaces(self, workspaces):
+        """Sets the workspaces of this RimeListWorkspacesResponse.
 
 
-        :param models: The models of this RimeListModelsResponse.  # noqa: E501
-        :type: list[RimeModelWithOwnerDetails]
+        :param workspaces: The workspaces of this RimeListWorkspacesResponse.  # noqa: E501
+        :type: list[RimeWorkspace]
         """
 
-        self._models = models
+        self._workspaces = workspaces
 
     @property
     def next_page_token(self):
-        """Gets the next_page_token of this RimeListModelsResponse.  # noqa: E501
+        """Gets the next_page_token of this RimeListWorkspacesResponse.  # noqa: E501
 
 
-        :return: The next_page_token of this RimeListModelsResponse.  # noqa: E501
+        :return: The next_page_token of this RimeListWorkspacesResponse.  # noqa: E501
         :rtype: str
         """
         return self._next_page_token
 
     @next_page_token.setter
     def next_page_token(self, next_page_token):
-        """Sets the next_page_token of this RimeListModelsResponse.
+        """Sets the next_page_token of this RimeListWorkspacesResponse.
 
 
-        :param next_page_token: The next_page_token of this RimeListModelsResponse.  # noqa: E501
+        :param next_page_token: The next_page_token of this RimeListWorkspacesResponse.  # noqa: E501
         :type: str
         """
 
         self._next_page_token = next_page_token
 
     @property
     def has_more(self):
-        """Gets the has_more of this RimeListModelsResponse.  # noqa: E501
+        """Gets the has_more of this RimeListWorkspacesResponse.  # noqa: E501
 
 
-        :return: The has_more of this RimeListModelsResponse.  # noqa: E501
+        :return: The has_more of this RimeListWorkspacesResponse.  # noqa: E501
         :rtype: bool
         """
         return self._has_more
 
     @has_more.setter
     def has_more(self, has_more):
-        """Sets the has_more of this RimeListModelsResponse.
+        """Sets the has_more of this RimeListWorkspacesResponse.
 
 
-        :param has_more: The has_more of this RimeListModelsResponse.  # noqa: E501
+        :param has_more: The has_more of this RimeListWorkspacesResponse.  # noqa: E501
         :type: bool
         """
 
         self._has_more = has_more
 
     def to_dict(self):
         """Returns the model properties as a dict"""
@@ -132,15 +132,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeListModelsResponse, dict):
+        if issubclass(RimeListWorkspacesResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -148,15 +148,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeListModelsResponse):
+        if not isinstance(other, RimeListWorkspacesResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_monitors_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_monitors_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_notifications_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_notifications_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_prediction_sets_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_prediction_sets_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_uploaded_file_urls_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_uploaded_file_urls_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_users_of_workspace_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_users_of_workspace_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_users_request_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_users_request_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_users_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_run_incremental_config.py`

 * *Files 21% similar despite different names*

```diff
@@ -11,113 +11,89 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeListUsersResponse(object):
+class TestrunTestRunIncrementalConfig(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'users': 'list[UserUserDetail]',
-        'next_page_token': 'str',
-        'has_more': 'bool'
+        'eval_dataset_id': 'str',
+        'run_time_info': 'RuntimeinfoRunTimeInfo'
     }
 
     attribute_map = {
-        'users': 'users',
-        'next_page_token': 'nextPageToken',
-        'has_more': 'hasMore'
+        'eval_dataset_id': 'evalDatasetId',
+        'run_time_info': 'runTimeInfo'
     }
 
-    def __init__(self, users=None, next_page_token=None, has_more=None):  # noqa: E501
-        """RimeListUsersResponse - a model defined in Swagger"""  # noqa: E501
-        self._users = None
-        self._next_page_token = None
-        self._has_more = None
+    def __init__(self, eval_dataset_id=None, run_time_info=None):  # noqa: E501
+        """TestrunTestRunIncrementalConfig - a model defined in Swagger"""  # noqa: E501
+        self._eval_dataset_id = None
+        self._run_time_info = None
         self.discriminator = None
-        if users is not None:
-            self.users = users
-        if next_page_token is not None:
-            self.next_page_token = next_page_token
-        if has_more is not None:
-            self.has_more = has_more
+        if eval_dataset_id is not None:
+            self.eval_dataset_id = eval_dataset_id
+        if run_time_info is not None:
+            self.run_time_info = run_time_info
 
     @property
-    def users(self):
-        """Gets the users of this RimeListUsersResponse.  # noqa: E501
+    def eval_dataset_id(self):
+        """Gets the eval_dataset_id of this TestrunTestRunIncrementalConfig.  # noqa: E501
 
+        Uniquely specifies an evaluation Dataset.  # noqa: E501
 
-        :return: The users of this RimeListUsersResponse.  # noqa: E501
-        :rtype: list[UserUserDetail]
-        """
-        return self._users
-
-    @users.setter
-    def users(self, users):
-        """Sets the users of this RimeListUsersResponse.
-
-
-        :param users: The users of this RimeListUsersResponse.  # noqa: E501
-        :type: list[UserUserDetail]
-        """
-
-        self._users = users
-
-    @property
-    def next_page_token(self):
-        """Gets the next_page_token of this RimeListUsersResponse.  # noqa: E501
-
-
-        :return: The next_page_token of this RimeListUsersResponse.  # noqa: E501
+        :return: The eval_dataset_id of this TestrunTestRunIncrementalConfig.  # noqa: E501
         :rtype: str
         """
-        return self._next_page_token
+        return self._eval_dataset_id
 
-    @next_page_token.setter
-    def next_page_token(self, next_page_token):
-        """Sets the next_page_token of this RimeListUsersResponse.
+    @eval_dataset_id.setter
+    def eval_dataset_id(self, eval_dataset_id):
+        """Sets the eval_dataset_id of this TestrunTestRunIncrementalConfig.
 
+        Uniquely specifies an evaluation Dataset.  # noqa: E501
 
-        :param next_page_token: The next_page_token of this RimeListUsersResponse.  # noqa: E501
+        :param eval_dataset_id: The eval_dataset_id of this TestrunTestRunIncrementalConfig.  # noqa: E501
         :type: str
         """
 
-        self._next_page_token = next_page_token
+        self._eval_dataset_id = eval_dataset_id
 
     @property
-    def has_more(self):
-        """Gets the has_more of this RimeListUsersResponse.  # noqa: E501
+    def run_time_info(self):
+        """Gets the run_time_info of this TestrunTestRunIncrementalConfig.  # noqa: E501
 
 
-        :return: The has_more of this RimeListUsersResponse.  # noqa: E501
-        :rtype: bool
+        :return: The run_time_info of this TestrunTestRunIncrementalConfig.  # noqa: E501
+        :rtype: RuntimeinfoRunTimeInfo
         """
-        return self._has_more
+        return self._run_time_info
 
-    @has_more.setter
-    def has_more(self, has_more):
-        """Sets the has_more of this RimeListUsersResponse.
+    @run_time_info.setter
+    def run_time_info(self, run_time_info):
+        """Sets the run_time_info of this TestrunTestRunIncrementalConfig.
 
 
-        :param has_more: The has_more of this RimeListUsersResponse.  # noqa: E501
-        :type: bool
+        :param run_time_info: The run_time_info of this TestrunTestRunIncrementalConfig.  # noqa: E501
+        :type: RuntimeinfoRunTimeInfo
         """
 
-        self._has_more = has_more
+        self._run_time_info = run_time_info
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -132,15 +108,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeListUsersResponse, dict):
+        if issubclass(TestrunTestRunIncrementalConfig, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -148,15 +124,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeListUsersResponse):
+        if not isinstance(other, TestrunTestRunIncrementalConfig):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspace_integrations_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspace_integrations_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspace_tags_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspace_tags_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_request_query.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_request_query.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_list_workspaces_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_runs_response.py`

 * *Files 18% similar despite different names*

```diff
@@ -11,109 +11,115 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeListWorkspacesResponse(object):
+class TestrunresultListTestRunsResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'workspaces': 'list[RimeWorkspace]',
+        'test_runs': 'list[TestrunresultTestRunDetail]',
         'next_page_token': 'str',
         'has_more': 'bool'
     }
 
     attribute_map = {
-        'workspaces': 'workspaces',
+        'test_runs': 'testRuns',
         'next_page_token': 'nextPageToken',
         'has_more': 'hasMore'
     }
 
-    def __init__(self, workspaces=None, next_page_token=None, has_more=None):  # noqa: E501
-        """RimeListWorkspacesResponse - a model defined in Swagger"""  # noqa: E501
-        self._workspaces = None
+    def __init__(self, test_runs=None, next_page_token=None, has_more=None):  # noqa: E501
+        """TestrunresultListTestRunsResponse - a model defined in Swagger"""  # noqa: E501
+        self._test_runs = None
         self._next_page_token = None
         self._has_more = None
         self.discriminator = None
-        if workspaces is not None:
-            self.workspaces = workspaces
+        if test_runs is not None:
+            self.test_runs = test_runs
         if next_page_token is not None:
             self.next_page_token = next_page_token
         if has_more is not None:
             self.has_more = has_more
 
     @property
-    def workspaces(self):
-        """Gets the workspaces of this RimeListWorkspacesResponse.  # noqa: E501
+    def test_runs(self):
+        """Gets the test_runs of this TestrunresultListTestRunsResponse.  # noqa: E501
 
+        The details of the test runs.  # noqa: E501
 
-        :return: The workspaces of this RimeListWorkspacesResponse.  # noqa: E501
-        :rtype: list[RimeWorkspace]
+        :return: The test_runs of this TestrunresultListTestRunsResponse.  # noqa: E501
+        :rtype: list[TestrunresultTestRunDetail]
         """
-        return self._workspaces
+        return self._test_runs
 
-    @workspaces.setter
-    def workspaces(self, workspaces):
-        """Sets the workspaces of this RimeListWorkspacesResponse.
+    @test_runs.setter
+    def test_runs(self, test_runs):
+        """Sets the test_runs of this TestrunresultListTestRunsResponse.
 
+        The details of the test runs.  # noqa: E501
 
-        :param workspaces: The workspaces of this RimeListWorkspacesResponse.  # noqa: E501
-        :type: list[RimeWorkspace]
+        :param test_runs: The test_runs of this TestrunresultListTestRunsResponse.  # noqa: E501
+        :type: list[TestrunresultTestRunDetail]
         """
 
-        self._workspaces = workspaces
+        self._test_runs = test_runs
 
     @property
     def next_page_token(self):
-        """Gets the next_page_token of this RimeListWorkspacesResponse.  # noqa: E501
+        """Gets the next_page_token of this TestrunresultListTestRunsResponse.  # noqa: E501
 
+        A token representing the next page from the list returned by a ListTestRuns query.  # noqa: E501
 
-        :return: The next_page_token of this RimeListWorkspacesResponse.  # noqa: E501
+        :return: The next_page_token of this TestrunresultListTestRunsResponse.  # noqa: E501
         :rtype: str
         """
         return self._next_page_token
 
     @next_page_token.setter
     def next_page_token(self, next_page_token):
-        """Sets the next_page_token of this RimeListWorkspacesResponse.
+        """Sets the next_page_token of this TestrunresultListTestRunsResponse.
 
+        A token representing the next page from the list returned by a ListTestRuns query.  # noqa: E501
 
-        :param next_page_token: The next_page_token of this RimeListWorkspacesResponse.  # noqa: E501
+        :param next_page_token: The next_page_token of this TestrunresultListTestRunsResponse.  # noqa: E501
         :type: str
         """
 
         self._next_page_token = next_page_token
 
     @property
     def has_more(self):
-        """Gets the has_more of this RimeListWorkspacesResponse.  # noqa: E501
+        """Gets the has_more of this TestrunresultListTestRunsResponse.  # noqa: E501
 
+        A Boolean that specifies whether there are more test runs to return.  # noqa: E501
 
-        :return: The has_more of this RimeListWorkspacesResponse.  # noqa: E501
+        :return: The has_more of this TestrunresultListTestRunsResponse.  # noqa: E501
         :rtype: bool
         """
         return self._has_more
 
     @has_more.setter
     def has_more(self, has_more):
-        """Sets the has_more of this RimeListWorkspacesResponse.
+        """Sets the has_more of this TestrunresultListTestRunsResponse.
 
+        A Boolean that specifies whether there are more test runs to return.  # noqa: E501
 
-        :param has_more: The has_more of this RimeListWorkspacesResponse.  # noqa: E501
+        :param has_more: The has_more of this TestrunresultListTestRunsResponse.  # noqa: E501
         :type: bool
         """
 
         self._has_more = has_more
 
     def to_dict(self):
         """Returns the model properties as a dict"""
@@ -132,15 +138,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeListWorkspacesResponse, dict):
+        if issubclass(TestrunresultListTestRunsResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -148,15 +154,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeListWorkspacesResponse):
+        if not isinstance(other, TestrunresultListTestRunsResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_long_description_tab.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_long_description_tab.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_managed_image.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_managed_image.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_managed_image_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_managed_image_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_model_card.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_model_card.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_model_task.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_model_task.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_model_with_owner_details.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_model_with_owner_details.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_monitor_data_point.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_monitor_data_point.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_named_double.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_named_double.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_order.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_order.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_parent_role_subject_role_pair.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_parent_role_subject_role_pair.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_data_stream_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_data_stream_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_dataset_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_dataset_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_internal_agent_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_internal_agent_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_model_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_model_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_register_prediction_set_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_register_prediction_set_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_remove_user_from_workspace_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_remove_user_from_workspace_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_reset_password_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_reset_password_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_resolve_detection_event_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_resolve_detection_event_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_ri_email_recipient.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_ri_email_recipient.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_ri_plan.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_ri_plan.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_safe_url.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_safe_url.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_send_ri_email_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_send_ri_email_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_severity.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_severity.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_severity_counts.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_severity_counts.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_sort_spec.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_sort_spec.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_continuous_test_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_file_scan_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_start_stress_test_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_start_stress_test_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_store_datapoints_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_store_datapoints_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_store_predictions_request_prediction.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_store_predictions_request_prediction.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_store_predictions_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_store_predictions_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_str_list.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_str_list.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_stress_test_job_progress.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_stress_test_job_progress.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_subject_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_subject_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_suggestion.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_suggestion.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_sync_image_tag_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_sync_image_tag_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_table_column.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_table_column.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_table_column_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_table_column_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_tag.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_tag.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_termination_reason.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_termination_reason.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_case_monitor_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_case_monitor_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_case_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_case_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_metric.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_metric.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_metric_category.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_metric_category.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_run_progress.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_run_progress.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_task_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_task_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_test_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_test_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_time_interval.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_time_interval.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_token_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_token_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_build_info_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_workspace_response.py`

 * *Files 5% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeUpdateBuildInfoResponse(object):
+class RimeUpdateWorkspaceResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
@@ -30,15 +30,15 @@
     swagger_types = {
     }
 
     attribute_map = {
     }
 
     def __init__(self):  # noqa: E501
-        """RimeUpdateBuildInfoResponse - a model defined in Swagger"""  # noqa: E501
+        """RimeUpdateWorkspaceResponse - a model defined in Swagger"""  # noqa: E501
         self.discriminator = None
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
@@ -54,15 +54,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeUpdateBuildInfoResponse, dict):
+        if issubclass(RimeUpdateWorkspaceResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -70,15 +70,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeUpdateBuildInfoResponse):
+        if not isinstance(other, RimeUpdateWorkspaceResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_firewall_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_firewall_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_integration_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_integration_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_model_card_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_model_card_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_monitor_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_monitor_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_notification_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_notification_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_user_of_workspace_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_user_of_workspace_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_user_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_user_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_workspace_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_upsert_feature_flags_response.py`

 * *Files 6% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeUpdateWorkspaceResponse(object):
+class RimeUpsertFeatureFlagsResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
@@ -30,15 +30,15 @@
     swagger_types = {
     }
 
     attribute_map = {
     }
 
     def __init__(self):  # noqa: E501
-        """RimeUpdateWorkspaceResponse - a model defined in Swagger"""  # noqa: E501
+        """RimeUpsertFeatureFlagsResponse - a model defined in Swagger"""  # noqa: E501
         self.discriminator = None
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
@@ -54,15 +54,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeUpdateWorkspaceResponse, dict):
+        if issubclass(RimeUpsertFeatureFlagsResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -70,15 +70,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeUpdateWorkspaceResponse):
+        if not isinstance(other, RimeUpsertFeatureFlagsResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_update_workspace_tag_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_update_workspace_tag_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_upsert_feature_flags_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_role.py`

 * *Files 9% similar despite different names*

```diff
@@ -11,34 +11,42 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeUpsertFeatureFlagsResponse(object):
+class UserRole(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
+
+    """
+    allowed enum values
+    """
+    UNSPECIFIED = "ROLE_UNSPECIFIED"
+    ADMIN = "ROLE_ADMIN"
+    TRIAL_USER = "ROLE_TRIAL_USER"
+    SUPPORT = "ROLE_SUPPORT"
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
     }
 
     attribute_map = {
     }
 
     def __init__(self):  # noqa: E501
-        """RimeUpsertFeatureFlagsResponse - a model defined in Swagger"""  # noqa: E501
+        """UserRole - a model defined in Swagger"""  # noqa: E501
         self.discriminator = None
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
@@ -54,15 +62,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeUpsertFeatureFlagsResponse, dict):
+        if issubclass(UserRole, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -70,15 +78,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeUpsertFeatureFlagsResponse):
+        if not isinstance(other, UserRole):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_upsert_job_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_file_info.py`

 * *Files 15% similar despite different names*

```diff
@@ -11,61 +11,64 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeUpsertJobResponse(object):
+class TestrunDataFileInfo(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'job': 'RimeJobMetadata'
+        'path': 'str'
     }
 
     attribute_map = {
-        'job': 'job'
+        'path': 'path'
     }
 
-    def __init__(self, job=None):  # noqa: E501
-        """RimeUpsertJobResponse - a model defined in Swagger"""  # noqa: E501
-        self._job = None
+    def __init__(self, path=None):  # noqa: E501
+        """TestrunDataFileInfo - a model defined in Swagger"""  # noqa: E501
+        self._path = None
         self.discriminator = None
-        if job is not None:
-            self.job = job
+        self.path = path
 
     @property
-    def job(self):
-        """Gets the job of this RimeUpsertJobResponse.  # noqa: E501
+    def path(self):
+        """Gets the path of this TestrunDataFileInfo.  # noqa: E501
 
+        The path to the data file.  # noqa: E501
 
-        :return: The job of this RimeUpsertJobResponse.  # noqa: E501
-        :rtype: RimeJobMetadata
+        :return: The path of this TestrunDataFileInfo.  # noqa: E501
+        :rtype: str
         """
-        return self._job
+        return self._path
 
-    @job.setter
-    def job(self, job):
-        """Sets the job of this RimeUpsertJobResponse.
+    @path.setter
+    def path(self, path):
+        """Sets the path of this TestrunDataFileInfo.
 
+        The path to the data file.  # noqa: E501
 
-        :param job: The job of this RimeUpsertJobResponse.  # noqa: E501
-        :type: RimeJobMetadata
+        :param path: The path of this TestrunDataFileInfo.  # noqa: E501
+        :type: str
         """
+        if path is None:
+            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
 
-        self._job = job
+        self._path = path
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -80,15 +83,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeUpsertJobResponse, dict):
+        if issubclass(TestrunDataFileInfo, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -96,15 +99,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeUpsertJobResponse):
+        if not isinstance(other, TestrunDataFileInfo):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_detail_with_role.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_detail_with_role.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_role.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_role.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_with_role.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_with_role.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_user_write_mask.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_user_write_mask.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_uuid.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_validate_test_config_response.py`

 * *Files 20% similar despite different names*

```diff
@@ -11,63 +11,35 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeUUID(object):
+class RimeValidateTestConfigResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'uuid': 'str'
     }
 
     attribute_map = {
-        'uuid': 'uuid'
     }
 
-    def __init__(self, uuid=None):  # noqa: E501
-        """RimeUUID - a model defined in Swagger"""  # noqa: E501
-        self._uuid = None
+    def __init__(self):  # noqa: E501
+        """RimeValidateTestConfigResponse - a model defined in Swagger"""  # noqa: E501
         self.discriminator = None
-        if uuid is not None:
-            self.uuid = uuid
-
-    @property
-    def uuid(self):
-        """Gets the uuid of this RimeUUID.  # noqa: E501
-
-        Unique object ID.  # noqa: E501
-
-        :return: The uuid of this RimeUUID.  # noqa: E501
-        :rtype: str
-        """
-        return self._uuid
-
-    @uuid.setter
-    def uuid(self, uuid):
-        """Sets the uuid of this RimeUUID.
-
-        Unique object ID.  # noqa: E501
-
-        :param uuid: The uuid of this RimeUUID.  # noqa: E501
-        :type: str
-        """
-
-        self._uuid = uuid
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -82,15 +54,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeUUID, dict):
+        if issubclass(RimeValidateTestConfigResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -98,15 +70,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeUUID):
+        if not isinstance(other, RimeValidateTestConfigResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_validate_test_config_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_sensitivity.py`

 * *Files 11% similar despite different names*

```diff
@@ -11,34 +11,42 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeValidateTestConfigResponse(object):
+class TestrunTestSensitivity(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
+
+    """
+    allowed enum values
+    """
+    UNSPECIFIED = "TEST_SENSITIVITY_UNSPECIFIED"
+    LESS_SENSITIVE = "TEST_SENSITIVITY_LESS_SENSITIVE"
+    DEFAULT = "TEST_SENSITIVITY_DEFAULT"
+    MORE_SENSITIVE = "TEST_SENSITIVITY_MORE_SENSITIVE"
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
     }
 
     attribute_map = {
     }
 
     def __init__(self):  # noqa: E501
-        """RimeValidateTestConfigResponse - a model defined in Swagger"""  # noqa: E501
+        """TestrunTestSensitivity - a model defined in Swagger"""  # noqa: E501
         self.discriminator = None
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
@@ -54,15 +62,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeValidateTestConfigResponse, dict):
+        if issubclass(TestrunTestSensitivity, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -70,15 +78,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeValidateTestConfigResponse):
+        if not isinstance(other, TestrunTestSensitivity):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/rime_workspace.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/rime_workspace_write_mask.py`

 * *Files 19% similar despite different names*

```diff
@@ -11,168 +11,144 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class RimeWorkspace(object):
+class RimeWorkspaceWriteMask(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'name': 'str',
-        'agent_ids': 'list[RimeUUID]',
-        'default_agent_id': 'RimeUUID',
-        'workspace_id': 'RimeUUID',
-        'description': 'str'
+        'name': 'bool',
+        'agent_ids': 'bool',
+        'default_agent_id': 'bool',
+        'description': 'bool'
     }
 
     attribute_map = {
         'name': 'name',
         'agent_ids': 'agentIds',
         'default_agent_id': 'defaultAgentId',
-        'workspace_id': 'workspaceId',
         'description': 'description'
     }
 
-    def __init__(self, name=None, agent_ids=None, default_agent_id=None, workspace_id=None, description=None):  # noqa: E501
-        """RimeWorkspace - a model defined in Swagger"""  # noqa: E501
+    def __init__(self, name=None, agent_ids=None, default_agent_id=None, description=None):  # noqa: E501
+        """RimeWorkspaceWriteMask - a model defined in Swagger"""  # noqa: E501
         self._name = None
         self._agent_ids = None
         self._default_agent_id = None
-        self._workspace_id = None
         self._description = None
         self.discriminator = None
         if name is not None:
             self.name = name
         if agent_ids is not None:
             self.agent_ids = agent_ids
         if default_agent_id is not None:
             self.default_agent_id = default_agent_id
-        if workspace_id is not None:
-            self.workspace_id = workspace_id
         if description is not None:
             self.description = description
 
     @property
     def name(self):
-        """Gets the name of this RimeWorkspace.  # noqa: E501
+        """Gets the name of this RimeWorkspaceWriteMask.  # noqa: E501
 
-        Name of the Workspace.  # noqa: E501
+        Specifies whether to update name.  # noqa: E501
 
-        :return: The name of this RimeWorkspace.  # noqa: E501
-        :rtype: str
+        :return: The name of this RimeWorkspaceWriteMask.  # noqa: E501
+        :rtype: bool
         """
         return self._name
 
     @name.setter
     def name(self, name):
-        """Sets the name of this RimeWorkspace.
+        """Sets the name of this RimeWorkspaceWriteMask.
 
-        Name of the Workspace.  # noqa: E501
+        Specifies whether to update name.  # noqa: E501
 
-        :param name: The name of this RimeWorkspace.  # noqa: E501
-        :type: str
+        :param name: The name of this RimeWorkspaceWriteMask.  # noqa: E501
+        :type: bool
         """
 
         self._name = name
 
     @property
     def agent_ids(self):
-        """Gets the agent_ids of this RimeWorkspace.  # noqa: E501
+        """Gets the agent_ids of this RimeWorkspaceWriteMask.  # noqa: E501
 
-        List of Agent IDs that can be used by the Workspace.  # noqa: E501
+        Specifies whether to update list of Agent IDs.  # noqa: E501
 
-        :return: The agent_ids of this RimeWorkspace.  # noqa: E501
-        :rtype: list[RimeUUID]
+        :return: The agent_ids of this RimeWorkspaceWriteMask.  # noqa: E501
+        :rtype: bool
         """
         return self._agent_ids
 
     @agent_ids.setter
     def agent_ids(self, agent_ids):
-        """Sets the agent_ids of this RimeWorkspace.
+        """Sets the agent_ids of this RimeWorkspaceWriteMask.
 
-        List of Agent IDs that can be used by the Workspace.  # noqa: E501
+        Specifies whether to update list of Agent IDs.  # noqa: E501
 
-        :param agent_ids: The agent_ids of this RimeWorkspace.  # noqa: E501
-        :type: list[RimeUUID]
+        :param agent_ids: The agent_ids of this RimeWorkspaceWriteMask.  # noqa: E501
+        :type: bool
         """
 
         self._agent_ids = agent_ids
 
     @property
     def default_agent_id(self):
-        """Gets the default_agent_id of this RimeWorkspace.  # noqa: E501
+        """Gets the default_agent_id of this RimeWorkspaceWriteMask.  # noqa: E501
 
+        Specifies whether to update default Agent ID.  # noqa: E501
 
-        :return: The default_agent_id of this RimeWorkspace.  # noqa: E501
-        :rtype: RimeUUID
+        :return: The default_agent_id of this RimeWorkspaceWriteMask.  # noqa: E501
+        :rtype: bool
         """
         return self._default_agent_id
 
     @default_agent_id.setter
     def default_agent_id(self, default_agent_id):
-        """Sets the default_agent_id of this RimeWorkspace.
+        """Sets the default_agent_id of this RimeWorkspaceWriteMask.
 
+        Specifies whether to update default Agent ID.  # noqa: E501
 
-        :param default_agent_id: The default_agent_id of this RimeWorkspace.  # noqa: E501
-        :type: RimeUUID
+        :param default_agent_id: The default_agent_id of this RimeWorkspaceWriteMask.  # noqa: E501
+        :type: bool
         """
 
         self._default_agent_id = default_agent_id
 
     @property
-    def workspace_id(self):
-        """Gets the workspace_id of this RimeWorkspace.  # noqa: E501
-
-
-        :return: The workspace_id of this RimeWorkspace.  # noqa: E501
-        :rtype: RimeUUID
-        """
-        return self._workspace_id
-
-    @workspace_id.setter
-    def workspace_id(self, workspace_id):
-        """Sets the workspace_id of this RimeWorkspace.
-
-
-        :param workspace_id: The workspace_id of this RimeWorkspace.  # noqa: E501
-        :type: RimeUUID
-        """
-
-        self._workspace_id = workspace_id
-
-    @property
     def description(self):
-        """Gets the description of this RimeWorkspace.  # noqa: E501
+        """Gets the description of this RimeWorkspaceWriteMask.  # noqa: E501
 
-        Description of the Workspace.  # noqa: E501
+        Specifies whether to update description.  # noqa: E501
 
-        :return: The description of this RimeWorkspace.  # noqa: E501
-        :rtype: str
+        :return: The description of this RimeWorkspaceWriteMask.  # noqa: E501
+        :rtype: bool
         """
         return self._description
 
     @description.setter
     def description(self, description):
-        """Sets the description of this RimeWorkspace.
+        """Sets the description of this RimeWorkspaceWriteMask.
 
-        Description of the Workspace.  # noqa: E501
+        Specifies whether to update description.  # noqa: E501
 
-        :param description: The description of this RimeWorkspace.  # noqa: E501
-        :type: str
+        :param description: The description of this RimeWorkspaceWriteMask.  # noqa: E501
+        :type: bool
         """
 
         self._description = description
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
@@ -190,15 +166,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(RimeWorkspace, dict):
+        if issubclass(RimeWorkspaceWriteMask, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -206,15 +182,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, RimeWorkspace):
+        if not isinstance(other, RimeWorkspaceWriteMask):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/riskscore_risk_category_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/riskscore_risk_category_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/riskscore_risk_score.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/riskscore_risk_score.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/role_users_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/role_users_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/role_workspace_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/role_workspace_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_custom_image_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_resource_request.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_resource_request.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/runtimeinfo_run_time_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/runtimeinfo_run_time_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemadatacollector_prediction.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemadatacollector_prediction.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemaintegration_integration_variable.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemaintegration_integration_variable.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemamonitor_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemamonitor_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/schemanotification_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/schemanotification_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/security_event_details_flagged_datapoint.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/security_event_details_flagged_datapoint.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/security_event_details_security_event_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/security_event_details_security_event_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/statedb_job_status.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/statedb_job_status.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_datapoints_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_datapoints_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_latest_logs_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_latest_logs_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_predictions_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stream_result_of_rime_get_predictions_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/stresstests_project_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/stresstests_project_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/test_run_metrics_category_summary_metric.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/test_run_metrics_category_summary_metric.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/test_run_metrics_model_perf_metric.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/test_run_metrics_model_perf_metric.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/test_run_progress_test_batch_progress.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/test_run_progress_test_batch_progress.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_annotated_test_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_annotated_test_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_connection_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_connection_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_collector_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_collector_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_file_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/users_user_id_uuid_body.py`

 * *Files 18% similar despite different names*

```diff
@@ -11,64 +11,87 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class TestrunDataFileInfo(object):
+class UsersUserIdUuidBody(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'path': 'str'
+        'user': 'V1usersuserIdUuidUser',
+        'mask': 'RimeUserWriteMask'
     }
 
     attribute_map = {
-        'path': 'path'
+        'user': 'user',
+        'mask': 'mask'
     }
 
-    def __init__(self, path=None):  # noqa: E501
-        """TestrunDataFileInfo - a model defined in Swagger"""  # noqa: E501
-        self._path = None
+    def __init__(self, user=None, mask=None):  # noqa: E501
+        """UsersUserIdUuidBody - a model defined in Swagger"""  # noqa: E501
+        self._user = None
+        self._mask = None
         self.discriminator = None
-        self.path = path
+        if user is not None:
+            self.user = user
+        if mask is not None:
+            self.mask = mask
 
     @property
-    def path(self):
-        """Gets the path of this TestrunDataFileInfo.  # noqa: E501
+    def user(self):
+        """Gets the user of this UsersUserIdUuidBody.  # noqa: E501
 
-        The path to the data file.  # noqa: E501
 
-        :return: The path of this TestrunDataFileInfo.  # noqa: E501
-        :rtype: str
+        :return: The user of this UsersUserIdUuidBody.  # noqa: E501
+        :rtype: V1usersuserIdUuidUser
         """
-        return self._path
+        return self._user
 
-    @path.setter
-    def path(self, path):
-        """Sets the path of this TestrunDataFileInfo.
+    @user.setter
+    def user(self, user):
+        """Sets the user of this UsersUserIdUuidBody.
 
-        The path to the data file.  # noqa: E501
 
-        :param path: The path of this TestrunDataFileInfo.  # noqa: E501
-        :type: str
+        :param user: The user of this UsersUserIdUuidBody.  # noqa: E501
+        :type: V1usersuserIdUuidUser
         """
-        if path is None:
-            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
 
-        self._path = path
+        self._user = user
+
+    @property
+    def mask(self):
+        """Gets the mask of this UsersUserIdUuidBody.  # noqa: E501
+
+
+        :return: The mask of this UsersUserIdUuidBody.  # noqa: E501
+        :rtype: RimeUserWriteMask
+        """
+        return self._mask
+
+    @mask.setter
+    def mask(self, mask):
+        """Sets the mask of this UsersUserIdUuidBody.
+
+
+        :param mask: The mask of this UsersUserIdUuidBody.  # noqa: E501
+        :type: RimeUserWriteMask
+        """
+
+        self._mask = mask
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -83,15 +106,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(TestrunDataFileInfo, dict):
+        if issubclass(UsersUserIdUuidBody, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -99,15 +122,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, TestrunDataFileInfo):
+        if not isinstance(other, UsersUserIdUuidBody):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_info_params.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_info_params.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_loading_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_loading_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_data_profiling.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_data_profiling.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_delta_lake_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_delta_lake_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_hugging_face_data_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_hugging_face_data_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_model_profiling.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_model_profiling.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_pred_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_pred_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_prediction_params.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_prediction_params.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_profiling_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_profiling_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_single_data_info.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_single_data_info.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_category.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_category.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_category_type.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_category_type.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_run_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_run_config.py`

 * *Files 1% similar despite different names*

```diff
@@ -50,16 +50,15 @@
         self._run_name = None
         self._model_id = None
         self._data_info = None
         self._run_time_info = None
         self._profiling_config = None
         self._test_suite_config = None
         self.discriminator = None
-        if run_name is not None:
-            self.run_name = run_name
+        self.run_name = run_name
         self.model_id = model_id
         self.data_info = data_info
         if run_time_info is not None:
             self.run_time_info = run_time_info
         if profiling_config is not None:
             self.profiling_config = profiling_config
         if test_suite_config is not None:
@@ -81,14 +80,16 @@
         """Sets the run_name of this TestrunTestRunConfig.
 
         Name for this Test Run.  # noqa: E501
 
         :param run_name: The run_name of this TestrunTestRunConfig.  # noqa: E501
         :type: str
         """
+        if run_name is None:
+            raise ValueError("Invalid value for `run_name`, must not be `None`")  # noqa: E501
 
         self._run_name = run_name
 
     @property
     def model_id(self):
         """Gets the model_id of this TestrunTestRunConfig.  # noqa: E501
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_run_incremental_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body.py`

 * *Files 26% similar despite different names*

```diff
@@ -11,89 +11,89 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class TestrunTestRunIncrementalConfig(object):
+class UsersUserUserIdUuidBody(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'eval_dataset_id': 'str',
-        'run_time_info': 'RuntimeinfoRunTimeInfo'
+        'project_id': 'object',
+        'user': 'V1projectsprojectIdUuidroleusersuserUserIdUuidUser'
     }
 
     attribute_map = {
-        'eval_dataset_id': 'evalDatasetId',
-        'run_time_info': 'runTimeInfo'
+        'project_id': 'projectId',
+        'user': 'user'
     }
 
-    def __init__(self, eval_dataset_id=None, run_time_info=None):  # noqa: E501
-        """TestrunTestRunIncrementalConfig - a model defined in Swagger"""  # noqa: E501
-        self._eval_dataset_id = None
-        self._run_time_info = None
+    def __init__(self, project_id=None, user=None):  # noqa: E501
+        """UsersUserUserIdUuidBody - a model defined in Swagger"""  # noqa: E501
+        self._project_id = None
+        self._user = None
         self.discriminator = None
-        if eval_dataset_id is not None:
-            self.eval_dataset_id = eval_dataset_id
-        if run_time_info is not None:
-            self.run_time_info = run_time_info
+        if project_id is not None:
+            self.project_id = project_id
+        if user is not None:
+            self.user = user
 
     @property
-    def eval_dataset_id(self):
-        """Gets the eval_dataset_id of this TestrunTestRunIncrementalConfig.  # noqa: E501
+    def project_id(self):
+        """Gets the project_id of this UsersUserUserIdUuidBody.  # noqa: E501
 
-        Uniquely specifies an evaluation Dataset.  # noqa: E501
+        Uniquely specifies a Project.  # noqa: E501
 
-        :return: The eval_dataset_id of this TestrunTestRunIncrementalConfig.  # noqa: E501
-        :rtype: str
+        :return: The project_id of this UsersUserUserIdUuidBody.  # noqa: E501
+        :rtype: object
         """
-        return self._eval_dataset_id
+        return self._project_id
 
-    @eval_dataset_id.setter
-    def eval_dataset_id(self, eval_dataset_id):
-        """Sets the eval_dataset_id of this TestrunTestRunIncrementalConfig.
+    @project_id.setter
+    def project_id(self, project_id):
+        """Sets the project_id of this UsersUserUserIdUuidBody.
 
-        Uniquely specifies an evaluation Dataset.  # noqa: E501
+        Uniquely specifies a Project.  # noqa: E501
 
-        :param eval_dataset_id: The eval_dataset_id of this TestrunTestRunIncrementalConfig.  # noqa: E501
-        :type: str
+        :param project_id: The project_id of this UsersUserUserIdUuidBody.  # noqa: E501
+        :type: object
         """
 
-        self._eval_dataset_id = eval_dataset_id
+        self._project_id = project_id
 
     @property
-    def run_time_info(self):
-        """Gets the run_time_info of this TestrunTestRunIncrementalConfig.  # noqa: E501
+    def user(self):
+        """Gets the user of this UsersUserUserIdUuidBody.  # noqa: E501
 
 
-        :return: The run_time_info of this TestrunTestRunIncrementalConfig.  # noqa: E501
-        :rtype: RuntimeinfoRunTimeInfo
+        :return: The user of this UsersUserUserIdUuidBody.  # noqa: E501
+        :rtype: V1projectsprojectIdUuidroleusersuserUserIdUuidUser
         """
-        return self._run_time_info
+        return self._user
 
-    @run_time_info.setter
-    def run_time_info(self, run_time_info):
-        """Sets the run_time_info of this TestrunTestRunIncrementalConfig.
+    @user.setter
+    def user(self, user):
+        """Sets the user of this UsersUserUserIdUuidBody.
 
 
-        :param run_time_info: The run_time_info of this TestrunTestRunIncrementalConfig.  # noqa: E501
-        :type: RuntimeinfoRunTimeInfo
+        :param user: The user of this UsersUserUserIdUuidBody.  # noqa: E501
+        :type: V1projectsprojectIdUuidroleusersuserUserIdUuidUser
         """
 
-        self._run_time_info = run_time_info
+        self._user = user
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -108,15 +108,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(TestrunTestRunIncrementalConfig, dict):
+        if issubclass(UsersUserUserIdUuidBody, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -124,15 +124,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, TestrunTestRunIncrementalConfig):
+        if not isinstance(other, UsersUserUserIdUuidBody):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_sensitivity.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_run_response.py`

 * *Files 17% similar despite different names*

```diff
@@ -11,43 +11,61 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class TestrunTestSensitivity(object):
+class TestrunresultGetTestRunResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
-
-    """
-    allowed enum values
-    """
-    UNSPECIFIED = "TEST_SENSITIVITY_UNSPECIFIED"
-    LESS_SENSITIVE = "TEST_SENSITIVITY_LESS_SENSITIVE"
-    DEFAULT = "TEST_SENSITIVITY_DEFAULT"
-    MORE_SENSITIVE = "TEST_SENSITIVITY_MORE_SENSITIVE"
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
+        'test_run': 'TestrunresultTestRunDetail'
     }
 
     attribute_map = {
+        'test_run': 'testRun'
     }
 
-    def __init__(self):  # noqa: E501
-        """TestrunTestSensitivity - a model defined in Swagger"""  # noqa: E501
+    def __init__(self, test_run=None):  # noqa: E501
+        """TestrunresultGetTestRunResponse - a model defined in Swagger"""  # noqa: E501
+        self._test_run = None
         self.discriminator = None
+        if test_run is not None:
+            self.test_run = test_run
+
+    @property
+    def test_run(self):
+        """Gets the test_run of this TestrunresultGetTestRunResponse.  # noqa: E501
+
+
+        :return: The test_run of this TestrunresultGetTestRunResponse.  # noqa: E501
+        :rtype: TestrunresultTestRunDetail
+        """
+        return self._test_run
+
+    @test_run.setter
+    def test_run(self, test_run):
+        """Sets the test_run of this TestrunresultGetTestRunResponse.
+
+
+        :param test_run: The test_run of this TestrunresultGetTestRunResponse.  # noqa: E501
+        :type: TestrunresultTestRunDetail
+        """
+
+        self._test_run = test_run
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -62,15 +80,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(TestrunTestSensitivity, dict):
+        if issubclass(TestrunresultGetTestRunResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -78,15 +96,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, TestrunTestSensitivity):
+        if not isinstance(other, TestrunresultGetTestRunResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrun_test_suite_config.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrun_test_suite_config.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_batch_result_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_batch_result_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_feature_result_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_feature_result_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_config_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_config_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_get_test_run_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_rename_test_run_response.py`

 * *Files 17% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class TestrunresultGetTestRunResponse(object):
+class TestrunresultRenameTestRunResponse(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
@@ -32,36 +32,36 @@
     }
 
     attribute_map = {
         'test_run': 'testRun'
     }
 
     def __init__(self, test_run=None):  # noqa: E501
-        """TestrunresultGetTestRunResponse - a model defined in Swagger"""  # noqa: E501
+        """TestrunresultRenameTestRunResponse - a model defined in Swagger"""  # noqa: E501
         self._test_run = None
         self.discriminator = None
         if test_run is not None:
             self.test_run = test_run
 
     @property
     def test_run(self):
-        """Gets the test_run of this TestrunresultGetTestRunResponse.  # noqa: E501
+        """Gets the test_run of this TestrunresultRenameTestRunResponse.  # noqa: E501
 
 
-        :return: The test_run of this TestrunresultGetTestRunResponse.  # noqa: E501
+        :return: The test_run of this TestrunresultRenameTestRunResponse.  # noqa: E501
         :rtype: TestrunresultTestRunDetail
         """
         return self._test_run
 
     @test_run.setter
     def test_run(self, test_run):
-        """Sets the test_run of this TestrunresultGetTestRunResponse.
+        """Sets the test_run of this TestrunresultRenameTestRunResponse.
 
 
-        :param test_run: The test_run of this TestrunresultGetTestRunResponse.  # noqa: E501
+        :param test_run: The test_run of this TestrunresultRenameTestRunResponse.  # noqa: E501
         :type: TestrunresultTestRunDetail
         """
 
         self._test_run = test_run
 
     def to_dict(self):
         """Returns the model properties as a dict"""
@@ -80,15 +80,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(TestrunresultGetTestRunResponse, dict):
+        if issubclass(TestrunresultRenameTestRunResponse, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -96,15 +96,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, TestrunresultGetTestRunResponse):
+        if not isinstance(other, TestrunresultRenameTestRunResponse):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_batch_results_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_batch_results_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_feature_results_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_feature_results_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_summary_tests_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_summary_tests_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_cases_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_cases_response.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_list_test_runs_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_case_display.py`

 * *Files 20% similar despite different names*

```diff
@@ -11,119 +11,117 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class TestrunresultListTestRunsResponse(object):
+class TestrunresultTestCaseDisplay(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'test_runs': 'list[TestrunresultTestRunDetail]',
-        'next_page_token': 'str',
-        'has_more': 'bool'
+        'table_info': 'str',
+        'details': 'str',
+        'details_layout': 'list[str]'
     }
 
     attribute_map = {
-        'test_runs': 'testRuns',
-        'next_page_token': 'nextPageToken',
-        'has_more': 'hasMore'
+        'table_info': 'tableInfo',
+        'details': 'details',
+        'details_layout': 'detailsLayout'
     }
 
-    def __init__(self, test_runs=None, next_page_token=None, has_more=None):  # noqa: E501
-        """TestrunresultListTestRunsResponse - a model defined in Swagger"""  # noqa: E501
-        self._test_runs = None
-        self._next_page_token = None
-        self._has_more = None
+    def __init__(self, table_info=None, details=None, details_layout=None):  # noqa: E501
+        """TestrunresultTestCaseDisplay - a model defined in Swagger"""  # noqa: E501
+        self._table_info = None
+        self._details = None
+        self._details_layout = None
         self.discriminator = None
-        if test_runs is not None:
-            self.test_runs = test_runs
-        if next_page_token is not None:
-            self.next_page_token = next_page_token
-        if has_more is not None:
-            self.has_more = has_more
+        if table_info is not None:
+            self.table_info = table_info
+        if details is not None:
+            self.details = details
+        if details_layout is not None:
+            self.details_layout = details_layout
 
     @property
-    def test_runs(self):
-        """Gets the test_runs of this TestrunresultListTestRunsResponse.  # noqa: E501
+    def table_info(self):
+        """Gets the table_info of this TestrunresultTestCaseDisplay.  # noqa: E501
 
-        The details of the test runs.  # noqa: E501
+        Table info contains information for displaying the test case in a table in the FE.  # noqa: E501
 
-        :return: The test_runs of this TestrunresultListTestRunsResponse.  # noqa: E501
-        :rtype: list[TestrunresultTestRunDetail]
+        :return: The table_info of this TestrunresultTestCaseDisplay.  # noqa: E501
+        :rtype: str
         """
-        return self._test_runs
+        return self._table_info
 
-    @test_runs.setter
-    def test_runs(self, test_runs):
-        """Sets the test_runs of this TestrunresultListTestRunsResponse.
+    @table_info.setter
+    def table_info(self, table_info):
+        """Sets the table_info of this TestrunresultTestCaseDisplay.
 
-        The details of the test runs.  # noqa: E501
+        Table info contains information for displaying the test case in a table in the FE.  # noqa: E501
 
-        :param test_runs: The test_runs of this TestrunresultListTestRunsResponse.  # noqa: E501
-        :type: list[TestrunresultTestRunDetail]
+        :param table_info: The table_info of this TestrunresultTestCaseDisplay.  # noqa: E501
+        :type: str
         """
 
-        self._test_runs = test_runs
+        self._table_info = table_info
 
     @property
-    def next_page_token(self):
-        """Gets the next_page_token of this TestrunresultListTestRunsResponse.  # noqa: E501
+    def details(self):
+        """Gets the details of this TestrunresultTestCaseDisplay.  # noqa: E501
 
-        A token representing the next page from the list returned by a ListTestRuns query.  # noqa: E501
+        Details includes ML-specified details for the test case. This can include graphs, HTML, etc.  # noqa: E501
 
-        :return: The next_page_token of this TestrunresultListTestRunsResponse.  # noqa: E501
+        :return: The details of this TestrunresultTestCaseDisplay.  # noqa: E501
         :rtype: str
         """
-        return self._next_page_token
+        return self._details
 
-    @next_page_token.setter
-    def next_page_token(self, next_page_token):
-        """Sets the next_page_token of this TestrunresultListTestRunsResponse.
+    @details.setter
+    def details(self, details):
+        """Sets the details of this TestrunresultTestCaseDisplay.
 
-        A token representing the next page from the list returned by a ListTestRuns query.  # noqa: E501
+        Details includes ML-specified details for the test case. This can include graphs, HTML, etc.  # noqa: E501
 
-        :param next_page_token: The next_page_token of this TestrunresultListTestRunsResponse.  # noqa: E501
+        :param details: The details of this TestrunresultTestCaseDisplay.  # noqa: E501
         :type: str
         """
 
-        self._next_page_token = next_page_token
+        self._details = details
 
     @property
-    def has_more(self):
-        """Gets the has_more of this TestrunresultListTestRunsResponse.  # noqa: E501
+    def details_layout(self):
+        """Gets the details_layout of this TestrunresultTestCaseDisplay.  # noqa: E501
 
-        A Boolean that specifies whether there are more test runs to return.  # noqa: E501
 
-        :return: The has_more of this TestrunresultListTestRunsResponse.  # noqa: E501
-        :rtype: bool
+        :return: The details_layout of this TestrunresultTestCaseDisplay.  # noqa: E501
+        :rtype: list[str]
         """
-        return self._has_more
+        return self._details_layout
 
-    @has_more.setter
-    def has_more(self, has_more):
-        """Sets the has_more of this TestrunresultListTestRunsResponse.
+    @details_layout.setter
+    def details_layout(self, details_layout):
+        """Sets the details_layout of this TestrunresultTestCaseDisplay.
 
-        A Boolean that specifies whether there are more test runs to return.  # noqa: E501
 
-        :param has_more: The has_more of this TestrunresultListTestRunsResponse.  # noqa: E501
-        :type: bool
+        :param details_layout: The details_layout of this TestrunresultTestCaseDisplay.  # noqa: E501
+        :type: list[str]
         """
 
-        self._has_more = has_more
+        self._details_layout = details_layout
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -138,15 +136,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(TestrunresultListTestRunsResponse, dict):
+        if issubclass(TestrunresultTestCaseDisplay, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -154,15 +152,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, TestrunresultListTestRunsResponse):
+        if not isinstance(other, TestrunresultTestCaseDisplay):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_rename_test_run_response.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_private_info.py`

 * *Files 22% similar despite different names*

```diff
@@ -11,61 +11,61 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class TestrunresultRenameTestRunResponse(object):
+class UserPrivateInfo(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'test_run': 'TestrunresultTestRunDetail'
+        'favorite_projects': 'list[UserFavoriteProjects]'
     }
 
     attribute_map = {
-        'test_run': 'testRun'
+        'favorite_projects': 'favoriteProjects'
     }
 
-    def __init__(self, test_run=None):  # noqa: E501
-        """TestrunresultRenameTestRunResponse - a model defined in Swagger"""  # noqa: E501
-        self._test_run = None
+    def __init__(self, favorite_projects=None):  # noqa: E501
+        """UserPrivateInfo - a model defined in Swagger"""  # noqa: E501
+        self._favorite_projects = None
         self.discriminator = None
-        if test_run is not None:
-            self.test_run = test_run
+        if favorite_projects is not None:
+            self.favorite_projects = favorite_projects
 
     @property
-    def test_run(self):
-        """Gets the test_run of this TestrunresultRenameTestRunResponse.  # noqa: E501
+    def favorite_projects(self):
+        """Gets the favorite_projects of this UserPrivateInfo.  # noqa: E501
 
 
-        :return: The test_run of this TestrunresultRenameTestRunResponse.  # noqa: E501
-        :rtype: TestrunresultTestRunDetail
+        :return: The favorite_projects of this UserPrivateInfo.  # noqa: E501
+        :rtype: list[UserFavoriteProjects]
         """
-        return self._test_run
+        return self._favorite_projects
 
-    @test_run.setter
-    def test_run(self, test_run):
-        """Sets the test_run of this TestrunresultRenameTestRunResponse.
+    @favorite_projects.setter
+    def favorite_projects(self, favorite_projects):
+        """Sets the favorite_projects of this UserPrivateInfo.
 
 
-        :param test_run: The test_run of this TestrunresultRenameTestRunResponse.  # noqa: E501
-        :type: TestrunresultTestRunDetail
+        :param favorite_projects: The favorite_projects of this UserPrivateInfo.  # noqa: E501
+        :type: list[UserFavoriteProjects]
         """
 
-        self._test_run = test_run
+        self._favorite_projects = favorite_projects
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -80,15 +80,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(TestrunresultRenameTestRunResponse, dict):
+        if issubclass(UserPrivateInfo, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -96,15 +96,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, TestrunresultRenameTestRunResponse):
+        if not isinstance(other, UserPrivateInfo):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_result_summary_counts.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_result_summary_counts.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result_display.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_batch_result_display.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_case.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_case.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result_display.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result_display.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_detail.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_detail.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_metrics.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/testrunresult_test_run_metrics.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/the_updates_to_the_monitor_.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/the_updates_to_the_monitor_.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/job_data_stress_test.py`

 * *Files 25% similar despite different names*

```diff
@@ -11,87 +11,113 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class UpsertJobRequestWriteMaskJobData(object):
+class JobDataStressTest(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'stress': 'UpsertJobRequestWriteMaskJobDataStressTest',
-        'continuous_inc': 'UpsertJobRequestWriteMaskJobDataContinuousIncrementalTest'
+        'project_id': 'RimeUUID',
+        'test_run_id': 'str',
+        'progress': 'RimeStressTestJobProgress'
     }
 
     attribute_map = {
-        'stress': 'stress',
-        'continuous_inc': 'continuousInc'
+        'project_id': 'projectId',
+        'test_run_id': 'testRunId',
+        'progress': 'progress'
     }
 
-    def __init__(self, stress=None, continuous_inc=None):  # noqa: E501
-        """UpsertJobRequestWriteMaskJobData - a model defined in Swagger"""  # noqa: E501
-        self._stress = None
-        self._continuous_inc = None
+    def __init__(self, project_id=None, test_run_id=None, progress=None):  # noqa: E501
+        """JobDataStressTest - a model defined in Swagger"""  # noqa: E501
+        self._project_id = None
+        self._test_run_id = None
+        self._progress = None
         self.discriminator = None
-        if stress is not None:
-            self.stress = stress
-        if continuous_inc is not None:
-            self.continuous_inc = continuous_inc
+        if project_id is not None:
+            self.project_id = project_id
+        if test_run_id is not None:
+            self.test_run_id = test_run_id
+        if progress is not None:
+            self.progress = progress
 
     @property
-    def stress(self):
-        """Gets the stress of this UpsertJobRequestWriteMaskJobData.  # noqa: E501
+    def project_id(self):
+        """Gets the project_id of this JobDataStressTest.  # noqa: E501
 
 
-        :return: The stress of this UpsertJobRequestWriteMaskJobData.  # noqa: E501
-        :rtype: UpsertJobRequestWriteMaskJobDataStressTest
+        :return: The project_id of this JobDataStressTest.  # noqa: E501
+        :rtype: RimeUUID
         """
-        return self._stress
+        return self._project_id
 
-    @stress.setter
-    def stress(self, stress):
-        """Sets the stress of this UpsertJobRequestWriteMaskJobData.
+    @project_id.setter
+    def project_id(self, project_id):
+        """Sets the project_id of this JobDataStressTest.
 
 
-        :param stress: The stress of this UpsertJobRequestWriteMaskJobData.  # noqa: E501
-        :type: UpsertJobRequestWriteMaskJobDataStressTest
+        :param project_id: The project_id of this JobDataStressTest.  # noqa: E501
+        :type: RimeUUID
         """
 
-        self._stress = stress
+        self._project_id = project_id
 
     @property
-    def continuous_inc(self):
-        """Gets the continuous_inc of this UpsertJobRequestWriteMaskJobData.  # noqa: E501
+    def test_run_id(self):
+        """Gets the test_run_id of this JobDataStressTest.  # noqa: E501
 
 
-        :return: The continuous_inc of this UpsertJobRequestWriteMaskJobData.  # noqa: E501
-        :rtype: UpsertJobRequestWriteMaskJobDataContinuousIncrementalTest
+        :return: The test_run_id of this JobDataStressTest.  # noqa: E501
+        :rtype: str
         """
-        return self._continuous_inc
+        return self._test_run_id
 
-    @continuous_inc.setter
-    def continuous_inc(self, continuous_inc):
-        """Sets the continuous_inc of this UpsertJobRequestWriteMaskJobData.
+    @test_run_id.setter
+    def test_run_id(self, test_run_id):
+        """Sets the test_run_id of this JobDataStressTest.
 
 
-        :param continuous_inc: The continuous_inc of this UpsertJobRequestWriteMaskJobData.  # noqa: E501
-        :type: UpsertJobRequestWriteMaskJobDataContinuousIncrementalTest
+        :param test_run_id: The test_run_id of this JobDataStressTest.  # noqa: E501
+        :type: str
         """
 
-        self._continuous_inc = continuous_inc
+        self._test_run_id = test_run_id
+
+    @property
+    def progress(self):
+        """Gets the progress of this JobDataStressTest.  # noqa: E501
+
+
+        :return: The progress of this JobDataStressTest.  # noqa: E501
+        :rtype: RimeStressTestJobProgress
+        """
+        return self._progress
+
+    @progress.setter
+    def progress(self, progress):
+        """Sets the progress of this JobDataStressTest.
+
+
+        :param progress: The progress of this JobDataStressTest.  # noqa: E501
+        :type: RimeStressTestJobProgress
+        """
+
+        self._progress = progress
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -106,15 +132,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(UpsertJobRequestWriteMaskJobData, dict):
+        if issubclass(JobDataStressTest, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -122,15 +148,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, UpsertJobRequestWriteMaskJobData):
+        if not isinstance(other, JobDataStressTest):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data_stress_test.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1projectsproject_id_uuidroleusersuser_user_id_uuid_user.py`

 * *Files 26% similar despite different names*

```diff
@@ -11,87 +11,89 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class UpsertJobRequestWriteMaskJobDataStressTest(object):
+class V1projectsprojectIdUuidroleusersuserUserIdUuidUser(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'project_id': 'bool',
-        'test_run_id': 'bool'
+        'user_id': 'object',
+        'user_role': 'RimeActorRole'
     }
 
     attribute_map = {
-        'project_id': 'projectId',
-        'test_run_id': 'testRunId'
+        'user_id': 'userId',
+        'user_role': 'userRole'
     }
 
-    def __init__(self, project_id=None, test_run_id=None):  # noqa: E501
-        """UpsertJobRequestWriteMaskJobDataStressTest - a model defined in Swagger"""  # noqa: E501
-        self._project_id = None
-        self._test_run_id = None
+    def __init__(self, user_id=None, user_role=None):  # noqa: E501
+        """V1projectsprojectIdUuidroleusersuserUserIdUuidUser - a model defined in Swagger"""  # noqa: E501
+        self._user_id = None
+        self._user_role = None
         self.discriminator = None
-        if project_id is not None:
-            self.project_id = project_id
-        if test_run_id is not None:
-            self.test_run_id = test_run_id
+        if user_id is not None:
+            self.user_id = user_id
+        if user_role is not None:
+            self.user_role = user_role
 
     @property
-    def project_id(self):
-        """Gets the project_id of this UpsertJobRequestWriteMaskJobDataStressTest.  # noqa: E501
+    def user_id(self):
+        """Gets the user_id of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.  # noqa: E501
 
+        Unique ID of an object in RIME.  # noqa: E501
 
-        :return: The project_id of this UpsertJobRequestWriteMaskJobDataStressTest.  # noqa: E501
-        :rtype: bool
+        :return: The user_id of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.  # noqa: E501
+        :rtype: object
         """
-        return self._project_id
+        return self._user_id
 
-    @project_id.setter
-    def project_id(self, project_id):
-        """Sets the project_id of this UpsertJobRequestWriteMaskJobDataStressTest.
+    @user_id.setter
+    def user_id(self, user_id):
+        """Sets the user_id of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.
 
+        Unique ID of an object in RIME.  # noqa: E501
 
-        :param project_id: The project_id of this UpsertJobRequestWriteMaskJobDataStressTest.  # noqa: E501
-        :type: bool
+        :param user_id: The user_id of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.  # noqa: E501
+        :type: object
         """
 
-        self._project_id = project_id
+        self._user_id = user_id
 
     @property
-    def test_run_id(self):
-        """Gets the test_run_id of this UpsertJobRequestWriteMaskJobDataStressTest.  # noqa: E501
+    def user_role(self):
+        """Gets the user_role of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.  # noqa: E501
 
 
-        :return: The test_run_id of this UpsertJobRequestWriteMaskJobDataStressTest.  # noqa: E501
-        :rtype: bool
+        :return: The user_role of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.  # noqa: E501
+        :rtype: RimeActorRole
         """
-        return self._test_run_id
+        return self._user_role
 
-    @test_run_id.setter
-    def test_run_id(self, test_run_id):
-        """Sets the test_run_id of this UpsertJobRequestWriteMaskJobDataStressTest.
+    @user_role.setter
+    def user_role(self, user_role):
+        """Sets the user_role of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.
 
 
-        :param test_run_id: The test_run_id of this UpsertJobRequestWriteMaskJobDataStressTest.  # noqa: E501
-        :type: bool
+        :param user_role: The user_role of this V1projectsprojectIdUuidroleusersuserUserIdUuidUser.  # noqa: E501
+        :type: RimeActorRole
         """
 
-        self._test_run_id = test_run_id
+        self._user_role = user_role
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -106,15 +108,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(UpsertJobRequestWriteMaskJobDataStressTest, dict):
+        if issubclass(V1projectsprojectIdUuidroleusersuserUserIdUuidUser, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -122,15 +124,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, UpsertJobRequestWriteMaskJobDataStressTest):
+        if not isinstance(other, V1projectsprojectIdUuidroleusersuserUserIdUuidUser):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/user_favorite_projects.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_favorite_projects.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/user_role.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/integration_integration_level.py`

 * *Files 22% similar despite different names*

```diff
@@ -11,42 +11,41 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class UserRole(object):
+class IntegrationIntegrationLevel(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
 
     """
     allowed enum values
     """
-    UNSPECIFIED = "ROLE_UNSPECIFIED"
-    ADMIN = "ROLE_ADMIN"
-    TRIAL_USER = "ROLE_TRIAL_USER"
-    SUPPORT = "ROLE_SUPPORT"
+    UNSPECIFIED = "INTEGRATION_LEVEL_UNSPECIFIED"
+    ORGANIZATION = "INTEGRATION_LEVEL_ORGANIZATION"
+    WORKSPACE = "INTEGRATION_LEVEL_WORKSPACE"
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
     }
 
     attribute_map = {
     }
 
     def __init__(self):  # noqa: E501
-        """UserRole - a model defined in Swagger"""  # noqa: E501
+        """IntegrationIntegrationLevel - a model defined in Swagger"""  # noqa: E501
         self.discriminator = None
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
@@ -62,15 +61,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(UserRole, dict):
+        if issubclass(IntegrationIntegrationLevel, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -78,15 +77,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, UserRole):
+        if not isinstance(other, IntegrationIntegrationLevel):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/user_user_detail.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/user_user_detail.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/users_user_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body1.py`

 * *Files 12% similar despite different names*

```diff
@@ -11,87 +11,89 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class UsersUserIdUuidBody(object):
+class UsersUserUserIdUuidBody1(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'user': 'V1usersuserIdUuidUser',
-        'mask': 'RimeUserWriteMask'
+        'workspace_id': 'object',
+        'user': 'V1projectsprojectIdUuidroleusersuserUserIdUuidUser'
     }
 
     attribute_map = {
-        'user': 'user',
-        'mask': 'mask'
+        'workspace_id': 'workspaceId',
+        'user': 'user'
     }
 
-    def __init__(self, user=None, mask=None):  # noqa: E501
-        """UsersUserIdUuidBody - a model defined in Swagger"""  # noqa: E501
+    def __init__(self, workspace_id=None, user=None):  # noqa: E501
+        """UsersUserUserIdUuidBody1 - a model defined in Swagger"""  # noqa: E501
+        self._workspace_id = None
         self._user = None
-        self._mask = None
         self.discriminator = None
+        if workspace_id is not None:
+            self.workspace_id = workspace_id
         if user is not None:
             self.user = user
-        if mask is not None:
-            self.mask = mask
 
     @property
-    def user(self):
-        """Gets the user of this UsersUserIdUuidBody.  # noqa: E501
+    def workspace_id(self):
+        """Gets the workspace_id of this UsersUserUserIdUuidBody1.  # noqa: E501
 
+        Unique ID of an object in RIME.  # noqa: E501
 
-        :return: The user of this UsersUserIdUuidBody.  # noqa: E501
-        :rtype: V1usersuserIdUuidUser
+        :return: The workspace_id of this UsersUserUserIdUuidBody1.  # noqa: E501
+        :rtype: object
         """
-        return self._user
+        return self._workspace_id
 
-    @user.setter
-    def user(self, user):
-        """Sets the user of this UsersUserIdUuidBody.
+    @workspace_id.setter
+    def workspace_id(self, workspace_id):
+        """Sets the workspace_id of this UsersUserUserIdUuidBody1.
 
+        Unique ID of an object in RIME.  # noqa: E501
 
-        :param user: The user of this UsersUserIdUuidBody.  # noqa: E501
-        :type: V1usersuserIdUuidUser
+        :param workspace_id: The workspace_id of this UsersUserUserIdUuidBody1.  # noqa: E501
+        :type: object
         """
 
-        self._user = user
+        self._workspace_id = workspace_id
 
     @property
-    def mask(self):
-        """Gets the mask of this UsersUserIdUuidBody.  # noqa: E501
+    def user(self):
+        """Gets the user of this UsersUserUserIdUuidBody1.  # noqa: E501
 
 
-        :return: The mask of this UsersUserIdUuidBody.  # noqa: E501
-        :rtype: RimeUserWriteMask
+        :return: The user of this UsersUserUserIdUuidBody1.  # noqa: E501
+        :rtype: V1projectsprojectIdUuidroleusersuserUserIdUuidUser
         """
-        return self._mask
+        return self._user
 
-    @mask.setter
-    def mask(self, mask):
-        """Sets the mask of this UsersUserIdUuidBody.
+    @user.setter
+    def user(self, user):
+        """Sets the user of this UsersUserUserIdUuidBody1.
 
 
-        :param mask: The mask of this UsersUserIdUuidBody.  # noqa: E501
-        :type: RimeUserWriteMask
+        :param user: The user of this UsersUserUserIdUuidBody1.  # noqa: E501
+        :type: V1projectsprojectIdUuidroleusersuserUserIdUuidUser
         """
 
-        self._mask = mask
+        self._user = user
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -106,15 +108,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(UsersUserIdUuidBody, dict):
+        if issubclass(UsersUserUserIdUuidBody1, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -122,15 +124,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, UsersUserIdUuidBody):
+        if not isinstance(other, UsersUserUserIdUuidBody1):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/workspace_id_uuid_users_body.py`

 * *Files 22% similar despite different names*

```diff
@@ -11,89 +11,91 @@
 """
 
 import pprint
 import re  # noqa: F401
 
 import six
 
-class UsersUserUserIdUuidBody(object):
+class WorkspaceIdUuidUsersBody(object):
     """NOTE: This class is auto generated by the swagger code generator program.
 
     Do not edit the class manually.
     """
     """
     Attributes:
       swagger_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     swagger_types = {
-        'project_id': 'object',
-        'user': 'V1projectsprojectIdUuidroleusersuserUserIdUuidUser'
+        'workspace_id': 'object',
+        'users': 'list[RimeUserWithRole]'
     }
 
     attribute_map = {
-        'project_id': 'projectId',
-        'user': 'user'
+        'workspace_id': 'workspaceId',
+        'users': 'users'
     }
 
-    def __init__(self, project_id=None, user=None):  # noqa: E501
-        """UsersUserUserIdUuidBody - a model defined in Swagger"""  # noqa: E501
-        self._project_id = None
-        self._user = None
+    def __init__(self, workspace_id=None, users=None):  # noqa: E501
+        """WorkspaceIdUuidUsersBody - a model defined in Swagger"""  # noqa: E501
+        self._workspace_id = None
+        self._users = None
         self.discriminator = None
-        if project_id is not None:
-            self.project_id = project_id
-        if user is not None:
-            self.user = user
+        if workspace_id is not None:
+            self.workspace_id = workspace_id
+        if users is not None:
+            self.users = users
 
     @property
-    def project_id(self):
-        """Gets the project_id of this UsersUserUserIdUuidBody.  # noqa: E501
+    def workspace_id(self):
+        """Gets the workspace_id of this WorkspaceIdUuidUsersBody.  # noqa: E501
 
-        Uniquely specifies a Project.  # noqa: E501
+        Unique ID of an object in RIME.  # noqa: E501
 
-        :return: The project_id of this UsersUserUserIdUuidBody.  # noqa: E501
+        :return: The workspace_id of this WorkspaceIdUuidUsersBody.  # noqa: E501
         :rtype: object
         """
-        return self._project_id
+        return self._workspace_id
 
-    @project_id.setter
-    def project_id(self, project_id):
-        """Sets the project_id of this UsersUserUserIdUuidBody.
+    @workspace_id.setter
+    def workspace_id(self, workspace_id):
+        """Sets the workspace_id of this WorkspaceIdUuidUsersBody.
 
-        Uniquely specifies a Project.  # noqa: E501
+        Unique ID of an object in RIME.  # noqa: E501
 
-        :param project_id: The project_id of this UsersUserUserIdUuidBody.  # noqa: E501
+        :param workspace_id: The workspace_id of this WorkspaceIdUuidUsersBody.  # noqa: E501
         :type: object
         """
 
-        self._project_id = project_id
+        self._workspace_id = workspace_id
 
     @property
-    def user(self):
-        """Gets the user of this UsersUserUserIdUuidBody.  # noqa: E501
+    def users(self):
+        """Gets the users of this WorkspaceIdUuidUsersBody.  # noqa: E501
 
+        List of Users to add to the Workspace.  # noqa: E501
 
-        :return: The user of this UsersUserUserIdUuidBody.  # noqa: E501
-        :rtype: V1projectsprojectIdUuidroleusersuserUserIdUuidUser
+        :return: The users of this WorkspaceIdUuidUsersBody.  # noqa: E501
+        :rtype: list[RimeUserWithRole]
         """
-        return self._user
+        return self._users
 
-    @user.setter
-    def user(self, user):
-        """Sets the user of this UsersUserUserIdUuidBody.
+    @users.setter
+    def users(self, users):
+        """Sets the users of this WorkspaceIdUuidUsersBody.
 
+        List of Users to add to the Workspace.  # noqa: E501
 
-        :param user: The user of this UsersUserUserIdUuidBody.  # noqa: E501
-        :type: V1projectsprojectIdUuidroleusersuserUserIdUuidUser
+        :param users: The users of this WorkspaceIdUuidUsersBody.  # noqa: E501
+        :type: list[RimeUserWithRole]
         """
 
-        self._user = user
+        self._users = users
 
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
@@ -108,15 +110,15 @@
                 result[attr] = dict(map(
                     lambda item: (item[0], item[1].to_dict())
                     if hasattr(item[1], "to_dict") else item,
                     value.items()
                 ))
             else:
                 result[attr] = value
-        if issubclass(UsersUserUserIdUuidBody, dict):
+        if issubclass(WorkspaceIdUuidUsersBody, dict):
             for key, value in self.items():
                 result[key] = value
 
         return result
 
     def to_str(self):
         """Returns the string representation of the model"""
@@ -124,15 +126,15 @@
 
     def __repr__(self):
         """For `print` and `pprint`"""
         return self.to_str()
 
     def __eq__(self, other):
         """Returns true if both objects are equal"""
-        if not isinstance(other, UsersUserUserIdUuidBody):
+        if not isinstance(other, WorkspaceIdUuidUsersBody):
             return False
 
         return self.__dict__ == other.__dict__
 
     def __ne__(self, other):
         """Returns true if both objects are not equal"""
         return not self == other
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1betaintegrationsintegration_id_uuid_integration.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1betaintegrationsintegration_id_uuid_integration.py`

 * *Files 10% similar despite different names*

```diff
@@ -29,47 +29,52 @@
     """
     swagger_types = {
         'id': 'object',
         'workspace_id': 'RimeUUID',
         'creation_time': 'datetime',
         'name': 'str',
         'type': 'IntegrationIntegrationType',
-        'schema': 'IntegrationIntegrationSchema'
+        'schema': 'IntegrationIntegrationSchema',
+        'level': 'IntegrationIntegrationLevel'
     }
 
     attribute_map = {
         'id': 'id',
         'workspace_id': 'workspaceId',
         'creation_time': 'creationTime',
         'name': 'name',
         'type': 'type',
-        'schema': 'schema'
+        'schema': 'schema',
+        'level': 'level'
     }
 
-    def __init__(self, id=None, workspace_id=None, creation_time=None, name=None, type=None, schema=None):  # noqa: E501
+    def __init__(self, id=None, workspace_id=None, creation_time=None, name=None, type=None, schema=None, level=None):  # noqa: E501
         """V1betaintegrationsintegrationIdUuidIntegration - a model defined in Swagger"""  # noqa: E501
         self._id = None
         self._workspace_id = None
         self._creation_time = None
         self._name = None
         self._type = None
         self._schema = None
+        self._level = None
         self.discriminator = None
         if id is not None:
             self.id = id
         if workspace_id is not None:
             self.workspace_id = workspace_id
         if creation_time is not None:
             self.creation_time = creation_time
         if name is not None:
             self.name = name
         if type is not None:
             self.type = type
         if schema is not None:
             self.schema = schema
+        if level is not None:
+            self.level = level
 
     @property
     def id(self):
         """Gets the id of this V1betaintegrationsintegrationIdUuidIntegration.  # noqa: E501
 
         Unique ID of an object in RIME.  # noqa: E501
 
@@ -191,14 +196,35 @@
 
         :param schema: The schema of this V1betaintegrationsintegrationIdUuidIntegration.  # noqa: E501
         :type: IntegrationIntegrationSchema
         """
 
         self._schema = schema
 
+    @property
+    def level(self):
+        """Gets the level of this V1betaintegrationsintegrationIdUuidIntegration.  # noqa: E501
+
+
+        :return: The level of this V1betaintegrationsintegrationIdUuidIntegration.  # noqa: E501
+        :rtype: IntegrationIntegrationLevel
+        """
+        return self._level
+
+    @level.setter
+    def level(self, level):
+        """Sets the level of this V1betaintegrationsintegrationIdUuidIntegration.
+
+
+        :param level: The level of this V1betaintegrationsintegrationIdUuidIntegration.  # noqa: E501
+        :type: IntegrationIntegrationLevel
+        """
+
+        self._level = level
+
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.swagger_types):
             value = getattr(self, attr)
             if isinstance(value, list):
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1betamodelcardsmodel_card_model_card_id_uuid_model_card.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1betamodelcardsmodel_card_model_card_id_uuid_model_card.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1firewallfirewall_firewall_id_uuid_firewall.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1firewallfirewall_firewall_id_uuid_firewall.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1usersuser_id_uuid_user.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1usersuser_id_uuid_user.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/v1workspaceworkspace_workspace_id_uuid_workspace.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/v1workspaceworkspace_workspace_id_uuid_workspace.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/models/workspace_workspace_workspace_id_uuid_body.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/models/workspace_workspace_workspace_id_uuid_body.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/swagger/swagger_client/rest.py` & `rime_sdk-2.0.0rc4/rime_sdk/swagger/swagger_client/rest.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/test_batch.py` & `rime_sdk-2.0.0rc4/rime_sdk/test_batch.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk/test_run.py` & `rime_sdk-2.0.0rc4/rime_sdk/test_run.py`

 * *Files identical despite different names*

### Comparing `rime_sdk-2.0.0rc3/rime_sdk.egg-info/PKG-INFO` & `rime_sdk-2.0.0rc4/rime_sdk.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rime-sdk
-Version: 2.0.0rc3
+Version: 2.0.0rc4
 Summary: Package to programmatically access a RIME deployment
 Home-page: UNKNOWN
 License: OSI Approved :: Apache Software License
 Platform: UNKNOWN
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `rime_sdk-2.0.0rc3/rime_sdk.egg-info/SOURCES.txt` & `rime_sdk-2.0.0rc4/rime_sdk.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -108,18 +108,21 @@
 rime_sdk/swagger/swagger_client/models/firewall_location_args.py
 rime_sdk/swagger/swagger_client/models/firewall_location_params.py
 rime_sdk/swagger/swagger_client/models/firewall_scheduled_ct_info.py
 rime_sdk/swagger/swagger_client/models/firewall_test_category_severity.py
 rime_sdk/swagger/swagger_client/models/googlerpc_status.py
 rime_sdk/swagger/swagger_client/models/image_reference_reference_type.py
 rime_sdk/swagger/swagger_client/models/integration_integration.py
+rime_sdk/swagger/swagger_client/models/integration_integration_level.py
 rime_sdk/swagger/swagger_client/models/integration_integration_schema.py
 rime_sdk/swagger/swagger_client/models/integration_integration_type.py
 rime_sdk/swagger/swagger_client/models/integration_variable_sensitivity.py
 rime_sdk/swagger/swagger_client/models/integrations_integration_id_uuid_body.py
+rime_sdk/swagger/swagger_client/models/job_data_continuous_incremental_test.py
+rime_sdk/swagger/swagger_client/models/job_data_stress_test.py
 rime_sdk/swagger/swagger_client/models/list_agents_request_list_agents_query.py
 rime_sdk/swagger/swagger_client/models/list_datasets_request_datasets_query.py
 rime_sdk/swagger/swagger_client/models/list_images_request_pip_library_filter.py
 rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_aggregated_metric.py
 rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metric_without_subsets.py
 rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_feature_metrics.py
 rime_sdk/swagger/swagger_client/models/list_metric_identifiers_response_subset_metric.py
@@ -238,20 +241,18 @@
 rime_sdk/swagger/swagger_client/models/rime_delete_integration_response.py
 rime_sdk/swagger/swagger_client/models/rime_delete_model_card_response.py
 rime_sdk/swagger/swagger_client/models/rime_delete_model_response.py
 rime_sdk/swagger/swagger_client/models/rime_delete_prediction_set_response.py
 rime_sdk/swagger/swagger_client/models/rime_delete_uploaded_file_url_response.py
 rime_sdk/swagger/swagger_client/models/rime_delete_workspace_tag_response.py
 rime_sdk/swagger/swagger_client/models/rime_ensure_image_existence_response.py
-rime_sdk/swagger/swagger_client/models/rime_fail_job_response.py
 rime_sdk/swagger/swagger_client/models/rime_failing_row.py
 rime_sdk/swagger/swagger_client/models/rime_failing_rows_result.py
 rime_sdk/swagger/swagger_client/models/rime_feature_flags.py
 rime_sdk/swagger/swagger_client/models/rime_feature_type.py
-rime_sdk/swagger/swagger_client/models/rime_finalize_cancellation_response.py
 rime_sdk/swagger/swagger_client/models/rime_float_list.py
 rime_sdk/swagger/swagger_client/models/rime_get_agent_response.py
 rime_sdk/swagger/swagger_client/models/rime_get_datapoints_response.py
 rime_sdk/swagger/swagger_client/models/rime_get_dataset_file_upload_url_response.py
 rime_sdk/swagger/swagger_client/models/rime_get_dataset_response.py
 rime_sdk/swagger/swagger_client/models/rime_get_enabled_feature_response.py
 rime_sdk/swagger/swagger_client/models/rime_get_feature_flag_jwt_response.py
@@ -275,16 +276,14 @@
 rime_sdk/swagger/swagger_client/models/rime_get_user_response.py
 rime_sdk/swagger/swagger_client/models/rime_get_workspace_response.py
 rime_sdk/swagger/swagger_client/models/rime_heartbeat_response.py
 rime_sdk/swagger/swagger_client/models/rime_image_reference.py
 rime_sdk/swagger/swagger_client/models/rime_int_list.py
 rime_sdk/swagger/swagger_client/models/rime_integration_info.py
 rime_sdk/swagger/swagger_client/models/rime_job_data.py
-rime_sdk/swagger/swagger_client/models/rime_job_data_continuous_incremental_test.py
-rime_sdk/swagger/swagger_client/models/rime_job_data_stress_test.py
 rime_sdk/swagger/swagger_client/models/rime_job_metadata.py
 rime_sdk/swagger/swagger_client/models/rime_job_type.py
 rime_sdk/swagger/swagger_client/models/rime_job_view.py
 rime_sdk/swagger/swagger_client/models/rime_license_feature.py
 rime_sdk/swagger/swagger_client/models/rime_license_limit.py
 rime_sdk/swagger/swagger_client/models/rime_limit_status.py
 rime_sdk/swagger/swagger_client/models/rime_limit_status_status.py
@@ -296,16 +295,14 @@
 rime_sdk/swagger/swagger_client/models/rime_list_detection_events_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_enabled_features_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_file_scan_results_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_images_request.py
 rime_sdk/swagger/swagger_client/models/rime_list_images_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_request_query.py
 rime_sdk/swagger/swagger_client/models/rime_list_jobs_for_project_response.py
-rime_sdk/swagger/swagger_client/models/rime_list_jobs_request_query.py
-rime_sdk/swagger/swagger_client/models/rime_list_jobs_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_metric_identifiers_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_model_cards_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_models_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_monitors_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_notifications_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_prediction_sets_response.py
 rime_sdk/swagger/swagger_client/models/rime_list_uploaded_file_urls_response.py
@@ -374,15 +371,14 @@
 rime_sdk/swagger/swagger_client/models/rime_update_monitor_response.py
 rime_sdk/swagger/swagger_client/models/rime_update_notification_response.py
 rime_sdk/swagger/swagger_client/models/rime_update_user_of_workspace_response.py
 rime_sdk/swagger/swagger_client/models/rime_update_user_response.py
 rime_sdk/swagger/swagger_client/models/rime_update_workspace_response.py
 rime_sdk/swagger/swagger_client/models/rime_update_workspace_tag_response.py
 rime_sdk/swagger/swagger_client/models/rime_upsert_feature_flags_response.py
-rime_sdk/swagger/swagger_client/models/rime_upsert_job_response.py
 rime_sdk/swagger/swagger_client/models/rime_user_detail_with_role.py
 rime_sdk/swagger/swagger_client/models/rime_user_role.py
 rime_sdk/swagger/swagger_client/models/rime_user_with_role.py
 rime_sdk/swagger/swagger_client/models/rime_user_write_mask.py
 rime_sdk/swagger/swagger_client/models/rime_uuid.py
 rime_sdk/swagger/swagger_client/models/rime_validate_test_config_response.py
 rime_sdk/swagger/swagger_client/models/rime_workspace.py
@@ -447,18 +443,14 @@
 rime_sdk/swagger/swagger_client/models/testrunresult_test_case.py
 rime_sdk/swagger/swagger_client/models/testrunresult_test_case_display.py
 rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result.py
 rime_sdk/swagger/swagger_client/models/testrunresult_test_feature_result_display.py
 rime_sdk/swagger/swagger_client/models/testrunresult_test_run_detail.py
 rime_sdk/swagger/swagger_client/models/testrunresult_test_run_metrics.py
 rime_sdk/swagger/swagger_client/models/the_updates_to_the_monitor_.py
-rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask.py
-rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data.py
-rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data_continuous_incremental_test.py
-rime_sdk/swagger/swagger_client/models/upsert_job_request_write_mask_job_data_stress_test.py
 rime_sdk/swagger/swagger_client/models/user_favorite_projects.py
 rime_sdk/swagger/swagger_client/models/user_private_info.py
 rime_sdk/swagger/swagger_client/models/user_role.py
 rime_sdk/swagger/swagger_client/models/user_user_detail.py
 rime_sdk/swagger/swagger_client/models/users_user_id_uuid_body.py
 rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body.py
 rime_sdk/swagger/swagger_client/models/users_user_user_id_uuid_body1.py
```

### Comparing `rime_sdk-2.0.0rc3/setup.py` & `rime_sdk-2.0.0rc4/setup.py`

 * *Files identical despite different names*

