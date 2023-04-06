# Comparing `tmp/sampo-0.1.1.98.tar.gz` & `tmp/sampo-0.1.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sampo-0.1.1.98.tar", max compression
+gzip compressed data, was "sampo-0.1.1.99.tar", max compression
```

## Comparing `sampo-0.1.1.98.tar` & `sampo-0.1.1.99.tar`

### file list

```diff
@@ -1,106 +1,106 @@
--rw-r--r--   0        0        0     1513 2022-12-27 09:46:58.876000 sampo-0.1.1.98/LICENSE
--rw-r--r--   0        0        0      690 2023-02-14 12:57:55.606948 sampo-0.1.1.98/pyproject.toml
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/__init__.py
--rw-r--r--   0        0        0      322 2022-12-27 10:41:54.852928 sampo-0.1.1.98/sampo/generator/__init__.py
--rw-r--r--   0        0        0     3083 2023-02-02 13:01:55.047773 sampo-0.1.1.98/sampo/generator/base.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/generator/config/__init__.py
--rw-r--r--   0        0        0      943 2022-12-27 10:41:54.852928 sampo-0.1.1.98/sampo/generator/config/gen_counts.py
--rw-r--r--   0        0        0    10216 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/generator/config/worker_req.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/generator/environment/__init__.py
--rw-r--r--   0        0        0     4985 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/generator/environment/contractor.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/generator/pipeline/__init__.py
--rw-r--r--   0        0        0    11972 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/generator/pipeline/cluster.py
--rw-r--r--   0        0        0     3101 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/generator/pipeline/extension.py
--rw-r--r--   0        0        0     9265 2023-01-19 10:15:18.573875 sampo-0.1.1.98/sampo/generator/pipeline/project.py
--rw-r--r--   0        0        0      223 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/generator/pipeline/types.py
--rw-r--r--   0        0        0      224 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/generator/types.py
--rw-r--r--   0        0        0        3 2023-01-19 10:15:18.574872 sampo-0.1.1.98/sampo/generator/utils/__init__.py
--rw-r--r--   0        0        0      453 2023-01-19 10:15:18.574872 sampo-0.1.1.98/sampo/generator/utils/graph_node_operations.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/metrics/__init__.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/metrics/resources_in_time/__init__.py
--rw-r--r--   0        0        0     4806 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/metrics/resources_in_time/base.py
--rw-r--r--   0        0        0     5110 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/metrics/resources_in_time/binary_search.py
--rw-r--r--   0        0        0     5114 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/metrics/resources_in_time/newton_conjugate_gradient.py
--rw-r--r--   0        0        0     3860 2022-12-27 10:41:54.837308 sampo-0.1.1.98/sampo/metrics/resources_in_time/service.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/scheduler/__init__.py
--rw-r--r--   0        0        0     4405 2023-02-13 10:39:37.312306 sampo-0.1.1.98/sampo/scheduler/base.py
--rw-r--r--   0        0        0     2001 2023-02-14 12:42:23.302627 sampo-0.1.1.98/sampo/scheduler/generate.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.98/sampo/scheduler/genetic/__init__.py
--rw-r--r--   0        0        0     6631 2023-02-14 11:51:10.538278 sampo-0.1.1.98/sampo/scheduler/genetic/base.py
--rw-r--r--   0        0        0     5049 2023-02-13 10:39:37.312306 sampo-0.1.1.98/sampo/scheduler/genetic/converter.py
--rw-r--r--   0        0        0    20267 2023-02-14 12:57:55.589831 sampo-0.1.1.98/sampo/scheduler/genetic/operators.py
--rw-r--r--   0        0        0    17242 2023-02-14 12:58:39.717130 sampo-0.1.1.98/sampo/scheduler/genetic/schedule_builder.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.98/sampo/scheduler/heft/__init__.py
--rw-r--r--   0        0        0     7591 2023-02-13 10:39:37.312306 sampo-0.1.1.98/sampo/scheduler/heft/base.py
--rw-r--r--   0        0        0     2586 2022-12-27 10:41:54.821687 sampo-0.1.1.98/sampo/scheduler/heft/prioritization.py
--rw-r--r--   0        0        0     2845 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/scheduler/heft/time_computaion.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.98/sampo/scheduler/multi_agency/__init__.py
--rw-r--r--   0        0        0     5560 2023-01-19 10:15:18.581372 sampo-0.1.1.98/sampo/scheduler/multi_agency/block_generator.py
--rw-r--r--   0        0        0     2564 2022-12-27 10:41:54.821687 sampo-0.1.1.98/sampo/scheduler/multi_agency/block_graph.py
--rw-r--r--   0        0        0     3102 2023-01-19 10:15:18.587075 sampo-0.1.1.98/sampo/scheduler/multi_agency/block_validation.py
--rw-r--r--   0        0        0     6212 2023-01-19 10:15:18.589089 sampo-0.1.1.98/sampo/scheduler/multi_agency/multi_agency.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.98/sampo/scheduler/resource/__init__.py
--rw-r--r--   0        0        0     1020 2022-12-27 10:41:54.806065 sampo-0.1.1.98/sampo/scheduler/resource/average_req.py
--rw-r--r--   0        0        0     1267 2022-12-27 10:41:54.806065 sampo-0.1.1.98/sampo/scheduler/resource/base.py
--rw-r--r--   0        0        0     1706 2022-12-27 10:41:54.806065 sampo-0.1.1.98/sampo/scheduler/resource/coordinate_descent.py
--rw-r--r--   0        0        0     1977 2022-12-27 10:41:54.806065 sampo-0.1.1.98/sampo/scheduler/resource/full_scan.py
--rw-r--r--   0        0        0      729 2022-12-27 10:41:54.806065 sampo-0.1.1.98/sampo/scheduler/resource/identity.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.98/sampo/scheduler/timeline/__init__.py
--rw-r--r--   0        0        0     2734 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/scheduler/timeline/base.py
--rw-r--r--   0        0        0     9183 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/scheduler/timeline/just_in_time_timeline.py
--rw-r--r--   0        0        0    17633 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/scheduler/timeline/momentum_timeline.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.98/sampo/scheduler/topological/__init__.py
--rw-r--r--   0        0        0     8408 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/scheduler/topological/base.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.587367 sampo-0.1.1.98/sampo/scheduler/utils/__init__.py
--rw-r--r--   0        0        0     8854 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/scheduler/utils/local_optimization.py
--rw-r--r--   0        0        0     3037 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/scheduler/utils/multi_contractor.py
--rw-r--r--   0        0        0     1998 2022-12-27 10:41:54.790444 sampo-0.1.1.98/sampo/scheduler/utils/obstruction.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.587367 sampo-0.1.1.98/sampo/schemas/__init__.py
--rw-r--r--   0        0        0     4435 2023-01-19 10:15:18.591599 sampo-0.1.1.98/sampo/schemas/contractor.py
--rw-r--r--   0        0        0      113 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/schemas/exceptions.py
--rw-r--r--   0        0        0    12115 2023-02-14 11:44:34.885448 sampo-0.1.1.98/sampo/schemas/graph.py
--rw-r--r--   0        0        0      322 2022-12-27 10:41:54.790444 sampo-0.1.1.98/sampo/schemas/identifiable.py
--rw-r--r--   0        0        0     4185 2022-12-27 10:41:54.790444 sampo-0.1.1.98/sampo/schemas/interval.py
--rw-r--r--   0        0        0     3363 2023-01-19 13:47:31.461861 sampo-0.1.1.98/sampo/schemas/requirements.py
--rw-r--r--   0        0        0     3223 2023-01-19 10:15:18.597323 sampo-0.1.1.98/sampo/schemas/resources.py
--rw-r--r--   0        0        0     8731 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/schemas/schedule.py
--rw-r--r--   0        0        0     2045 2022-12-27 11:20:19.072277 sampo-0.1.1.98/sampo/schemas/schedule_spec.py
--rw-r--r--   0        0        0     4775 2023-02-13 10:39:37.327927 sampo-0.1.1.98/sampo/schemas/scheduled_work.py
--rw-r--r--   0        0        0    14647 2022-12-27 10:41:54.774823 sampo-0.1.1.98/sampo/schemas/serializable.py
--rw-r--r--   0        0        0     2455 2022-12-27 10:43:19.445862 sampo-0.1.1.98/sampo/schemas/sorted_list.py
--rw-r--r--   0        0        0     4211 2022-12-27 10:41:54.774823 sampo-0.1.1.98/sampo/schemas/time.py
--rw-r--r--   0        0        0      672 2023-02-14 12:55:45.907922 sampo-0.1.1.98/sampo/schemas/time_estimator.py
--rw-r--r--   0        0        0      886 2023-02-13 10:39:37.343548 sampo-0.1.1.98/sampo/schemas/types.py
--rw-r--r--   0        0        0      987 2023-01-19 10:15:18.601354 sampo-0.1.1.98/sampo/schemas/utils.py
--rw-r--r--   0        0        0     4651 2023-01-19 10:15:18.601354 sampo-0.1.1.98/sampo/schemas/works.py
--rw-r--r--   0        0        0      209 2023-01-19 10:15:18.601354 sampo-0.1.1.98/sampo/structurator/__init__.py
--rw-r--r--   0        0        0     8992 2023-02-13 10:39:37.343548 sampo-0.1.1.98/sampo/structurator/base.py
--rw-r--r--   0        0        0     5059 2023-01-19 10:15:18.601354 sampo-0.1.1.98/sampo/structurator/graph_insertion.py
--rw-r--r--   0        0        0      679 2023-01-19 10:15:18.601354 sampo-0.1.1.98/sampo/structurator/light_modifications.py
--rw-r--r--   0        0        0     5132 2022-12-27 10:43:03.022066 sampo-0.1.1.98/sampo/structurator/metric.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.587367 sampo-0.1.1.98/sampo/utilities/__init__.py
--rw-r--r--   0        0        0     1336 2022-12-27 10:41:54.774823 sampo-0.1.1.98/sampo/utilities/base_opt.py
--rw-r--r--   0        0        0     1061 2022-12-27 10:41:54.774823 sampo-0.1.1.98/sampo/utilities/collections.py
--rw-r--r--   0        0        0     1291 2022-12-27 10:41:54.774823 sampo-0.1.1.98/sampo/utilities/datetime.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.602989 sampo-0.1.1.98/sampo/utilities/generation/__init__.py
--rw-r--r--   0        0        0     1559 2023-01-19 10:15:18.607483 sampo-0.1.1.98/sampo/utilities/generation/work_graph.py
--rw-r--r--   0        0        0     1127 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/priority_queue.py
--rw-r--r--   0        0        0      189 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/resource_cost.py
--rw-r--r--   0        0        0      374 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/resource_path.py
--rw-r--r--   0        0        0     3003 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/sampler/__init__.py
--rw-r--r--   0        0        0     1706 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/sampler/requirements.py
--rw-r--r--   0        0        0      436 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/sampler/resources.py
--rw-r--r--   0        0        0      262 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/sampler/types.py
--rw-r--r--   0        0        0     1619 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/sampler/works.py
--rw-r--r--   0        0        0     3668 2023-01-19 10:15:18.607494 sampo-0.1.1.98/sampo/utilities/schedule.py
--rw-r--r--   0        0        0     3770 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/serializers.py
--rw-r--r--   0        0        0      704 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/stack.py
--rw-r--r--   0        0        0     1833 2022-12-27 10:41:54.759201 sampo-0.1.1.98/sampo/utilities/task_name.py
--rw-r--r--   0        0        0     8587 2023-02-13 10:55:30.091609 sampo-0.1.1.98/sampo/utilities/validation.py
--rw-r--r--   0        0        0        0 2022-12-27 10:41:54.602989 sampo-0.1.1.98/sampo/utilities/visualization/__init__.py
--rw-r--r--   0        0        0     1076 2022-12-27 10:41:54.743579 sampo-0.1.1.98/sampo/utilities/visualization/base.py
--rw-r--r--   0        0        0    11917 2022-12-27 10:41:54.743579 sampo-0.1.1.98/sampo/utilities/visualization/resources.py
--rw-r--r--   0        0        0     2392 2023-02-02 13:01:55.050765 sampo-0.1.1.98/sampo/utilities/visualization/schedule.py
--rw-r--r--   0        0        0     8584 2022-12-27 10:41:54.743579 sampo-0.1.1.98/sampo/utilities/visualization/work_graph.py
--rw-r--r--   0        0        0     1484 1970-01-01 00:00:00.000000 sampo-0.1.1.98/setup.py
--rw-r--r--   0        0        0      826 1970-01-01 00:00:00.000000 sampo-0.1.1.98/PKG-INFO
+-rw-r--r--   0        0        0     1513 2022-12-27 09:46:58.876000 sampo-0.1.1.99/LICENSE
+-rw-r--r--   0        0        0      690 2023-02-14 13:14:55.559318 sampo-0.1.1.99/pyproject.toml
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/__init__.py
+-rw-r--r--   0        0        0      322 2022-12-27 10:41:54.852928 sampo-0.1.1.99/sampo/generator/__init__.py
+-rw-r--r--   0        0        0     3083 2023-02-02 13:01:55.047773 sampo-0.1.1.99/sampo/generator/base.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/generator/config/__init__.py
+-rw-r--r--   0        0        0      943 2022-12-27 10:41:54.852928 sampo-0.1.1.99/sampo/generator/config/gen_counts.py
+-rw-r--r--   0        0        0    10216 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/generator/config/worker_req.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/generator/environment/__init__.py
+-rw-r--r--   0        0        0     4985 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/generator/environment/contractor.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/generator/pipeline/__init__.py
+-rw-r--r--   0        0        0    11972 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/generator/pipeline/cluster.py
+-rw-r--r--   0        0        0     3101 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/generator/pipeline/extension.py
+-rw-r--r--   0        0        0     9265 2023-01-19 10:15:18.573875 sampo-0.1.1.99/sampo/generator/pipeline/project.py
+-rw-r--r--   0        0        0      223 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/generator/pipeline/types.py
+-rw-r--r--   0        0        0      224 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/generator/types.py
+-rw-r--r--   0        0        0        3 2023-01-19 10:15:18.574872 sampo-0.1.1.99/sampo/generator/utils/__init__.py
+-rw-r--r--   0        0        0      453 2023-01-19 10:15:18.574872 sampo-0.1.1.99/sampo/generator/utils/graph_node_operations.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/metrics/__init__.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/metrics/resources_in_time/__init__.py
+-rw-r--r--   0        0        0     4806 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/metrics/resources_in_time/base.py
+-rw-r--r--   0        0        0     5110 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/metrics/resources_in_time/binary_search.py
+-rw-r--r--   0        0        0     5114 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/metrics/resources_in_time/newton_conjugate_gradient.py
+-rw-r--r--   0        0        0     3860 2022-12-27 10:41:54.837308 sampo-0.1.1.99/sampo/metrics/resources_in_time/service.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/scheduler/__init__.py
+-rw-r--r--   0        0        0     4405 2023-02-13 10:39:37.312306 sampo-0.1.1.99/sampo/scheduler/base.py
+-rw-r--r--   0        0        0     2001 2023-02-14 12:42:23.302627 sampo-0.1.1.99/sampo/scheduler/generate.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.556139 sampo-0.1.1.99/sampo/scheduler/genetic/__init__.py
+-rw-r--r--   0        0        0     6631 2023-02-14 11:51:10.538278 sampo-0.1.1.99/sampo/scheduler/genetic/base.py
+-rw-r--r--   0        0        0     5049 2023-02-13 10:39:37.312306 sampo-0.1.1.99/sampo/scheduler/genetic/converter.py
+-rw-r--r--   0        0        0    20343 2023-02-14 13:13:31.351762 sampo-0.1.1.99/sampo/scheduler/genetic/operators.py
+-rw-r--r--   0        0        0    17329 2023-02-14 13:09:48.854786 sampo-0.1.1.99/sampo/scheduler/genetic/schedule_builder.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.99/sampo/scheduler/heft/__init__.py
+-rw-r--r--   0        0        0     7591 2023-02-13 10:39:37.312306 sampo-0.1.1.99/sampo/scheduler/heft/base.py
+-rw-r--r--   0        0        0     2586 2022-12-27 10:41:54.821687 sampo-0.1.1.99/sampo/scheduler/heft/prioritization.py
+-rw-r--r--   0        0        0     2845 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/scheduler/heft/time_computaion.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.99/sampo/scheduler/multi_agency/__init__.py
+-rw-r--r--   0        0        0     5560 2023-01-19 10:15:18.581372 sampo-0.1.1.99/sampo/scheduler/multi_agency/block_generator.py
+-rw-r--r--   0        0        0     2564 2022-12-27 10:41:54.821687 sampo-0.1.1.99/sampo/scheduler/multi_agency/block_graph.py
+-rw-r--r--   0        0        0     3102 2023-01-19 10:15:18.587075 sampo-0.1.1.99/sampo/scheduler/multi_agency/block_validation.py
+-rw-r--r--   0        0        0     6212 2023-01-19 10:15:18.589089 sampo-0.1.1.99/sampo/scheduler/multi_agency/multi_agency.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.99/sampo/scheduler/resource/__init__.py
+-rw-r--r--   0        0        0     1020 2022-12-27 10:41:54.806065 sampo-0.1.1.99/sampo/scheduler/resource/average_req.py
+-rw-r--r--   0        0        0     1267 2022-12-27 10:41:54.806065 sampo-0.1.1.99/sampo/scheduler/resource/base.py
+-rw-r--r--   0        0        0     1706 2022-12-27 10:41:54.806065 sampo-0.1.1.99/sampo/scheduler/resource/coordinate_descent.py
+-rw-r--r--   0        0        0     1977 2022-12-27 10:41:54.806065 sampo-0.1.1.99/sampo/scheduler/resource/full_scan.py
+-rw-r--r--   0        0        0      729 2022-12-27 10:41:54.806065 sampo-0.1.1.99/sampo/scheduler/resource/identity.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.99/sampo/scheduler/timeline/__init__.py
+-rw-r--r--   0        0        0     2734 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/scheduler/timeline/base.py
+-rw-r--r--   0        0        0     9183 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/scheduler/timeline/just_in_time_timeline.py
+-rw-r--r--   0        0        0    17633 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/scheduler/timeline/momentum_timeline.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.571745 sampo-0.1.1.99/sampo/scheduler/topological/__init__.py
+-rw-r--r--   0        0        0     8408 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/scheduler/topological/base.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.587367 sampo-0.1.1.99/sampo/scheduler/utils/__init__.py
+-rw-r--r--   0        0        0     8854 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/scheduler/utils/local_optimization.py
+-rw-r--r--   0        0        0     3037 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/scheduler/utils/multi_contractor.py
+-rw-r--r--   0        0        0     1998 2022-12-27 10:41:54.790444 sampo-0.1.1.99/sampo/scheduler/utils/obstruction.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.587367 sampo-0.1.1.99/sampo/schemas/__init__.py
+-rw-r--r--   0        0        0     4435 2023-01-19 10:15:18.591599 sampo-0.1.1.99/sampo/schemas/contractor.py
+-rw-r--r--   0        0        0      113 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/schemas/exceptions.py
+-rw-r--r--   0        0        0    12115 2023-02-14 11:44:34.885448 sampo-0.1.1.99/sampo/schemas/graph.py
+-rw-r--r--   0        0        0      322 2022-12-27 10:41:54.790444 sampo-0.1.1.99/sampo/schemas/identifiable.py
+-rw-r--r--   0        0        0     4185 2022-12-27 10:41:54.790444 sampo-0.1.1.99/sampo/schemas/interval.py
+-rw-r--r--   0        0        0     3363 2023-01-19 13:47:31.461861 sampo-0.1.1.99/sampo/schemas/requirements.py
+-rw-r--r--   0        0        0     3223 2023-01-19 10:15:18.597323 sampo-0.1.1.99/sampo/schemas/resources.py
+-rw-r--r--   0        0        0     8731 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/schemas/schedule.py
+-rw-r--r--   0        0        0     2045 2022-12-27 11:20:19.072277 sampo-0.1.1.99/sampo/schemas/schedule_spec.py
+-rw-r--r--   0        0        0     4775 2023-02-13 10:39:37.327927 sampo-0.1.1.99/sampo/schemas/scheduled_work.py
+-rw-r--r--   0        0        0    14647 2022-12-27 10:41:54.774823 sampo-0.1.1.99/sampo/schemas/serializable.py
+-rw-r--r--   0        0        0     2455 2022-12-27 10:43:19.445862 sampo-0.1.1.99/sampo/schemas/sorted_list.py
+-rw-r--r--   0        0        0     4211 2022-12-27 10:41:54.774823 sampo-0.1.1.99/sampo/schemas/time.py
+-rw-r--r--   0        0        0      672 2023-02-14 12:55:45.907922 sampo-0.1.1.99/sampo/schemas/time_estimator.py
+-rw-r--r--   0        0        0      886 2023-02-13 10:39:37.343548 sampo-0.1.1.99/sampo/schemas/types.py
+-rw-r--r--   0        0        0      987 2023-01-19 10:15:18.601354 sampo-0.1.1.99/sampo/schemas/utils.py
+-rw-r--r--   0        0        0     4651 2023-01-19 10:15:18.601354 sampo-0.1.1.99/sampo/schemas/works.py
+-rw-r--r--   0        0        0      209 2023-01-19 10:15:18.601354 sampo-0.1.1.99/sampo/structurator/__init__.py
+-rw-r--r--   0        0        0     8992 2023-02-13 10:39:37.343548 sampo-0.1.1.99/sampo/structurator/base.py
+-rw-r--r--   0        0        0     5059 2023-01-19 10:15:18.601354 sampo-0.1.1.99/sampo/structurator/graph_insertion.py
+-rw-r--r--   0        0        0      679 2023-01-19 10:15:18.601354 sampo-0.1.1.99/sampo/structurator/light_modifications.py
+-rw-r--r--   0        0        0     5132 2022-12-27 10:43:03.022066 sampo-0.1.1.99/sampo/structurator/metric.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.587367 sampo-0.1.1.99/sampo/utilities/__init__.py
+-rw-r--r--   0        0        0     1336 2022-12-27 10:41:54.774823 sampo-0.1.1.99/sampo/utilities/base_opt.py
+-rw-r--r--   0        0        0     1061 2022-12-27 10:41:54.774823 sampo-0.1.1.99/sampo/utilities/collections.py
+-rw-r--r--   0        0        0     1291 2022-12-27 10:41:54.774823 sampo-0.1.1.99/sampo/utilities/datetime.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.602989 sampo-0.1.1.99/sampo/utilities/generation/__init__.py
+-rw-r--r--   0        0        0     1559 2023-01-19 10:15:18.607483 sampo-0.1.1.99/sampo/utilities/generation/work_graph.py
+-rw-r--r--   0        0        0     1127 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/priority_queue.py
+-rw-r--r--   0        0        0      189 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/resource_cost.py
+-rw-r--r--   0        0        0      374 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/resource_path.py
+-rw-r--r--   0        0        0     3003 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/sampler/__init__.py
+-rw-r--r--   0        0        0     1706 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/sampler/requirements.py
+-rw-r--r--   0        0        0      436 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/sampler/resources.py
+-rw-r--r--   0        0        0      262 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/sampler/types.py
+-rw-r--r--   0        0        0     1619 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/sampler/works.py
+-rw-r--r--   0        0        0     3668 2023-01-19 10:15:18.607494 sampo-0.1.1.99/sampo/utilities/schedule.py
+-rw-r--r--   0        0        0     3770 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/serializers.py
+-rw-r--r--   0        0        0      704 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/stack.py
+-rw-r--r--   0        0        0     1833 2022-12-27 10:41:54.759201 sampo-0.1.1.99/sampo/utilities/task_name.py
+-rw-r--r--   0        0        0     8587 2023-02-13 10:55:30.091609 sampo-0.1.1.99/sampo/utilities/validation.py
+-rw-r--r--   0        0        0        0 2022-12-27 10:41:54.602989 sampo-0.1.1.99/sampo/utilities/visualization/__init__.py
+-rw-r--r--   0        0        0     1076 2022-12-27 10:41:54.743579 sampo-0.1.1.99/sampo/utilities/visualization/base.py
+-rw-r--r--   0        0        0    11917 2022-12-27 10:41:54.743579 sampo-0.1.1.99/sampo/utilities/visualization/resources.py
+-rw-r--r--   0        0        0     2392 2023-02-02 13:01:55.050765 sampo-0.1.1.99/sampo/utilities/visualization/schedule.py
+-rw-r--r--   0        0        0     8584 2022-12-27 10:41:54.743579 sampo-0.1.1.99/sampo/utilities/visualization/work_graph.py
+-rw-r--r--   0        0        0     1484 1970-01-01 00:00:00.000000 sampo-0.1.1.99/setup.py
+-rw-r--r--   0        0        0      826 1970-01-01 00:00:00.000000 sampo-0.1.1.99/PKG-INFO
```

### Comparing `sampo-0.1.1.98/LICENSE` & `sampo-0.1.1.99/LICENSE`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/pyproject.toml` & `sampo-0.1.1.99/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "sampo"
-version = "0.1.1.98"
+version = "0.1.1.99"
 description = "Open-source framework for adaptive manufacturing processes scheduling"
 authors = ["iAirLab <iairlab@yandex.ru>"]
 license = "BSD-3-Clause"
 # readme = "README.rst"
 # readme = "README.md"
 
 [tool.poetry.dependencies]
```

### Comparing `sampo-0.1.1.98/sampo/generator/base.py` & `sampo-0.1.1.99/sampo/generator/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/generator/config/gen_counts.py` & `sampo-0.1.1.99/sampo/generator/config/gen_counts.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/generator/config/worker_req.py` & `sampo-0.1.1.99/sampo/generator/config/worker_req.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/generator/environment/contractor.py` & `sampo-0.1.1.99/sampo/generator/environment/contractor.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/generator/pipeline/cluster.py` & `sampo-0.1.1.99/sampo/generator/pipeline/cluster.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/generator/pipeline/extension.py` & `sampo-0.1.1.99/sampo/generator/pipeline/extension.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/generator/pipeline/project.py` & `sampo-0.1.1.99/sampo/generator/pipeline/project.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/metrics/resources_in_time/base.py` & `sampo-0.1.1.99/sampo/metrics/resources_in_time/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/metrics/resources_in_time/binary_search.py` & `sampo-0.1.1.99/sampo/metrics/resources_in_time/binary_search.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/metrics/resources_in_time/newton_conjugate_gradient.py` & `sampo-0.1.1.99/sampo/metrics/resources_in_time/newton_conjugate_gradient.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/metrics/resources_in_time/service.py` & `sampo-0.1.1.99/sampo/metrics/resources_in_time/service.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/base.py` & `sampo-0.1.1.99/sampo/scheduler/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/generate.py` & `sampo-0.1.1.99/sampo/scheduler/generate.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/genetic/base.py` & `sampo-0.1.1.99/sampo/scheduler/genetic/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/genetic/converter.py` & `sampo-0.1.1.99/sampo/scheduler/genetic/converter.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/genetic/operators.py` & `sampo-0.1.1.99/sampo/scheduler/genetic/operators.py`

 * *Files 0% similar despite different names*

```diff
@@ -185,15 +185,20 @@
 
 
 def evaluate(ind) -> Time:
     return toolbox.evaluate(ind)
 
 
 def evaluation(chromosome):
-    return (fitness_f.evaluate(chromosome[0]) if toolbox.validate(chromosome[0]) else Time.inf()).value
+    if toolbox.validate(chromosome[0]):
+        v = fitness_f.evaluate(chromosome[0])
+    else:
+        logger.error('Validation failed')
+        v = Time.inf()
+    return v.value
 
 
 def init_toolbox(wg: WorkGraph, contractors: List[Contractor], worker_pool: WorkerContractorPool,
                  index2node: Dict[int, GraphNode],
                  work_id2index: Dict[str, int], worker_name2index: Dict[str, int],
                  index2contractor: Dict[int, str],
                  index2contractor_obj: Dict[int, Contractor],
```

### Comparing `sampo-0.1.1.98/sampo/scheduler/genetic/schedule_builder.py` & `sampo-0.1.1.99/sampo/scheduler/genetic/schedule_builder.py`

 * *Files 2% similar despite different names*

```diff
@@ -141,14 +141,17 @@
     toolbox = init_toolbox(wg, contractors, worker_pool, index2node,
                            work_id2index, worker_name2index, index2contractor,
                            index2contractor_obj, init_chromosomes, mutate_order,
                            mutate_resources, selection_size, rand, spec, worker_pool_indices,
                            contractor2index, contractor_borders, node_indices, index2node_list, parents,
                            assigned_parent_time, work_estimator)
 
+    for chromosome in init_chromosomes.values():
+        toolbox.validate(chromosome)
+
     def prepare_distributed_genetic_args():
         # for more information please refer operators.py#prepare_toolbox
         hyperparams = mutate_order, mutate_resources, selection_size, spec, rand, assigned_parent_time
         return wg, contractors, init_chromosomes, hyperparams
 
     with ProcessPoolExecutor(max_workers=n_cpu, initializer=init_worker,
                              initargs=(fitness, (None, None) if work_estimator is None
```

### Comparing `sampo-0.1.1.98/sampo/scheduler/heft/base.py` & `sampo-0.1.1.99/sampo/scheduler/heft/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/heft/prioritization.py` & `sampo-0.1.1.99/sampo/scheduler/heft/prioritization.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/heft/time_computaion.py` & `sampo-0.1.1.99/sampo/scheduler/heft/time_computaion.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/multi_agency/block_generator.py` & `sampo-0.1.1.99/sampo/scheduler/multi_agency/block_generator.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/multi_agency/block_graph.py` & `sampo-0.1.1.99/sampo/scheduler/multi_agency/block_graph.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/multi_agency/block_validation.py` & `sampo-0.1.1.99/sampo/scheduler/multi_agency/block_validation.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/multi_agency/multi_agency.py` & `sampo-0.1.1.99/sampo/scheduler/multi_agency/multi_agency.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/resource/average_req.py` & `sampo-0.1.1.99/sampo/scheduler/resource/average_req.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/resource/base.py` & `sampo-0.1.1.99/sampo/scheduler/resource/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/resource/coordinate_descent.py` & `sampo-0.1.1.99/sampo/scheduler/resource/coordinate_descent.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/resource/full_scan.py` & `sampo-0.1.1.99/sampo/scheduler/resource/full_scan.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/resource/identity.py` & `sampo-0.1.1.99/sampo/scheduler/resource/identity.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/timeline/base.py` & `sampo-0.1.1.99/sampo/scheduler/timeline/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/timeline/just_in_time_timeline.py` & `sampo-0.1.1.99/sampo/scheduler/timeline/just_in_time_timeline.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/timeline/momentum_timeline.py` & `sampo-0.1.1.99/sampo/scheduler/timeline/momentum_timeline.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/topological/base.py` & `sampo-0.1.1.99/sampo/scheduler/topological/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/utils/local_optimization.py` & `sampo-0.1.1.99/sampo/scheduler/utils/local_optimization.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/utils/multi_contractor.py` & `sampo-0.1.1.99/sampo/scheduler/utils/multi_contractor.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/scheduler/utils/obstruction.py` & `sampo-0.1.1.99/sampo/scheduler/utils/obstruction.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/contractor.py` & `sampo-0.1.1.99/sampo/schemas/contractor.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/graph.py` & `sampo-0.1.1.99/sampo/schemas/graph.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/interval.py` & `sampo-0.1.1.99/sampo/schemas/interval.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/requirements.py` & `sampo-0.1.1.99/sampo/schemas/requirements.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/resources.py` & `sampo-0.1.1.99/sampo/schemas/resources.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/schedule.py` & `sampo-0.1.1.99/sampo/schemas/schedule.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/schedule_spec.py` & `sampo-0.1.1.99/sampo/schemas/schedule_spec.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/scheduled_work.py` & `sampo-0.1.1.99/sampo/schemas/scheduled_work.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/serializable.py` & `sampo-0.1.1.99/sampo/schemas/serializable.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/sorted_list.py` & `sampo-0.1.1.99/sampo/schemas/sorted_list.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/time.py` & `sampo-0.1.1.99/sampo/schemas/time.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/time_estimator.py` & `sampo-0.1.1.99/sampo/schemas/time_estimator.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/types.py` & `sampo-0.1.1.99/sampo/schemas/types.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/utils.py` & `sampo-0.1.1.99/sampo/schemas/utils.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/schemas/works.py` & `sampo-0.1.1.99/sampo/schemas/works.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/structurator/base.py` & `sampo-0.1.1.99/sampo/structurator/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/structurator/graph_insertion.py` & `sampo-0.1.1.99/sampo/structurator/graph_insertion.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/structurator/light_modifications.py` & `sampo-0.1.1.99/sampo/structurator/light_modifications.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/structurator/metric.py` & `sampo-0.1.1.99/sampo/structurator/metric.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/base_opt.py` & `sampo-0.1.1.99/sampo/utilities/base_opt.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/collections.py` & `sampo-0.1.1.99/sampo/utilities/collections.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/datetime.py` & `sampo-0.1.1.99/sampo/utilities/datetime.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/generation/work_graph.py` & `sampo-0.1.1.99/sampo/utilities/generation/work_graph.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/priority_queue.py` & `sampo-0.1.1.99/sampo/utilities/priority_queue.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/sampler/__init__.py` & `sampo-0.1.1.99/sampo/utilities/sampler/__init__.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/sampler/requirements.py` & `sampo-0.1.1.99/sampo/utilities/sampler/requirements.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/sampler/works.py` & `sampo-0.1.1.99/sampo/utilities/sampler/works.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/schedule.py` & `sampo-0.1.1.99/sampo/utilities/schedule.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/serializers.py` & `sampo-0.1.1.99/sampo/utilities/serializers.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/stack.py` & `sampo-0.1.1.99/sampo/utilities/stack.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/task_name.py` & `sampo-0.1.1.99/sampo/utilities/task_name.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/validation.py` & `sampo-0.1.1.99/sampo/utilities/validation.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/visualization/base.py` & `sampo-0.1.1.99/sampo/utilities/visualization/base.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/visualization/resources.py` & `sampo-0.1.1.99/sampo/utilities/visualization/resources.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/visualization/schedule.py` & `sampo-0.1.1.99/sampo/utilities/visualization/schedule.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/sampo/utilities/visualization/work_graph.py` & `sampo-0.1.1.99/sampo/utilities/visualization/work_graph.py`

 * *Files identical despite different names*

### Comparing `sampo-0.1.1.98/setup.py` & `sampo-0.1.1.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -39,15 +39,15 @@
  'scipy>=1.9.3,<1.10.0',
  'seaborn>=0.12.1,<0.13.0',
  'sortedcontainers>=2.4.0,<2.5.0',
  'toposort>=1.7,<2.0']
 
 setup_kwargs = {
     'name': 'sampo',
-    'version': '0.1.1.98',
+    'version': '0.1.1.99',
     'description': 'Open-source framework for adaptive manufacturing processes scheduling',
     'long_description': 'None',
     'author': 'iAirLab',
     'author_email': 'iairlab@yandex.ru',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `sampo-0.1.1.98/PKG-INFO` & `sampo-0.1.1.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sampo
-Version: 0.1.1.98
+Version: 0.1.1.99
 Summary: Open-source framework for adaptive manufacturing processes scheduling
 License: BSD-3-Clause
 Author: iAirLab
 Author-email: iairlab@yandex.ru
 Requires-Python: >=3.10,<3.11
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Programming Language :: Python :: 3
```

