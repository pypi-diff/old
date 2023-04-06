# Comparing `tmp/kfp-2.0.0b8.tar.gz` & `tmp/kfp-2.0.0b9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/var/folders/s4/q287k45x17x_j2mlv1lc_43r00xv1g/T/tmp.iQj0LF6M/kfp-2.0.0b8.tar", last modified: Wed Nov 30 05:12:37 2022, max compression
+gzip compressed data, was "/var/folders/s4/q287k45x17x_j2mlv1lc_43r00xv1g/T/tmp.fOlpoJia/kfp-2.0.0b9.tar", last modified: Wed Dec 21 02:26:58 2022, max compression
```

## Comparing `kfp-2.0.0b8.tar` & `kfp-2.0.0b9.tar`

### file list

```diff
@@ -1,247 +1,247 @@
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)       60 2022-11-28 19:47:25.000000 kfp-2.0.0b8/MANIFEST.in
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3890 2022-11-30 05:12:37.000000 kfp-2.0.0b8/PKG-INFO
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2155 2022-11-28 19:47:25.000000 kfp-2.0.0b8/README.md
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      869 2022-11-30 05:11:37.000000 kfp-2.0.0b8/kfp/__init__.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/cli/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      878 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/__main__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4024 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/cli.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7072 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/cli_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5391 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/compile_.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2304 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/compile_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    15375 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    19857 2022-11-28 22:46:03.000000 kfp-2.0.0b8/kfp/cli/component_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      603 2022-06-02 23:27:30.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2460 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/dev_env.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2694 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/dev_env_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6098 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/gcp.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3786 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/gcp_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4495 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/kubernetes_cluster.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3280 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/kubernetes_cluster_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3155 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/utility.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1500 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me/utility_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3511 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/diagnose_me_cli.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      744 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/dsl.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5347 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/experiment.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8261 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/output.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8152 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/pipeline.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9066 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/recurring_run.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8286 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/run.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/cli/utils/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/utils/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1434 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/utils/aliased_plurals_group.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1684 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/utils/aliased_plurals_group_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2439 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/utils/deprecated_alias_group.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1595 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/utils/deprecated_alias_group_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2568 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/utils/parsing.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4169 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/cli/utils/parsing_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/client/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      998 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/client/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    20322 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/client/auth.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    62818 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/client/client.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4014 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/client/client_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3269 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/client/set_volume_credentials.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1926 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/client/set_volume_credentials_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1765 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/client/token_credentials_base.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2390 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/client/token_credentials_base_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/compiler/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      749 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/compiler/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3418 2022-11-29 23:43:01.000000 kfp-2.0.0b8/kfp/compiler/compiler.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    53444 2022-11-29 23:43:01.000000 kfp-2.0.0b8/kfp/compiler/compiler_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    19157 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/compiler/compiler_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    72907 2022-11-29 23:43:01.000000 kfp-2.0.0b8/kfp/compiler/pipeline_spec_builder.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    13102 2022-11-29 23:43:01.000000 kfp-2.0.0b8/kfp/compiler/pipeline_spec_builder_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8163 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/compiler/read_write_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/components/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1321 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3833 2022-11-29 23:43:01.000000 kfp-2.0.0b8/kfp/components/base_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4396 2022-11-28 22:46:03.000000 kfp-2.0.0b8/kfp/components/base_component_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5995 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/component_decorator.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5507 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/component_decorator_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    19739 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/component_factory.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2534 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/component_factory_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1079 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/constants.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1459 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/container_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1997 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/container_component_artifact_channel.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1831 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/container_component_artifact_channel_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1905 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/container_component_decorator.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2707 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/container_component_decorator_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14323 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/executor.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3775 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/executor_main.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    38387 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/executor_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9855 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/for_loop.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6428 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/for_loop_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2975 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/graph_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1015 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/importer_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5510 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/importer_node.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7662 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/importer_node_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4036 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/kfp_config.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    12875 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/pipeline_channel.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5657 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/pipeline_channel_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6352 2022-11-29 20:18:16.000000 kfp-2.0.0b8/kfp/components/pipeline_context.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    21421 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/pipeline_task.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14724 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/pipeline_task_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14193 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/placeholders.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    18122 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/placeholders_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1466 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/python_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    39396 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/structures.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    32584 2022-11-28 22:46:03.000000 kfp-2.0.0b8/kfp/components/structures_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2372 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/task_final_status.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7713 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/tasks_group.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2851 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/tasks_group_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/components/types/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/types/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    18836 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/types/artifact_types.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2415 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/types/artifact_types_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8046 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/types/custom_artifact_types.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    16140 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/types/custom_artifact_types_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6691 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/types/type_annotations.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7131 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/components/types/type_annotations_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14984 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/types/type_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    13813 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/types/type_utils_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3859 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3679 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/utils_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1740 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/v1_components.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    16606 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/v1_modelbase.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    28068 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/v1_structures.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4194 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/yaml_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4324 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/components/yaml_component_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      811 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      767 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/__main__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9693 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/_auth.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    63449 2022-11-28 22:46:03.000000 kfp-2.0.0b8/kfp/deprecated/_client.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      799 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/_config.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    20892 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/_local_client.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3829 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/_runners.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/auth/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      859 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/auth/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2594 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/auth/_satvolumecredentials.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1551 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/auth/_tokencredentialsbase.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2561 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/aws.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2272 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/azure.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/cli/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      584 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3038 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/cli.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    15615 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/components.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17870 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/components_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      603 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2489 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/dev_env.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2734 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/dev_env_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6151 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/gcp.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3826 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/gcp_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4547 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/kubernetes_cluster.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3320 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/kubernetes_cluster_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3169 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/utility.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1529 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/utility_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3729 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me_cli.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4548 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/experiment.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2156 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/output.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9207 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/pipeline.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7544 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/recurring_run.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7476 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/cli/run.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/compiler/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      761 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    24589 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/_data_passing_rewriter.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    12032 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/_data_passing_using_volume.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3480 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/_default_transformers.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3168 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/_k8s_helper.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14459 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/_op_to_template.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    58420 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/compiler.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5028 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/main.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6946 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/v2_compat.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7033 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/compiler/v2_compatible_compiler_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/components/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      740 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6680 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_airflow_op.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    16145 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_component_store.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    25925 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_components.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8214 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_data_passing.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3572 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_dynamic.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2552 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_key_value_store.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4189 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_naming.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    52469 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_python_op.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9535 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_python_to_graph_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    29100 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_structures.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2757 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/_yaml_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17572 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/modelbase.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/components/structures/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)       28 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/structures/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1917 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/type_annotation_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2809 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/components/type_annotation_utils_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/containers/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      581 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7468 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/_build_image_api.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2527 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/_cache.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17356 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/_component_builder.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    10904 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/_container_builder.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3603 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/_gcs_helper.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7344 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/_k8s_job_helper.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8735 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/entrypoint.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7158 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/containers/entrypoint_utils.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/dsl/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1665 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6364 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_component.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    30557 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_component_bridge.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    63751 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_container_op.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1865 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_container_op_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    10053 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_for_loop.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3857 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_metadata.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8123 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_ops_group.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    13111 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_pipeline.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9125 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_pipeline_param.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4483 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_pipeline_volume.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8409 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_resource_op.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6057 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_volume_op.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4771 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/_volume_snapshot_op.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7871 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/artifact.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3439 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/artifact_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    18942 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/component_spec.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    25290 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/component_spec_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1210 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/data_passing_methods.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5155 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/dsl_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2119 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/dsl_utils_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/dsl/extensions/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/extensions/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3511 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/extensions/kubernetes.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1311 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/io_types.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6121 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/metrics_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2330 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/metrics_utils_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1367 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/serialization_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1221 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/serialization_utils_test.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3750 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/type_utils.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7886 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/dsl/types.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5984 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/gcp.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/deprecated/notebook/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      607 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/notebook/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/notebook/_magic.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4757 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/deprecated/onprem.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/dsl/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7143 2022-11-30 05:11:36.000000 kfp-2.0.0b8/kfp/dsl/__init__.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/registry/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      837 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/registry/__init__.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/registry/context/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/registry/context/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1060 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/registry/context/default_pkg_dev.json
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2381 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/registry/context/kfp_pkg_dev.json
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    21147 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/registry/registry_client.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17404 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/registry/registry_client_test.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp/v2/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      921 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/v2/__init__.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      621 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/v2/compiler.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      623 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/v2/components.py
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      616 2022-11-28 19:47:25.000000 kfp-2.0.0b8/kfp/v2/dsl.py
-drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp.egg-info/
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3890 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp.egg-info/PKG-INFO
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7594 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp.egg-info/SOURCES.txt
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)        1 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp.egg-info/dependency_links.txt
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      142 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp.egg-info/entry_points.txt
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      556 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp.egg-info/requires.txt
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)        4 2022-11-30 05:12:37.000000 kfp-2.0.0b8/kfp.egg-info/top_level.txt
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1418 2022-11-28 19:47:25.000000 kfp-2.0.0b8/requirements.in
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)       38 2022-11-30 05:12:37.000000 kfp-2.0.0b8/setup.cfg
--rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3613 2022-11-28 19:47:25.000000 kfp-2.0.0b8/setup.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)       60 2022-12-21 00:57:23.000000 kfp-2.0.0b9/MANIFEST.in
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3890 2022-12-21 02:26:58.000000 kfp-2.0.0b9/PKG-INFO
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2155 2022-12-21 00:57:23.000000 kfp-2.0.0b9/README.md
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      869 2022-12-21 02:23:10.000000 kfp-2.0.0b9/kfp/__init__.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/cli/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      878 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/__main__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4024 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/cli.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7072 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/cli_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5391 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/compile_.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2304 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/compile_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    15375 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    19857 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/component_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      603 2022-06-02 23:27:30.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2460 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/dev_env.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2694 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/dev_env_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6098 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/gcp.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3786 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/gcp_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4495 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/kubernetes_cluster.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3280 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/kubernetes_cluster_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3155 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/utility.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1500 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me/utility_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3511 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/diagnose_me_cli.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      744 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/dsl.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5347 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/experiment.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8261 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/output.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8152 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/pipeline.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9066 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/recurring_run.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8286 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/run.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/cli/utils/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/utils/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1434 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/utils/aliased_plurals_group.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1684 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/utils/aliased_plurals_group_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2439 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/utils/deprecated_alias_group.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1595 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/utils/deprecated_alias_group_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2568 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/utils/parsing.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4169 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/cli/utils/parsing_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/client/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      998 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    20239 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/auth.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    62973 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/client.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    12327 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/client_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3269 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/set_volume_credentials.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1926 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/set_volume_credentials_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1765 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/token_credentials_base.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2390 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/client/token_credentials_base_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/compiler/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      749 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/compiler/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3414 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/compiler/compiler.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    84159 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/compiler/compiler_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    20834 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/compiler/compiler_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    75610 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/compiler/pipeline_spec_builder.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    11250 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/compiler/pipeline_spec_builder_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8163 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/compiler/read_write_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/components/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1321 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4851 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/base_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5441 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/base_component_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5995 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/component_decorator.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5507 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/component_decorator_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    21063 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/component_factory.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6109 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/component_factory_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1079 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/constants.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1459 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/container_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1997 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/container_component_artifact_channel.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1831 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/container_component_artifact_channel_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1905 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/container_component_decorator.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2707 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/container_component_decorator_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    15216 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/executor.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3649 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/executor_main.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    43375 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/executor_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9775 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/for_loop.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6428 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/for_loop_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2975 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/graph_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1015 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/importer_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5510 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/importer_node.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7662 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/importer_node_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4012 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/kfp_config.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    12848 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/pipeline_channel.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5657 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/pipeline_channel_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6352 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/pipeline_context.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    20812 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/pipeline_task.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9602 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/pipeline_task_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14193 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/placeholders.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    18122 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/placeholders_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1466 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/python_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    41899 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/structures.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    32584 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/structures_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2372 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/task_final_status.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7705 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/tasks_group.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2851 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/tasks_group_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/components/types/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    18756 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/artifact_types.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2415 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/artifact_types_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8059 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/custom_artifact_types.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    16140 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/custom_artifact_types_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7405 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/type_annotations.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7717 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/type_annotations_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14982 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/type_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    13813 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/types/type_utils_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3859 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3679 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/utils_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1740 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/v1_components.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    16240 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/v1_modelbase.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    27893 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/v1_structures.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4194 2022-12-21 02:25:42.000000 kfp-2.0.0b9/kfp/components/yaml_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4324 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/components/yaml_component_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      811 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      767 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/__main__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9693 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/_auth.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    63449 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/_client.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      799 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/_config.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    20892 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/_local_client.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3829 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/_runners.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/auth/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      859 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/auth/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2594 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/auth/_satvolumecredentials.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1551 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/auth/_tokencredentialsbase.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2561 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/aws.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2272 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/azure.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/cli/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      584 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3038 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/cli.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    15615 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/components.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17870 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/components_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      603 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2489 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/dev_env.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2734 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/dev_env_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6151 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/gcp.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3826 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/gcp_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4547 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/kubernetes_cluster.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3320 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/kubernetes_cluster_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3169 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/utility.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1529 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/utility_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3729 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me_cli.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4548 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/experiment.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2156 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/output.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9207 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/pipeline.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7544 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/recurring_run.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7476 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/cli/run.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/compiler/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      761 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    24589 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/_data_passing_rewriter.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    12032 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/_data_passing_using_volume.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3480 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/_default_transformers.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3168 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/_k8s_helper.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    14459 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/_op_to_template.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    58420 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/compiler.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5028 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/main.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6946 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/v2_compat.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7033 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/compiler/v2_compatible_compiler_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/components/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      740 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6680 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_airflow_op.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    16145 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_component_store.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    25925 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_components.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8214 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_data_passing.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3572 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_dynamic.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2552 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_key_value_store.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4189 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_naming.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    52469 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_python_op.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9535 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_python_to_graph_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    29100 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_structures.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2757 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/_yaml_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17572 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/modelbase.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/components/structures/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)       28 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/structures/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1917 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/type_annotation_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2809 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/components/type_annotation_utils_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/containers/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      581 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7468 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/_build_image_api.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2527 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/_cache.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17356 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/_component_builder.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    10904 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/_container_builder.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3603 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/_gcs_helper.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7344 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/_k8s_job_helper.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8735 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/entrypoint.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7158 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/containers/entrypoint_utils.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/dsl/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1665 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6364 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_component.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    30557 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_component_bridge.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    63751 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_container_op.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1865 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_container_op_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    10053 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_for_loop.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3857 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_metadata.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8123 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_ops_group.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    13111 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_pipeline.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     9125 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_pipeline_param.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4483 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_pipeline_volume.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     8409 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_resource_op.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6057 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_volume_op.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4771 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/_volume_snapshot_op.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7871 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/artifact.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3439 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/artifact_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    18942 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/component_spec.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    25290 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/component_spec_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1210 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/data_passing_methods.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5155 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/dsl_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2119 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/dsl_utils_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/dsl/extensions/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/extensions/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3511 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/extensions/kubernetes.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1311 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/io_types.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     6121 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/metrics_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2330 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/metrics_utils_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1367 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/serialization_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1221 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/serialization_utils_test.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3750 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/type_utils.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7886 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/dsl/types.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     5984 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/gcp.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/deprecated/notebook/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      607 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/notebook/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/notebook/_magic.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     4757 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/deprecated/onprem.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/dsl/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7143 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/dsl/__init__.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/registry/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      837 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/registry/__init__.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/registry/context/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      585 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/registry/context/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1060 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/registry/context/default_pkg_dev.json
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     2381 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/registry/context/kfp_pkg_dev.json
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    21147 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/registry/registry_client.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)    17404 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/registry/registry_client_test.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp/v2/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      921 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/v2/__init__.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      621 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/v2/compiler.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      623 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/v2/components.py
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      616 2022-12-21 00:57:23.000000 kfp-2.0.0b9/kfp/v2/dsl.py
+drwxr-xr-x   0 cjmccarthy (977967) primarygroup (89939)        0 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp.egg-info/
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3890 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp.egg-info/PKG-INFO
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     7594 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp.egg-info/SOURCES.txt
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)        1 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp.egg-info/dependency_links.txt
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      142 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp.egg-info/entry_points.txt
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)      556 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp.egg-info/requires.txt
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)        4 2022-12-21 02:26:58.000000 kfp-2.0.0b9/kfp.egg-info/top_level.txt
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     1418 2022-12-21 00:57:23.000000 kfp-2.0.0b9/requirements.in
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)       38 2022-12-21 02:26:58.000000 kfp-2.0.0b9/setup.cfg
+-rw-r--r--   0 cjmccarthy (977967) primarygroup (89939)     3613 2022-12-21 00:57:23.000000 kfp-2.0.0b9/setup.py
```

### Comparing `kfp-2.0.0b8/PKG-INFO` & `kfp-2.0.0b9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kfp
-Version: 2.0.0b8
+Version: 2.0.0b9
 Summary: Kubeflow Pipelines SDK
 Home-page: https://github.com/kubeflow/pipelines
 Author: The Kubeflow Authors
 License: UNKNOWN
 Project-URL: Documentation, https://kubeflow-pipelines.readthedocs.io/en/stable/
 Project-URL: Bug Tracker, https://github.com/kubeflow/pipelines/issues
 Project-URL: Source, https://github.com/kubeflow/pipelines/tree/master/sdk
```

### Comparing `kfp-2.0.0b8/README.md` & `kfp-2.0.0b9/README.md`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/__init__.py` & `kfp-2.0.0b9/kfp/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,12 +12,12 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 # `kfp` is a namespace package.
 # https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages
 __path__ = __import__('pkgutil').extend_path(__path__, __name__)
 
-__version__ = '2.0.0-beta.8'
+__version__ = '2.0.0-beta.9'
 
 TYPE_CHECK = True
 
 from kfp.client import Client
```

### Comparing `kfp-2.0.0b8/kfp/cli/__init__.py` & `kfp-2.0.0b9/kfp/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/__main__.py` & `kfp-2.0.0b9/kfp/cli/__main__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/cli.py` & `kfp-2.0.0b9/kfp/cli/cli.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/cli_test.py` & `kfp-2.0.0b9/kfp/cli/cli_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/compile_.py` & `kfp-2.0.0b9/kfp/cli/compile_.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/compile_test.py` & `kfp-2.0.0b9/kfp/cli/compile_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/component.py` & `kfp-2.0.0b9/kfp/cli/component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/component_test.py` & `kfp-2.0.0b9/kfp/cli/component_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/__init__.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/dev_env.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/dev_env.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/dev_env_test.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/dev_env_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/gcp.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/gcp.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/gcp_test.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/gcp_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/kubernetes_cluster.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/kubernetes_cluster.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/kubernetes_cluster_test.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/kubernetes_cluster_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/utility.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/utility.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me/utility_test.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me/utility_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/diagnose_me_cli.py` & `kfp-2.0.0b9/kfp/cli/diagnose_me_cli.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/dsl.py` & `kfp-2.0.0b9/kfp/cli/dsl.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/experiment.py` & `kfp-2.0.0b9/kfp/cli/experiment.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/output.py` & `kfp-2.0.0b9/kfp/cli/output.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/pipeline.py` & `kfp-2.0.0b9/kfp/cli/pipeline.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/recurring_run.py` & `kfp-2.0.0b9/kfp/cli/recurring_run.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/run.py` & `kfp-2.0.0b9/kfp/cli/run.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/utils/__init__.py` & `kfp-2.0.0b9/kfp/cli/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/utils/aliased_plurals_group.py` & `kfp-2.0.0b9/kfp/cli/utils/aliased_plurals_group.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/utils/aliased_plurals_group_test.py` & `kfp-2.0.0b9/kfp/cli/utils/aliased_plurals_group_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/utils/deprecated_alias_group.py` & `kfp-2.0.0b9/kfp/cli/utils/deprecated_alias_group.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/utils/deprecated_alias_group_test.py` & `kfp-2.0.0b9/kfp/cli/utils/deprecated_alias_group_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/utils/parsing.py` & `kfp-2.0.0b9/kfp/cli/utils/parsing.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/cli/utils/parsing_test.py` & `kfp-2.0.0b9/kfp/cli/utils/parsing_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/client/__init__.py` & `kfp-2.0.0b9/kfp/client/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/client/auth.py` & `kfp-2.0.0b9/kfp/client/auth.py`

 * *Files 0% similar despite different names*

```diff
@@ -97,17 +97,19 @@
         # and return ID token
         refresh_token, is_refresh_token = get_refresh_token_from_client_id(
             other_client_id, other_client_secret)
         credentials = {}
         if os.path.exists(LOCAL_KFP_CREDENTIAL):
             with open(LOCAL_KFP_CREDENTIAL, 'r') as f:
                 credentials = json.load(f)
-        credentials[client_id] = {}
-        credentials[client_id]['other_client_id'] = other_client_id
-        credentials[client_id]['other_client_secret'] = other_client_secret
+        credentials[client_id] = {
+            'other_client_id': other_client_id,
+            'other_client_secret': other_client_secret
+        }
+
         if is_refresh_token:
             credentials[client_id]['refresh_token'] = refresh_token
         else:
             credentials[client_id]['access_token'] = refresh_token
         # TODO: handle the case when the refresh_token expires, which only
         # happens if the refresh_token is not used once for six months.
         if not os.path.exists(os.path.dirname(LOCAL_KFP_CREDENTIAL)):
@@ -304,20 +306,19 @@
         port: Port in redirect_uri.
         auth_url: OAuth request URL.
 
     Returns:
         A URL containing authorization code.
     """
     print(auth_url)
-    authorization_response = input(
+    return input(
         'Carefully follow these steps: (1) open the URL above in your'
         ' browser, (2) authenticate and copy a url of the response page'
         f' that starts with http://{host}:{port}..., and (3) paste it'
         ' below:\n')
-    return authorization_response
 
 
 def get_auth_response_local(host: str, port: int,
                             auth_url: str) -> Union[str, None]:
     """Fetches OAuth authorization response URL using a local web-server.
 
     Args:
```

### Comparing `kfp-2.0.0b8/kfp/client/client.py` & `kfp-2.0.0b9/kfp/client/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -394,40 +394,45 @@
         """
         self._context_setting['namespace'] = namespace
         if not os.path.exists(os.path.dirname(Client._LOCAL_KFP_CONTEXT)):
             os.makedirs(os.path.dirname(Client._LOCAL_KFP_CONTEXT))
         with open(Client._LOCAL_KFP_CONTEXT, 'w') as f:
             json.dump(self._context_setting, f)
 
-    def get_kfp_healthz(self) -> kfp_server_api.ApiGetHealthzResponse:
+    def get_kfp_healthz(
+            self,
+            sleep_duration: int = 5) -> kfp_server_api.ApiGetHealthzResponse:
         """Gets healthz info for KFP deployment.
 
+        Args:
+            sleep_duration: Time in seconds between retries.
+
         Returns:
-            JSON response from the healtz endpoint.
+            JSON response from the healthz endpoint.
         """
         count = 0
         response = None
         max_attempts = 5
         while not response:
             count += 1
             if count > max_attempts:
                 raise TimeoutError(
                     f'Failed getting healthz endpoint after {max_attempts} attempts.'
                 )
 
             try:
-                response = self._healthz_api.get_healthz()
-                return response
+                return self._healthz_api.get_healthz()
             # ApiException, including network errors, is the only type that may
             # recover after retry.
             except kfp_server_api.ApiException:
                 # logging.exception also logs detailed info about the ApiException
                 logging.exception(
-                    f'Failed to get healthz info attempt {count} of 5.')
-                time.sleep(5)
+                    f'Failed to get healthz info attempt {count} of {max_attempts}.'
+                )
+                time.sleep(sleep_duration)
 
     def get_user_namespace(self) -> str:
         """Gets user namespace in context config.
 
         Returns:
             Kubernetes namespace from the local context file or empty if it
             wasn't set.
@@ -459,15 +464,15 @@
             if not str(error).startswith('No experiment is found with name'):
                 raise error
 
         if not experiment:
             logging.info(f'Creating experiment {name}.')
 
             resource_references = []
-            if namespace:
+            if namespace is not None:
                 key = kfp_server_api.ApiResourceKey(
                     id=namespace, type=kfp_server_api.ApiResourceType.NAMESPACE)
                 reference = kfp_server_api.ApiResourceReference(
                     key=key, relationship=kfp_server_api.ApiRelationship.OWNER)
                 resource_references.append(reference)
 
             experiment = kfp_server_api.ApiExperiment(
@@ -541,23 +546,22 @@
                         }]
                     })
 
         Returns:
             ``ApiListExperimentsResponse`` object.
         """
         namespace = namespace or self.get_user_namespace()
-        response = self._experiment_api.list_experiment(
+        return self._experiment_api.list_experiment(
             page_token=page_token,
             page_size=page_size,
             sort_by=sort_by,
             resource_reference_key_type=kfp_server_api.ApiResourceType
             .NAMESPACE,
             resource_reference_key_id=namespace,
             filter=filter)
-        return response
 
     def get_experiment(self,
                        experiment_id=None,
                        experiment_name=None,
                        namespace=None) -> kfp_server_api.ApiExperiment:
         """Gets details of an experiment.
 
@@ -580,15 +584,15 @@
         experiment_filter = json.dumps({
             'predicates': [{
                 'op': _FILTER_OPERATIONS['EQUALS'],
                 'key': 'name',
                 'stringValue': experiment_name,
             }]
         })
-        if namespace:
+        if namespace is not None:
             result = self._experiment_api.list_experiment(
                 filter=experiment_filter,
                 resource_reference_key_type=kfp_server_api.ApiResourceType
                 .NAMESPACE,
                 resource_reference_key_id=namespace)
         else:
             result = self._experiment_api.list_experiment(
@@ -1201,38 +1205,39 @@
                     })
 
           Returns:
             ``ApiListRunsResponse`` object.
         """
         namespace = namespace or self.get_user_namespace()
         if experiment_id is not None:
-            response = self._run_api.list_runs(
+            return self._run_api.list_runs(
                 page_token=page_token,
                 page_size=page_size,
                 sort_by=sort_by,
                 resource_reference_key_type=kfp_server_api.ApiResourceType
                 .EXPERIMENT,
                 resource_reference_key_id=experiment_id,
                 filter=filter)
-        elif namespace:
-            response = self._run_api.list_runs(
+
+        elif namespace is not None:
+            return self._run_api.list_runs(
                 page_token=page_token,
                 page_size=page_size,
                 sort_by=sort_by,
                 resource_reference_key_type=kfp_server_api.ApiResourceType
                 .NAMESPACE,
                 resource_reference_key_id=namespace,
                 filter=filter)
+
         else:
-            response = self._run_api.list_runs(
+            return self._run_api.list_runs(
                 page_token=page_token,
                 page_size=page_size,
                 sort_by=sort_by,
                 filter=filter)
-        return response
 
     def list_recurring_runs(
             self,
             page_token: str = '',
             page_size: int = 10,
             sort_by: str = '',
             experiment_id: Optional[str] = None,
@@ -1257,29 +1262,29 @@
                         }]
                     })
 
         Returns:
             ``ApiListJobsResponse`` object.
         """
         if experiment_id is not None:
-            response = self._job_api.list_jobs(
+            return self._job_api.list_jobs(
                 page_token=page_token,
                 page_size=page_size,
                 sort_by=sort_by,
                 resource_reference_key_type=kfp_server_api.ApiResourceType
                 .EXPERIMENT,
                 resource_reference_key_id=experiment_id,
                 filter=filter)
+
         else:
-            response = self._job_api.list_jobs(
+            return self._job_api.list_jobs(
                 page_token=page_token,
                 page_size=page_size,
                 sort_by=sort_by,
                 filter=filter)
-        return response
 
     def get_recurring_run(self, job_id: str) -> kfp_server_api.ApiJob:
         """Gets recurring run (job) details.
 
         Args:
             job_id: ID of the recurring run (job).
 
@@ -1295,21 +1300,25 @@
             run_id: ID of the run.
 
         Returns:
             ``ApiRun`` object.
         """
         return self._run_api.get_run(run_id=run_id)
 
-    def wait_for_run_completion(self, run_id: str,
-                                timeout: int) -> kfp_server_api.ApiRun:
+    def wait_for_run_completion(
+            self,
+            run_id: str,
+            timeout: int,
+            sleep_duration: int = 5) -> kfp_server_api.ApiRun:
         """Waits for a run to complete.
 
         Args:
             run_id: ID of the run.
             timeout: Timeout after which the client should stop waiting for run completion (seconds).
+            sleep_duration: Time in seconds between retries.
 
         Returns:
             ``ApiRun`` object.
         """
         status = 'Running:'
         start_time = datetime.datetime.now()
         if isinstance(timeout, datetime.timedelta):
@@ -1331,30 +1340,29 @@
                     raise api_ex
             status = get_run_response.run.status
             elapsed_time = (datetime.datetime.now() -
                             start_time).total_seconds()
             logging.info('Waiting for the job to complete...')
             if elapsed_time > timeout:
                 raise TimeoutError('Run timeout')
-            time.sleep(5)
+            time.sleep(sleep_duration)
         return get_run_response
 
     def _get_workflow_json(self, run_id: str) -> dict:
         """Gets the workflow json.
 
         Args:
             run_id: run id, returned from run_pipeline.
 
         Returns:
             Workflow JSON.
         """
         get_run_response = self._run_api.get_run(run_id=run_id)
         workflow = get_run_response.pipeline_runtime.workflow_manifest
-        workflow_json = json.loads(workflow)
-        return workflow_json
+        return json.loads(workflow)
 
     def upload_pipeline(
         self,
         pipeline_package_path: str = None,
         pipeline_name: str = None,
         description: str = None,
     ) -> kfp_server_api.ApiPipeline:
```

### Comparing `kfp-2.0.0b8/kfp/client/client_test.py` & `kfp-2.0.0b9/kfp/deprecated/_runners.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,114 +1,95 @@
-# Copyright 2022 The Kubeflow Authors
+# Copyright 2019 The Kubeflow Authors
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-import os
-import tempfile
-import unittest
-
-from absl.testing import parameterized
-from kfp.client import client
-from kfp.compiler import Compiler
-from kfp.dsl import component
-from kfp.dsl import pipeline
-import yaml
-
-
-class TestValidatePipelineName(parameterized.TestCase):
-
-    @parameterized.parameters([
-        'pipeline',
-        'my-pipeline',
-        'my-pipeline-1',
-        '1pipeline',
-        'pipeline1',
-    ])
-    def test_valid(self, name: str):
-        client.validate_pipeline_resource_name(name)
-
-    @parameterized.parameters([
-        'my_pipeline',
-        "person's-pipeline",
-        'my pipeline',
-        'pipeline.yaml',
-    ])
-    def test_invalid(self, name: str):
-        with self.assertRaisesRegex(ValueError, r'Invalid pipeline name:'):
-            client.validate_pipeline_resource_name(name)
-
-
-class TestOverrideCachingOptions(parameterized.TestCase):
-
-    def test_override_caching_from_pipeline(self):
-
-        @component
-        def hello_world(text: str) -> str:
-            """Hello world component."""
-            return text
-
-        @pipeline(name='hello-world', description='A simple intro pipeline')
-        def pipeline_hello_world(text: str = 'hi there'):
-            """Hello world pipeline."""
-
-            hello_world(text=text).set_caching_options(True)
-
-        with tempfile.TemporaryDirectory() as tempdir:
-            temp_filepath = os.path.join(tempdir, 'hello_world_pipeline.yaml')
-            Compiler().compile(
-                pipeline_func=pipeline_hello_world, package_path=temp_filepath)
-
-            with open(temp_filepath, 'r') as f:
-                pipeline_obj = yaml.safe_load(f)
-                test_client = client.Client(namespace='dummy_namespace')
-                test_client._override_caching_options(pipeline_obj, False)
-                for _, task in pipeline_obj['root']['dag']['tasks'].items():
-                    self.assertFalse(task['cachingOptions']['enableCache'])
-
-    def test_override_caching_of_multiple_components(self):
-
-        @component
-        def hello_word(text: str) -> str:
-            return text
-
-        @component
-        def to_lower(text: str) -> str:
-            return text.lower()
-
-        @pipeline(
-            name='sample two-step pipeline',
-            description='a minimal two-step pipeline')
-        def pipeline_with_two_component(text: str = 'hi there'):
-
-            component_1 = hello_word(text=text).set_caching_options(True)
-            component_2 = to_lower(
-                text=component_1.output).set_caching_options(True)
-
-        with tempfile.TemporaryDirectory() as tempdir:
-            temp_filepath = os.path.join(tempdir, 'hello_world_pipeline.yaml')
-            Compiler().compile(
-                pipeline_func=pipeline_with_two_component,
-                package_path=temp_filepath)
-
-            with open(temp_filepath, 'r') as f:
-                pipeline_obj = yaml.safe_load(f)
-                test_client = client.Client(namespace='dummy_namespace')
-                test_client._override_caching_options(pipeline_obj, False)
-                self.assertFalse(
-                    pipeline_obj['root']['dag']['tasks']['hello-word']
-                    ['cachingOptions']['enableCache'])
-                self.assertFalse(pipeline_obj['root']['dag']['tasks']
-                                 ['to-lower']['cachingOptions']['enableCache'])
-
-
-if __name__ == '__main__':
-    unittest.main()
+__all__ = [
+    "run_pipeline_func_on_cluster",
+    "run_pipeline_func_locally",
+]
+
+from typing import Callable, Mapping, Optional
+
+from . import Client, LocalClient, dsl
+
+
+def run_pipeline_func_on_cluster(
+    pipeline_func: Callable,
+    arguments: Mapping[str, str],
+    run_name: str = None,
+    experiment_name: str = None,
+    kfp_client: Client = None,
+    pipeline_conf: dsl.PipelineConf = None,
+):
+    """Runs pipeline on KFP-enabled Kubernetes cluster.
+
+    This command compiles the pipeline function, creates or gets an experiment
+    and submits the pipeline for execution.
+
+    Feature stage:
+    [Alpha](https://github.com/kubeflow/pipelines/blob/07328e5094ac2981d3059314cc848fbb71437a76/docs/release/feature-stages.md#alpha)
+
+    Args:
+      pipeline_func: A function that describes a pipeline by calling components
+      and composing them into execution graph.
+      arguments: Arguments to the pipeline function provided as a dict.
+      run_name: Optional. Name of the run to be shown in the UI.
+      experiment_name: Optional. Name of the experiment to add the run to.
+      kfp_client: Optional. An instance of kfp.Client configured for the desired
+        KFP cluster.
+      pipeline_conf: Optional. kfp.dsl.PipelineConf instance. Can specify op
+        transforms, image pull secrets and other pipeline-level configuration
+        options.
+    """
+    kfp_client = kfp_client or Client()
+    return kfp_client.create_run_from_pipeline_func(pipeline_func, arguments,
+                                                    run_name, experiment_name,
+                                                    pipeline_conf)
+
+
+def run_pipeline_func_locally(
+        pipeline_func: Callable,
+        arguments: Mapping[str, str],
+        local_client: Optional[LocalClient] = None,
+        pipeline_root: Optional[str] = None,
+        execution_mode: LocalClient.ExecutionMode = LocalClient.ExecutionMode(),
+):
+    """Runs a pipeline locally, either using Docker or in a local process.
+
+    Feature stage:
+    [Alpha](https://github.com/kubeflow/pipelines/blob/master/docs/release/feature-stages.md#alpha)
+
+    In this alpha implementation, we support:
+      * Control flow: Condition, ParallelFor
+      * Data passing: InputValue, InputPath, OutputPath
+
+    And we don't support:
+      * Control flow: ExitHandler, Graph, SubGraph
+      * ContainerOp with environment variables, init containers, sidecars, pvolumes
+      * ResourceOp
+      * VolumeOp
+      * Caching
+
+    Args:
+      pipeline_func: A function that describes a pipeline by calling components
+        and composing them into execution graph.
+      arguments: Arguments to the pipeline function provided as a dict.
+        reference to `kfp.client.create_run_from_pipeline_func`.
+      local_client: Optional. An instance of kfp.LocalClient.
+      pipeline_root: Optional. The root directory where the output artifact of component
+        will be saved.
+      execution_mode: Configuration to decide whether the client executes component
+        in docker or in local process.
+    """
+    local_client = local_client or LocalClient(pipeline_root)
+    return local_client.create_run_from_pipeline_func(
+        pipeline_func, arguments, execution_mode=execution_mode)
```

### Comparing `kfp-2.0.0b8/kfp/client/set_volume_credentials.py` & `kfp-2.0.0b9/kfp/client/set_volume_credentials.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/client/set_volume_credentials_test.py` & `kfp-2.0.0b9/kfp/client/set_volume_credentials_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/client/token_credentials_base.py` & `kfp-2.0.0b9/kfp/client/token_credentials_base.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/client/token_credentials_base_test.py` & `kfp-2.0.0b9/kfp/client/token_credentials_base_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/compiler/__init__.py` & `kfp-2.0.0b9/kfp/compiler/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/compiler/compiler.py` & `kfp-2.0.0b9/kfp/compiler/compiler.py`

 * *Files 14% similar despite different names*

```diff
@@ -17,16 +17,14 @@
 https://docs.google.com/document/d/1PUDuSQ8vmeKSBloli53mp7GIvzekaY7sggg6ywy35Dk/
 """
 
 from typing import Any, Callable, Dict, Optional, Union
 
 from kfp.compiler import pipeline_spec_builder as builder
 from kfp.components import base_component
-from kfp.components import graph_component
-from kfp.components import yaml_component
 from kfp.components.types import type_utils
 
 
 class Compiler:
     """Compiles pipelines composed using the KFP SDK DSL to a YAML pipeline
     definition.
 
@@ -75,9 +73,12 @@
                     f'decorator. Got: {type(pipeline_func)}')
 
             pipeline_spec = builder.modify_pipeline_spec_with_override(
                 pipeline_spec=pipeline_func.pipeline_spec,
                 pipeline_name=pipeline_name,
                 pipeline_parameters=pipeline_parameters,
             )
+
             builder.write_pipeline_spec_to_file(
-                pipeline_spec=pipeline_spec, package_path=package_path)
+                pipeline_spec=pipeline_spec,
+                pipeline_description=pipeline_func.description,
+                package_path=package_path)
```

### Comparing `kfp-2.0.0b8/kfp/compiler/compiler_test.py` & `kfp-2.0.0b9/kfp/compiler/compiler_test.py`

 * *Files 21% similar despite different names*

```diff
@@ -14,25 +14,31 @@
 
 import collections
 import json
 import os
 import re
 import subprocess
 import tempfile
+import textwrap
 from typing import Any, Dict, List, NamedTuple, Optional
 import unittest
 
 from absl.testing import parameterized
 from click import testing
 from google.protobuf import json_format
 from kfp import components
 from kfp import dsl
 from kfp.cli import cli
 from kfp.compiler import compiler
 from kfp.components.types import type_utils
+from kfp.dsl import ContainerSpec
+from kfp.dsl import Input
+from kfp.dsl import Model
+from kfp.dsl import Output
+from kfp.dsl import OutputPath
 from kfp.dsl import PipelineTaskFinalStatus
 from kfp.pipeline_spec import pipeline_spec_pb2
 import yaml
 
 VALID_PRODUCER_COMPONENT_SAMPLE = components.load_component_from_text("""
     name: producer
     inputs:
@@ -433,15 +439,15 @@
 
         @dsl.component
         def dummy_op(msg: str = ''):
             pass
 
         with self.assertRaisesRegex(
                 RuntimeError,
-                'Task dummy-op cannot dependent on any task inside the group:'):
+                r'Tasks cannot depend on an upstream task inside'):
 
             @dsl.pipeline(name='test-pipeline')
             def my_pipeline(val: bool):
                 with dsl.ParallelFor(['a, b']):
                     producer_task = producer_op()
 
                 dummy_op(msg=producer_task.output)
@@ -475,15 +481,15 @@
 
         @dsl.component
         def dummy_op(msg: str = ''):
             pass
 
         with self.assertRaisesRegex(
                 RuntimeError,
-                'Task dummy-op cannot dependent on any task inside the group:'):
+                r'Tasks cannot depend on an upstream task inside'):
 
             @dsl.pipeline(name='test-pipeline')
             def my_pipeline(val: bool):
                 with dsl.Condition(val == False):
                     producer_task = producer_op()
 
                 dummy_op(msg=producer_task.output)
@@ -517,15 +523,15 @@
 
         @dsl.component
         def dummy_op(msg: str = ''):
             pass
 
         with self.assertRaisesRegex(
                 RuntimeError,
-                'Task dummy-op cannot dependent on any task inside the group:'):
+                r'Tasks cannot depend on an upstream task inside'):
 
             @dsl.pipeline(name='test-pipeline')
             def my_pipeline(val: bool):
                 first_producer = producer_op()
                 with dsl.ExitHandler(first_producer):
                     producer_task = producer_op()
 
@@ -1486,9 +1492,833 @@
 
         # test pipeline interface
         self.assertEqual(
             pipeline_spec.root.input_definitions.parameters['boolean']
             .default_value.bool_value, True)
 
 
+# helper component defintions for the ValidLegalTopologies tests
+@dsl.component
+def print_op(message: str):
+    print(message)
+
+
+@dsl.component
+def return_1() -> int:
+    return 1
+
+
+@dsl.component
+def args_generator_op() -> List[Dict[str, str]]:
+    return [{'A_a': '1', 'B_b': '2'}, {'A_a': '10', 'B_b': '20'}]
+
+
+class TestValidLegalTopologies(unittest.TestCase):
+
+    def test_inside_of_root_group_permitted(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            return_1_task = return_1()
+
+            one = print_op(message='1')
+            two = print_op(message='2')
+            three = print_op(message=str(return_1_task.output))
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_upstream_inside_deeper_condition_blocked(self):
+
+        with self.assertRaisesRegex(
+                RuntimeError,
+                r'Tasks cannot depend on an upstream task inside'):
+
+            @dsl.pipeline()
+            def my_pipeline():
+                return_1_task = return_1()
+
+                one = print_op(message='1')
+                with dsl.Condition(return_1_task.output == 1):
+                    two = print_op(message='2')
+
+                three = print_op(message='3').after(two)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_upstream_in_the_same_condition_permitted(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            return_1_task = return_1()
+
+            with dsl.Condition(return_1_task.output == 1):
+                one = return_1()
+                two = print_op(message='2')
+                three = print_op(message=str(one.output))
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_inside_deeper_condition_permitted(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            return_1_task = return_1()
+
+            one = print_op(message='1')
+            with dsl.Condition(return_1_task.output == 1):
+                two = print_op(message='2')
+                three = print_op(message='3').after(one)
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_and_upstream_in_different_condition_on_same_level_blocked(
+            self):
+
+        with self.assertRaisesRegex(
+                RuntimeError,
+                r'Tasks cannot depend on an upstream task inside'):
+
+            @dsl.pipeline()
+            def my_pipeline():
+                return_1_task = return_1()
+
+                one = print_op(message='1')
+                with dsl.Condition(return_1_task.output == 1):
+                    two = print_op(message='2')
+
+                with dsl.Condition(return_1_task.output == 1):
+                    three = print_op(message='3').after(two)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_inside_deeper_nested_condition_permitted(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            return_1_task = return_1()
+            return_1_task2 = return_1()
+
+            with dsl.Condition(return_1_task.output == 1):
+                one = return_1()
+                with dsl.Condition(return_1_task2.output == 1):
+                    two = print_op(message='2')
+                    three = print_op(message=str(one.output))
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_upstream_inside_deeper_nested_condition_blocked(self):
+
+        with self.assertRaisesRegex(
+                RuntimeError,
+                r'Tasks cannot depend on an upstream task inside'):
+
+            @dsl.pipeline()
+            def my_pipeline():
+                return_1_task = return_1()
+
+                with dsl.Condition(return_1_task.output == 1):
+                    one = print_op(message='1')
+                    with dsl.Condition(return_1_task.output == 1):
+                        two = print_op(message='2')
+                    three = print_op(message='3').after(two)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_upstream_in_same_for_loop_with_downstream_permitted(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            args_generator = args_generator_op()
+
+            with dsl.ParallelFor(args_generator.output):
+                one = print_op(message='1')
+                two = print_op(message='3').after(one)
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_not_in_same_for_loop_with_upstream_blocked(self):
+
+        with self.assertRaisesRegex(
+                RuntimeError,
+                r'Tasks cannot depend on an upstream task inside'):
+
+            @dsl.pipeline()
+            def my_pipeline():
+                args_generator = args_generator_op()
+
+                with dsl.ParallelFor(args_generator.output):
+                    one = print_op(message='1')
+                two = print_op(message='3').after(one)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_not_in_same_for_loop_with_upstream_seperate_blocked(
+            self):
+
+        with self.assertRaisesRegex(
+                RuntimeError,
+                r'Tasks cannot depend on an upstream task inside'):
+
+            @dsl.pipeline()
+            def my_pipeline():
+                args_generator = args_generator_op()
+
+                with dsl.ParallelFor(args_generator.output):
+                    one = print_op(message='1')
+
+                with dsl.ParallelFor(args_generator.output):
+                    two = print_op(message='3').after(one)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_not_in_same_for_loop_with_upstream_nested_blocked(self):
+
+        with self.assertRaisesRegex(
+                RuntimeError,
+                r'Downstream tasks in a nested ParallelFor group cannot depend on an upstream task in a shallower ParallelFor group.'
+        ):
+
+            @dsl.pipeline()
+            def my_pipeline():
+                args_generator = args_generator_op()
+
+                with dsl.ParallelFor(args_generator.output):
+                    one = print_op(message='1')
+
+                    with dsl.ParallelFor(args_generator.output):
+                        two = print_op(message='3').after(one)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_in_condition_nested_in_a_for_loop(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            return_1_task = return_1()
+
+            with dsl.ParallelFor([1, 2, 3]):
+                one = print_op(message='1')
+                with dsl.Condition(return_1_task.output == 1):
+                    two = print_op(message='2').after(one)
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_in_a_for_loop_nested_in_a_condition(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            return_1_task = return_1()
+
+            with dsl.Condition(return_1_task.output == 1):
+                one = print_op(message='1')
+                with dsl.ParallelFor([1, 2, 3]):
+                    two = print_op(message='2').after(one)
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_downstream_in_a_nested_for_loop_not_related_to_upstream(self):
+
+        @dsl.pipeline()
+        def my_pipeline():
+            return_1_task = return_1()
+
+            with dsl.ParallelFor([1, 2, 3]):
+                one = print_op(message='1')
+                with dsl.ParallelFor([1, 2, 3]):
+                    two = print_op(message='2').after(return_1_task)
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+
+class TestCannotUseAfterCrossDAG(unittest.TestCase):
+
+    def test_inner_task_prevented(self):
+        with self.assertRaisesRegex(RuntimeError, r'Task'):
+
+            @dsl.component
+            def print_op(message: str):
+                print(message)
+
+            @dsl.pipeline(name='pipeline-with-multiple-exit-handlers')
+            def my_pipeline():
+                first_exit_task = print_op(message='First exit task.')
+
+                with dsl.ExitHandler(first_exit_task):
+                    first_print_op = print_op(
+                        message='Inside first exit handler.')
+
+                second_exit_task = print_op(message='Second exit task.')
+                with dsl.ExitHandler(second_exit_task):
+                    print_op(message='Inside second exit handler.').after(
+                        first_print_op)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_exit_handler_task_prevented(self):
+        with self.assertRaisesRegex(RuntimeError, r'Task'):
+
+            @dsl.component
+            def print_op(message: str):
+                print(message)
+
+            @dsl.pipeline(name='pipeline-with-multiple-exit-handlers')
+            def my_pipeline():
+                first_exit_task = print_op(message='First exit task.')
+
+                with dsl.ExitHandler(first_exit_task):
+                    first_print_op = print_op(
+                        message='Inside first exit handler.')
+
+                second_exit_task = print_op(message='Second exit task.')
+                with dsl.ExitHandler(second_exit_task):
+                    x = print_op(message='Inside second exit handler.')
+                    x.after(first_print_op)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_within_same_exit_handler_permitted(self):
+
+        @dsl.component
+        def print_op(message: str):
+            print(message)
+
+        @dsl.pipeline(name='pipeline-with-multiple-exit-handlers')
+        def my_pipeline():
+            first_exit_task = print_op(message='First exit task.')
+
+            with dsl.ExitHandler(first_exit_task):
+                first_print_op = print_op(
+                    message='First task inside first exit handler.')
+                second_print_op = print_op(
+                    message='Second task inside first exit handler.').after(
+                        first_print_op)
+
+            second_exit_task = print_op(message='Second exit task.')
+            with dsl.ExitHandler(second_exit_task):
+                print_op(message='Inside second exit handler.')
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_outside_of_condition_blocked(self):
+        with self.assertRaisesRegex(RuntimeError, r'Task'):
+
+            @dsl.component
+            def print_op(message: str):
+                print(message)
+
+            @dsl.component
+            def return_1() -> int:
+                return 1
+
+            @dsl.pipeline(name='pipeline-with-multiple-exit-handlers')
+            def my_pipeline():
+                return_1_task = return_1()
+
+                with dsl.Condition(return_1_task.output == 1):
+                    one = print_op(message='1')
+                    two = print_op(message='2')
+                three = print_op(message='3').after(one)
+
+            with tempfile.TemporaryDirectory() as tempdir:
+                package_path = os.path.join(tempdir, 'pipeline.yaml')
+                compiler.Compiler().compile(
+                    pipeline_func=my_pipeline, package_path=package_path)
+
+    def test_inside_of_condition_permitted(self):
+
+        @dsl.component
+        def print_op(message: str):
+            print(message)
+
+        @dsl.component
+        def return_1() -> int:
+            return 1
+
+        @dsl.pipeline(name='pipeline-with-multiple-exit-handlers')
+        def my_pipeline():
+            return_1_task = return_1()
+
+            with dsl.Condition(return_1_task.output == '1'):
+                one = print_op(message='1')
+                two = print_op(message='2').after(one)
+            three = print_op(message='3')
+
+        with tempfile.TemporaryDirectory() as tempdir:
+            package_path = os.path.join(tempdir, 'pipeline.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=package_path)
+
+
+class TestYamlComments(unittest.TestCase):
+
+    def test_comments_include_inputs_and_outputs_and_pipeline_name(self):
+
+        @dsl.component
+        def identity(string: str, model: bool) -> str:
+            return string
+
+        @dsl.pipeline()
+        def my_pipeline(sample_input1: bool = True,
+                        sample_input2: str = 'string') -> str:
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=pipeline_spec_path)
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        inputs_string = textwrap.dedent("""\
+                # Inputs:
+                #    sample_input1: bool [Default: True]
+                #    sample_input2: str [Default: 'string']
+                """)
+
+        outputs_string = textwrap.dedent("""\
+                # Outputs:
+                #    Output: str
+                """)
+
+        name_string = '# Name: my-pipeline'
+
+        self.assertIn(name_string, yaml_content)
+
+        self.assertIn(inputs_string, yaml_content)
+
+        self.assertIn(outputs_string, yaml_content)
+
+    def test_comments_include_definition(self):
+
+        @dsl.component
+        def identity(string: str, model: bool) -> str:
+            return string
+
+        @dsl.pipeline()
+        def pipeline_with_no_definition(sample_input1: bool = True,
+                                        sample_input2: str = 'string') -> str:
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=pipeline_with_no_definition,
+                package_path=pipeline_spec_path)
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+            description_string = '# Description:'
+
+        self.assertNotIn(description_string, yaml_content)
+
+        @dsl.pipeline()
+        def pipeline_with_definition(sample_input1: bool = True,
+                                     sample_input2: str = 'string') -> str:
+            """This is a definition of this pipeline."""
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=pipeline_with_definition,
+                package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+            description_string = '# Description:'
+
+        self.assertIn(description_string, yaml_content)
+
+    def test_comments_on_pipeline_with_no_inputs_or_outputs(self):
+
+        @dsl.component
+        def identity(string: str, model: bool) -> str:
+            return string
+
+        @dsl.pipeline()
+        def pipeline_with_no_inputs() -> str:
+            op1 = identity(string='string', model=True)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=pipeline_with_no_inputs,
+                package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        inputs_string = '# Inputs:'
+
+        self.assertNotIn(inputs_string, yaml_content)
+
+        @dsl.pipeline()
+        def pipeline_with_no_outputs(sample_input1: bool = True,
+                                     sample_input2: str = 'string'):
+            identity(string=sample_input2, model=sample_input1)
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=pipeline_with_no_outputs,
+                package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        outputs_string = '# Outputs:'
+
+        self.assertNotIn(outputs_string, yaml_content)
+
+    def test_comments_follow_pattern(self):
+
+        @dsl.component
+        def identity(string: str, model: bool) -> str:
+            return string
+
+        @dsl.pipeline()
+        def my_pipeline(sample_input1: bool = True,
+                        sample_input2: str = 'string') -> str:
+            """This is a definition of this pipeline."""
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        pattern_sample = textwrap.dedent("""\
+                # PIPELINE DEFINITION
+                # Name: my-pipeline
+                # Description: This is a definition of this pipeline.
+                # Inputs:
+                #    sample_input1: bool [Default: True]
+                #    sample_input2: str [Default: 'string']
+                # Outputs:
+                #    Output: str
+                """)
+
+        self.assertIn(pattern_sample, yaml_content)
+
+    def test_verbose_comment_characteristics(self):
+
+        @dsl.component
+        def output_model(metrics: Output[Model]):
+            """Dummy component that outputs metrics with a random accuracy."""
+            import random
+            result = random.randint(0, 100)
+            metrics.log_metric('accuracy', result)
+
+        @dsl.pipeline(name='Test pipeline')
+        def my_pipeline(sample_input1: bool,
+                        sample_input2: str,
+                        sample_input3: Input[Model],
+                        sample_input4: float = 3.14,
+                        sample_input5: list = [1],
+                        sample_input6: dict = {'one': 1},
+                        sample_input7: int = 5) -> Model:
+            """This is a definition of this pipeline."""
+
+            task = output_model()
+            return task.output
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        predicted_comment = textwrap.dedent("""\
+                # PIPELINE DEFINITION
+                # Name: test-pipeline
+                # Description: This is a definition of this pipeline.
+                # Inputs:
+                #    sample_input1: bool
+                #    sample_input2: str
+                #    sample_input3: system.Model
+                #    sample_input4: float [Default: 3.14]
+                #    sample_input5: list [Default: [1.0]]
+                #    sample_input6: dict [Default: {'one': 1.0}]
+                #    sample_input7: int [Default: 5.0]
+                # Outputs:
+                #    Output: system.Model
+                """)
+
+        self.assertIn(predicted_comment, yaml_content)
+
+    def test_comments_on_compiled_components(self):
+
+        @dsl.component
+        def my_component(string: str, model: bool) -> str:
+            """component description."""
+            return string
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_component, package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        predicted_comment = textwrap.dedent("""\
+                # PIPELINE DEFINITION
+                # Name: my-component
+                # Description: component description.
+                # Inputs:
+                #    model: bool
+                #    string: str
+                """)
+
+        self.assertIn(predicted_comment, yaml_content)
+
+        @dsl.container_component
+        def my_container_component(text: str, output_path: OutputPath(str)):
+            """component description."""
+            return ContainerSpec(
+                image='python:3.7',
+                command=['my_program', text],
+                args=['--output_path', output_path])
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_container_component,
+                package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        predicted_comment = textwrap.dedent("""\
+                # PIPELINE DEFINITION
+                # Name: my-container-component
+                # Description: component description.
+                # Inputs:
+                #    text: str
+                """)
+
+        self.assertIn(predicted_comment, yaml_content)
+
+    def test_comments_idempotency(self):
+
+        @dsl.component
+        def identity(string: str, model: bool) -> str:
+            return string
+
+        @dsl.pipeline()
+        def my_pipeline(sample_input1: bool = True,
+                        sample_input2: str = 'string') -> str:
+            """My description."""
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=pipeline_spec_path)
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+            comp = components.load_component_from_file(pipeline_spec_path)
+            compiler.Compiler().compile(
+                pipeline_func=comp, package_path=pipeline_spec_path)
+            with open(pipeline_spec_path, 'r+') as f:
+                reloaded_yaml_content = f.read()
+
+        predicted_comment = textwrap.dedent("""\
+                # PIPELINE DEFINITION
+                # Name: my-pipeline
+                # Description: My description.
+                # Inputs:
+                #    sample_input1: bool [Default: True]
+                #    sample_input2: str [Default: 'string']
+                # Outputs:
+                #    Output: str
+                """)
+
+        # test initial comments
+        self.assertIn(predicted_comment, yaml_content)
+
+        # test reloaded comments
+        self.assertIn(predicted_comment, reloaded_yaml_content)
+
+    def test_comment_with_multiline_docstring(self):
+
+        @dsl.component
+        def identity(string: str, model: bool) -> str:
+            return string
+
+        @dsl.pipeline()
+        def pipeline_with_multiline_definition(
+                sample_input1: bool = True,
+                sample_input2: str = 'string') -> str:
+            """docstring short description.
+            docstring long description. docstring long description.
+            """
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=pipeline_with_multiline_definition,
+                package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        description_string = textwrap.dedent("""\
+            # Description: docstring short description.
+            #              docstring long description. docstring long description.
+            """)
+
+        self.assertIn(description_string, yaml_content)
+
+        @dsl.pipeline()
+        def pipeline_with_multiline_definition(
+                sample_input1: bool = True,
+                sample_input2: str = 'string') -> str:
+            """
+            docstring long description.
+            docstring long description.
+            docstring long description.
+            """
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=pipeline_with_multiline_definition,
+                package_path=pipeline_spec_path)
+
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+
+        description_string = textwrap.dedent("""\
+            # Description: docstring long description.
+            #              docstring long description.
+            #              docstring long description.
+            """)
+
+        self.assertIn(description_string, yaml_content)
+
+    def test_idempotency_on_comment_with_multiline_docstring(self):
+
+        @dsl.component
+        def identity(string: str, model: bool) -> str:
+            return string
+
+        @dsl.pipeline()
+        def my_pipeline(sample_input1: bool = True,
+                        sample_input2: str = 'string') -> str:
+            """docstring short description.
+            docstring long description.
+            docstring long description.
+            """
+            op1 = identity(string=sample_input2, model=sample_input1)
+            result = op1.output
+            return result
+
+        with tempfile.TemporaryDirectory() as tmpdir:
+            pipeline_spec_path = os.path.join(tmpdir, 'output.yaml')
+            compiler.Compiler().compile(
+                pipeline_func=my_pipeline, package_path=pipeline_spec_path)
+            with open(pipeline_spec_path, 'r+') as f:
+                yaml_content = f.read()
+            comp = components.load_component_from_file(pipeline_spec_path)
+            compiler.Compiler().compile(
+                pipeline_func=comp, package_path=pipeline_spec_path)
+            with open(pipeline_spec_path, 'r+') as f:
+                reloaded_yaml_content = f.read()
+
+        predicted_comment = textwrap.dedent("""\
+                # PIPELINE DEFINITION
+                # Name: my-pipeline
+                # Description: docstring short description.
+                #              docstring long description.
+                #              docstring long description.
+                # Inputs:
+                #    sample_input1: bool [Default: True]
+                #    sample_input2: str [Default: 'string']
+                # Outputs:
+                #    Output: str
+                """)
+
+        # test initial comments
+        self.assertIn(predicted_comment, yaml_content)
+
+        # test reloaded comments
+        self.assertIn(predicted_comment, reloaded_yaml_content)
+
+
 if __name__ == '__main__':
     unittest.main()
```

### Comparing `kfp-2.0.0b8/kfp/compiler/compiler_utils.py` & `kfp-2.0.0b9/kfp/compiler/compiler_utils.py`

 * *Files 6% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 """Utility methods for compiler implementation that is IR-agnostic."""
 
 import collections
+from copy import deepcopy
 from typing import Dict, List, Mapping, Set, Tuple, Union
 
 from kfp.components import for_loop
 from kfp.components import pipeline_channel
 from kfp.components import pipeline_context
 from kfp.components import pipeline_task
 from kfp.components import tasks_group
@@ -423,19 +424,47 @@
             upstream_groups, downstream_groups = _get_uncommon_ancestors(
                 task_name_to_parent_groups=task_name_to_parent_groups,
                 group_name_to_parent_groups=group_name_to_parent_groups,
                 task1=upstream_task,
                 task2=task,
             )
 
-            # a task cannot depend on a task created in a for loop group since individual PipelineTask variables are reassigned after each loop iteration
-            dependent_group = group_name_to_group.get(upstream_groups[0], None)
-            if isinstance(dependent_group,
-                          (tasks_group.ParallelFor, tasks_group.Condition,
-                           tasks_group.ExitHandler)):
+            # uncommon upstream ancestor check
+            uncommon_upstream_groups = deepcopy(upstream_groups)
+            uncommon_upstream_groups.remove(
+                upstream_task.name
+            )  # because a task's `upstream_groups` contains the task's name
+            if uncommon_upstream_groups:
+                dependent_group = group_name_to_group.get(
+                    uncommon_upstream_groups[0], None)
+                if isinstance(dependent_group, tasks_group.ExitHandler):
+                    task_group_type = 'an ' + tasks_group.ExitHandler.__name__
+
+                elif isinstance(dependent_group, tasks_group.Condition):
+                    task_group_type = 'a ' + tasks_group.Condition.__name__
+
+                else:
+                    task_group_type = 'a ' + tasks_group.ParallelFor.__name__
+
                 raise RuntimeError(
-                    f'Task {task.name} cannot dependent on any task inside'
-                    f' the group: {upstream_groups[0]}.')
+                    f'Tasks cannot depend on an upstream task inside {task_group_type} that is not a common ancestor of both tasks. Task {task.name} depends on upstream task {upstream_task.name}.'
+                )
+
+            # ParralelFor Nested Check
+            # if there is a parrallelFor group type in the upstream parents tasks and there also exists a parallelFor in the uncommon_ancestors of downstream: this means a nested for loop exists in the DAG
+            upstream_parent_tasks = task_name_to_parent_groups[
+                upstream_task.name]
+            for group in downstream_groups:
+                if isinstance(
+                        group_name_to_group.get(group, None),
+                        tasks_group.ParallelFor):
+                    for parent_task in upstream_parent_tasks:
+                        if isinstance(
+                                group_name_to_group.get(parent_task, None),
+                                tasks_group.ParallelFor):
+                            raise RuntimeError(
+                                f'Downstream tasks in a nested {tasks_group.ParallelFor.__name__} group cannot depend on an upstream task in a shallower {tasks_group.ParallelFor.__name__} group. Task {task.name} depends on upstream task {upstream_task.name}, while {group} is nested in {parent_task}.'
+                            )
 
             dependencies[downstream_groups[0]].add(upstream_groups[0])
 
     return dependencies
```

### Comparing `kfp-2.0.0b8/kfp/compiler/pipeline_spec_builder.py` & `kfp-2.0.0b9/kfp/compiler/pipeline_spec_builder.py`

 * *Files 2% similar despite different names*

```diff
@@ -151,16 +151,15 @@
                             input_value.name)
                 else:
                     # Dependent task not from the same DAG.
                     component_input_artifact = (
                         _additional_input_name_for_pipeline_channel(input_value)
                     )
                     assert component_input_artifact in parent_component_inputs.artifacts, \
-                        'component_input_artifact: {} not found. All inputs: {}'.format(
-                            component_input_artifact, parent_component_inputs)
+                        f'component_input_artifact: {component_input_artifact} not found. All inputs: {parent_component_inputs}'
                     pipeline_task_spec.inputs.artifacts[
                         input_name].component_input_artifact = (
                             component_input_artifact)
             else:
                 component_input_artifact = input_value.full_name
                 if component_input_artifact not in parent_component_inputs.artifacts:
                     component_input_artifact = (
@@ -184,16 +183,15 @@
                             input_value.name)
                 else:
                     # Dependent task not from the same DAG.
                     component_input_parameter = (
                         _additional_input_name_for_pipeline_channel(input_value)
                     )
                     assert component_input_parameter in parent_component_inputs.parameters, \
-                        'component_input_parameter: {} not found. All inputs: {}'.format(
-                            component_input_parameter, parent_component_inputs)
+                        f'component_input_parameter: {component_input_parameter} not found. All inputs: {parent_component_inputs}'
                     pipeline_task_spec.inputs.parameters[
                         input_name].component_input_parameter = (
                             component_input_parameter)
             else:
                 # Value is from pipeline input.
                 component_input_parameter = input_value.full_name
                 if component_input_parameter not in parent_component_inputs.parameters:
@@ -205,35 +203,32 @@
                         component_input_parameter)
 
         elif isinstance(input_value, for_loop.LoopArgument):
 
             component_input_parameter = (
                 _additional_input_name_for_pipeline_channel(input_value))
             assert component_input_parameter in parent_component_inputs.parameters, \
-                'component_input_parameter: {} not found. All inputs: {}'.format(
-                    component_input_parameter, parent_component_inputs)
+                f'component_input_parameter: {component_input_parameter} not found. All inputs: {parent_component_inputs}'
             pipeline_task_spec.inputs.parameters[
                 input_name].component_input_parameter = (
                     component_input_parameter)
 
         elif isinstance(input_value, for_loop.LoopArgumentVariable):
 
             component_input_parameter = (
                 _additional_input_name_for_pipeline_channel(
                     input_value.loop_argument))
             assert component_input_parameter in parent_component_inputs.parameters, \
-                'component_input_parameter: {} not found. All inputs: {}'.format(
-                    component_input_parameter, parent_component_inputs)
+                f'component_input_parameter: {component_input_parameter} not found. All inputs: {parent_component_inputs}'
             pipeline_task_spec.inputs.parameters[
                 input_name].component_input_parameter = (
                     component_input_parameter)
             pipeline_task_spec.inputs.parameters[
                 input_name].parameter_expression_selector = (
-                    'parseJson(string_value)["{}"]'.format(
-                        input_value.subvar_name))
+                    f'parseJson(string_value)["{input_value.subvar_name}"]')
 
         elif isinstance(input_value, str):
             # Handle extra input due to string concat
             pipeline_channels = (
                 pipeline_channel.extract_pipeline_channels_from_any(input_value)
             )
             for channel in pipeline_channels:
@@ -248,17 +243,16 @@
                 # We don't expect collision to happen because we prefix the name
                 # of additional input with 'pipelinechannel--'. But just in case
                 # collision did happend, throw a RuntimeError so that we don't
                 # get surprise at runtime.
                 for existing_input_name, _ in task.inputs.items():
                     if existing_input_name == additional_input_name:
                         raise RuntimeError(
-                            'Name collision between existing input name '
-                            '{} and compiler injected input name {}'.format(
-                                existing_input_name, additional_input_name))
+                            f'Name collision between existing input name {existing_input_name} and compiler injected input name {additional_input_name}'
+                        )
 
                 additional_input_placeholder = placeholders.InputValuePlaceholder(
                     additional_input_name)._to_string()
                 input_value = input_value.replace(channel.pattern,
                                                   additional_input_placeholder)
 
                 if channel.task_name:
@@ -273,16 +267,15 @@
                                 channel.name)
                     else:
                         # Dependent task not from the same DAG.
                         component_input_parameter = (
                             _additional_input_name_for_pipeline_channel(channel)
                         )
                         assert component_input_parameter in parent_component_inputs.parameters, \
-                            'component_input_parameter: {} not found. All inputs: {}'.format(
-                                component_input_parameter, parent_component_inputs)
+                            f'component_input_parameter: {component_input_parameter} not found. All inputs: {parent_component_inputs}'
                         pipeline_task_spec.inputs.parameters[
                             additional_input_name].component_input_parameter = (
                                 component_input_parameter)
                 else:
                     # Value is from pipeline input. (or loop?)
                     component_input_parameter = channel.full_name
                     if component_input_parameter not in parent_component_inputs.parameters:
@@ -675,30 +668,29 @@
     if group.items_is_pipeline_channel:
         loop_items_channel = group.loop_argument.items_or_pipeline_channel
         input_parameter_name = _additional_input_name_for_pipeline_channel(
             loop_items_channel)
         loop_argument_item_name = _additional_input_name_for_pipeline_channel(
             group.loop_argument.full_name)
 
-        loop_arguments_item = '{}-{}'.format(
-            input_parameter_name, for_loop.LoopArgument.LOOP_ITEM_NAME_BASE)
+        loop_arguments_item = f'{input_parameter_name}-{for_loop.LoopArgument.LOOP_ITEM_NAME_BASE}'
         assert loop_arguments_item == loop_argument_item_name
 
         pipeline_task_spec.parameter_iterator.items.input_parameter = (
             input_parameter_name)
         pipeline_task_spec.parameter_iterator.item_input = (
             loop_argument_item_name)
 
         # If the loop items itself is a loop arguments variable, handle the
         # subvar name.
         if isinstance(loop_items_channel, for_loop.LoopArgumentVariable):
             pipeline_task_spec.inputs.parameters[
                 input_parameter_name].parameter_expression_selector = (
-                    'parseJson(string_value)["{}"]'.format(
-                        loop_items_channel.subvar_name))
+                    f'parseJson(string_value)["{loop_items_channel.subvar_name}"]'
+                )
             pipeline_task_spec.inputs.parameters[
                 input_parameter_name].component_input_parameter = (
                     _additional_input_name_for_pipeline_channel(
                         loop_items_channel.loop_argument))
 
     else:
         input_parameter_name = _additional_input_name_for_pipeline_channel(
@@ -743,19 +735,17 @@
                     pipeline_spec_pb2.ParameterType.STRUCT,
                     pipeline_spec_pb2.ParameterType.LIST,
                     pipeline_spec_pb2.ParameterType
                     .PARAMETER_TYPE_ENUM_UNSPECIFIED,
             ]:
                 input_name = _additional_input_name_for_pipeline_channel(
                     value_or_reference)
-                raise ValueError('Conditional requires scalar parameter values'
-                                 ' for comparison. Found input "{}" of type {}'
-                                 ' in pipeline definition instead.'.format(
-                                     input_name,
-                                     value_or_reference.channel_type))
+                raise ValueError(
+                    f'Conditional requires scalar parameter values for comparison. Found input "{input_name}" of type {value_or_reference.channel_type} in pipeline definition instead.'
+                )
     parameter_types = set()
     for value_or_reference in [left_operand, right_operand]:
         if isinstance(value_or_reference, pipeline_channel.PipelineChannel):
             parameter_type = type_utils.get_parameter_type(
                 value_or_reference.channel_type)
         else:
             parameter_type = type_utils.get_parameter_type(
@@ -771,40 +761,38 @@
         if pipeline_spec_pb2.ParameterType.STRING in parameter_types:
             canonical_parameter_type = pipeline_spec_pb2.ParameterType.STRING
         elif pipeline_spec_pb2.ParameterType.BOOLEAN in parameter_types:
             canonical_parameter_type = pipeline_spec_pb2.ParameterType.BOOLEAN
         else:
             # Must be a double and int, promote to double.
             assert pipeline_spec_pb2.ParameterType.NUMBER_DOUBLE in parameter_types, \
-                'Types: {} [{} {}]'.format(
-                parameter_types, left_operand, right_operand)
+                f'Types: {parameter_types} [{left_operand} {right_operand}]'
             assert pipeline_spec_pb2.ParameterType.NUMBER_INTEGER in parameter_types, \
-                'Types: {} [{} {}]'.format(
-                parameter_types, left_operand, right_operand)
+                f'Types: {parameter_types} [{left_operand} {right_operand}]'
             canonical_parameter_type = pipeline_spec_pb2.ParameterType.NUMBER_DOUBLE
     elif len(parameter_types) == 1:  # Both operands are the same type.
         canonical_parameter_type = parameter_types.pop()
     else:
         # Probably shouldn't happen.
-        raise ValueError('Unable to determine operand types for'
-                         ' "{}" and "{}"'.format(left_operand, right_operand))
+        raise ValueError(
+            f'Unable to determine operand types for "{left_operand}" and "{right_operand}"'
+        )
 
     operand_values = []
     for value_or_reference in [left_operand, right_operand]:
         if isinstance(value_or_reference, pipeline_channel.PipelineChannel):
             input_name = _additional_input_name_for_pipeline_channel(
                 value_or_reference)
-            operand_value = "inputs.parameter_values['{input_name}']".format(
-                input_name=input_name)
+            operand_value = f"inputs.parameter_values['{input_name}']"
             parameter_type = type_utils.get_parameter_type(
                 value_or_reference.channel_type)
             if parameter_type == pipeline_spec_pb2.ParameterType.NUMBER_INTEGER:
-                operand_value = 'int({})'.format(operand_value)
+                operand_value = f'int({operand_value})'
         elif isinstance(value_or_reference, str):
-            operand_value = "'{}'".format(value_or_reference)
+            operand_value = f"'{value_or_reference}'"
             parameter_type = pipeline_spec_pb2.ParameterType.STRING
         elif isinstance(value_or_reference, bool):
             # Booleans need to be compared as 'true' or 'false' in CEL.
             operand_value = str(value_or_reference).lower()
             parameter_type = pipeline_spec_pb2.ParameterType.BOOLEAN
         elif isinstance(value_or_reference, int):
             operand_value = str(value_or_reference)
@@ -818,25 +806,25 @@
             # Type-cast to so CEL does not complain.
             if canonical_parameter_type == pipeline_spec_pb2.ParameterType.STRING:
                 assert parameter_type in [
                     pipeline_spec_pb2.ParameterType.BOOLEAN,
                     pipeline_spec_pb2.ParameterType.NUMBER_INTEGER,
                     pipeline_spec_pb2.ParameterType.NUMBER_DOUBLE,
                 ]
-                operand_value = "'{}'".format(operand_value)
+                operand_value = f"'{operand_value}'"
             elif canonical_parameter_type == pipeline_spec_pb2.ParameterType.BOOLEAN:
                 assert parameter_type in [
                     pipeline_spec_pb2.ParameterType.NUMBER_INTEGER,
                     pipeline_spec_pb2.ParameterType.NUMBER_DOUBLE,
                 ]
                 operand_value = 'true' if int(operand_value) == 0 else 'false'
             else:
                 assert canonical_parameter_type == pipeline_spec_pb2.ParameterType.NUMBER_DOUBLE
                 assert parameter_type == pipeline_spec_pb2.ParameterType.NUMBER_INTEGER
-                operand_value = 'double({})'.format(operand_value)
+                operand_value = f'double({operand_value})'
 
         operand_values.append(operand_value)
 
     return tuple(operand_values)
 
 
 def _update_task_spec_for_condition_group(
@@ -927,15 +915,15 @@
 
         input_name = _additional_input_name_for_pipeline_channel(channel)
 
         channel_name = channel.name
         if subvar_name:
             pipeline_task_spec.inputs.parameters[
                 input_name].parameter_expression_selector = (
-                    'parseJson(string_value)["{}"]'.format(subvar_name))
+                    f'parseJson(string_value)["{subvar_name}"]')
             if not channel.is_with_items_loop_argument:
                 channel_name = channel.items_or_pipeline_channel.name
 
         if isinstance(channel, pipeline_channel.PipelineArtifactChannel):
             if channel.task_name and channel.task_name in tasks_in_current_dag:
                 pipeline_task_spec.inputs.artifacts[
                     input_name].task_output_artifact.producer_task = (
@@ -944,30 +932,27 @@
                     input_name].task_output_artifact.output_artifact_key = (
                         channel_name)
             else:
                 pipeline_task_spec.inputs.artifacts[
                     input_name].component_input_artifact = (
                         channel_full_name
                         if is_parent_component_root else input_name)
+        elif channel.task_name and channel.task_name in tasks_in_current_dag:
+            pipeline_task_spec.inputs.parameters[
+                input_name].task_output_parameter.producer_task = (
+                    utils.sanitize_task_name(channel.task_name))
+            pipeline_task_spec.inputs.parameters[
+                input_name].task_output_parameter.output_parameter_key = (
+                    channel_name)
         else:
-            # channel is one of PipelineParameterChannel, LoopArgument, or
-            # LoopArgumentVariable
-            if channel.task_name and channel.task_name in tasks_in_current_dag:
-                pipeline_task_spec.inputs.parameters[
-                    input_name].task_output_parameter.producer_task = (
-                        utils.sanitize_task_name(channel.task_name))
-                pipeline_task_spec.inputs.parameters[
-                    input_name].task_output_parameter.output_parameter_key = (
-                        channel_name)
-            else:
-                pipeline_task_spec.inputs.parameters[
-                    input_name].component_input_parameter = (
-                        channel_full_name if is_parent_component_root else
-                        _additional_input_name_for_pipeline_channel(
-                            channel_full_name))
+            pipeline_task_spec.inputs.parameters[
+                input_name].component_input_parameter = (
+                    channel_full_name if is_parent_component_root else
+                    _additional_input_name_for_pipeline_channel(
+                        channel_full_name))
 
     if isinstance(group, tasks_group.ParallelFor):
         _update_task_spec_for_loop_group(
             group=group,
             pipeline_task_spec=pipeline_task_spec,
         )
     elif isinstance(group, tasks_group.Condition):
@@ -1015,15 +1000,15 @@
 
             if artifact_spec.artifact_type.WhichOneof(
                     'kind'
             ) == 'schema_title' and artifact_spec.artifact_type.schema_title in [
                     artifact_types.Metrics.schema_title,
                     artifact_types.ClassificationMetrics.schema_title,
             ]:
-                unique_output_name = '{}-{}'.format(task.name, output_name)
+                unique_output_name = f'{task.name}-{output_name}'
 
                 sub_task_name = task.name
                 sub_task_output = output_name
                 for component_name, task_name in parent_components_and_tasks:
                     group_component_spec = (
                         pipeline_spec.root if component_name == '_root' else
                         pipeline_spec.components[component_name])
@@ -1071,16 +1056,17 @@
         if input_name in pipeline_spec.root.input_definitions.parameters:
             _fill_in_component_input_default_value(pipeline_spec.root,
                                                    input_name, input_value)
         elif input_name in pipeline_spec.root.input_definitions.artifacts:
             raise NotImplementedError(
                 'Default value for artifact input is not supported.')
         else:
-            raise ValueError('Pipeline parameter {} does not match any known '
-                             'pipeline input.'.format(input_name))
+            raise ValueError(
+                f'Pipeline parameter {input_name} does not match any known pipeline input.'
+            )
 
     return pipeline_spec
 
 
 def build_spec_by_group(
     pipeline_spec: pipeline_spec_pb2.PipelineSpec,
     deployment_config: pipeline_spec_pb2.PipelineDeploymentConfig,
@@ -1600,34 +1586,118 @@
         deployment_config=deployment_config,
     )
 
     return pipeline_spec
 
 
 def write_pipeline_spec_to_file(pipeline_spec: pipeline_spec_pb2.PipelineSpec,
+                                pipeline_description: str,
                                 package_path: str) -> None:
     """Writes PipelineSpec into a YAML or JSON (deprecated) file.
 
     Args:
         pipeline_spec (pipeline_spec_pb2.PipelineSpec): The PipelineSpec.
         package_path (str): The path to which to write the PipelineSpec.
     """
     json_dict = json_format.MessageToDict(pipeline_spec)
+    yaml_comments = extract_comments_from_pipeline_spec(json_dict,
+                                                        pipeline_description)
 
     if package_path.endswith('.json'):
         warnings.warn(
             ('Compiling to JSON is deprecated and will be '
              'removed in a future version. Please compile to a YAML file by '
              'providing a file path with a .yaml extension instead.'),
             category=DeprecationWarning,
             stacklevel=2,
         )
         with open(package_path, 'w') as json_file:
             json.dump(json_dict, json_file, indent=2, sort_keys=True)
 
     elif package_path.endswith(('.yaml', '.yml')):
         with open(package_path, 'w') as yaml_file:
+            yaml_file.write(yaml_comments)
             yaml.dump(json_dict, yaml_file, sort_keys=True)
 
     else:
         raise ValueError(
             f'The output path {package_path} should end with ".yaml".')
+
+
+def extract_comments_from_pipeline_spec(pipeline_spec: dict,
+                                        pipeline_description: str) -> str:
+    map_parameter_types = {
+        'NUMBER_INTEGER': int.__name__,
+        'NUMBER_DOUBLE': float.__name__,
+        'STRING': str.__name__,
+        'BOOLEAN': bool.__name__,
+        'LIST': list.__name__,
+        'STRUCT': dict.__name__
+    }
+
+    map_headings = {
+        'inputDefinitions': '# Inputs:',
+        'outputDefinitions': '# Outputs:'
+    }
+
+    def collect_pipeline_signatures(root_dict: dict,
+                                    signature_type: str) -> List[str]:
+        comment_strings = []
+        if signature_type in root_dict:
+            signature = root_dict[signature_type]
+            comment_strings.append(map_headings[signature_type])
+
+            # Collect data
+            array_of_signatures = []
+            for parameter_name, parameter_body in signature.get(
+                    'parameters', {}).items():
+                data = {}
+                data['name'] = parameter_name
+                data['parameterType'] = map_parameter_types[
+                    parameter_body['parameterType']]
+                if 'defaultValue' in signature['parameters'][parameter_name]:
+                    data['defaultValue'] = signature['parameters'][
+                        parameter_name]['defaultValue']
+                    if isinstance(data['defaultValue'], str):
+                        data['defaultValue'] = "'" + data['defaultValue'] + "'"
+                array_of_signatures.append(data)
+
+            for artifact_name, artifact_body in signature.get('artifacts',
+                                                              {}).items():
+                data = {
+                    'name':
+                        artifact_name,
+                    'parameterType':
+                        artifact_body['artifactType']['schemaTitle']
+                }
+                array_of_signatures.append(data)
+
+            array_of_signatures = sorted(
+                array_of_signatures, key=lambda d: d.get('name'))
+
+            # Present data
+            for signature in array_of_signatures:
+                string = '#    ' + signature['name'] + ': ' + signature[
+                    'parameterType']
+                if 'defaultValue' in signature:
+                    string += ' [Default: ' + str(
+                        signature['defaultValue']) + ']'
+                comment_strings.append(string)
+
+        return comment_strings
+
+    multi_line_description_prefix = '#              '
+    comment_sections = []
+    comment_sections.append('# PIPELINE DEFINITION')
+    comment_sections.append('# Name: ' + pipeline_spec['pipelineInfo']['name'])
+    if pipeline_description:
+        pipeline_description = f'\n{multi_line_description_prefix}'.join(
+            pipeline_description.splitlines())
+        comment_sections.append('# Description: ' + pipeline_description)
+    comment_sections.extend(
+        collect_pipeline_signatures(pipeline_spec['root'], 'inputDefinitions'))
+    comment_sections.extend(
+        collect_pipeline_signatures(pipeline_spec['root'], 'outputDefinitions'))
+
+    comment = '\n'.join(comment_sections) + '\n'
+
+    return comment
```

### Comparing `kfp-2.0.0b8/kfp/compiler/pipeline_spec_builder_test.py` & `kfp-2.0.0b9/kfp/compiler/pipeline_spec_builder_test.py`

 * *Files 6% similar despite different names*

```diff
@@ -9,16 +9,14 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 """Tests for kfp.compiler.pipeline_spec_builder."""
 
-import os
-import tempfile
 import unittest
 
 from absl.testing import parameterized
 from google.protobuf import json_format
 from google.protobuf import struct_pb2
 from kfp.compiler import pipeline_spec_builder
 from kfp.components import pipeline_channel
@@ -255,50 +253,9 @@
 
 def pipeline_spec_from_file(filepath: str) -> str:
     with open(filepath, 'r') as f:
         dictionary = yaml.safe_load(f)
     return json_format.ParseDict(dictionary, pipeline_spec_pb2.PipelineSpec())
 
 
-class TestWriteIrToFile(unittest.TestCase):
-
-    @classmethod
-    def setUpClass(cls) -> None:
-        pipeline_spec = pipeline_spec_pb2.PipelineSpec()
-        pipeline_spec.pipeline_info.name = 'pipeline-name'
-        cls.pipeline_spec = pipeline_spec
-
-    def test_yaml(self):
-        with tempfile.TemporaryDirectory() as tempdir:
-            temp_filepath = os.path.join(tempdir, 'output.yaml')
-            pipeline_spec_builder.write_pipeline_spec_to_file(
-                self.pipeline_spec, temp_filepath)
-            actual = pipeline_spec_from_file(temp_filepath)
-        self.assertEqual(actual, self.pipeline_spec)
-
-    def test_yml(self):
-        with tempfile.TemporaryDirectory() as tempdir:
-            temp_filepath = os.path.join(tempdir, 'output.yml')
-            pipeline_spec_builder.write_pipeline_spec_to_file(
-                self.pipeline_spec, temp_filepath)
-            actual = pipeline_spec_from_file(temp_filepath)
-        self.assertEqual(actual, self.pipeline_spec)
-
-    def test_json(self):
-        with tempfile.TemporaryDirectory() as tempdir, self.assertWarnsRegex(
-                DeprecationWarning, r'Compiling to JSON is deprecated'):
-            temp_filepath = os.path.join(tempdir, 'output.json')
-            pipeline_spec_builder.write_pipeline_spec_to_file(
-                self.pipeline_spec, temp_filepath)
-            actual = pipeline_spec_from_file(temp_filepath)
-        self.assertEqual(actual, self.pipeline_spec)
-
-    def test_incorrect_extension(self):
-        with tempfile.TemporaryDirectory() as tempdir, self.assertRaisesRegex(
-                ValueError, r'should end with "\.yaml"\.'):
-            temp_filepath = os.path.join(tempdir, 'output.txt')
-            pipeline_spec_builder.write_pipeline_spec_to_file(
-                self.pipeline_spec, temp_filepath)
-
-
 if __name__ == '__main__':
     unittest.main()
```

### Comparing `kfp-2.0.0b8/kfp/compiler/read_write_test.py` & `kfp-2.0.0b9/kfp/compiler/read_write_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/__init__.py` & `kfp-2.0.0b9/kfp/components/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/base_component.py` & `kfp-2.0.0b9/kfp/components/base_component.py`

 * *Files 16% similar despite different names*

```diff
@@ -35,14 +35,15 @@
         """Init function for BaseComponent.
 
         Args:
           component_spec: The component definition.
         """
         self.component_spec = component_spec
         self.name = component_spec.name
+        self.description = component_spec.description or None
 
         # Arguments typed as PipelineTaskFinalStatus are special arguments that
         # do not count as user inputs. Instead, they are reserved to for the
         # (backend) system to pass a value.
         self._component_inputs = {
             input_name for input_name, input_spec in (
                 self.component_spec.inputs or {}).items()
@@ -53,15 +54,15 @@
         """Creates a PipelineTask object.
 
         The arguments are generated on the fly based on component input
         definitions.
         """
         task_inputs = {}
 
-        if len(args) > 0:
+        if args:
             raise TypeError(
                 'Components must be instantiated using keyword arguments. Positional '
                 f'parameters are not allowed (found {len(args)} such parameters for '
                 f'component "{self.name}").')
 
         for k, v in kwargs.items():
             if k not in self._component_inputs:
@@ -81,21 +82,40 @@
                 missing_arguments) == 1 else 'arguments'
             arguments = ', '.join(missing_arguments)
 
             raise TypeError(
                 f'{self.name}() missing {len(missing_arguments)} required '
                 f'{argument_or_arguments}: {arguments}.')
 
-        return pipeline_task.create_pipeline_task(
+        return pipeline_task.PipelineTask(
             component_spec=self.component_spec,
             args=task_inputs,
         )
 
     @property
     def pipeline_spec(self) -> pipeline_spec_pb2.PipelineSpec:
         """Returns the pipeline spec of the component."""
-        return self.component_spec.to_pipeline_spec()
+        with BlockPipelineTaskRegistration():
+            return self.component_spec.to_pipeline_spec()
 
     @abc.abstractmethod
     def execute(self, **kwargs):
         """Executes the component locally if implemented by the inheriting
         subclass."""
+
+
+class BlockPipelineTaskRegistration:
+    """Temporarily stop registering tasks to the default pipeline.
+
+    Handles special, uncommon functions that decorate and mutate a
+    component, possibly by using the component's .pipeline_spec
+    attribute. This is exhibited in the version of
+    google_cloud_pipeline_components compatible with KFP SDK v2.
+    """
+
+    # TODO: this handles the special case of a compiled component (when compiled inside a pipeline), which should not have any concept of a default pipeline. Perhaps there is a way to unify component/pipeline compilation concepts to remove this workaround?
+
+    def __enter__(self):
+        self.task_handler, pipeline_task.PipelineTask._register_task_handler = pipeline_task.PipelineTask._register_task_handler, pipeline_task._register_task_handler
+
+    def __exit__(self, *args):
+        pipeline_task.PipelineTask._register_task_handler = self.task_handler
```

### Comparing `kfp-2.0.0b8/kfp/components/component_decorator.py` & `kfp-2.0.0b9/kfp/components/component_decorator.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/component_decorator_test.py` & `kfp-2.0.0b9/kfp/components/component_decorator_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/component_factory.py` & `kfp-2.0.0b9/kfp/components/component_factory.py`

 * *Files 8% similar despite different names*

```diff
@@ -102,15 +102,15 @@
         index_url_options=index_url_options,
         concat_package_list=concat_package_list)
     return ['sh', '-c', install_python_packages_script]
 
 
 def _get_default_kfp_package_path() -> str:
     import kfp
-    return 'kfp=={}'.format(kfp.__version__)
+    return f'kfp=={kfp.__version__}'
 
 
 def _get_function_source_definition(func: Callable) -> str:
     func_code = inspect.getsource(func)
 
     # Function might be defined in some indented scope (e.g. in another
     # function). We need to handle this and properly dedent the function source
@@ -121,30 +121,30 @@
     # Removing possible decorators (can be multiline) until the function
     # definition is found
     func_code_lines = itertools.dropwhile(lambda x: not x.startswith('def'),
                                           func_code_lines)
 
     if not func_code_lines:
         raise ValueError(
-            'Failed to dedent and clean up the source of function "{}". '
-            'It is probably not properly indented.'.format(func.__name__))
+            f'Failed to dedent and clean up the source of function "{func.__name__}". It is probably not properly indented.'
+        )
 
     return '\n'.join(func_code_lines)
 
 
 def _maybe_make_unique(name: str, names: List[str]):
     if name not in names:
         return name
 
     for i in range(2, 100):
-        unique_name = '{}_{}'.format(name, i)
+        unique_name = f'{name}_{i}'
         if unique_name not in names:
             return unique_name
 
-    raise RuntimeError('Too many arguments with the name {}'.format(name))
+    raise RuntimeError(f'Too many arguments with the name {name}')
 
 
 def extract_component_interface(
         func: Callable,
         containerized: bool = False) -> structures.ComponentSpec:
     single_output_name_const = 'Output'
 
@@ -160,28 +160,31 @@
     output_names = set()
     for parameter in parameters:
         parameter_type = type_annotations.maybe_strip_optional_from_annotation(
             parameter.annotation)
         passing_style = None
         io_name = parameter.name
 
-        if type_annotations.is_artifact_annotation(parameter_type):
+        if type_annotations.is_Input_Output_artifact_annotation(parameter_type):
             # passing_style is either type_annotations.InputAnnotation or
             # type_annotations.OutputAnnotation.
             passing_style = type_annotations.get_io_artifact_annotation(
                 parameter_type)
 
-            # parameter_type is type_annotations.Artifact or one of its subclasses.
+            # parameter_type is a type like typing_extensions.Annotated[kfp.components.types.artifact_types.Artifact, <class 'kfp.components.types.type_annotations.OutputAnnotation'>] OR typing_extensions.Annotated[typing.List[kfp.components.types.artifact_types.Artifact], <class 'kfp.components.types.type_annotations.OutputAnnotation'>]
+
+            is_artifact_list = type_annotations.is_list_of_artifacts(
+                parameter_type.__origin__)
+
             parameter_type = type_annotations.get_io_artifact_class(
                 parameter_type)
             if not type_annotations.is_artifact_class(parameter_type):
                 raise ValueError(
-                    'Input[T] and Output[T] are only supported when T is a '
-                    'subclass of Artifact. Found `{} with type {}`'.format(
-                        io_name, parameter_type))
+                    f'Input[T] and Output[T] are only supported when T is an artifact or list of artifacts. Found `{io_name} with type {parameter_type}`'
+                )
 
             if parameter.default is not inspect.Parameter.empty:
                 raise ValueError(
                     'Default values for Input/Output artifacts are not supported.'
                 )
         elif isinstance(
                 parameter_type,
@@ -193,41 +196,45 @@
                     parameter.default is None):
                 raise ValueError(
                     'Path inputs only support default values of None. Default'
                     ' values for outputs are not supported.')
 
         type_struct = type_utils._annotation_to_type_struct(parameter_type)
         if type_struct is None:
-            raise TypeError('Missing type annotation for argument: {}'.format(
-                parameter.name))
+            raise TypeError(
+                f'Missing type annotation for argument: {parameter.name}')
 
         if passing_style in [
                 type_annotations.OutputAnnotation, type_annotations.OutputPath
         ]:
             if io_name == single_output_name_const:
-                raise ValueError('"{}" is an invalid parameter name.'.format(
-                    single_output_name_const))
+                raise ValueError(
+                    f'"{single_output_name_const}" is an invalid parameter name.'
+                )
             io_name = _maybe_make_unique(io_name, output_names)
             output_names.add(io_name)
             if type_annotations.is_artifact_class(parameter_type):
                 schema_version = parameter_type.schema_version
                 output_spec = structures.OutputSpec(
                     type=type_utils.create_bundled_artifact_type(
-                        type_struct, schema_version))
+                        type_struct, schema_version),
+                    is_artifact_list=is_artifact_list)
             else:
                 output_spec = structures.OutputSpec(type=type_struct)
             outputs[io_name] = output_spec
         else:
             io_name = _maybe_make_unique(io_name, input_names)
             input_names.add(io_name)
             if type_annotations.is_artifact_class(parameter_type):
                 schema_version = parameter_type.schema_version
                 input_spec = structures.InputSpec(
                     type=type_utils.create_bundled_artifact_type(
-                        type_struct, schema_version))
+                        type_struct, schema_version),
+                    is_artifact_list=is_artifact_list,
+                )
             else:
                 if parameter.default is not inspect.Parameter.empty:
                     input_spec = structures.InputSpec(
                         type=type_struct,
                         default=parameter.default,
                         optional=True)
                 else:
@@ -244,22 +251,26 @@
             # _field_types does not exist in python 3.9 and later
             field_annotations = getattr(return_ann, '__annotations__',
                                         None) or getattr(
                                             return_ann, '_field_types', None)
             for field_name in return_ann._fields:
                 output_name = _maybe_make_unique(field_name, output_names)
                 output_names.add(output_name)
-                annotation = field_annotations.get(field_name)
-                if type_annotations.is_artifact_class(annotation):
+                type_var = field_annotations.get(field_name)
+                if type_annotations.is_list_of_artifacts(type_var):
+                    raise ValueError(
+                        f'Cannot use output lists of artifacts in NamedTuple return annotations. Got output list of artifacts annotation for NamedTuple field `{field_name}`.'
+                    )
+                elif type_annotations.is_artifact_class(type_var):
                     output_spec = structures.OutputSpec(
                         type=type_utils.create_bundled_artifact_type(
-                            annotation.schema_title, annotation.schema_version))
+                            type_var.schema_title, type_var.schema_version))
                 else:
                     type_struct = type_utils._annotation_to_type_struct(
-                        annotation)
+                        type_var)
                     output_spec = structures.OutputSpec(type=type_struct)
                 outputs[output_name] = output_spec
         # Deprecated dict-based way of declaring multiple outputs. Was only used by
         # the @component decorator
         elif isinstance(return_ann, dict):
             warnings.warn(
                 'The ability to specify multiple outputs using the dict syntax'
@@ -274,18 +285,25 @@
         elif signature.return_annotation is not None and signature.return_annotation != inspect.Parameter.empty:
             output_name = _maybe_make_unique(single_output_name_const,
                                              output_names)
             # Fixes exotic, but possible collision:
             #   `def func(output_path: OutputPath()) -> str: ...`
             output_names.add(output_name)
             return_ann = signature.return_annotation
-            if type_annotations.is_artifact_class(signature.return_annotation):
+            if type_annotations.is_list_of_artifacts(return_ann):
+                artifact_cls = return_ann.__args__[0]
+                output_spec = structures.OutputSpec(
+                    type=type_utils.create_bundled_artifact_type(
+                        artifact_cls.schema_title, artifact_cls.schema_version),
+                    is_artifact_list=True)
+            elif type_annotations.is_artifact_class(return_ann):
                 output_spec = structures.OutputSpec(
                     type=type_utils.create_bundled_artifact_type(
-                        return_ann.schema_title, return_ann.schema_version))
+                        return_ann.schema_title, return_ann.schema_version),
+                    is_artifact_list=False)
             else:
                 type_struct = type_utils._annotation_to_type_struct(return_ann)
                 output_spec = structures.OutputSpec(type=type_struct)
 
             outputs[output_name] = output_spec
     elif return_ann != inspect.Parameter.empty and return_ann != structures.ContainerSpec:
         raise TypeError(
@@ -296,16 +314,21 @@
     # docstring.  The name can be overridden by setting setting func.__name__
     # attribute (of the legacy func._component_human_name attribute).  The
     # description can be overridden by setting the func.__doc__ attribute (or
     # the legacy func._component_description attribute).
     component_name = getattr(
         func, '_component_human_name',
         _python_function_name_to_component_name(func.__name__))
-    description = getattr(func, '_component_description',
-                          parsed_docstring.short_description)
+
+    short_description = parsed_docstring.short_description
+    long_description = parsed_docstring.long_description
+    docstring_description = short_description + '\n' + long_description if long_description else short_description
+
+    description = getattr(func, '_component_description', docstring_description)
+
     if description:
         description = description.strip()
 
     component_spec = structures.ComponentSpec(
         name=component_name,
         description=description,
         inputs=inputs if inputs else None,
```

### Comparing `kfp-2.0.0b8/kfp/components/constants.py` & `kfp-2.0.0b9/kfp/components/constants.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/container_component.py` & `kfp-2.0.0b9/kfp/components/container_component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/container_component_artifact_channel.py` & `kfp-2.0.0b9/kfp/components/container_component_artifact_channel.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/container_component_artifact_channel_test.py` & `kfp-2.0.0b9/kfp/components/container_component_artifact_channel_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/container_component_decorator.py` & `kfp-2.0.0b9/kfp/components/container_component_decorator.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/container_component_decorator_test.py` & `kfp-2.0.0b9/kfp/components/container_component_decorator_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/executor.py` & `kfp-2.0.0b9/kfp/components/executor.py`

 * *Files 15% similar despite different names*

```diff
@@ -21,39 +21,51 @@
 from kfp.components.types import type_annotations
 
 
 class Executor():
     """Executor executes v2-based Python function components."""
 
     def __init__(self, executor_input: Dict, function_to_execute: Callable):
-        if hasattr(function_to_execute, 'python_func'):
-            self._func = function_to_execute.python_func
-        else:
-            self._func = function_to_execute
+        self._func = function_to_execute
 
         self._input = executor_input
-        self._input_artifacts: Dict[str, artifact_types.Artifact] = {}
+        self._input_artifacts: Dict[str,
+                                    Union[artifact_types.Artifact,
+                                          List[artifact_types.Artifact]]] = {}
         self._output_artifacts: Dict[str, artifact_types.Artifact] = {}
 
         for name, artifacts in self._input.get('inputs',
                                                {}).get('artifacts', {}).items():
-            artifacts_list = artifacts.get('artifacts')
-            if artifacts_list:
-                self._input_artifacts[name] = self.make_artifact(
-                    artifacts_list[0],
-                    name,
-                    self._func,
-                )
+            list_of_artifact_proto_structs = artifacts.get('artifacts')
+            if list_of_artifact_proto_structs:
+                annotation = self._func.__annotations__[name]
+                # InputPath has no attribute __origin__ and also should be handled as a single artifact
+                if type_annotations.is_Input_Output_artifact_annotation(
+                        annotation) and type_annotations.is_list_of_artifacts(
+                            annotation.__origin__):
+                    self._input_artifacts[name] = [
+                        self.make_artifact(
+                            msg,
+                            name,
+                            self._func,
+                        ) for msg in list_of_artifact_proto_structs
+                    ]
+                else:
+                    self._input_artifacts[name] = self.make_artifact(
+                        list_of_artifact_proto_structs[0],
+                        name,
+                        self._func,
+                    )
 
         for name, artifacts in self._input.get('outputs',
                                                {}).get('artifacts', {}).items():
-            artifacts_list = artifacts.get('artifacts')
-            if artifacts_list:
+            list_of_artifact_proto_structs = artifacts.get('artifacts')
+            if list_of_artifact_proto_structs:
                 output_artifact = self.make_artifact(
-                    artifacts_list[0],
+                    list_of_artifact_proto_structs[0],
                     name,
                     self._func,
                 )
                 self._output_artifacts[name] = output_artifact
                 self.makedirs_recursively(output_artifact.path)
 
         self._return_annotation = inspect.signature(
@@ -112,40 +124,40 @@
             os.makedirs(os.path.dirname(path), exist_ok=True)
         return path
 
     def _get_output_artifact_path(self, artifact_name: str):
         output_artifact = self._output_artifacts.get(artifact_name)
         if not output_artifact:
             raise ValueError(
-                'Failed to get output artifact path for artifact name {}'
-                .format(artifact_name))
+                f'Failed to get output artifact path for artifact name {artifact_name}'
+            )
         return output_artifact.path
 
     def _get_input_artifact_path(self, artifact_name: str):
         input_artifact = self._input_artifacts.get(artifact_name)
         if not input_artifact:
             raise ValueError(
-                'Failed to get input artifact path for artifact name {}'.format(
-                    artifact_name))
+                f'Failed to get input artifact path for artifact name {artifact_name}'
+            )
         return input_artifact.path
 
     def _write_output_parameter_value(self, name: str,
                                       value: Union[str, int, float, bool, dict,
                                                    list, Dict, List]):
         if isinstance(value, (float, int)):
             output = str(value)
         elif isinstance(value, str):
             # value is already a string.
             output = value
         elif isinstance(value, (bool, list, dict)):
             output = json.dumps(value)
         else:
             raise ValueError(
-                'Unable to serialize unknown type `{}` for parameter'
-                ' input with value `{}`'.format(value, type(value)))
+                f'Unable to serialize unknown type `{value}` for parameter input with value `{type(value)}`'
+            )
 
         if not self._executor_output.get('parameterValues'):
             self._executor_output['parameterValues'] = {}
 
         self._executor_output['parameterValues'][name] = value
 
     def _write_output_artifact_payload(self, name: str, value: Any):
@@ -171,18 +183,15 @@
           type_name: The original type name.
 
         Returns:
           The short form type name or the original name if pattern doesn't match.
         """
         import re
         match = re.match('(typing\.)?(?P<type>\w+)(?:\[.+\])?', type_name)
-        if match:
-            return match.group('type')
-        else:
-            return type_name
+        return match.group('type') if match else type_name
 
     # TODO: merge with type_utils.is_parameter_type
     @classmethod
     def _is_parameter(cls, annotation: Any) -> bool:
         if type(annotation) == type:
             return annotation in [str, int, float, bool, dict, list]
 
@@ -206,24 +215,23 @@
     def _handle_single_return_value(self, output_name: str,
                                     annotation_type: Any, return_value: Any):
         if self._is_parameter(annotation_type):
             origin_type = getattr(annotation_type, '__origin__',
                                   None) or annotation_type
             if not isinstance(return_value, origin_type):
                 raise ValueError(
-                    'Function `{}` returned value of type {}; want type {}'
-                    .format(self._func.__name__, type(return_value),
-                            origin_type))
+                    f'Function `{self._func.__name__}` returned value of type {type(return_value)}; want type {origin_type}'
+                )
             self._write_output_parameter_value(output_name, return_value)
         elif self._is_artifact(annotation_type):
             self._write_output_artifact_payload(output_name, return_value)
         else:
             raise RuntimeError(
-                'Unknown return type: {}. Must be one of `str`, `int`, `float`, or a'
-                ' subclass of `Artifact`'.format(annotation_type))
+                f'Unknown return type: {annotation_type}. Must be one of `str`, `int`, `float`, or a subclass of `Artifact`'
+            )
 
     def _write_executor_output(self, func_output: Optional[Any] = None):
         if self._output_artifacts:
             self._executor_output['artifacts'] = {}
 
         for name, artifact in self._output_artifacts.items():
             runtime_artifact = {
@@ -241,36 +249,42 @@
                 # Note: single output is named `Output` in component.yaml.
                 self._handle_single_return_value('Output',
                                                  self._return_annotation,
                                                  func_output)
             elif self._is_named_tuple(self._return_annotation):
                 if len(self._return_annotation._fields) != len(func_output):
                     raise RuntimeError(
-                        'Expected {} return values from function `{}`, got {}'
-                        .format(
-                            len(self._return_annotation._fields),
-                            self._func.__name__, len(func_output)))
+                        f'Expected {len(self._return_annotation._fields)} return values from function `{self._func.__name__}`, got {len(func_output)}'
+                    )
                 for i in range(len(self._return_annotation._fields)):
                     field = self._return_annotation._fields[i]
                     field_type = self._return_annotation.__annotations__[field]
                     if type(func_output) == tuple:
                         field_value = func_output[i]
                     else:
                         field_value = getattr(func_output, field)
                     self._handle_single_return_value(field, field_type,
                                                      field_value)
             else:
                 raise RuntimeError(
-                    'Unknown return type: {}. Must be one of `str`, `int`, `float`, a'
-                    ' subclass of `Artifact`, or a NamedTuple collection of these types.'
-                    .format(self._return_annotation))
-
-        executor_output_path = self._input['outputs']['outputFile']
-        # This check is to reduce the likelihood that two or more workers (in a distributed training/compute strategy) attempt to write to the same executor output file at the same time using gcsfuse. Do not remove until fixed by gcsfuse.
-        if not os.path.exists(executor_output_path):
+                    f'Unknown return type: {self._return_annotation}. Must be one of `str`, `int`, `float`, a subclass of `Artifact`, or a NamedTuple collection of these types.'
+                )
+
+        # This check is to ensure only one worker (in a mirrored, distributed training/compute strategy) attempts to write to the same executor output file at the same time using gcsfuse, which enforces immutability of files.
+        write_file = True
+
+        CLUSTER_SPEC_ENV_VAR_NAME = 'CLUSTER_SPEC'
+        cluster_spec_string = os.environ.get(CLUSTER_SPEC_ENV_VAR_NAME)
+        if cluster_spec_string:
+            cluster_spec = json.loads(cluster_spec_string)
+            CHIEF_NODE_LABELS = {'workerpool0', 'chief', 'master'}
+            write_file = cluster_spec['task']['type'] in CHIEF_NODE_LABELS
+
+        if write_file:
+            executor_output_path = self._input['outputs']['outputFile']
             os.makedirs(os.path.dirname(executor_output_path), exist_ok=True)
             with open(executor_output_path, 'w') as f:
                 f.write(json.dumps(self._executor_output))
 
     def execute(self):
         annotations = inspect.getfullargspec(self._func).annotations
 
@@ -298,15 +312,15 @@
                 )
 
             elif self._is_parameter(v):
                 value = self._get_input_parameter_value(k)
                 if value is not None:
                     func_kwargs[k] = value
 
-            elif type_annotations.is_artifact_annotation(v):
+            elif type_annotations.is_Input_Output_artifact_annotation(v):
                 if type_annotations.is_input_artifact(v):
                     func_kwargs[k] = self._get_input_artifact(k)
                 if type_annotations.is_output_artifact(v):
                     func_kwargs[k] = self._get_output_artifact(k)
 
             elif isinstance(v, type_annotations.OutputPath):
                 if self._is_parameter(v.type):
```

### Comparing `kfp-2.0.0b8/kfp/components/executor_main.py` & `kfp-2.0.0b9/kfp/components/executor_main.py`

 * *Files 10% similar despite different names*

```diff
@@ -55,51 +55,49 @@
     func_name = args.function_to_execute
     module_path = None
     module_directory = None
     module_name = None
 
     if args.component_module_path is not None:
         logging.info(
-            'Looking for component `{}` in --component_module_path `{}`'.format(
-                func_name, args.component_module_path))
+            f'Looking for component `{func_name}` in --component_module_path `{args.component_module_path}`'
+        )
         module_path = args.component_module_path
         module_directory = os.path.dirname(args.component_module_path)
         module_name = os.path.basename(args.component_module_path)[:-len('.py')]
     else:
         # Look for module directory using kfp_config.ini
-        logging.info('--component_module_path is not specified. Looking for'
-                     ' component `{}` in config file `kfp_config.ini`'
-                     ' instead'.format(func_name))
+        logging.info(
+            f'--component_module_path is not specified. Looking for component `{func_name}` in config file `kfp_config.ini` instead'
+        )
         config = kfp_config.KFPConfig()
         components = config.get_components()
         if not components:
             raise RuntimeError('No components found in `kfp_config.ini`')
         try:
             module_path = components[func_name]
         except KeyError:
             raise RuntimeError(
-                'Could not find component `{}` in `kfp_config.ini`. Found the '
-                ' following components instead:\n{}'.format(
-                    func_name, components))
+                f'Could not find component `{func_name}` in `kfp_config.ini`. Found the  following components instead:\n{components}'
+            )
 
         module_directory = str(module_path.parent)
         module_name = str(module_path.name)[:-len('.py')]
 
     logging.info(
-        'Loading KFP component "{}" from {} (directory "{}" and module name'
-        ' "{}")'.format(func_name, module_path, module_directory, module_name))
+        f'Loading KFP component "{func_name}" from {module_path} (directory "{module_directory}" and module name "{module_name}")'
+    )
 
     module = utils.load_module(
         module_name=module_name, module_directory=module_directory)
 
     executor_input = json.loads(args.executor_input)
     function_to_execute = getattr(module, func_name)
 
-    logging.info('Got executor_input:\n{}'.format(
-        json.dumps(executor_input, indent=4)))
+    logging.info(f'Got executor_input:\n{json.dumps(executor_input, indent=4)}')
 
     executor = component_executor.Executor(
         executor_input=executor_input, function_to_execute=function_to_execute)
 
     executor.execute()
```

### Comparing `kfp-2.0.0b8/kfp/components/executor_test.py` & `kfp-2.0.0b9/kfp/components/executor_test.py`

 * *Files 6% similar despite different names*

```diff
@@ -14,14 +14,15 @@
 """Tests for kfp.components.executor."""
 
 import json
 import os
 import tempfile
 from typing import Callable, Dict, List, NamedTuple, Optional
 import unittest
+from unittest import mock
 
 from absl.testing import parameterized
 from kfp.components import executor
 from kfp.components.task_final_status import PipelineTaskFinalStatus
 from kfp.components.types import artifact_types
 from kfp.components.types.artifact_types import Artifact
 from kfp.components.types.artifact_types import Dataset
@@ -39,22 +40,25 @@
     def setUp(cls):
         cls.maxDiff = None
         cls._test_dir = tempfile.mkdtemp()
         artifact_types._GCS_LOCAL_MOUNT_PREFIX = cls._test_dir + '/'
         artifact_types._MINIO_LOCAL_MOUNT_PREFIX = cls._test_dir + '/minio/'
         artifact_types._S3_LOCAL_MOUNT_PREFIX = cls._test_dir + '/s3/'
 
-    def execute_and_load_output_metadata(self, func: Callable,
-                                         executor_input: str) -> dict:
+    def execute(self, func: Callable, executor_input: str) -> None:
         executor_input_dict = json.loads(executor_input %
                                          {'test_dir': self._test_dir})
 
         executor.Executor(
             executor_input=executor_input_dict,
             function_to_execute=func).execute()
+
+    def execute_and_load_output_metadata(self, func: Callable,
+                                         executor_input: str) -> dict:
+        self.execute(func, executor_input)
         with open(os.path.join(self._test_dir, 'output_metadata.json'),
                   'r') as f:
             return json.loads(f.read())
 
     def test_input_and_output_parameters(self):
         executor_input = """\
         {
@@ -998,14 +1002,176 @@
                                 'accuracy': 0.9
                             }
                         }]
                     }
                 }
             })
 
+    @mock.patch.dict(
+        os.environ,
+        {'CLUSTER_SPEC': json.dumps({'task': {
+            'type': 'workerpool0'
+        }})},
+        clear=True)
+    def test_distributed_training_strategy_write(self):
+        executor_input = """\
+        {
+          "inputs": {
+            "parameterValues": {
+              "input_parameter": "Hello, KFP"
+            }
+          },
+          "outputs": {
+            "parameters": {
+              "Output": {
+                "outputFile": "gs://some-bucket/output"
+              }
+            },
+            "outputFile": "%(test_dir)s/output_metadata.json"
+          }
+        }
+        """
+
+        def test_func(input_parameter: str):
+            self.assertEqual(input_parameter, 'Hello, KFP')
+
+        self.execute(
+            func=test_func,
+            executor_input=executor_input,
+        )
+        self.assertTrue(
+            os.path.exists(
+                os.path.join(self._test_dir, 'output_metadata.json')))
+
+    @mock.patch.dict(
+        os.environ,
+        {'CLUSTER_SPEC': json.dumps({'task': {
+            'type': 'workerpool1'
+        }})},
+        clear=True)
+    def test_distributed_training_strategy_no_write(self):
+        executor_input = """\
+        {
+          "inputs": {
+            "parameterValues": {
+              "input_parameter": "Hello, KFP"
+            }
+          },
+          "outputs": {
+            "parameters": {
+              "Output": {
+                "outputFile": "gs://some-bucket/output"
+              }
+            },
+            "outputFile": "%(test_dir)s/output_metadata.json"
+          }
+        }
+        """
+
+        def test_func(input_parameter: str):
+            self.assertEqual(input_parameter, 'Hello, KFP')
+
+        self.execute(
+            func=test_func,
+            executor_input=executor_input,
+        )
+        self.assertFalse(
+            os.path.exists(
+                os.path.join(self._test_dir, 'output_metadata.json')))
+
+    def test_single_artifact_input(self):
+        executor_input = """\
+    {
+      "inputs": {
+        "artifacts": {
+          "input_artifact": {
+            "artifacts": [
+              {
+                "metadata": {},
+                "name": "projects/123/locations/us-central1/metadataStores/default/artifacts/input_artifact",
+                "type": {
+                  "schemaTitle": "system.Artifact"
+                },
+                "uri": "gs://some-bucket/output/input_artifact"
+              }
+            ]
+          }
+        }
+      },
+      "outputs": {
+        "outputFile": "%(test_dir)s/output_metadata.json"
+      }
+    }
+    """
+
+        def test_func(input_artifact: Input[Artifact]):
+            self.assertIsInstance(input_artifact, Artifact)
+            self.assertEqual(
+                input_artifact.name,
+                'projects/123/locations/us-central1/metadataStores/default/artifacts/input_artifact'
+            )
+            self.assertEqual(
+                input_artifact.name,
+                'projects/123/locations/us-central1/metadataStores/default/artifacts/input_artifact'
+            )
+
+        output_metadata = self.execute_and_load_output_metadata(
+            test_func, executor_input)
+
+        self.assertDictEqual(output_metadata, {})
+
+    def test_list_of_artifacts_input(self):
+        executor_input = """\
+    {
+      "inputs": {
+        "artifacts": {
+          "input_list": {
+            "artifacts": [
+              {
+                "metadata": {},
+                "name": "projects/123/locations/us-central1/metadataStores/default/artifacts/input_list/0",
+                "type": {
+                  "schemaTitle": "system.Artifact"
+                },
+                "uri": "gs://some-bucket/output/input_list/0"
+              },
+              {
+                "metadata": {},
+                "name": "projects/123/locations/us-central1/metadataStores/default/artifacts/input_list/1",
+                "type": {
+                  "schemaTitle": "system.Artifact"
+                },
+                "uri": "gs://some-bucket/output/input_list/1"
+              }
+            ]
+          }
+        }
+      },
+      "outputs": {
+        "outputFile": "%(test_dir)s/output_metadata.json"
+      }
+    }
+    """
+
+        def test_func(input_list: Input[List[Artifact]]):
+            self.assertEqual(len(input_list), 2)
+            self.assertEqual(
+                input_list[0].name,
+                'projects/123/locations/us-central1/metadataStores/default/artifacts/input_list/0'
+            )
+            self.assertEqual(
+                input_list[1].name,
+                'projects/123/locations/us-central1/metadataStores/default/artifacts/input_list/1'
+            )
+
+        output_metadata = self.execute_and_load_output_metadata(
+            test_func, executor_input)
+
+        self.assertDictEqual(output_metadata, {})
+
 
 class VertexDataset:
     schema_title = 'google.VertexDataset'
     schema_version = '0.0.0'
 
     @classmethod
     def _from_executor_fields(
```

### Comparing `kfp-2.0.0b8/kfp/components/for_loop.py` & `kfp-2.0.0b9/kfp/components/for_loop.py`

 * *Files 3% similar despite different names*

```diff
@@ -36,18 +36,15 @@
     Args:
         type_name: The collection type name, like `List`, Sequence`, etc.
 
     Returns:
         The collection item type or None if no match found.
     """
     match = re.match('(typing\.)?(?:\w+)(?:\[(?P<item_type>.+)\])', type_name)
-    if match:
-        return match.group('item_type').lstrip().rstrip()
-    else:
-        return None
+    return match['item_type'].lstrip().rstrip() if match else None
 
 
 def _get_subvar_type(type_name: str) -> Optional[str]:
     """Extracts the subvar type.
 
     This method is used for extract the value type from a dictionary type.
     For example:
@@ -60,18 +57,15 @@
 
     Returns:
         The dictionary value type or None if no match found.
     """
     match = re.match(
         '(typing\.)?(?:\w+)(?:\[\s*(?:\w+)\s*,\s*(?P<value_type>.+)\])',
         type_name)
-    if match:
-        return match.group('value_type').lstrip().rstrip()
-    else:
-        return None
+    return match['value_type'].lstrip().rstrip() if match else None
 
 
 class LoopArgument(pipeline_channel.PipelineParameterChannel):
     """Represents the argument that are looped over in a ParallelFor loop.
 
     The class shouldn't be instantiated by the end user, rather it is
     created automatically by a ParallelFor ops group.
@@ -151,15 +145,15 @@
             name, LoopArgumentVariable(
                 loop_argument=self,
                 subvar_name=name,
             ))
 
     def _make_name(self, code: str):
         """Makes a name for this loop argument from a unique code."""
-        return '{}-{}'.format(self.LOOP_ITEM_PARAM_NAME_BASE, code)
+        return f'{self.LOOP_ITEM_PARAM_NAME_BASE}-{code}'
 
     @classmethod
     def from_pipeline_channel(
         cls,
         channel: pipeline_channel.PipelineChannel,
     ) -> 'LoopArgument':
         """Creates a LoopArgument object from a PipelineChannel object."""
```

### Comparing `kfp-2.0.0b8/kfp/components/for_loop_test.py` & `kfp-2.0.0b9/kfp/components/for_loop_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/graph_component.py` & `kfp-2.0.0b9/kfp/components/graph_component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/importer_component.py` & `kfp-2.0.0b9/kfp/components/importer_component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/importer_node.py` & `kfp-2.0.0b9/kfp/components/importer_node.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/importer_node_test.py` & `kfp-2.0.0b9/kfp/components/importer_node_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/kfp_config.py` & `kfp-2.0.0b9/kfp/components/kfp_config.py`

 * *Files 1% similar despite different names*

```diff
@@ -96,12 +96,11 @@
     def get_components(self) -> Dict[str, pathlib.Path]:
         """Returns a list of known KFP components.
 
         Returns:
             A dictionary from component name (function name) to a pathlib.Path
             pointing to the Python file with this component's definition.
         """
-        result = {
+        return {
             function_name: pathlib.Path(module_path) for function_name,
             module_path in self._config_parser[_COMPONENTS_SECTION].items()
         }
-        return result
```

### Comparing `kfp-2.0.0b8/kfp/components/pipeline_channel.py` & `kfp-2.0.0b9/kfp/components/pipeline_channel.py`

 * *Files 5% similar despite different names*

```diff
@@ -8,15 +8,17 @@
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 """Definition of PipelineChannel."""
+
 import abc
+import contextlib
 import dataclasses
 import json
 import re
 from typing import Dict, List, Optional, Union
 
 from kfp.components.types import type_utils
 
@@ -82,16 +84,16 @@
         Raises:
             ValueError: If name or task_name contains invalid characters.
             ValueError: If both task_name and value are set.
         """
         valid_name_regex = r'^[A-Za-z][A-Za-z0-9\s_-]*$'
         if not re.match(valid_name_regex, name):
             raise ValueError(
-                'Only letters, numbers, spaces, "_", and "-" are allowed in the '
-                'name. Must begin with a letter. Got name: {}'.format(name))
+                f'Only letters, numbers, spaces, "_", and "-" are allowed in the name. Must begin with a letter. Got name: {name}'
+            )
 
         self.name = name
         self.channel_type = channel_type
         # ensure value is None even if empty string or empty list/dict
         # so that serialization and unserialization remain consistent
         # (i.e. None => '' => None)
         self.task_name = task_name or None
@@ -299,18 +301,16 @@
     for match in matches:
         task_name, name, channel_type = match
 
         # channel_type could be either a string (e.g. "Integer") or a dictionary
         # (e.g.: {"custom_type": {"custom_property": "some_value"}}).
         # Try loading it into dictionary, if failed, it means channel_type is a
         # string.
-        try:
+        with contextlib.suppress(json.JSONDecodeError):
             channel_type = json.loads(channel_type)
-        except json.JSONDecodeError:
-            pass
 
         if type_utils.is_parameter_type(channel_type):
             pipeline_channel = PipelineParameterChannel(
                 name=name,
                 channel_type=channel_type,
                 task_name=task_name,
             )
@@ -342,15 +342,15 @@
 
     if isinstance(payload, PipelineChannel):
         return [payload]
 
     if isinstance(payload, str):
         return list(set(extract_pipeline_channels_from_string(payload)))
 
-    if isinstance(payload, list) or isinstance(payload, tuple):
+    if isinstance(payload, (list, tuple)):
         pipeline_channels = []
         for item in payload:
             pipeline_channels += extract_pipeline_channels_from_any(item)
         return list(set(pipeline_channels))
 
     if isinstance(payload, dict):
         pipeline_channels = []
```

### Comparing `kfp-2.0.0b8/kfp/components/pipeline_channel_test.py` & `kfp-2.0.0b9/kfp/components/pipeline_channel_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/pipeline_context.py` & `kfp-2.0.0b9/kfp/components/pipeline_context.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/pipeline_task.py` & `kfp-2.0.0b9/kfp/components/pipeline_task.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,20 +21,16 @@
 from kfp.components import constants
 from kfp.components import pipeline_channel
 from kfp.components import placeholders
 from kfp.components import structures
 from kfp.components import utils
 from kfp.components.types import type_utils
 
-
-def create_pipeline_task(
-    component_spec: structures.ComponentSpec,
-    args: Mapping[str, Any],
-) -> 'PipelineTask':
-    return PipelineTask(component_spec=component_spec, args=args)
+_register_task_handler = lambda task: utils.maybe_rename_for_k8s(
+    task.component_spec.name)
 
 
 class PipelineTask:
     """Represents a pipeline task (instantiated component).
 
     **Note:** ``PipelineTask`` should not be constructed by pipeline authors directly, but instead obtained via an instantiated component (see example).
 
@@ -53,20 +49,19 @@
             return message
 
         @dsl.pipeline(name='my_pipeline')
         def my_pipeline():
             # task is an instance of PipelineTask
             task = identity(message='my string')
     """
+    _register_task_handler = _register_task_handler
 
     # Fallback behavior for compiling a component. This should be overriden by
     # pipeline `register_task_and_generate_id` if compiling a pipeline (more
     # than one component).
-    _register_task_handler = lambda task: utils.maybe_rename_for_k8s(
-        task.component_spec.name)
 
     def __init__(
         self,
         component_spec: structures.ComponentSpec,
         args: Mapping[str, Any],
     ):
         """Initilizes a PipelineTask instance."""
@@ -115,19 +110,18 @@
                     f'"{input_name}" of component "{component_spec.name}": '),
             )
 
         self.component_spec = component_spec
 
         self._task_spec = structures.TaskSpec(
             name=self._register_task_handler(),
-            inputs={input_name: value for input_name, value in args.items()},
+            inputs=dict(args.items()),
             dependent_tasks=[],
             component_ref=component_spec.name,
-            enable_caching=True,
-        )
+            enable_caching=True)
 
         self.importer_spec = None
         self.container_spec = None
         self.pipeline_spec = None
 
         def validate_placeholder_types(
                 component_spec: structures.ComponentSpec) -> None:
@@ -264,19 +258,15 @@
             Self return to allow chained setting calls.
         """
         if re.match(r'([0-9]*[.])?[0-9]+m?$', cpu) is None:
             raise ValueError(
                 'Invalid cpu string. Should be float or integer, or integer'
                 ' followed by "m".')
 
-        if cpu.endswith('m'):
-            cpu = float(cpu[:-1]) / 1000
-        else:
-            cpu = float(cpu)
-
+        cpu = float(cpu[:-1]) / 1000 if cpu.endswith('m') else float(cpu)
         if self.container_spec is None:
             raise ValueError(
                 'There is no container specified in implementation')
 
         if self.container_spec.resources is not None:
             self.container_spec.resources.cpu_limit = cpu
         else:
@@ -459,18 +449,14 @@
 
             @dsl.pipeline(name='my-pipeline')
             def my_pipeline():
                 task1 = my_component(text='1st task')
                 task2 = my_component(text='2nd task').after(task1)
         """
         for task in tasks:
-            if task.parent_task_group is not self.parent_task_group:
-                raise ValueError(
-                    f'Cannot use .after() across inner pipelines or DSL control flow features. Tried to set {self.name} after {task.name}, but these tasks do not belong to the same pipeline or are not enclosed in the same control flow content manager.'
-                )
             self._task_spec.dependent_tasks.append(task.name)
         return self
 
 
 # TODO: this function should ideally be in the function kfp.components.structures.check_placeholder_references_valid_io_name, which does something similar, but this causes the exception to be raised at component definition time, rather than compile time. This would break tests that load v1 component YAML, even though that YAML is invalid.
 def check_primitive_placeholder_is_used_for_correct_io_type(
     inputs_dict: Dict[str, structures.InputSpec],
```

### Comparing `kfp-2.0.0b8/kfp/components/placeholders.py` & `kfp-2.0.0b9/kfp/components/placeholders.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/placeholders_test.py` & `kfp-2.0.0b9/kfp/components/placeholders_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/python_component.py` & `kfp-2.0.0b9/kfp/components/python_component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/structures.py` & `kfp-2.0.0b9/kfp/components/structures.py`

 * *Files 3% similar despite different names*

```diff
@@ -40,18 +40,21 @@
 class InputSpec:
     """Component input definitions.
 
     Attributes:
         type: The type of the input.
         default (optional): the default value for the input.
         optional: Wether the input is optional. An input is optional when it has an explicit default value.
+        is_artifact_list: True if `type` represents a list of the artifact type. Only applies when `type` is an artifact.
     """
     type: Union[str, dict]
     default: Optional[Any] = None
     optional: bool = False
+    # This special flag for lists of artifacts allows type to be used the same way for list of artifacts and single artifacts. This is aligned with how IR represents lists of artifacts (same as for single artifacts), as well as simplifies downstream type handling/checking operations in the SDK since we don't need to parse the string `type` to determine if single artifact or list.
+    is_artifact_list: bool = False
 
     def __post_init__(self) -> None:
         self._validate_type()
         self._validate_usage_of_optional()
 
     @classmethod
     def from_ir_component_inputs_dict(
@@ -128,19 +131,24 @@
 
 @dataclasses.dataclass
 class OutputSpec:
     """Component output definitions.
 
     Attributes:
         type: The type of the output.
+        is_artifact_list: True if `type` represents a list of the artifact type. Only applies when `type` is an artifact.
     """
     type: Union[str, dict]
+    # This special flag for lists of artifacts allows type to be used the same way for list of artifacts and single artifacts. This is aligned with how IR represents lists of artifacts (same as for single artifacts), as well as simplifies downstream type handling/checking operations in the SDK since we don't need to parse the string `type` to determine if single artifact or list.
+    is_artifact_list: bool = False
 
     def __post_init__(self) -> None:
         self._validate_type()
+        # TODO: remove this method when we support output lists of artifacts
+        self._prevent_using_output_lists_of_artifacts()
 
     @classmethod
     def from_ir_component_outputs_dict(
             cls, ir_component_outputs_dict: Dict[str, Any]) -> 'OutputSpec':
         """Creates an OutputSpec from a ComponentOutputsSpec message in dict
         format (pipeline_spec.components.<component-
         key>.outputDefinitions.parameters|artifacts.<output-key>).
@@ -192,14 +200,19 @@
 
         This allows us to perform fewer checks downstream.
         """
         # TODO: add transformation logic so that we don't have to transform outputs at every place they are used, including v1 back compat support
         if not spec_type_is_parameter(self.type):
             type_utils.validate_bundled_artifact_type(self.type)
 
+    def _prevent_using_output_lists_of_artifacts(self):
+        if self.is_artifact_list:
+            raise NotImplementedError(
+                'Output lists of artifacts are not yet supported.')
+
 
 def spec_type_is_parameter(type_: str) -> bool:
     in_memory_type = type_annotations.maybe_strip_optional_from_annotation_string(
         type_utils.get_canonical_name_for_outer_generic(type_))
 
     return in_memory_type in type_utils.IN_MEMORY_SPEC_TYPE_TO_IR_TYPE or in_memory_type == 'PipelineTaskFinalStatus'
 
@@ -812,33 +825,58 @@
         Args:
             component_yaml: the component yaml in string format.
 
         Returns:
             Component spec in the form of V2 ComponentSpec.
         """
 
+        def extract_description(component_yaml: str) -> Union[str, None]:
+            heading = '# Description: '
+            multi_line_description_prefix = '#             '
+            index_of_heading = 2
+            if heading in component_yaml:
+                description = component_yaml.splitlines()[index_of_heading]
+
+                # Multi line
+                comments = component_yaml.splitlines()
+                index = index_of_heading + 1
+                while comments[index][:len(multi_line_description_prefix
+                                          )] == multi_line_description_prefix:
+                    description += '\n' + comments[index][
+                        len(multi_line_description_prefix) + 1:]
+                    index += 1
+
+                return description[len(heading):]
+            else:
+                return None
+
         json_component = yaml.safe_load(component_yaml)
         is_v1 = 'implementation' in set(json_component.keys())
         if is_v1:
             v1_component = v1_components._load_component_spec_from_component_text(
                 component_yaml)
             return cls.from_v1_component_spec(v1_component)
         else:
-            return ComponentSpec.from_pipeline_spec_dict(json_component)
+            component_spec = ComponentSpec.from_pipeline_spec_dict(
+                json_component)
+            if not component_spec.description:
+                component_spec.description = extract_description(
+                    component_yaml=component_yaml)
+            return component_spec
 
     def save_to_component_yaml(self, output_file: str) -> None:
         """Saves ComponentSpec into IR YAML file.
 
         Args:
             output_file: File path to store the component yaml.
         """
         from kfp.compiler import pipeline_spec_builder as builder
 
         pipeline_spec = self.to_pipeline_spec()
-        builder.write_pipeline_spec_to_file(pipeline_spec, output_file)
+        builder.write_pipeline_spec_to_file(pipeline_spec, None, output_file)
 
     def to_pipeline_spec(self) -> pipeline_spec_pb2.PipelineSpec:
         """Creates a pipeline instance and constructs the pipeline spec for a
         single component.
 
         Args:
             component_spec: The ComponentSpec to convert to PipelineSpec.
```

### Comparing `kfp-2.0.0b8/kfp/components/structures_test.py` & `kfp-2.0.0b9/kfp/components/structures_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/task_final_status.py` & `kfp-2.0.0b9/kfp/components/task_final_status.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/tasks_group.py` & `kfp-2.0.0b9/kfp/components/tasks_group.py`

 * *Files 2% similar despite different names*

```diff
@@ -56,16 +56,16 @@
         """Create a new instance of TasksGroup.
 
         Args:
           group_type: The type of the group.
           name: The name of the group. Used as display name in UI.
         """
         self.group_type = group_type
-        self.tasks = list()
-        self.groups = list()
+        self.tasks = []
+        self.groups = []
         self.display_name = name
         self.dependencies = []
         self.is_root = is_root
 
     def __enter__(self):
         if not pipeline_context.Pipeline.get_default_pipeline():
             raise ValueError('Default pipeline not defined.')
```

### Comparing `kfp-2.0.0b8/kfp/components/tasks_group_test.py` & `kfp-2.0.0b9/kfp/components/tasks_group_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/types/__init__.py` & `kfp-2.0.0b9/kfp/components/types/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/types/artifact_types.py` & `kfp-2.0.0b9/kfp/components/types/artifact_types.py`

 * *Files 2% similar despite different names*

```diff
@@ -223,17 +223,16 @@
 
         Raises:
           ValueError: If the lists ``fpr``, ``tpr`` and ``threshold`` are not the same length.
         """
         if len(fpr) != len(tpr) or len(fpr) != len(threshold) or len(
                 tpr) != len(threshold):
             raise ValueError(
-                'Length of fpr, tpr and threshold must be the same. '
-                'Got lengths {}, {} and {} respectively.'.format(
-                    len(fpr), len(tpr), len(threshold)))
+                f'Length of fpr, tpr and threshold must be the same. Got lengths {len(fpr)}, {len(tpr)} and {len(threshold)} respectively.'
+            )
 
         for i in range(len(fpr)):
             self.log_roc_data_point(
                 fpr=fpr[i], tpr=tpr[i], threshold=threshold[i])
 
     def set_confusion_matrix_categories(self, categories: List[str]) -> None:
         """Stores confusion matrix categories to metadata.
@@ -249,17 +248,19 @@
             self._categories.append(category)
             annotation_specs.append(annotation_spec)
 
         self._matrix = []
         for row in range(len(self._categories)):
             self._matrix.append({'row': [0] * len(self._categories)})
 
-        self._confusion_matrix = {}
-        self._confusion_matrix['annotationSpecs'] = annotation_specs
-        self._confusion_matrix['rows'] = self._matrix
+        self._confusion_matrix = {
+            'annotationSpecs': annotation_specs,
+            'rows': self._matrix
+        }
+
         self.metadata['confusionMatrix'] = self._confusion_matrix
 
     def log_confusion_matrix_row(self, row_category: str,
                                  row: List[float]) -> None:
         """Logs a confusion matrix row to metadata.
 
         Args:
@@ -267,20 +268,22 @@
           row: List of integers specifying the values for the row.
 
         Raises:
           ValueError: If ``row_category`` is not in the list of categories
             set in ``set_categories`` call.
         """
         if row_category not in self._categories:
-            raise ValueError('Invalid category: {} passed. Expected one of: {}'.\
-              format(row_category, self._categories))
+            raise ValueError(
+                f'Invalid category: {row_category} passed. Expected one of: {self._categories}'
+            )
 
         if len(row) != len(self._categories):
-            raise ValueError('Invalid row. Expected size: {} got: {}'.\
-              format(len(self._categories), len(row)))
+            raise ValueError(
+                f'Invalid row. Expected size: {len(self._categories)} got: {len(row)}'
+            )
 
         self._matrix[self._categories.index(row_category)] = {'row': row}
         self.metadata['confusionMatrix'] = self._confusion_matrix
 
     def log_confusion_matrix_cell(self, row_category: str, col_category: str,
                                   value: int) -> None:
         """Logs a cell in the confusion matrix to metadata.
@@ -291,20 +294,22 @@
           value: Value of the cell.
 
         Raises:
           ValueError: If ``row_category`` or ``col_category`` is not in the list of
            categories set in ``set_categories``.
         """
         if row_category not in self._categories:
-            raise ValueError('Invalid category: {} passed. Expected one of: {}'.\
-              format(row_category, self._categories))
+            raise ValueError(
+                f'Invalid category: {row_category} passed. Expected one of: {self._categories}'
+            )
 
         if col_category not in self._categories:
-            raise ValueError('Invalid category: {} passed. Expected one of: {}'.\
-              format(row_category, self._categories))
+            raise ValueError(
+                f'Invalid category: {row_category} passed. Expected one of: {self._categories}'
+            )
 
         self._matrix[self._categories.index(row_category)]['row'][
             self._categories.index(col_category)] = value
         self.metadata['confusionMatrix'] = self._confusion_matrix
 
     def log_confusion_matrix(self, categories: List[str],
                              matrix: List[List[int]]) -> None:
@@ -316,21 +321,22 @@
 
         Raises:
           ValueError: If the length of ``categories`` does not match number of rows or columns of ``matrix``.
         """
         self.set_confusion_matrix_categories(categories)
 
         if len(matrix) != len(categories):
-            raise ValueError('Invalid matrix: {} passed for categories: {}'.\
-              format(matrix, categories))
+            raise ValueError(
+                f'Invalid matrix: {matrix} passed for categories: {categories}')
 
         for index in range(len(categories)):
             if len(matrix[index]) != len(categories):
-                raise ValueError('Invalid matrix: {} passed for categories: {}'.\
-                  format(matrix, categories))
+                raise ValueError(
+                    f'Invalid matrix: {matrix} passed for categories: {categories}'
+                )
 
             self.log_confusion_matrix_row(categories[index], matrix[index])
 
         self.metadata['confusionMatrix'] = self._confusion_matrix
 
 
 class SlicedClassificationMetrics(Artifact):
@@ -358,16 +364,15 @@
     def _upsert_classification_metrics_for_slice(self, slice: str) -> None:
         """Upserts the classification metrics instance for a slice."""
         if slice not in self._sliced_metrics:
             self._sliced_metrics[slice] = ClassificationMetrics()
 
     def _update_metadata(self, slice: str) -> None:
         """Updates metadata to adhere to the metrics schema."""
-        self.metadata = {}
-        self.metadata['evaluationSlices'] = []
+        self.metadata = {'evaluationSlices': []}
         for slice in self._sliced_metrics.keys():
             slice_metrics = {
                 'slice':
                     slice,
                 'sliceClassificationMetrics':
                     self._sliced_metrics[slice].metadata
             }
```

### Comparing `kfp-2.0.0b8/kfp/components/types/artifact_types_test.py` & `kfp-2.0.0b9/kfp/components/types/artifact_types_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/types/custom_artifact_types.py` & `kfp-2.0.0b9/kfp/components/types/custom_artifact_types.py`

 * *Files 0% similar despite different names*

```diff
@@ -45,15 +45,15 @@
     """
     param_to_artifact_cls: Dict[str, type] = {}
     kfp_artifact_classes = set(type_utils._ARTIFACT_CLASSES_MAPPING.values())
 
     signature = inspect.signature(func)
     for name, param in signature.parameters.items():
         annotation = param.annotation
-        if type_annotations.is_artifact_annotation(annotation):
+        if type_annotations.is_Input_Output_artifact_annotation(annotation):
             artifact_class = type_annotations.get_io_artifact_class(annotation)
             if artifact_class not in kfp_artifact_classes:
                 param_to_artifact_cls[name] = artifact_class
         elif type_annotations.is_artifact_class(annotation):
             param_to_artifact_cls[name] = annotation
             if artifact_class not in kfp_artifact_classes:
                 param_to_artifact_cls[name] = artifact_class
```

### Comparing `kfp-2.0.0b8/kfp/components/types/custom_artifact_types_test.py` & `kfp-2.0.0b9/kfp/components/types/custom_artifact_types_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/types/type_annotations.py` & `kfp-2.0.0b9/kfp/components/types/type_annotations.py`

 * *Files 8% similar despite different names*

```diff
@@ -13,16 +13,17 @@
 # limitations under the License.
 """Classes for input/output type annotations in KFP SDK.
 
 These are only compatible with v2 Pipelines.
 """
 
 import re
-from typing import Type, TypeVar, Union
+from typing import List, Type, TypeVar, Union
 
+from kfp.components.types import artifact_types
 from kfp.components.types import type_annotations
 from kfp.components.types import type_utils
 
 
 class OutputPath:
     """Type annotation used in component definitions for indicating a parameter
     is a path to an output. The path parameter typed with this annotation can
@@ -116,53 +117,58 @@
     """Marker type for input artifacts."""
 
 
 class OutputAnnotation:
     """Marker type for output artifacts."""
 
 
-def is_artifact_annotation(typ) -> bool:
+def is_Input_Output_artifact_annotation(typ) -> bool:
     if not hasattr(typ, '__metadata__'):
         return False
 
     if typ.__metadata__[0] not in [InputAnnotation, OutputAnnotation]:
         return False
 
     return True
 
 
 def is_input_artifact(typ) -> bool:
     """Returns True if typ is of type Input[T]."""
-    if not is_artifact_annotation(typ):
+    if not is_Input_Output_artifact_annotation(typ):
         return False
 
     return typ.__metadata__[0] == InputAnnotation
 
 
 def is_output_artifact(typ) -> bool:
     """Returns True if typ is of type Output[T]."""
-    if not is_artifact_annotation(typ):
+    if not is_Input_Output_artifact_annotation(typ):
         return False
 
     return typ.__metadata__[0] == OutputAnnotation
 
 
 def get_io_artifact_class(typ):
     from kfp.dsl import Input
     from kfp.dsl import Output
-    if not is_artifact_annotation(typ):
+    if not is_Input_Output_artifact_annotation(typ):
         return None
     if typ == Input or typ == Output:
         return None
 
-    return typ.__args__[0]
+    # extract inner type from list of artifacts
+    inner = typ.__args__[0]
+    if hasattr(inner, '__origin__') and inner.__origin__ == list:
+        return inner.__args__[0]
+
+    return inner
 
 
 def get_io_artifact_annotation(typ):
-    if not is_artifact_annotation(typ):
+    if not is_Input_Output_artifact_annotation(typ):
         return None
 
     return typ.__metadata__[0]
 
 
 T = TypeVar('T')
 
@@ -209,17 +215,24 @@
     Args:
       type_name: The original type name.
 
     Returns:
       The short form type name or the original name if pattern doesn't match.
     """
     match = re.match('(typing\.)?(?P<type>\w+)(?:\[.+\])?', type_name)
-    if match:
-        return match.group('type')
-    else:
-        return type_name
+    return match['type'] if match else type_name
 
 
 def is_artifact_class(artifact_class_or_instance: Type) -> bool:
     # we do not yet support non-pre-registered custom artifact types with instance_schema attribute
     return hasattr(artifact_class_or_instance, 'schema_title') and hasattr(
         artifact_class_or_instance, 'schema_version')
+
+
+def is_list_of_artifacts(
+    type_var: Union[Type[List[artifact_types.Artifact]],
+                    Type[artifact_types.Artifact]]
+) -> bool:
+    # the type annotation for this function's `type_var` parameter may not actually be a subclass of the KFP SDK's Artifact class for custom artifact types
+    return getattr(type_var, '__origin__',
+                   None) == list and type_annotations.is_artifact_class(
+                       type_var.__args__[0])
```

### Comparing `kfp-2.0.0b8/kfp/components/types/type_annotations_test.py` & `kfp-2.0.0b9/kfp/components/types/type_annotations_test.py`

 * *Files 10% similar despite different names*

```diff
@@ -26,57 +26,91 @@
 from kfp.components.types.type_annotations import OutputPath
 from kfp.dsl import Input
 from kfp.dsl import Output
 
 
 class AnnotationsTest(parameterized.TestCase):
 
-    def test_is_artifact_annotation(self):
-        self.assertTrue(type_annotations.is_artifact_annotation(Input[Model]))
-        self.assertTrue(type_annotations.is_artifact_annotation(Output[Model]))
+    @parameterized.parameters([
+        Input[Model],
+        Output[Model],
+        Output[List[Model]],
+        Output['MyArtifact'],
+    ])
+    def test_is_artifact_annotation(self, annotation):
         self.assertTrue(
-            type_annotations.is_artifact_annotation(Output['MyArtifact']))
+            type_annotations.is_Input_Output_artifact_annotation(annotation))
 
-        self.assertFalse(type_annotations.is_artifact_annotation(Model))
-        self.assertFalse(type_annotations.is_artifact_annotation(int))
-        self.assertFalse(type_annotations.is_artifact_annotation('Dataset'))
-        self.assertFalse(type_annotations.is_artifact_annotation(List[str]))
-        self.assertFalse(type_annotations.is_artifact_annotation(Optional[str]))
-
-    def test_is_input_artifact(self):
-        self.assertTrue(type_annotations.is_input_artifact(Input[Model]))
-        self.assertTrue(type_annotations.is_input_artifact(Input))
-
-        self.assertFalse(type_annotations.is_input_artifact(Output[Model]))
-        self.assertFalse(type_annotations.is_input_artifact(Output))
-
-    def test_is_output_artifact(self):
-        self.assertTrue(type_annotations.is_output_artifact(Output[Model]))
-        self.assertTrue(type_annotations.is_output_artifact(Output))
-
-        self.assertFalse(type_annotations.is_output_artifact(Input[Model]))
-        self.assertFalse(type_annotations.is_output_artifact(Input))
+    @parameterized.parameters([
+        Model,
+        int,
+        'Dataset',
+        List[str],
+        Optional[str],
+    ])
+    def test_is_not_artifact_annotation(self, annotation):
+        self.assertFalse(
+            type_annotations.is_Input_Output_artifact_annotation(annotation))
+
+    @parameterized.parameters([
+        Input[Model],
+        Input,
+    ])
+    def test_is_input_artifact(self, annotation):
+        self.assertTrue(type_annotations.is_input_artifact(annotation))
+
+    @parameterized.parameters([
+        Output[Model],
+        Output,
+    ])
+    def test_is_not_input_artifact(self, annotation):
+        self.assertFalse(type_annotations.is_input_artifact(annotation))
+
+    @parameterized.parameters([
+        Output[Model],
+        Output[List[Model]],
+    ])
+    def test_is_output_artifact(self, annotation):
+        self.assertTrue(type_annotations.is_output_artifact(annotation))
+
+    @parameterized.parameters([
+        Input[Model],
+        Input[List[Model]],
+        Input,
+    ])
+    def test_is_not_output_artifact(self, annotation):
+        self.assertFalse(type_annotations.is_output_artifact(annotation))
 
     def test_get_io_artifact_class(self):
         self.assertEqual(
             type_annotations.get_io_artifact_class(Output[Model]), Model)
+        self.assertEqual(
+            type_annotations.get_io_artifact_class(Output[List[Model]]), Model)
+        self.assertEqual(
+            type_annotations.get_io_artifact_class(Input[List[Model]]), Model)
 
         self.assertEqual(type_annotations.get_io_artifact_class(Input), None)
         self.assertEqual(type_annotations.get_io_artifact_class(Output), None)
         self.assertEqual(type_annotations.get_io_artifact_class(Model), None)
         self.assertEqual(type_annotations.get_io_artifact_class(str), None)
 
     def test_get_io_artifact_annotation(self):
         self.assertEqual(
             type_annotations.get_io_artifact_annotation(Output[Model]),
             OutputAnnotation)
         self.assertEqual(
+            type_annotations.get_io_artifact_annotation(Output[List[Model]]),
+            OutputAnnotation)
+        self.assertEqual(
             type_annotations.get_io_artifact_annotation(Input[Model]),
             InputAnnotation)
         self.assertEqual(
+            type_annotations.get_io_artifact_annotation(Input[List[Model]]),
+            InputAnnotation)
+        self.assertEqual(
             type_annotations.get_io_artifact_annotation(Input), InputAnnotation)
         self.assertEqual(
             type_annotations.get_io_artifact_annotation(Output),
             OutputAnnotation)
 
         self.assertEqual(
             type_annotations.get_io_artifact_annotation(Model), None)
```

### Comparing `kfp-2.0.0b8/kfp/components/types/type_utils.py` & `kfp-2.0.0b9/kfp/components/types/type_utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -127,15 +127,17 @@
 
     Returns:
       The enum value of the mapped IR I/O primitive type.
 
     Raises:
       AttributeError: if type_name is not a string type.
     """
-
+    # Special handling for PipelineTaskFinalStatus, treat it as Dict type.
+    if is_task_final_status_type(param_type):
+        param_type = 'dict'
     if type(param_type) == type:
         type_name = param_type.__name__
     elif isinstance(param_type, dict):
         type_name = list(param_type.keys())[0]
     else:
         type_name = type_annotations.get_short_type_name(str(param_type))
     return _PARAMETER_TYPES_MAPPING.get(type_name.lower())
@@ -190,18 +192,14 @@
     Returns:
         True if types are compatible, and False if otherwise.
 
     Raises:
         InconsistentTypeException if types are incompatible and TYPE_CHECK==True.
     """
 
-    # Special handling for PipelineTaskFinalStatus, treat it as Dict type.
-    if is_task_final_status_type(given_type):
-        given_type = 'Dict'
-
     types_are_compatible = False
     is_parameter = is_parameter_type(str(given_type))
 
     # handle parameters
     if is_parameter:
         # Normalize parameter type names.
         if is_parameter_type(given_type):
```

### Comparing `kfp-2.0.0b8/kfp/components/types/type_utils_test.py` & `kfp-2.0.0b9/kfp/components/types/type_utils_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/utils.py` & `kfp-2.0.0b9/kfp/components/utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/utils_test.py` & `kfp-2.0.0b9/kfp/components/utils_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/v1_components.py` & `kfp-2.0.0b9/kfp/components/v1_components.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/v1_modelbase.py` & `kfp-2.0.0b9/kfp/deprecated/components/modelbase.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,27 +1,28 @@
-# Copyright 2018-2022 The Kubeflow Authors
+# Copyright 2018 The Kubeflow Authors
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-from collections import abc
-from collections import OrderedDict
+__all__ = [
+    'ModelBase',
+]
+
 import inspect
-from typing import (Any, cast, Dict, get_type_hints, List, Mapping,
-                    MutableMapping, MutableSequence, Sequence, Type, TypeVar,
-                    Union)
+from collections import abc, OrderedDict
+from typing import Any, Dict, List, Mapping, MutableMapping, MutableSequence, Sequence, Type, TypeVar, Union, cast, get_type_hints
 
 T = TypeVar('T')
 
 
 def verify_object_against_type(x: Any, typ: Type[T]) -> T:
     """Verifies that the object is compatible to the specified type (types from
     the typing package can be used)."""
@@ -34,15 +35,15 @@
 
     if typ is Any or type(typ) is TypeVar:
         return x
 
     try:  #isinstance can fail for generics
         if isinstance(x, typ):
             return cast(typ, x)
-    except Exception:
+    except:
         pass
 
     if hasattr(typ, '__origin__'):  #Handling generic types
         if typ.__origin__ is Union:  #Optional == Union
             exception_map = {}
             possible_types = typ.__args__
             if type(
@@ -63,24 +64,27 @@
             raise TypeError('\n'.join(exception_lines))
 
         #not Union => not None
         if x is None:
             raise TypeError(
                 'Error: None object is incompatible with type {}'.format(typ))
 
-        generic_type = typ.__origin__
+        #assert isinstance(x, typ.__origin__)
+        generic_type = typ.__origin__ or getattr(
+            typ, '__extra__', None
+        )  #In python <3.7 typing.List.__origin__ == None; Python 3.7 has working __origin__, but no __extra__  TODO: Remove the __extra__ once we move to Python 3.7
         if generic_type in [
                 list, List, abc.Sequence, abc.MutableSequence, Sequence,
                 MutableSequence
         ] and type(x) is not str:  #! str is also Sequence
             if not isinstance(x, generic_type):
                 raise TypeError(
                     'Error: Object "{}" is incompatible with type "{}"'.format(
                         x, typ))
-
+            # In Python <3.7 Mapping.__args__ is None.
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_type = type_args[0]
             for item in x:
                 verify_object_against_type(item, inner_type)
             return x
@@ -89,15 +93,15 @@
                 dict, Dict, abc.Mapping, abc.MutableMapping, Mapping,
                 MutableMapping, OrderedDict
         ]:
             if not isinstance(x, generic_type):
                 raise TypeError(
                     'Error: Object "{}" is incompatible with type "{}"'.format(
                         x, typ))
-
+            # In Python <3.7 Mapping.__args__ is None.
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_key_type = type_args[0]
             inner_value_type = type_args[1]
             for k, v in x.items():
                 verify_object_against_type(k, inner_key_type)
@@ -150,15 +154,17 @@
             results = {}
             exception_map = {}
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             # Union without subscripts seems useless, but semantically it should be the same as Any.
             possible_types = list(getattr(typ, '__args__', [Any]))
             #if type(None) in possible_types and struct is None: #Shortcut for Optional[] tests. Can be removed, but the exceptions will be more noisy.
             #    return None
-
+            #Hack for Python <3.7 which for some reason "simplifies" Union[bool, int, ...] to just Union[int, ...]
+            if int in possible_types:
+                possible_types = possible_types + [bool]
             for possible_type in possible_types:
                 try:
                     obj = parse_object_from_struct_based_on_type(
                         struct, possible_type)
                     results[possible_type] = obj
                 except Exception as ex:
                     if isinstance(ex, TypeError):
@@ -184,42 +190,45 @@
             raise TypeError('\n'.join(exception_lines))
         #not Union => not None
         if struct is None:
             raise TypeError(
                 'Error: None structure is incompatible with type {}'.format(
                     typ))
 
-        generic_type = typ.__origin__
+        #assert isinstance(x, typ.__origin__)
+        generic_type = typ.__origin__ or getattr(
+            typ, '__extra__', None
+        )  #In python <3.7 typing.List.__origin__ == None; Python 3.7 has working __origin__, but no __extra__  TODO: Remove the __extra__ once we move to Python 3.7
         if generic_type in [
                 list, List, abc.Sequence, abc.MutableSequence, Sequence,
                 MutableSequence
         ] and type(struct) is not str:  #! str is also Sequence
             if not isinstance(struct, generic_type):
                 raise TypeError(
                     'Error: Structure "{}" is incompatible with type "{}" - it does not have list type.'
                     .format(struct, typ))
-
+            # In Python <3.7 Mapping.__args__ is None.
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_type = type_args[0]
             return [
                 parse_object_from_struct_based_on_type(item, inner_type)
                 for item in struct
             ]
 
         elif generic_type in [
                 dict, Dict, abc.Mapping, abc.MutableMapping, Mapping,
                 MutableMapping, OrderedDict
-        ]:
+        ]:  #in Python <3.7 there is a difference between abc.Mapping and typing.Mapping
             if not isinstance(struct, generic_type):
                 raise TypeError(
                     'Error: Structure "{}" is incompatible with type "{}" - it does not have dict type.'
                     .format(struct, typ))
-
+            # In Python <3.7 Mapping.__args__ is None.
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_key_type = type_args[0]
             inner_value_type = type_args[1]
             return {
                 parse_object_from_struct_based_on_type(k, inner_key_type):
@@ -247,15 +256,15 @@
     signature = inspect.signature(obj.__init__)  #Needed for default values
     result = {}
     for python_name in signature.parameters:  #TODO: Make it possible to specify the field ordering regardless of the presence of default values
         value = getattr(obj, python_name)
         if python_name.startswith('_'):
             continue
         attr_name = serialized_names.get(python_name, python_name)
-        if hasattr(value, 'to_dict'):
+        if hasattr(value, "to_dict"):
             result[attr_name] = value.to_dict()
         elif isinstance(value, list):
             result[attr_name] = [
                 (x.to_dict() if hasattr(x, 'to_dict') else x) for x in value
             ]
         elif isinstance(value, dict):
             result[attr_name] = {
@@ -357,15 +366,15 @@
         self.__dict__.update(field_values)
 
     @classmethod
     def from_dict(cls: Type[T], struct: Mapping) -> T:
         return parse_object_from_struct_based_on_class_init(
             cls, struct, serialized_names=cls._serialized_names)
 
-    def to_dict(self) -> Dict[str, Any]:
+    def to_dict(self) -> Mapping:
         return convert_object_to_struct(
             self, serialized_names=self._serialized_names)
 
     def _get_field_names(self):
         return list(inspect.signature(self.__init__).parameters)
 
     def __repr__(self):
```

### Comparing `kfp-2.0.0b8/kfp/components/v1_structures.py` & `kfp-2.0.0b9/kfp/components/v1_structures.py`

 * *Files 2% similar despite different names*

```diff
@@ -198,16 +198,16 @@
     _serialized_names = {
         'executor_input': 'executorInput',
     }
 
     def __init__(self, executor_input: type(None) = None):
         if executor_input:
             raise RuntimeError(
-                'Executor input placeholder cannot be associated with input key'
-                '. Got %s' % executor_input)
+                f'Executor input placeholder cannot be associated with input key. Got {executor_input}'
+            )
         super().__init__(locals())
 
     def to_dict(self) -> Mapping[str, Any]:
         # Override parent implementation. Otherwise it always returns {}.
         return {'executorInput': None}
 
 
@@ -356,25 +356,23 @@
 
     def _post_init(self):
         #Checking input names for uniqueness
         self._inputs_dict = {}
         if self.inputs:
             for input in self.inputs:
                 if input.name in self._inputs_dict:
-                    raise ValueError('Non-unique input name "{}"'.format(
-                        input.name))
+                    raise ValueError(f'Non-unique input name "{input.name}"')
                 self._inputs_dict[input.name] = input
 
         #Checking output names for uniqueness
         self._outputs_dict = {}
         if self.outputs:
             for output in self.outputs:
                 if output.name in self._outputs_dict:
-                    raise ValueError('Non-unique output name "{}"'.format(
-                        output.name))
+                    raise ValueError(f'Non-unique output name "{output.name}"')
                 self._outputs_dict[output.name] = output
 
         if isinstance(self.implementation, ContainerImplementation):
             container = self.implementation.container
 
             if container.file_outputs:
                 for output_name, path in container.file_outputs.items():
@@ -396,31 +394,29 @@
                 elif isinstance(
                         arg,
                     (InputUriPlaceholder, InputValuePlaceholder,
                      InputPathPlaceholder, IsPresentPlaceholder,
                      InputMetadataPlaceholder, InputOutputPortNamePlaceholder)):
                     if arg.input_name not in self._inputs_dict:
                         raise TypeError(
-                            'Argument "{}" references non-existing input.'
-                            .format(arg))
+                            f'Argument "{arg}" references non-existing input.')
                 elif isinstance(arg,
                                 (OutputUriPlaceholder, OutputPathPlaceholder)):
                     if arg.output_name not in self._outputs_dict:
                         raise TypeError(
-                            'Argument "{}" references non-existing output.'
-                            .format(arg))
+                            f'Argument "{arg}" references non-existing output.')
                 elif isinstance(arg, ConcatPlaceholder):
                     for arg2 in arg.items:
                         verify_arg(arg2)
                 elif isinstance(arg, IfPlaceholder):
                     verify_arg(arg.if_structure.condition)
                     verify_arg(arg.if_structure.then_value)
                     verify_arg(arg.if_structure.else_value)
                 else:
-                    raise TypeError('Unexpected argument "{}"'.format(arg))
+                    raise TypeError(f'Unexpected argument "{arg}"')
 
             verify_arg(container.command)
             verify_arg(container.args)
 
         if isinstance(self.implementation, GraphImplementation):
             graph = self.implementation.graph
 
@@ -435,16 +431,16 @@
                 for task in graph.tasks.values():
                     if task.arguments is not None:
                         for argument in task.arguments.values():
                             if isinstance(
                                     argument, GraphInputArgument
                             ) and argument.graph_input.input_name not in self._inputs_dict:
                                 raise TypeError(
-                                    'Argument "{}" references non-existing input.'
-                                    .format(argument))
+                                    f'Argument "{argument}" references non-existing input.'
+                                )
 
     def save(self, file_path: str):
         """Saves the component definition to file.
 
         It can be shared online and later loaded using the
         load_component function.
         """
@@ -785,16 +781,16 @@
             task_dependencies[task_id] = dependencies
             if task.arguments is not None:
                 for argument in task.arguments.values():
                     if isinstance(argument, TaskOutputArgument):
                         dependencies.add(argument.task_output.task_id)
                         if argument.task_output.task_id not in self.tasks:
                             raise TypeError(
-                                'Argument "{}" references non-existing task.'
-                                .format(argument))
+                                f'Argument "{argument}" references non-existing task.'
+                            )
 
         #Topologically sorting tasks to detect cycles
         task_dependents = {k: set() for k in task_dependencies.keys()}
         for task_id, dependencies in task_dependencies.items():
             for dependency in dependencies:
                 task_dependents[dependency].add(task_id)
         task_number_of_remaining_dependencies = {
@@ -820,16 +816,17 @@
                 for k, v in task_number_of_remaining_dependencies.items()
                 if v > 0
             }
             task_wth_minimal_number_of_unsatisfied_dependencies = min(
                 tasks_with_unsatisfied_dependencies.keys(),
                 key=lambda task_id: tasks_with_unsatisfied_dependencies[task_id]
             )
-            raise ValueError('Task "{}" has cyclical dependency.'.format(
-                task_wth_minimal_number_of_unsatisfied_dependencies))
+            raise ValueError(
+                f'Task "{task_wth_minimal_number_of_unsatisfied_dependencies}" has cyclical dependency.'
+            )
 
         self._toposorted_tasks = sorted_tasks
 
 
 class GraphImplementation(ModelBase):
     """Represents the graph component implementation."""
```

### Comparing `kfp-2.0.0b8/kfp/components/yaml_component.py` & `kfp-2.0.0b9/kfp/components/yaml_component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/components/yaml_component_test.py` & `kfp-2.0.0b9/kfp/components/yaml_component_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/__main__.py` & `kfp-2.0.0b9/kfp/deprecated/__main__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/_auth.py` & `kfp-2.0.0b9/kfp/deprecated/_auth.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/_client.py` & `kfp-2.0.0b9/kfp/deprecated/_client.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/_config.py` & `kfp-2.0.0b9/kfp/deprecated/_config.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/_local_client.py` & `kfp-2.0.0b9/kfp/deprecated/_local_client.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/auth/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/auth/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/auth/_satvolumecredentials.py` & `kfp-2.0.0b9/kfp/deprecated/auth/_satvolumecredentials.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/auth/_tokencredentialsbase.py` & `kfp-2.0.0b9/kfp/deprecated/auth/_tokencredentialsbase.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/aws.py` & `kfp-2.0.0b9/kfp/deprecated/aws.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/azure.py` & `kfp-2.0.0b9/kfp/deprecated/azure.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/cli.py` & `kfp-2.0.0b9/kfp/deprecated/cli/cli.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/components.py` & `kfp-2.0.0b9/kfp/deprecated/cli/components.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/components_test.py` & `kfp-2.0.0b9/kfp/deprecated/cli/components_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/dev_env.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/dev_env.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/dev_env_test.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/dev_env_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/gcp.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/gcp.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/gcp_test.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/gcp_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/kubernetes_cluster.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/kubernetes_cluster.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/kubernetes_cluster_test.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/kubernetes_cluster_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/utility.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/utility.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me/utility_test.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me/utility_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/diagnose_me_cli.py` & `kfp-2.0.0b9/kfp/deprecated/cli/diagnose_me_cli.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/experiment.py` & `kfp-2.0.0b9/kfp/deprecated/cli/experiment.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/output.py` & `kfp-2.0.0b9/kfp/deprecated/cli/output.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/pipeline.py` & `kfp-2.0.0b9/kfp/deprecated/cli/pipeline.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/recurring_run.py` & `kfp-2.0.0b9/kfp/deprecated/cli/recurring_run.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/cli/run.py` & `kfp-2.0.0b9/kfp/deprecated/cli/run.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/_data_passing_rewriter.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/_data_passing_rewriter.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/_data_passing_using_volume.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/_data_passing_using_volume.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/_default_transformers.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/_default_transformers.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/_k8s_helper.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/_k8s_helper.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/_op_to_template.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/_op_to_template.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/compiler.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/compiler.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/main.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/main.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/v2_compat.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/v2_compat.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/compiler/v2_compatible_compiler_test.py` & `kfp-2.0.0b9/kfp/deprecated/compiler/v2_compatible_compiler_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/components/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_airflow_op.py` & `kfp-2.0.0b9/kfp/deprecated/components/_airflow_op.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_component_store.py` & `kfp-2.0.0b9/kfp/deprecated/components/_component_store.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_components.py` & `kfp-2.0.0b9/kfp/deprecated/components/_components.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_data_passing.py` & `kfp-2.0.0b9/kfp/deprecated/components/_data_passing.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_dynamic.py` & `kfp-2.0.0b9/kfp/deprecated/components/_dynamic.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_key_value_store.py` & `kfp-2.0.0b9/kfp/deprecated/components/_key_value_store.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_naming.py` & `kfp-2.0.0b9/kfp/deprecated/components/_naming.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_python_op.py` & `kfp-2.0.0b9/kfp/deprecated/components/_python_op.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_python_to_graph_component.py` & `kfp-2.0.0b9/kfp/deprecated/components/_python_to_graph_component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_structures.py` & `kfp-2.0.0b9/kfp/deprecated/components/_structures.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/_yaml_utils.py` & `kfp-2.0.0b9/kfp/deprecated/components/_yaml_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/modelbase.py` & `kfp-2.0.0b9/kfp/components/v1_modelbase.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,49 +1,48 @@
-# Copyright 2018 The Kubeflow Authors
+# Copyright 2018-2022 The Kubeflow Authors
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-__all__ = [
-    'ModelBase',
-]
-
+from collections import abc
+from collections import OrderedDict
 import inspect
-from collections import abc, OrderedDict
-from typing import Any, Dict, List, Mapping, MutableMapping, MutableSequence, Sequence, Type, TypeVar, Union, cast, get_type_hints
+from typing import (Any, cast, Dict, get_type_hints, List, Mapping,
+                    MutableMapping, MutableSequence, Sequence, Type, TypeVar,
+                    Union)
 
 T = TypeVar('T')
 
 
 def verify_object_against_type(x: Any, typ: Type[T]) -> T:
     """Verifies that the object is compatible to the specified type (types from
     the typing package can be used)."""
     #TODO: Merge with parse_object_from_struct_based_on_type which has almost the same code
     if typ is type(None):
         if x is None:
             return x
         else:
-            raise TypeError('Error: Object "{}" is not None.'.format(x))
+            raise TypeError(f'Error: Object "{x}" is not None.')
 
     if typ is Any or type(typ) is TypeVar:
         return x
 
     try:  #isinstance can fail for generics
         if isinstance(x, typ):
             return cast(typ, x)
-    except:
+    except Exception:
         pass
 
     if hasattr(typ, '__origin__'):  #Handling generic types
         if typ.__origin__ is Union:  #Optional == Union
             exception_map = {}
             possible_types = typ.__args__
             if type(
@@ -55,84 +54,77 @@
                     verify_object_against_type(x, possible_type)
                     return x
                 except Exception as ex:
                     exception_map[possible_type] = ex
             #exception_lines = ['Exception for type {}: {}.'.format(t, e) for t, e in exception_map.items()]
             exception_lines = [str(e) for t, e in exception_map.items()]
             exception_lines.append(
-                'Error: Object "{}" is incompatible with type "{}".'.format(
-                    x, typ))
+                f'Error: Object "{x}" is incompatible with type "{typ}".')
             raise TypeError('\n'.join(exception_lines))
 
         #not Union => not None
         if x is None:
             raise TypeError(
-                'Error: None object is incompatible with type {}'.format(typ))
+                f'Error: None object is incompatible with type {typ}')
 
-        #assert isinstance(x, typ.__origin__)
-        generic_type = typ.__origin__ or getattr(
-            typ, '__extra__', None
-        )  #In python <3.7 typing.List.__origin__ == None; Python 3.7 has working __origin__, but no __extra__  TODO: Remove the __extra__ once we move to Python 3.7
+        generic_type = typ.__origin__
         if generic_type in [
                 list, List, abc.Sequence, abc.MutableSequence, Sequence,
                 MutableSequence
         ] and type(x) is not str:  #! str is also Sequence
             if not isinstance(x, generic_type):
                 raise TypeError(
-                    'Error: Object "{}" is incompatible with type "{}"'.format(
-                        x, typ))
-            # In Python <3.7 Mapping.__args__ is None.
+                    f'Error: Object "{x}" is incompatible with type "{typ}"')
+
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_type = type_args[0]
             for item in x:
                 verify_object_against_type(item, inner_type)
             return x
 
         elif generic_type in [
                 dict, Dict, abc.Mapping, abc.MutableMapping, Mapping,
                 MutableMapping, OrderedDict
         ]:
             if not isinstance(x, generic_type):
                 raise TypeError(
-                    'Error: Object "{}" is incompatible with type "{}"'.format(
-                        x, typ))
-            # In Python <3.7 Mapping.__args__ is None.
+                    f'Error: Object "{x}" is incompatible with type "{typ}"')
+
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_key_type = type_args[0]
             inner_value_type = type_args[1]
             for k, v in x.items():
                 verify_object_against_type(k, inner_key_type)
                 verify_object_against_type(v, inner_value_type)
             return x
 
         else:
             raise TypeError(
-                'Error: Unsupported generic type "{}". type.__origin__ or type.__extra__ == "{}"'
-                .format(typ, generic_type))
+                f'Error: Unsupported generic type "{typ}". type.__origin__ or type.__extra__ == "{generic_type}"'
+            )
 
-    raise TypeError('Error: Object "{}" is incompatible with type "{}"'.format(
-        x, typ))
+    raise TypeError(f'Error: Object "{x}" is incompatible with type "{typ}"')
 
 
 def parse_object_from_struct_based_on_type(struct: Any, typ: Type[T]) -> T:
     """Constructs an object from structure (usually dict) based on type.
 
     Supports list and dict types from the typing package plus Optional[]
     and Union[] types. If some type is a class that has .from_dict class
     method, that method is used for object construction.
     """
     if typ is type(None):
         if struct is None:
             return None
         else:
-            raise TypeError('Error: Structure "{}" is not None.'.format(struct))
+            raise TypeError(f'Error: Structure "{struct}" is not None.')
 
     if typ is Any or type(typ) is TypeVar:
         return struct
 
     try:  #isinstance can fail for generics
         #if (isinstance(struct, typ)
         #    and not (typ is Sequence and type(struct) is str) #! str is also Sequence
@@ -143,111 +135,104 @@
     except:
         pass
     if hasattr(typ, 'from_dict'):
         try:  #More informative errors
             return typ.from_dict(struct)
         except Exception as ex:
             raise TypeError(
-                'Error: {}.from_dict(struct={}) failed with exception:\n{}'
-                .format(typ.__name__, struct, str(ex)))
+                f'Error: {typ.__name__}.from_dict(struct={struct}) failed with exception:\n{str(ex)}'
+            )
     if hasattr(typ, '__origin__'):  #Handling generic types
         if typ.__origin__ is Union:  #Optional == Union
             results = {}
             exception_map = {}
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             # Union without subscripts seems useless, but semantically it should be the same as Any.
             possible_types = list(getattr(typ, '__args__', [Any]))
             #if type(None) in possible_types and struct is None: #Shortcut for Optional[] tests. Can be removed, but the exceptions will be more noisy.
             #    return None
-            #Hack for Python <3.7 which for some reason "simplifies" Union[bool, int, ...] to just Union[int, ...]
-            if int in possible_types:
-                possible_types = possible_types + [bool]
+
             for possible_type in possible_types:
                 try:
                     obj = parse_object_from_struct_based_on_type(
                         struct, possible_type)
                     results[possible_type] = obj
                 except Exception as ex:
                     if isinstance(ex, TypeError):
                         exception_map[possible_type] = ex
                     else:
                         exception_map[
-                            possible_type] = 'Unexpected exception when trying to convert structure "{}" to type "{}": {}: {}'.format(
-                                struct, typ, type(ex), ex)
+                            possible_type] = f'Unexpected exception when trying to convert structure "{struct}" to type "{typ}": {type(ex)}: {ex}'
 
             #Single successful parsing.
             if len(results) == 1:
                 return list(results.values())[0]
 
             if len(results) > 1:
                 raise TypeError(
-                    'Error: Structure "{}" is ambiguous. It can be parsed to multiple types: {}.'
-                    .format(struct, list(results.keys())))
+                    f'Error: Structure "{struct}" is ambiguous. It can be parsed to multiple types: {list(results.keys())}.'
+                )
 
             exception_lines = [str(e) for t, e in exception_map.items()]
             exception_lines.append(
-                'Error: Structure "{}" is incompatible with type "{}" - none of the types in Union are compatible.'
-                .format(struct, typ))
+                f'Error: Structure "{struct}" is incompatible with type "{typ}" - none of the types in Union are compatible.'
+            )
             raise TypeError('\n'.join(exception_lines))
         #not Union => not None
         if struct is None:
             raise TypeError(
-                'Error: None structure is incompatible with type {}'.format(
-                    typ))
+                f'Error: None structure is incompatible with type {typ}')
 
-        #assert isinstance(x, typ.__origin__)
-        generic_type = typ.__origin__ or getattr(
-            typ, '__extra__', None
-        )  #In python <3.7 typing.List.__origin__ == None; Python 3.7 has working __origin__, but no __extra__  TODO: Remove the __extra__ once we move to Python 3.7
+        generic_type = typ.__origin__
         if generic_type in [
                 list, List, abc.Sequence, abc.MutableSequence, Sequence,
                 MutableSequence
         ] and type(struct) is not str:  #! str is also Sequence
             if not isinstance(struct, generic_type):
                 raise TypeError(
-                    'Error: Structure "{}" is incompatible with type "{}" - it does not have list type.'
-                    .format(struct, typ))
-            # In Python <3.7 Mapping.__args__ is None.
+                    f'Error: Structure "{struct}" is incompatible with type "{typ}" - it does not have list type.'
+                )
+
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_type = type_args[0]
             return [
                 parse_object_from_struct_based_on_type(item, inner_type)
                 for item in struct
             ]
 
         elif generic_type in [
                 dict, Dict, abc.Mapping, abc.MutableMapping, Mapping,
                 MutableMapping, OrderedDict
-        ]:  #in Python <3.7 there is a difference between abc.Mapping and typing.Mapping
+        ]:
             if not isinstance(struct, generic_type):
                 raise TypeError(
-                    'Error: Structure "{}" is incompatible with type "{}" - it does not have dict type.'
-                    .format(struct, typ))
-            # In Python <3.7 Mapping.__args__ is None.
+                    f'Error: Structure "{struct}" is incompatible with type "{typ}" - it does not have dict type.'
+                )
+
             # In Python 3.9 typ.__args__ does not exist when the generic type does not have subscripts
             type_args = typ.__args__ if getattr(
                 typ, '__args__', None) is not None else (Any, Any)
             inner_key_type = type_args[0]
             inner_value_type = type_args[1]
             return {
                 parse_object_from_struct_based_on_type(k, inner_key_type):
                 parse_object_from_struct_based_on_type(v, inner_value_type)
                 for k, v in struct.items()
             }
 
         else:
             raise TypeError(
-                'Error: Unsupported generic type "{}". type.__origin__ or type.__extra__ == "{}"'
-                .format(typ, generic_type))
+                f'Error: Unsupported generic type "{typ}". type.__origin__ or type.__extra__ == "{generic_type}"'
+            )
 
     raise TypeError(
-        'Error: Structure "{}" is incompatible with type "{}". Structure is not the instance of the type, the type does not have .from_dict method and is not generic.'
-        .format(struct, typ))
+        f'Error: Structure "{struct}" is incompatible with type "{typ}". Structure is not the instance of the type, the type does not have .from_dict method and is not generic.'
+    )
 
 
 def convert_object_to_struct(obj, serialized_names: Mapping[str, str] = {}):
     """Converts an object to structure (usually a dict).
 
     Serializes all properties that do not start with underscores. If the
     type of some property is a class that has .to_dict class method,
@@ -256,15 +241,15 @@
     signature = inspect.signature(obj.__init__)  #Needed for default values
     result = {}
     for python_name in signature.parameters:  #TODO: Make it possible to specify the field ordering regardless of the presence of default values
         value = getattr(obj, python_name)
         if python_name.startswith('_'):
             continue
         attr_name = serialized_names.get(python_name, python_name)
-        if hasattr(value, "to_dict"):
+        if hasattr(value, 'to_dict'):
             result[attr_name] = value.to_dict()
         elif isinstance(value, list):
             result[attr_name] = [
                 (x.to_dict() if hasattr(x, 'to_dict') else x) for x in value
             ]
         elif isinstance(value, dict):
             result[attr_name] = {
@@ -300,16 +285,16 @@
     forbidden_struct_keys = set(
         serialized_names_to_pythonic.values()).difference(
             serialized_names_to_pythonic.keys())
     args = {}
     for original_name, value in struct.items():
         if original_name in forbidden_struct_keys:
             raise ValueError(
-                'Use "{}" key instead of pythonic key "{}" in the structure: {}.'
-                .format(serialized_names[original_name], original_name, struct))
+                f'Use "{serialized_names[original_name]}" key instead of pythonic key "{original_name}" in the structure: {struct}.'
+            )
         python_name = serialized_names_to_pythonic.get(original_name,
                                                        original_name)
         param_type = parameter_types.get(python_name, None)
         if param_type is not None:
             args[python_name] = parse_object_from_struct_based_on_type(
                 value, param_type)
         else:
@@ -357,24 +342,24 @@
         for k, v in field_values.items():
             parameter_type = parameter_types.get(k, None)
             if parameter_type is not None:
                 try:
                     verify_object_against_type(v, parameter_type)
                 except Exception as e:
                     raise TypeError(
-                        'Argument for {} is not compatible with type "{}". Exception: {}'
-                        .format(k, parameter_type, e))
+                        f'Argument for {k} is not compatible with type "{parameter_type}". Exception: {e}'
+                    )
         self.__dict__.update(field_values)
 
     @classmethod
     def from_dict(cls: Type[T], struct: Mapping) -> T:
         return parse_object_from_struct_based_on_class_init(
             cls, struct, serialized_names=cls._serialized_names)
 
-    def to_dict(self) -> Mapping:
+    def to_dict(self) -> Dict[str, Any]:
         return convert_object_to_struct(
             self, serialized_names=self._serialized_names)
 
     def _get_field_names(self):
         return list(inspect.signature(self.__init__).parameters)
 
     def __repr__(self):
```

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/type_annotation_utils.py` & `kfp-2.0.0b9/kfp/deprecated/components/type_annotation_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/components/type_annotation_utils_test.py` & `kfp-2.0.0b9/kfp/deprecated/components/type_annotation_utils_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/containers/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/_build_image_api.py` & `kfp-2.0.0b9/kfp/deprecated/containers/_build_image_api.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/_cache.py` & `kfp-2.0.0b9/kfp/deprecated/containers/_cache.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/_component_builder.py` & `kfp-2.0.0b9/kfp/deprecated/containers/_component_builder.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/_container_builder.py` & `kfp-2.0.0b9/kfp/deprecated/containers/_container_builder.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/_gcs_helper.py` & `kfp-2.0.0b9/kfp/deprecated/containers/_gcs_helper.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/_k8s_job_helper.py` & `kfp-2.0.0b9/kfp/deprecated/containers/_k8s_job_helper.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/entrypoint.py` & `kfp-2.0.0b9/kfp/deprecated/containers/entrypoint.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/containers/entrypoint_utils.py` & `kfp-2.0.0b9/kfp/deprecated/containers/entrypoint_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_component.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_component.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_component_bridge.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_component_bridge.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_container_op.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_container_op.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_container_op_test.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_container_op_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_for_loop.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_for_loop.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_metadata.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_metadata.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_ops_group.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_ops_group.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_pipeline.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_pipeline.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_pipeline_param.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_pipeline_param.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_pipeline_volume.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_pipeline_volume.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_resource_op.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_resource_op.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_volume_op.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_volume_op.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/_volume_snapshot_op.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/_volume_snapshot_op.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/artifact.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/artifact.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/artifact_utils.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/artifact_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/component_spec.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/component_spec.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/component_spec_test.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/component_spec_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/data_passing_methods.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/data_passing_methods.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/dsl_utils.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/dsl_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/dsl_utils_test.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/dsl_utils_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/extensions/kubernetes.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/extensions/kubernetes.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/io_types.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/io_types.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/metrics_utils.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/metrics_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/metrics_utils_test.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/metrics_utils_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/serialization_utils.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/serialization_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/serialization_utils_test.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/serialization_utils_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/type_utils.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/type_utils.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/dsl/types.py` & `kfp-2.0.0b9/kfp/deprecated/dsl/types.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/gcp.py` & `kfp-2.0.0b9/kfp/deprecated/gcp.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/notebook/__init__.py` & `kfp-2.0.0b9/kfp/deprecated/notebook/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/notebook/_magic.py` & `kfp-2.0.0b9/kfp/deprecated/notebook/_magic.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/deprecated/onprem.py` & `kfp-2.0.0b9/kfp/deprecated/onprem.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/dsl/__init__.py` & `kfp-2.0.0b9/kfp/dsl/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/registry/__init__.py` & `kfp-2.0.0b9/kfp/registry/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/registry/context/__init__.py` & `kfp-2.0.0b9/kfp/registry/context/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/registry/context/default_pkg_dev.json` & `kfp-2.0.0b9/kfp/registry/context/default_pkg_dev.json`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/registry/context/kfp_pkg_dev.json` & `kfp-2.0.0b9/kfp/registry/context/kfp_pkg_dev.json`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/registry/registry_client.py` & `kfp-2.0.0b9/kfp/registry/registry_client.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/registry/registry_client_test.py` & `kfp-2.0.0b9/kfp/registry/registry_client_test.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/v2/__init__.py` & `kfp-2.0.0b9/kfp/v2/__init__.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/v2/compiler.py` & `kfp-2.0.0b9/kfp/v2/compiler.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/v2/components.py` & `kfp-2.0.0b9/kfp/v2/components.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp/v2/dsl.py` & `kfp-2.0.0b9/kfp/v2/dsl.py`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp.egg-info/PKG-INFO` & `kfp-2.0.0b9/kfp.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kfp
-Version: 2.0.0b8
+Version: 2.0.0b9
 Summary: Kubeflow Pipelines SDK
 Home-page: https://github.com/kubeflow/pipelines
 Author: The Kubeflow Authors
 License: UNKNOWN
 Project-URL: Documentation, https://kubeflow-pipelines.readthedocs.io/en/stable/
 Project-URL: Bug Tracker, https://github.com/kubeflow/pipelines/issues
 Project-URL: Source, https://github.com/kubeflow/pipelines/tree/master/sdk
```

### Comparing `kfp-2.0.0b8/kfp.egg-info/SOURCES.txt` & `kfp-2.0.0b9/kfp.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/kfp.egg-info/requires.txt` & `kfp-2.0.0b9/kfp.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/requirements.in` & `kfp-2.0.0b9/requirements.in`

 * *Files identical despite different names*

### Comparing `kfp-2.0.0b8/setup.py` & `kfp-2.0.0b9/setup.py`

 * *Files identical despite different names*

