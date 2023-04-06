# Comparing `tmp/acryl-datahub-0.9.6rc0.tar.gz` & `tmp/acryl-datahub-0.9.6rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "acryl-datahub-0.9.6rc0.tar", last modified: Fri Jan 13 23:23:39 2023, max compression
+gzip compressed data, was "acryl-datahub-0.9.6rc1.tar", last modified: Fri Jan 13 23:39:10 2023, max compression
```

## Comparing `acryl-datahub-0.9.6rc0.tar` & `acryl-datahub-0.9.6rc1.tar`

### file list

```diff
@@ -1,739 +1,740 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.794424 acryl-datahub-0.9.6rc0/
--rw-r--r--   0 runner    (1001) docker     (123)    12901 2023-01-13 23:23:39.794424 acryl-datahub-0.9.6rc0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     9980 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      943 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     2035 2023-01-13 23:23:39.798424 acryl-datahub-0.9.6rc0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)    25908 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.654425 acryl-datahub-0.9.6rc0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    12901 2023-01-13 23:23:39.000000 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    30528 2023-01-13 23:23:39.000000 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:23:39.000000 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)     6366 2023-01-13 23:23:39.000000 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:00:29.000000 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)    32470 2023-01-13 23:23:39.000000 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-01-13 23:23:39.000000 acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-01-13 23:23:29.000000 acryl-datahub-0.9.6rc0/src/datahub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/
--rw-r--r--   0 runner    (1001) docker     (123)      268 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5324 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/assertion_circuit_breaker.py
--rw-r--r--   0 runner    (1001) docker     (123)     1471 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/circuit_breaker.py
--rw-r--r--   0 runner    (1001) docker     (123)     2908 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/operation_circuit_breaker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/entities/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpgroup/
--rw-r--r--   0 runner    (1001) docker     (123)       63 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpgroup/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpgroup/corpgroup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpuser/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpuser/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3639 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpuser/corpuser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/entities/datajob/
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/datajob/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4265 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/datajob/dataflow.py
--rw-r--r--   0 runner    (1001) docker     (123)     7492 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/datajob/datajob.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/entities/dataprocess/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/dataprocess/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14547 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/entities/dataprocess/dataprocess_instance.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.658425 acryl-datahub-0.9.6rc0/src/datahub/api/graphql/
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/graphql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2818 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/graphql/assertion.py
--rw-r--r--   0 runner    (1001) docker     (123)     1566 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/graphql/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5116 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/api/graphql/operation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.662425 acryl-datahub-0.9.6rc0/src/datahub/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2725 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/check_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)    22695 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/cli_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    16162 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/delete_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     4851 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/docker_check.py
--rw-r--r--   0 runner    (1001) docker     (123)    32728 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/docker_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     1429 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/get_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)    12891 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/ingest_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/json_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    16440 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/migrate.py
--rw-r--r--   0 runner    (1001) docker     (123)     8936 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/migration_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3174 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/put_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     2590 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/state_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      487 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/telemetry.py
--rw-r--r--   0 runner    (1001) docker     (123)     7350 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/cli/timeline_cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.662425 acryl-datahub-0.9.6rc0/src/datahub/configuration/
--rw-r--r--   0 runner    (1001) docker     (123)      114 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      934 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/_config_enum.py
--rw-r--r--   0 runner    (1001) docker     (123)     9913 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/common.py
--rw-r--r--   0 runner    (1001) docker     (123)     3250 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/config_loader.py
--rw-r--r--   0 runner    (1001) docker     (123)     3606 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/github.py
--rw-r--r--   0 runner    (1001) docker     (123)      369 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/import_resolver.py
--rw-r--r--   0 runner    (1001) docker     (123)     2105 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/kafka.py
--rw-r--r--   0 runner    (1001) docker     (123)      386 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/pattern_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      660 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/pydantic_field_deprecation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2337 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/source_common.py
--rw-r--r--   0 runner    (1001) docker     (123)     2363 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/time_window_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/toml.py
--rw-r--r--   0 runner    (1001) docker     (123)      688 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/validate_field_removal.py
--rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/validate_field_rename.py
--rw-r--r--   0 runner    (1001) docker     (123)      867 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/validate_host_port.py
--rw-r--r--   0 runner    (1001) docker     (123)      301 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/configuration/yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.666425 acryl-datahub-0.9.6rc0/src/datahub/emitter/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      292 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/aspect.py
--rw-r--r--   0 runner    (1001) docker     (123)     5645 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/kafka_emitter.py
--rw-r--r--   0 runner    (1001) docker     (123)    14257 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/mce_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     8174 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/mcp.py
--rw-r--r--   0 runner    (1001) docker     (123)     8969 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/mcp_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2523 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/mcp_patch_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/request_helper.py
--rw-r--r--   0 runner    (1001) docker     (123)    11320 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/rest_emitter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1674 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/emitter/serialization_helper.py
--rw-r--r--   0 runner    (1001) docker     (123)     7876 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/entrypoints.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.666425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.666425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      449 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/closeable.py
--rw-r--r--   0 runner    (1001) docker     (123)      886 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/committable.py
--rw-r--r--   0 runner    (1001) docker     (123)     2671 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/common.py
--rw-r--r--   0 runner    (1001) docker     (123)     3571 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/decorators.py
--rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/ingestion_job_checkpointing_provider_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      608 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/pipeline_run_listener.py
--rw-r--r--   0 runner    (1001) docker     (123)     6346 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/report.py
--rw-r--r--   0 runner    (1001) docker     (123)     4485 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/sink.py
--rw-r--r--   0 runner    (1001) docker     (123)     4989 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/source.py
--rw-r--r--   0 runner    (1001) docker     (123)      582 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     2881 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/workunit.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.666425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      342 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/extractor_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     3701 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/mce_extractor.py
--rw-r--r--   0 runner    (1001) docker     (123)    13147 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/protobuf_util.py
--rw-r--r--   0 runner    (1001) docker     (123)    21985 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/schema_util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.666425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6189 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/classification_mixin.py
--rw-r--r--   0 runner    (1001) docker     (123)     2675 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      307 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/classifier_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     4813 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/datahub_classifier.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.666425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/graph/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/graph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18260 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/graph/client.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.666425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/reporting/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/reporting/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8241 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/reporting/datahub_ingestion_run_summary_provider.py
--rw-r--r--   0 runner    (1001) docker     (123)     1576 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/reporting/file_reporter.py
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/reporting/reporting_provider_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.670425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1474 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)    22445 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     3902 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/pipeline_config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.670425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      591 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/console.py
--rw-r--r--   0 runner    (1001) docker     (123)     2838 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/datahub_kafka.py
--rw-r--r--   0 runner    (1001) docker     (123)     8138 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/datahub_rest.py
--rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/file.py
--rw-r--r--   0 runner    (1001) docker     (123)      593 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/sink_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.674425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.674425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8134 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/aws_common.py
--rw-r--r--   0 runner    (1001) docker     (123)    48184 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/glue.py
--rw-r--r--   0 runner    (1001) docker     (123)     8485 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/path_spec.py
--rw-r--r--   0 runner    (1001) docker     (123)     3884 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/s3_boto_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1694 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/s3_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     3809 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.674425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/common.py
--rw-r--r--   0 runner    (1001) docker     (123)    10383 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/feature_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    10165 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/job_classes.py
--rw-r--r--   0 runner    (1001) docker     (123)    34904 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)     9290 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/lineage.py
--rw-r--r--   0 runner    (1001) docker     (123)    19207 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.674425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/azure/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/azure/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/azure/azure_common.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.678425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    51727 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)    21982 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_audit.py
--rw-r--r--   0 runner    (1001) docker     (123)    12122 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3679 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_report.py
--rw-r--r--   0 runner    (1001) docker     (123)    17574 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     1640 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/common.py
--rw-r--r--   0 runner    (1001) docker     (123)    27853 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/lineage.py
--rw-r--r--   0 runner    (1001) docker     (123)    12757 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/profiler.py
--rw-r--r--   0 runner    (1001) docker     (123)    35244 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/usage.py
--rw-r--r--   0 runner    (1001) docker     (123)    13215 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/confluent_schema_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)    26242 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/csv_enricher.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.678425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12194 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/dbt_cloud.py
--rw-r--r--   0 runner    (1001) docker     (123)    55246 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/dbt_common.py
--rw-r--r--   0 runner    (1001) docker     (123)    17557 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/dbt_core.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.678425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/
--rw-r--r--   0 runner    (1001) docker     (123)       71 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3356 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1635 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/delta_lake_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      467 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/report.py
--rw-r--r--   0 runner    (1001) docker     (123)    12437 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/source.py
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/demo_data.py
--rw-r--r--   0 runner    (1001) docker     (123)    17210 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/elastic_search.py
--rw-r--r--   0 runner    (1001) docker     (123)    14671 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/feast.py
--rw-r--r--   0 runner    (1001) docker     (123)    15277 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/file.py
--rw-r--r--   0 runner    (1001) docker     (123)    41778 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/ge_data_profiler.py
--rw-r--r--   0 runner    (1001) docker     (123)     8586 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/ge_profiling_config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.678425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/git/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/git/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/git/git_import.py
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/glue_profiling_config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.678425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19431 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/iceberg.py
--rw-r--r--   0 runner    (1001) docker     (123)     8221 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/iceberg_common.py
--rw-r--r--   0 runner    (1001) docker     (123)     9563 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/iceberg_profiler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.678425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/identity/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/identity/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27571 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/identity/azure_ad.py
--rw-r--r--   0 runner    (1001) docker     (123)    30901 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/identity/okta.py
--rw-r--r--   0 runner    (1001) docker     (123)    17714 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/kafka.py
--rw-r--r--   0 runner    (1001) docker     (123)    48418 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/kafka_connect.py
--rw-r--r--   0 runner    (1001) docker     (123)      321 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/kafka_schema_registry_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    17354 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/ldap.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.678425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    41479 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_common.py
--rw-r--r--   0 runner    (1001) docker     (123)     7473 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_lib_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     2202 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_query_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    51202 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_source.py
--rw-r--r--   0 runner    (1001) docker     (123)    24029 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_usage.py
--rw-r--r--   0 runner    (1001) docker     (123)    75974 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/lookml_source.py
--rw-r--r--   0 runner    (1001) docker     (123)    22348 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metabase.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.682425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metadata/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metadata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16861 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metadata/business_glossary.py
--rw-r--r--   0 runner    (1001) docker     (123)     8676 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metadata/lineage.py
--rw-r--r--   0 runner    (1001) docker     (123)      326 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metadata_common.py
--rw-r--r--   0 runner    (1001) docker     (123)    30025 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/mode.py
--rw-r--r--   0 runner    (1001) docker     (123)    17163 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/mongodb.py
--rw-r--r--   0 runner    (1001) docker     (123)    43350 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/nifi.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    13322 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/openapi.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    13485 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/openapi_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.682425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7566 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.682425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/data_classes.py
--rw-r--r--   0 runner    (1001) docker     (123)     1586 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/native_sql_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)    24168 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/resolver.py
--rw-r--r--   0 runner    (1001) docker     (123)     4809 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/tree_function.py
--rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/validator.py
--rw-r--r--   0 runner    (1001) docker     (123)    17280 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/powerbi-lexical-grammar.rule
--rw-r--r--   0 runner    (1001) docker     (123)    27978 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/powerbi.py
--rw-r--r--   0 runner    (1001) docker     (123)    33148 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/proxy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.682425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/
--rw-r--r--   0 runner    (1001) docker     (123)      324 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3689 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    20069 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/report_server.py
--rw-r--r--   0 runner    (1001) docker     (123)    11684 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/report_server_domain.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.682425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/profiling/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/profiling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1426 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/profiling/common.py
--rw-r--r--   0 runner    (1001) docker     (123)    20909 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/pulsar.py
--rw-r--r--   0 runner    (1001) docker     (123)    32287 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/redash.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.682425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5057 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/data_lake_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    20777 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/profiling.py
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/report.py
--rw-r--r--   0 runner    (1001) docker     (123)    31007 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/source.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.682425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sagemaker_processors/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sagemaker_processors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27711 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/salesforce.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.686425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      563 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/avro.py
--rw-r--r--   0 runner    (1001) docker     (123)      379 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2229 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/csv_tsv.py
--rw-r--r--   0 runner    (1001) docker     (123)     2103 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/json.py
--rw-r--r--   0 runner    (1001) docker     (123)     5760 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/object.py
--rw-r--r--   0 runner    (1001) docker     (123)     3426 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/parquet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.686425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1581 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     7021 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_config.py
--rw-r--r--   0 runner    (1001) docker     (123)    28950 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_lineage.py
--rw-r--r--   0 runner    (1001) docker     (123)     7204 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_profiler.py
--rw-r--r--   0 runner    (1001) docker     (123)    24377 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     3076 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_report.py
--rw-r--r--   0 runner    (1001) docker     (123)    19227 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     6141 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_tag.py
--rw-r--r--   0 runner    (1001) docker     (123)    18683 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_usage_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)    11155 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    62090 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1043 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/source_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.690425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7350 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/athena.py
--rw-r--r--   0 runner    (1001) docker     (123)    25276 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/clickhouse.py
--rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/druid.py
--rw-r--r--   0 runner    (1001) docker     (123)     1304 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/hana.py
--rw-r--r--   0 runner    (1001) docker     (123)     6411 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/hive.py
--rw-r--r--   0 runner    (1001) docker     (123)      737 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/mariadb.py
--rw-r--r--   0 runner    (1001) docker     (123)    10919 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/mssql.py
--rw-r--r--   0 runner    (1001) docker     (123)     2650 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/mysql.py
--rw-r--r--   0 runner    (1001) docker     (123)     2316 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/oauth_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     6322 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/oracle.py
--rw-r--r--   0 runner    (1001) docker     (123)     8384 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/postgres.py
--rw-r--r--   0 runner    (1001) docker     (123)     3608 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/presto.py
--rw-r--r--   0 runner    (1001) docker     (123)    32011 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/presto_on_hive.py
--rw-r--r--   0 runner    (1001) docker     (123)    43407 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/redshift.py
--rw-r--r--   0 runner    (1001) docker     (123)    53219 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_common.py
--rw-r--r--   0 runner    (1001) docker     (123)     2882 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_generic.py
--rw-r--r--   0 runner    (1001) docker     (123)     7016 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_generic_profiler.py
--rw-r--r--   0 runner    (1001) docker     (123)     9991 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_types.py
--rw-r--r--   0 runner    (1001) docker     (123)    10506 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/trino.py
--rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/two_tier_sql_source.py
--rw-r--r--   0 runner    (1001) docker     (123)    52662 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/vertica.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.690425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8797 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/checkpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     4220 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/entity_removal_state.py
--rw-r--r--   0 runner    (1001) docker     (123)      512 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/profiling_state.py
--rw-r--r--   0 runner    (1001) docker     (123)     4209 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/profiling_state_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)     5544 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/redundant_run_skip_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/sql_common_state.py
--rw-r--r--   0 runner    (1001) docker     (123)    11896 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/stale_entity_removal_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)    16871 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/stateful_ingestion_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/usage_common_state.py
--rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/use_case_handler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.690425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state_provider/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state_provider/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5368 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state_provider/datahub_ingestion_checkpointing_provider.py
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state_provider/state_provider_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)    14155 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/superset.py
--rw-r--r--   0 runner    (1001) docker     (123)    65454 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/tableau.py
--rw-r--r--   0 runner    (1001) docker     (123)    14830 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/tableau_common.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.690425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    11710 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/proxy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1772 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/report.py
--rw-r--r--   0 runner    (1001) docker     (123)    18625 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/source.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.690425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9853 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/clickhouse_usage.py
--rw-r--r--   0 runner    (1001) docker     (123)    15330 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/redshift_usage.py
--rw-r--r--   0 runner    (1001) docker     (123)    10159 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/starburst_trino_usage.py
--rw-r--r--   0 runner    (1001) docker     (123)     5931 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/usage_common.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.690425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1654 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)     1661 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/csv_enricher.py
--rw-r--r--   0 runner    (1001) docker     (123)     6099 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/pulsar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/sql/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5582 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/sql/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)    19492 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/sql/snowflake.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/usage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/usage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7841 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/usage/bigquery_usage.py
--rw-r--r--   0 runner    (1001) docker     (123)      565 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/usage/snowflake_usage.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1037 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/pulsar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/sql/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/sql/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/sql/snowflake.py
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/time_window.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/usage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/usage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/usage/bigquery_usage.py
--rw-r--r--   0 runner    (1001) docker     (123)      780 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/usage/snowflake_usage.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3420 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_browse_path.py
--rw-r--r--   0 runner    (1001) docker     (123)     6849 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_ownership.py
--rw-r--r--   0 runner    (1001) docker     (123)     5605 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_properties.py
--rw-r--r--   0 runner    (1001) docker     (123)     5664 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_schema_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     6239 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_schema_terms.py
--rw-r--r--   0 runner    (1001) docker     (123)     4911 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     5707 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_terms.py
--rw-r--r--   0 runner    (1001) docker     (123)    11200 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/base_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)     6187 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/dataset_domain.py
--rw-r--r--   0 runner    (1001) docker     (123)     1598 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/dataset_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1323 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/mark_dataset_status.py
--rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/remove_dataset_ownership.py
--rw-r--r--   0 runner    (1001) docker     (123)     1401 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/transform_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/integrations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/integrations/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.694425 acryl-datahub-0.9.6rc0/src/datahub/integrations/great_expectations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/integrations/great_expectations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    34380 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/integrations/great_expectations/action.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.698425 acryl-datahub-0.9.6rc0/src/datahub/metadata/
--rw-r--r--   0 runner    (1001) docker     (123)      197 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.698425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.698425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.698425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/events/
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/events/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.698425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.698425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/access/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/access/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.698425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/access/token/
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/access/token/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/assertion/
--rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/assertion/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/chart/
--rw-r--r--   0 runner    (1001) docker     (123)      807 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/chart/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/common/
--rw-r--r--   0 runner    (1001) docker     (123)     3456 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/common/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/common/fieldtransformer/
--rw-r--r--   0 runner    (1001) docker     (123)      355 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/common/fieldtransformer/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/container/
--rw-r--r--   0 runner    (1001) docker     (123)      469 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/container/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dashboard/
--rw-r--r--   0 runner    (1001) docker     (123)      615 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dashboard/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/
--rw-r--r--   0 runner    (1001) docker     (123)      828 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/azkaban/
--rw-r--r--   0 runner    (1001) docker     (123)      253 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/azkaban/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/datahub/
--rw-r--r--   0 runner    (1001) docker     (123)      535 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/datahub/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatform/
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatform/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.702425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatforminstance/
--rw-r--r--   0 runner    (1001) docker     (123)      300 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatforminstance/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataprocess/
--rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataprocess/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataset/
--rw-r--r--   0 runner    (1001) docker     (123)     2204 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataset/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/domain/
--rw-r--r--   0 runner    (1001) docker     (123)      326 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/domain/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/events/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/events/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/events/metadata/
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/events/metadata/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/execution/
--rw-r--r--   0 runner    (1001) docker     (123)      734 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/execution/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/glossary/
--rw-r--r--   0 runner    (1001) docker     (123)      460 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/glossary/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/identity/
--rw-r--r--   0 runner    (1001) docker     (123)     1443 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/identity/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ingestion/
--rw-r--r--   0 runner    (1001) docker     (123)      556 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ingestion/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.706425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/key/
--rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/key/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/filter/
--rw-r--r--   0 runner    (1001) docker     (123)      491 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/filter/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/snapshot/
--rw-r--r--   0 runner    (1001) docker     (123)     2317 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/snapshot/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ml/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ml/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ml/metadata/
--rw-r--r--   0 runner    (1001) docker     (123)     3151 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ml/metadata/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/mxe/
--rw-r--r--   0 runner    (1001) docker     (123)      932 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/mxe/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/notebook/
--rw-r--r--   0 runner    (1001) docker     (123)      860 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/notebook/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/platform/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/platform/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/v1/
--rw-r--r--   0 runner    (1001) docker     (123)      342 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/v1/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/policy/
--rw-r--r--   0 runner    (1001) docker     (123)      876 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/policy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.710425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/post/
--rw-r--r--   0 runner    (1001) docker     (123)      477 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/post/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/retention/
--rw-r--r--   0 runner    (1001) docker     (123)      561 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/retention/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/schema/
--rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/schema/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/secret/
--rw-r--r--   0 runner    (1001) docker     (123)      264 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/secret/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/settings/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/settings/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/settings/global/
--rw-r--r--   0 runner    (1001) docker     (123)      370 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/settings/global/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/step/
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/step/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/tag/
--rw-r--r--   0 runner    (1001) docker     (123)      249 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/tag/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/telemetry/
--rw-r--r--   0 runner    (1001) docker     (123)      261 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/telemetry/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/test/
--rw-r--r--   0 runner    (1001) docker     (123)      670 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/test/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/timeseries/
--rw-r--r--   0 runner    (1001) docker     (123)      596 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/timeseries/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/upgrade/
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/upgrade/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/usage/
--rw-r--r--   0 runner    (1001) docker     (123)      561 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/usage/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.714425 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/view/
--rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/view/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   481738 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schema.avsc
--rw-r--r--   0 runner    (1001) docker     (123)   765987 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schema_classes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.778424 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/
--rw-r--r--   0 runner    (1001) docker     (123)    11363 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/AssertionInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      311 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/AssertionKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     8820 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/AssertionRunEvent.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/BrowsePaths.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2769 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CaveatsAndRecommendations.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    10317 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      863 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartQuery.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     5331 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartUsageStatistics.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      741 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Container.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ContainerKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ContainerProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1290 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpGroupEditableInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpGroupInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      440 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpGroupKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserCredentials.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2473 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserEditableInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3048 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1699 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserSettings.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserStatus.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Cost.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    10755 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DashboardInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DashboardKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     7139 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DashboardUsageStatistics.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3047 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataFlowInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      808 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataFlowKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1606 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubAccessTokenInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      346 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubAccessTokenKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2736 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubIngestionSourceInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      381 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubIngestionSourceKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     7539 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubPolicyInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      390 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubPolicyKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1413 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubRetentionConfig.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      525 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubRetentionKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      687 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubRoleInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubRoleKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      313 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubSecretKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2805 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubSecretValue.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      322 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubStepStateKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2327 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubStepStateProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubUpgradeKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      476 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubUpgradeRequest.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      636 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubUpgradeResult.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    10119 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubViewInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      305 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubViewKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     5490 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataJobInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    13272 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataJobInputOutput.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataJobKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1018 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInstance.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      528 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInstanceKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInstanceProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      340 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      799 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceInput.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      428 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceOutput.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3594 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2098 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceRelationships.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     5739 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceRunEvent.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1930 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     5155 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatahubIngestionCheckpoint.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     8907 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatahubIngestionRunSummary.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1236 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetDeprecation.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1900 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     9088 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetProfile.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3949 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     5197 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetUpstreamLineage.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     6385 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetUsageStatistics.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1033 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Deprecation.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DomainKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2735 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DomainProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      756 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Domains.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3715 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableChartProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      603 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableContainerProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3730 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDashboardProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3726 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDataFlowProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3724 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDataJobProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDatasetProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      439 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableMLFeatureProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      459 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableMLFeatureTableProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      557 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableMLModelGroupProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      534 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableMLModelProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      451 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableMLPrimaryKeyProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3757 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableNotebookProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    10879 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableSchemaMetadata.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      401 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Embed.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3580 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EntityChangeEvent.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EthicalConsiderations.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1615 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EvaluationData.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2229 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ExecutionRequestInput.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ExecutionRequestKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2163 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ExecutionRequestResult.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2463 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ExecutionRequestSignal.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Filter.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      993 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlobalSettingsInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      378 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlobalSettingsKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlobalTags.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryNodeInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryNodeKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2511 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryRelatedTerms.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2755 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryTermInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryTermKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryTerms.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      509 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GroupMembership.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    22925 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/InputFields.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     3593 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/InstitutionalMemory.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1295 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/IntendedUse.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      717 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/InviteToken.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      315 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/InviteTokenKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      605 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     4182 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureTableKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1774 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureTableProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      833 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLHyperParam.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      804 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLMetric.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1925 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelDeploymentKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2976 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelDeploymentProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2613 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelFactorPrompts.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1820 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelGroupKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelGroupProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1862 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     7839 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      622 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLPrimaryKeyKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     4140 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLPrimaryKeyProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)   320156 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MetadataChangeEvent.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    10577 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MetadataChangeLog.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     8224 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MetadataChangeProposal.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      690 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Metrics.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      540 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NativeGroupMembership.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    11920 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NotebookContent.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     5485 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NotebookInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      642 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NotebookKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     6409 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Operation.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      949 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Origin.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     7723 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Ownership.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1460 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/PlatformEvent.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/PostInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/PostKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/QuantitativeAnalyses.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/RoleMembership.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SchemaFieldKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    29823 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SchemaMetadata.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      794 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Siblings.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1236 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SourceCode.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      522 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Status.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SubTypes.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TagKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      821 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TagProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TelemetryClientId.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      370 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TelemetryKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TestInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      281 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TestKey.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     2049 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TestResults.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1970 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TrainingData.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     9068 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/UpstreamLineage.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     4205 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/UsageAggregation.avsc
--rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/VersionInfo.avsc
--rw-r--r--   0 runner    (1001) docker     (123)      701 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ViewProperties.avsc
--rw-r--r--   0 runner    (1001) docker     (123)    19709 2023-01-13 23:01:02.000000 acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.778424 acryl-datahub-0.9.6rc0/src/datahub/specific/
--rw-r--r--   0 runner    (1001) docker     (123)       88 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/specific/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5940 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/specific/dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.778424 acryl-datahub-0.9.6rc0/src/datahub/telemetry/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/telemetry/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      967 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/telemetry/stats.py
--rw-r--r--   0 runner    (1001) docker     (123)    10665 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/telemetry/telemetry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.782424 acryl-datahub-0.9.6rc0/src/datahub/upgrade/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/upgrade/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15072 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/upgrade/upgrade.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.786424 acryl-datahub-0.9.6rc0/src/datahub/utilities/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      444 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/_markupsafe_compat.py
--rw-r--r--   0 runner    (1001) docker     (123)     3146 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/bigquery_sql_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1138 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/checkpoint_state_util.py
--rw-r--r--   0 runner    (1001) docker     (123)      459 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/config_clean.py
--rw-r--r--   0 runner    (1001) docker     (123)      468 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/dedup_list.py
--rw-r--r--   0 runner    (1001) docker     (123)      645 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/delayed_iter.py
--rw-r--r--   0 runner    (1001) docker     (123)    10998 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/hive_schema_to_avro.py
--rw-r--r--   0 runner    (1001) docker     (123)     4614 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/lossy_collections.py
--rw-r--r--   0 runner    (1001) docker     (123)    10545 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/memory_footprint.py
--rw-r--r--   0 runner    (1001) docker     (123)     3933 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/memory_leak_detector.py
--rw-r--r--   0 runner    (1001) docker     (123)      598 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/parsing_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/perf_timer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.786424 acryl-datahub-0.9.6rc0/src/datahub/utilities/registries/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/registries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2450 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/registries/domain_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)      766 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/sample_data.py
--rw-r--r--   0 runner    (1001) docker     (123)      698 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/server_config_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     3250 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/source_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)      871 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/sql_formatter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6522 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/sql_lineage_parser_impl.py
--rw-r--r--   0 runner    (1001) docker     (123)     5961 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/sql_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/sql_parser_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    14281 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/sqlalchemy_query_combiner.py
--rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/sqllineage_patch.py
--rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/stats_collections.py
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/time.py
--rw-r--r--   0 runner    (1001) docker     (123)      970 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/type_annotations.py
--rw-r--r--   0 runner    (1001) docker     (123)      984 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urn_encoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.790424 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/corp_group_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1307 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/corpuser_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     2603 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_flow_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1744 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_job_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_platform_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_process_instance_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     3877 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/dataset_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/domain_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/error.py
--rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/notebook_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1247 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/tag_urn.py
--rw-r--r--   0 runner    (1001) docker     (123)     5447 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/urn.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.790424 acryl-datahub-0.9.6rc0/src/datahub_provider/
--rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      291 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/_airflow_compat.py
--rw-r--r--   0 runner    (1001) docker     (123)      844 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/_airflow_shims.py
--rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/_lineage_core.py
--rw-r--r--   0 runner    (1001) docker     (123)    12817 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/_plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.790424 acryl-datahub-0.9.6rc0/src/datahub_provider/client/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/client/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19518 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/client/airflow_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)      994 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/entities.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.794424 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1319 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/generic_recipe_sample_dag.py
--rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/lineage_backend_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1414 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/lineage_backend_taskflow_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/lineage_emission_dag.py
--rw-r--r--   0 runner    (1001) docker     (123)     1922 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/mysql_sample_dag.py
--rw-r--r--   0 runner    (1001) docker     (123)     3234 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/snowflake_sample_dag.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.794424 acryl-datahub-0.9.6rc0/src/datahub_provider/hooks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/hooks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6980 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/hooks/datahub.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.794424 acryl-datahub-0.9.6rc0/src/datahub_provider/lineage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/lineage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/lineage/datahub.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:23:39.794424 acryl-datahub-0.9.6rc0/src/datahub_provider/operators/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/operators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1848 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub.py
--rw-r--r--   0 runner    (1001) docker     (123)     2900 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_assertion_operator.py
--rw-r--r--   0 runner    (1001) docker     (123)     2903 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_assertion_sensor.py
--rw-r--r--   0 runner    (1001) docker     (123)     3338 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_operation_operator.py
--rw-r--r--   0 runner    (1001) docker     (123)     3606 2023-01-13 22:59:01.000000 acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_operation_sensor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.313660 acryl-datahub-0.9.6rc1/
+-rw-r--r--   0 runner    (1001) docker     (123)    12901 2023-01-13 23:39:10.313660 acryl-datahub-0.9.6rc1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     9980 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      943 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     2035 2023-01-13 23:39:10.313660 acryl-datahub-0.9.6rc1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)    25908 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.081650 acryl-datahub-0.9.6rc1/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.085650 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    12901 2023-01-13 23:39:10.000000 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    30562 2023-01-13 23:39:10.000000 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:39:10.000000 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     6366 2023-01-13 23:39:10.000000 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:10:15.000000 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)    32470 2023-01-13 23:39:10.000000 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-01-13 23:39:10.000000 acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.085650 acryl-datahub-0.9.6rc1/src/datahub/
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-01-13 23:38:56.000000 acryl-datahub-0.9.6rc1/src/datahub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.085650 acryl-datahub-0.9.6rc1/src/datahub/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.085650 acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/
+-rw-r--r--   0 runner    (1001) docker     (123)      268 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5324 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/assertion_circuit_breaker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1471 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/circuit_breaker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2908 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/operation_circuit_breaker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.085650 acryl-datahub-0.9.6rc1/src/datahub/api/entities/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.085650 acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpgroup/
+-rw-r--r--   0 runner    (1001) docker     (123)       63 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpgroup/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpgroup/corpgroup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.085650 acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpuser/
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpuser/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3639 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpuser/corpuser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.089650 acryl-datahub-0.9.6rc1/src/datahub/api/entities/datajob/
+-rw-r--r--   0 runner    (1001) docker     (123)      116 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/datajob/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4265 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/datajob/dataflow.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7492 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/datajob/datajob.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.089650 acryl-datahub-0.9.6rc1/src/datahub/api/entities/dataprocess/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/dataprocess/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14547 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/entities/dataprocess/dataprocess_instance.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.089650 acryl-datahub-0.9.6rc1/src/datahub/api/graphql/
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/graphql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2818 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/graphql/assertion.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1566 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/graphql/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5116 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/api/graphql/operation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.093650 acryl-datahub-0.9.6rc1/src/datahub/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2725 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/check_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22695 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/cli_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16162 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/delete_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4851 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/docker_check.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32728 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/docker_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1429 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/get_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12891 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/ingest_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/json_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16440 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/migrate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8936 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/migration_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3174 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/put_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2590 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/state_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      487 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/telemetry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7350 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/cli/timeline_cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.097651 acryl-datahub-0.9.6rc1/src/datahub/configuration/
+-rw-r--r--   0 runner    (1001) docker     (123)      114 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      934 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/_config_enum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9913 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3250 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/config_loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3606 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/github.py
+-rw-r--r--   0 runner    (1001) docker     (123)      369 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/import_resolver.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2105 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/kafka.py
+-rw-r--r--   0 runner    (1001) docker     (123)      386 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/pattern_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      660 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/pydantic_field_deprecation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2337 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/source_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2363 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/time_window_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/toml.py
+-rw-r--r--   0 runner    (1001) docker     (123)      688 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/validate_field_removal.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/validate_field_rename.py
+-rw-r--r--   0 runner    (1001) docker     (123)      867 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/validate_host_port.py
+-rw-r--r--   0 runner    (1001) docker     (123)      301 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/configuration/yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.097651 acryl-datahub-0.9.6rc1/src/datahub/emitter/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      292 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/aspect.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5645 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/kafka_emitter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14257 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/mce_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8174 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/mcp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9187 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/mcp_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2523 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/mcp_patch_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/request_helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11320 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/rest_emitter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1674 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/emitter/serialization_helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7876 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/entrypoints.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.097651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.101651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      449 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/closeable.py
+-rw-r--r--   0 runner    (1001) docker     (123)      886 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/committable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2671 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3571 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/ingestion_job_checkpointing_provider_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      608 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/pipeline_run_listener.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6346 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4485 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/sink.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4989 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/source.py
+-rw-r--r--   0 runner    (1001) docker     (123)      582 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2881 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/workunit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.105651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      342 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/extractor_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3701 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/mce_extractor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13147 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/protobuf_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21985 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/schema_util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.105651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6189 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/classification_mixin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2675 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/classifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)      307 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/classifier_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4813 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/datahub_classifier.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.105651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/graph/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/graph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18260 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/graph/client.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.105651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/reporting/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/reporting/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8241 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/reporting/datahub_ingestion_run_summary_provider.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1576 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/reporting/file_reporter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/reporting/reporting_provider_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.105651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1474 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22445 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3902 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/pipeline_config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.109651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      591 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/console.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2838 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/datahub_kafka.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8138 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/datahub_rest.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      593 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/sink_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.117651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.117651 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8134 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/aws_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48184 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/glue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8485 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/path_spec.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3884 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/s3_boto_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1694 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/s3_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3809 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.121652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10383 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/feature_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10165 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/job_classes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34904 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9290 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/lineage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19207 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.121652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/azure/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/azure/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/azure/azure_common.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.125652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51727 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21982 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_audit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12122 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3679 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17574 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1640 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27853 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/lineage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12757 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/profiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35171 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13215 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/confluent_schema_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26242 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/csv_enricher.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.125652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12194 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/dbt_cloud.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55246 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/dbt_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17557 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/dbt_core.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.125652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/
+-rw-r--r--   0 runner    (1001) docker     (123)       71 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3356 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1635 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/delta_lake_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      467 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12437 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/source.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/demo_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17210 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/elastic_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14671 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/feast.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15277 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41778 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/ge_data_profiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8586 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/ge_profiling_config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.125652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/git/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/git/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/git/git_import.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/glue_profiling_config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.129652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19431 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/iceberg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8221 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/iceberg_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9563 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/iceberg_profiler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.129652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/identity/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/identity/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27571 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/identity/azure_ad.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30901 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/identity/okta.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17714 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/kafka.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48418 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/kafka_connect.py
+-rw-r--r--   0 runner    (1001) docker     (123)      321 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/kafka_schema_registry_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17354 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/ldap.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.129652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42243 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7473 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_lib_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2202 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_query_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    54007 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_source.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24029 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    75974 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/lookml_source.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22348 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metabase.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.133652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metadata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16861 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metadata/business_glossary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8676 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metadata/lineage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metadata_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30025 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/mode.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17163 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/mongodb.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43350 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/nifi.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    13322 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/openapi.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    13485 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/openapi_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.133652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7566 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.137652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/data_classes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1586 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/native_sql_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24168 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/resolver.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4809 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/tree_function.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17280 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/powerbi-lexical-grammar.rule
+-rw-r--r--   0 runner    (1001) docker     (123)    27285 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/powerbi.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33148 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/proxy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.137652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/
+-rw-r--r--   0 runner    (1001) docker     (123)      324 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3689 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20069 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/report_server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11684 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/report_server_domain.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.137652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/profiling/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/profiling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1426 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/profiling/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20909 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/pulsar.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32287 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/redash.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.141652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5057 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/data_lake_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20777 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/profiling.py
+-rw-r--r--   0 runner    (1001) docker     (123)      466 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31007 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/source.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.141652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sagemaker_processors/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sagemaker_processors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27711 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/salesforce.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.141652 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      563 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/avro.py
+-rw-r--r--   0 runner    (1001) docker     (123)      379 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2229 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/csv_tsv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2103 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5760 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/object.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3426 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/parquet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.145653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1581 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7021 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28950 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_lineage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7204 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_profiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24377 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3076 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19227 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6141 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_tag.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18683 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_usage_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11155 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    62090 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1043 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/source_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.153653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7350 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/athena.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25276 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/clickhouse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/druid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1304 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/hana.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6411 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/hive.py
+-rw-r--r--   0 runner    (1001) docker     (123)      737 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/mariadb.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10919 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/mssql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2650 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/mysql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2316 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/oauth_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6322 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/oracle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8384 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/postgres.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3608 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/presto.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32011 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/presto_on_hive.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43407 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (123)    53219 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2882 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_generic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7016 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_generic_profiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9991 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10506 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/trino.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/two_tier_sql_source.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52662 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/vertica.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.157653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8797 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/checkpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4220 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/entity_removal_state.py
+-rw-r--r--   0 runner    (1001) docker     (123)      512 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/profiling_state.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4209 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/profiling_state_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5544 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/redundant_run_skip_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/sql_common_state.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11896 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/stale_entity_removal_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16871 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/stateful_ingestion_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/usage_common_state.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/use_case_handler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.157653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state_provider/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state_provider/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5368 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state_provider/datahub_ingestion_checkpointing_provider.py
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state_provider/state_provider_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14155 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/superset.py
+-rw-r--r--   0 runner    (1001) docker     (123)    65454 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/tableau.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14830 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/tableau_common.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.161653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11710 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/proxy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1772 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18625 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/source.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.161653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9853 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/clickhouse_usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15330 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/redshift_usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10159 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/starburst_trino_usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5931 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/usage_common.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.165653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1654 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1661 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/csv_enricher.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6099 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/pulsar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.165653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5582 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/sql/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19492 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/sql/snowflake.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.165653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/usage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/usage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7841 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/usage/bigquery_usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      565 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/usage/snowflake_usage.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.165653 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1037 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/pulsar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.169654 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/sql/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/sql/snowflake.py
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/time_window.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.169654 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/usage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/usage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/usage/bigquery_usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      780 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/usage/snowflake_usage.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.173654 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3420 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_browse_path.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6849 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_ownership.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5605 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_properties.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5664 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_schema_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6239 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_schema_terms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4911 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5707 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_terms.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11200 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/base_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6187 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/dataset_domain.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1598 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/dataset_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1323 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/mark_dataset_status.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/remove_dataset_ownership.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1401 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/transform_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.173654 acryl-datahub-0.9.6rc1/src/datahub/integrations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/integrations/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.173654 acryl-datahub-0.9.6rc1/src/datahub/integrations/great_expectations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/integrations/great_expectations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34380 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/integrations/great_expectations/action.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)      197 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/events/
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/events/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/access/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/access/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/access/token/
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/access/token/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.177654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/assertion/
+-rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/assertion/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/chart/
+-rw-r--r--   0 runner    (1001) docker     (123)      807 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/chart/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/common/
+-rw-r--r--   0 runner    (1001) docker     (123)     3456 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/common/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/common/fieldtransformer/
+-rw-r--r--   0 runner    (1001) docker     (123)      355 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/common/fieldtransformer/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/container/
+-rw-r--r--   0 runner    (1001) docker     (123)      469 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/container/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dashboard/
+-rw-r--r--   0 runner    (1001) docker     (123)      615 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dashboard/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/
+-rw-r--r--   0 runner    (1001) docker     (123)      828 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/azkaban/
+-rw-r--r--   0 runner    (1001) docker     (123)      253 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/azkaban/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/datahub/
+-rw-r--r--   0 runner    (1001) docker     (123)      535 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/datahub/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatform/
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatform/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatforminstance/
+-rw-r--r--   0 runner    (1001) docker     (123)      300 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataplatforminstance/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataprocess/
+-rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataprocess/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataset/
+-rw-r--r--   0 runner    (1001) docker     (123)     2204 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataset/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.181654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/domain/
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/domain/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/events/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/events/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/events/metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/events/metadata/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/execution/
+-rw-r--r--   0 runner    (1001) docker     (123)      734 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/execution/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/glossary/
+-rw-r--r--   0 runner    (1001) docker     (123)      460 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/glossary/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/identity/
+-rw-r--r--   0 runner    (1001) docker     (123)     1443 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/identity/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ingestion/
+-rw-r--r--   0 runner    (1001) docker     (123)      556 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ingestion/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/key/
+-rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/key/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/filter/
+-rw-r--r--   0 runner    (1001) docker     (123)      491 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/query/filter/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/snapshot/
+-rw-r--r--   0 runner    (1001) docker     (123)     2317 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/snapshot/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ml/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ml/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ml/metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)     3151 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ml/metadata/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/mxe/
+-rw-r--r--   0 runner    (1001) docker     (123)      932 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/mxe/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/notebook/
+-rw-r--r--   0 runner    (1001) docker     (123)      860 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/notebook/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.185654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/platform/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/platform/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/v1/
+-rw-r--r--   0 runner    (1001) docker     (123)      342 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/platform/event/v1/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/policy/
+-rw-r--r--   0 runner    (1001) docker     (123)      876 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/policy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/post/
+-rw-r--r--   0 runner    (1001) docker     (123)      477 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/post/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/retention/
+-rw-r--r--   0 runner    (1001) docker     (123)      561 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/retention/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/schema/
+-rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/schema/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/secret/
+-rw-r--r--   0 runner    (1001) docker     (123)      264 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/secret/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/settings/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/settings/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/settings/global/
+-rw-r--r--   0 runner    (1001) docker     (123)      370 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/settings/global/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/step/
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/step/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/tag/
+-rw-r--r--   0 runner    (1001) docker     (123)      249 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/tag/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/telemetry/
+-rw-r--r--   0 runner    (1001) docker     (123)      261 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/telemetry/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/test/
+-rw-r--r--   0 runner    (1001) docker     (123)      670 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/test/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/timeseries/
+-rw-r--r--   0 runner    (1001) docker     (123)      596 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/timeseries/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.189654 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/upgrade/
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/upgrade/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.193655 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/usage/
+-rw-r--r--   0 runner    (1001) docker     (123)      561 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/usage/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.193655 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/view/
+-rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/view/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   481738 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schema.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)   765987 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schema_classes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.293659 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/
+-rw-r--r--   0 runner    (1001) docker     (123)    11363 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/AssertionInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      311 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/AssertionKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     8820 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/AssertionRunEvent.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/BrowsePaths.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2769 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CaveatsAndRecommendations.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    10317 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      758 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      863 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartQuery.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     5331 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartUsageStatistics.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      741 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Container.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ContainerKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ContainerProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1290 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpGroupEditableInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpGroupInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      440 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpGroupKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      980 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserCredentials.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2473 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserEditableInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3048 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1699 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserSettings.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserStatus.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Cost.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    10755 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DashboardInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DashboardKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     7139 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DashboardUsageStatistics.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3047 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataFlowInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      808 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataFlowKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1606 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubAccessTokenInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      346 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubAccessTokenKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2736 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubIngestionSourceInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      381 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubIngestionSourceKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     7539 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubPolicyInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      390 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubPolicyKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1413 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubRetentionConfig.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      525 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubRetentionKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      687 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubRoleInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubRoleKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      313 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubSecretKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2805 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubSecretValue.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      322 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubStepStateKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2327 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubStepStateProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubUpgradeKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      476 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubUpgradeRequest.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      636 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubUpgradeResult.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    10119 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubViewInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      305 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubViewKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     5490 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataJobInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    13272 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataJobInputOutput.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataJobKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1018 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInstance.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      528 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInstanceKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInstanceProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      340 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceInput.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      428 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceOutput.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3594 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2098 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceRelationships.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     5739 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceRunEvent.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1930 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     5155 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatahubIngestionCheckpoint.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     8907 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatahubIngestionRunSummary.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1236 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetDeprecation.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1900 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     9088 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetProfile.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3949 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     5197 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetUpstreamLineage.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     6385 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetUsageStatistics.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1033 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Deprecation.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DomainKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2735 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DomainProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      756 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Domains.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3715 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableChartProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      603 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableContainerProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3730 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDashboardProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3726 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDataFlowProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3724 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDataJobProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDatasetProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      439 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableMLFeatureProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      459 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableMLFeatureTableProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      557 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableMLModelGroupProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableMLModelProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      451 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableMLPrimaryKeyProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3757 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableNotebookProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    10879 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableSchemaMetadata.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      401 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Embed.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3580 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EntityChangeEvent.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EthicalConsiderations.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1615 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EvaluationData.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2229 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ExecutionRequestInput.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ExecutionRequestKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2163 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ExecutionRequestResult.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2463 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ExecutionRequestSignal.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Filter.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      993 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlobalSettingsInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      378 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlobalSettingsKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlobalTags.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryNodeInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryNodeKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2511 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryRelatedTerms.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2755 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryTermInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryTermKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryTerms.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      509 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GroupMembership.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    22925 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/InputFields.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     3593 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/InstitutionalMemory.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1295 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/IntendedUse.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      717 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/InviteToken.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      315 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/InviteTokenKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      605 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     4182 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureTableKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1774 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureTableProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      833 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLHyperParam.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      804 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLMetric.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1925 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelDeploymentKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2976 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelDeploymentProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2613 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelFactorPrompts.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1820 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelGroupKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelGroupProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1862 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     7839 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      622 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLPrimaryKeyKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     4140 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLPrimaryKeyProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)   320156 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MetadataChangeEvent.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    10577 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MetadataChangeLog.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     8224 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MetadataChangeProposal.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      690 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Metrics.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      540 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NativeGroupMembership.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    11920 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NotebookContent.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     5485 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NotebookInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      642 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NotebookKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     6409 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Operation.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      949 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Origin.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     7723 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Ownership.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1460 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/PlatformEvent.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/PostInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/PostKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      960 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/QuantitativeAnalyses.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/RoleMembership.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SchemaFieldKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    29823 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SchemaMetadata.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      794 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Siblings.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1236 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SourceCode.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      522 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Status.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      654 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SubTypes.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      457 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TagKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      821 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TagProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TelemetryClientId.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      370 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TelemetryKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TestInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      281 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TestKey.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     2049 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TestResults.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1970 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TrainingData.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     9068 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/UpstreamLineage.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     4205 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/UsageAggregation.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/VersionInfo.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)      701 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ViewProperties.avsc
+-rw-r--r--   0 runner    (1001) docker     (123)    19709 2023-01-13 23:11:01.000000 acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.293659 acryl-datahub-0.9.6rc1/src/datahub/specific/
+-rw-r--r--   0 runner    (1001) docker     (123)       88 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/specific/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5940 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/specific/dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.293659 acryl-datahub-0.9.6rc1/src/datahub/telemetry/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/telemetry/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      967 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/telemetry/stats.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10665 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/telemetry/telemetry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.297659 acryl-datahub-0.9.6rc1/src/datahub/upgrade/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/upgrade/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15072 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/upgrade/upgrade.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.305659 acryl-datahub-0.9.6rc1/src/datahub/utilities/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      444 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/_markupsafe_compat.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3146 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/bigquery_sql_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1138 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/checkpoint_state_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)      459 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/config_clean.py
+-rw-r--r--   0 runner    (1001) docker     (123)      468 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/dedup_list.py
+-rw-r--r--   0 runner    (1001) docker     (123)      645 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/delayed_iter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10998 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/hive_schema_to_avro.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4614 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/lossy_collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10545 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/memory_footprint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3933 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/memory_leak_detector.py
+-rw-r--r--   0 runner    (1001) docker     (123)      598 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/parsing_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/perf_timer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.305659 acryl-datahub-0.9.6rc1/src/datahub/utilities/registries/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/registries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2450 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/registries/domain_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)      766 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/sample_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      698 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/server_config_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3250 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/source_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      871 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/sql_formatter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6522 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/sql_lineage_parser_impl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5961 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/sql_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/sql_parser_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14281 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/sqlalchemy_query_combiner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/sqllineage_patch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/stats_collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/time.py
+-rw-r--r--   0 runner    (1001) docker     (123)      970 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/type_annotations.py
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/url_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)      984 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urn_encoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.305659 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/corp_group_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1307 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/corpuser_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2603 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_flow_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1744 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_job_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_platform_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_process_instance_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3877 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/dataset_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/domain_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/error.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/notebook_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1247 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/tag_urn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5447 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/urn.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.309660 acryl-datahub-0.9.6rc1/src/datahub_provider/
+-rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      291 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/_airflow_compat.py
+-rw-r--r--   0 runner    (1001) docker     (123)      844 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/_airflow_shims.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/_lineage_core.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12817 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/_plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.309660 acryl-datahub-0.9.6rc1/src/datahub_provider/client/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/client/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19518 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/client/airflow_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)      994 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/entities.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.309660 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1319 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/generic_recipe_sample_dag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/lineage_backend_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1414 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/lineage_backend_taskflow_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/lineage_emission_dag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1922 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/mysql_sample_dag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3234 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/snowflake_sample_dag.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.313660 acryl-datahub-0.9.6rc1/src/datahub_provider/hooks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/hooks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6980 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/hooks/datahub.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.313660 acryl-datahub-0.9.6rc1/src/datahub_provider/lineage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/lineage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/lineage/datahub.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:39:10.313660 acryl-datahub-0.9.6rc1/src/datahub_provider/operators/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/operators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1848 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2900 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_assertion_operator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2903 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_assertion_sensor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3338 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_operation_operator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3606 2023-01-13 23:08:22.000000 acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_operation_sensor.py
```

### Comparing `acryl-datahub-0.9.6rc0/PKG-INFO` & `acryl-datahub-0.9.6rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: acryl-datahub
-Version: 0.9.6rc0
+Version: 0.9.6rc1
 Summary: A CLI to work with DataHub metadata
 Home-page: https://datahubproject.io/
 License: Apache License 2.0
 Project-URL: Documentation, https://datahubproject.io/docs/
 Project-URL: Source, https://github.com/datahub-project/datahub
 Project-URL: Changelog, https://github.com/datahub-project/datahub/releases
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `acryl-datahub-0.9.6rc0/README.md` & `acryl-datahub-0.9.6rc1/README.md`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/pyproject.toml` & `acryl-datahub-0.9.6rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/setup.cfg` & `acryl-datahub-0.9.6rc1/setup.cfg`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/setup.py` & `acryl-datahub-0.9.6rc1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -339,15 +339,15 @@
     },
     "tableau": {"tableauserverclient>=0.17.0"},
     "trino": sql_common | trino,
     "starburst-trino-usage": sql_common | usage_common | trino,
     "nifi": {"requests", "packaging"},
     "powerbi": microsoft_common | {"lark[regex]==1.1.4", "sqlparse"},
     "powerbi-report-server": powerbi_report_server,
-    "vertica": sql_common | {"sqlalchemy-vertica-dialect[vertica-python]==0.1.4"},
+    "vertica": sql_common | {"vertica-sqlalchemy-dialect[vertica-python]==0.0.1"},
     "unity-catalog": databricks_cli | {"requests"},
 }
 
 all_exclude_plugins: Set[str] = {
     # SQL Server ODBC requires additional drivers, and so we don't want to keep
     # it included in the default "all" installation.
     "mssql-odbc",
```

### Comparing `acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/PKG-INFO` & `acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: acryl-datahub
-Version: 0.9.6rc0
+Version: 0.9.6rc1
 Summary: A CLI to work with DataHub metadata
 Home-page: https://datahubproject.io/
 License: Apache License 2.0
 Project-URL: Documentation, https://datahubproject.io/docs/
 Project-URL: Source, https://github.com/datahub-project/datahub
 Project-URL: Changelog, https://github.com/datahub-project/datahub/releases
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/SOURCES.txt` & `acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -567,14 +567,15 @@
 src/datahub/utilities/sql_parser.py
 src/datahub/utilities/sql_parser_base.py
 src/datahub/utilities/sqlalchemy_query_combiner.py
 src/datahub/utilities/sqllineage_patch.py
 src/datahub/utilities/stats_collections.py
 src/datahub/utilities/time.py
 src/datahub/utilities/type_annotations.py
+src/datahub/utilities/url_util.py
 src/datahub/utilities/urn_encoder.py
 src/datahub/utilities/registries/__init__.py
 src/datahub/utilities/registries/domain_registry.py
 src/datahub/utilities/urns/__init__.py
 src/datahub/utilities/urns/corp_group_urn.py
 src/datahub/utilities/urns/corpuser_urn.py
 src/datahub/utilities/urns/data_flow_urn.py
```

### Comparing `acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/entry_points.txt` & `acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/entry_points.txt`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/acryl_datahub.egg-info/requires.txt` & `acryl-datahub-0.9.6rc1/src/acryl_datahub.egg-info/requires.txt`

 * *Files 16% similar despite different names*

```diff
@@ -1,2200 +1,2200 @@
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
-mixpanel>=4.9.0
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
+typing-inspect
+mixpanel>=4.9.0
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-typing-inspect
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-mypy_extensions>=0.4.3
-pydantic!=1.10.3,>=1.5.1
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+pydantic!=1.10.3,>=1.5.1
+expandvars>=0.6.5
+mypy_extensions>=0.4.3
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [:python_version < "3.8"]
 typing_extensions>=3.7.4.3
 
 [:python_version >= "3.8"]
 typing_extensions>=3.10.0.2
 
 [airflow]
-fastavro>=1.2.0
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
-avro-gen3==0.7.8
-toml>=0.10.0
-avro<1.11,>=1.10.2
-humanfriendly
-click>=7.1.2
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
 apache-airflow>=2.0.2
-entrypoints
 Deprecated
-requests
-PyYAML
 cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro-gen3==0.7.8
+toml>=0.10.0
+humanfriendly
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
-ijson
+expandvars>=0.6.5
+stackprinter>=0.2.6
 confluent_kafka>=1.5.0
-progressbar2
-ratelimiter
+click>=7.1.2
+requests
+ijson
+fastavro>=1.2.0
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [airflow:platform_system != "Darwin" and (platform_machine == "aarch64" or platform_machine == "arm64")]
 confluent_kafka<1.9.0
 
 [all]
-great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
-stackprinter>=0.2.6
-feast~=0.26.0
-click-spinner
-acryl-pyhive[hive]>=0.6.12
-looker-sdk==22.2.1
-avro-gen3==0.7.8
+great_expectations
+sqlalchemy-pytds>=0.3
+elasticsearch==7.13.4
+spacy==3.4.3
+sqlparse
+sqlalchemy-redshift
+traitlets<5.2.2
+pymysql>=1.0.2
 sql-metadata
+avro-gen3==0.7.8
+humanfriendly
+botocore!=1.23.0
+snowflake-sqlalchemy!=1.2.5,>=1.2.4
+pydeequ>=1.0.1
+GitPython>2
+SQLAlchemy<1.4.42
+feast~=0.26.0
 click>=7.1.2
-pymongo[srv]>=3.11
-cached_property
-deltalake!=0.6.4,>=0.6.3
-requests_file
-JPype1
-great-expectations<=0.15.41,>=0.15.12
-sqlparse
-psutil>=5.8.0
-databricks-dbapi
+vertica-sqlalchemy-dialect[vertica-python]==0.0.1
 tableauserverclient>=0.17.0
-okta~=1.7.0
-google-cloud-logging<3.1.2
-pyarrow>=6.0.1
-python-dateutil>=2.8.0
-progressbar2
-PyAthena[sqlalchemy]==2.4.1
-wcmatch
-azure-identity==1.10.0
-pydeequ>=1.0.1
-spacy==3.4.3
-snowflake-sqlalchemy!=1.2.5,>=1.2.4
-traitlets<5.2.2
-simple-salesforce
-lkml>=1.3.0b5
-acryl-pyhive[hive]>=0.6.13
-Deprecated
-requests
-greenlet
-more-itertools>=8.12.0
-great_expectations
-PyYAML
-sqllineage==1.3.6
-grpcio-tools<2,>=1.44.0
-python-ldap>=2.4
-msal==1.16.0
-click-default-group
-moto[s3]
-acryl-datahub-classify>=0.0.4
-GeoAlchemy2
-ratelimiter
+tabulate
+great-expectations<=0.15.41,>=0.15.12
+requests_ntlm
+aiohttp<4
+click-spinner
+great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
+pymongo[srv]>=3.11
 pandas
+ujson>=5.2.0
+acryl-datahub-classify>=0.0.4
 msal
-databricks-cli==0.17.3
-trino[sqlalchemy]!=0.317,>=0.308
-lark[regex]==1.1.4
+looker-sdk==22.2.1
 toml>=0.10.0
-botocore!=1.23.0
+cx_Oracle
+progressbar2
+deltalake!=0.6.4,>=0.6.3
+acryl-iceberg-legacy==0.0.4
 cryptography
+okta~=1.7.0
+google-api-python-client
+python-ldap>=2.4
+grpcio-tools<2,>=1.44.0
+grpcio<2,>=1.44.0
+psycopg2-binary
+sqllineage==1.3.6
+databricks-cli==0.17.3
+fastavro>=1.2.0
+parse>=1.19.0
 sql-metadata==2.2.2
-apache-airflow>=2.0.2
-tableschema>=1.20.2
 scipy>=1.7.2
-psycopg2-binary
-sqlalchemy-pytds>=0.3
-tabulate
+packaging
+tableschema>=1.20.2
+azure-identity==1.10.0
+JPype1
+PyAthena[sqlalchemy]==2.4.1
 google-cloud-bigquery
-clickhouse-sqlalchemy>=0.1.8
-termcolor>=1.0.0
-requests_ntlm
-redash-toolbelt
-pymysql>=1.0.2
-grpcio<2,>=1.44.0
-GitPython>2
-snowflake-connector-python!=2.8.2
-fastavro>=1.2.0
-SQLAlchemy<1.4.42
-cx_Oracle
-networkx>=2.6.2
+lark[regex]==1.1.4
+databricks-dbapi
+sqlalchemy-bigquery>=1.4.1
+psutil>=5.8.0
+pyspark==3.0.3
+acryl-pyhive[hive]>=0.6.12
+Deprecated
+cached_property
+tenacity>=8.0.1
 avro<1.11,>=1.10.2
-acryl-iceberg-legacy==0.0.4
-flask-openid>=1.3.0
+simple-salesforce
 sqlalchemy
-humanfriendly
-ujson>=5.2.0
-sqlalchemy-redshift
-entrypoints
+redash-toolbelt
+more-itertools>=8.12.0
+confluent_kafka>=1.5.0
 sqlalchemy<2,>=1.3.24
-google-api-python-client
-gql[requests]>=3.3.0
-pydruid>=0.6.2
-aiohttp<4
-smart-open[s3]>=5.2.1
-expandvars>=0.6.5
-tenacity>=8.0.1
-sqlalchemy-vertica-dialect[vertica-python]==0.1.4
-pyspark==3.0.3
-parse>=1.19.0
-packaging
+requests
+entrypoints
+pyarrow>=6.0.1
 gql>=3.3.0
-boto3
+requests_file
+snowflake-connector-python!=2.8.2
+msal==1.16.0
+gql[requests]>=3.3.0
+lkml>=1.3.0b5
+GeoAlchemy2
+moto[s3]
+click-default-group
+ratelimiter
+networkx>=2.6.2
+greenlet
+PyYAML
+apache-airflow>=2.0.2
+trino[sqlalchemy]!=0.317,>=0.308
+termcolor>=1.0.0
 docker
+acryl-pyhive[hive]>=0.6.13
+flask-openid>=1.3.0
+expandvars>=0.6.5
+clickhouse-sqlalchemy>=0.1.8
+wcmatch
+stackprinter>=0.2.6
+google-cloud-logging<3.1.2
 ijson
-elasticsearch==7.13.4
-confluent_kafka>=1.5.0
-sqlalchemy-bigquery>=1.4.1
+smart-open[s3]>=5.2.1
+boto3
+pydruid>=0.6.2
+python-dateutil>=2.8.0
 
 [all:platform_machine != "aarch64" and platform_machine != "arm64"]
-sqlalchemy-hana>=0.5.0
 hdbcli>=2.11.20
+sqlalchemy-hana>=0.5.0
 
 [all:platform_system != "Darwin" and (platform_machine == "aarch64" or platform_machine == "arm64")]
 confluent_kafka<1.9.0
 
 [athena]
-python-dateutil>=2.8.0
 PyAthena[sqlalchemy]==2.4.1
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [azure-ad]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [base]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [bigquery]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
+google-cloud-bigquery
 click-spinner
+click-default-group
+ratelimiter
+sqlalchemy-bigquery>=1.4.1
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+sql_metadata
+expandvars>=0.6.5
+google-api-python-client
 more-itertools>=8.12.0
-sqlalchemy-bigquery>=1.4.1
+stackprinter>=0.2.6
+google-cloud-logging<3.1.2
+click>=7.1.2
+sqllineage==1.3.6
 sqlalchemy<2,>=1.3.24
+ijson
+entrypoints
 scipy>=1.7.2
-greenlet
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-sqllineage==1.3.6
-google-cloud-bigquery
-google-api-python-client
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-sql_metadata
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
-google-cloud-logging<3.1.2
+python-dateutil>=2.8.0
 
 [bigquery-beta]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
+google-cloud-bigquery
 click-spinner
+click-default-group
+ratelimiter
+sqlalchemy-bigquery>=1.4.1
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+sql_metadata
+expandvars>=0.6.5
+google-api-python-client
 more-itertools>=8.12.0
-sqlalchemy-bigquery>=1.4.1
+stackprinter>=0.2.6
+google-cloud-logging<3.1.2
+click>=7.1.2
+sqllineage==1.3.6
 sqlalchemy<2,>=1.3.24
+ijson
+entrypoints
 scipy>=1.7.2
-greenlet
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-sqllineage==1.3.6
-google-cloud-bigquery
-google-api-python-client
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-sql_metadata
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
-google-cloud-logging<3.1.2
+python-dateutil>=2.8.0
 
 [circuit-breaker]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
-click-spinner
-avro-gen3==0.7.8
-toml>=0.10.0
-avro<1.11,>=1.10.2
-humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
 aiohttp<4
-tabulate
-expandvars>=0.6.5
+click-spinner
 gql[requests]>=3.3.0
-requests_file
 click-default-group
-termcolor>=1.0.0
-packaging
+ratelimiter
 gql>=3.3.0
 psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
+avro-gen3==0.7.8
+toml>=0.10.0
+humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [clickhouse]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+clickhouse-sqlalchemy>=0.1.8
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-clickhouse-sqlalchemy>=0.1.8
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [clickhouse-usage]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+sqlparse
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+clickhouse-sqlalchemy>=0.1.8
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-clickhouse-sqlalchemy>=0.1.8
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-sqlparse
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [datahub-business-glossary]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [datahub-kafka]
-fastavro>=1.2.0
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
-ijson
+expandvars>=0.6.5
+stackprinter>=0.2.6
 confluent_kafka>=1.5.0
-progressbar2
-ratelimiter
+click>=7.1.2
+ijson
+fastavro>=1.2.0
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [datahub-kafka:platform_system != "Darwin" and (platform_machine == "aarch64" or platform_machine == "arm64")]
 confluent_kafka<1.9.0
 
 [datahub-lineage-file]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [datahub-rest]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+requests
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [dbt]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 botocore!=1.23.0
-humanfriendly
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
+ijson
+entrypoints
 packaging
 boto3
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [dbt-cloud]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+requests
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [delta-lake]
-python-dateutil>=2.8.0
-wcmatch
-stackprinter>=0.2.6
-pydeequ>=1.0.1
+aiohttp<4
+moto[s3]
+boto3
 click-spinner
+ujson>=5.2.0
+click-default-group
+ratelimiter
+psutil>=5.8.0
+pyspark==3.0.3
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 botocore!=1.23.0
-humanfriendly
-click>=7.1.2
-ujson>=5.2.0
-entrypoints
-Deprecated
-tableschema>=1.20.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-smart-open[s3]>=5.2.1
 deltalake!=0.6.4,>=0.6.3
-requests_file
-click-default-group
-moto[s3]
-termcolor>=1.0.0
-packaging
-pyspark==3.0.3
-parse>=1.19.0
-boto3
-psutil>=5.8.0
 docker
+pydeequ>=1.0.1
+expandvars>=0.6.5
+wcmatch
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+parse>=1.19.0
 pyarrow>=6.0.1
+packaging
+tableschema>=1.20.2
+requests_file
+smart-open[s3]>=5.2.1
+tabulate
+python-dateutil>=2.8.0
 
 [dev]
-types-six
-great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
+spacy==3.4.3
+sqlalchemy-redshift
+types-PyMySQL
+traitlets<5.2.2
+pymysql>=1.0.2
+botocore!=1.23.0
+snowflake-sqlalchemy!=1.2.5,>=1.2.4
+pydeequ>=1.0.1
+pydantic!=1.10.3,>=1.5.1
+sql_metadata
+GitPython>2
+SQLAlchemy<1.4.42
+types-cachetools
 feast~=0.26.0
-mixpanel>=4.9.0
-types-pyOpenSSL
+types-freezegun
+click>=7.1.2
 coverage>=5.1
-typing-inspect
-cached_property
-pydantic!=1.10.3,>=1.5.1
-types-PyMySQL
+types-tabulate
+tableauserverclient>=0.17.0
+types-dataclasses
+types-toml
 great-expectations<=0.15.41,>=0.15.12
-types-click-spinner>=0.1.13.1
-requests-mock
-databricks-dbapi
-pyarrow>=6.0.1
-wcmatch
-azure-identity==1.10.0
-pydeequ>=1.0.1
-spacy==3.4.3
-snowflake-sqlalchemy!=1.2.5,>=1.2.4
-traitlets<5.2.2
-simple-salesforce
-types-pytz
-acryl-pyhive[hive]>=0.6.13
-Deprecated
-more-itertools>=8.12.0
-greenlet
-python-ldap>=2.4
-click-default-group
-pytest-cov>=2.8.1
-types-protobuf>=4.21.0.1
-black==22.12.0
-ratelimiter
+types-six
+aiohttp<4
+click-spinner
+great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
 msal
-types-requests>=2.28.11.6
-trino[sqlalchemy]!=0.317,>=0.308
 toml>=0.10.0
-cryptography
-types-cachetools
-sql-metadata==2.2.2
-tableschema>=1.20.2
-build
+cx_Oracle
+deepdiff
+progressbar2
+types-requests>=2.28.11.6
+acryl-iceberg-legacy==0.0.4
+twine
+google-api-python-client
+grpcio-tools<2,>=1.44.0
+grpcio<2,>=1.44.0
+databricks-cli==0.17.3
 types-termcolor>=1.0.0
-pytest-asyncio>=0.16.0
-google-cloud-bigquery
-types-click==0.1.12
-clickhouse-sqlalchemy>=0.1.8
-redash-toolbelt
-types-freezegun
-flake8>=3.8.3
+parse>=1.19.0
+sql-metadata==2.2.2
 fastavro>=1.2.0
-twine
-avro<1.11,>=1.10.2
-acryl-iceberg-legacy==0.0.4
+packaging
+types-ujson>=5.2.0
+boto3-stubs[glue,s3,sagemaker,sts]
+lark[regex]==1.1.4
+jsonpickle
+psutil>=5.8.0
+pyspark==3.0.3
+acryl-pyhive[hive]>=0.6.12
+Deprecated
+cached_property
+typing-inspect
+simple-salesforce
+redash-toolbelt
+more-itertools>=8.12.0
+confluent_kafka>=1.5.0
+pyarrow>=6.0.1
+snowflake-connector-python!=2.8.2
+lkml>=1.3.0b5
+types-pyOpenSSL
+moto[s3]
+pytest-cov>=2.8.1
+click-default-group
+ratelimiter
+greenlet
+mixpanel>=4.9.0
+docker
+acryl-pyhive[hive]>=0.6.13
 flask-openid>=1.3.0
+expandvars>=0.6.5
+stackprinter>=0.2.6
+google-cloud-logging<3.1.2
+types-python-dateutil
+python-dateutil>=2.8.0
+types-pkg_resources
+elasticsearch==7.13.4
+mypy==0.991
+sqlparse
+avro-gen3==0.7.8
 humanfriendly
+flake8-tidy-imports>=4.3.0
+pytest-asyncio>=0.16.0
+vertica-sqlalchemy-dialect[vertica-python]==0.0.1
+tabulate
+build
+requests_ntlm
+freezegun
+pandas
 ujson>=5.2.0
-isort>=5.7.0
-sqlalchemy-redshift
-google-api-python-client
-pyspark==3.0.3
-packaging
-boto3
-sqlalchemy-bigquery>=1.4.1
-stackprinter>=0.2.6
-click-spinner
-acryl-pyhive[hive]>=0.6.12
+acryl-datahub-classify>=0.0.4
+black==22.12.0
 looker-sdk==22.2.1
-avro-gen3==0.7.8
-sql-metadata
-click>=7.1.2
-mypy==0.991
 deltalake!=0.6.4,>=0.6.3
-mypy_extensions>=0.4.3
-requests_file
-sqlparse
-tableauserverclient>=0.17.0
-psutil>=5.8.0
+cryptography
 okta~=1.7.0
-google-cloud-logging<3.1.2
-python-dateutil>=2.8.0
-flake8-tidy-imports>=4.3.0
+python-ldap>=2.4
+mypy_extensions>=0.4.3
+pytest>=6.2.2
+psycopg2-binary
+isort>=5.7.0
 pytest-docker>=1.0.1
-lkml>=1.3.0b5
-requests
-types-pkg_resources
-PyYAML
-types-tabulate
 sqllineage==1.3.6
-grpcio-tools<2,>=1.44.0
+types-protobuf>=4.21.0.1
+scipy>=1.7.2
+tableschema>=1.20.2
+azure-identity==1.10.0
+google-cloud-bigquery
+databricks-dbapi
+types-PyYAML
+sqlalchemy-bigquery>=1.4.1
+avro<1.11,>=1.10.2
+pydantic>=1.9.0
+requests-mock
+requests
+entrypoints
+types-click==0.1.12
+requests_file
 msal==1.16.0
-moto[s3]
-acryl-datahub-classify>=0.0.4
-types-toml
-types-ujson>=5.2.0
 GeoAlchemy2
-types-python-dateutil
-pytest>=6.2.2
-pandas
-databricks-cli==0.17.3
-lark[regex]==1.1.4
-deepdiff
-botocore!=1.23.0
-psycopg2-binary
-scipy>=1.7.2
-freezegun
-tabulate
+flake8>=3.8.3
+networkx>=2.6.2
+PyYAML
+trino[sqlalchemy]!=0.317,>=0.308
 termcolor>=1.0.0
-requests_ntlm
-pymysql>=1.0.2
-grpcio<2,>=1.44.0
-apache-airflow[snowflake]>=2.0.2
-jsonpickle
+types-pytz
+clickhouse-sqlalchemy>=0.1.8
+wcmatch
 types-Deprecated
-GitPython>2
-pydantic>=1.9.0
-snowflake-connector-python!=2.8.2
-SQLAlchemy<1.4.42
-cx_Oracle
-networkx>=2.6.2
-types-PyYAML
 virtualenv
-entrypoints
-types-dataclasses
-sqlalchemy<2,>=1.3.24
-boto3-stubs[glue,s3,sagemaker,sts]
-pydruid>=0.6.2
-aiohttp<4
-smart-open[s3]>=5.2.1
-expandvars>=0.6.5
-sqlalchemy-vertica-dialect[vertica-python]==0.1.4
-parse>=1.19.0
-docker
 ijson
-elasticsearch==7.13.4
-confluent_kafka>=1.5.0
-progressbar2
+types-click-spinner>=0.1.13.1
+smart-open[s3]>=5.2.1
+boto3
+apache-airflow[snowflake]>=2.0.2
+pydruid>=0.6.2
+sqlalchemy<2,>=1.3.24
 
 [dev:platform_system != "Darwin" and (platform_machine == "aarch64" or platform_machine == "arm64")]
 confluent_kafka<1.9.0
 
 [dev:python_version < "3.8"]
 typing_extensions>=3.7.4.3
 
 [dev:python_version >= "3.8"]
 typing_extensions>=3.10.0.2
 
 [druid]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-pydruid>=0.6.2
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+pydruid>=0.6.2
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [elasticsearch]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+elasticsearch==7.13.4
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-elasticsearch==7.13.4
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [feast]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
-feast~=0.26.0
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
 flask-openid>=1.3.0
-humanfriendly
+expandvars>=0.6.5
+feast~=0.26.0
+stackprinter>=0.2.6
 click>=7.1.2
+ijson
 entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [glue]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 botocore!=1.23.0
-humanfriendly
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
+ijson
 entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
 boto3
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [great-expectations]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
-scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
 sqllineage==1.3.6
-requests_file
-click-default-group
-termcolor>=1.0.0
+ijson
+entrypoints
+scipy>=1.7.2
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [hana]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [hana:platform_machine != "aarch64" and platform_machine != "arm64"]
 sqlalchemy-hana>=0.5.0
 hdbcli>=2.11.20
 
 [hive]
-python-dateutil>=2.8.0
-great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
+click-default-group
+ratelimiter
+databricks-dbapi
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
 acryl-pyhive[hive]>=0.6.13
-greenlet
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 sqlalchemy<2,>=1.3.24
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-databricks-dbapi
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [iceberg]
-python-dateutil>=2.8.0
-azure-identity==1.10.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 acryl-iceberg-legacy==0.0.4
-humanfriendly
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
+ijson
 entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+requests_file
+tabulate
+python-dateutil>=2.8.0
+azure-identity==1.10.0
 
 [integration-tests]
-great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
-botocore!=1.23.0
-sql-metadata
-pymongo[srv]>=3.11
-tableschema>=1.20.2
-scipy>=1.7.2
+PyAthena[sqlalchemy]==2.4.1
 sqlalchemy-pytds>=0.3
-deltalake!=0.6.4,>=0.6.3
-clickhouse-sqlalchemy>=0.1.8
-JPype1
-redash-toolbelt
-great-expectations<=0.15.41,>=0.15.12
-pymysql>=1.0.2
 databricks-dbapi
-pyarrow>=6.0.1
-PyAthena[sqlalchemy]==2.4.1
-wcmatch
-azure-identity==1.10.0
-pydeequ>=1.0.1
+pyspark==3.0.3
 traitlets<5.2.2
-acryl-iceberg-legacy==0.0.4
-ujson>=5.2.0
-acryl-pyhive[hive]>=0.6.13
-sqlalchemy<2,>=1.3.24
+pymysql>=1.0.2
+sql-metadata
+botocore!=1.23.0
+pydeequ>=1.0.1
+redash-toolbelt
 requests
-greenlet
+vertica-sqlalchemy-dialect[vertica-python]==0.0.1
+pyarrow>=6.0.1
+gql>=3.3.0
+JPype1
+great-expectations<=0.15.41,>=0.15.12
 gql[requests]>=3.3.0
-pydruid>=0.6.2
-smart-open[s3]>=5.2.1
-sqllineage==1.3.6
-python-ldap>=2.4
 moto[s3]
-pyspark==3.0.3
+great-expectations!=0.15.23,!=0.15.24,!=0.15.25,!=0.15.26
+pymongo[srv]>=3.11
+ujson>=5.2.0
+greenlet
+acryl-iceberg-legacy==0.0.4
+deltalake!=0.6.4,>=0.6.3
+acryl-pyhive[hive]>=0.6.13
+clickhouse-sqlalchemy>=0.1.8
+wcmatch
+python-ldap>=2.4
+sqllineage==1.3.6
 parse>=1.19.0
-gql>=3.3.0
-packaging
-sqlalchemy-vertica-dialect[vertica-python]==0.1.4
+scipy>=1.7.2
+tableschema>=1.20.2
 boto3
+smart-open[s3]>=5.2.1
+pydruid>=0.6.2
+packaging
+sqlalchemy<2,>=1.3.24
+azure-identity==1.10.0
 
 [integration-tests:platform_machine != "aarch64" and platform_machine != "arm64"]
-sqlalchemy-hana>=0.5.0
 hdbcli>=2.11.20
+sqlalchemy-hana>=0.5.0
 
 [kafka]
-fastavro>=1.2.0
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
-networkx>=2.6.2
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+networkx>=2.6.2
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
 expandvars>=0.6.5
 grpcio-tools<2,>=1.44.0
-requests_file
-click-default-group
-termcolor>=1.0.0
-packaging
+stackprinter>=0.2.6
+confluent_kafka>=1.5.0
+click>=7.1.2
 grpcio<2,>=1.44.0
-psutil>=5.8.0
-docker
 ijson
-confluent_kafka>=1.5.0
-progressbar2
-ratelimiter
+fastavro>=1.2.0
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [kafka-connect]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
-requests
-greenlet
 sqlalchemy<2,>=1.3.24
+requests
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
-JPype1
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
+JPype1
 
 [kafka:platform_system != "Darwin" and (platform_machine == "aarch64" or platform_machine == "arm64")]
 confluent_kafka<1.9.0
 
 [ldap]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-python-ldap>=2.4
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+python-ldap>=2.4
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [looker]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
-looker-sdk==22.2.1
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
-lkml>=1.3.0b5
 humanfriendly
-click>=7.1.2
-sql-metadata==2.2.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-sqllineage==1.3.6
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
+looker-sdk==22.2.1
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+sqllineage==1.3.6
 ijson
+entrypoints
+sql-metadata==2.2.2
+lkml>=1.3.0b5
+packaging
 GitPython>2
-progressbar2
-ratelimiter
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [lookml]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
-looker-sdk==22.2.1
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
-lkml>=1.3.0b5
 humanfriendly
-click>=7.1.2
-sql-metadata==2.2.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-sqllineage==1.3.6
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
+looker-sdk==22.2.1
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+sqllineage==1.3.6
 ijson
+entrypoints
+sql-metadata==2.2.2
+lkml>=1.3.0b5
+packaging
 GitPython>2
-progressbar2
-ratelimiter
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [mariadb]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+pymysql>=1.0.2
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-pymysql>=1.0.2
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [metabase]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-sqllineage==1.3.6
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+sqllineage==1.3.6
+requests
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [mode]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-tenacity>=8.0.1
-sqllineage==1.3.6
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
+tenacity>=8.0.1
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+sqllineage==1.3.6
+requests
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [mongodb]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
-avro-gen3==0.7.8
-toml>=0.10.0
-avro<1.11,>=1.10.2
-humanfriendly
-click>=7.1.2
 pymongo[srv]>=3.11
-entrypoints
-Deprecated
+click-default-group
+ratelimiter
+psutil>=5.8.0
 PyYAML
+Deprecated
 cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro-gen3==0.7.8
+toml>=0.10.0
+humanfriendly
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [mssql]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+sqlalchemy-pytds>=0.3
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-sqlalchemy-pytds>=0.3
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [mssql-odbc]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+pyodbc
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-pyodbc
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [mysql]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+pymysql>=1.0.2
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-pymysql>=1.0.2
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [nifi]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+requests
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [okta]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-okta~=1.7.0
-psutil>=5.8.0
+progressbar2
 docker
+okta~=1.7.0
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [oracle]
-python-dateutil>=2.8.0
-cx_Oracle
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+cx_Oracle
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [postgres]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 psycopg2-binary
-greenlet
+click>=7.1.2
 sqlalchemy<2,>=1.3.24
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
+python-dateutil>=2.8.0
 GeoAlchemy2
-progressbar2
-ratelimiter
 
 [powerbi]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+sqlparse
+lark[regex]==1.1.4
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
-lark[regex]==1.1.4
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
+ijson
 entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
+packaging
 msal==1.16.0
 requests_file
-click-default-group
-termcolor>=1.0.0
-packaging
-sqlparse
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+tabulate
+python-dateutil>=2.8.0
 
 [powerbi-report-server]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
+ijson
+entrypoints
 packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 requests_ntlm
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
 
 [presto]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
-click-spinner
 acryl-pyhive[hive]>=0.6.12
+aiohttp<4
+click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
-trino[sqlalchemy]!=0.317,>=0.308
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+trino[sqlalchemy]!=0.317,>=0.308
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [presto-on-hive]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
-click-spinner
 acryl-pyhive[hive]>=0.6.12
+aiohttp<4
+click-spinner
+click-default-group
+ratelimiter
+pymysql>=1.0.2
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 psycopg2-binary
-greenlet
+click>=7.1.2
 sqlalchemy<2,>=1.3.24
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-pymysql>=1.0.2
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [pulsar]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+requests
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [redash]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 sql-metadata
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
+docker
 expandvars>=0.6.5
-sqllineage==1.3.6
-requests_file
-click-default-group
-termcolor>=1.0.0
-packaging
 redash-toolbelt
-psutil>=5.8.0
-docker
+stackprinter>=0.2.6
+click>=7.1.2
+sqllineage==1.3.6
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [redshift]
-python-dateutil>=2.8.0
-wcmatch
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+sqlalchemy-redshift
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-sqlalchemy-redshift
-entrypoints
-Deprecated
-psycopg2-binary
-sqlalchemy<2,>=1.3.24
-scipy>=1.7.2
-greenlet
-PyYAML
-cached_property
-aiohttp<4
-tabulate
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
 expandvars>=0.6.5
+wcmatch
+stackprinter>=0.2.6
+psycopg2-binary
+click>=7.1.2
 sqllineage==1.3.6
-requests_file
-click-default-group
+sqlalchemy<2,>=1.3.24
+ijson
+entrypoints
 parse>=1.19.0
-termcolor>=1.0.0
+scipy>=1.7.2
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
+python-dateutil>=2.8.0
 GeoAlchemy2
-progressbar2
-ratelimiter
 
 [redshift-usage]
-python-dateutil>=2.8.0
-wcmatch
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+sqlalchemy-redshift
+sqlparse
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-sqlalchemy-redshift
-entrypoints
-Deprecated
-psycopg2-binary
-sqlalchemy<2,>=1.3.24
-scipy>=1.7.2
-greenlet
-PyYAML
-cached_property
-aiohttp<4
-tabulate
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
 expandvars>=0.6.5
+wcmatch
+stackprinter>=0.2.6
+psycopg2-binary
+click>=7.1.2
 sqllineage==1.3.6
-requests_file
-click-default-group
+sqlalchemy<2,>=1.3.24
+ijson
+entrypoints
 parse>=1.19.0
-termcolor>=1.0.0
+scipy>=1.7.2
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-sqlparse
-psutil>=5.8.0
-docker
-ijson
+python-dateutil>=2.8.0
 GeoAlchemy2
-progressbar2
-ratelimiter
 
 [s3]
-python-dateutil>=2.8.0
-wcmatch
-stackprinter>=0.2.6
-pydeequ>=1.0.1
+aiohttp<4
+moto[s3]
+boto3
 click-spinner
+ujson>=5.2.0
+click-default-group
+ratelimiter
+psutil>=5.8.0
+pyspark==3.0.3
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 botocore!=1.23.0
-humanfriendly
+docker
+pydeequ>=1.0.1
+expandvars>=0.6.5
+wcmatch
+stackprinter>=0.2.6
 click>=7.1.2
-ujson>=5.2.0
+ijson
 entrypoints
-Deprecated
-tableschema>=1.20.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-smart-open[s3]>=5.2.1
-requests_file
-click-default-group
-moto[s3]
-termcolor>=1.0.0
-packaging
 parse>=1.19.0
-pyspark==3.0.3
-boto3
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
 pyarrow>=6.0.1
+packaging
+tableschema>=1.20.2
+requests_file
+smart-open[s3]>=5.2.1
+tabulate
+python-dateutil>=2.8.0
 
 [sagemaker]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
 botocore!=1.23.0
-humanfriendly
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
+ijson
 entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
 boto3
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [salesforce]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
-simple-salesforce
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
-docker
-ijson
 progressbar2
-ratelimiter
-
-[snowflake]
+simple-salesforce
+docker
+expandvars>=0.6.5
 stackprinter>=0.2.6
-click-spinner
-pandas
-msal
-avro-gen3==0.7.8
-toml>=0.10.0
-cryptography
 click>=7.1.2
-scipy>=1.7.2
-cached_property
-tabulate
+ijson
+entrypoints
+packaging
 requests_file
-termcolor>=1.0.0
-great-expectations<=0.15.41,>=0.15.12
-sqlparse
-psutil>=5.8.0
-snowflake-connector-python!=2.8.2
-SQLAlchemy<1.4.42
+tabulate
 python-dateutil>=2.8.0
+
+[snowflake]
 spacy==3.4.3
-snowflake-sqlalchemy!=1.2.5,>=1.2.4
+sqlparse
+psutil>=5.8.0
 traitlets<5.2.2
-avro<1.11,>=1.10.2
-humanfriendly
-entrypoints
 Deprecated
+cached_property
+avro-gen3==0.7.8
+humanfriendly
+avro<1.11,>=1.10.2
+snowflake-sqlalchemy!=1.2.5,>=1.2.4
+SQLAlchemy<1.4.42
+click>=7.1.2
 sqlalchemy<2,>=1.3.24
-greenlet
-PyYAML
+entrypoints
+requests_file
+snowflake-connector-python!=2.8.2
+tabulate
+great-expectations<=0.15.41,>=0.15.12
 aiohttp<4
-expandvars>=0.6.5
-click-default-group
-acryl-datahub-classify>=0.0.4
-packaging
-docker
-ijson
-progressbar2
-ratelimiter
-
-[snowflake-beta]
-stackprinter>=0.2.6
 click-spinner
 pandas
+acryl-datahub-classify>=0.0.4
+click-default-group
+ratelimiter
+PyYAML
+greenlet
 msal
-avro-gen3==0.7.8
 toml>=0.10.0
+termcolor>=1.0.0
+progressbar2
 cryptography
-click>=7.1.2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+ijson
 scipy>=1.7.2
-cached_property
-tabulate
-requests_file
-termcolor>=1.0.0
-great-expectations<=0.15.41,>=0.15.12
-sqlparse
-psutil>=5.8.0
-snowflake-connector-python!=2.8.2
-SQLAlchemy<1.4.42
+packaging
 python-dateutil>=2.8.0
+
+[snowflake-beta]
 spacy==3.4.3
-snowflake-sqlalchemy!=1.2.5,>=1.2.4
+sqlparse
+psutil>=5.8.0
 traitlets<5.2.2
-avro<1.11,>=1.10.2
-humanfriendly
-entrypoints
 Deprecated
+cached_property
+avro-gen3==0.7.8
+humanfriendly
+avro<1.11,>=1.10.2
+snowflake-sqlalchemy!=1.2.5,>=1.2.4
+SQLAlchemy<1.4.42
+click>=7.1.2
 sqlalchemy<2,>=1.3.24
-greenlet
-PyYAML
+entrypoints
+requests_file
+snowflake-connector-python!=2.8.2
+tabulate
+great-expectations<=0.15.41,>=0.15.12
 aiohttp<4
-expandvars>=0.6.5
-click-default-group
+click-spinner
+pandas
 acryl-datahub-classify>=0.0.4
-packaging
+click-default-group
+ratelimiter
+PyYAML
+greenlet
+msal
+toml>=0.10.0
+termcolor>=1.0.0
+progressbar2
+cryptography
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 ijson
-progressbar2
-ratelimiter
+scipy>=1.7.2
+packaging
+python-dateutil>=2.8.0
 
 [sqlalchemy]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [starburst-trino-usage]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+sqlparse
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
-trino[sqlalchemy]!=0.317,>=0.308
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+trino[sqlalchemy]!=0.317,>=0.308
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-sqlparse
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [superset]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
+great_expectations
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
+humanfriendly
 avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
 sqlalchemy
-humanfriendly
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 requests
-great_expectations
-greenlet
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
-packaging
-psutil>=5.8.0
-docker
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [tableau]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-tableauserverclient>=0.17.0
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
 ijson
-progressbar2
-ratelimiter
+entrypoints
+tableauserverclient>=0.17.0
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [trino]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
-trino[sqlalchemy]!=0.317,>=0.308
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+trino[sqlalchemy]!=0.317,>=0.308
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
 
 [unity-catalog]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
-databricks-cli==0.17.3
+click-default-group
+ratelimiter
+psutil>=5.8.0
+PyYAML
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
-click>=7.1.2
-entrypoints
-Deprecated
-requests
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
+avro<1.11,>=1.10.2
 termcolor>=1.0.0
-packaging
-psutil>=5.8.0
+progressbar2
 docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
+click>=7.1.2
+databricks-cli==0.17.3
+requests
 ijson
-progressbar2
-ratelimiter
+entrypoints
+packaging
+requests_file
+tabulate
+python-dateutil>=2.8.0
 
 [vertica]
-python-dateutil>=2.8.0
-stackprinter>=0.2.6
+aiohttp<4
 click-spinner
+click-default-group
+ratelimiter
+psutil>=5.8.0
 traitlets<5.2.2
+PyYAML
+greenlet
+Deprecated
+cached_property
 avro-gen3==0.7.8
 toml>=0.10.0
-avro<1.11,>=1.10.2
 humanfriendly
+avro<1.11,>=1.10.2
+termcolor>=1.0.0
+progressbar2
+docker
+expandvars>=0.6.5
+stackprinter>=0.2.6
 click>=7.1.2
-entrypoints
-Deprecated
 sqlalchemy<2,>=1.3.24
-greenlet
+ijson
+vertica-sqlalchemy-dialect[vertica-python]==0.0.1
+entrypoints
 scipy>=1.7.2
-PyYAML
-cached_property
-aiohttp<4
-tabulate
-expandvars>=0.6.5
-requests_file
-click-default-group
-sqlalchemy-vertica-dialect[vertica-python]==0.1.4
-termcolor>=1.0.0
 packaging
+requests_file
+tabulate
 great-expectations<=0.15.41,>=0.15.12
-psutil>=5.8.0
-docker
-ijson
-progressbar2
-ratelimiter
+python-dateutil>=2.8.0
```

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import sys
 import warnings
 
 # Published at https://pypi.org/project/acryl-datahub/.
 __package_name__ = "acryl-datahub"
-__version__ = "0.9.6rc0"
+__version__ = "0.9.6rc1"
 
 
 def is_dev_mode() -> bool:
     return __version__.endswith("dev0")
 
 
 def nice_version_name() -> str:
```

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/assertion_circuit_breaker.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/assertion_circuit_breaker.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/circuit_breaker.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/circuit_breaker.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/circuit_breaker/operation_circuit_breaker.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/circuit_breaker/operation_circuit_breaker.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpgroup/corpgroup.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpgroup/corpgroup.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/entities/corpuser/corpuser.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/entities/corpuser/corpuser.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/entities/datajob/dataflow.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/entities/datajob/dataflow.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/entities/datajob/datajob.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/entities/datajob/datajob.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/entities/dataprocess/dataprocess_instance.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/entities/dataprocess/dataprocess_instance.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/graphql/assertion.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/graphql/assertion.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/graphql/base.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/graphql/base.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/api/graphql/operation.py` & `acryl-datahub-0.9.6rc1/src/datahub/api/graphql/operation.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/check_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/check_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/cli_utils.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/cli_utils.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/delete_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/delete_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/docker_check.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/docker_check.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/docker_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/docker_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/get_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/get_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/ingest_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/ingest_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/json_file.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/json_file.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/migrate.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/migrate.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/migration_utils.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/migration_utils.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/put_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/put_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/state_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/state_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/cli/timeline_cli.py` & `acryl-datahub-0.9.6rc1/src/datahub/cli/timeline_cli.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/_config_enum.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/_config_enum.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/common.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/config_loader.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/config_loader.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/github.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/github.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/kafka.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/kafka.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/pydantic_field_deprecation.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/pydantic_field_deprecation.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/source_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/source_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/time_window_config.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/time_window_config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/validate_field_removal.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/validate_field_removal.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/validate_field_rename.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/validate_field_rename.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/configuration/validate_host_port.py` & `acryl-datahub-0.9.6rc1/src/datahub/configuration/validate_host_port.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/kafka_emitter.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/kafka_emitter.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/mce_builder.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/mce_builder.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/mcp.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/mcp.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/mcp_builder.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/mcp_builder.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,14 +17,15 @@
     DataPlatformInstance,
     TimeStamp,
 )
 from datahub.metadata.com.linkedin.pegasus2avro.container import ContainerProperties
 from datahub.metadata.schema_classes import (
     ContainerClass,
     DomainsClass,
+    EmbedClass,
     GlobalTagsClass,
     MetadataChangeEventClass,
     OwnerClass,
     OwnershipClass,
     OwnershipTypeClass,
     StatusClass,
     SubTypesClass,
@@ -305,7 +306,14 @@
     for aspect in mce.proposedSnapshot.aspects:
         yield MetadataChangeProposalWrapper(
             entityUrn=mce.proposedSnapshot.urn,
             auditHeader=mce.auditHeader,
             aspect=aspect,
             systemMetadata=mce.systemMetadata,
         )
+
+
+def create_embed_mcp(urn: str, embed_url: str) -> MetadataChangeProposalWrapper:
+    return MetadataChangeProposalWrapper(
+        entityUrn=urn,
+        aspect=EmbedClass(renderUrl=embed_url),
+    )
```

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/mcp_patch_builder.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/mcp_patch_builder.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/request_helper.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/request_helper.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/rest_emitter.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/rest_emitter.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/emitter/serialization_helper.py` & `acryl-datahub-0.9.6rc1/src/datahub/emitter/serialization_helper.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/entrypoints.py` & `acryl-datahub-0.9.6rc1/src/datahub/entrypoints.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/committable.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/committable.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/decorators.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/decorators.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/ingestion_job_checkpointing_provider_base.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/ingestion_job_checkpointing_provider_base.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/pipeline_run_listener.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/pipeline_run_listener.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/registry.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/registry.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/report.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/report.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/sink.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/sink.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/source.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/source.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/transform.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/transform.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/api/workunit.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/api/workunit.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/mce_extractor.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/mce_extractor.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/protobuf_util.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/protobuf_util.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/extractor/schema_util.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/extractor/schema_util.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/classification_mixin.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/classification_mixin.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/classifier.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/classifier.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/glossary/datahub_classifier.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/glossary/datahub_classifier.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/graph/client.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/graph/client.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/reporting/datahub_ingestion_run_summary_provider.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/reporting/datahub_ingestion_run_summary_provider.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/reporting/file_reporter.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/reporting/file_reporter.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/connection.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/connection.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/pipeline.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/pipeline.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/run/pipeline_config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/run/pipeline_config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/console.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/console.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/datahub_kafka.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/datahub_kafka.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/datahub_rest.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/datahub_rest.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/file.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/file.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/sink/sink_registry.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/sink/sink_registry.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/aws_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/aws_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/glue.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/glue.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/path_spec.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/path_spec.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/s3_boto_utils.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/s3_boto_utils.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/s3_util.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/s3_util.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/feature_groups.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/feature_groups.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/job_classes.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/job_classes.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/jobs.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/jobs.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/lineage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/lineage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/aws/sagemaker_processors/models.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/aws/sagemaker_processors/models.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/azure/azure_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/azure/azure_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_audit.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_audit.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_report.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_report.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/bigquery_schema.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/bigquery_schema.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/lineage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/lineage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/profiler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/profiler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/bigquery_v2/usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/bigquery_v2/usage.py`

 * *Files 1% similar despite different names*

```diff
@@ -433,15 +433,15 @@
             return event.query_event.destinationTable.get_sanitized_table_ref()
         elif event.read_event:
             return event.read_event.resource.get_sanitized_table_ref()
         else:
             # TODO: CREATE_SCHEMA operation ends up here, maybe we should capture that as well
             # but it is tricky as we only get the query so it can't be tied to anything
             # - SCRIPT statement type ends up here as well
-            logger.warning(f"Unable to find destination table in event {event}")
+            logger.debug(f"Unable to find destination table in event {event}")
             return None
 
     def _extract_operational_meta(
         self, event: AuditEvent
     ) -> Optional[OperationalDataMeta]:
         # If we don't have Query object that means this is a queryless read operation or a read operation which was not executed as JOB
         # https://cloud.google.com/bigquery/docs/reference/auditlogs/rest/Shared.Types/BigQueryAuditMetadata.TableDataRead.Reason/
@@ -730,17 +730,16 @@
             # https://cloud.google.com/bigquery/docs/reference/auditlogs/rest/Shared.Types/BigQueryAuditMetadata.TableDataRead.Reason
             if event.read_event.jobName:
                 if event.read_event.jobName in query_jobs:
                     # Join the query log event into the table read log event.
                     num_joined += 1
                     event.query_event = query_jobs[event.read_event.jobName]
                 else:
-                    self.report.report_warning(
-                        str(event.read_event.resource),
-                        f"Failed to match table read event {event.read_event.jobName} with reason {event.read_event.readReason} with job at {event.read_event.timestamp}; try increasing `query_log_delay` or `max_query_duration`",
+                    logger.debug(
+                        f"Failed to match table read event {event.read_event.jobName} with reason {event.read_event.readReason} with job at {event.read_event.timestamp}; try increasing `query_log_delay` or `max_query_duration`"
                     )
             yield event
         logger.info(f"Number of read events joined with query events: {num_joined}")
 
     def _aggregate_enriched_read_events(
         self,
         datasets: Dict[datetime, Dict[BigQueryTableRef, AggregatedDataset]],
```

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/confluent_schema_registry.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/confluent_schema_registry.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/csv_enricher.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/csv_enricher.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/dbt_cloud.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/dbt_cloud.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/dbt_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/dbt_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/dbt/dbt_core.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/dbt/dbt_core.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/delta_lake_utils.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/delta_lake_utils.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/delta_lake/source.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/delta_lake/source.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/demo_data.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/demo_data.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/elastic_search.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/elastic_search.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/feast.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/feast.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/file.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/file.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/ge_data_profiler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/ge_data_profiler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/ge_profiling_config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/ge_profiling_config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/git/git_import.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/git/git_import.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/glue_profiling_config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/glue_profiling_config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/iceberg.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/iceberg.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/iceberg_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/iceberg_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/iceberg/iceberg_profiler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/iceberg/iceberg_profiler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/identity/azure_ad.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/identity/azure_ad.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/identity/okta.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/identity/okta.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/kafka.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/kafka.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/kafka_connect.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/kafka_connect.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/ldap.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/ldap.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_common.py`

 * *Files 2% similar despite different names*

```diff
@@ -26,14 +26,15 @@
 from pydantic.class_validators import validator
 
 import datahub.emitter.mce_builder as builder
 from datahub.configuration import ConfigModel
 from datahub.configuration.common import ConfigurationError
 from datahub.configuration.source_common import DatasetSourceConfigBase
 from datahub.emitter.mcp import MetadataChangeProposalWrapper
+from datahub.emitter.mcp_builder import create_embed_mcp
 from datahub.ingestion.api.report import Report
 from datahub.ingestion.api.source import SourceReport
 from datahub.ingestion.source.looker.looker_lib_wrapper import LookerAPI
 from datahub.ingestion.source.sql.sql_types import (
     POSTGRES_TYPES_MAP,
     SNOWFLAKE_TYPES_MAP,
     resolve_postgres_modified_type,
@@ -78,14 +79,15 @@
     StatusClass,
     SubTypesClass,
     TagAssociationClass,
     TagPropertiesClass,
     TagSnapshotClass,
 )
 from datahub.utilities.lossy_collections import LossyList, LossySet
+from datahub.utilities.url_util import remove_port_from_url
 
 if TYPE_CHECKING:
     from datahub.ingestion.source.looker.lookml_source import (
         LookerViewFileLoader,
         LookMLSourceReport,
     )
 
@@ -159,29 +161,26 @@
 
 
 class LookerCommonConfig(DatasetSourceConfigBase):
     explore_naming_pattern: LookerNamingPattern = pydantic.Field(
         description=f"Pattern for providing dataset names to explores. {LookerNamingPattern.allowed_docstring()}",
         default=LookerNamingPattern(pattern="{model}.explore.{name}"),
     )
-
     explore_browse_pattern: LookerNamingPattern = pydantic.Field(
         description=f"Pattern for providing browse paths to explores. {LookerNamingPattern.allowed_docstring()}",
         default=LookerNamingPattern(pattern="/{env}/{platform}/{project}/explores"),
     )
-
     view_naming_pattern: LookerNamingPattern = Field(
         LookerNamingPattern(pattern="{project}.view.{name}"),
         description=f"Pattern for providing dataset names to views. {LookerNamingPattern.allowed_docstring()}",
     )
     view_browse_pattern: LookerNamingPattern = Field(
         LookerNamingPattern(pattern="/{env}/{platform}/{project}/views"),
         description=f"Pattern for providing browse paths to views. {LookerNamingPattern.allowed_docstring()}",
     )
-
     tag_measures_and_dimensions: bool = Field(
         True,
         description="When enabled, attaches tags to measures, dimensions and dimension groups to make them more discoverable. When disabled, adds this information to the description of the column.",
     )
     platform_name: str = Field(
         "looker", description="Default platform name. Don't change."
     )
@@ -752,22 +751,27 @@
     def get_explore_browse_path(self, config: LookerCommonConfig) -> str:
         browse_path = config.explore_browse_pattern.replace_variables(
             self.get_mapping(config)
         )
         return browse_path
 
     def _get_url(self, base_url):
-        # If the base_url contains a port number (like https://company.looker.com:19999) remove the port number
-        m = re.match("^(.*):([0-9]+)$", base_url)
-        if m is not None:
-            base_url = m[1]
+        base_url = remove_port_from_url(base_url)
         return f"{base_url}/explore/{self.model_name}/{self.name}"
 
+    def _get_embed_url(self, base_url: str) -> str:
+        base_url = remove_port_from_url(base_url)
+        return f"{base_url}/embed/explore/{self.model_name}/{self.name}"
+
     def _to_metadata_events(  # noqa: C901
-        self, config: LookerCommonConfig, reporter: SourceReport, base_url: str
+        self,
+        config: LookerCommonConfig,
+        reporter: SourceReport,
+        base_url: str,
+        extract_embed_urls: bool,
     ) -> Optional[List[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]]]:
         # We only generate MCE-s for explores that contain from clauses and do NOT contain joins
         # All other explores (passthrough explores and joins) end in correct resolution of lineage, and don't need additional nodes in the graph.
         from datahub.ingestion.source.looker.lookml_source import _BASE_PROJECT_NAME
 
         dataset_snapshot = DatasetSnapshot(
             urn=self.get_explore_urn(config),
@@ -858,15 +862,27 @@
             entityType="dataset",
             changeType=ChangeTypeClass.UPSERT,
             entityUrn=dataset_snapshot.urn,
             aspectName="subTypes",
             aspect=SubTypesClass(typeNames=["explore"]),
         )
 
-        return [mce, mcp]
+        proposals: List[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]] = [
+            mce,
+            mcp,
+        ]
+
+        # If extracting embeds is enabled, produce an MCP for embed URL.
+        if extract_embed_urls:
+            embed_mcp = create_embed_mcp(
+                dataset_snapshot.urn, self._get_embed_url(base_url)
+            )
+            proposals.append(embed_mcp)
+
+        return proposals
 
 
 class LookerExploreRegistry:
     """A LRU caching registry of Looker Explores"""
 
     def __init__(
         self,
@@ -1044,23 +1060,29 @@
     look_id: Optional[str]
     type: Optional[str] = None
     description: Optional[str] = None
     input_fields: Optional[List[InputFieldElement]] = None
 
     def url(self, base_url: str) -> str:
         # A dashboard element can use a look or just a raw query against an explore
-        # If the base_url contains a port number (like https://company.looker.com:19999) remove the port number
-        m = re.match("^(.*):([0-9]+)$", base_url)
-        if m is not None:
-            base_url = m[1]
+        base_url = remove_port_from_url(base_url)
         if self.look_id is not None:
             return f"{base_url}/looks/{self.look_id}"
         else:
             return f"{base_url}/x/{self.query_slug}"
 
+    def embed_url(self, base_url: str) -> Optional[str]:
+        # A dashboard element can use a look or just a raw query against an explore
+        base_url = remove_port_from_url(base_url)
+        if self.look_id is not None:
+            return f"{base_url}/embed/looks/{self.look_id}"
+        else:
+            # No embeddable URL
+            return None
+
     def get_urn_element_id(self):
         # A dashboard element can use a look or just a raw query against an explore
         return f"dashboard_elements.{self.id}"
 
     def get_view_urns(self, config: LookerCommonConfig) -> List[str]:
         return [v.get_explore_urn(config) for v in self.upstream_explores]
 
@@ -1091,20 +1113,21 @@
     deleted_at: Optional[datetime.datetime] = None
     deleted_by: Optional[LookerUser] = None
     favorite_count: Optional[int] = None
     view_count: Optional[int] = None
     last_viewed_at: Optional[datetime.datetime] = None
 
     def url(self, base_url):
-        # If the base_url contains a port number (like https://company.looker.com:19999) remove the port number
-        m = re.match("^(.*):([0-9]+)$", base_url)
-        if m is not None:
-            base_url = m[1]
+        base_url = remove_port_from_url(base_url)
         return f"{base_url}/dashboards/{self.id}"
 
+    def embed_url(self, base_url: str) -> str:
+        base_url = remove_port_from_url(base_url)
+        return f"{base_url}/embed/dashboards/{self.id}"
+
     def get_urn_dashboard_id(self):
         return get_urn_looker_dashboard_id(self.id)
 
 
 class LookerUserRegistry:
     looker_api_wrapper: LookerAPI
     fields: str = ",".join(["id", "email", "display_name", "first_name", "last_name"])
```

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_lib_wrapper.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_lib_wrapper.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_query_model.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_query_model.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_source.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_source.py`

 * *Files 3% similar despite different names*

```diff
@@ -22,14 +22,15 @@
 from looker_sdk.sdk.api31.models import Dashboard, DashboardElement, FolderBase, Query
 from pydantic import Field, validator
 
 import datahub.emitter.mce_builder as builder
 from datahub.configuration.common import AllowDenyPattern, ConfigurationError
 from datahub.configuration.validate_field_removal import pydantic_removed_field
 from datahub.emitter.mcp import MetadataChangeProposalWrapper
+from datahub.emitter.mcp_builder import create_embed_mcp
 from datahub.ingestion.api.common import PipelineContext
 from datahub.ingestion.api.decorators import (
     SupportStatus,
     capability,
     config_class,
     platform_name,
     support_status,
@@ -145,15 +146,18 @@
         description="Whether to ingest usage statistics for dashboards. Setting this to True will query looker system activity explores to fetch historical dashboard usage.",
     )
     # TODO - stateful ingestion to autodetect usage history interval
     extract_usage_history_for_interval: str = Field(
         "30 days",
         description="Used only if extract_usage_history is set to True. Interval to extract looker dashboard usage history for. See https://docs.looker.com/reference/filter-expressions#date_and_time.",
     )
-
+    extract_embed_urls: bool = Field(
+        True,
+        description="Produce URLs used to render Looker Explores as Previews inside of DataHub UI. Embeds must be enabled inside of Looker to use this feature.",
+    )
     stateful_ingestion: Optional[StatefulStaleMetadataRemovalConfig] = Field(
         default=None, description=""
     )
 
     @validator("external_base_url", pre=True, always=True)
     def external_url_defaults_to_api_config_base_url(
         cls, v: Optional[str], *, values: Dict[str, Any], **kwargs: Dict[str, Any]
@@ -646,17 +650,17 @@
                 key=f"looker-chart-{dashboard_element.id}",
                 reason=f"Chart type {type_str} not supported. Setting to None",
             )
             chart_type = None
 
         return chart_type
 
-    def _make_chart_mce(
+    def _make_chart_metadata_events(
         self, dashboard_element: LookerDashboardElement, dashboard: LookerDashboard
-    ) -> MetadataChangeEvent:
+    ) -> List[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]]:
         chart_urn = builder.make_chart_urn(
             self.source_config.platform_name, dashboard_element.get_urn_element_id()
         )
         chart_snapshot = ChartSnapshot(
             urn=chart_urn,
             aspects=[Status(removed=False)],
         )
@@ -680,15 +684,89 @@
 
         chart_snapshot.aspects.append(chart_info)
 
         ownership = self.get_ownership(dashboard)
         if ownership is not None:
             chart_snapshot.aspects.append(ownership)
 
-        return MetadataChangeEvent(proposedSnapshot=chart_snapshot)
+        chart_mce = MetadataChangeEvent(proposedSnapshot=chart_snapshot)
+
+        proposals: List[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]] = [
+            chart_mce
+        ]
+
+        # If extracting embeds is enabled, produce an MCP for embed URL.
+        if (
+            self.source_config.extract_embed_urls
+            and self.source_config.external_base_url
+        ):
+            maybe_embed_url = dashboard_element.embed_url(
+                self.source_config.external_base_url
+            )
+            if maybe_embed_url:
+                proposals.append(
+                    create_embed_mcp(
+                        chart_snapshot.urn,
+                        maybe_embed_url,
+                    )
+                )
+
+        return proposals
+
+    def _make_dashboard_metadata_events(
+        self, looker_dashboard: LookerDashboard, chart_urns: List[str]
+    ) -> List[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]]:
+        dashboard_urn = builder.make_dashboard_urn(
+            self.source_config.platform_name, looker_dashboard.get_urn_dashboard_id()
+        )
+        dashboard_snapshot = DashboardSnapshot(
+            urn=dashboard_urn,
+            aspects=[],
+        )
+
+        dashboard_info = DashboardInfoClass(
+            description=looker_dashboard.description or "",
+            title=looker_dashboard.title,
+            charts=chart_urns,
+            lastModified=self._get_change_audit_stamps(looker_dashboard),
+            dashboardUrl=looker_dashboard.url(self.source_config.external_base_url),
+        )
+
+        dashboard_snapshot.aspects.append(dashboard_info)
+        if looker_dashboard.folder_path is not None:
+            browse_path = BrowsePathsClass(
+                paths=[f"/looker/{looker_dashboard.folder_path}"]
+            )
+            dashboard_snapshot.aspects.append(browse_path)
+
+        ownership = self.get_ownership(looker_dashboard)
+        if ownership is not None:
+            dashboard_snapshot.aspects.append(ownership)
+
+        dashboard_snapshot.aspects.append(Status(removed=looker_dashboard.is_deleted))
+
+        dashboard_mce = MetadataChangeEvent(proposedSnapshot=dashboard_snapshot)
+
+        proposals: List[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]] = [
+            dashboard_mce
+        ]
+
+        # If extracting embeds is enabled, produce an MCP for embed URL.
+        if (
+            self.source_config.extract_embed_urls
+            and self.source_config.external_base_url
+        ):
+            proposals.append(
+                create_embed_mcp(
+                    dashboard_snapshot.urn,
+                    looker_dashboard.embed_url(self.source_config.external_base_url),
+                )
+            )
+
+        return proposals
 
     def _make_explore_metadata_events(
         self,
     ) -> Iterable[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]]:
         with concurrent.futures.ThreadPoolExecutor(
             max_workers=self.source_config.max_threads
         ) as async_executor:
@@ -722,63 +800,60 @@
     ]:
         start_time = datetime.datetime.now()
         events: List[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]] = []
         looker_explore = self.explore_registry.get_explore(model, explore)
         if looker_explore is not None:
             events = (
                 looker_explore._to_metadata_events(
-                    self.source_config, self.reporter, self.source_config.base_url
+                    self.source_config,
+                    self.reporter,
+                    self.source_config.base_url,
+                    self.source_config.extract_embed_urls,
                 )
                 or events
             )
 
         return events, f"{model}:{explore}", start_time, datetime.datetime.now()
 
+    def _extract_event_urn(
+        self, event: Union[MetadataChangeEvent, MetadataChangeProposalWrapper]
+    ) -> Optional[str]:
+        if isinstance(event, MetadataChangeEvent):
+            return event.proposedSnapshot.urn
+        else:
+            return event.entityUrn
+
     def _make_dashboard_and_chart_mces(
         self, looker_dashboard: LookerDashboard
     ) -> Iterable[Union[MetadataChangeEvent, MetadataChangeProposalWrapper]]:
-        chart_mces = [
-            self._make_chart_mce(element, looker_dashboard)
-            for element in looker_dashboard.dashboard_elements
-            if element.type == "vis"
-        ]
-        for chart_mce in chart_mces:
-            yield chart_mce
 
-        dashboard_urn = builder.make_dashboard_urn(
-            self.source_config.platform_name, looker_dashboard.get_urn_dashboard_id()
-        )
-        dashboard_snapshot = DashboardSnapshot(
-            urn=dashboard_urn,
-            aspects=[],
-        )
+        # Step 1: Emit metadata for each Chart inside the Dashboard.
+        chart_events = []
+        for element in looker_dashboard.dashboard_elements:
+            if element.type == "vis":
+                chart_events.extend(
+                    self._make_chart_metadata_events(element, looker_dashboard)
+                )
+
+        yield from chart_events
+
+        # Step 2: Emit metadata events for the Dashboard itself.
+        chart_urns: Set[
+            str
+        ] = set()  # Collect the unique child chart urns for dashboard input lineage.
+        for chart_event in chart_events:
+            chart_event_urn = self._extract_event_urn(chart_event)
+            if chart_event_urn:
+                chart_urns.add(chart_event_urn)
 
-        dashboard_info = DashboardInfoClass(
-            description=looker_dashboard.description or "",
-            title=looker_dashboard.title,
-            charts=[mce.proposedSnapshot.urn for mce in chart_mces],
-            lastModified=self._get_change_audit_stamps(looker_dashboard),
-            dashboardUrl=looker_dashboard.url(self.source_config.external_base_url),
+        dashboard_events = self._make_dashboard_metadata_events(
+            looker_dashboard, list(chart_urns)
         )
-
-        dashboard_snapshot.aspects.append(dashboard_info)
-        if looker_dashboard.folder_path is not None:
-            browse_path = BrowsePathsClass(
-                paths=[f"/looker/{looker_dashboard.folder_path}"]
-            )
-            dashboard_snapshot.aspects.append(browse_path)
-
-        ownership = self.get_ownership(looker_dashboard)
-        if ownership is not None:
-            dashboard_snapshot.aspects.append(ownership)
-
-        dashboard_snapshot.aspects.append(Status(removed=looker_dashboard.is_deleted))
-
-        dashboard_mce = MetadataChangeEvent(proposedSnapshot=dashboard_snapshot)
-        yield dashboard_mce
+        for dashboard_event in dashboard_events:
+            yield dashboard_event
 
     def get_ownership(
         self, looker_dashboard: LookerDashboard
     ) -> Optional[OwnershipClass]:
         if looker_dashboard.owner is not None:
             owner_urn = looker_dashboard.owner.get_urn(
                 self.source_config.strip_user_ids_from_email
```

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/looker_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/looker_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/looker/lookml_source.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/looker/lookml_source.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metabase.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metabase.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metadata/business_glossary.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metadata/business_glossary.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/metadata/lineage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/metadata/lineage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/mode.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/mode.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/mongodb.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/mongodb.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/nifi.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/nifi.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/openapi.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/openapi.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/openapi_parser.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/openapi_parser.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/data_classes.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/data_classes.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/native_sql_parser.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/native_sql_parser.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/parser.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/parser.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/resolver.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/resolver.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/tree_function.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/tree_function.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/m_query/validator.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/m_query/validator.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/powerbi-lexical-grammar.rule` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/powerbi-lexical-grammar.rule`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/powerbi.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/powerbi.py`

 * *Files 0% similar despite different names*

```diff
@@ -31,15 +31,14 @@
 from datahub.ingestion.source.powerbi.proxy import PowerBiAPI
 from datahub.metadata.com.linkedin.pegasus2avro.common import ChangeAuditStamps
 from datahub.metadata.schema_classes import (
     BrowsePathsClass,
     ChangeTypeClass,
     ChartInfoClass,
     ChartKeyClass,
-    CorpUserInfoClass,
     CorpUserKeyClass,
     DashboardInfoClass,
     DashboardKeyClass,
     DatasetLineageTypeClass,
     DatasetPropertiesClass,
     OwnerClass,
     OwnershipClass,
@@ -432,46 +431,24 @@
         """
 
         logger.debug(f"Mapping user {user.displayName}(id={user.id}) to datahub's user")
 
         # Create an URN for user
         user_urn = builder.make_user_urn(user.get_urn_part())
 
-        user_info_instance = CorpUserInfoClass(
-            displayName=user.displayName,
-            email=user.emailAddress,
-            title=user.displayName,
-            active=True,
-        )
-
-        info_mcp = self.new_mcp(
-            entity_type=Constant.CORP_USER,
-            entity_urn=user_urn,
-            aspect_name=Constant.CORP_USER_INFO,
-            aspect=user_info_instance,
-        )
-
-        # removed status mcp
-        status_mcp = self.new_mcp(
-            entity_type=Constant.CORP_USER,
-            entity_urn=user_urn,
-            aspect_name=Constant.STATUS,
-            aspect=StatusClass(removed=False),
-        )
-
         user_key = CorpUserKeyClass(username=user.id)
 
         user_key_mcp = self.new_mcp(
             entity_type=Constant.CORP_USER,
             entity_urn=user_urn,
             aspect_name=Constant.CORP_USER_KEY,
             aspect=user_key,
         )
 
-        return [info_mcp, status_mcp, user_key_mcp]
+        return [user_key_mcp]
 
     def to_datahub_users(
         self, users: List[PowerBiAPI.User]
     ) -> List[MetadataChangeProposalWrapper]:
         user_mcps = []
 
         for user in users:
```

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi/proxy.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi/proxy.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/constants.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/constants.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/report_server.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/report_server.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/powerbi_report_server/report_server_domain.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/powerbi_report_server/report_server_domain.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/profiling/common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/profiling/common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/pulsar.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/pulsar.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/redash.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/redash.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/data_lake_utils.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/data_lake_utils.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/profiling.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/profiling.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/s3/source.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/s3/source.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/salesforce.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/salesforce.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/avro.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/avro.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/csv_tsv.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/csv_tsv.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/json.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/json.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/object.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/object.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/schema_inference/parquet.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/schema_inference/parquet.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/constants.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/constants.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_lineage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_lineage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_profiler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_profiler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_query.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_query.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_report.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_report.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_schema.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_schema.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_tag.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_tag.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_usage_v2.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_usage_v2.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_utils.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_utils.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/snowflake/snowflake_v2.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/snowflake/snowflake_v2.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/source_registry.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/source_registry.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/athena.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/athena.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/clickhouse.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/clickhouse.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/druid.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/druid.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/hana.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/hana.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/hive.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/hive.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/mariadb.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/mariadb.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/mssql.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/mssql.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/mysql.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/mysql.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/oauth_generator.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/oauth_generator.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/oracle.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/oracle.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/postgres.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/postgres.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/presto.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/presto.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/presto_on_hive.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/presto_on_hive.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/redshift.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/redshift.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_generic.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_generic.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_generic_profiler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_generic_profiler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/sql_types.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/sql_types.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/trino.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/trino.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/two_tier_sql_source.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/two_tier_sql_source.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/sql/vertica.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/sql/vertica.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/checkpoint.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/checkpoint.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/entity_removal_state.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/entity_removal_state.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/profiling_state.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/profiling_state.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/profiling_state_handler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/profiling_state_handler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/redundant_run_skip_handler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/redundant_run_skip_handler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/stale_entity_removal_handler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/stale_entity_removal_handler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/stateful_ingestion_base.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/stateful_ingestion_base.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state/use_case_handler.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state/use_case_handler.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/state_provider/datahub_ingestion_checkpointing_provider.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/state_provider/datahub_ingestion_checkpointing_provider.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/superset.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/superset.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/tableau.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/tableau.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/tableau_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/tableau_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/config.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/config.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/proxy.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/proxy.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/report.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/report.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/unity/source.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/unity/source.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/clickhouse_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/clickhouse_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/redshift_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/redshift_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/starburst_trino_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/starburst_trino_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source/usage/usage_common.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source/usage/usage_common.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/bigquery.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/bigquery.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/csv_enricher.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/csv_enricher.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/pulsar.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/pulsar.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/sql/bigquery.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/sql/bigquery.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/sql/snowflake.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/sql/snowflake.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/usage/bigquery_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/usage/bigquery_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_config/usage/snowflake_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_config/usage/snowflake_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/pulsar.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/pulsar.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/sql/bigquery.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/sql/bigquery.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/sql/snowflake.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/sql/snowflake.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/usage/bigquery_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/usage/bigquery_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/source_report/usage/snowflake_usage.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/source_report/usage/snowflake_usage.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_browse_path.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_browse_path.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_ownership.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_ownership.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_properties.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_properties.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_schema_tags.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_schema_tags.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_schema_terms.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_schema_terms.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_tags.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_tags.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/add_dataset_terms.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/add_dataset_terms.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/base_transformer.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/base_transformer.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/dataset_domain.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/dataset_domain.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/dataset_transformer.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/dataset_transformer.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/mark_dataset_status.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/mark_dataset_status.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/remove_dataset_ownership.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/remove_dataset_ownership.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/ingestion/transformer/transform_registry.py` & `acryl-datahub-0.9.6rc1/src/datahub/ingestion/transformer/transform_registry.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/integrations/great_expectations/action.py` & `acryl-datahub-0.9.6rc1/src/datahub/integrations/great_expectations/action.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/assertion/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/assertion/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/chart/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/chart/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/common/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/common/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dashboard/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dashboard/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/datahub/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/datajob/datahub/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataprocess/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataprocess/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/dataset/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/dataset/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/execution/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/execution/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/identity/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/identity/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ingestion/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ingestion/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/key/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/key/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/snapshot/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/metadata/snapshot/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/ml/metadata/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/ml/metadata/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/mxe/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/mxe/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/notebook/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/notebook/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/policy/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/policy/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/retention/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/retention/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/schema/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/schema/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/test/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/test/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/timeseries/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/timeseries/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/com/linkedin/pegasus2avro/usage/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/com/linkedin/pegasus2avro/usage/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schema.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schema.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schema_classes.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schema_classes.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/AssertionInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/AssertionInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/AssertionRunEvent.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/AssertionRunEvent.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/BrowsePaths.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/BrowsePaths.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CaveatsAndRecommendations.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CaveatsAndRecommendations.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartQuery.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartQuery.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ChartUsageStatistics.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ChartUsageStatistics.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Container.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Container.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ContainerProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ContainerProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpGroupEditableInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpGroupEditableInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpGroupInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpGroupInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserCredentials.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserCredentials.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserEditableInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserEditableInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserSettings.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserSettings.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/CorpUserStatus.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/CorpUserStatus.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Cost.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Cost.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DashboardInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DashboardInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DashboardKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DashboardKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DashboardUsageStatistics.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DashboardUsageStatistics.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataFlowInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataFlowInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataFlowKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataFlowKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubAccessTokenInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubAccessTokenInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubIngestionSourceInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubIngestionSourceInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubPolicyInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubPolicyInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubRetentionConfig.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubRetentionConfig.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubRetentionKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubRetentionKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubRoleInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubRoleInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubSecretValue.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubSecretValue.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubStepStateProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubStepStateProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubUpgradeResult.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubUpgradeResult.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataHubViewInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataHubViewInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataJobInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataJobInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataJobInputOutput.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataJobInputOutput.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataJobKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataJobKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInstance.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInstance.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInstanceKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInstanceKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataPlatformInstanceProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataPlatformInstanceProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceInput.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceInput.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceOutput.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceOutput.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceRelationships.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceRelationships.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessInstanceRunEvent.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessInstanceRunEvent.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DataProcessKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DataProcessKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatahubIngestionCheckpoint.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatahubIngestionCheckpoint.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatahubIngestionRunSummary.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatahubIngestionRunSummary.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetDeprecation.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetDeprecation.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetProfile.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetProfile.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetUpstreamLineage.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetUpstreamLineage.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DatasetUsageStatistics.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DatasetUsageStatistics.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Deprecation.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Deprecation.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/DomainProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/DomainProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Domains.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Domains.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableChartProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableChartProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableContainerProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableContainerProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDashboardProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDashboardProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDataFlowProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDataFlowProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDataJobProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDataJobProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableDatasetProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableDatasetProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableMLModelGroupProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableMLModelGroupProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableMLModelProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableMLModelProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableNotebookProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableNotebookProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EditableSchemaMetadata.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EditableSchemaMetadata.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EntityChangeEvent.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EntityChangeEvent.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EthicalConsiderations.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EthicalConsiderations.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/EvaluationData.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/EvaluationData.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ExecutionRequestInput.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ExecutionRequestInput.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ExecutionRequestResult.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ExecutionRequestResult.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ExecutionRequestSignal.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ExecutionRequestSignal.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Filter.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Filter.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlobalSettingsInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlobalSettingsInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlobalTags.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlobalTags.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryNodeInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryNodeInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryRelatedTerms.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryRelatedTerms.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryTermInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryTermInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/GlossaryTerms.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/GlossaryTerms.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/InputFields.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/InputFields.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/InstitutionalMemory.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/InstitutionalMemory.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/IntendedUse.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/IntendedUse.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/InviteToken.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/InviteToken.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureTableKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureTableKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLFeatureTableProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLFeatureTableProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLHyperParam.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLHyperParam.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLMetric.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLMetric.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelDeploymentKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelDeploymentKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelDeploymentProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelDeploymentProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelFactorPrompts.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelFactorPrompts.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelGroupKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelGroupKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelGroupProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelGroupProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLModelProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLModelProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLPrimaryKeyKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLPrimaryKeyKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MLPrimaryKeyProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MLPrimaryKeyProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MetadataChangeEvent.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MetadataChangeEvent.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MetadataChangeLog.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MetadataChangeLog.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/MetadataChangeProposal.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/MetadataChangeProposal.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Metrics.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Metrics.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NativeGroupMembership.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NativeGroupMembership.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NotebookContent.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NotebookContent.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NotebookInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NotebookInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/NotebookKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/NotebookKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Operation.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Operation.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Origin.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Origin.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Ownership.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Ownership.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/PlatformEvent.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/PlatformEvent.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/PostInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/PostInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/QuantitativeAnalyses.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/QuantitativeAnalyses.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/RoleMembership.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/RoleMembership.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SchemaFieldKey.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SchemaFieldKey.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SchemaMetadata.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SchemaMetadata.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Siblings.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Siblings.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SourceCode.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SourceCode.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/Status.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/Status.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/SubTypes.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/SubTypes.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TagProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TagProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TestInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TestInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TestResults.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TestResults.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/TrainingData.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/TrainingData.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/UpstreamLineage.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/UpstreamLineage.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/UsageAggregation.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/UsageAggregation.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/VersionInfo.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/VersionInfo.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/ViewProperties.avsc` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/ViewProperties.avsc`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/metadata/schemas/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub/metadata/schemas/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/specific/dataset.py` & `acryl-datahub-0.9.6rc1/src/datahub/specific/dataset.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/telemetry/stats.py` & `acryl-datahub-0.9.6rc1/src/datahub/telemetry/stats.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/telemetry/telemetry.py` & `acryl-datahub-0.9.6rc1/src/datahub/telemetry/telemetry.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/upgrade/upgrade.py` & `acryl-datahub-0.9.6rc1/src/datahub/upgrade/upgrade.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/bigquery_sql_parser.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/bigquery_sql_parser.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/checkpoint_state_util.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/checkpoint_state_util.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/delayed_iter.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/delayed_iter.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/hive_schema_to_avro.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/hive_schema_to_avro.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/lossy_collections.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/lossy_collections.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/mapping.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/mapping.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/memory_footprint.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/memory_footprint.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/memory_leak_detector.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/memory_leak_detector.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/parsing_util.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/parsing_util.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/perf_timer.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/perf_timer.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/registries/domain_registry.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/registries/domain_registry.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/sample_data.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/sample_data.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/server_config_util.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/server_config_util.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/source_helpers.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/source_helpers.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/sql_formatter.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/sql_formatter.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/sql_lineage_parser_impl.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/sql_lineage_parser_impl.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/sql_parser.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/sql_parser.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/sqlalchemy_query_combiner.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/sqlalchemy_query_combiner.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/sqllineage_patch.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/sqllineage_patch.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/stats_collections.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/stats_collections.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/type_annotations.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/type_annotations.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urn_encoder.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urn_encoder.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/corp_group_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/corp_group_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/corpuser_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/corpuser_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_flow_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_flow_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_job_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_job_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_platform_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_platform_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/data_process_instance_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/data_process_instance_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/dataset_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/dataset_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/domain_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/domain_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/notebook_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/notebook_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/tag_urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/tag_urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub/utilities/urns/urn.py` & `acryl-datahub-0.9.6rc1/src/datahub/utilities/urns/urn.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/__init__.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/__init__.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/_airflow_shims.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/_airflow_shims.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/_lineage_core.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/_lineage_core.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/_plugin.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/_plugin.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/client/airflow_generator.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/client/airflow_generator.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/entities.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/entities.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/generic_recipe_sample_dag.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/generic_recipe_sample_dag.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/lineage_backend_demo.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/lineage_backend_demo.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/lineage_backend_taskflow_demo.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/lineage_backend_taskflow_demo.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/lineage_emission_dag.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/lineage_emission_dag.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/mysql_sample_dag.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/mysql_sample_dag.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/example_dags/snowflake_sample_dag.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/example_dags/snowflake_sample_dag.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/hooks/datahub.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/hooks/datahub.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/lineage/datahub.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/lineage/datahub.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_assertion_operator.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_assertion_operator.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_assertion_sensor.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_assertion_sensor.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_operation_operator.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_operation_operator.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-0.9.6rc0/src/datahub_provider/operators/datahub_operation_sensor.py` & `acryl-datahub-0.9.6rc1/src/datahub_provider/operators/datahub_operation_sensor.py`

 * *Files identical despite different names*

