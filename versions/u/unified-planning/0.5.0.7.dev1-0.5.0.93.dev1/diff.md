# Comparing `tmp/unified_planning-0.5.0.7.dev1.tar.gz` & `tmp/unified_planning-0.5.0.93.dev1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "unified_planning-0.5.0.7.dev1.tar", last modified: Wed Jan  4 10:17:33 2023, max compression
+gzip compressed data, was "unified_planning-0.5.0.93.dev1.tar", last modified: Tue Jan 24 18:25:18 2023, max compression
```

## Comparing `unified_planning-0.5.0.7.dev1.tar` & `unified_planning-0.5.0.93.dev1.tar`

### file list

```diff
@@ -1,204 +1,209 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      977 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2188 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.750746 unified_planning-0.5.0.7.dev1/unified_planning/
--rw-r--r--   0 runner    (1001) docker     (123)     2137 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.750746 unified_planning-0.5.0.7.dev1/unified_planning/engines/
--rw-r--r--   0 runner    (1001) docker     (123)     2235 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.754746 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/
--rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3922 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/compilers_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)    12815 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/conditional_effects_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)    14692 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/disjunctive_conditions_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)    15625 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/grounder.py
--rw-r--r--   0 runner    (1001) docker     (123)    13884 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/negative_conditions_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)     8926 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/quantifiers_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)     6739 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/tarski_grounder.py
--rw-r--r--   0 runner    (1001) docker     (123)    10505 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1841 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/credits.py
--rw-r--r--   0 runner    (1001) docker     (123)     5362 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/engine.py
--rw-r--r--   0 runner    (1001) docker     (123)    34547 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     4003 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/meta_engine.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.754746 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/
--rw-r--r--   0 runner    (1001) docker     (123)     1116 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3679 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/anytime_planner.py
--rw-r--r--   0 runner    (1001) docker     (123)     5881 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/compiler.py
--rw-r--r--   0 runner    (1001) docker     (123)     4000 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/oneshot_planner.py
--rw-r--r--   0 runner    (1001) docker     (123)     2918 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/plan_validator.py
--rw-r--r--   0 runner    (1001) docker     (123)     6411 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/replanner.py
--rw-r--r--   0 runner    (1001) docker     (123)    10327 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/simulator.py
--rw-r--r--   0 runner    (1001) docker     (123)     7013 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/oversubscription_planner.py
--rw-r--r--   0 runner    (1001) docker     (123)     8086 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/parallel.py
--rw-r--r--   0 runner    (1001) docker     (123)    18187 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/pddl_planner.py
--rw-r--r--   0 runner    (1001) docker     (123)     5500 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/plan_validator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4372 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/replanner.py
--rw-r--r--   0 runner    (1001) docker     (123)     7024 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/results.py
--rw-r--r--   0 runner    (1001) docker     (123)    15437 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/engines/sequential_simulator.py
--rw-r--r--   0 runner    (1001) docker     (123)     5490 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/environment.py
--rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.754746 unified_planning-0.5.0.7.dev1/unified_planning/grpc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/grpc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/grpc/converter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.754746 unified_planning-0.5.0.7.dev1/unified_planning/grpc/generated/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/grpc/generated/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    30767 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/grpc/generated/unified_planning_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     7519 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/grpc/generated/unified_planning_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    29238 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/grpc/proto_reader.py
--rw-r--r--   0 runner    (1001) docker     (123)    29516 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/grpc/proto_writer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.754746 unified_planning-0.5.0.7.dev1/unified_planning/interop/
--rw-r--r--   0 runner    (1001) docker     (123)      734 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/interop/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16893 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/interop/from_tarski.py
--rw-r--r--   0 runner    (1001) docker     (123)    17971 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/interop/to_tarski.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.754746 unified_planning-0.5.0.7.dev1/unified_planning/io/
--rw-r--r--   0 runner    (1001) docker     (123)      224 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18415 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/io/anml_writer.py
--rw-r--r--   0 runner    (1001) docker     (123)    54598 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/io/pddl_reader.py
--rw-r--r--   0 runner    (1001) docker     (123)    33504 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/io/pddl_writer.py
--rw-r--r--   0 runner    (1001) docker     (123)    26053 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/io/python_writer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.758746 unified_planning-0.5.0.7.dev1/unified_planning/model/
--rw-r--r--   0 runner    (1001) docker     (123)     3145 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2636 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/abstract_problem.py
--rw-r--r--   0 runner    (1001) docker     (123)    39697 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/action.py
--rw-r--r--   0 runner    (1001) docker     (123)     7288 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/contingent_problem.py
--rw-r--r--   0 runner    (1001) docker     (123)     8086 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/effect.py
--rw-r--r--   0 runner    (1001) docker     (123)    23925 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/expression.py
--rw-r--r--   0 runner    (1001) docker     (123)     8868 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/fluent.py
--rw-r--r--   0 runner    (1001) docker     (123)    15699 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/fnode.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.758746 unified_planning-0.5.0.7.dev1/unified_planning/model/htn/
--rw-r--r--   0 runner    (1001) docker     (123)      401 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/htn/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6190 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/htn/hierarchical_problem.py
--rw-r--r--   0 runner    (1001) docker     (123)    11951 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/htn/method.py
--rw-r--r--   0 runner    (1001) docker     (123)     5387 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/htn/task.py
--rw-r--r--   0 runner    (1001) docker     (123)     5609 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/htn/task_network.py
--rw-r--r--   0 runner    (1001) docker     (123)     4008 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/metrics.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.758746 unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5474 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/actions_set.py
--rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/agents_set.py
--rw-r--r--   0 runner    (1001) docker     (123)     6892 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/fluents_set.py
--rw-r--r--   0 runner    (1001) docker     (123)     5235 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/objects_set.py
--rw-r--r--   0 runner    (1001) docker     (123)     4068 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/user_types_set.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.758746 unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/
--rw-r--r--   0 runner    (1001) docker     (123)      870 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3169 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/agent.py
--rw-r--r--   0 runner    (1001) docker     (123)     2296 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/ma_environment.py
--rw-r--r--   0 runner    (1001) docker     (123)    15610 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/ma_problem.py
--rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/object.py
--rw-r--r--   0 runner    (1001) docker     (123)     2015 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/operators.py
--rw-r--r--   0 runner    (1001) docker     (123)     5362 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/parameter.py
--rw-r--r--   0 runner    (1001) docker     (123)    37579 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/problem.py
--rw-r--r--   0 runner    (1001) docker     (123)     8747 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/problem_kind.py
--rw-r--r--   0 runner    (1001) docker     (123)     5786 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/state.py
--rw-r--r--   0 runner    (1001) docker     (123)    16710 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/timing.py
--rw-r--r--   0 runner    (1001) docker     (123)    15015 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/types.py
--rw-r--r--   0 runner    (1001) docker     (123)     6734 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/variable.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.758746 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/
--rw-r--r--   0 runner    (1001) docker     (123)     1453 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5521 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/dag.py
--rw-r--r--   0 runner    (1001) docker     (123)     7869 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/dnf.py
--rw-r--r--   0 runner    (1001) docker     (123)     4122 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/expression_quantifiers_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)     1608 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/free_vars.py
--rw-r--r--   0 runner    (1001) docker     (123)     3765 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/generic.py
--rw-r--r--   0 runner    (1001) docker     (123)     4465 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/identitydag.py
--rw-r--r--   0 runner    (1001) docker     (123)     8769 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/linear_checker.py
--rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/operators_extractor.py
--rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/quantifier_simplifier.py
--rw-r--r--   0 runner    (1001) docker     (123)    13594 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/simplifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     3426 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/state_evaluator.py
--rw-r--r--   0 runner    (1001) docker     (123)     3444 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/substituter.py
--rw-r--r--   0 runner    (1001) docker     (123)    11004 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/type_checker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.758746 unified_planning-0.5.0.7.dev1/unified_planning/plans/
--rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/plans/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6468 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/plans/contingent_plan.py
--rw-r--r--   0 runner    (1001) docker     (123)     8268 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/plans/partial_order_plan.py
--rw-r--r--   0 runner    (1001) docker     (123)     4584 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/plans/plan.py
--rw-r--r--   0 runner    (1001) docker     (123)    10010 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/plans/sequential_plan.py
--rw-r--r--   0 runner    (1001) docker     (123)     4991 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/plans/time_triggered_plan.py
--rw-r--r--   0 runner    (1001) docker     (123)    21135 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/shortcuts.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.762746 unified_planning-0.5.0.7.dev1/unified_planning/test/
--rw-r--r--   0 runner    (1001) docker     (123)     4534 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.762746 unified_planning-0.5.0.7.dev1/unified_planning/test/examples/
--rw-r--r--   0 runner    (1001) docker     (123)     1029 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/examples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3665 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/examples/hierarchical.py
--rw-r--r--   0 runner    (1001) docker     (123)    14613 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/examples/minimals.py
--rw-r--r--   0 runner    (1001) docker     (123)     5195 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/examples/multi_agent.py
--rw-r--r--   0 runner    (1001) docker     (123)    38705 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/examples/realistic.py
--rw-r--r--   0 runner    (1001) docker     (123)    24667 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/examples/testing_variants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.762746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.762746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/citycar/
--rw-r--r--   0 runner    (1001) docker     (123)     3742 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/citycar/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/citycar/problem.pddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.762746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/counters/
--rw-r--r--   0 runner    (1001) docker     (123)      843 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/counters/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      446 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/counters/problem.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      866 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/counters/problem2.pddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.762746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/depot/
--rw-r--r--   0 runner    (1001) docker     (123)     1377 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/depot/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      948 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/depot/problem.pddl
--rw-r--r--   0 runner    (1001) docker     (123)     6890 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/enhsp.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.762746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/htn-transport/
--rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/htn-transport/domain.hddl
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/htn-transport/problem.hddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/matchcellar/
--rw-r--r--   0 runner    (1001) docker     (123)      915 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/matchcellar/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/matchcellar/problem.pddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/miconic/
--rw-r--r--   0 runner    (1001) docker     (123)     3542 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/miconic/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      397 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/miconic/problem.pddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/robot_fastener/
--rw-r--r--   0 runner    (1001) docker     (123)     1085 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/robot_fastener/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/robot_fastener/problem.pddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/safe_road/
--rw-r--r--   0 runner    (1001) docker     (123)      675 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/safe_road/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/safe_road/problem.pddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/sailing/
--rw-r--r--   0 runner    (1001) docker     (123)     1694 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/sailing/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/sailing/problem.pddl
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.766746 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/visit_precedence/
--rwxr-xr-x   0 runner    (1001) docker     (123)      555 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/visit_precedence/domain.pddl
--rw-r--r--   0 runner    (1001) docker     (123)      314 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/visit_precedence/problem.pddl
--rw-r--r--   0 runner    (1001) docker     (123)    14089 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_anml_writer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2236 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_anytime.py
--rw-r--r--   0 runner    (1001) docker     (123)     2383 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_compilers_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     6367 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_conditional_effects_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)     3142 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_contingent_pddl.py
--rw-r--r--   0 runner    (1001) docker     (123)     2355 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_credits.py
--rw-r--r--   0 runner    (1001) docker     (123)    13148 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_disjunctive_conditions_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)     7770 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_dnf.py
--rw-r--r--   0 runner    (1001) docker     (123)     1522 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)    16725 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_grounder.py
--rw-r--r--   0 runner    (1001) docker     (123)     5009 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_infix_notation.py
--rw-r--r--   0 runner    (1001) docker     (123)     7915 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     5878 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_multi_agent.py
--rw-r--r--   0 runner    (1001) docker     (123)    10390 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_negative_conditions_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_partial_order_plan.py
--rw-r--r--   0 runner    (1001) docker     (123)    31663 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_pddl_io.py
--rw-r--r--   0 runner    (1001) docker     (123)    14875 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_pddl_planner.py
--rw-r--r--   0 runner    (1001) docker     (123)     2819 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_plan_validator.py
--rw-r--r--   0 runner    (1001) docker     (123)    12104 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_planner.py
--rw-r--r--   0 runner    (1001) docker     (123)    25417 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_problem.py
--rw-r--r--   0 runner    (1001) docker     (123)    12605 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_protobuf_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     4537 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_pyperplan.py
--rw-r--r--   0 runner    (1001) docker     (123)     3743 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_python_writer.py
--rw-r--r--   0 runner    (1001) docker     (123)     9690 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_quantifier_remover.py
--rw-r--r--   0 runner    (1001) docker     (123)     2385 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_replanner.py
--rw-r--r--   0 runner    (1001) docker     (123)     7300 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_sequential_simulator.py
--rw-r--r--   0 runner    (1001) docker     (123)    25132 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_simplifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     4601 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_simulated_effects.py
--rw-r--r--   0 runner    (1001) docker     (123)     3276 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_substituter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4208 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_tarski_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     7865 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_tarski_grounder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1786 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_temporal.py
--rw-r--r--   0 runner    (1001) docker     (123)     3482 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/test/test_validator.py
--rw-r--r--   0 runner    (1001) docker     (123)      875 2023-01-04 10:17:31.000000 unified_planning-0.5.0.7.dev1/unified_planning/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-04 10:17:33.750746 unified_planning-0.5.0.7.dev1/unified_planning.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      977 2023-01-04 10:17:33.000000 unified_planning-0.5.0.7.dev1/unified_planning.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7386 2023-01-04 10:17:33.000000 unified_planning-0.5.0.7.dev1/unified_planning.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-04 10:17:33.000000 unified_planning-0.5.0.7.dev1/unified_planning.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      366 2023-01-04 10:17:33.000000 unified_planning-0.5.0.7.dev1/unified_planning.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-04 10:17:33.000000 unified_planning-0.5.0.7.dev1/unified_planning.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.664664 unified_planning-0.5.0.93.dev1/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-01-24 18:25:18.664664 unified_planning-0.5.0.93.dev1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2188 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-24 18:25:18.664664 unified_planning-0.5.0.93.dev1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.648664 unified_planning-0.5.0.93.dev1/unified_planning/
+-rw-r--r--   0 runner    (1001) docker     (123)     2137 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.648664 unified_planning-0.5.0.93.dev1/unified_planning/engines/
+-rw-r--r--   0 runner    (1001) docker     (123)     2468 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.648664 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1287 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3977 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/compilers_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12815 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/conditional_effects_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15526 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/disjunctive_conditions_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17366 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/grounder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14669 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/negative_conditions_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9834 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/quantifiers_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7032 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/tarski_grounder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17654 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/trajectory_constraints_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10505 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1841 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/credits.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5671 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37012 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4003 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/meta_engine.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.652664 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/
+-rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3679 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/anytime_planner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5926 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4000 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/oneshot_planner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2918 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/plan_validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4001 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/portfolio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6411 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/replanner.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10465 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/simulator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7013 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/oversubscription_planner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8086 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/parallel.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18186 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/pddl_planner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6000 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/plan_validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4372 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/replanner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7024 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/results.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16077 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/engines/sequential_simulator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5490 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.652664 unified_planning-0.5.0.93.dev1/unified_planning/grpc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/grpc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/grpc/converter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.652664 unified_planning-0.5.0.93.dev1/unified_planning/grpc/generated/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/grpc/generated/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30767 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/grpc/generated/unified_planning_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7519 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/grpc/generated/unified_planning_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29238 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/grpc/proto_reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29516 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/grpc/proto_writer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.652664 unified_planning-0.5.0.93.dev1/unified_planning/interop/
+-rw-r--r--   0 runner    (1001) docker     (123)      734 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/interop/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16893 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/interop/from_tarski.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17971 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/interop/to_tarski.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.652664 unified_planning-0.5.0.93.dev1/unified_planning/io/
+-rw-r--r--   0 runner    (1001) docker     (123)      224 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18415 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/io/anml_writer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    55978 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/io/pddl_reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34687 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/io/pddl_writer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26053 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/io/python_writer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.652664 unified_planning-0.5.0.93.dev1/unified_planning/model/
+-rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2636 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/abstract_problem.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39697 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/action.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7288 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/contingent_problem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8086 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/effect.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26679 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/expression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8868 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/fluent.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17046 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/fnode.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.656664 unified_planning-0.5.0.93.dev1/unified_planning/model/htn/
+-rw-r--r--   0 runner    (1001) docker     (123)      401 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/htn/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6190 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/htn/hierarchical_problem.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11951 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/htn/method.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5387 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/htn/task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5609 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/htn/task_network.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4008 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/metrics.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.656664 unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5474 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/actions_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/agents_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6892 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/fluents_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5235 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/objects_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4068 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/user_types_set.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.656664 unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/
+-rw-r--r--   0 runner    (1001) docker     (123)      870 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3169 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/agent.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2296 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/ma_environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15610 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/ma_problem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/object.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2361 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/operators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5362 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/parameter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39865 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/problem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8888 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/problem_kind.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5786 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/state.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16710 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/timing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15015 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6734 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/variable.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.656664 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1453 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5521 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/dag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7869 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/dnf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4122 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/expression_quantifiers_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1608 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/free_vars.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3765 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/generic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5216 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/identitydag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8769 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/linear_checker.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/operators_extractor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/quantifier_simplifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15170 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/simplifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3426 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/state_evaluator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3444 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/substituter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13347 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/type_checker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.656664 unified_planning-0.5.0.93.dev1/unified_planning/plans/
+-rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/plans/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7221 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/plans/contingent_plan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9109 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/plans/partial_order_plan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5199 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/plans/plan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10958 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/plans/sequential_plan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5744 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/plans/time_triggered_plan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24091 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/shortcuts.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/
+-rw-r--r--   0 runner    (1001) docker     (123)     4621 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/examples/
+-rw-r--r--   0 runner    (1001) docker     (123)     1029 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/examples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3665 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/examples/hierarchical.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14613 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/examples/minimals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5195 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/examples/multi_agent.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38705 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/examples/realistic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30647 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/examples/testing_variants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/citycar/
+-rw-r--r--   0 runner    (1001) docker     (123)     3742 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/citycar/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/citycar/problem.pddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/counters/
+-rw-r--r--   0 runner    (1001) docker     (123)      843 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/counters/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      446 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/counters/problem.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      866 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/counters/problem2.pddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/depot/
+-rw-r--r--   0 runner    (1001) docker     (123)     1377 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/depot/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/depot/problem.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)     6890 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/enhsp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/htn-transport/
+-rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/htn-transport/domain.hddl
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/htn-transport/problem.hddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/matchcellar/
+-rw-r--r--   0 runner    (1001) docker     (123)      915 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/matchcellar/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/matchcellar/problem.pddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.660664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/miconic/
+-rw-r--r--   0 runner    (1001) docker     (123)     3542 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/miconic/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      397 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/miconic/problem.pddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.664664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/robot_fastener/
+-rw-r--r--   0 runner    (1001) docker     (123)     1085 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/robot_fastener/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/robot_fastener/problem.pddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.664664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/safe_road/
+-rw-r--r--   0 runner    (1001) docker     (123)      675 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/safe_road/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/safe_road/problem.pddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.664664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/sailing/
+-rw-r--r--   0 runner    (1001) docker     (123)     1694 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/sailing/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/sailing/problem.pddl
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.664664 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/visit_precedence/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      555 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/visit_precedence/domain.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)      314 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/visit_precedence/problem.pddl
+-rw-r--r--   0 runner    (1001) docker     (123)    14089 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_anml_writer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2236 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_anytime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2383 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_compilers_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3005 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_compilers_quality_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6367 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_conditional_effects_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3142 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_contingent_pddl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2355 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_credits.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13148 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_disjunctive_conditions_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7770 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_dnf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1522 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16725 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_grounder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5009 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_infix_notation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7915 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5878 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_multi_agent.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10390 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_negative_conditions_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3387 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_partial_order_plan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32310 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_pddl_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14875 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_pddl_planner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2819 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_plan_validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12730 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_planner.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25466 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_problem.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12605 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_protobuf_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4537 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_pyperplan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3743 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_python_writer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9690 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_quantifier_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2385 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_replanner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7300 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_sequential_simulator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25132 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_simplifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4601 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_simulated_effects.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3276 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_substituter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4208 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_tarski_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7865 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_tarski_grounder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1786 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_temporal.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13120 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_trajectory_constraint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5924 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_trajectory_constraints_remover.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3482 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/test/test_validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)      875 2023-01-24 18:25:15.000000 unified_planning-0.5.0.93.dev1/unified_planning/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 18:25:18.648664 unified_planning-0.5.0.93.dev1/unified_planning.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-01-24 18:25:18.000000 unified_planning-0.5.0.93.dev1/unified_planning.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7669 2023-01-24 18:25:18.000000 unified_planning-0.5.0.93.dev1/unified_planning.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-24 18:25:18.000000 unified_planning-0.5.0.93.dev1/unified_planning.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      366 2023-01-24 18:25:18.000000 unified_planning-0.5.0.93.dev1/unified_planning.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-24 18:25:18.000000 unified_planning-0.5.0.93.dev1/unified_planning.egg-info/top_level.txt
```

### Comparing `unified_planning-0.5.0.7.dev1/LICENSE` & `unified_planning-0.5.0.93.dev1/LICENSE`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/PKG-INFO` & `unified_planning-0.5.0.93.dev1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: unified_planning
-Version: 0.5.0.7.dev1
+Version: 0.5.0.93.dev1
 Summary: Unified Planning Framework
 Home-page: https://www.aiplan4eu-project.eu
 Author: AIPlan4EU Project
 Author-email: aiplan4eu@fbk.eu
 License: APACHE
 Description: UNKNOWN
 Keywords: planning logic STRIPS RDDL
```

### Comparing `unified_planning-0.5.0.7.dev1/README.md` & `unified_planning-0.5.0.93.dev1/README.md`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/setup.py` & `unified_planning-0.5.0.93.dev1/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,23 +22,23 @@
     python_requires=">=3.7",  # supported Python ranges
     install_requires=["pyparsing", "networkx"],
     extras_require={
         "dev": ["tarski[arithmetic]", "pytest", "pytest-cov", "mypy"],
         "grpc": ["grpcio", "grpcio-tools", "grpc-stubs"],
         "tarski": ["tarski[arithmetic]"],
         "pyperplan": ["up-pyperplan==0.3.0"],
-        "tamer": ["up-tamer==0.3.0"],
+        "tamer": ["up-tamer==0.3.1"],
         "enhsp": ["up-enhsp==0.0.9"],
-        "fast-downward": ["up-fast-downward==0.0.6"],
+        "fast-downward": ["up-fast-downward==0.1.1"],
         "engines": [
             "tarski[arithmetic]",
             "up-pyperplan==0.3.0",
-            "up-tamer==0.3.0",
+            "up-tamer==0.3.1",
             "up-enhsp==0.0.9",
-            "up-fast-downward==0.0.6",
+            "up-fast-downward==0.1.1",
         ],
     },
     license="APACHE",
     keywords="planning logic STRIPS RDDL",
     classifiers=[
         "Development Status :: 3 - Alpha",
         "Intended Audience :: Science/Research",
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/__init__.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/__init__.py`

 * *Files 15% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 
 
-from unified_planning.engines.engine import Engine
+from unified_planning.engines.engine import Engine, OperationMode
 from unified_planning.engines.meta_engine import MetaEngine
 from unified_planning.engines.credits import Credits
 from unified_planning.engines.factory import Factory
 from unified_planning.engines.parallel import Parallel
 from unified_planning.engines.pddl_planner import PDDLPlanner
 from unified_planning.engines.plan_validator import SequentialPlanValidator
 from unified_planning.engines.oversubscription_planner import OversubscriptionPlanner
@@ -37,14 +37,15 @@
     SequentialSimulator,
     InstantaneousEvent,
 )
 from unified_planning.engines.mixins.simulator import SimulatorMixin, Event
 from unified_planning.engines.mixins.oneshot_planner import OptimalityGuarantee
 from unified_planning.engines.mixins.anytime_planner import AnytimeGuarantee
 from unified_planning.engines.mixins.compiler import CompilationKind
+from unified_planning.engines.mixins.portfolio import PortfolioSelectorMixin
 
 __all__ = [
     "Factory",
     "Grounder",
     "Parallel",
     "PDDLPlanner",
     "SequentialPlanValidator",
@@ -60,8 +61,14 @@
     "LogMessage",
     "PlanGenerationResult",
     "LogLevel",
     "PlanGenerationResultStatus",
     "ValidationResult",
     "ValidationResultStatus",
     "CompilerResult",
+    "PortfolioSelectorMixin",
+    "OperationMode",
+    "AnytimeGuarantee",
+    "MetaEngine",
+    "OversubscriptionPlanner",
+    "Replanner",
 ]
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -20,8 +20,11 @@
     DisjunctiveConditionsRemover,
 )
 from unified_planning.engines.compilers.grounder import Grounder, GrounderHelper
 from unified_planning.engines.compilers.quantifiers_remover import QuantifiersRemover
 from unified_planning.engines.compilers.negative_conditions_remover import (
     NegativeConditionsRemover,
 )
+from unified_planning.engines.compilers.trajectory_constraints_remover import (
+    TrajectoryConstraintsRemover,
+)
 from unified_planning.engines.compilers.compilers_pipeline import CompilersPipeline
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/compilers_pipeline.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/compilers_pipeline.py`

 * *Files 2% similar despite different names*

```diff
@@ -94,11 +94,13 @@
             self.name,
         )
 
 
 def map_back_action_instance(
     action: ActionInstance,
     map_back_functions: List[Callable[[ActionInstance], ActionInstance]],
-) -> ActionInstance:
+) -> Optional[ActionInstance]:
     for f in map_back_functions:
         action = f(action)
+        if action is None:
+            break
     return action
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/conditional_effects_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/conditional_effects_remover.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/disjunctive_conditions_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/disjunctive_conditions_remover.py`

 * *Files 4% similar despite different names*

```diff
@@ -25,14 +25,15 @@
     Problem,
     InstantaneousAction,
     DurativeAction,
     TimeInterval,
     Timing,
     Action,
     ProblemKind,
+    Oversubscription,
 )
 from unified_planning.model.walkers import Dnf
 from typing import List, Optional, Tuple, Dict, cast
 from itertools import product
 from functools import partial
 
 
@@ -80,14 +81,19 @@
         supported_kind.set_time("CONTINUOUS_TIME")
         supported_kind.set_time("DISCRETE_TIME")
         supported_kind.set_time("INTERMEDIATE_CONDITIONS_AND_EFFECTS")
         supported_kind.set_time("TIMED_EFFECT")
         supported_kind.set_time("TIMED_GOALS")
         supported_kind.set_time("DURATION_INEQUALITIES")
         supported_kind.set_simulated_entities("SIMULATED_EFFECTS")
+        supported_kind.set_quality_metrics("ACTIONS_COST")
+        supported_kind.set_quality_metrics("PLAN_LENGTH")
+        supported_kind.set_quality_metrics("OVERSUBSCRIPTION")
+        supported_kind.set_quality_metrics("MAKESPAN")
+        supported_kind.set_quality_metrics("FINAL_VALUE")
         return supported_kind
 
     @staticmethod
     def supports(problem_kind):
         return problem_kind <= DisjunctiveConditionsRemover.supported_kind()
 
     @staticmethod
@@ -124,14 +130,15 @@
         new_fluents: List["up.model.Fluent"] = []
 
         new_problem = problem.clone()
         new_problem.name = f"{self.name}_{problem.name}"
         new_problem.clear_actions()
         new_problem.clear_goals()
         new_problem.clear_timed_goals()
+        new_problem.clear_quality_metrics()
 
         dnf = Dnf(env)
         for a in problem.actions:
             if isinstance(a, InstantaneousAction):
                 new_precond = dnf.get_dnf_expression(
                     env.expression_manager.And(a.preconditions)
                 )
@@ -174,32 +181,45 @@
             else:
                 raise NotImplementedError
 
         # Meaningful action is the list of the actions that modify fluents that are not added
         # just to remove the disjunction from goals
         meaningful_actions: List["up.model.Action"] = new_problem.actions[:]
 
-        self._remove_disjunctions_from_goals_adding_new_elements(
+        goal_to_add = self._goals_without_disjunctions_adding_new_elements(
             dnf,
             new_problem,
             new_to_old,
             new_fluents,
             problem.goals,
         )
+        new_problem.add_goal(goal_to_add)
 
         for t, gl in problem.timed_goals.items():
-            self._remove_disjunctions_from_goals_adding_new_elements(
+            goal_to_add = self._goals_without_disjunctions_adding_new_elements(
                 dnf,
                 new_problem,
                 new_to_old,
                 new_fluents,
                 gl,
                 t,
             )
+            new_problem.add_timed_goal(t, goal_to_add)
 
+        for qm in problem.quality_metrics:
+            if isinstance(qm, Oversubscription):
+                new_oversubscription = {}
+                for g, v in qm.goals.items():
+                    new_goal = self._goals_without_disjunctions_adding_new_elements(
+                        dnf, new_problem, new_to_old, new_fluents, [g]
+                    )
+                    new_oversubscription[new_goal] = v
+                new_problem.add_quality_metric(Oversubscription(new_oversubscription))
+            else:
+                new_problem.add_quality_metric(qm)
         # Every meaningful action must set to False every new fluent added.
         # For the DurativeActions this must happen every time the action modifies something
         em = env.expression_manager
         # new_effects is the List of effects that must be added to every meaningful action
         new_effects: List["up.model.Effect"] = [
             up.model.Effect(em.FluentExp(f), em.FALSE(), em.TRUE()) for f in new_fluents
         ]
@@ -217,23 +237,23 @@
                 raise NotImplementedError
             new_to_old[a] = old_action
 
         return CompilerResult(
             new_problem, partial(replace_action, map=new_to_old), self.name
         )
 
-    def _remove_disjunctions_from_goals_adding_new_elements(
+    def _goals_without_disjunctions_adding_new_elements(
         self,
         dnf: Dnf,
         new_problem: "up.model.Problem",
         new_to_old: Dict[Action, Optional[Action]],
         new_fluents: List["up.model.Fluent"],
         goals: List["up.model.FNode"],
         timing: Optional["up.model.timing.TimeInterval"] = None,
-    ):
+    ) -> "up.model.FNode":
         env = new_problem.env
         new_goal = dnf.get_dnf_expression(env.expression_manager.And(goals))
         if new_goal.is_or():
             new_name = self.name if timing is None else f"{self.name}_timed"
             fake_fluent = up.model.Fluent(
                 get_fresh_name(new_problem, f"{new_name}_fake_goal")
             )
@@ -244,23 +264,17 @@
                     new_problem, and_exp, fake_action, dnf
                 )
                 if na is not None:
                     new_to_old[na] = None
                     new_problem.add_action(na)
             new_problem.add_fluent(fake_fluent, default_initial_value=False)
             new_fluents.append(fake_fluent)
-            if timing is None:
-                new_problem.add_goal(fake_fluent)
-            else:
-                new_problem.add_timed_goal(timing, fake_fluent)
+            return env.expression_manager.FluentExp(fake_fluent)
         else:
-            if timing is None:
-                new_problem.add_goal(new_goal)
-            else:
-                new_problem.add_timed_goal(timing, new_goal)
+            return new_goal
 
     def _create_new_durative_action_with_given_conds_at_given_times(
         self,
         new_problem: "up.model.Problem",
         interval_list: List[TimeInterval],
         cond_list: List[FNode],
         original_action: DurativeAction,
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/grounder.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/grounder.py`

 * *Files 7% similar despite different names*

```diff
@@ -16,22 +16,32 @@
 import unified_planning as up
 import unified_planning.environment
 import unified_planning.engines as engines
 import unified_planning.engines.compilers
 from unified_planning.plans import ActionInstance
 from unified_planning.engines.mixins.compiler import CompilationKind, CompilerMixin
 from unified_planning.engines.results import CompilerResult
-from unified_planning.model import Problem, ProblemKind, Action, Type, Expression, FNode
+from unified_planning.model import (
+    Problem,
+    ProblemKind,
+    Action,
+    Type,
+    Expression,
+    FNode,
+    MinimizeActionCosts,
+    Parameter,
+)
 from unified_planning.model.types import domain_size, domain_item
 from unified_planning.model.walkers import Substituter, Simplifier
 from unified_planning.engines.compilers.utils import (
     lift_action_instance,
     create_action_with_given_subs,
 )
-from typing import Dict, List, Optional, Tuple, Iterator
+from unified_planning.exceptions import UPUsageError
+from typing import Dict, Iterable, List, Optional, Tuple, Iterator, cast
 from itertools import product
 from functools import partial
 
 
 class GrounderHelper:
     """
     This class gives the capability of grounding a :class:`~unified_planning.model.Problem` by taking
@@ -78,14 +88,22 @@
         self._grounded_actions: Dict[
             Tuple[Action, Tuple[FNode, ...]], Optional[Action]
         ] = {}
         env = problem.env
         self._substituter = Substituter(env)
         self._simplifier = Simplifier(env, problem)
 
+    @property
+    def substituter(self) -> Substituter:
+        return self._substituter
+
+    @property
+    def simplifier(self) -> Simplifier:
+        return self._simplifier
+
     def ground_action(
         self, action: Action, parameters: Tuple[FNode, ...] = tuple()
     ) -> Optional[Action]:
         """
         Grounds the given `action` with the given `parameters`.
         An `Action` is grounded when it has no :func:`parameters <unified_planning.model.Action.parameters>`.
 
@@ -249,14 +267,20 @@
         supported_kind.set_time("INTERMEDIATE_CONDITIONS_AND_EFFECTS")
         supported_kind.set_time("TIMED_EFFECT")
         supported_kind.set_time("TIMED_GOALS")
         supported_kind.set_time("DURATION_INEQUALITIES")
         supported_kind.set_expression_duration("STATIC_FLUENTS_IN_DURATION")
         supported_kind.set_expression_duration("FLUENTS_IN_DURATION")
         supported_kind.set_simulated_entities("SIMULATED_EFFECTS")
+        supported_kind.set_constraints_kind("TRAJECTORY_CONSTRAINTS")
+        supported_kind.set_quality_metrics("ACTIONS_COST")
+        supported_kind.set_quality_metrics("PLAN_LENGTH")
+        supported_kind.set_quality_metrics("OVERSUBSCRIPTION")
+        supported_kind.set_quality_metrics("MAKESPAN")
+        supported_kind.set_quality_metrics("FINAL_VALUE")
         return supported_kind
 
     @staticmethod
     def supports(problem_kind):
         return problem_kind <= Grounder.supported_kind()
 
     @staticmethod
@@ -297,12 +321,34 @@
             parameters,
             new_action,
         ) in grounder_helper.get_grounded_actions():
             if new_action is not None:
                 new_problem.add_action(new_action)
                 trace_back_map[new_action] = (old_action, list(parameters))
 
+        new_problem.clear_quality_metrics()
+        for qm in problem.quality_metrics:
+            if isinstance(qm, MinimizeActionCosts):
+                substituter = grounder_helper.substituter
+                simplifier = grounder_helper.simplifier
+                new_costs: Dict[Action, Optional[FNode]] = {}
+                for new_action, (old_action, params) in trace_back_map.items():
+                    subs = cast(
+                        Dict[Expression, Expression],
+                        dict(zip(old_action.parameters, params)),
+                    )
+                    old_cost = qm.get_action_cost(old_action)
+                    if old_cost is None:
+                        new_costs[new_action] = None
+                    else:
+                        new_costs[new_action] = simplifier.simplify(
+                            substituter.substitute(old_cost, subs)
+                        )
+                new_problem.add_quality_metric(MinimizeActionCosts(new_costs))
+            else:
+                new_problem.add_quality_metric(qm)
+
         return CompilerResult(
             new_problem,
             partial(lift_action_instance, map=trace_back_map),
             self.name,
         )
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/negative_conditions_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/negative_conditions_remover.py`

 * *Files 6% similar despite different names*

```diff
@@ -24,14 +24,15 @@
     InstantaneousAction,
     DurativeAction,
     FNode,
     Action,
     Effect,
     Timing,
     ProblemKind,
+    Oversubscription,
 )
 from unified_planning.model.walkers.identitydag import IdentityDagWalker
 from unified_planning.engines.compilers.utils import get_fresh_name, replace_action
 from unified_planning.exceptions import (
     UPExpressionDefinitionError,
     UPProblemDefinitionError,
 )
@@ -116,14 +117,19 @@
         supported_kind.set_effects_kind("DECREASE_EFFECTS")
         supported_kind.set_time("CONTINUOUS_TIME")
         supported_kind.set_time("DISCRETE_TIME")
         supported_kind.set_time("INTERMEDIATE_CONDITIONS_AND_EFFECTS")
         supported_kind.set_time("TIMED_EFFECT")
         supported_kind.set_time("TIMED_GOALS")
         supported_kind.set_time("DURATION_INEQUALITIES")
+        supported_kind.set_quality_metrics("ACTIONS_COST")
+        supported_kind.set_quality_metrics("PLAN_LENGTH")
+        supported_kind.set_quality_metrics("OVERSUBSCRIPTION")
+        supported_kind.set_quality_metrics("MAKESPAN")
+        supported_kind.set_quality_metrics("FINAL_VALUE")
         return supported_kind
 
     @staticmethod
     def supports(problem_kind):
         return problem_kind <= NegativeConditionsRemover.supported_kind()
 
     @staticmethod
@@ -210,14 +216,27 @@
                 ng = fluent_remover.remove_negative_fluents(g)
                 new_problem.add_timed_goal(i, ng)
 
         for g in problem.goals:
             ng = fluent_remover.remove_negative_fluents(g)
             new_problem.add_goal(ng)
 
+        for qm in problem.quality_metrics:
+            if isinstance(qm, Oversubscription):
+                new_problem.add_quality_metric(
+                    Oversubscription(
+                        {
+                            fluent_remover.remove_negative_fluents(g): v
+                            for g, v in qm.goals.items()
+                        }
+                    )
+                )
+            else:
+                new_problem.add_quality_metric(qm)
+
         # fluent_mapping is the map between a fluent and it's negation, when the
         # negation is None it means the fluent is never found in a negation into
         # every condititon analized before; therefore it does not need to exist.
         fluent_mapping = fluent_remover.fluent_mapping
         for f in problem.fluents:
             new_problem.add_fluent(f)
             fneg = fluent_mapping.get(f, None)
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/quantifiers_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/quantifiers_remover.py`

 * *Files 7% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 from unified_planning.engines.results import CompilerResult
 from unified_planning.model import (
     Problem,
     InstantaneousAction,
     DurativeAction,
     Action,
     ProblemKind,
+    Oversubscription,
 )
 from unified_planning.model.walkers import ExpressionQuantifiersRemover
 from unified_planning.engines.compilers.utils import get_fresh_name, replace_action
 from typing import Dict, Optional
 from functools import partial
 
 
@@ -77,14 +78,19 @@
         supported_kind.set_time("CONTINUOUS_TIME")
         supported_kind.set_time("DISCRETE_TIME")
         supported_kind.set_time("INTERMEDIATE_CONDITIONS_AND_EFFECTS")
         supported_kind.set_time("TIMED_EFFECT")
         supported_kind.set_time("TIMED_GOALS")
         supported_kind.set_time("DURATION_INEQUALITIES")
         supported_kind.set_simulated_entities("SIMULATED_EFFECTS")
+        supported_kind.set_quality_metrics("ACTIONS_COST")
+        supported_kind.set_quality_metrics("PLAN_LENGTH")
+        supported_kind.set_quality_metrics("OVERSUBSCRIPTION")
+        supported_kind.set_quality_metrics("MAKESPAN")
+        supported_kind.set_quality_metrics("FINAL_VALUE")
         return supported_kind
 
     @staticmethod
     def supports(problem_kind):
         return problem_kind <= QuantifiersRemover.supported_kind()
 
     @staticmethod
@@ -122,14 +128,16 @@
 
         new_to_old: Dict[Action, Action] = {}
 
         new_problem = problem.clone()
         new_problem.name = f"{self.name}_{problem.name}"
         new_problem.clear_timed_goals()
         new_problem.clear_goals()
+        new_problem.clear_quality_metrics()
+
         for action in new_problem.actions:
             if isinstance(action, InstantaneousAction):
                 original_action = problem.action(action.name)
                 assert isinstance(original_action, InstantaneousAction)
                 action.name = get_fresh_name(new_problem, action.name)
                 action.clear_preconditions()
                 for p in original_action.preconditions:
@@ -174,15 +182,15 @@
                             expression_quantifier_remover.remove_quantifiers(
                                 e.value, problem
                             )
                         )
                 new_to_old[action] = original_action
             else:
                 raise NotImplementedError
-        for t, el in new_problem.timed_effects.items():
+        for el in new_problem.timed_effects.values():
             for e in el:
                 if e.is_conditional():
                     e.set_condition(
                         expression_quantifier_remover.remove_quantifiers(
                             e.condition, problem
                         )
                     )
@@ -192,11 +200,25 @@
         for i, gl in problem.timed_goals.items():
             for g in gl:
                 ng = expression_quantifier_remover.remove_quantifiers(g, problem)
                 new_problem.add_timed_goal(i, ng)
         for g in problem.goals:
             ng = expression_quantifier_remover.remove_quantifiers(g, problem)
             new_problem.add_goal(ng)
+        for qm in problem.quality_metrics:
+            if isinstance(qm, Oversubscription):
+                new_problem.add_quality_metric(
+                    Oversubscription(
+                        {
+                            expression_quantifier_remover.remove_quantifiers(
+                                g, problem
+                            ): v
+                            for g, v in qm.goals.items()
+                        }
+                    )
+                )
+            else:
+                new_problem.add_quality_metric(qm)
 
         return CompilerResult(
             new_problem, partial(replace_action, map=new_to_old), self.name
         )
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/tarski_grounder.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/tarski_grounder.py`

 * *Files 6% similar despite different names*

```diff
@@ -70,14 +70,19 @@
         supported_kind.set_typing("HIERARCHICAL_TYPING")
         supported_kind.set_conditions_kind("NEGATIVE_CONDITIONS")
         supported_kind.set_conditions_kind("DISJUNCTIVE_CONDITIONS")
         supported_kind.set_conditions_kind("EQUALITY")
         supported_kind.set_conditions_kind("EXISTENTIAL_CONDITIONS")
         supported_kind.set_conditions_kind("UNIVERSAL_CONDITIONS")
         supported_kind.set_effects_kind("CONDITIONAL_EFFECTS")
+        supported_kind.set_quality_metrics("ACTIONS_COST")
+        supported_kind.set_quality_metrics("PLAN_LENGTH")
+        supported_kind.set_quality_metrics("OVERSUBSCRIPTION")
+        supported_kind.set_quality_metrics("MAKESPAN")
+        supported_kind.set_quality_metrics("FINAL_VALUE")
         return supported_kind
 
     @staticmethod
     def supports(problem_kind: "unified_planning.model.ProblemKind") -> bool:
         return problem_kind <= TarskiGrounder.supported_kind()
 
     @staticmethod
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/compilers/utils.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/compilers/utils.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/credits.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/credits.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/engine.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/engine.py`

 * *Files 5% similar despite different names*

```diff
@@ -10,37 +10,47 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 """This module defines the engine interface."""
 
+from enum import Enum
 from unified_planning.model import ProblemKind
 from unified_planning.engines.credits import Credits
 from typing import Optional
 
 
+class OperationMode(Enum):
+    """
+    This class represents all the operation modes that the library supports.
+    """
+
+    ONESHOT_PLANNER = "oneshot_planner"
+    ANYTIME_PLANNER = "anytime_planner"
+    PLAN_VALIDATOR = "plan_validator"
+    PORTFOLIO_SELECTOR = "portfolio_selector"
+    COMPILER = "compiler"
+    SIMULATOR = "simulator"
+    REPLANNER = "replanner"
+
+
 class EngineMeta(type):
     def __new__(cls, name, bases, dct):
         obj = type.__new__(cls, name, bases, dct)
-        oms = [
-            "oneshot_planner",
-            "anytime_planner",
-            "plan_validator",
-            "compiler",
-            "simulator",
-            "replanner",
-        ]
         for base in bases:
-            for om in oms:
-                if hasattr(base, "is_" + om) and getattr(base, "is_" + om)():
-                    setattr(obj, "is_" + om, staticmethod(lambda: True))
-        for om in oms:
-            if not hasattr(obj, "is_" + om):
-                setattr(obj, "is_" + om, staticmethod(lambda: False))
+            for om in OperationMode:
+                if (
+                    hasattr(base, "is_" + om.value)
+                    and getattr(base, "is_" + om.value)()
+                ):
+                    setattr(obj, "is_" + om.value, staticmethod(lambda: True))
+        for om in OperationMode:
+            if not hasattr(obj, "is_" + om.value):
+                setattr(obj, "is_" + om.value, staticmethod(lambda: False))
         return obj
 
 
 class Engine(metaclass=EngineMeta):
     """
     Represents the engine interface that must be implemented.
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/factory.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/factory.py`

 * *Files 6% similar despite different names*

```diff
@@ -25,16 +25,18 @@
 from unified_planning.plans import PlanKind
 from unified_planning.engines.mixins.oneshot_planner import OptimalityGuarantee
 from unified_planning.engines.mixins.anytime_planner import AnytimeGuarantee
 from unified_planning.engines.mixins.anytime_planner import AnytimePlannerMixin
 from unified_planning.engines.mixins.compiler import CompilationKind, CompilerMixin
 from unified_planning.engines.mixins.oneshot_planner import OneshotPlannerMixin
 from unified_planning.engines.mixins.plan_validator import PlanValidatorMixin
+from unified_planning.engines.mixins.portfolio import PortfolioSelectorMixin
 from unified_planning.engines.mixins.replanner import ReplannerMixin
 from unified_planning.engines.mixins.simulator import SimulatorMixin
+from unified_planning.engines.engine import OperationMode
 from typing import IO, Any, Dict, Tuple, Optional, List, Union, Type, cast
 from pathlib import PurePath
 
 
 DEFAULT_ENGINES = {
     "fast-downward": ("up_fast_downward", "FastDownwardPDDLPlanner"),
     "fast-downward-opt": ("up_fast_downward", "FastDownwardOptimalPDDLPlanner"),
@@ -67,14 +69,19 @@
         "unified_planning.engines.compilers.quantifiers_remover",
         "QuantifiersRemover",
     ),
     "tarski_grounder": (
         "unified_planning.engines.compilers.tarski_grounder",
         "TarskiGrounder",
     ),
+    "fast-downward-grounder": ("up_fast_downward", "FastDownwardGrounder"),
+    "fast-downward-reachability-grounder": (
+        "up_fast_downward",
+        "FastDownwardReachabilityGrounder",
+    ),
     "up_grounder": ("unified_planning.engines.compilers.grounder", "Grounder"),
 }
 
 DEFAULT_META_ENGINES = {
     "oversubscription": (
         "unified_planning.engines.oversubscription_planner",
         "OversubscriptionPlanner",
@@ -96,14 +103,16 @@
     "sequential_plan_validator",
     "sequential_simulator",
     "up_conditional_effects_remover",
     "up_disjunctive_conditions_remover",
     "up_negative_conditions_remover",
     "up_quantifiers_remover",
     "tarski_grounder",
+    "fast-downward-reachability-grounder",
+    "fast-downward-grounder",
     "up_grounder",
 ]
 
 DEFAULT_META_ENGINES_PREFERENCE_LIST = ["oversubscription"]
 
 
 def format_table(header: List[str], rows: List[List[str]]) -> str:
@@ -358,15 +367,15 @@
             self._meta_engines[name] = EngineImpl
             self._meta_engines_info.append((name, module_name, class_name))
         if EngineImpl.is_compatible_engine(engine):
             self._engines[f"{name}[{engine_name}]"] = EngineImpl[engine]
 
     def _get_engine_class(
         self,
-        engine_kind: str,
+        operation_mode: "OperationMode",
         name: Optional[str] = None,
         problem_kind: ProblemKind = ProblemKind(),
         optimality_guarantee: Optional["OptimalityGuarantee"] = None,
         compilation_kind: Optional["CompilationKind"] = None,
         plan_kind: Optional["PlanKind"] = None,
         anytime_guarantee: Optional["AnytimeGuarantee"] = None,
     ) -> Type["up.engines.engine.Engine"]:
@@ -377,46 +386,52 @@
                 raise up.exceptions.UPNoRequestedEngineAvailableException
         problem_features = list(problem_kind.features)
         planners_features = []
         # Make sure that optimality guarantees and compilation kind are mutually exclusive
         assert optimality_guarantee is None or compilation_kind is None
         for name in self._preference_list:
             EngineClass = self._engines[name]
-            if getattr(EngineClass, "is_" + engine_kind)():
-                if engine_kind == "oneshot_planner" or engine_kind == "replanner":
-                    assert issubclass(EngineClass, OneshotPlannerMixin) or issubclass(
-                        EngineClass, ReplannerMixin
+            if getattr(EngineClass, "is_" + operation_mode.value)():
+                if (
+                    operation_mode == OperationMode.ONESHOT_PLANNER
+                    or operation_mode == OperationMode.REPLANNER
+                    or operation_mode == OperationMode.PORTFOLIO_SELECTOR
+                ):
+                    assert (
+                        issubclass(EngineClass, OneshotPlannerMixin)
+                        or issubclass(EngineClass, ReplannerMixin)
+                        or issubclass(EngineClass, PortfolioSelectorMixin)
                     )
                     assert anytime_guarantee is None
                     assert compilation_kind is None
                     assert plan_kind is None
                     if optimality_guarantee is not None and not EngineClass.satisfies(
                         optimality_guarantee
                     ):
                         continue
-                elif engine_kind == "plan_validator":
+                elif operation_mode == OperationMode.PLAN_VALIDATOR:
                     assert issubclass(EngineClass, PlanValidatorMixin)
                     assert optimality_guarantee is None
                     assert anytime_guarantee is None
                     assert compilation_kind is None
                     if plan_kind is not None and not EngineClass.supports_plan(
                         plan_kind
                     ):
                         continue
-                elif engine_kind == "compiler":
+                elif operation_mode == OperationMode.COMPILER:
                     assert issubclass(EngineClass, CompilerMixin)
                     assert optimality_guarantee is None
                     assert anytime_guarantee is None
                     assert plan_kind is None
                     if (
                         compilation_kind is not None
                         and not EngineClass.supports_compilation(compilation_kind)
                     ):
                         continue
-                elif engine_kind == "anytime_planner":
+                elif operation_mode == OperationMode.ANYTIME_PLANNER:
                     assert issubclass(EngineClass, AnytimePlannerMixin)
                     assert optimality_guarantee is None
                     assert compilation_kind is None
                     assert plan_kind is None
                     if anytime_guarantee is not None and not EngineClass.ensures(
                         anytime_guarantee
                     ):
@@ -442,15 +457,15 @@
         elif plan_kind is not None:
             msg = f"No available engine supports {plan_kind}"
         elif optimality_guarantee is not None:
             msg = f"No available engine supports {optimality_guarantee}"
         elif anytime_guarantee is not None:
             msg = f"No available engine supports {anytime_guarantee}"
         else:
-            msg = f"No available {engine_kind} engine"
+            msg = f"No available {operation_mode} engine"
         raise up.exceptions.UPNoSuitableEngineAvailableException(msg)
 
     def _print_credits(self, all_credits: List[Optional["up.engines.Credits"]]):
         """
         This function prints the credits of the engine(s) used by an operation mode
         """
         credits: List["up.engines.Credits"] = [c for c in all_credits if c is not None]
@@ -496,54 +511,57 @@
                 w.write("you are using the following planning engine:\n")
             for c in credits:
                 c.write_credits(w)
             w.write("\n")
 
     def _get_engine(
         self,
-        engine_kind: str,
+        operation_mode: "OperationMode",
         name: Optional[str] = None,
         names: Optional[List[str]] = None,
         params: Optional[Union[Dict[str, str], List[Dict[str, str]]]] = None,
         problem_kind: ProblemKind = ProblemKind(),
         optimality_guarantee: Optional["OptimalityGuarantee"] = None,
         compilation_kind: Optional["CompilationKind"] = None,
         compilation_kinds: Optional[List["CompilationKind"]] = None,
         plan_kind: Optional["PlanKind"] = None,
         anytime_guarantee: Optional["AnytimeGuarantee"] = None,
         problem: Optional["up.model.AbstractProblem"] = None,
     ) -> "up.engines.engine.Engine":
-        if names is not None and engine_kind != "compiler":
+        if names is not None and operation_mode != OperationMode.COMPILER:
             assert name is None
             assert problem is None, "Parallel simulation is not supported"
             if params is None:
                 params = [{} for i in range(len(names))]
             assert isinstance(params, List) and len(names) == len(params)
             engines = []
             all_credits = []
             for name, param in zip(names, params):
-                EngineClass = self._get_engine_class(engine_kind, name)
+                EngineClass = self._get_engine_class(operation_mode, name)
                 all_credits.append(EngineClass.get_credits(**param))
                 engines.append((name, param))
             self._print_credits(all_credits)
             p_engine = up.engines.parallel.Parallel(self, engines)
             return p_engine
-        elif engine_kind == "compiler" and compilation_kinds is not None:
+        elif operation_mode == OperationMode.COMPILER and compilation_kinds is not None:
             assert name is None
             assert names is not None or problem_kind is not None
             if names is None:
                 names = [None for i in range(len(compilation_kinds))]  # type: ignore
             if params is None:
                 params = [{} for i in range(len(compilation_kinds))]
             assert isinstance(params, List) and len(names) == len(params)
             compilers: List["up.engines.engine.Engine"] = []
             all_credits = []
             for name, param, compilation_kind in zip(names, params, compilation_kinds):
                 EngineClass = self._get_engine_class(
-                    engine_kind, name, problem_kind, compilation_kind=compilation_kind
+                    operation_mode,
+                    name,
+                    problem_kind,
+                    compilation_kind=compilation_kind,
                 )
                 assert issubclass(EngineClass, CompilerMixin)
                 problem_kind = EngineClass.resulting_problem_kind(
                     problem_kind, compilation_kind
                 )
                 all_credits.append(EngineClass.get_credits(**param))
                 compiler = EngineClass(**param)
@@ -554,51 +572,57 @@
         else:
             assert names is None
             error_failed_checks = name is None
             if params is None:
                 params = {}
             assert isinstance(params, Dict)
             EngineClass = self._get_engine_class(
-                engine_kind,
+                operation_mode,
                 name,
                 problem_kind,
                 optimality_guarantee,
                 compilation_kind,
                 plan_kind,
                 anytime_guarantee,
             )
             credits = EngineClass.get_credits(**params)
             self._print_credits([credits])
-            if engine_kind == "replanner":
+            if operation_mode == OperationMode.REPLANNER:
                 assert problem is not None
                 if (
                     problem.kind.has_quality_metrics()
                     and optimality_guarantee == OptimalityGuarantee.SOLVED_OPTIMALLY
                 ):
                     msg = f"The problem has no quality metrics but the engine is required to be optimal!"
                     raise up.exceptions.UPUsageError(msg)
                 res = EngineClass(problem=problem, **params)
-            elif engine_kind == "simulator":
+            elif operation_mode == OperationMode.SIMULATOR:
                 assert problem is not None
                 res = EngineClass(
                     problem=problem,
                     error_on_failed_checks=error_failed_checks,
                     **params,
                 )
-            elif engine_kind == "compiler":
+                assert isinstance(res, SimulatorMixin)
+            elif operation_mode == OperationMode.COMPILER:
                 res = EngineClass(**params)
                 assert isinstance(res, CompilerMixin)
                 if compilation_kind is not None:
                     res.default = compilation_kind
-            elif engine_kind == "oneshot_planner":
+            elif (
+                operation_mode == OperationMode.ONESHOT_PLANNER
+                or operation_mode == OperationMode.PORTFOLIO_SELECTOR
+            ):
                 res = EngineClass(**params)
-                assert isinstance(res, OneshotPlannerMixin)
+                assert isinstance(res, OneshotPlannerMixin) or isinstance(
+                    res, PortfolioSelectorMixin
+                )
                 if optimality_guarantee == OptimalityGuarantee.SOLVED_OPTIMALLY:
                     res.optimality_metric_required = True
-            elif engine_kind == "anytime_planner":
+            elif operation_mode == OperationMode.ANYTIME_PLANNER:
                 res = EngineClass(**params)
                 assert isinstance(res, AnytimePlannerMixin)
                 if (
                     anytime_guarantee == AnytimeGuarantee.INCREASING_QUALITY
                     or anytime_guarantee == AnytimeGuarantee.OPTIMAL_PLANS
                 ):
                     res.optimality_metric_required = True
@@ -631,15 +655,20 @@
                               params=[{'heuristic': 'hadd'}, {'heuristic': 'hmax'}])
         - using 'problem_kind' and 'optimality_guarantee'.
           e.g. OneshotPlanner(problem_kind=problem.kind, optimality_guarantee=SOLVED_OPTIMALLY)
         """
         if isinstance(optimality_guarantee, str):
             optimality_guarantee = OptimalityGuarantee[optimality_guarantee]
         return self._get_engine(
-            "oneshot_planner", name, names, params, problem_kind, optimality_guarantee
+            OperationMode.ONESHOT_PLANNER,
+            name,
+            names,
+            params,
+            problem_kind,
+            optimality_guarantee,
         )
 
     def AnytimePlanner(
         self,
         *,
         name: Optional[str] = None,
         params: Optional[Dict[str, str]] = None,
@@ -661,15 +690,15 @@
 
         It raises an exception if the problem has no optimality metrics and anytime_guarantee
         is equal to INCREASING_QUALITY or OPTIMAL_PLAN.
         """
         if isinstance(anytime_guarantee, str):
             anytime_guarantee = AnytimeGuarantee[anytime_guarantee]
         return self._get_engine(
-            "anytime_planner",
+            OperationMode.ANYTIME_PLANNER,
             name,
             None,
             params,
             problem_kind,
             anytime_guarantee=anytime_guarantee,
         )
 
@@ -693,15 +722,20 @@
                              params=[{'opt1': 'val1'}, {'opt2': 'val2'}])
         - using 'problem_kind' and 'plan_kind' parameters.
           e.g. PlanValidator(problem_kind=problem.kind, plan_kind=plan.kind)
         """
         if isinstance(plan_kind, str):
             plan_kind = PlanKind[plan_kind]
         return self._get_engine(
-            "plan_validator", name, names, params, problem_kind, plan_kind=plan_kind
+            OperationMode.PLAN_VALIDATOR,
+            name,
+            names,
+            params,
+            problem_kind,
+            plan_kind=plan_kind,
         )
 
     def Compiler(
         self,
         *,
         name: Optional[str] = None,
         names: Optional[List[str]] = None,
@@ -740,15 +774,15 @@
                 if isinstance(kind, str):
                     kinds.append(CompilationKind[kind])
                 else:
                     assert isinstance(kind, CompilationKind)
                     kinds.append(kind)
 
         return self._get_engine(
-            "compiler",
+            OperationMode.COMPILER,
             name,
             names,
             params,
             problem_kind,
             compilation_kind=compilation_kind,
             compilation_kinds=kinds,
         )
@@ -765,15 +799,15 @@
         - using 'problem_kind' through the problem field.
           e.g. Simulator(problem)
         - using 'name' (the name of a specific simulator) and eventually some 'params'
           (simulator dependent options).
           e.g. Simulator(problem, name='sequential_simulator')
         """
         return self._get_engine(
-            "simulator", name, None, params, problem.kind, problem=problem
+            OperationMode.SIMULATOR, name, None, params, problem.kind, problem=problem
         )
 
     def Replanner(
         self,
         problem: "up.model.AbstractProblem",
         *,
         name: Optional[str] = None,
@@ -787,23 +821,49 @@
         - using 'name' (the name of a specific replanner) and 'params'
           (replanner dependent options).
           e.g. Replanner(problem, name='replanner[tamer]')
         """
         if isinstance(optimality_guarantee, str):
             optimality_guarantee = OptimalityGuarantee[optimality_guarantee]
         return self._get_engine(
-            "replanner",
+            OperationMode.REPLANNER,
             name,
             None,
             params,
             problem.kind,
             optimality_guarantee,
             problem=problem,
         )
 
+    def PortfolioSelector(
+        self,
+        *,
+        name: Optional[str] = None,
+        params: Optional[Dict[str, Any]] = None,
+        problem_kind: ProblemKind = ProblemKind(),
+        optimality_guarantee: Optional[Union["OptimalityGuarantee", str]] = None,
+    ) -> "up.engines.engine.Engine":
+        """
+        Returns a portfolio selector. There are two ways to call this method:
+        - using 'name' (the name of a specific portfolio) and eventually 'params'
+            (portfolio dependent options).
+          e.g. PortfolioSelector(name='ibacop')
+        - using 'problem_kind' and 'optimality_guarantee'.
+          e.g. OneshotPlanner(problem_kind=problem.kind, optimality_guarantee=SOLVED_OPTIMALLY)
+        """
+        if isinstance(optimality_guarantee, str):
+            optimality_guarantee = OptimalityGuarantee[optimality_guarantee]
+        return self._get_engine(
+            OperationMode.PORTFOLIO_SELECTOR,
+            name=name,
+            params=params,
+            problem_kind=problem_kind,
+            optimality_guarantee=optimality_guarantee,
+        )
+
     def print_engines_info(
         self, stream: IO[str] = sys.stdout, full_credits: bool = True
     ):
         stream.write("These are the engines currently available:\n")
         for Engine in self._engines.values():
             credits = Engine.get_credits()
             if credits is not None:
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/meta_engine.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/meta_engine.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/__init__.py`

 * *Files 25% similar despite different names*

```diff
@@ -19,9 +19,10 @@
     OptimalityGuarantee,
 )
 from unified_planning.engines.mixins.anytime_planner import (
     AnytimePlannerMixin,
     AnytimeGuarantee,
 )
 from unified_planning.engines.mixins.plan_validator import PlanValidatorMixin
+from unified_planning.engines.mixins.portfolio import PortfolioSelectorMixin
 from unified_planning.engines.mixins.simulator import Event, SimulatorMixin
 from unified_planning.engines.mixins.replanner import ReplannerMixin
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/anytime_planner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/anytime_planner.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/compiler.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/compiler.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,14 +24,15 @@
     """Enum representing the available compilation kinds currently in the library."""
 
     GROUNDING = auto()
     CONDITIONAL_EFFECTS_REMOVING = auto()
     DISJUNCTIVE_CONDITIONS_REMOVING = auto()
     NEGATIVE_CONDITIONS_REMOVING = auto()
     QUANTIFIERS_REMOVING = auto()
+    TRAJECTORY_CONSTRAINTS_REMOVING = auto()
 
 
 class CompilerMixin:
     """Generic class for a compiler defining it's interface."""
 
     def __init__(self, default: Optional[CompilationKind] = None):
         self._default = default
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/oneshot_planner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/oneshot_planner.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/plan_validator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/plan_validator.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/replanner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/replanner.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/mixins/simulator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/mixins/simulator.py`

 * *Files 2% similar despite different names*

```diff
@@ -206,14 +206,16 @@
     def is_simulator():
         return True
 
     def is_goal(self, state: "up.model.ROState") -> bool:
         """
         Returns `True` if the given `state` satisfies the :class:`~unified_planning.model.AbstractProblem` :func:`goals <unified_planning.model.Problem.goals>`.
 
+        NOTE: This method does not consider the :func:`quality_metrics <unified_planning.model.Problem.quality_metrics>` of the problem.
+
         :param state: the `State` in which the `problem goals` are evaluated.
         :return: `True` if the evaluation of every `goal` is `True`, `False` otherwise.
         """
         return self._is_goal(state)
 
     def _is_goal(self, state: "up.model.ROState") -> bool:
         """
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/oversubscription_planner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/oversubscription_planner.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/parallel.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/parallel.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/pddl_planner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/pddl_planner.py`

 * *Files 0% similar despite different names*

```diff
@@ -200,15 +200,14 @@
         with tempfile.TemporaryDirectory() as tempdir:
             domain_filename = os.path.join(tempdir, "domain.pddl")
             problem_filename = os.path.join(tempdir, "problem.pddl")
             plan_filename = os.path.join(tempdir, "plan.txt")
             self._writer.write_domain(domain_filename)
             self._writer.write_problem(problem_filename)
             cmd = self._get_cmd(domain_filename, problem_filename, plan_filename)
-
             if output_stream is None:
                 # If we do not have an output stream to write to, we simply call
                 # a subprocess and retrieve the final output and error with communicate
                 process = subprocess.Popen(
                     cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                 )
                 timeout_occurred: bool = False
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/plan_validator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/plan_validator.py`

 * *Files 8% similar despite different names*

```diff
@@ -36,15 +36,21 @@
     SequentialSimulator,
     InstantaneousEvent,
 )
 from unified_planning.plans import SequentialPlan, PlanKind
 
 
 class SequentialPlanValidator(engines.engine.Engine, mixins.PlanValidatorMixin):
-    """Performs :class:`~unified_planning.plans.Plan` validation."""
+    """
+    Performs :class:`~unified_planning.plans.Plan` validation.
+
+    If the given :class:`~unified_planning.model.Problem` has any quality metric,
+    the metric is simply ignored because it predicates over the Optimality of
+    the Plan, but not the Validity!
+    """
 
     def __init__(self, **options):
         engines.engine.Engine.__init__(self)
         self._env: "unified_planning.environment.Environment" = (
             unified_planning.environment.get_env(options.get("env", None))
         )
         self.manager = self._env.expression_manager
@@ -74,14 +80,19 @@
         supported_kind.set_conditions_kind("EXISTENTIAL_CONDITIONS")
         supported_kind.set_conditions_kind("UNIVERSAL_CONDITIONS")
         supported_kind.set_effects_kind("CONDITIONAL_EFFECTS")
         supported_kind.set_effects_kind("INCREASE_EFFECTS")
         supported_kind.set_effects_kind("DECREASE_EFFECTS")
         supported_kind.set_fluents_type("NUMERIC_FLUENTS")
         supported_kind.set_fluents_type("OBJECT_FLUENTS")
+        supported_kind.set_quality_metrics("ACTIONS_COST")
+        supported_kind.set_quality_metrics("PLAN_LENGTH")
+        supported_kind.set_quality_metrics("OVERSUBSCRIPTION")
+        supported_kind.set_quality_metrics("MAKESPAN")
+        supported_kind.set_quality_metrics("FINAL_VALUE")
         return supported_kind
 
     @staticmethod
     def supports(problem_kind):
         return problem_kind <= SequentialPlanValidator.supported_kind()
 
     def _validate(
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/replanner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/replanner.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/results.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/results.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/engines/sequential_simulator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/engines/sequential_simulator.py`

 * *Files 3% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 
 
+from warnings import warn
 import unified_planning as up
 from unified_planning.engines.compilers import Grounder, GrounderHelper
 from unified_planning.engines.engine import Engine
 from unified_planning.engines.mixins.simulator import Event, SimulatorMixin
 from unified_planning.exceptions import UPUsageError, UPConflictingEffectsException
 from unified_planning.plans import ActionInstance
 from unified_planning.model.walkers import StateEvaluator
@@ -49,24 +50,32 @@
     def simulated_effect(self) -> Optional["up.model.SimulatedEffect"]:
         return self._simulated_effect
 
 
 class SequentialSimulator(Engine, SimulatorMixin):
     """
     Sequential SimulatorMixin implementation.
+
+    This Simulator, when considering if a state is goal or not, ignores the
+    quality metrics.
     """
 
     def __init__(
         self, problem: "up.model.Problem", error_on_failed_checks: bool = True, **kwargs
     ):
         Engine.__init__(self)
         self.error_on_failed_checks = error_on_failed_checks
         SimulatorMixin.__init__(self, problem)
         pk = problem.kind
-        assert Grounder.supports(pk)
+        if not Grounder.supports(pk):
+            msg = f"The Grounder used in the {type(self)} does not support the given problem"
+            if self.error_on_failed_checks:
+                raise UPUsageError(msg)
+            else:
+                warn(msg)
         assert isinstance(self._problem, up.model.Problem)
         self._grounder = GrounderHelper(problem)
         self._actions = set(self._problem.actions)
         self._events: Dict[
             Tuple["up.model.Action", Tuple["up.model.FNode", ...]], List[Event]
         ] = {}
         self._se = StateEvaluator(self._problem)
@@ -279,14 +288,19 @@
         supported_kind.set_conditions_kind("EQUALITY")
         supported_kind.set_conditions_kind("EXISTENTIAL_CONDITIONS")
         supported_kind.set_conditions_kind("UNIVERSAL_CONDITIONS")
         supported_kind.set_effects_kind("CONDITIONAL_EFFECTS")
         supported_kind.set_effects_kind("INCREASE_EFFECTS")
         supported_kind.set_effects_kind("DECREASE_EFFECTS")
         supported_kind.set_simulated_entities("SIMULATED_EFFECTS")
+        supported_kind.set_quality_metrics("ACTIONS_COST")
+        supported_kind.set_quality_metrics("PLAN_LENGTH")
+        supported_kind.set_quality_metrics("OVERSUBSCRIPTION")
+        supported_kind.set_quality_metrics("MAKESPAN")
+        supported_kind.set_quality_metrics("FINAL_VALUE")
         return supported_kind
 
     @staticmethod
     def supports(problem_kind):
         return problem_kind <= SequentialSimulator.supported_kind()
 
     def _get_or_create_events(
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/environment.py` & `unified_planning-0.5.0.93.dev1/unified_planning/environment.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/exceptions.py` & `unified_planning-0.5.0.93.dev1/unified_planning/exceptions.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/grpc/converter.py` & `unified_planning-0.5.0.93.dev1/unified_planning/grpc/converter.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/grpc/generated/unified_planning_pb2.py` & `unified_planning-0.5.0.93.dev1/unified_planning/grpc/generated/unified_planning_pb2.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/grpc/generated/unified_planning_pb2_grpc.py` & `unified_planning-0.5.0.93.dev1/unified_planning/grpc/generated/unified_planning_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/grpc/proto_reader.py` & `unified_planning-0.5.0.93.dev1/unified_planning/grpc/proto_reader.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/grpc/proto_writer.py` & `unified_planning-0.5.0.93.dev1/unified_planning/grpc/proto_writer.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/interop/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/interop/__init__.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/interop/from_tarski.py` & `unified_planning-0.5.0.93.dev1/unified_planning/interop/from_tarski.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/interop/to_tarski.py` & `unified_planning-0.5.0.93.dev1/unified_planning/interop/to_tarski.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/io/anml_writer.py` & `unified_planning-0.5.0.93.dev1/unified_planning/io/anml_writer.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/io/pddl_reader.py` & `unified_planning-0.5.0.93.dev1/unified_planning/io/pddl_reader.py`

 * *Files 2% similar despite different names*

```diff
@@ -84,15 +84,15 @@
         variable = Suppress("?") + name
 
         require_def = (
             Suppress("(")
             + ":requirements"
             + OneOrMore(
                 one_of(
-                    ":strips :typing :negative-preconditions :disjunctive-preconditions :equality :existential-preconditions :universal-preconditions :quantified-preconditions :conditional-effects :fluents :numeric-fluents :adl :durative-actions :duration-inequalities :timed-initial-literals :action-costs :hierarchy :method-preconditions :contingent"
+                    ":strips :typing :negative-preconditions :disjunctive-preconditions :equality :existential-preconditions :universal-preconditions :quantified-preconditions :conditional-effects :fluents :numeric-fluents :adl :durative-actions :duration-inequalities :timed-initial-literals :action-costs :hierarchy :method-preconditions :constraints :contingent :preferences"
                 )
             )
             + Suppress(")")
         )
 
         types_def = (
             Suppress("(")
@@ -273,14 +273,20 @@
             + Suppress(")")
             + Optional(
                 Suppress("(")
                 + ":goal"
                 + nested_expr().setResultsName("goal")
                 + Suppress(")")
             )
+            + Optional(
+                Suppress("(")
+                + ":constraints"
+                + nested_expr().setResultsName("constraints")
+                + Suppress(")")
+            )
             + Optional(Suppress("(") + ":metric" + metric + Suppress(")"))
             + Suppress(")")
         )
 
         domain.ignore(";" + rest_of_line)
         problem.ignore(";" + rest_of_line)
 
@@ -321,14 +327,21 @@
             "<": self._em.LT,
             "=": self._em.Equals,
             "+": self._em.Plus,
             "-": self._em.Minus,
             "/": self._em.Div,
             "*": self._em.Times,
         }
+        self._trajectory_constraints: Dict[str, Callable] = {
+            "always": self._em.Always,
+            "sometime": self._em.Sometime,
+            "sometime-before": self._em.SometimeBefore,
+            "sometime-after": self._em.SometimeAfter,
+            "at-most-once": self._em.AtMostOnce,
+        }
         grammar = PDDLGrammar()
         self._pp_domain = grammar.domain
         self._pp_problem = grammar.problem
         self._pp_parameters = grammar.parameters
         self._fve = self._env.free_vars_extractor
         self._totalcost: typing.Optional[up.model.FNode] = None
 
@@ -352,14 +365,19 @@
                     op: Callable = self._operators[exp[0]]
                     solved.append(op(*[solved.pop() for _ in exp[1:]]))
                 elif exp[0] in ["exists", "forall"]:  # quantifier operators
                     q_op: Callable = (
                         self._em.Exists if exp[0] == "exists" else self._em.Forall
                     )
                     solved.append(q_op(solved.pop(), *var.values()))
+                elif (
+                    exp[0] in self._trajectory_constraints
+                ):  # trajectory_constraints reference
+                    t_op: Callable = self._trajectory_constraints[exp[0]]
+                    solved.append(t_op(*[solved.pop() for _ in exp[1:]]))
                 elif problem.has_fluent(exp[0]):  # fluent reference
                     f = problem.fluent(exp[0])
                     args = [solved.pop() for _ in exp[1:]]
                     solved.append(self._em.FluentExp(f, tuple(args)))
                 elif exp[0] in assignments:  # quantified assignment variable
                     assert len(exp) == 1
                     solved.append(self._em.ObjectExp(assignments[exp[0]]))
@@ -386,14 +404,20 @@
                                 new_vars[o] = up.model.Variable(o, t, self._env)
                         # new_vars are the variables defined by the quantifier currently being solved
                         # all_vars are the variables defined by all the quantifiers around this expression
                         stack.append((new_vars, exp, True))
                         all_vars = var.copy()
                         all_vars.update(new_vars)
                         stack.append((all_vars, exp[2], False))
+                    elif (
+                        exp[0] in self._trajectory_constraints
+                    ):  # trajectory_constraints reference
+                        stack.append((var, exp, True))
+                        for e in exp[1:]:
+                            stack.append((var, e, False))
                     elif problem.has_fluent(exp[0]):  # fluent reference
                         stack.append((var, exp, True))
                         for e in exp[1:]:
                             stack.append((var, e, False))
                     elif exp[0] in assignments:  # quantified assignment variable
                         assert len(exp) == 1
                         stack.append((var, exp, True))
@@ -1164,18 +1188,24 @@
                     self._parse_exp(
                         problem, None, types_map, {}, problem_res["goal"][0]
                     )
                 )
             elif not isinstance(problem, htn.HierarchicalProblem):
                 raise SyntaxError("Missing goal section in problem file.")
 
+            if "constraints" in problem_res:
+                problem.add_trajectory_constraint(
+                    self._parse_exp(
+                        problem, None, types_map, {}, problem_res["constraints"][0]
+                    )
+                )
+
             has_actions_cost = has_actions_cost and self._problem_has_actions_cost(
                 problem
             )
-
             optimization = problem_res.get("optimization", None)
             metric = problem_res.get("metric", None)
 
             if metric is not None:
                 if (
                     optimization == "minimize"
                     and len(metric) == 1
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/io/pddl_writer.py` & `unified_planning-0.5.0.93.dev1/unified_planning/io/pddl_writer.py`

 * *Files 3% similar despite different names*

```diff
@@ -200,14 +200,34 @@
         assert len(args) == 1
         vars_string_list = [
             f"{self.get_mangled_name(v)} - {self.get_mangled_name(v.type)}"
             for v in expression.variables()
         ]
         return f'(forall ({" ".join(vars_string_list)})\n {args[0]})'
 
+    def walk_always(self, expression, args):
+        assert len(args) == 1
+        return f"(always {args[0]})"
+
+    def walk_at_most_once(self, expression, args):
+        assert len(args) == 1
+        return f"(at-most-once {args[0]})"
+
+    def walk_sometime(self, expression, args):
+        assert len(args) == 1
+        return f"(sometime {args[0]})"
+
+    def walk_sometime_before(self, expression, args):
+        assert len(args) == 2
+        return f"(sometime-before {args[0]} {args[1]})"
+
+    def walk_sometime_after(self, expression, args):
+        assert len(args) == 2
+        return f"(sometime-after {args[0]} {args[1]})"
+
     def walk_variable_exp(self, expression, args):
         assert len(args) == 0
         return f"{self.get_mangled_name(expression.variable())}"
 
     def walk_and(self, expression, args):
         assert len(args) > 1
         return f'(and {" ".join(args)})'
@@ -359,14 +379,16 @@
                 or self.problem_kind.has_discrete_numbers()
             ):
                 out.write(" :numeric-fluents")
             if self.problem_kind.has_conditional_effects():
                 out.write(" :conditional-effects")
             if self.problem_kind.has_existential_conditions():
                 out.write(" :existential-preconditions")
+            if self.problem_kind.has_trajectory_constraints():
+                out.write(" :constraints")
             if self.problem_kind.has_universal_conditions():
                 out.write(" :universal-preconditions")
             if (
                 self.problem_kind.has_continuous_time()
                 or self.problem_kind.has_discrete_time()
             ):
                 out.write(" :durative-actions")
@@ -476,16 +498,19 @@
                 for a in self.problem.actions:
                     costs[a] = self.problem.env.expression_manager.Int(1)
         elif len(metrics) > 1:
             raise up.exceptions.UPUnsupportedProblemTypeError(
                 "Only one metric is supported!"
             )
 
+        em = self.problem.env.expression_manager
         for a in self.problem.actions:
             if isinstance(a, up.model.InstantaneousAction):
+                if em.FALSE() in a.preconditions:
+                    continue
                 out.write(f" (:action {self._get_mangled_name(a)}")
                 out.write(f"\n  :parameters (")
                 for ap in a.parameters:
                     if ap.type.is_user_type():
                         out.write(
                             f" {self._get_mangled_name(ap)} - {self._get_mangled_name(ap.type)}"
                         )
@@ -523,14 +548,16 @@
                     if a in costs:
                         out.write(
                             f" (increase (total-cost) {converter.convert(costs[a])})"
                         )
                     out.write(")")
                 out.write(")\n")
             elif isinstance(a, DurativeAction):
+                if any(em.FALSE() in cl for cl in a.conditions.values()):
+                    continue
                 out.write(f" (:durative-action {self._get_mangled_name(a)}")
                 out.write(f"\n  :parameters (")
                 for ap in a.parameters:
                     if ap.type.is_user_type():
                         out.write(
                             f" {self._get_mangled_name(ap)} - {self._get_mangled_name(ap.type)}"
                         )
@@ -647,14 +674,18 @@
                 out.write(f" (= {converter.convert(f)} {converter.convert(v)})")
         if self.problem.kind.has_actions_cost():
             out.write(f" (= (total-cost) 0)")
         out.write(")\n")
         out.write(
             f' (:goal (and {" ".join([converter.convert(p) for p in self.problem.goals])}))\n'
         )
+        if len(self.problem.trajectory_constraints) > 0:
+            out.write(
+                f' (:constraints {" ".join([converter.convert(c) for c in self.problem.trajectory_constraints])})\n'
+            )
         metrics = self.problem.quality_metrics
         if len(metrics) == 1:
             metric = metrics[0]
             out.write(" (:metric ")
             if isinstance(metric, up.model.metrics.MinimizeExpressionOnFinalState):
                 out.write(f"minimize {converter.convert(metric.expression)}")
             elif isinstance(metric, up.model.metrics.MaximizeExpressionOnFinalState):
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/io/python_writer.py` & `unified_planning-0.5.0.93.dev1/unified_planning/io/python_writer.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/abstract_problem.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/abstract_problem.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/action.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/action.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/contingent_problem.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/contingent_problem.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/effect.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/effect.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/expression.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/expression.py`

 * *Files 4% similar despite different names*

```diff
@@ -344,14 +344,75 @@
         for v in vars:
             if not isinstance(v, up.model.variable.Variable):
                 raise UPTypeError("Expecting 'up.Variable', got %s", type(v))
         return self.create_node(
             node_type=OperatorKind.FORALL, args=expressions, payload=vars
         )
 
+    def Always(self, expression: BoolExpression) -> "up.model.fnode.FNode":
+        """Creates an expression of the form:
+            `Always(a)`
+        Restriction: expression must be of `boolean type` and with only one arg.
+
+        :param expression: The `boolean` expression of the trajectory constraints.
+        :return: The created `Always` expression.
+        """
+        expressions = tuple(self.auto_promote(expression))
+        return self.create_node(node_type=OperatorKind.ALWAYS, args=expressions)
+
+    def Sometime(self, expression: BoolExpression) -> "up.model.fnode.FNode":
+        """Creates an expression of the form:
+            `Sometime(a)`
+        Restriction: expression must be of `boolean type` and with only one arg.
+
+        :param expression: The `boolean` expression of the trajectory constraints.
+        :return: The created `Sometime` expression.
+        """
+        expressions = tuple(self.auto_promote(expression))
+        return self.create_node(node_type=OperatorKind.SOMETIME, args=expressions)
+
+    def AtMostOnce(self, expression: BoolExpression) -> "up.model.fnode.FNode":
+        """Creates an expression of the form:
+            `At-Most-Once(a, b)`
+        Restriction: expression must be of `boolean type` and with only two arg.
+
+        :param expression: The `boolean` expression of the trajectory constraints.
+        :return: The created `At-Most-Once(a, b)` expression.
+        """
+        expressions = tuple(self.auto_promote(expression))
+        return self.create_node(node_type=OperatorKind.AT_MOST_ONCE, args=expressions)
+
+    def SometimeBefore(
+        self, phi: BoolExpression, psi: BoolExpression
+    ) -> "up.model.fnode.FNode":
+        """Creates an expression of the form:
+            `Sometime-Before(a, b)`
+        Restriction: expression must be of `boolean type` and with only one args
+
+        :param expression: The `boolean` expression of the trajectory constraints.
+        :return: The created `Sometime` expression.
+        """
+        expressions = tuple(self.auto_promote(phi, psi))
+        return self.create_node(
+            node_type=OperatorKind.SOMETIME_BEFORE, args=expressions
+        )
+
+    def SometimeAfter(
+        self, phi: BoolExpression, psi: BoolExpression
+    ) -> "up.model.fnode.FNode":
+        """Creates an expression of the form:
+            `Sometime-After(a, b)`
+        Restriction: expression must be of `boolean type` and with only two arg.
+
+        :param expression: The `boolean` expression of the trajectory constraints.
+        :return: The created `Sometime-After(a, b)` expression.
+        """
+        expressions = tuple(self.auto_promote(phi, psi))
+        return self.create_node(node_type=OperatorKind.SOMETIME_AFTER, args=expressions)
+
     def FluentExp(
         self, fluent: "up.model.fluent.Fluent", params: Iterable[Expression] = tuple()
     ) -> "up.model.fnode.FNode":
         """
         Creates an expression for the given `fluent` and `parameters`.
         Restriction: `parameters type` must be compatible with the `Fluent` :func:`signature <unified_planning.model.Fluent.signature>`
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/fluent.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/fluent.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/fnode.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/fnode.py`

 * *Files 6% similar despite different names*

```diff
@@ -92,14 +92,26 @@
         elif self.is_implies():
             return self.get_nary_expression_string(" implies ", self.args)
         elif self.is_iff():
             return self.get_nary_expression_string(" iff ", self.args)
         elif self.is_exists():
             s = ", ".join(str(v) for v in self.variables())
             return f"Exists ({s}) {str(self.arg(0))}"
+        elif self.is_always():
+            return f"Always({str(self.arg(0))})"
+        elif self.is_sometime():
+            return f"Sometime({str(self.arg(0))})"
+        elif self.is_sometime_before():
+            s = ", ".join(str(v) for v in self.args)
+            return f"Sometime-Before({str(s)})"
+        elif self.is_sometime_after():
+            s = ", ".join(str(v) for v in self.args)
+            return f"Sometime-After({str(s)})"
+        elif self.is_at_most_once():
+            return f"At-Most-Once({str(self.arg(0))})"
         elif self.is_forall():
             s = ", ".join(str(v) for v in self.variables())
             return f"Forall ({s}) {str(self.arg(0))}"
         elif self.is_plus():
             return self.get_nary_expression_string(" + ", self.args)
         elif self.is_minus():
             return self.get_nary_expression_string(" - ", self.args)
@@ -186,15 +198,15 @@
 
     def parameter(self) -> "unified_planning.model.parameter.Parameter":
         """Return the `Parameter` stored in this expression."""
         assert self.is_parameter_exp()
         return self._content.payload
 
     def variable(self) -> "unified_planning.model.variable.Variable":
-        """Return the `Variable` stored in this expression."""
+        """Return the variable of the VariableExp."""
         assert self.is_variable_exp()
         return self._content.payload
 
     def variables(self) -> List["unified_planning.model.variable.Variable"]:
         """Return the `Variables` of the `Exists` or `Forall`."""
         assert self.is_exists() or self.is_forall()
         return list(self._content.payload)
@@ -262,14 +274,34 @@
         """Test whether the node is the `Iff` operator."""
         return self.node_type == OperatorKind.IFF
 
     def is_exists(self) -> bool:
         """Test whether the node is the `Exists` operator."""
         return self.node_type == OperatorKind.EXISTS
 
+    def is_always(self) -> bool:
+        """Test whether the node is the Always constraint."""
+        return self.node_type == OperatorKind.ALWAYS
+
+    def is_sometime(self) -> bool:
+        """Test whether the node is the Sometime constraint."""
+        return self.node_type == OperatorKind.SOMETIME
+
+    def is_at_most_once(self) -> bool:
+        """Test whether the node is the At-Most-Once constraint."""
+        return self.node_type == OperatorKind.AT_MOST_ONCE
+
+    def is_sometime_before(self) -> bool:
+        """Test whether the node is the Sometime-Before constraint."""
+        return self.node_type == OperatorKind.SOMETIME_BEFORE
+
+    def is_sometime_after(self) -> bool:
+        """Test whether the node is the Sometime-After constraint."""
+        return self.node_type == OperatorKind.SOMETIME_AFTER
+
     def is_forall(self) -> bool:
         """Test whether the node is the `Forall` operator."""
         return self.node_type == OperatorKind.FORALL
 
     def is_fluent_exp(self) -> bool:
         """Test whether the node is a :class:`~unified_planning.model.Fluent` Expression."""
         return self.node_type == OperatorKind.FLUENT_EXP
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/htn/hierarchical_problem.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/htn/hierarchical_problem.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/htn/method.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/htn/method.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/htn/task.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/htn/task.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/htn/task_network.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/htn/task_network.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/metrics.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/metrics.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/__init__.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/actions_set.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/actions_set.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/agents_set.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/agents_set.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/fluents_set.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/fluents_set.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/objects_set.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/objects_set.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/mixins/user_types_set.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/mixins/user_types_set.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/__init__.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/agent.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/agent.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/ma_environment.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/ma_environment.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/multi_agent/ma_problem.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/multi_agent/ma_problem.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/object.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/object.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/operators.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/operators.py`

 * *Files 7% similar despite different names*

```diff
@@ -40,14 +40,19 @@
     PLUS = auto()
     MINUS = auto()
     TIMES = auto()
     DIV = auto()
     LE = auto()
     LT = auto()
     EQUALS = auto()
+    ALWAYS = auto()
+    SOMETIME = auto()
+    SOMETIME_BEFORE = auto()
+    SOMETIME_AFTER = auto()
+    AT_MOST_ONCE = auto()
     DOT = auto()
 
 
 BOOL_OPERATORS = frozenset(
     [
         OperatorKind.AND,
         OperatorKind.OR,
@@ -66,7 +71,17 @@
 IRA_RELATIONS = frozenset([OperatorKind.LE, OperatorKind.LT])
 
 RELATIONS = frozenset((OperatorKind.EQUALS,)) | IRA_RELATIONS
 
 IRA_OPERATORS = frozenset(
     [OperatorKind.PLUS, OperatorKind.MINUS, OperatorKind.TIMES, OperatorKind.DIV]
 )
+
+TRAJECTORY_CONSTRAINTS = frozenset(
+    [
+        OperatorKind.ALWAYS,
+        OperatorKind.SOMETIME,
+        OperatorKind.SOMETIME_BEFORE,
+        OperatorKind.SOMETIME_AFTER,
+        OperatorKind.AT_MOST_ONCE,
+    ]
+)
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/parameter.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/parameter.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/problem.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/problem.py`

 * *Files 7% similar despite different names*

```diff
@@ -66,14 +66,15 @@
         self._initial_value: Dict["up.model.fnode.FNode", "up.model.fnode.FNode"] = {}
         self._timed_effects: Dict[
             "up.model.timing.Timing", List["up.model.effect.Effect"]
         ] = {}
         self._timed_goals: Dict[
             "up.model.timing.TimeInterval", List["up.model.fnode.FNode"]
         ] = {}
+        self._trajectory_constraints: List["up.model.fnode.FNode"] = list()
         self._goals: List["up.model.fnode.FNode"] = list()
         self._metrics: List["up.model.metrics.PlanQualityMetric"] = []
 
     def __repr__(self) -> str:
         s = []
         if not self.name is None:
             s.append(f"problem name = {str(self.name)}\n\n")
@@ -116,14 +117,19 @@
                 for g in gl:
                     s.append(f"    {str(g)}\n")
             s.append("]\n\n")
         s.append("goals = [\n")
         for g in self.goals:
             s.append(f"  {str(g)}\n")
         s.append("]\n\n")
+        if self.trajectory_constraints:
+            s.append("trajectory constraints = [\n")
+            for c in self.trajectory_constraints:
+                s.append(f"  {str(c)}\n")
+            s.append("]\n\n")
         if len(self.quality_metrics) > 0:
             s.append("quality metrics = [\n")
             for qm in self.quality_metrics:
                 s.append(f"  {str(qm)}\n")
             s.append("]\n\n")
         return "".join(s)
 
@@ -138,14 +144,16 @@
             return False
         if set(self._user_types) != set(oth._user_types) or set(self._objects) != set(
             oth._objects
         ):
             return False
         if set(self._actions) != set(oth._actions):
             return False
+        if set(self._trajectory_constraints) != set(oth._trajectory_constraints):
+            return False
         oth_initial_values = oth.initial_values
         initial_values = self.initial_values
         if len(initial_values) != len(oth_initial_values):
             return False
         for fluent, value in initial_values.items():
             oth_value = oth_initial_values.get(fluent, None)
             if oth_value is None:
@@ -176,14 +184,16 @@
             res += hash(f)
         for a in self._actions:
             res += hash(a)
         for ut in self._user_types:
             res += hash(ut)
         for o in self._objects:
             res += hash(o)
+        for c in self._trajectory_constraints:
+            res += hash(c)
         for iv in self.initial_values.items():
             res += hash(iv)
         for t, el in self._timed_effects.items():
             res += hash(t)
             for e in set(el):
                 res += hash(e)
         for i, gl in self._timed_goals.items():
@@ -203,14 +213,15 @@
         new_p._objects = self._objects[:]
         new_p._initial_value = self._initial_value.copy()
         new_p._timed_effects = {
             t: [e.clone() for e in el] for t, el in self._timed_effects.items()
         }
         new_p._timed_goals = {i: [g for g in gl] for i, gl in self._timed_goals.items()}
         new_p._goals = self._goals[:]
+        new_p._trajectory_constraints = self._trajectory_constraints[:]
         new_p._metrics = []
         for m in self._metrics:
             if isinstance(m, up.model.metrics.MinimizeActionCosts):
                 costs = {new_p.action(a.name): c for a, c in m.costs.items()}
                 new_p._metrics.append(up.model.metrics.MinimizeActionCosts(costs))
             else:
                 new_p._metrics.append(m)
@@ -551,23 +562,61 @@
             isinstance(goal, bool) or goal.environment == self._env
         ), "goal does not have the same environment of the problem"
         (goal_exp,) = self._env.expression_manager.auto_promote(goal)
         assert self._env.type_checker.get_type(goal_exp).is_bool_type()
         if goal_exp != self._env.expression_manager.TRUE():
             self._goals.append(goal_exp)
 
+    def add_trajectory_constraint(self, constraint: "up.model.fnode.FNode"):
+        """
+        Adds the given `trajectory_constraint` to the `Problem`;
+        a trajectory_constraint is an expression defined as:
+        Always, Sometime, At-Most-Once, Sometime-Before, Sometime-After or
+        defined with universal quantifiers.
+        Nesting of these temporal operators is forbidden.
+
+        :param trajectory_constraint: The expression added to the `Problem`.
+        """
+        if constraint.is_and() or constraint.is_forall():
+            for arg in constraint.args:
+                assert (
+                    arg.is_sometime()
+                    or arg.is_sometime_after()
+                    or arg.is_sometime_before()
+                    or arg.is_at_most_once()
+                    or arg.is_always()
+                ), "trajectory constraint not in the correct form"
+        else:
+            assert (
+                constraint.is_sometime()
+                or constraint.is_sometime_after()
+                or constraint.is_sometime_before()
+                or constraint.is_at_most_once()
+                or constraint.is_always()
+            ), "trajectory constraint not in the correct form"
+        self._trajectory_constraints.append(constraint.simplify())
+
     @property
     def goals(self) -> List["up.model.fnode.FNode"]:
         """Returns all the `goals` in the `Problem`."""
         return self._goals
 
+    @property
+    def trajectory_constraints(self) -> List["up.model.fnode.FNode"]:
+        """Returns the 'trajectory_constraints' in the 'Problem'."""
+        return self._trajectory_constraints
+
     def clear_goals(self):
         """Removes all the `goals` from the `Problem`."""
         self._goals = []
 
+    def clear_trajectory_constraints(self):
+        """Removes the trajectory_constraints."""
+        self._trajectory_constraints = []
+
     def add_quality_metric(self, metric: "up.model.metrics.PlanQualityMetric"):
         """
         Adds the given `quality metric` to the `Problem`; a `quality metric` defines extra requirements that a :class:`~unified_planning.plans.Plan`
         must satisfy in order to be valid.
 
         :param metric: The `quality metric` that a `Plan` of this `Problem` must satisfy in order to be valid.
         """
@@ -669,14 +718,16 @@
                     fluents_to_only_decrease,
                     simplifier,
                     linear_checker,
                 )
         if len(self._timed_goals) > 0:
             self._kind.set_time("TIMED_GOALS")
             self._kind.set_time("CONTINUOUS_TIME")
+        if len(self._trajectory_constraints) > 0:
+            self._kind.set_constraints_kind("TRAJECTORY_CONSTRAINTS")
         for goal_list in self._timed_goals.values():
             for goal in goal_list:
                 self._update_problem_kind_condition(goal, linear_checker)
         for goal in self._goals:
             self._update_problem_kind_condition(goal, linear_checker)
         if (
             not self._kind.has_continuous_numbers()
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/problem_kind.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/problem_kind.py`

 * *Files 1% similar despite different names*

```diff
@@ -46,14 +46,15 @@
         "ACTIONS_COST",
         "FINAL_VALUE",
         "MAKESPAN",
         "PLAN_LENGTH",
         "OVERSUBSCRIPTION",
     ],
     "SIMULATED_ENTITIES": ["SIMULATED_EFFECTS"],
+    "CONSTRAINTS_KIND": ["TRAJECTORY_CONSTRAINTS"],
 }
 
 
 class ProblemKindMeta(type):
     """Meta class used to interpret the nodehandler decorator."""
 
     def __new__(cls, name, bases, dct):
@@ -216,7 +217,10 @@
 quality_metrics_kind = ProblemKind()
 quality_metrics_kind.set_quality_metrics("PLAN_LENGTH")
 quality_metrics_kind.set_quality_metrics("ACTIONS_COST")
 quality_metrics_kind.set_quality_metrics("FINAL_VALUE")
 
 oversubscription_kind = ProblemKind()
 oversubscription_kind.set_quality_metrics("OVERSUBSCRIPTION")
+
+actions_cost_kind = ProblemKind()
+actions_cost_kind.set_quality_metrics("ACTIONS_COST")
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/state.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/state.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/timing.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/timing.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/types.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/types.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/variable.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/variable.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/__init__.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/dag.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/dag.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/dnf.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/dnf.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/expression_quantifiers_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/expression_quantifiers_remover.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/free_vars.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/free_vars.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/generic.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/generic.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/identitydag.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/identitydag.py`

 * *Files 12% similar despite different names*

```diff
@@ -108,7 +108,28 @@
         return self.manager.VariableExp(expression.variable())
 
     def walk_object_exp(self, expression: FNode, args: List[FNode], **kwargs) -> FNode:
         return self.manager.ObjectExp(expression.object())
 
     def walk_timing_exp(self, expression: FNode, args: List[FNode], **kwargs) -> FNode:
         return self.manager.TimingExp(expression.timing())
+
+    def walk_at_most_once(
+        self, expression: FNode, args: List[FNode], **kwargs
+    ) -> FNode:
+        return self.manager.AtMostOnce(args[0])
+
+    def walk_always(self, expression: FNode, args: List[FNode], **kwargs) -> FNode:
+        return self.manager.Always(args[0])
+
+    def walk_sometime(self, expression: FNode, args: List[FNode], **kwargs) -> FNode:
+        return self.manager.Sometime(args[0])
+
+    def walk_sometime_before(
+        self, expression: FNode, args: List[FNode], **kwargs
+    ) -> FNode:
+        return self.manager.SometimeBefore(args[0], args[1])
+
+    def walk_sometime_after(
+        self, expression: FNode, args: List[FNode], **kwargs
+    ) -> FNode:
+        return self.manager.SometimeAfter(args[0], args[1])
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/linear_checker.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/linear_checker.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/operators_extractor.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/operators_extractor.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/quantifier_simplifier.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/quantifier_simplifier.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/simplifier.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/simplifier.py`

 * *Files 4% similar despite different names*

```diff
@@ -191,14 +191,55 @@
             "up.model.variable.Variable"
         ] = self.env.free_vars_oracle.get_free_variables(args[0])
         vars = tuple(var for var in expression.variables() if var in free_vars)
         if len(vars) == 0:
             return args[0]
         return self.manager.Forall(args[0], *vars)
 
+    def walk_always(self, expression: FNode, args: List[FNode]) -> FNode:
+        assert len(args) == 1
+        if args[0].is_true():
+            return self.manager.TRUE()
+        if args[0].is_false():
+            return self.manager.FALSE()
+        return self.manager.Always(args[0])
+
+    def walk_at_most_once(self, expression: FNode, args: List[FNode]) -> FNode:
+        assert len(args) == 1
+        if args[0].is_true() or args[0].is_false():
+            return self.manager.TRUE()
+        return self.manager.AtMostOnce(args[0])
+
+    def walk_sometime(self, expression: FNode, args: List[FNode]) -> FNode:
+        assert len(args) == 1
+        if args[0].is_true():
+            return self.manager.TRUE()
+        if args[0].is_false():
+            return self.manager.FALSE()
+        return self.manager.Sometime(args[0])
+
+    def walk_sometime_before(self, expression: FNode, args: List[FNode]) -> FNode:
+        assert len(args) == 2
+        if args[0].is_false():
+            return self.manager.TRUE()
+        if args[0].is_true():
+            return self.manager.FALSE()
+        return self.manager.SometimeBefore(args[0], args[1])
+
+    def walk_sometime_after(self, expression: FNode, args: List[FNode]) -> FNode:
+        assert len(args) == 2
+        if args[0].is_false():
+            return self.manager.TRUE()
+        if args[0].is_true():
+            if args[1].is_true():
+                return self.manager.TRUE()
+            if args[1].is_false():
+                return self.manager.FALSE()
+        return self.manager.SometimeAfter(args[0], args[1])
+
     def walk_equals(self, expression: FNode, args: List[FNode]) -> FNode:
         assert len(args) == 2
 
         sl = args[0]
         sr = args[1]
 
         if sl.is_constant() and sr.is_constant():
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/state_evaluator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/state_evaluator.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/substituter.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/substituter.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/model/walkers/type_checker.py` & `unified_planning-0.5.0.93.dev1/unified_planning/model/walkers/type_checker.py`

 * *Files 12% similar despite different names*

```diff
@@ -80,14 +80,79 @@
     def walk_param_exp(
         self, expression: FNode, args: List["unified_planning.model.types.Type"]
     ) -> "unified_planning.model.types.Type":
         assert expression is not None
         assert len(args) == 0
         return expression.parameter().type
 
+    def walk_always(
+        self, expression: FNode, args: List["unified_planning.model.types.Type"]
+    ) -> Optional["unified_planning.model.types.Type"]:
+        assert expression is not None
+        assert expression.is_always()
+        assert len(expression.args) == 1
+        if args[0] is None or not args[0].is_bool_type():
+            return None
+        return args[0]
+
+    def walk_sometime(
+        self, expression: FNode, args: List["unified_planning.model.types.Type"]
+    ) -> Optional["unified_planning.model.types.Type"]:
+        assert expression is not None
+        assert expression.is_sometime()
+        assert len(expression.args) == 1
+        if args[0] is None or not args[0].is_bool_type():
+            return None
+        return args[0]
+
+    def walk_at_most_once(
+        self, expression: FNode, args: List["unified_planning.model.types.Type"]
+    ) -> Optional["unified_planning.model.types.Type"]:
+        assert expression is not None
+        assert expression.is_at_most_once()
+        assert len(expression.args) == 1
+        if args[0] is None or not args[0].is_bool_type():
+            return None
+        return args[0]
+
+    def walk_sometime_before(
+        self, expression: FNode, args: List["unified_planning.model.types.Type"]
+    ) -> Optional["unified_planning.model.types.Type"]:
+        assert expression is not None
+        assert expression.is_sometime_before()
+        assert len(expression.args) == 2
+        if (
+            args[0] is None
+            or args[1] is None
+            or not args[0].is_bool_type()
+            or not args[1].is_bool_type()
+            or args[0] != args[1]
+        ):
+            return None
+        else:
+            return args[0]
+
+    def walk_sometime_after(
+        self, expression: FNode, args: List["unified_planning.model.types.Type"]
+    ) -> Optional["unified_planning.model.types.Type"]:
+        assert expression is not None
+        assert expression.is_sometime_after()
+        assert len(expression.args) == 2
+        assert expression.args[0].type == expression.args[1].type
+        if (
+            args[0] is None
+            or args[1] is None
+            or not args[0].is_bool_type()
+            or not args[1].is_bool_type()
+            or args[0] != args[1]
+        ):
+            return None
+        else:
+            return args[0]
+
     def walk_variable_exp(
         self, expression: FNode, args: List["unified_planning.model.types.Type"]
     ) -> "unified_planning.model.types.Type":
         assert expression is not None
         assert len(args) == 0
         return expression.variable().type
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/plans/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/plans/__init__.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/plans/contingent_plan.py` & `unified_planning-0.5.0.93.dev1/unified_planning/plans/contingent_plan.py`

 * *Files 5% similar despite different names*

```diff
@@ -171,7 +171,27 @@
         ],
     ) -> "up.plans.plan.Plan":
         if self.root_node is None:
             return ContingentPlan(None, self._environment)
         new_root = self.root_node.replace_action_instances(replace_function)
         new_env = new_root.action_instance.action.env
         return ContingentPlan(new_root, new_env)
+
+    def convert_to(
+        self,
+        plan_kind: "plans.plan.PlanKind",
+        problem: "up.model.AbstractProblem",
+    ) -> "plans.plan.Plan":
+        """
+        This function takes a `PlanKind` and returns the representation of `self`
+        in the given `plan_kind`. If the conversion does not make sense, raises
+        an exception.
+
+        :param plan_kind: The plan_kind of the returned plan.
+        :param problem: The `Problem` of which this plan is referring to.
+        :return: The plan equivalent to self but represented in the kind of
+            `plan_kind`.
+        """
+        if plan_kind == self._kind:
+            return self
+        else:
+            raise UPUsageError(f"{type(self)} can't be converted to {plan_kind}.")
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/plans/partial_order_plan.py` & `unified_planning-0.5.0.93.dev1/unified_planning/plans/partial_order_plan.py`

 * *Files 5% similar despite different names*

```diff
@@ -155,17 +155,41 @@
 
         new_env = self._environment
         for ai in new_adj_list.keys():
             new_env = ai.action.env
             break
         return up.plans.PartialOrderPlan(new_adj_list, new_env)
 
-    def to_sequential_plan(self) -> SequentialPlan:
-        """Returns one between all possible `SequentialPlans` that respects the ordering constraints given by this `PartialOrderPlan`."""
-        return SequentialPlan(list(nx.topological_sort(self._graph)), self._environment)
+    def convert_to(
+        self,
+        plan_kind: "plans.plan.PlanKind",
+        problem: "up.model.AbstractProblem",
+    ) -> "plans.plan.Plan":
+        """
+        This function takes a `PlanKind` and returns the representation of `self`
+        in the given `plan_kind`. If the conversion does not make sense, raises
+        an exception.
+
+        For the conversion to `SequentialPlan`, returns one  all possible
+        `SequentialPlans` that respects the ordering constraints given by
+        this `PartialOrderPlan`.
+
+        :param plan_kind: The plan_kind of the returned plan.
+        :param problem: The `Problem` of which this plan is referring to.
+        :return: The plan equivalent to self but represented in the kind of
+            `plan_kind`.
+        """
+        if plan_kind == self._kind:
+            return self
+        elif plan_kind == plans.plan.PlanKind.SEQUENTIAL_PLAN:
+            return SequentialPlan(
+                list(nx.topological_sort(self._graph)), self._environment
+            )
+        else:
+            raise UPUsageError(f"{type(self)} can't be converted to {plan_kind}.")
 
     def all_sequential_plans(self) -> Iterator[SequentialPlan]:
         """Returns all possible `SequentialPlans` that respects the ordering constraints given by this `PartialOrderPlan`."""
         for sorted_plan in nx.all_topological_sorts(self._graph):
             yield SequentialPlan(list(sorted_plan), self._environment)
 
     def get_neighbors(
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/plans/plan.py` & `unified_planning-0.5.0.93.dev1/unified_planning/plans/plan.py`

 * *Files 11% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
 
 
 import unified_planning as up
 from unified_planning.environment import Environment, get_env
+from unified_planning.model import AbstractProblem
 from typing import Callable, Optional, Tuple
 from enum import Enum, auto
 
 
 """This module defines the general `Plan` interface and the `ActionInstance` class."""
 
 
@@ -129,7 +130,20 @@
 
         If the returned `ActionInstance` is `None` it means that the `ActionInstance` should not go in the resulting `Plan`.
 
         :param replace_function: The function that must be used on the `ActionInstances` that must be replaced.
         :return: The new `Plan` in which every `ActionInstance` of the original `Plan` is modified by the given `replace_function`.
         """
         raise NotImplementedError
+
+    def convert_to(self, plan_kind: PlanKind, problem: AbstractProblem) -> "Plan":
+        """
+        This function takes a `PlanKind` and returns the representation of `self`
+        in the given `plan_kind`. If the conversion does not make sense, raises
+        an exception.
+
+        :param plan_kind: The plan_kind of the returned plan.
+        :param problem: The `Problem` of which this plan is referring to.
+        :return: The plan equivalent to self but represented in the kind of
+            `plan_kind`.
+        """
+        raise NotImplementedError
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/plans/sequential_plan.py` & `unified_planning-0.5.0.93.dev1/unified_planning/plans/sequential_plan.py`

 * *Files 3% similar despite different names*

```diff
@@ -100,15 +100,15 @@
             if replaced_ai is not None:
                 new_ai.append(replaced_ai)
         new_env = self._environment
         if len(new_ai) > 0:
             new_env = new_ai[0].action.env
         return SequentialPlan(new_ai, new_env)
 
-    def to_partial_order_plan(
+    def _to_partial_order_plan(
         self, problem: "up.model.mixins.ObjectsSetMixin"
     ) -> "up.plans.partial_order_plan.PartialOrderPlan":
         """
         Returns the `PartialOrderPlan` version of this `SequentialPlan`.
 
         This is done by keeping the ordering constraints, given by the `SequentialPlan`, between 2 `ActionInstances`
         that satisfy one of these conditions:
@@ -202,7 +202,30 @@
                         graph.add_edge(dependent_action_instance, action_instance)
 
         assert nx.is_directed_acyclic_graph(graph)
         # remove redundant edges and return the up.plans.partial_order_plan.PartialOrderPlan structure.
         return up.plans.partial_order_plan.PartialOrderPlan(
             {}, self._environment, nx.transitive_reduction(graph)
         )
+
+    def convert_to(
+        self,
+        plan_kind: "plans.plan.PlanKind",
+        problem: "up.model.AbstractProblem",
+    ) -> "plans.plan.Plan":
+        """
+        This function takes a `PlanKind` and returns the representation of `self`
+        in the given `plan_kind`. If the conversion does not make sense, raises
+        an exception.
+
+        :param plan_kind: The plan_kind of the returned plan.
+        :param problem: The `Problem` of which this plan is referring to.
+        :return: The plan equivalent to self but represented in the kind of
+            `plan_kind`.
+        """
+        if plan_kind == self._kind:
+            return self
+        elif plan_kind == plans.plan.PlanKind.PARTIAL_ORDER_PLAN:
+            assert isinstance(problem, up.model.mixins.ObjectsSetMixin)
+            return self._to_partial_order_plan(problem)
+        else:
+            raise UPUsageError(f"{type(self)} can't be converted to {plan_kind}.")
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/plans/time_triggered_plan.py` & `unified_planning-0.5.0.93.dev1/unified_planning/plans/time_triggered_plan.py`

 * *Files 18% similar despite different names*

```diff
@@ -123,7 +123,27 @@
             if replaced_ai is not None:
                 new_ai.append((s, replaced_ai, d))
         new_env = self._environment
         if len(new_ai) > 0:
             _, ai, _ = new_ai[0]
             new_env = ai.action.env
         return TimeTriggeredPlan(new_ai, new_env)
+
+    def convert_to(
+        self,
+        plan_kind: "plans.plan.PlanKind",
+        problem: "up.model.AbstractProblem",
+    ) -> "plans.plan.Plan":
+        """
+        This function takes a `PlanKind` and returns the representation of `self`
+        in the given `plan_kind`. If the conversion does not make sense, raises
+        an exception.
+
+        :param plan_kind: The plan_kind of the returned plan.
+        :param problem: The `Problem` of which this plan is referring to.
+        :return: The plan equivalent to self but represented in the kind of
+            `plan_kind`.
+        """
+        if plan_kind == self._kind:
+            return self
+        else:
+            raise UPUsageError(f"{type(self)} can't be converted to {plan_kind}.")
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/shortcuts.py` & `unified_planning-0.5.0.93.dev1/unified_planning/shortcuts.py`

 * *Files 13% similar despite different names*

```diff
@@ -19,15 +19,21 @@
 
 import sys
 import unified_planning as up
 import unified_planning.model.types
 import unified_planning.model.multi_agent
 from unified_planning.environment import get_env
 from unified_planning.model import *
-from unified_planning.engines import Engine, CompilationKind, OptimalityGuarantee
+from unified_planning.engines import (
+    Engine,
+    CompilationKind,
+    OptimalityGuarantee,
+    OperationMode,
+)
+from unified_planning.plans import PlanKind
 from typing import IO, Any, Iterable, List, Union, Dict, Tuple, Optional
 from fractions import Fraction
 
 
 def And(*args: Union[BoolExpression, Iterable[BoolExpression]]) -> FNode:
     """
     Returns a conjunction of terms.
@@ -156,14 +162,69 @@
     :param params: The Iterable of expressions acting as `parameters` for this `Fluent`; mainly the parameters will
         be :class:`Objects <unified_planning.model.Object>` (when the `FluentExp` is grounded) or :func:`Action parameters <unified_planning.model.Action.parameters>` (when the `FluentExp` is lifted).
     :return: The created `Fluent` Expression.
     """
     return get_env().expression_manager.FluentExp(fluent, params)
 
 
+def Always(expression: BoolExpression) -> FNode:
+    """Creates an expression of the form:
+        `Always(a)`
+    Restriction: expression must be of `boolean type` and with only one arg.
+
+    :param expression: The `boolean` expression of the trajectory constraints.
+    :return: The created `Always` expression.
+    """
+    return get_env().expression_manager.Always(expression)
+
+
+def Sometime(expression: BoolExpression) -> FNode:
+    """Creates an expression of the form:
+        `Sometime(a)`
+    Restriction: expression must be of `boolean type` and with only one arg.
+
+    :param expression: The `boolean` expression of the trajectory constraints.
+    :return: The created `Sometime` expression.
+    """
+    return get_env().expression_manager.Sometime(expression)
+
+
+def SometimeBefore(*expression: BoolExpression) -> FNode:
+    """Creates an expression of the form:
+        `Sometime-Before(a, b)`
+    Restriction: expression must be of `boolean type` and with only one args
+
+    :param expression: The `boolean` expression of the trajectory constraints.
+    :return: The created `Sometime` expression.
+    """
+    return get_env().expression_manager.SometimeBefore(*expression)
+
+
+def SometimeAfter(*expression: BoolExpression) -> FNode:
+    """Creates an expression of the form:
+        `Sometime-After(a, b)`
+    Restriction: expression must be of `boolean type` and with only two arg.
+
+    :param expression: The `boolean` expression of the trajectory constraints.
+    :return: The created `Sometime-After(a, b)` expression.
+    """
+    return get_env().expression_manager.SometimeAfter(*expression)
+
+
+def AtMostOnce(expression: BoolExpression) -> FNode:
+    """Creates an expression of the form:
+        `At-Most-Once(a, b)`
+    Restriction: expression must be of `boolean type` and with only two arg.
+
+    :param expression: The `boolean` expression of the trajectory constraints.
+    :return: The created `At-Most-Once(a, b)` expression.
+    """
+    return get_env().expression_manager.AtMostOnce(expression)
+
+
 def ParameterExp(param: "unified_planning.model.Parameter") -> FNode:
     """
     Returns an expression for the given :func:`Action parameter <unified_planning.model.Action.parameters>`.
 
     :param param: The `Parameter` that must be promoted to `FNode`.
     :return: The `FNode` containing the given `param` as his payload.
     """
@@ -569,13 +630,36 @@
         problem=problem,
         name=name,
         params=params,
         optimality_guarantee=optimality_guarantee,
     )
 
 
+def PortfolioSelector(
+    *,
+    name: Optional[str] = None,
+    params: Optional[Dict[str, Any]] = None,
+    problem_kind: ProblemKind = ProblemKind(),
+    optimality_guarantee: Optional[Union["OptimalityGuarantee", str]] = None,
+) -> "up.engines.engine.Engine":
+    """
+    Returns a portfolio selector. There are two ways to call this method:
+    - using 'name' (the name of a specific portfolio) and eventually 'params'
+        (portfolio dependent options).
+        e.g. PortfolioSelector(name='ibacop')
+    - using 'problem_kind' and 'optimality_guarantee'.
+        e.g. OneshotPlanner(problem_kind=problem.kind, optimality_guarantee=SOLVED_OPTIMALLY)
+    """
+    return get_env().factory.PortfolioSelector(
+        name=name,
+        params=params,
+        problem_kind=problem_kind,
+        optimality_guarantee=optimality_guarantee,
+    )
+
+
 def print_engines_info(stream: IO[str] = sys.stdout, full_credits: bool = False):
     get_env().factory.print_engines_info(stream, full_credits)
 
 
 def set_credits_stream(stream: Optional[IO[str]]):
     get_env().credits_stream = stream
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -13,14 +13,15 @@
 # limitations under the License.
 
 
 import unittest
 import unified_planning as up
 from functools import wraps
 from importlib.util import find_spec
+from unified_planning.engines import OperationMode
 from unified_planning.environment import get_env
 from unified_planning.model import ProblemKind
 from unified_planning.test.pddl import enhsp
 from typing import Optional
 
 
 skipIf = unittest.skipIf
@@ -57,15 +58,15 @@
         self.optimality_guarantee = optimality_guarantee
 
     def __call__(self, test_fun):
         msg = "no oneshot planner available for the given problem kind"
         cond = False
         try:
             get_env().factory._get_engine_class(
-                "oneshot_planner",
+                OperationMode.ONESHOT_PLANNER,
                 problem_kind=self.kind,
                 optimality_guarantee=self.optimality_guarantee,
             )
         except:
             cond = True
 
         @unittest.skipIf(cond, msg)
@@ -88,15 +89,15 @@
         self.anytime_guarantee = anytime_guarantee
 
     def __call__(self, test_fun):
         msg = "no anytime planner available for the given problem kind"
         cond = False
         try:
             get_env().factory._get_engine_class(
-                "anytime_planner",
+                OperationMode.ANYTIME_PLANNER,
                 problem_kind=self.kind,
                 anytime_guarantee=self.anytime_guarantee,
             )
         except:
             cond = True
 
         @unittest.skipIf(cond, msg)
@@ -114,15 +115,15 @@
         self.kind = kind
 
     def __call__(self, test_fun):
         msg = "no plan validator available for the given problem kind"
         cond = False
         try:
             get_env().factory._get_engine_class(
-                "plan_validator", problem_kind=self.kind
+                OperationMode.PLAN_VALIDATOR, problem_kind=self.kind
             )
         except:
             cond = True
 
         @unittest.skipIf(cond, msg)
         @wraps(test_fun)
         def wrapper(*args, **kwargs):
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/examples/__init__.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/examples/__init__.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/examples/hierarchical.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/examples/hierarchical.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/examples/minimals.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/examples/minimals.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/examples/multi_agent.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/examples/multi_agent.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/examples/realistic.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/examples/realistic.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/examples/testing_variants.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/examples/testing_variants.py`

 * *Files 24% similar despite different names*

```diff
@@ -581,8 +581,142 @@
                 Fraction(3, 1),
             ),
         ]
     )
     matchcellar_static_duration = Example(problem=problem, plan=t_plan)
     problems["matchcellar_static_duration"] = matchcellar_static_duration
 
+    # locations connected visited oversubscription
+    Location = UserType("Location")
+    is_at = Fluent("is_at", BoolType(), position=Location)
+    is_connected = Fluent(
+        "is_connected", BoolType(), location_1=Location, location_2=Location
+    )
+    visited = Fluent("visited", BoolType(), location=Location)
+    move = InstantaneousAction("move", l_from=Location, l_to=Location)
+    l_from = move.parameter("l_from")
+    l_to = move.parameter("l_to")
+    move.add_precondition(Not(Equals(l_from, l_to)))
+    move.add_precondition(is_at(l_from))
+    move.add_precondition(Not(is_at(l_to)))
+    move.add_precondition(Or(is_connected(l_from, l_to), is_connected(l_to, l_from)))
+    move.add_effect(is_at(l_from), False)
+    move.add_effect(is_at(l_to), True)
+    move.add_effect(visited(l_to), True)
+    l1 = Object("l1", Location)
+    l2 = Object("l2", Location)
+    l3 = Object("l3", Location)
+    l4 = Object("l4", Location)
+    l5 = Object("l5", Location)
+    problem = Problem("locations_connected_visited_oversubscription")
+    problem.add_fluent(is_at, default_initial_value=False)
+    problem.add_fluent(visited, default_initial_value=False)
+    problem.add_fluent(is_connected, default_initial_value=False)
+    problem.add_action(move)
+    problem.add_object(l1)
+    problem.add_object(l2)
+    problem.add_object(l3)
+    problem.add_object(l4)
+    problem.add_object(l5)
+    problem.set_initial_value(is_at(l1), True)
+    problem.set_initial_value(visited(l1), True)
+    problem.set_initial_value(is_connected(l1, l2), True)
+    problem.set_initial_value(is_connected(l1, l3), True)
+    problem.set_initial_value(is_connected(l1, l5), True)
+    problem.set_initial_value(is_connected(l2, l3), True)
+    problem.set_initial_value(is_connected(l2, l5), True)
+    problem.set_initial_value(is_connected(l3, l4), True)
+    problem.set_initial_value(is_connected(l4, l5), True)
+    problem.add_goal(is_at(l5))
+    loc_var = Variable("loc_var", Location)
+    problem.add_quality_metric(
+        Oversubscription(
+            {
+                visited(l2): 9,
+                visited(l2) | visited(l3): 5,
+                Forall(visited(loc_var) | loc_var.Equals(l2), loc_var)
+                & visited(l2).Not(): 10,
+            }
+        )
+    )
+
+    plan = unified_planning.plans.SequentialPlan(
+        [
+            unified_planning.plans.ActionInstance(move, (ObjectExp(l1), ObjectExp(l3))),
+            unified_planning.plans.ActionInstance(move, (ObjectExp(l3), ObjectExp(l4))),
+            unified_planning.plans.ActionInstance(move, (ObjectExp(l4), ObjectExp(l5))),
+        ]
+    )
+    locations_connected_visited_oversubscription = Example(problem=problem, plan=plan)
+    problems[
+        "locations_connected_visited_oversubscription"
+    ] = locations_connected_visited_oversubscription
+
+    # locations connected cost minimize
+    Location = UserType("Location")
+    is_at = Fluent("is_at", BoolType(), position=Location)
+    is_connected = Fluent(
+        "is_connected", BoolType(), location_1=Location, location_2=Location
+    )
+    distance = Fluent("distance", RealType(), location_1=Location, location_2=Location)
+    move = InstantaneousAction("move", l_from=Location, l_to=Location)
+    l_from = move.parameter("l_from")
+    l_to = move.parameter("l_to")
+    move.add_precondition(Not(Equals(l_from, l_to)))
+    move.add_precondition(is_at(l_from))
+    move.add_precondition(Not(is_at(l_to)))
+    move.add_precondition(Or(is_connected(l_from, l_to), is_connected(l_to, l_from)))
+    move.add_effect(is_at(l_from), False)
+    move.add_effect(is_at(l_to), True)
+    move_cost = distance(l_from, l_to)
+    l1 = Object("l1", Location)
+    l2 = Object("l2", Location)
+    l3 = Object("l3", Location)
+    l4 = Object("l4", Location)
+    l5 = Object("l5", Location)
+    problem = Problem("locations_connected_cost_minimize")
+    problem.add_fluent(is_at, default_initial_value=False)
+    problem.add_fluent(is_connected, default_initial_value=False)
+    problem.add_fluent(distance, default_initial_value=100)
+    problem.add_action(move)
+    problem.add_object(l1)
+    problem.add_object(l2)
+    problem.add_object(l3)
+    problem.add_object(l4)
+    problem.add_object(l5)
+    problem.set_initial_value(is_at(l1), True)
+    problem.set_initial_value(is_connected(l1, l2), True)
+    problem.set_initial_value(is_connected(l1, l3), True)
+    problem.set_initial_value(is_connected(l1, l5), True)
+    problem.set_initial_value(is_connected(l2, l3), True)
+    problem.set_initial_value(is_connected(l2, l5), True)
+    problem.set_initial_value(is_connected(l3, l4), True)
+    problem.set_initial_value(is_connected(l4, l5), True)
+    problem.set_initial_value(distance(l1, l2), 4)
+    problem.set_initial_value(distance(l1, l3), 8)
+    problem.set_initial_value(distance(l1, l5), 11)
+    problem.set_initial_value(distance(l2, l3), 5)
+    problem.set_initial_value(distance(l2, l5), 8)
+    problem.set_initial_value(distance(l3, l4), 1)
+    problem.set_initial_value(distance(l4, l5), 1)
+
+    problem.set_initial_value(distance(l2, l1), 4)
+    problem.set_initial_value(distance(l3, l1), 8)
+    problem.set_initial_value(distance(l5, l1), 11)
+    problem.set_initial_value(distance(l3, l2), 5)
+    problem.set_initial_value(distance(l5, l2), 8)
+    problem.set_initial_value(distance(l4, l3), 1)
+    problem.set_initial_value(distance(l5, l4), 1)
+    problem.add_goal(is_at(l5))
+    problem.add_quality_metric(MinimizeActionCosts({move: move_cost}))
+
+    plan = unified_planning.plans.SequentialPlan(
+        [
+            unified_planning.plans.ActionInstance(move, (ObjectExp(l1), ObjectExp(l3))),
+            unified_planning.plans.ActionInstance(move, (ObjectExp(l3), ObjectExp(l4))),
+            unified_planning.plans.ActionInstance(move, (ObjectExp(l4), ObjectExp(l5))),
+        ]
+    )
+    locations_connected_cost_minimize = Example(problem=problem, plan=plan)
+    problems["locations_connected_cost_minimize"] = locations_connected_cost_minimize
+
     return problems
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/citycar/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/citycar/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/citycar/problem.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/citycar/problem.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/counters/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/counters/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/counters/problem2.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/counters/problem2.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/depot/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/depot/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/depot/problem.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/depot/problem.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/enhsp.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/enhsp.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/htn-transport/domain.hddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/htn-transport/domain.hddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/htn-transport/problem.hddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/htn-transport/problem.hddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/matchcellar/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/matchcellar/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/miconic/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/miconic/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/robot_fastener/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/robot_fastener/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/safe_road/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/safe_road/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/sailing/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/sailing/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/pddl/visit_precedence/domain.pddl` & `unified_planning-0.5.0.93.dev1/unified_planning/test/pddl/visit_precedence/domain.pddl`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_anml_writer.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_anml_writer.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_anytime.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_anytime.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_compilers_pipeline.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_compilers_pipeline.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_conditional_effects_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_conditional_effects_remover.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_contingent_pddl.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_contingent_pddl.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_credits.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_credits.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_disjunctive_conditions_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_disjunctive_conditions_remover.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_dnf.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_dnf.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_factory.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_factory.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_grounder.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_grounder.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_infix_notation.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_infix_notation.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_model.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_model.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_multi_agent.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_multi_agent.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_negative_conditions_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_negative_conditions_remover.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_partial_order_plan.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_partial_order_plan.py`

 * *Files 10% similar despite different names*

```diff
@@ -33,15 +33,15 @@
     @skipIfEngineNotAvailable("sequential_plan_validator")
     def test_all(self):
         with PlanValidator(name="sequential_plan_validator") as validator:
             assert validator is not None
             for problem, plan in self.problems.values():
                 if validator.supports(problem.kind):
                     self.assertTrue(isinstance(plan, up.plans.SequentialPlan))
-                    pop_plan = plan.to_partial_order_plan(problem)
+                    pop_plan = plan.convert_to(PlanKind.PARTIAL_ORDER_PLAN, problem)
                     for sorted_plan in pop_plan.all_sequential_plans():
                         validation_result = validator.validate(problem, sorted_plan)
                         self.assertEqual(
                             up.engines.ValidationResultStatus.VALID,
                             validation_result.status,
                         )
 
@@ -57,15 +57,17 @@
         ) as compiler:
             comp_res = compiler.compile(problem)
         with OneshotPlanner(problem_kind=comp_res.problem.kind) as solver:
             self.assertIsNotNone(solver)
             comp_plan = solver.solve(comp_res.problem).plan
             self.assertIsNotNone(comp_plan)
             assert isinstance(comp_plan, up.plans.SequentialPlan)
-            pop_comp_plan = comp_plan.to_partial_order_plan(comp_res.problem)
+            pop_comp_plan = comp_plan.convert_to(
+                PlanKind.PARTIAL_ORDER_PLAN, comp_res.problem
+            )
             pop_plan = pop_comp_plan.replace_action_instances(
                 comp_res.map_back_action_instance
             )
             assert isinstance(pop_plan, up.plans.PartialOrderPlan)
         with PlanValidator(problem_kind=problem.kind) as validator:
             for plan in pop_plan.all_sequential_plans():
                 validation_result = validator.validate(problem, plan)
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_pddl_io.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_pddl_io.py`

 * *Files 1% similar despite different names*

```diff
@@ -448,14 +448,15 @@
             problem_filename = os.path.join(domain, "instance.1.pb.hddl")
             reader = PDDLReader()
             problem = reader.parse_problem(domain_filename, problem_filename)
 
             assert isinstance(problem, up.model.htn.HierarchicalProblem)
 
     def test_examples_io(self):
+
         for example in self.problems.values():
             problem = example.problem
             kind = problem.kind
             if (
                 kind.has_intermediate_conditions_and_effects()
                 or kind.has_object_fluents()
                 or kind.has_oversubscription()
@@ -468,15 +469,22 @@
                 w = PDDLWriter(problem)
                 w.write_domain(domain_filename)
                 w.write_problem(problem_filename)
 
                 reader = PDDLReader()
                 parsed_problem = reader.parse_problem(domain_filename, problem_filename)
 
-                self.assertEqual(len(problem.fluents), len(parsed_problem.fluents))
+                # Case where the reader does not convert the final_value back to actions_cost.
+                if kind.has_actions_cost() and parsed_problem.kind.has_final_value():
+                    self.assertEqual(
+                        len(problem.fluents) + 1, len(parsed_problem.fluents)
+                    )
+                else:
+                    self.assertEqual(len(problem.fluents), len(parsed_problem.fluents))
+
                 self.assertTrue(
                     _have_same_user_types_considering_renamings(
                         problem, parsed_problem, w.get_item_named
                     )
                 )
                 self.assertEqual(len(problem.actions), len(parsed_problem.actions))
                 for a in problem.actions:
@@ -485,15 +493,21 @@
                     for param, parsed_param in zip(a.parameters, parsed_a.parameters):
                         self.assertEqual(
                             param.type,
                             w.get_item_named(cast(_UserType, parsed_param.type).name),
                         )
                     if isinstance(a, InstantaneousAction):
                         assert isinstance(parsed_a, InstantaneousAction)
-                        self.assertEqual(len(a.effects), len(parsed_a.effects))
+                        if (
+                            kind.has_actions_cost()
+                            and parsed_problem.kind.has_final_value()
+                        ):
+                            self.assertEqual(len(a.effects) + 1, len(parsed_a.effects))
+                        else:
+                            self.assertEqual(len(a.effects), len(parsed_a.effects))
                     elif isinstance(a, DurativeAction):
                         assert isinstance(parsed_a, DurativeAction)
                         self.assertEqual(str(a.duration), str(parsed_a.duration))
                         for t, e in a.effects.items():
                             self.assertEqual(len(e), len(parsed_a.effects[t]))
 
     def test_basic_with_object_constant(self):
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_pddl_planner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_pddl_planner.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_plan_validator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_plan_validator.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_planner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_planner.py`

 * *Files 1% similar despite different names*

```diff
@@ -88,14 +88,32 @@
             self.assertEqual(
                 final_report.status, PlanGenerationResultStatus.SOLVED_SATISFICING
             )
             self.assertEqual(len(plan.actions), 1)
             self.assertEqual(plan.actions[0].action, a)
             self.assertEqual(len(plan.actions[0].actual_parameters), 0)
 
+    @skipIfEngineNotAvailable("tamer")
+    def test_basic_with_custom_heuristic(self):
+        problem = self.problems["basic"].problem
+        x = problem.fluent("x")
+
+        with OneshotPlanner(name="tamer") as planner:
+            self.assertNotEqual(planner, None)
+
+            def h(state):
+                v = state.get_value(x()).bool_constant_value()
+                return 0 if v else 1
+
+            final_report = planner.solve(problem, heuristic=h)
+            plan = final_report.plan
+            self.assertEqual(
+                final_report.status, PlanGenerationResultStatus.SOLVED_SATISFICING
+            )
+
     @skipIfNoOneshotPlannerForProblemKind(
         basic_classical_kind.union(oversubscription_kind)
     )
     def test_basic_oversubscription(self):
         problem = self.problems["basic_oversubscription"].problem
         a = problem.action("a")
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_problem.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_problem.py`

 * *Files 1% similar despite different names*

```diff
@@ -543,14 +543,15 @@
             "counter_to_50",
             "robot_decrease",
             "robot_locations_connected",
             "robot_locations_visited",
             "robot_with_durative_action",
             "robot_fluent_of_user_type_with_int_id",
             "matchcellar_static_duration",
+            "locations_connected_cost_minimize",
         ]
         for problem, _ in self.problems.values():
             if problem.name in names_of_SNP_problems:
                 self.assertTrue(problem.kind.has_simple_numeric_planning())
             else:
                 self.assertFalse(problem.kind.has_simple_numeric_planning())
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_protobuf_io.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_protobuf_io.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_pyperplan.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_pyperplan.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_python_writer.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_python_writer.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_quantifier_remover.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_quantifier_remover.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_replanner.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_replanner.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_sequential_simulator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_sequential_simulator.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_simplifier.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_simplifier.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_simulated_effects.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_simulated_effects.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_substituter.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_substituter.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_tarski_converter.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_tarski_converter.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_tarski_grounder.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_tarski_grounder.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_temporal.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_temporal.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/test/test_validator.py` & `unified_planning-0.5.0.93.dev1/unified_planning/test/test_validator.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning/utils.py` & `unified_planning-0.5.0.93.dev1/unified_planning/utils.py`

 * *Files identical despite different names*

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning.egg-info/PKG-INFO` & `unified_planning-0.5.0.93.dev1/unified_planning.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: unified-planning
-Version: 0.5.0.7.dev1
+Version: 0.5.0.93.dev1
 Summary: Unified Planning Framework
 Home-page: https://www.aiplan4eu-project.eu
 Author: AIPlan4EU Project
 Author-email: aiplan4eu@fbk.eu
 License: APACHE
 Description: UNKNOWN
 Keywords: planning logic STRIPS RDDL
```

### Comparing `unified_planning-0.5.0.7.dev1/unified_planning.egg-info/SOURCES.txt` & `unified_planning-0.5.0.93.dev1/unified_planning.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -28,20 +28,22 @@
 unified_planning/engines/compilers/compilers_pipeline.py
 unified_planning/engines/compilers/conditional_effects_remover.py
 unified_planning/engines/compilers/disjunctive_conditions_remover.py
 unified_planning/engines/compilers/grounder.py
 unified_planning/engines/compilers/negative_conditions_remover.py
 unified_planning/engines/compilers/quantifiers_remover.py
 unified_planning/engines/compilers/tarski_grounder.py
+unified_planning/engines/compilers/trajectory_constraints_remover.py
 unified_planning/engines/compilers/utils.py
 unified_planning/engines/mixins/__init__.py
 unified_planning/engines/mixins/anytime_planner.py
 unified_planning/engines/mixins/compiler.py
 unified_planning/engines/mixins/oneshot_planner.py
 unified_planning/engines/mixins/plan_validator.py
+unified_planning/engines/mixins/portfolio.py
 unified_planning/engines/mixins/replanner.py
 unified_planning/engines/mixins/simulator.py
 unified_planning/grpc/__init__.py
 unified_planning/grpc/converter.py
 unified_planning/grpc/proto_reader.py
 unified_planning/grpc/proto_writer.py
 unified_planning/grpc/generated/__init__.py
@@ -108,14 +110,15 @@
 unified_planning/plans/plan.py
 unified_planning/plans/sequential_plan.py
 unified_planning/plans/time_triggered_plan.py
 unified_planning/test/__init__.py
 unified_planning/test/test_anml_writer.py
 unified_planning/test/test_anytime.py
 unified_planning/test/test_compilers_pipeline.py
+unified_planning/test/test_compilers_quality_metrics.py
 unified_planning/test/test_conditional_effects_remover.py
 unified_planning/test/test_contingent_pddl.py
 unified_planning/test/test_credits.py
 unified_planning/test/test_disjunctive_conditions_remover.py
 unified_planning/test/test_dnf.py
 unified_planning/test/test_factory.py
 unified_planning/test/test_grounder.py
@@ -137,14 +140,16 @@
 unified_planning/test/test_sequential_simulator.py
 unified_planning/test/test_simplifier.py
 unified_planning/test/test_simulated_effects.py
 unified_planning/test/test_substituter.py
 unified_planning/test/test_tarski_converter.py
 unified_planning/test/test_tarski_grounder.py
 unified_planning/test/test_temporal.py
+unified_planning/test/test_trajectory_constraint.py
+unified_planning/test/test_trajectory_constraints_remover.py
 unified_planning/test/test_validator.py
 unified_planning/test/examples/__init__.py
 unified_planning/test/examples/hierarchical.py
 unified_planning/test/examples/minimals.py
 unified_planning/test/examples/multi_agent.py
 unified_planning/test/examples/realistic.py
 unified_planning/test/examples/testing_variants.py
```

