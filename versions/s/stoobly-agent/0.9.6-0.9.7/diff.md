# Comparing `tmp/stoobly-agent-0.9.6.tar.gz` & `tmp/stoobly-agent-0.9.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "stoobly-agent-0.9.6.tar", last modified: Fri May  6 05:43:44 2022, max compression
+gzip compressed data, was "stoobly-agent-0.9.7.tar", last modified: Mon May  9 08:39:57 2022, max compression
```

## Comparing `stoobly-agent-0.9.6.tar` & `stoobly-agent-0.9.7.tar`

### file list

```diff
@@ -1,224 +1,224 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/
--rw-r--r--   0 runner    (1001) docker     (121)      548 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      249 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      567 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/README.md
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1493 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.670751 stoobly-agent-0.9.6/stoobly_agent/
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/api/
--rw-r--r--   0 runner    (1001) docker     (121)     7632 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3477 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/api/configs_controller.py
--rw-r--r--   0 runner    (1001) docker     (121)     3625 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/api/proxy_controller.py
--rw-r--r--   0 runner    (1001) docker     (121)     1238 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/api/statuses_controller.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/cli/
--rw-r--r--   0 runner    (1001) docker     (121)      299 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      861 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/ca_cert_cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     1493 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/ca_cert_installer.py
--rw-r--r--   0 runner    (1001) docker     (121)     3020 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/config_cli.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/cli/decorators/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/decorators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1678 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/decorators/config.py
--rw-r--r--   0 runner    (1001) docker     (121)      994 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/decorators/exec.py
--rw-r--r--   0 runner    (1001) docker     (121)      419 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/dev_tools_cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     1230 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/feature_cli.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/
--rw-r--r--   0 runner    (1001) docker     (121)      117 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      564 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/migrate_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     1823 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/project_facade.py
--rw-r--r--   0 runner    (1001) docker     (121)     1056 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/report_facade.py
--rw-r--r--   0 runner    (1001) docker     (121)     2700 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/request_facade.py
--rw-r--r--   0 runner    (1001) docker     (121)      731 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/run_command_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     2750 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/scenario_facade.py
--rw-r--r--   0 runner    (1001) docker     (121)      956 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/tabulate_print_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     2870 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/validations.py
--rw-r--r--   0 runner    (1001) docker     (121)     2074 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/main_group.py
--rw-r--r--   0 runner    (1001) docker     (121)     3917 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/project_cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     2858 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/report_cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     4522 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/request_cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     4644 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/cli/scenario_cli.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/models/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4587 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/local_db_request_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)      705 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/request_adapter_factory.py
--rw-r--r--   0 runner    (1001) docker     (121)     1306 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/stoobly_request_adapter.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/types/
--rw-r--r--   0 runner    (1001) docker     (121)      105 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      292 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/types/request_create_params.py
--rw-r--r--   0 runner    (1001) docker     (121)      150 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/types/request_show_params.py
--rw-r--r--   0 runner    (1001) docker     (121)     1715 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/request_model.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/models/schemas/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/schemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      973 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/schemas/request.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/models/types/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      169 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/models/types/requests_model_index.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/
--rw-r--r--   0 runner    (1001) docker     (121)     2509 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/constants/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/constants/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       40 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/constants/custom_response_codes.py
--rw-r--r--   0 runner    (1001) docker     (121)     4882 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_mock_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     3535 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_record_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     1918 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_replay_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     4219 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_test_service.py
--rw-r--r--   0 runner    (1001) docker     (121)      903 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/hot_reload.py
--rw-r--r--   0 runner    (1001) docker     (121)     2575 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/intercept_handler.py
--rw-r--r--   0 runner    (1001) docker     (121)     5876 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/intercept_settings.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      878 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/request.py
--rw-r--r--   0 runner    (1001) docker     (121)     2565 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/request_body_facade.py
--rw-r--r--   0 runner    (1001) docker     (121)     6325 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/request_facade.py
--rw-r--r--   0 runner    (1001) docker     (121)      339 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/response.py
--rw-r--r--   0 runner    (1001) docker     (121)     1361 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/response_adapter.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      840 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/context.py
--rw-r--r--   0 runner    (1001) docker     (121)      415 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/custom_not_found_response_builder.py
--rw-r--r--   0 runner    (1001) docker     (121)     3756 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/eval_request_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     4354 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/hashed_request_decorator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/replay/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/replay/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1692 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/replay/replay_request_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     1905 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/replay/replay_scenario_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     2667 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.678752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/
--rw-r--r--   0 runner    (1001) docker     (121)       82 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      509 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/context.py
--rw-r--r--   0 runner    (1001) docker     (121)      836 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/context_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     1025 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/decode_response_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     1622 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/iterable_matches.py
--rw-r--r--   0 runner    (1001) docker     (121)      480 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/mitmproxy_response_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)      424 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/requests_response_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)      633 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/stoobly_response_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)     3614 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/test_service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.682752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1770 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/join_request_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     1323 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/joined_request.py
--rw-r--r--   0 runner    (1001) docker     (121)      353 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/proxy_request.py
--rw-r--r--   0 runner    (1001) docker     (121)     2091 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/request_string.py
--rw-r--r--   0 runner    (1001) docker     (121)     2072 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/response_string.py
--rw-r--r--   0 runner    (1001) docker     (121)     2875 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/upload_request_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     1930 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/upload_test_service.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.682752 stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2071 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/allowed_request_service.py
--rw-r--r--   0 runner    (1001) docker     (121)     1042 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/filter_rules_to_ignored_components_service.py
--rw-r--r--   0 runner    (1001) docker     (121)      749 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/publish_change_service.py
--rw-r--r--   0 runner    (1001) docker     (121)      528 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/request_handler.py
--rw-r--r--   0 runner    (1001) docker     (121)     1075 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/response_handler.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.682752 stoobly-agent-0.9.6/stoobly_agent/app/settings/
--rw-r--r--   0 runner    (1001) docker     (121)     3924 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      487 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/cli_settings.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.682752 stoobly-agent-0.9.6/stoobly_agent/app/settings/constants/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/constants/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       39 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/constants/firewall_action.py
--rw-r--r--   0 runner    (1001) docker     (121)       63 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/constants/intercept_mode.py
--rw-r--r--   0 runner    (1001) docker     (121)       71 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/constants/request_component.py
--rw-r--r--   0 runner    (1001) docker     (121)     1719 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/data_rules.py
--rw-r--r--   0 runner    (1001) docker     (121)      618 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/data_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1089 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/feature_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1005 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/filter_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)      712 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/filter_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)      679 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/firewall_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)      707 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/firewall_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1648 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/intercept_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)      776 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/parameter_rule.py
--rw-r--r--   0 runner    (1001) docker     (121)     1574 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/proxy_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1192 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/remote_settings.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.682752 stoobly-agent-0.9.6/stoobly_agent/app/settings/types/
--rw-r--r--   0 runner    (1001) docker     (121)     1840 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      157 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/types/cli_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1359 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/types/proxy_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/types/remote_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)       84 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/types/ui_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1107 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/app/settings/ui_settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     3438 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.682752 stoobly-agent-0.9.6/stoobly_agent/config/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.686752 stoobly-agent-0.9.6/stoobly_agent/config/constants/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      377 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/custom_headers.py
--rw-r--r--   0 runner    (1001) docker     (121)      767 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/env_vars.py
--rw-r--r--   0 runner    (1001) docker     (121)      120 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/headers.py
--rw-r--r--   0 runner    (1001) docker     (121)       41 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/mock_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)       77 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/mode.py
--rw-r--r--   0 runner    (1001) docker     (121)       65 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/record_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)       25 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/replay_policy.py
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/test_origin.py
--rw-r--r--   0 runner    (1001) docker     (121)       47 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/constants/test_strategy.py
--rw-r--r--   0 runner    (1001) docker     (121)     1394 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/data_dir.py
--rw-r--r--   0 runner    (1001) docker     (121)     1146 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/config/source_dir.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.686752 stoobly-agent-0.9.6/stoobly_agent/lib/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.686752 stoobly-agent-0.9.6/stoobly_agent/lib/api/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      521 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/agent_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1368 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/api.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.686752 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/
--rw-r--r--   0 runner    (1001) docker     (121)      697 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       93 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/pagination_query_params.py
--rw-r--r--   0 runner    (1001) docker     (121)      448 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/projects.py
--rw-r--r--   0 runner    (1001) docker     (121)       78 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/report_show_response.py
--rw-r--r--   0 runner    (1001) docker     (121)      138 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/request_create_params.py
--rw-r--r--   0 runner    (1001) docker     (121)      115 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/request_show_query_params.py
--rw-r--r--   0 runner    (1001) docker     (121)      380 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/request_show_response.py
--rw-r--r--   0 runner    (1001) docker     (121)      151 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/requests_index_query_params.py
--rw-r--r--   0 runner    (1001) docker     (121)      178 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/requests_index_response.py
--rw-r--r--   0 runner    (1001) docker     (121)       98 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/response_show_response.py
--rw-r--r--   0 runner    (1001) docker     (121)      242 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/scenarios.py
--rw-r--r--   0 runner    (1001) docker     (121)      126 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/users.py
--rw-r--r--   0 runner    (1001) docker     (121)      375 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/json_response_builder.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/
--rw-r--r--   0 runner    (1001) docker     (121)      289 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      433 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/organization_key.py
--rw-r--r--   0 runner    (1001) docker     (121)      465 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/project_key.py
--rw-r--r--   0 runner    (1001) docker     (121)      444 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/report_key.py
--rw-r--r--   0 runner    (1001) docker     (121)      601 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/request_key.py
--rw-r--r--   0 runner    (1001) docker     (121)      675 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/resource_key.py
--rw-r--r--   0 runner    (1001) docker     (121)      452 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/scenario_key.py
--rw-r--r--   0 runner    (1001) docker     (121)     1165 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/param_builder.py
--rw-r--r--   0 runner    (1001) docker     (121)     1079 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/projects_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)      678 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/reports_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)     1554 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/requests_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)     1254 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/scenarios_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)     2599 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/stoobly_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      360 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/tests_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)      476 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/api/users_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)      501 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/cache.py
--rw-r--r--   0 runner    (1001) docker     (121)      789 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/logger.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/stoobly_agent/lib/orm/
--rw-r--r--   0 runner    (1001) docker     (121)     1172 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      311 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/base.py
--rw-r--r--   0 runner    (1001) docker     (121)      427 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/request.py
--rw-r--r--   0 runner    (1001) docker     (121)      105 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/response.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/
--rw-r--r--   0 runner    (1001) docker     (121)      242 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1511 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/orm_to_requests_response_transformer.py
--rw-r--r--   0 runner    (1001) docker     (121)     2867 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/orm_to_stoobly_request_transformer.py
--rw-r--r--   0 runner    (1001) docker     (121)     1238 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/orm_to_stoobly_response_transformer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/stoobly_agent/lib/orm/types/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      245 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/types/request_columns.py
--rw-r--r--   0 runner    (1001) docker     (121)       94 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/types/response_columns.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      855 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/request_parse_handler.py
--rw-r--r--   0 runner    (1001) docker     (121)      675 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/requests_response_builder.py
--rw-r--r--   0 runner    (1001) docker     (121)      725 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/response_parse_handler.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.690752 stoobly-agent-0.9.6/stoobly_agent/lib/utils/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      246 2022-05-06 05:42:23.000000 stoobly-agent-0.9.6/stoobly_agent/lib/utils/conditional_decorator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-06 05:43:44.674752 stoobly-agent-0.9.6/stoobly_agent.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      249 2022-05-06 05:43:44.000000 stoobly-agent-0.9.6/stoobly_agent.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     8518 2022-05-06 05:43:44.000000 stoobly-agent-0.9.6/stoobly_agent.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-06 05:43:44.000000 stoobly-agent-0.9.6/stoobly_agent.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       58 2022-05-06 05:43:44.000000 stoobly-agent-0.9.6/stoobly_agent.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      252 2022-05-06 05:43:44.000000 stoobly-agent-0.9.6/stoobly_agent.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       14 2022-05-06 05:43:44.000000 stoobly-agent-0.9.6/stoobly_agent.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/
+-rw-r--r--   0 runner    (1001) docker     (121)      548 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      249 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      567 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1493 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.227595 stoobly-agent-0.9.7/stoobly_agent/
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.227595 stoobly-agent-0.9.7/stoobly_agent/app/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.227595 stoobly-agent-0.9.7/stoobly_agent/app/api/
+-rw-r--r--   0 runner    (1001) docker     (121)     7632 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3477 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/api/configs_controller.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3625 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/api/proxy_controller.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1238 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/api/statuses_controller.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/cli/
+-rw-r--r--   0 runner    (1001) docker     (121)      299 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      861 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/ca_cert_cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1493 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/ca_cert_installer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3020 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/config_cli.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/cli/decorators/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/decorators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1678 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/decorators/config.py
+-rw-r--r--   0 runner    (1001) docker     (121)      994 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/decorators/exec.py
+-rw-r--r--   0 runner    (1001) docker     (121)      419 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/dev_tools_cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1230 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/feature_cli.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/
+-rw-r--r--   0 runner    (1001) docker     (121)      117 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      564 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/migrate_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1823 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/project_facade.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1056 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/report_facade.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2700 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/request_facade.py
+-rw-r--r--   0 runner    (1001) docker     (121)      731 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/run_command_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2750 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/scenario_facade.py
+-rw-r--r--   0 runner    (1001) docker     (121)      956 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/tabulate_print_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2870 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/validations.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2074 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/main_group.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3917 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/project_cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2858 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/report_cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4522 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/request_cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4644 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/cli/scenario_cli.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/models/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4587 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/local_db_request_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)      705 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/request_adapter_factory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1306 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/stoobly_request_adapter.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/types/
+-rw-r--r--   0 runner    (1001) docker     (121)      105 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      292 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/types/request_create_params.py
+-rw-r--r--   0 runner    (1001) docker     (121)      150 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/types/request_show_params.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1715 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/request_model.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/models/schemas/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/schemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      973 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/schemas/request.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/models/types/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      169 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/models/types/requests_model_index.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/
+-rw-r--r--   0 runner    (1001) docker     (121)     2509 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.231595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/constants/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/constants/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       40 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/constants/custom_response_codes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4882 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_mock_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3535 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_record_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1918 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_replay_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4219 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_test_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)      903 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/hot_reload.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2575 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/intercept_handler.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5876 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/intercept_settings.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.235595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      878 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/request.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2565 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/request_body_facade.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6325 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/request_facade.py
+-rw-r--r--   0 runner    (1001) docker     (121)      339 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/response.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1361 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/response_adapter.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.235595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      840 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/context.py
+-rw-r--r--   0 runner    (1001) docker     (121)      415 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/custom_not_found_response_builder.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3756 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/eval_request_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4354 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/hashed_request_decorator.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.235595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/replay/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/replay/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1692 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/replay/replay_request_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1905 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/replay/replay_scenario_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2667 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.235595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/
+-rw-r--r--   0 runner    (1001) docker     (121)       82 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      509 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/context.py
+-rw-r--r--   0 runner    (1001) docker     (121)      836 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/context_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1025 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/decode_response_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1622 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/iterable_matches.py
+-rw-r--r--   0 runner    (1001) docker     (121)      480 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/mitmproxy_response_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/requests_response_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)      633 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/stoobly_response_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3614 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/test_service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.235595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1770 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/join_request_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1323 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/joined_request.py
+-rw-r--r--   0 runner    (1001) docker     (121)      353 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/proxy_request.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2091 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/request_string.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2072 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/response_string.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2875 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/upload_request_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1930 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/upload_test_service.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.235595 stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2071 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/allowed_request_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1042 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/filter_rules_to_ignored_components_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)      749 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/publish_change_service.py
+-rw-r--r--   0 runner    (1001) docker     (121)      528 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/request_handler.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1075 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/response_handler.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.239595 stoobly-agent-0.9.7/stoobly_agent/app/settings/
+-rw-r--r--   0 runner    (1001) docker     (121)     3924 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      487 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/cli_settings.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.239595 stoobly-agent-0.9.7/stoobly_agent/app/settings/constants/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/constants/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       39 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/constants/firewall_action.py
+-rw-r--r--   0 runner    (1001) docker     (121)       63 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/constants/intercept_mode.py
+-rw-r--r--   0 runner    (1001) docker     (121)       71 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/constants/request_component.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1719 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/data_rules.py
+-rw-r--r--   0 runner    (1001) docker     (121)      618 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/data_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1089 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/feature_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1005 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/filter_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)      712 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/filter_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)      679 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/firewall_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)      707 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/firewall_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1648 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/intercept_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)      776 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/parameter_rule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1574 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/proxy_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1192 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/remote_settings.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.239595 stoobly-agent-0.9.7/stoobly_agent/app/settings/types/
+-rw-r--r--   0 runner    (1001) docker     (121)     1840 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      157 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/types/cli_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1359 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/types/proxy_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/types/remote_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)       84 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/types/ui_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1107 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/app/settings/ui_settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3438 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.239595 stoobly-agent-0.9.7/stoobly_agent/config/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.239595 stoobly-agent-0.9.7/stoobly_agent/config/constants/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      377 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/custom_headers.py
+-rw-r--r--   0 runner    (1001) docker     (121)      767 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/env_vars.py
+-rw-r--r--   0 runner    (1001) docker     (121)      120 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/headers.py
+-rw-r--r--   0 runner    (1001) docker     (121)       41 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/mock_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)       77 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/mode.py
+-rw-r--r--   0 runner    (1001) docker     (121)       65 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/record_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)       25 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/replay_policy.py
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/test_origin.py
+-rw-r--r--   0 runner    (1001) docker     (121)       47 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/constants/test_strategy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1394 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/data_dir.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1146 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/config/source_dir.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.239595 stoobly-agent-0.9.7/stoobly_agent/lib/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.239595 stoobly-agent-0.9.7/stoobly_agent/lib/api/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      521 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/agent_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1420 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/api.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/
+-rw-r--r--   0 runner    (1001) docker     (121)      697 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       93 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/pagination_query_params.py
+-rw-r--r--   0 runner    (1001) docker     (121)      448 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/projects.py
+-rw-r--r--   0 runner    (1001) docker     (121)       78 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/report_show_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)      138 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/request_create_params.py
+-rw-r--r--   0 runner    (1001) docker     (121)      115 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/request_show_query_params.py
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/request_show_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)      151 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/requests_index_query_params.py
+-rw-r--r--   0 runner    (1001) docker     (121)      178 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/requests_index_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)       98 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/response_show_response.py
+-rw-r--r--   0 runner    (1001) docker     (121)      242 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/scenarios.py
+-rw-r--r--   0 runner    (1001) docker     (121)      126 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/users.py
+-rw-r--r--   0 runner    (1001) docker     (121)      375 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/json_response_builder.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/
+-rw-r--r--   0 runner    (1001) docker     (121)      289 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      433 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/organization_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)      465 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/project_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)      444 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/report_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)      601 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/request_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)      675 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/resource_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)      452 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/scenario_key.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1165 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/param_builder.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1079 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/projects_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)      678 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/reports_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1554 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/requests_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1254 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/scenarios_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2599 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/stoobly_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      360 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/tests_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)      476 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/api/users_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)      501 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/cache.py
+-rw-r--r--   0 runner    (1001) docker     (121)      789 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/logger.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/stoobly_agent/lib/orm/
+-rw-r--r--   0 runner    (1001) docker     (121)     1172 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      311 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/base.py
+-rw-r--r--   0 runner    (1001) docker     (121)      427 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/request.py
+-rw-r--r--   0 runner    (1001) docker     (121)      105 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/response.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/
+-rw-r--r--   0 runner    (1001) docker     (121)      242 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1511 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/orm_to_requests_response_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2867 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/orm_to_stoobly_request_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1238 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/orm_to_stoobly_response_transformer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/stoobly_agent/lib/orm/types/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      245 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/types/request_columns.py
+-rw-r--r--   0 runner    (1001) docker     (121)       94 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/types/response_columns.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      855 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/request_parse_handler.py
+-rw-r--r--   0 runner    (1001) docker     (121)      675 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/requests_response_builder.py
+-rw-r--r--   0 runner    (1001) docker     (121)      725 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/response_parse_handler.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.243595 stoobly-agent-0.9.7/stoobly_agent/lib/utils/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      246 2022-05-09 08:38:46.000000 stoobly-agent-0.9.7/stoobly_agent/lib/utils/conditional_decorator.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-09 08:39:57.227595 stoobly-agent-0.9.7/stoobly_agent.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      249 2022-05-09 08:39:57.000000 stoobly-agent-0.9.7/stoobly_agent.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     8518 2022-05-09 08:39:57.000000 stoobly-agent-0.9.7/stoobly_agent.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-09 08:39:57.000000 stoobly-agent-0.9.7/stoobly_agent.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       58 2022-05-09 08:39:57.000000 stoobly-agent-0.9.7/stoobly_agent.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      252 2022-05-09 08:39:57.000000 stoobly-agent-0.9.7/stoobly_agent.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       14 2022-05-09 08:39:57.000000 stoobly-agent-0.9.7/stoobly_agent.egg-info/top_level.txt
```

### Comparing `stoobly-agent-0.9.6/LICENSE` & `stoobly-agent-0.9.7/LICENSE`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/README.md` & `stoobly-agent-0.9.7/README.md`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/setup.py` & `stoobly-agent-0.9.7/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -44,10 +44,10 @@
         'stoobly_agent', 'stoobly_agent.*',
     ]),
     package_data={
         'stoobly_agent': ['config/*'] + db_files + public_files
     },
     #scripts=['bin/stoobly-agent'],
     url='https://github.com/Stoobly/stoobly-agent',
-    version='0.9.6',
+    version='0.9.7',
 )
```

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/api/__init__.py` & `stoobly-agent-0.9.7/stoobly_agent/app/api/__init__.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/api/configs_controller.py` & `stoobly-agent-0.9.7/stoobly_agent/app/api/configs_controller.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/api/proxy_controller.py` & `stoobly-agent-0.9.7/stoobly_agent/app/api/proxy_controller.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/api/statuses_controller.py` & `stoobly-agent-0.9.7/stoobly_agent/app/api/statuses_controller.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/ca_cert_cli.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/ca_cert_cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/ca_cert_installer.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/ca_cert_installer.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/config_cli.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/config_cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/decorators/config.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/decorators/config.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/decorators/exec.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/decorators/exec.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/feature_cli.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/feature_cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/migrate_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/migrate_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/project_facade.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/project_facade.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/report_facade.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/report_facade.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/request_facade.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/request_facade.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/run_command_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/run_command_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/scenario_facade.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/scenario_facade.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/tabulate_print_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/tabulate_print_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/helpers/validations.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/helpers/validations.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/main_group.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/main_group.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/project_cli.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/project_cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/report_cli.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/report_cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/request_cli.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/request_cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/cli/scenario_cli.py` & `stoobly-agent-0.9.7/stoobly_agent/app/cli/scenario_cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/local_db_request_adapter.py` & `stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/local_db_request_adapter.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/request_adapter_factory.py` & `stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/request_adapter_factory.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/models/adapters/stoobly_request_adapter.py` & `stoobly-agent-0.9.7/stoobly_agent/app/models/adapters/stoobly_request_adapter.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/models/request_model.py` & `stoobly-agent-0.9.7/stoobly_agent/app/models/request_model.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/models/schemas/request.py` & `stoobly-agent-0.9.7/stoobly_agent/app/models/schemas/request.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/__init__.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/__init__.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_mock_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_mock_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_record_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_record_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_replay_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_replay_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/handle_test_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/handle_test_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/hot_reload.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/hot_reload.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/intercept_handler.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/intercept_handler.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/intercept_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/intercept_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/request.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/request.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/request_body_facade.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/request_body_facade.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/request_facade.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/request_facade.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/mitmproxy/response_adapter.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/mitmproxy/response_adapter.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/context.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/context.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/eval_request_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/eval_request_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/mock/hashed_request_decorator.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/mock/hashed_request_decorator.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/replay/replay_request_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/replay/replay_request_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/replay/replay_scenario_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/replay/replay_scenario_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/context_response.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/context_response.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/decode_response_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/decode_response_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/iterable_matches.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/iterable_matches.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/stoobly_response_adapter.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/stoobly_response_adapter.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/test/test_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/test/test_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/join_request_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/join_request_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/joined_request.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/joined_request.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/request_string.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/request_string.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/response_string.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/response_string.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/upload_request_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/upload_request_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/upload/upload_test_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/upload/upload_test_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/allowed_request_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/allowed_request_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/filter_rules_to_ignored_components_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/filter_rules_to_ignored_components_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/publish_change_service.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/publish_change_service.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/request_handler.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/request_handler.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/proxy/utils/response_handler.py` & `stoobly-agent-0.9.7/stoobly_agent/app/proxy/utils/response_handler.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/__init__.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/__init__.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/data_rules.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/data_rules.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/data_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/data_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/feature_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/feature_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/filter_rule.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/filter_rule.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/filter_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/filter_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/firewall_rule.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/firewall_rule.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/firewall_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/firewall_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/intercept_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/intercept_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/parameter_rule.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/parameter_rule.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/proxy_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/proxy_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/remote_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/remote_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/types/__init__.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/types/__init__.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/types/proxy_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/types/proxy_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/app/settings/ui_settings.py` & `stoobly-agent-0.9.7/stoobly_agent/app/settings/ui_settings.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/cli.py` & `stoobly-agent-0.9.7/stoobly_agent/cli.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/config/constants/env_vars.py` & `stoobly-agent-0.9.7/stoobly_agent/config/constants/env_vars.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/config/data_dir.py` & `stoobly-agent-0.9.7/stoobly_agent/config/data_dir.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/config/source_dir.py` & `stoobly-agent-0.9.7/stoobly_agent/config/source_dir.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/agent_api.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/agent_api.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/api.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/api.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,14 +9,17 @@
 
     def without_proxy(self, handler):
       current = self.set_proxy('')
 
       res = handler()
 
       for key, val in current.items():
+        if not val:
+          continue
+        
         os.environ[key] = val
 
       return res
 
     def with_proxy(self, handler):
       settings = Settings.instance()
       proxy_url = settings.proxy.url
@@ -29,24 +32,24 @@
 
       return res
 
     def set_proxy(self, val):
       current = {}
 
       current[HTTP_PROXY] = os.environ.get(HTTP_PROXY)
-      os.environ[HTTP_PROXY] = ''
+      os.environ[HTTP_PROXY] = val
 
       current[HTTPS_PROXY] = os.environ.get(HTTPS_PROXY)
-      os.environ[HTTPS_PROXY] = ''
+      os.environ[HTTPS_PROXY] = val
 
       current[HTTP_PROXY.lower()] = os.environ.get(HTTP_PROXY.lower())
-      os.environ[HTTP_PROXY.lower()] = ''
+      os.environ[HTTP_PROXY.lower()] = val
 
       current[HTTPS_PROXY.lower()] = os.environ.get(HTTPS_PROXY.lower())
-      os.environ[HTTPS_PROXY.lower()] = ''
+      os.environ[HTTPS_PROXY.lower()] = val
 
       return current
 
     def get(self, url, **kwargs):
       handler = lambda: requests.get(url, **kwargs)
       return self.without_proxy(handler)
```

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/interfaces/__init__.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/interfaces/__init__.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/request_key.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/request_key.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/keys/resource_key.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/keys/resource_key.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/param_builder.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/param_builder.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/projects_resource.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/projects_resource.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/reports_resource.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/reports_resource.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/requests_resource.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/requests_resource.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/scenarios_resource.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/scenarios_resource.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/api/stoobly_api.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/api/stoobly_api.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/logger.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/logger.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/orm/__init__.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/orm/__init__.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/orm_to_requests_response_transformer.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/orm_to_requests_response_transformer.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/orm_to_stoobly_request_transformer.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/orm_to_stoobly_request_transformer.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/orm/transformers/orm_to_stoobly_response_transformer.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/orm/transformers/orm_to_stoobly_response_transformer.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/request_parse_handler.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/request_parse_handler.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/requests_response_builder.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/requests_response_builder.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent/lib/orm/utils/response_parse_handler.py` & `stoobly-agent-0.9.7/stoobly_agent/lib/orm/utils/response_parse_handler.py`

 * *Files identical despite different names*

### Comparing `stoobly-agent-0.9.6/stoobly_agent.egg-info/SOURCES.txt` & `stoobly-agent-0.9.7/stoobly_agent.egg-info/SOURCES.txt`

 * *Files identical despite different names*

