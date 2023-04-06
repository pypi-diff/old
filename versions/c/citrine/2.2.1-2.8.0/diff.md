# Comparing `tmp/citrine-2.2.1.tar.gz` & `tmp/citrine-2.8.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/citrine-2.2.1.tar", last modified: Thu Mar  2 20:29:14 2023, max compression
+gzip compressed data, was "dist/citrine-2.8.0.tar", last modified: Thu Mar 16 19:22:06 2023, max compression
```

## Comparing `citrine-2.2.1.tar` & `citrine-2.8.0.tar`

### file list

```diff
@@ -1,168 +1,171 @@
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/
--rw-rw-r--   0 travis    (2000) travis    (2000)    11349 2023-03-02 20:27:18.000000 citrine-2.2.1/LICENSE
--rw-rw-r--   0 travis    (2000) travis    (2000)     1097 2023-03-02 20:29:14.000000 citrine-2.2.1/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)      544 2023-03-02 20:27:18.000000 citrine-2.2.1/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)       38 2023-03-02 20:29:14.000000 citrine-2.2.1/setup.cfg
--rw-rw-r--   0 travis    (2000) travis    (2000)     1773 2023-03-02 20:27:18.000000 citrine-2.2.1/setup.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/
--rw-rw-r--   0 travis    (2000) travis    (2000)      343 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)       22 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/__version__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/_rest/
--rw-rw-r--   0 travis    (2000) travis    (2000)       58 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2222 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/ai_resource_metadata.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1316 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/asynchronous_object.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5408 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/collection.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3499 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/engine_resource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4185 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/pageable.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5112 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/paginator.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1992 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_rest/resource.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/_serialization/
--rw-rw-r--   0 travis    (2000) travis    (2000)       31 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_serialization/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      963 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_serialization/include_parent_properties.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      643 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_serialization/polymorphic_serializable.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34446 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_serialization/properties.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      912 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_serialization/serializable.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13685 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_session.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/_utils/
--rw-rw-r--   0 travis    (2000) travis    (2000)       31 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_utils/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5085 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_utils/batcher.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7598 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_utils/functions.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2930 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/_utils/template_util.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/builders/
--rw-rw-r--   0 travis    (2000) travis    (2000)       55 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/builders/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    30465 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/builders/auto_configure.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9238 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/builders/descriptors.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13111 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/builders/design_spaces.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10073 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/builders/predictors.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2891 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/builders/scores.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2109 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/citrine.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4263 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/exceptions.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/gemtables/
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/gemtables/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16098 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/gemtables/columns.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2522 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/gemtables/rows.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    51689 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/gemtables/variables.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/informatics/
--rw-rw-r--   0 travis    (2000) travis    (2000)       64 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/informatics/constraints/
--rw-rw-r--   0 travis    (2000) travis    (2000)      248 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/constraints/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1245 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/constraints/categorical_constraint.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1308 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/constraints/constraint.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1717 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/constraints/ingredient_count_constraint.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2109 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/constraints/ingredient_fraction_constraint.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2022 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/constraints/label_fraction_constraint.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2099 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/constraints/scalar_range_constraint.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5622 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/data_sources.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7861 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/descriptors.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5189 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/design_candidate.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine/informatics/design_spaces/
--rw-rw-r--   0 travis    (2000) travis    (2000)      198 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/design_spaces/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1526 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/design_spaces/data_source_design_space.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1402 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/design_spaces/design_space.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2124 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/design_spaces/enumerated_design_space.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3321 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/design_spaces/formulation_design_space.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3502 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/design_spaces/product_design_space.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2775 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/dimensions.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/src/citrine/informatics/executions/
--rw-rw-r--   0 travis    (2000) travis    (2000)      136 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/executions/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5324 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/executions/design_execution.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4495 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/executions/generative_design_execution.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3848 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/executions/predictor_evaluation_execution.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4472 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/experiment_values.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3458 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/generative_design.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1218 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/modules.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1901 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/objectives.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1147 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predict_request.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6619 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictor_evaluation_metrics.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10281 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictor_evaluation_result.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7653 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictor_evaluator.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/src/citrine/informatics/predictors/
--rw-rw-r--   0 travis    (2000) travis    (2000)      447 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4096 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/auto_ml_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7520 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/chemical_formula_featurizer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2078 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/expression_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3168 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/graph_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1688 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/ingredient_fractions_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2333 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/ingredients_to_formulation_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1586 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/label_fractions_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5458 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/mean_property_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7593 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/molecular_structure_featurizer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3832 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2670 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/predictors/simple_mixture_predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10291 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/reports.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4835 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/scores.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/src/citrine/informatics/workflows/
--rw-rw-r--   0 travis    (2000) travis    (2000)      115 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/workflows/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2694 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/workflows/design_workflow.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2183 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/workflows/predictor_evaluation_workflow.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1181 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/informatics/workflows/workflow.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/src/citrine/jobs/
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/jobs/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5105 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/jobs/job.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5458 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/jobs/waiting.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/src/citrine/resources/
--rw-rw-r--   0 travis    (2000) travis    (2000)      140 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1676 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/api_error.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      617 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/attribute_templates.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1781 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/audit_info.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10482 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/branch.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3215 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/condition_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    35612 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/data_concepts.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6530 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/data_objects.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2135 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/data_version_update.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    20037 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/dataset.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4405 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/delete.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2487 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/descriptors.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4022 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/design_execution.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5981 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/design_space.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6795 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/design_workflow.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6887 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/experiment_datasource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34992 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/file_link.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9098 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/gemd_resource.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14898 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/gemtables.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3198 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/generative_design_execution.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7882 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/ingredient_run.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7209 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/ingredient_spec.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      227 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/job.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8812 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/material_run.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5874 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/material_spec.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4570 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/material_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6682 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/measurement_run.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5113 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/measurement_spec.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6634 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/measurement_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2471 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/module.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      553 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/object_runs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      563 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/object_specs.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      592 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/object_templates.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3197 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/parameter_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18640 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/predictor.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6100 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/predictor_evaluation_execution.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4185 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/predictor_evaluation_workflow.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5570 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/process_run.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5473 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/process_spec.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5820 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/process_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24305 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/project.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      725 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/project_member.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      146 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/project_roles.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3095 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/property_template.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1478 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/report.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      873 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/response.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      948 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/status_detail.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    25639 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/table_config.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14278 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/team.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      702 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/templates.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2847 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/resources/user.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/src/citrine/seeding/
--rw-rw-r--   0 travis    (2000) travis    (2000)       50 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/seeding/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6541 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/seeding/find_or_create.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      903 2023-03-02 20:27:18.000000 citrine-2.2.1/src/citrine/seeding/sort_gems.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine.egg-info/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1097 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine.egg-info/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)     6119 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine.egg-info/SOURCES.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine.egg-info/dependency_links.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      313 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine.egg-info/requires.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)        8 2023-03-02 20:29:13.000000 citrine-2.2.1/src/citrine.egg-info/top_level.txt
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-02 20:29:14.000000 citrine-2.2.1/tests/
--rw-rw-r--   0 travis    (2000) travis    (2000)     3620 2023-03-02 20:27:18.000000 citrine-2.2.1/tests/test_citrine.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11073 2023-03-02 20:27:18.000000 citrine-2.2.1/tests/test_session.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11349 2023-03-16 19:20:10.000000 citrine-2.8.0/LICENSE
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1097 2023-03-16 19:22:06.000000 citrine-2.8.0/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)      544 2023-03-16 19:20:10.000000 citrine-2.8.0/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)       38 2023-03-16 19:22:06.000000 citrine-2.8.0/setup.cfg
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1773 2023-03-16 19:20:10.000000 citrine-2.8.0/setup.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      343 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       22 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/__version__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/_rest/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       58 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2222 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/ai_resource_metadata.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1316 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/asynchronous_object.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5408 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/collection.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3499 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/engine_resource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4185 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/pageable.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5112 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/paginator.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1992 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_rest/resource.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/_serialization/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       31 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_serialization/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      963 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_serialization/include_parent_properties.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      643 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_serialization/polymorphic_serializable.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34446 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_serialization/properties.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      912 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_serialization/serializable.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13685 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_session.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/_utils/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       31 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_utils/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5085 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_utils/batcher.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7598 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_utils/functions.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2930 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/_utils/template_util.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/builders/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       55 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/builders/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    30465 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/builders/auto_configure.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9238 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/builders/descriptors.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13111 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/builders/design_spaces.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10073 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/builders/predictors.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2891 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/builders/scores.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2109 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/citrine.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4263 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/exceptions.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/gemtables/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/gemtables/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16098 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/gemtables/columns.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2522 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/gemtables/rows.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    51689 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/gemtables/variables.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/informatics/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       64 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/informatics/constraints/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      291 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1245 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/categorical_constraint.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1441 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/constraint.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1717 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/ingredient_count_constraint.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2109 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/ingredient_fraction_constraint.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4286 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/ingredient_ratio_constraint.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2022 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/label_fraction_constraint.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2099 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/constraints/scalar_range_constraint.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5387 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/data_sources.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8969 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/descriptors.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5189 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/design_candidate.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/informatics/design_spaces/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      198 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/design_spaces/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1526 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/design_spaces/data_source_design_space.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1402 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/design_spaces/design_space.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2124 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/design_spaces/enumerated_design_space.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3321 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/design_spaces/formulation_design_space.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3502 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/design_spaces/product_design_space.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2775 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/dimensions.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/informatics/executions/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      136 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/executions/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5324 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/executions/design_execution.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4495 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/executions/generative_design_execution.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3848 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/executions/predictor_evaluation_execution.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4472 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/experiment_values.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3458 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/generative_design.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1218 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/modules.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1901 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/objectives.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1147 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predict_request.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6619 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictor_evaluation_metrics.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10281 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictor_evaluation_result.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7653 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictor_evaluator.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/informatics/predictors/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      447 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4096 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/auto_ml_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7520 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/chemical_formula_featurizer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2078 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/expression_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3168 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/graph_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1688 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/ingredient_fractions_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2333 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/ingredients_to_formulation_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1586 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/label_fractions_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5458 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/mean_property_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7593 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/molecular_structure_featurizer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4837 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2670 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/simple_mixture_predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1028 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/single_predict_request.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      820 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/predictors/single_prediction.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10291 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/reports.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4835 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/scores.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/informatics/workflows/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      115 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/workflows/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2694 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/workflows/design_workflow.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2183 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/workflows/predictor_evaluation_workflow.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1181 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/informatics/workflows/workflow.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/jobs/
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/jobs/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5105 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/jobs/job.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5458 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/jobs/waiting.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/resources/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      140 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1676 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/api_error.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      617 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/attribute_templates.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1781 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/audit_info.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10482 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/branch.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3215 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/condition_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35612 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/data_concepts.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6530 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/data_objects.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2135 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/data_version_update.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20037 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/dataset.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4405 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/delete.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2487 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/descriptors.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4022 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/design_execution.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5981 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/design_space.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6795 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/design_workflow.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6887 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/experiment_datasource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33712 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/file_link.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9098 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/gemd_resource.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14898 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/gemtables.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3198 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/generative_design_execution.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7882 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/ingredient_run.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7209 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/ingredient_spec.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      227 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/job.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8812 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/material_run.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5874 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/material_spec.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4570 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/material_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6682 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/measurement_run.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5113 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/measurement_spec.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6634 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/measurement_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2471 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/module.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      553 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/object_runs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      563 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/object_specs.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      592 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/object_templates.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3197 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/parameter_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18640 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/predictor.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6100 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/predictor_evaluation_execution.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4185 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/predictor_evaluation_workflow.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5570 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/process_run.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5473 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/process_spec.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5820 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/process_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24305 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/project.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      725 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/project_member.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      146 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/project_roles.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3095 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/property_template.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1478 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/report.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      873 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/response.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      948 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/status_detail.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    25639 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/table_config.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14278 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/team.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      702 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/templates.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2847 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/resources/user.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine/seeding/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       50 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/seeding/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6541 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/seeding/find_or_create.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      903 2023-03-16 19:20:10.000000 citrine-2.8.0/src/citrine/seeding/sort_gems.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1097 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6303 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      313 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        8 2023-03-16 19:22:06.000000 citrine-2.8.0/src/citrine.egg-info/top_level.txt
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-16 19:22:06.000000 citrine-2.8.0/tests/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3620 2023-03-16 19:20:10.000000 citrine-2.8.0/tests/test_citrine.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11073 2023-03-16 19:20:10.000000 citrine-2.8.0/tests/test_session.py
```

### Comparing `citrine-2.2.1/LICENSE` & `citrine-2.8.0/LICENSE`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/PKG-INFO` & `citrine-2.8.0/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: citrine
-Version: 2.2.1
+Version: 2.8.0
 Summary: Python library for the Citrine Platform
 Home-page: http://github.com/CitrineInformatics/citrine-python
 Author: Citrine Informatics
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `citrine-2.2.1/README.md` & `citrine-2.8.0/README.md`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/setup.py` & `citrine-2.8.0/setup.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_rest/ai_resource_metadata.py` & `citrine-2.8.0/src/citrine/_rest/ai_resource_metadata.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_rest/asynchronous_object.py` & `citrine-2.8.0/src/citrine/_rest/asynchronous_object.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_rest/collection.py` & `citrine-2.8.0/src/citrine/_rest/collection.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_rest/engine_resource.py` & `citrine-2.8.0/src/citrine/_rest/engine_resource.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_rest/pageable.py` & `citrine-2.8.0/src/citrine/_rest/pageable.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_rest/paginator.py` & `citrine-2.8.0/src/citrine/_rest/paginator.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_rest/resource.py` & `citrine-2.8.0/src/citrine/_rest/resource.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_serialization/include_parent_properties.py` & `citrine-2.8.0/src/citrine/_serialization/include_parent_properties.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_serialization/polymorphic_serializable.py` & `citrine-2.8.0/src/citrine/_serialization/polymorphic_serializable.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_serialization/properties.py` & `citrine-2.8.0/src/citrine/_serialization/properties.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_serialization/serializable.py` & `citrine-2.8.0/src/citrine/_serialization/serializable.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_session.py` & `citrine-2.8.0/src/citrine/_session.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_utils/batcher.py` & `citrine-2.8.0/src/citrine/_utils/batcher.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_utils/functions.py` & `citrine-2.8.0/src/citrine/_utils/functions.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/_utils/template_util.py` & `citrine-2.8.0/src/citrine/_utils/template_util.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/builders/auto_configure.py` & `citrine-2.8.0/src/citrine/builders/auto_configure.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/builders/descriptors.py` & `citrine-2.8.0/src/citrine/builders/descriptors.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/builders/design_spaces.py` & `citrine-2.8.0/src/citrine/builders/design_spaces.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/builders/predictors.py` & `citrine-2.8.0/src/citrine/builders/predictors.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/builders/scores.py` & `citrine-2.8.0/src/citrine/builders/scores.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/citrine.py` & `citrine-2.8.0/src/citrine/citrine.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/exceptions.py` & `citrine-2.8.0/src/citrine/exceptions.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/gemtables/columns.py` & `citrine-2.8.0/src/citrine/gemtables/columns.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/gemtables/rows.py` & `citrine-2.8.0/src/citrine/gemtables/rows.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/gemtables/variables.py` & `citrine-2.8.0/src/citrine/gemtables/variables.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/constraints/categorical_constraint.py` & `citrine-2.8.0/src/citrine/informatics/constraints/categorical_constraint.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/constraints/constraint.py` & `citrine-2.8.0/src/citrine/informatics/constraints/constraint.py`

 * *Files 2% similar despite different names*

```diff
@@ -18,15 +18,17 @@
     def get_type(cls, data):
         """Return the subtype."""
         from .ingredient_count_constraint import IngredientCountConstraint
         from .ingredient_fraction_constraint import IngredientFractionConstraint
         from .label_fraction_constraint import LabelFractionConstraint
         from .scalar_range_constraint import ScalarRangeConstraint
         from .categorical_constraint import AcceptableCategoriesConstraint
+        from .ingredient_ratio_constraint import IngredientRatioConstraint
         return {
             'Categorical': AcceptableCategoriesConstraint,  # Kept for backwards compatibility.
             'AcceptableCategoriesConstraint': AcceptableCategoriesConstraint,
             'IngredientCountConstraint': IngredientCountConstraint,
             'IngredientFractionConstraint': IngredientFractionConstraint,
             'LabelFractionConstraint': LabelFractionConstraint,
             'ScalarRange': ScalarRangeConstraint,
+            'IngredientRatio': IngredientRatioConstraint,
         }[data['type']]
```

### Comparing `citrine-2.2.1/src/citrine/informatics/constraints/ingredient_count_constraint.py` & `citrine-2.8.0/src/citrine/informatics/constraints/ingredient_count_constraint.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/constraints/ingredient_fraction_constraint.py` & `citrine-2.8.0/src/citrine/informatics/constraints/ingredient_fraction_constraint.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/constraints/label_fraction_constraint.py` & `citrine-2.8.0/src/citrine/informatics/constraints/label_fraction_constraint.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/constraints/scalar_range_constraint.py` & `citrine-2.8.0/src/citrine/informatics/constraints/scalar_range_constraint.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/data_sources.py` & `citrine-2.8.0/src/citrine/informatics/data_sources.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 """Tools for working with Descriptors."""
+import warnings
 from abc import abstractmethod
 from typing import Type, List, Mapping, Optional, Union
 from uuid import UUID
 
 from citrine._serialization import properties
 from citrine._serialization.polymorphic_serializable import PolymorphicSerializable
 from citrine._serialization.serializable import Serializable
@@ -91,42 +92,40 @@
     Parameters
     ----------
     table_id: UUID
         Unique identifier for the GEM Table
     table_version: Union[str,int]
         Version number for the GEM Table. The first GEM table built from a configuration
         has version = 1. Strings are cast to ints.
-    formulation_descriptor: Optional[FormulationDescriptor]
-        Optional descriptor used to store formulations emitted by the data source.
-        If the data source emits a formulation but this argument is not provided, then a
-        default formulation descriptor will be generated. The formulations descriptor, and
-        other descriptors, can be retrieved using
-        :func:`~citrine.resources.descriptors.DescriptorMethods.descriptors_from_data_source`.
 
     """
 
     typ = properties.String('type', default='hosted_table_data_source', deserializable=False)
     table_id = properties.UUID("table_id")
     table_version = properties.Integer("table_version")
-    formulation_descriptor = properties.Optional(
-        properties.Object(FormulationDescriptor),
-        "formulation_descriptor"
-    )
 
     def _attrs(self) -> List[str]:
         return ["table_id", "table_version", "typ"]
 
     def __init__(self,
                  *,
                  table_id: UUID,
                  table_version: Union[int, str],
                  formulation_descriptor: Optional[FormulationDescriptor] = None):
         self.table_id: UUID = table_id
         self.table_version: Union[int, str] = table_version
-        self.formulation_descriptor: Optional[FormulationDescriptor] = formulation_descriptor
+
+        if formulation_descriptor is not None:
+            warnings.warn(
+                "The field `formulation_descriptor` on a GemTableDataSource is deprecated "
+                "and will be ignored. The Citrine Platform will automatically generate a "
+                "FormulationDescriptor with key 'Formulation' for tables containing formulations.",
+                DeprecationWarning
+            )
+        self.formulation_descriptor = None
 
 
 class ExperimentDataSourceRef(Serializable['ExperimentDataSourceRef'], DataSource):
     """A reference to a data source based on an experiment result hosted on the data platform.
 
     Parameters
     ----------
```

### Comparing `citrine-2.2.1/src/citrine/informatics/descriptors.py` & `citrine-2.8.0/src/citrine/informatics/descriptors.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,21 +1,36 @@
 """Tools for working with Descriptors."""
-from typing import Type, Set
+from typing import Type, Set, Union
+
+from gemd.enumeration.base_enumeration import BaseEnumeration
 
 from citrine._serialization.serializable import Serializable
 from citrine._serialization.polymorphic_serializable import PolymorphicSerializable
 from citrine._serialization import properties
 
 __all__ = ['Descriptor',
            'RealDescriptor',
            'IntegerDescriptor',
            'ChemicalFormulaDescriptor',
            'MolecularStructureDescriptor',
            'CategoricalDescriptor',
-           'FormulationDescriptor']
+           'FormulationDescriptor',
+           'FormulationKey']
+
+
+class FormulationKey(BaseEnumeration):
+    """The allowed names for a FormulationDescriptor.
+
+    * ``HIERARCHICAL`` is the key "Formulation"
+    * ``FLAT`` is the key "Flat Formulation"
+
+    """
+
+    HIERARCHICAL = "Formulation"
+    FLAT = "Flat Formulation"
 
 
 class Descriptor(PolymorphicSerializable['Descriptor']):
     """A Descriptor describes the range of values that a quantity can take on.
 
     Abstract type that returns the proper type given a serialized dict.
     """
@@ -231,24 +246,40 @@
 
 class FormulationDescriptor(Serializable['FormulationDescriptor'], Descriptor):
     """A descriptor to hold formulations.
 
     Parameters
     ----------
     key: str
-        the key corresponding to a descriptor
+        The key for the descriptor, which must be either 'Formulation' or 'Flat Formulation'
+        to produce valid Citrine Platform assets.
+        The two allowed values can be accessed from the `FormulationKey` enum.
 
     """
 
-    typ = properties.String('type', default='Formulation', deserializable=False)
+    typ = properties.String(
+        'type', default=FormulationKey.HIERARCHICAL.value, deserializable=False
+    )
+
+    def __init__(self, key: Union[FormulationKey, str]):
+        if not isinstance(key, FormulationKey):
+            key = FormulationKey.get_enum(key)
+        self.key: str = key.value
 
     def __eq__(self, other):
         return self._equals(other, ["key", "typ"])
 
-    def __init__(self, key: str):
-        self.key: str = key
-
     def __str__(self):
         return "<FormulationDescriptor {!r}>".format(self.key)
 
     def __repr__(self):
         return "FormulationDescriptor(key={})".format(self.key)
+
+    @classmethod
+    def hierarchical(cls) -> "FormulationDescriptor":
+        """The hierarchical formulation descriptor with key 'Formulation'."""
+        return FormulationDescriptor(FormulationKey.HIERARCHICAL)
+
+    @classmethod
+    def flat(cls) -> "FormulationDescriptor":
+        """The flat formulation descriptor with key 'Flat Formulation'."""
+        return FormulationDescriptor(FormulationKey.FLAT)
```

### Comparing `citrine-2.2.1/src/citrine/informatics/design_candidate.py` & `citrine-2.8.0/src/citrine/informatics/design_candidate.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/design_spaces/data_source_design_space.py` & `citrine-2.8.0/src/citrine/informatics/design_spaces/data_source_design_space.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/design_spaces/design_space.py` & `citrine-2.8.0/src/citrine/informatics/design_spaces/design_space.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/design_spaces/enumerated_design_space.py` & `citrine-2.8.0/src/citrine/informatics/design_spaces/enumerated_design_space.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/design_spaces/formulation_design_space.py` & `citrine-2.8.0/src/citrine/informatics/design_spaces/formulation_design_space.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/design_spaces/product_design_space.py` & `citrine-2.8.0/src/citrine/informatics/design_spaces/product_design_space.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/dimensions.py` & `citrine-2.8.0/src/citrine/informatics/dimensions.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/executions/design_execution.py` & `citrine-2.8.0/src/citrine/informatics/executions/design_execution.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/executions/generative_design_execution.py` & `citrine-2.8.0/src/citrine/informatics/executions/generative_design_execution.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/executions/predictor_evaluation_execution.py` & `citrine-2.8.0/src/citrine/informatics/executions/predictor_evaluation_execution.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/experiment_values.py` & `citrine-2.8.0/src/citrine/informatics/experiment_values.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/generative_design.py` & `citrine-2.8.0/src/citrine/informatics/generative_design.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/modules.py` & `citrine-2.8.0/src/citrine/informatics/modules.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/objectives.py` & `citrine-2.8.0/src/citrine/informatics/objectives.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predict_request.py` & `citrine-2.8.0/src/citrine/informatics/predict_request.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictor_evaluation_metrics.py` & `citrine-2.8.0/src/citrine/informatics/predictor_evaluation_metrics.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictor_evaluation_result.py` & `citrine-2.8.0/src/citrine/informatics/predictor_evaluation_result.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictor_evaluator.py` & `citrine-2.8.0/src/citrine/informatics/predictor_evaluator.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/auto_ml_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/auto_ml_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/chemical_formula_featurizer.py` & `citrine-2.8.0/src/citrine/informatics/predictors/chemical_formula_featurizer.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/expression_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/expression_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/graph_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/graph_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/ingredient_fractions_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/ingredient_fractions_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/ingredients_to_formulation_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/ingredients_to_formulation_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/label_fractions_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/label_fractions_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/mean_property_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/mean_property_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/molecular_structure_featurizer.py` & `citrine-2.8.0/src/citrine/informatics/predictors/molecular_structure_featurizer.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/predictors/simple_mixture_predictor.py` & `citrine-2.8.0/src/citrine/informatics/predictors/simple_mixture_predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/reports.py` & `citrine-2.8.0/src/citrine/informatics/reports.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/scores.py` & `citrine-2.8.0/src/citrine/informatics/scores.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/workflows/design_workflow.py` & `citrine-2.8.0/src/citrine/informatics/workflows/design_workflow.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/workflows/predictor_evaluation_workflow.py` & `citrine-2.8.0/src/citrine/informatics/workflows/predictor_evaluation_workflow.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/informatics/workflows/workflow.py` & `citrine-2.8.0/src/citrine/informatics/workflows/workflow.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/jobs/job.py` & `citrine-2.8.0/src/citrine/jobs/job.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/jobs/waiting.py` & `citrine-2.8.0/src/citrine/jobs/waiting.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/api_error.py` & `citrine-2.8.0/src/citrine/resources/api_error.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/attribute_templates.py` & `citrine-2.8.0/src/citrine/resources/attribute_templates.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/audit_info.py` & `citrine-2.8.0/src/citrine/resources/audit_info.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/branch.py` & `citrine-2.8.0/src/citrine/resources/branch.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/condition_template.py` & `citrine-2.8.0/src/citrine/resources/condition_template.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/data_concepts.py` & `citrine-2.8.0/src/citrine/resources/data_concepts.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/data_objects.py` & `citrine-2.8.0/src/citrine/resources/data_objects.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/data_version_update.py` & `citrine-2.8.0/src/citrine/resources/data_version_update.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/dataset.py` & `citrine-2.8.0/src/citrine/resources/dataset.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/delete.py` & `citrine-2.8.0/src/citrine/resources/delete.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/descriptors.py` & `citrine-2.8.0/src/citrine/resources/descriptors.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/design_execution.py` & `citrine-2.8.0/src/citrine/resources/design_execution.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/design_space.py` & `citrine-2.8.0/src/citrine/resources/design_space.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/design_workflow.py` & `citrine-2.8.0/src/citrine/resources/design_workflow.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/experiment_datasource.py` & `citrine-2.8.0/src/citrine/resources/experiment_datasource.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/file_link.py` & `citrine-2.8.0/src/citrine/resources/file_link.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,26 +1,25 @@
 """A collection of FileLink objects."""
+from deprecation import deprecated
 import mimetypes
 import os
 from pathlib import Path
 from enum import Enum
 from logging import getLogger
-from typing import Iterable, Optional, Tuple, Union, List, Dict
+from typing import Optional, Tuple, Union, List, Dict
 from urllib.parse import urlparse, quote
 from uuid import UUID
 
 import requests
 from boto3 import client as boto3_client
 from boto3.session import Config
 from botocore.exceptions import ClientError
 from citrine._rest.collection import Collection
 from citrine._rest.resource import Resource
-from citrine._serialization.properties import List as PropertyList
-from citrine._serialization.properties import Optional as PropertyOptional
-from citrine._serialization.properties import String, Object, Integer
+from citrine._serialization import properties
 from citrine._serialization.serializable import Serializable
 from citrine._session import Session
 from citrine._utils.functions import rewrite_s3_links_locally
 from citrine._utils.functions import write_file_locally, format_escaped_url
 
 from citrine.jobs.job import JobSubmissionResponse, _poll_for_job_completion
 from citrine.resources.response import Response
@@ -78,35 +77,35 @@
 
     pass
 
 
 class CsvColumnInfo(Serializable):
     """The info for a CSV Column, contains the name, recommended and exact bounds."""
 
-    name = String('name')
+    name = properties.String('name')
     """:str: name of the column"""
-    bounds = Object(BaseBounds, 'bounds')
+    bounds = properties.Object(BaseBounds, 'bounds')
     """:BaseBounds: recommended bounds of the column (might include some padding)"""
-    exact_range_bounds = Object(BaseBounds, 'exact_range_bounds')
+    exact_range_bounds = properties.Object(BaseBounds, 'exact_range_bounds')
     """:BaseBounds: exact bounds of the column"""
 
-    def __init__(self, name: String, bounds: BaseBounds,
+    def __init__(self, name: str, bounds: BaseBounds,
                  exact_range_bounds: BaseBounds):  # pragma: no cover
         self.name = name
         self.bounds = bounds
         self.exact_range_bounds = exact_range_bounds
 
 
 class CsvValidationData(FileProcessingData, Serializable):
     """The resulting data from the processed CSV file."""
 
-    columns = PropertyOptional(PropertyList(Object(CsvColumnInfo)), 'columns',
-                               override=True)
+    columns = properties.Optional(properties.List(properties.Object(CsvColumnInfo)),
+                                  'columns', override=True)
     """:Optional[List[CsvColumnInfo]]: all of the columns in the CSV"""
-    record_count = Integer('record_count')
+    record_count = properties.Integer('record_count')
     """:int: the number of rows in the CSV"""
 
     def __init__(self, columns: List[CsvColumnInfo],
                  record_count: int):  # pragma: no cover
         self.columns = columns
         self.record_count = record_count
 
@@ -133,29 +132,40 @@
     filename: str
         The name of the file.
     url: str
         URL that can be used to access the file.
 
     """
 
-    filename = String('filename', override=True)
-    url = String('url', override=True)
-    typ = String('type')
+    # NOTE: skipping the "metadata" field since it appears to be unused
+    # NOTE: skipping the "versioned_url" field since it is redundant
+    # NOTE: skipping the "unversioned_url" field since it is redundant
+    filename = properties.String('filename', override=True)
+    url = properties.String('url', override=True)
+    uid = properties.Optional(properties.UUID, 'id', serializable=False)
+    version = properties.Optional(properties.UUID, 'version', serializable=False)
+    created_time = properties.Optional(properties.Datetime, 'created_time', serializable=False)
+    created_by = properties.Optional(properties.UUID, 'created_by', serializable=False)
+    mime_type = properties.Optional(properties.String, 'mime_type', serializable=False)
+    size = properties.Optional(properties.Integer, 'size', serializable=False)
+    description = properties.Optional(properties.String, 'description', serializable=False)
+    version_number = properties.Optional(properties.Integer, 'version_number', serializable=False)
+    typ = properties.String('type', default="file_link", deserializable=False)
 
     def __init__(self, filename: str, url: str):
         GEMDFileLink.__init__(self, filename, url)
         self.typ = GEMDFileLink.typ
 
     @property
     def name(self):
         """Attribute name is an alias for filename."""
         return self.filename
 
     def __str__(self):
-        return '<File link {!r}>'.format(self.filename)
+        return f'<File link {self.filename!r}>'
 
     def as_dict(self) -> dict:
         """Dump to a dictionary (useful for interoperability with gemd)."""
         return self.dump()
 
 
 class FileCollection(Collection[FileLink]):
@@ -212,91 +222,31 @@
                 return None, None
         return file_id, version_id
 
     def _get_path_from_file_link(self, file_link: FileLink,
                                  *,
                                  action: str = None) -> str:
         """Build the platform path for taking an action with a particular file link."""
-        # Use this sessions project/dataset credentials and the URL's file / version
-        file_id, version_id = self._get_ids_from_url(file_link.url)
-        if file_id is None:
-            raise ValueError("FileLink did not contain a Citrine platform file URL.")
+        # Use this session's project/dataset credentials and the URLs file / version
+        if file_link.uid is not None:
+            file_id = file_link.uid
+            version_id = file_link.version
+        else:
+            file_id, version_id = self._get_ids_from_url(file_link.url)
+            if file_id is None:
+                raise ValueError("FileLink did not contain a Citrine platform file URL.")
         return self._get_path(uid=file_id, version=version_id, action=action)
 
     def build(self, data: dict) -> FileLink:
         """Build an instance of FileLink."""
+        # Use this chance to construct a URL from platform metadata
+        if 'url' not in data:
+            data['url'] = self._get_path(uid=data["id"], version=data["version"])
         return FileLink.build(data)
 
-    def _fetch_page(self,
-                    page: Optional[int] = None,
-                    per_page: Optional[int] = None) -> Tuple[Iterable[FileLink], str]:
-        """
-        List all visible files in the collection.
-
-        Parameters
-        ---------
-        page: int, optional
-            The "page" number of results to list. Default is the first page, which is 1.
-        per_page: int, optional
-            Max number of results to return for each call. Default is 20.
-
-        Returns
-        -------
-        Iterable[FileLink]
-            FileLink objects in this collection.
-        str
-            The next uri if one is available, empty string otherwise
-
-        """
-        path = self._get_path()
-        params = {}
-        if page is not None:
-            params["page"] = page
-        if per_page is not None:
-            params["per_page"] = per_page
-
-        response = self.session.get_resource(path=path, params=params)
-        collection = response[self._collection_key]
-        return collection, ""
-
-    def _build_collection_elements(self, collection):
-        for file in collection:
-            yield self.build(self._as_dict_from_resource(file))
-
-    def _as_dict_from_resource(self, file: dict):
-        """
-        Convert a file link resource downloaded from the API into a FileLink dictionary.
-
-        This is necessary because the database resource contains additional information that is
-        not in the FileLink object, such as file size and the id of the user who uploaded the file.
-
-        Parameters
-        ---------
-        file: dict
-            A JSON dictionary corresponding to the file link as it is saved in the database.
-
-        Returns
-        -------
-        dict
-            A dictionary that can be built into a FileLink object.
-
-        """
-        # FIXME  While the 'id' field is supposed to be the file ID, it contains the version
-        #  for some reason.  Needs to be fixed on back end.  PLA-9482
-        filename = file['filename']
-        file_id = file['id']
-        version_id = file['version']
-
-        file_dict = {
-            'url': self._get_path(uid=file_id, version=version_id),
-            'filename': filename,
-            'type': GEMDFileLink.typ
-        }
-        return file_dict
-
     def get(self,
             uid: Union[UUID, str],
             *,
             version: Optional[Union[UUID, str, int]] = None) -> FileLink:
         """
         Get an element of the collection by its id.
 
@@ -341,15 +291,15 @@
 
         if isinstance(uid, str):
             # Assume it's the filename on platform;
             if version is None or isinstance(version, int):
                 file = self._search_by_file_name(dset_id=self.dataset_id,
                                                  file_name=uid,
                                                  file_version_number=version)
-            else:  # We did our type checks earlier; version is an UUID
+            else:  # We did our type checks earlier; version is a UUID
                 file = self._search_by_file_version_id(file_version_id=version)
         else:  # We did our type checks earlier; uid is a UUID
             if isinstance(version, UUID):
                 file = self._search_by_file_version_id(file_version_id=version)
             else:  # We did our type checks earlier; version is an int or None
                 file = self._search_by_dataset_file_id(dataset_file_id=uid,
                                                        dset_id=self.dataset_id,
@@ -483,15 +433,15 @@
                     'fileName': file_name,
                     'fileVersionNumber': file_version_number
                 }
         }
 
         data = self.session.post_resource(path=path, json=search_json)
 
-        return self.build(self._as_dict_from_resource(data['files'][0]))
+        return self.build(data['files'][0])
 
     def _search_by_file_version_id(self,
                                    file_version_id: UUID
                                    ) -> Optional[FileLink]:
         """
         Make a request to the backend to search a file by file version id.
 
@@ -513,15 +463,15 @@
                 'type': SearchFileFilterTypeEnum.VERSION_ID_SEARCH.value,
                 'fileVersionUuid': str(file_version_id)
             }
         }
 
         data = self.session.post_resource(path=path, json=search_json)
 
-        return self.build(self._as_dict_from_resource(data['files'][0]))
+        return self.build(data['files'][0])
 
     def _search_by_dataset_file_id(self,
                                    dataset_file_id: UUID,
                                    dset_id: UUID,
                                    file_version_number: Optional[int] = None
                                    ) -> Optional[FileLink]:
         """
@@ -554,15 +504,15 @@
                 'datasetFileId': str(dataset_file_id),
                 'fileVersionNumber': file_version_number
             }
         }
 
         data = self.session.post_resource(path=path, json=search_json)
 
-        return self.build(self._as_dict_from_resource(data['files'][0]))
+        return self.build(data['files'][0])
 
     @staticmethod
     def _mime_type(file_path: Path):
         # This string coercion is for supporting pathlib.Path objects in python 3.6
         mime_type = mimetypes.guess_type(str(file_path))[0]
         if mime_type is None:
             mime_type = "application/octet-stream"
@@ -640,16 +590,15 @@
         try:
             file_id = complete_response['file_info']['file_id']
             version_id = complete_response['file_info']['version']
         except KeyError:
             raise RuntimeError("Upload completion response is missing some "
                                "fields: {}".format(complete_response))
 
-        url = self._get_path(uid=file_id, version=version_id)
-        return FileLink(filename=dest_name, url=url)
+        return self.build({"filename": dest_name, "id": file_id, "version": version_id})
 
     def download(self, *, file_link: Union[str, UUID, FileLink], local_path: Union[str, Path]):
         """
         Download the file associated with a given FileLink to the local computer.
 
         Parameters
         ----------
@@ -669,27 +618,16 @@
             else:
                 final_path = Path(directory) / filename
         elif local_path.is_dir():
             final_path = local_path / file_link.filename
         else:
             final_path = local_path
 
-        if self._is_external_url(file_link.url):  # Pull it from where ever it lives
-            final_url = file_link.url
-        elif self._validate_local_url(file_link.url):
-            # The "/content-link" route returns a pre-signed url to download the file.
-            content_link = self._get_path_from_file_link(file_link, action='content-link')
-            content_link_response = self.session.get_resource(content_link)
-            pre_signed_url = content_link_response['pre_signed_read_link']
-            final_url = rewrite_s3_links_locally(pre_signed_url, self.session.s3_endpoint_url)
-        else:  # Unrecognized
-            raise ValueError(f"URL was malformed for a local file resource ({file_link.url}).")
-
-        download_response = requests.get(final_url)
-        write_file_locally(download_response.content, final_path)
+        response_content = self.read(file_link=file_link)
+        write_file_locally(response_content, final_path)
 
     def read(self, *, file_link: Union[str, UUID, FileLink]):
         """
         Read the file associated with a given FileLink.
 
         Parameters
         ----------
@@ -714,14 +652,18 @@
             final_url = rewrite_s3_links_locally(pre_signed_url, self.session.s3_endpoint_url)
         else:  # Unrecognized
             raise ValueError(f"URL was malformed for a local file resource ({file_link.url}).")
 
         download_response = requests.get(final_url)
         return download_response.content
 
+    @deprecated(deprecated_in="2.4.0",
+                removed_in="3.0.0",
+                details="The process file protocol is deprecated "
+                        "in favor of GUI-based ingest routes")
     def process(self, *, file_link: Union[FileLink, str, UUID],
                 processing_type: FileProcessingType,
                 wait_for_response: bool = True,
                 timeout: float = 2 * 60,
                 polling_delay: float = 1.0) -> Union[JobSubmissionResponse,
                                                      Dict[FileProcessingType,
                                                           FileProcessingResult]]:
@@ -766,14 +708,18 @@
             return self.poll_file_processing_job(file_link=file_link,
                                                  processing_type=processing_type,
                                                  job_id=job.job_id, timeout=timeout,
                                                  polling_delay=polling_delay)
         else:
             return job
 
+    @deprecated(deprecated_in="2.4.0",
+                removed_in="3.0.0",
+                details="The process file protocol is deprecated "
+                        "in favor of GUI-based ingest routes")
     def poll_file_processing_job(self, *, file_link: FileLink,
                                  processing_type: FileProcessingType,
                                  job_id: UUID,
                                  timeout: float = 2 * 60,
                                  polling_delay: float = 1.0) -> Dict[FileProcessingType,
                                                                      FileProcessingResult]:
         """
@@ -802,14 +748,18 @@
         """
         # Poll for job completion - this will raise an error if the job failed
         _poll_for_job_completion(self.session, self.project_id, job_id, timeout=timeout,
                                  polling_delay=polling_delay)
 
         return self.file_processing_result(file_link=file_link, processing_types=[processing_type])
 
+    @deprecated(deprecated_in="2.4.0",
+                removed_in="3.0.0",
+                details="The process file protocol is deprecated "
+                        "in favor of GUI-based ingest routes")
     def file_processing_result(self, *,
                                file_link: FileLink,
                                processing_types: List[FileProcessingType]) -> \
             Dict[FileProcessingType, FileProcessingResult]:
         """
         Return the file processing result for the given file link and processing type.
```

### Comparing `citrine-2.2.1/src/citrine/resources/gemd_resource.py` & `citrine-2.8.0/src/citrine/resources/gemd_resource.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/gemtables.py` & `citrine-2.8.0/src/citrine/resources/gemtables.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/generative_design_execution.py` & `citrine-2.8.0/src/citrine/resources/generative_design_execution.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/ingredient_run.py` & `citrine-2.8.0/src/citrine/resources/ingredient_run.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/ingredient_spec.py` & `citrine-2.8.0/src/citrine/resources/ingredient_spec.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/material_run.py` & `citrine-2.8.0/src/citrine/resources/material_run.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/material_spec.py` & `citrine-2.8.0/src/citrine/resources/material_spec.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/material_template.py` & `citrine-2.8.0/src/citrine/resources/material_template.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/measurement_run.py` & `citrine-2.8.0/src/citrine/resources/measurement_run.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/measurement_spec.py` & `citrine-2.8.0/src/citrine/resources/measurement_spec.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/measurement_template.py` & `citrine-2.8.0/src/citrine/resources/measurement_template.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/module.py` & `citrine-2.8.0/src/citrine/resources/module.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/object_runs.py` & `citrine-2.8.0/src/citrine/resources/object_runs.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/object_specs.py` & `citrine-2.8.0/src/citrine/resources/object_specs.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/object_templates.py` & `citrine-2.8.0/src/citrine/resources/object_templates.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/parameter_template.py` & `citrine-2.8.0/src/citrine/resources/parameter_template.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/predictor.py` & `citrine-2.8.0/src/citrine/resources/predictor.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/predictor_evaluation_execution.py` & `citrine-2.8.0/src/citrine/resources/predictor_evaluation_execution.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/predictor_evaluation_workflow.py` & `citrine-2.8.0/src/citrine/resources/predictor_evaluation_workflow.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/process_run.py` & `citrine-2.8.0/src/citrine/resources/process_run.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/process_spec.py` & `citrine-2.8.0/src/citrine/resources/process_spec.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/process_template.py` & `citrine-2.8.0/src/citrine/resources/process_template.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/project.py` & `citrine-2.8.0/src/citrine/resources/project.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/project_member.py` & `citrine-2.8.0/src/citrine/resources/project_member.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/property_template.py` & `citrine-2.8.0/src/citrine/resources/property_template.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/report.py` & `citrine-2.8.0/src/citrine/resources/report.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/response.py` & `citrine-2.8.0/src/citrine/resources/response.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/status_detail.py` & `citrine-2.8.0/src/citrine/resources/status_detail.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/table_config.py` & `citrine-2.8.0/src/citrine/resources/table_config.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/team.py` & `citrine-2.8.0/src/citrine/resources/team.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/templates.py` & `citrine-2.8.0/src/citrine/resources/templates.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/resources/user.py` & `citrine-2.8.0/src/citrine/resources/user.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/seeding/find_or_create.py` & `citrine-2.8.0/src/citrine/seeding/find_or_create.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine/seeding/sort_gems.py` & `citrine-2.8.0/src/citrine/seeding/sort_gems.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/src/citrine.egg-info/PKG-INFO` & `citrine-2.8.0/src/citrine.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: citrine
-Version: 2.2.1
+Version: 2.8.0
 Summary: Python library for the Citrine Platform
 Home-page: http://github.com/CitrineInformatics/citrine-python
 Author: Citrine Informatics
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `citrine-2.2.1/src/citrine.egg-info/SOURCES.txt` & `citrine-2.8.0/src/citrine.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -54,14 +54,15 @@
 src/citrine/informatics/reports.py
 src/citrine/informatics/scores.py
 src/citrine/informatics/constraints/__init__.py
 src/citrine/informatics/constraints/categorical_constraint.py
 src/citrine/informatics/constraints/constraint.py
 src/citrine/informatics/constraints/ingredient_count_constraint.py
 src/citrine/informatics/constraints/ingredient_fraction_constraint.py
+src/citrine/informatics/constraints/ingredient_ratio_constraint.py
 src/citrine/informatics/constraints/label_fraction_constraint.py
 src/citrine/informatics/constraints/scalar_range_constraint.py
 src/citrine/informatics/design_spaces/__init__.py
 src/citrine/informatics/design_spaces/data_source_design_space.py
 src/citrine/informatics/design_spaces/design_space.py
 src/citrine/informatics/design_spaces/enumerated_design_space.py
 src/citrine/informatics/design_spaces/formulation_design_space.py
@@ -78,14 +79,16 @@
 src/citrine/informatics/predictors/ingredient_fractions_predictor.py
 src/citrine/informatics/predictors/ingredients_to_formulation_predictor.py
 src/citrine/informatics/predictors/label_fractions_predictor.py
 src/citrine/informatics/predictors/mean_property_predictor.py
 src/citrine/informatics/predictors/molecular_structure_featurizer.py
 src/citrine/informatics/predictors/predictor.py
 src/citrine/informatics/predictors/simple_mixture_predictor.py
+src/citrine/informatics/predictors/single_predict_request.py
+src/citrine/informatics/predictors/single_prediction.py
 src/citrine/informatics/workflows/__init__.py
 src/citrine/informatics/workflows/design_workflow.py
 src/citrine/informatics/workflows/predictor_evaluation_workflow.py
 src/citrine/informatics/workflows/workflow.py
 src/citrine/jobs/__init__.py
 src/citrine/jobs/job.py
 src/citrine/jobs/waiting.py
```

### Comparing `citrine-2.2.1/tests/test_citrine.py` & `citrine-2.8.0/tests/test_citrine.py`

 * *Files identical despite different names*

### Comparing `citrine-2.2.1/tests/test_session.py` & `citrine-2.8.0/tests/test_session.py`

 * *Files identical despite different names*

