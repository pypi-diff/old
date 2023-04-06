# Comparing `tmp/sagemaker-2.98.0.tar.gz` & `tmp/sagemaker-2.99.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/sagemaker-2.98.0.tar", last modified: Tue Jul  5 18:31:47 2022, max compression
+gzip compressed data, was "dist/sagemaker-2.99.0.tar", last modified: Fri Jul  8 05:22:37 2022, max compression
```

## Comparing `sagemaker-2.98.0.tar` & `sagemaker-2.99.0.tar`

### file list

```diff
@@ -1,332 +1,333 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/
--rw-rw-r--   0 root         (0) root         (0)    10118 2022-06-30 18:50:06.000000 sagemaker-2.98.0/LICENSE.txt
--rw-rw-r--   0 root         (0) root         (0)      248 2022-06-30 18:50:06.000000 sagemaker-2.98.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)    12375 2022-07-05 18:31:47.000000 sagemaker-2.98.0/PKG-INFO
--rw-rw-r--   0 root         (0) root         (0)     9632 2022-06-30 18:50:06.000000 sagemaker-2.98.0/README.rst
--rw-rw-r--   0 root         (0) root         (0)        7 2022-07-05 18:31:46.000000 sagemaker-2.98.0/VERSION
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/requirements/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/requirements/extras/
--rw-rw-r--   0 root         (0) root         (0)       67 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/extras/local_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       13 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/extras/scipy_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)      373 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/extras/test_requirements.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/requirements/tox/
--rw-rw-r--   0 root         (0) root         (0)       30 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/doc8_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       18 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/docstyle_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       42 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/flake8_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       12 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/mypy_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       18 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/pydocstyle_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       29 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/pylint_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       31 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/spelling_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)       13 2022-06-30 18:50:06.000000 sagemaker-2.98.0/requirements/tox/twine_requirements.txt
--rw-rw-r--   0 root         (0) root         (0)      204 2022-07-05 18:31:47.000000 sagemaker-2.98.0/setup.cfg
--rw-rw-r--   0 root         (0) root         (0)     3364 2022-06-30 18:50:06.000000 sagemaker-2.98.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/
--rw-rw-r--   0 root         (0) root         (0)     3003 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     3221 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/_studio.py
--rw-rw-r--   0 root         (0) root         (0)    25339 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/algorithm.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/amazon/
--rw-rw-r--   0 root         (0) root         (0)      560 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    20009 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/amazon_estimator.py
--rw-rw-r--   0 root         (0) root         (0)     9690 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/common.py
--rw-rw-r--   0 root         (0) root         (0)    16678 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/factorization_machines.py
--rw-rw-r--   0 root         (0) root         (0)     3448 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/hyperparameter.py
--rw-rw-r--   0 root         (0) root         (0)    11546 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/ipinsights.py
--rw-rw-r--   0 root         (0) root         (0)    12755 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/kmeans.py
--rw-rw-r--   0 root         (0) root         (0)    12301 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/knn.py
--rw-rw-r--   0 root         (0) root         (0)    11182 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/lda.py
--rw-rw-r--   0 root         (0) root         (0)    25618 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/linear_learner.py
--rw-rw-r--   0 root         (0) root         (0)    12708 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/ntm.py
--rw-rw-r--   0 root         (0) root         (0)    16876 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/object2vec.py
--rw-rw-r--   0 root         (0) root         (0)    11849 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/pca.py
--rw-rw-r--   0 root         (0) root         (0)    10874 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/randomcutforest.py
--rw-rw-r--   0 root         (0) root         (0)    25553 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/record_pb2.py
--rw-rw-r--   0 root         (0) root         (0)     1426 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/amazon/validation.py
--rw-rw-r--   0 root         (0) root         (0)    30165 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/analytics.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/apiutils/
--rw-rw-r--   0 root         (0) root         (0)      629 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/apiutils/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     8541 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/apiutils/_base_types.py
--rw-rw-r--   0 root         (0) root         (0)     5117 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/apiutils/_boto_functions.py
--rw-rw-r--   0 root         (0) root         (0)     1136 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/apiutils/_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/async_inference/
--rw-rw-r--   0 root         (0) root         (0)      946 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/async_inference/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     3901 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/async_inference/async_inference_config.py
--rw-rw-r--   0 root         (0) root         (0)     3867 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/async_inference/async_inference_response.py
--rw-rw-r--   0 root         (0) root         (0)     1653 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/async_inference/waiter_config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/automl/
--rw-rw-r--   0 root         (0) root         (0)      560 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/automl/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    33849 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/automl/automl.py
--rw-rw-r--   0 root         (0) root         (0)    14365 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/automl/candidate_estimator.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/chainer/
--rw-rw-r--   0 root         (0) root         (0)      771 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/chainer/__init__.py
--rw-rw-r--   0 root         (0) root         (0)      657 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/chainer/defaults.py
--rw-rw-r--   0 root         (0) root         (0)    12725 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/chainer/estimator.py
--rw-rw-r--   0 root         (0) root         (0)     9171 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/chainer/model.py
--rw-rw-r--   0 root         (0) root         (0)    60066 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/clarify.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/cli/
--rw-rw-r--   0 root         (0) root         (0)      640 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/
--rw-rw-r--   0 root         (0) root         (0)      679 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/
--rw-rw-r--   0 root         (0) root         (0)      690 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     6468 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/ast_transformer.py
--rw-rw-r--   0 root         (0) root         (0)     7848 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/files.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/
--rw-rw-r--   0 root         (0) root         (0)      923 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     3662 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/airflow.py
--rw-rw-r--   0 root         (0) root         (0)     2482 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/deprecated_params.py
--rw-rw-r--   0 root         (0) root         (0)     6892 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/framework_version.py
--rw-rw-r--   0 root         (0) root         (0)     4954 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/image_uris.py
--rw-rw-r--   0 root         (0) root         (0)     4261 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/matching.py
--rw-rw-r--   0 root         (0) root         (0)     1245 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/modifier.py
--rw-rw-r--   0 root         (0) root         (0)     1870 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/parsing.py
--rw-rw-r--   0 root         (0) root         (0)     4655 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/predictors.py
--rw-rw-r--   0 root         (0) root         (0)    11490 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/renamed_params.py
--rw-rw-r--   0 root         (0) root         (0)    17894 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/serde.py
--rw-rw-r--   0 root         (0) root         (0)     8776 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/tf_legacy_mode.py
--rw-rw-r--   0 root         (0) root         (0)     5223 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/tfs.py
--rw-rw-r--   0 root         (0) root         (0)     6393 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/training_input.py
--rw-rw-r--   0 root         (0) root         (0)     4094 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/training_params.py
--rw-rw-r--   0 root         (0) root         (0)     2933 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/sagemaker_upgrade_v2.py
--rw-rw-r--   0 root         (0) root         (0)     9491 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/cli/framework_upgrade.py
--rw-rw-r--   0 root         (0) root         (0)      925 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/content_types.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/dataset_definition/
--rw-rw-r--   0 root         (0) root         (0)      845 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/dataset_definition/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     9158 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/dataset_definition/inputs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/debugger/
--rw-rw-r--   0 root         (0) root         (0)     1417 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/debugger/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    39259 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/debugger/debugger.py
--rw-rw-r--   0 root         (0) root         (0)    12353 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/debugger/framework_profile.py
--rw-rw-r--   0 root         (0) root         (0)    17955 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/debugger/metrics_config.py
--rw-rw-r--   0 root         (0) root         (0)     4685 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/debugger/profiler_config.py
--rw-rw-r--   0 root         (0) root         (0)     1481 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/debugger/profiler_constants.py
--rw-rw-r--   0 root         (0) root         (0)     4428 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/debugger/utils.py
--rw-rw-r--   0 root         (0) root         (0)     6507 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/deprecations.py
--rw-rw-r--   0 root         (0) root         (0)    11915 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/deserializers.py
--rw-rw-r--   0 root         (0) root         (0)     5140 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/drift_check_baselines.py
--rw-rw-r--   0 root         (0) root         (0)     1967 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/environment_variables.py
--rw-rw-r--   0 root         (0) root         (0)   150767 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/estimator.py
--rw-rw-r--   0 root         (0) root         (0)     2365 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/exceptions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/feature_store/
--rw-rw-r--   0 root         (0) root         (0)      560 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/feature_store/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     4066 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/feature_store/feature_definition.py
--rw-rw-r--   0 root         (0) root         (0)    28436 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/feature_store/feature_group.py
--rw-rw-r--   0 root         (0) root         (0)     6319 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/feature_store/inputs.py
--rw-rw-r--   0 root         (0) root         (0)    25575 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/fw_utils.py
--rw-rw-r--   0 root         (0) root         (0)    15141 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/git_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/huggingface/
--rw-rw-r--   0 root         (0) root         (0)      967 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/huggingface/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    16429 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/huggingface/estimator.py
--rw-rw-r--   0 root         (0) root         (0)    21613 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/huggingface/model.py
--rw-rw-r--   0 root         (0) root         (0)     5173 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/huggingface/processing.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/huggingface/training_compiler/
--rw-rw-r--   0 root         (0) root         (0)        0 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/huggingface/training_compiler/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     4129 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/huggingface/training_compiler/config.py
--rw-rw-r--   0 root         (0) root         (0)     4730 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/hyperparameters.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/
--rw-rw-r--   0 root         (0) root         (0)    11735 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/autogluon.json
--rw-rw-r--   0 root         (0) root         (0)     1350 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/blazingtext.json
--rw-rw-r--   0 root         (0) root         (0)     4062 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/chainer.json
--rw-rw-r--   0 root         (0) root         (0)     1430 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/clarify.json
--rw-rw-r--   0 root         (0) root         (0)     2728 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/coach-mxnet.json
--rw-rw-r--   0 root         (0) root         (0)     7536 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/coach-tensorflow.json
--rw-rw-r--   0 root         (0) root         (0)     1060 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/data-wrangler.json
--rw-rw-r--   0 root         (0) root         (0)     1306 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/debugger.json
--rw-rw-r--   0 root         (0) root         (0)     1361 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/factorization-machines.json
--rw-rw-r--   0 root         (0) root         (0)     1357 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/forecasting-deepar.json
--rw-rw-r--   0 root         (0) root         (0)     1963 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/huggingface-neuron.json
--rw-rw-r--   0 root         (0) root         (0)     4516 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/huggingface-training-compiler.json
--rw-rw-r--   0 root         (0) root         (0)    55091 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/huggingface.json
--rw-rw-r--   0 root         (0) root         (0)     1307 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/image-classification-neo.json
--rw-rw-r--   0 root         (0) root         (0)     1359 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/image-classification.json
--rw-rw-r--   0 root         (0) root         (0)     2660 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/inferentia-mxnet.json
--rw-rw-r--   0 root         (0) root         (0)     3928 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/inferentia-pytorch.json
--rw-rw-r--   0 root         (0) root         (0)     2673 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/inferentia-tensorflow.json
--rw-rw-r--   0 root         (0) root         (0)     1349 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/ipinsights.json
--rw-rw-r--   0 root         (0) root         (0)     1345 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/kmeans.json
--rw-rw-r--   0 root         (0) root         (0)     1342 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/knn.json
--rw-rw-r--   0 root         (0) root         (0)      877 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/lda.json
--rw-rw-r--   0 root         (0) root         (0)     1353 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/linear-learner.json
--rw-rw-r--   0 root         (0) root         (0)     1261 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/model-monitor.json
--rw-rw-r--   0 root         (0) root         (0)    42939 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/mxnet.json
--rw-rw-r--   0 root         (0) root         (0)     1687 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/neo-mxnet.json
--rw-rw-r--   0 root         (0) root         (0)     6800 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/neo-pytorch.json
--rw-rw-r--   0 root         (0) root         (0)     3111 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/neo-tensorflow.json
--rw-rw-r--   0 root         (0) root         (0)     1342 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/ntm.json
--rw-rw-r--   0 root         (0) root         (0)     1355 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/object-detection.json
--rw-rw-r--   0 root         (0) root         (0)     1349 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/object2vec.json
--rw-rw-r--   0 root         (0) root         (0)     1342 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/pca.json
--rw-rw-r--   0 root         (0) root         (0)    50643 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/pytorch.json
--rw-rw-r--   0 root         (0) root         (0)     1354 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/randomcutforest.json
--rw-rw-r--   0 root         (0) root         (0)     1730 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/ray-pytorch.json
--rw-rw-r--   0 root         (0) root         (0)     7826 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/ray-tensorflow.json
--rw-rw-r--   0 root         (0) root         (0)     1360 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/semantic-segmentation.json
--rw-rw-r--   0 root         (0) root         (0)     1346 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/seq2seq.json
--rw-rw-r--   0 root         (0) root         (0)     4098 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/sklearn.json
--rw-rw-r--   0 root         (0) root         (0)     4262 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/spark.json
--rw-rw-r--   0 root         (0) root         (0)     2553 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/sparkml-serving.json
--rw-rw-r--   0 root         (0) root         (0)   129904 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/tensorflow.json
--rw-rw-r--   0 root         (0) root         (0)      857 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/vw.json
--rw-rw-r--   0 root         (0) root         (0)     1294 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/xgboost-neo.json
--rw-rw-r--   0 root         (0) root         (0)    10665 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uri_config/xgboost.json
--rw-rw-r--   0 root         (0) root         (0)    21478 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/image_uris.py
--rw-rw-r--   0 root         (0) root         (0)     8883 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/inputs.py
--rw-rw-r--   0 root         (0) root         (0)    11305 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/job.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/
--rw-rw-r--   0 root         (0) root         (0)        0 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     7181 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/accessors.py
--rw-rw-r--   0 root         (0) root         (0)    15343 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/artifacts.py
--rw-rw-r--   0 root         (0) root         (0)    15910 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/cache.py
--rw-rw-r--   0 root         (0) root         (0)     4834 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/constants.py
--rw-rw-r--   0 root         (0) root         (0)     2292 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/enums.py
--rw-rw-r--   0 root         (0) root         (0)     4758 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/exceptions.py
--rw-rw-r--   0 root         (0) root         (0)    16623 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/filters.py
--rw-rw-r--   0 root         (0) root         (0)    17765 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/notebook_utils.py
--rw-rw-r--   0 root         (0) root         (0)      948 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/parameters.py
--rw-rw-r--   0 root         (0) root         (0)    14964 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/types.py
--rw-rw-r--   0 root         (0) root         (0)    15366 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/utils.py
--rw-rw-r--   0 root         (0) root         (0)    10388 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/jumpstart/validators.py
--rw-rw-r--   0 root         (0) root         (0)    10629 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lambda_helper.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/lineage/
--rw-rw-r--   0 root         (0) root         (0)      589 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     7032 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/_api_types.py
--rw-rw-r--   0 root         (0) root         (0)     2110 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/_utils.py
--rw-rw-r--   0 root         (0) root         (0)    12422 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/action.py
--rw-rw-r--   0 root         (0) root         (0)    24348 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/artifact.py
--rw-rw-r--   0 root         (0) root         (0)     7024 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/association.py
--rw-rw-r--   0 root         (0) root         (0)    18902 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/context.py
--rw-rw-r--   0 root         (0) root         (0)     7655 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/lineage_trial_component.py
--rw-rw-r--   0 root         (0) root         (0)    13330 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/query.py
--rw-rw-r--   0 root         (0) root         (0)    13236 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/lineage/visualizer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/local/
--rw-rw-r--   0 root         (0) root         (0)      766 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/local/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    12858 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/local/data.py
--rw-rw-r--   0 root         (0) root         (0)    24836 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/local/entities.py
--rw-rw-r--   0 root         (0) root         (0)    42493 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/local/image.py
--rw-rw-r--   0 root         (0) root         (0)    21169 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/local/local_session.py
--rw-rw-r--   0 root         (0) root         (0)     4881 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/local/utils.py
--rw-rw-r--   0 root         (0) root         (0)     5916 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/logs.py
--rw-rw-r--   0 root         (0) root         (0)     1951 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/metadata_properties.py
--rw-rw-r--   0 root         (0) root         (0)    71357 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model.py
--rw-rw-r--   0 root         (0) root         (0)     6417 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_metrics.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/
--rw-rw-r--   0 root         (0) root         (0)     2310 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    60563 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/clarify_model_monitoring.py
--rw-rw-r--   0 root         (0) root         (0)     2805 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/cron_expression_generator.py
--rw-rw-r--   0 root         (0) root         (0)     4771 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/data_capture_config.py
--rw-rw-r--   0 root         (0) root         (0)     2311 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/dataset_format.py
--rw-rw-r--   0 root         (0) root         (0)   150925 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/model_monitoring.py
--rw-rw-r--   0 root         (0) root         (0)    19947 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_monitor/monitoring_files.py
--rw-rw-r--   0 root         (0) root         (0)     3100 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/model_uris.py
--rw-rw-r--   0 root         (0) root         (0)    15258 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/multidatamodel.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/mxnet/
--rw-rw-r--   0 root         (0) root         (0)      868 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/mxnet/__init__.py
--rw-rw-r--   0 root         (0) root         (0)      657 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/mxnet/defaults.py
--rw-rw-r--   0 root         (0) root         (0)    14635 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/mxnet/estimator.py
--rw-rw-r--   0 root         (0) root         (0)    13786 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/mxnet/model.py
--rw-rw-r--   0 root         (0) root         (0)     2674 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/mxnet/processing.py
--rw-rw-r--   0 root         (0) root         (0)     2849 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/network.py
--rw-rw-r--   0 root         (0) root         (0)     5683 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/parameter.py
--rw-rw-r--   0 root         (0) root         (0)    19027 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/pipeline.py
--rw-rw-r--   0 root         (0) root         (0)    23439 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/predictor.py
--rw-rw-r--   0 root         (0) root         (0)    15745 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/predictor_async.py
--rw-rw-r--   0 root         (0) root         (0)    79660 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/processing.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/pytorch/
--rw-rw-r--   0 root         (0) root         (0)      870 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/pytorch/__init__.py
--rw-rw-r--   0 root         (0) root         (0)      657 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/pytorch/defaults.py
--rw-rw-r--   0 root         (0) root         (0)    14968 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/pytorch/estimator.py
--rw-rw-r--   0 root         (0) root         (0)    13858 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/pytorch/model.py
--rw-rw-r--   0 root         (0) root         (0)     2682 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/pytorch/processing.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/rl/
--rw-rw-r--   0 root         (0) root         (0)      765 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/rl/__init__.py
--rw-rw-r--   0 root         (0) root         (0)    19305 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/rl/estimator.py
--rw-rw-r--   0 root         (0) root         (0)     7193 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/s3.py
--rw-rw-r--   0 root         (0) root         (0)     2960 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/script_uris.py
--rw-rw-r--   0 root         (0) root         (0)    13190 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/serializers.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/serverless/
--rw-rw-r--   0 root         (0) root         (0)      877 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/serverless/__init__.py
--rw-rw-r--   0 root         (0) root         (0)      913 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/serverless/model.py
--rw-rw-r--   0 root         (0) root         (0)      911 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/serverless/predictor.py
--rw-rw-r--   0 root         (0) root         (0)     2316 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/serverless/serverless_inference_config.py
--rw-rw-r--   0 root         (0) root         (0)   219824 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/session.py
--rw-rw-r--   0 root         (0) root         (0)     1463 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/session_settings.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/sklearn/
--rw-rw-r--   0 root         (0) root         (0)      875 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/sklearn/__init__.py
--rw-rw-r--   0 root         (0) root         (0)      653 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/sklearn/defaults.py
--rw-rw-r--   0 root         (0) root         (0)    12581 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/sklearn/estimator.py
--rw-rw-r--   0 root         (0) root         (0)    12754 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/sklearn/model.py
--rw-rw-r--   0 root         (0) root         (0)     4893 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/sklearn/processing.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/spark/
--rw-rw-r--   0 root         (0) root         (0)      717 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/spark/__init__.py
--rw-rw-r--   0 root         (0) root         (0)      671 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/spark/defaults.py
--rw-rw-r--   0 root         (0) root         (0)    52078 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/spark/processing.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/sparkml/
--rw-rw-r--   0 root         (0) root         (0)      709 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/sparkml/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     4786 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/sparkml/model.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/
--rw-rw-r--   0 root         (0) root         (0)     1035 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/__init__.py
--rw-rw-r--   0 root         (0) root         (0)      657 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/defaults.py
--rw-rw-r--   0 root         (0) root         (0)    24915 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/estimator.py
--rw-rw-r--   0 root         (0) root         (0)    18684 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/model.py
--rw-rw-r--   0 root         (0) root         (0)     2701 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/processing.py
--rw-rw-r--   0 root         (0) root         (0)      940 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/serving.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/training_compiler/
--rw-rw-r--   0 root         (0) root         (0)        0 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/training_compiler/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     4312 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tensorflow/training_compiler/config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/training_compiler/
--rw-rw-r--   0 root         (0) root         (0)        0 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/training_compiler/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     7072 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/training_compiler/config.py
--rw-rw-r--   0 root         (0) root         (0)    20504 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/transformer.py
--rw-rw-r--   0 root         (0) root         (0)    77234 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/tuner.py
--rw-rw-r--   0 root         (0) root         (0)     2081 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/user_agent.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/utilities/
--rw-rw-r--   0 root         (0) root         (0)        0 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/utilities/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     6555 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/utilities/cache.py
--rw-rw-r--   0 root         (0) root         (0)    24538 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/utils.py
--rw-rw-r--   0 root         (0) root         (0)     4637 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/vpc_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/workflow/
--rw-rw-r--   0 root         (0) root         (0)     1188 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     5095 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/_repack_model.py
--rw-rw-r--   0 root         (0) root         (0)    21053 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/_utils.py
--rw-rw-r--   0 root         (0) root         (0)    52545 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/airflow.py
--rw-rw-r--   0 root         (0) root         (0)     5060 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/callback_step.py
--rw-rw-r--   0 root         (0) root         (0)     7356 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/check_job_config.py
--rw-rw-r--   0 root         (0) root         (0)    22203 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/clarify_check_step.py
--rw-rw-r--   0 root         (0) root         (0)     5375 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/condition_step.py
--rw-rw-r--   0 root         (0) root         (0)    11201 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/conditions.py
--rw-rw-r--   0 root         (0) root         (0)     4704 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/emr_step.py
--rw-rw-r--   0 root         (0) root         (0)     3540 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/entities.py
--rw-rw-r--   0 root         (0) root         (0)     2336 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/execution_variables.py
--rw-rw-r--   0 root         (0) root         (0)     3006 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/fail_step.py
--rw-rw-r--   0 root         (0) root         (0)     3690 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/functions.py
--rw-rw-r--   0 root         (0) root         (0)     5737 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/lambda_step.py
--rw-rw-r--   0 root         (0) root         (0)    12629 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/model_step.py
--rw-rw-r--   0 root         (0) root         (0)     1286 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/parallelism_config.py
--rw-rw-r--   0 root         (0) root         (0)     7065 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/parameters.py
--rw-rw-r--   0 root         (0) root         (0)    25886 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/pipeline.py
--rw-rw-r--   0 root         (0) root         (0)     8330 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/pipeline_context.py
--rw-rw-r--   0 root         (0) root         (0)     3148 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/pipeline_experiment_config.py
--rw-rw-r--   0 root         (0) root         (0)     8233 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/properties.py
--rw-rw-r--   0 root         (0) root         (0)    20621 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/quality_check_step.py
--rw-rw-r--   0 root         (0) root         (0)     8667 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/retry.py
--rw-rw-r--   0 root         (0) root         (0)    18819 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/step_collections.py
--rw-rw-r--   0 root         (0) root         (0)    43310 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/steps.py
--rw-rw-r--   0 root         (0) root         (0)     6751 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/workflow/utilities.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/wrangler/
--rw-rw-r--   0 root         (0) root         (0)        0 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/wrangler/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     7151 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/wrangler/ingestion.py
--rw-rw-r--   0 root         (0) root         (0)     7003 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/wrangler/processing.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker/xgboost/
--rw-rw-r--   0 root         (0) root         (0)      936 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/xgboost/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     1067 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/xgboost/defaults.py
--rw-rw-r--   0 root         (0) root         (0)    13230 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/xgboost/estimator.py
--rw-rw-r--   0 root         (0) root         (0)     8290 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/xgboost/model.py
--rw-rw-r--   0 root         (0) root         (0)     2681 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/xgboost/processing.py
--rw-rw-r--   0 root         (0) root         (0)     1149 2022-06-30 18:50:06.000000 sagemaker-2.98.0/src/sagemaker/xgboost/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker.egg-info/
--rw-r--r--   0 root         (0) root         (0)    12375 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    11329 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       99 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)      847 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       10 2022-07-05 18:31:47.000000 sagemaker-2.98.0/src/sagemaker.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/
+-rw-rw-r--   0 root         (0) root         (0)    10118 2022-07-07 23:43:14.000000 sagemaker-2.99.0/LICENSE.txt
+-rw-rw-r--   0 root         (0) root         (0)      248 2022-07-07 23:43:14.000000 sagemaker-2.99.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)    12375 2022-07-08 05:22:37.000000 sagemaker-2.99.0/PKG-INFO
+-rw-rw-r--   0 root         (0) root         (0)     9632 2022-07-07 23:43:14.000000 sagemaker-2.99.0/README.rst
+-rw-rw-r--   0 root         (0) root         (0)        7 2022-07-08 05:22:37.000000 sagemaker-2.99.0/VERSION
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/requirements/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/requirements/extras/
+-rw-rw-r--   0 root         (0) root         (0)       67 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/extras/local_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       13 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/extras/scipy_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)      373 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/extras/test_requirements.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/requirements/tox/
+-rw-rw-r--   0 root         (0) root         (0)       30 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/doc8_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       18 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/docstyle_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       42 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/flake8_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       12 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/mypy_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       18 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/pydocstyle_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       29 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/pylint_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       31 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/spelling_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)       13 2022-07-07 23:43:14.000000 sagemaker-2.99.0/requirements/tox/twine_requirements.txt
+-rw-rw-r--   0 root         (0) root         (0)      204 2022-07-08 05:22:37.000000 sagemaker-2.99.0/setup.cfg
+-rw-rw-r--   0 root         (0) root         (0)     3368 2022-07-07 23:43:14.000000 sagemaker-2.99.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/
+-rw-rw-r--   0 root         (0) root         (0)     3003 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     3221 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/_studio.py
+-rw-rw-r--   0 root         (0) root         (0)    25505 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/algorithm.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/amazon/
+-rw-rw-r--   0 root         (0) root         (0)      560 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    20009 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/amazon_estimator.py
+-rw-rw-r--   0 root         (0) root         (0)     9690 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/common.py
+-rw-rw-r--   0 root         (0) root         (0)    16678 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/factorization_machines.py
+-rw-rw-r--   0 root         (0) root         (0)     3448 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/hyperparameter.py
+-rw-rw-r--   0 root         (0) root         (0)    11546 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/ipinsights.py
+-rw-rw-r--   0 root         (0) root         (0)    12755 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/kmeans.py
+-rw-rw-r--   0 root         (0) root         (0)    12301 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/knn.py
+-rw-rw-r--   0 root         (0) root         (0)    11182 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/lda.py
+-rw-rw-r--   0 root         (0) root         (0)    25618 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/linear_learner.py
+-rw-rw-r--   0 root         (0) root         (0)    12708 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/ntm.py
+-rw-rw-r--   0 root         (0) root         (0)    16876 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/object2vec.py
+-rw-rw-r--   0 root         (0) root         (0)    11849 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/pca.py
+-rw-rw-r--   0 root         (0) root         (0)    10874 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/randomcutforest.py
+-rw-rw-r--   0 root         (0) root         (0)    25553 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/record_pb2.py
+-rw-rw-r--   0 root         (0) root         (0)     1426 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/amazon/validation.py
+-rw-rw-r--   0 root         (0) root         (0)    30165 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/analytics.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/apiutils/
+-rw-rw-r--   0 root         (0) root         (0)      629 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/apiutils/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     8541 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/apiutils/_base_types.py
+-rw-rw-r--   0 root         (0) root         (0)     5117 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/apiutils/_boto_functions.py
+-rw-rw-r--   0 root         (0) root         (0)     1136 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/apiutils/_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/async_inference/
+-rw-rw-r--   0 root         (0) root         (0)      946 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/async_inference/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     3901 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/async_inference/async_inference_config.py
+-rw-rw-r--   0 root         (0) root         (0)     3867 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/async_inference/async_inference_response.py
+-rw-rw-r--   0 root         (0) root         (0)     1653 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/async_inference/waiter_config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/automl/
+-rw-rw-r--   0 root         (0) root         (0)      560 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/automl/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    33849 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/automl/automl.py
+-rw-rw-r--   0 root         (0) root         (0)    14365 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/automl/candidate_estimator.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/chainer/
+-rw-rw-r--   0 root         (0) root         (0)      771 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/chainer/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)      657 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/chainer/defaults.py
+-rw-rw-r--   0 root         (0) root         (0)    12725 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/chainer/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)     9171 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/chainer/model.py
+-rw-rw-r--   0 root         (0) root         (0)    60066 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/clarify.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/cli/
+-rw-rw-r--   0 root         (0) root         (0)      640 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/
+-rw-rw-r--   0 root         (0) root         (0)      679 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/
+-rw-rw-r--   0 root         (0) root         (0)      690 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     6468 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/ast_transformer.py
+-rw-rw-r--   0 root         (0) root         (0)     7848 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/files.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/
+-rw-rw-r--   0 root         (0) root         (0)      923 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     3662 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/airflow.py
+-rw-rw-r--   0 root         (0) root         (0)     2482 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/deprecated_params.py
+-rw-rw-r--   0 root         (0) root         (0)     6892 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/framework_version.py
+-rw-rw-r--   0 root         (0) root         (0)     4954 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/image_uris.py
+-rw-rw-r--   0 root         (0) root         (0)     4261 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/matching.py
+-rw-rw-r--   0 root         (0) root         (0)     1245 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/modifier.py
+-rw-rw-r--   0 root         (0) root         (0)     1870 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/parsing.py
+-rw-rw-r--   0 root         (0) root         (0)     4655 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/predictors.py
+-rw-rw-r--   0 root         (0) root         (0)    11490 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/renamed_params.py
+-rw-rw-r--   0 root         (0) root         (0)    17894 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/serde.py
+-rw-rw-r--   0 root         (0) root         (0)     8776 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/tf_legacy_mode.py
+-rw-rw-r--   0 root         (0) root         (0)     5223 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/tfs.py
+-rw-rw-r--   0 root         (0) root         (0)     6393 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/training_input.py
+-rw-rw-r--   0 root         (0) root         (0)     4094 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/training_params.py
+-rw-rw-r--   0 root         (0) root         (0)     2933 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/sagemaker_upgrade_v2.py
+-rw-rw-r--   0 root         (0) root         (0)     9491 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/cli/framework_upgrade.py
+-rw-rw-r--   0 root         (0) root         (0)      925 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/content_types.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/dataset_definition/
+-rw-rw-r--   0 root         (0) root         (0)      845 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/dataset_definition/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     9158 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/dataset_definition/inputs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/debugger/
+-rw-rw-r--   0 root         (0) root         (0)     1417 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/debugger/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    39259 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/debugger/debugger.py
+-rw-rw-r--   0 root         (0) root         (0)    12353 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/debugger/framework_profile.py
+-rw-rw-r--   0 root         (0) root         (0)    17955 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/debugger/metrics_config.py
+-rw-rw-r--   0 root         (0) root         (0)     4685 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/debugger/profiler_config.py
+-rw-rw-r--   0 root         (0) root         (0)     1481 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/debugger/profiler_constants.py
+-rw-rw-r--   0 root         (0) root         (0)     4428 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/debugger/utils.py
+-rw-rw-r--   0 root         (0) root         (0)     6507 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/deprecations.py
+-rw-rw-r--   0 root         (0) root         (0)    11915 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/deserializers.py
+-rw-rw-r--   0 root         (0) root         (0)     5140 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/drift_check_baselines.py
+-rw-rw-r--   0 root         (0) root         (0)     1967 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/environment_variables.py
+-rw-rw-r--   0 root         (0) root         (0)   159849 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)     2365 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/exceptions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/feature_store/
+-rw-rw-r--   0 root         (0) root         (0)      560 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/feature_store/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     4066 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/feature_store/feature_definition.py
+-rw-rw-r--   0 root         (0) root         (0)    28436 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/feature_store/feature_group.py
+-rw-rw-r--   0 root         (0) root         (0)     6319 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/feature_store/inputs.py
+-rw-rw-r--   0 root         (0) root         (0)    30371 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/fw_utils.py
+-rw-rw-r--   0 root         (0) root         (0)    15141 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/git_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/huggingface/
+-rw-rw-r--   0 root         (0) root         (0)      967 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/huggingface/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    16429 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/huggingface/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)    22956 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/huggingface/model.py
+-rw-rw-r--   0 root         (0) root         (0)     5173 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/huggingface/processing.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/huggingface/training_compiler/
+-rw-rw-r--   0 root         (0) root         (0)        0 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/huggingface/training_compiler/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     4129 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/huggingface/training_compiler/config.py
+-rw-rw-r--   0 root         (0) root         (0)     4730 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/hyperparameters.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/
+-rw-rw-r--   0 root         (0) root         (0)    11735 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/autogluon.json
+-rw-rw-r--   0 root         (0) root         (0)     1350 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/blazingtext.json
+-rw-rw-r--   0 root         (0) root         (0)     4062 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/chainer.json
+-rw-rw-r--   0 root         (0) root         (0)     1430 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/clarify.json
+-rw-rw-r--   0 root         (0) root         (0)     2728 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/coach-mxnet.json
+-rw-rw-r--   0 root         (0) root         (0)     7536 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/coach-tensorflow.json
+-rw-rw-r--   0 root         (0) root         (0)     1060 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/data-wrangler.json
+-rw-rw-r--   0 root         (0) root         (0)     1306 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/debugger.json
+-rw-rw-r--   0 root         (0) root         (0)     1361 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/factorization-machines.json
+-rw-rw-r--   0 root         (0) root         (0)     1357 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/forecasting-deepar.json
+-rw-rw-r--   0 root         (0) root         (0)     1963 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/huggingface-neuron.json
+-rw-rw-r--   0 root         (0) root         (0)     4516 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/huggingface-training-compiler.json
+-rw-rw-r--   0 root         (0) root         (0)    55091 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/huggingface.json
+-rw-rw-r--   0 root         (0) root         (0)     1307 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/image-classification-neo.json
+-rw-rw-r--   0 root         (0) root         (0)     1359 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/image-classification.json
+-rw-rw-r--   0 root         (0) root         (0)     2660 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/inferentia-mxnet.json
+-rw-rw-r--   0 root         (0) root         (0)     3928 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/inferentia-pytorch.json
+-rw-rw-r--   0 root         (0) root         (0)     2673 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/inferentia-tensorflow.json
+-rw-rw-r--   0 root         (0) root         (0)     1349 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/ipinsights.json
+-rw-rw-r--   0 root         (0) root         (0)     1345 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/kmeans.json
+-rw-rw-r--   0 root         (0) root         (0)     1342 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/knn.json
+-rw-rw-r--   0 root         (0) root         (0)      877 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/lda.json
+-rw-rw-r--   0 root         (0) root         (0)     1353 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/linear-learner.json
+-rw-rw-r--   0 root         (0) root         (0)     1261 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/model-monitor.json
+-rw-rw-r--   0 root         (0) root         (0)    42939 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/mxnet.json
+-rw-rw-r--   0 root         (0) root         (0)     1687 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/neo-mxnet.json
+-rw-rw-r--   0 root         (0) root         (0)     6800 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/neo-pytorch.json
+-rw-rw-r--   0 root         (0) root         (0)     3111 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/neo-tensorflow.json
+-rw-rw-r--   0 root         (0) root         (0)     1342 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/ntm.json
+-rw-rw-r--   0 root         (0) root         (0)     1355 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/object-detection.json
+-rw-rw-r--   0 root         (0) root         (0)     1349 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/object2vec.json
+-rw-rw-r--   0 root         (0) root         (0)     1342 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/pca.json
+-rw-rw-r--   0 root         (0) root         (0)    50643 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/pytorch.json
+-rw-rw-r--   0 root         (0) root         (0)     1354 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/randomcutforest.json
+-rw-rw-r--   0 root         (0) root         (0)     1730 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/ray-pytorch.json
+-rw-rw-r--   0 root         (0) root         (0)     7826 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/ray-tensorflow.json
+-rw-rw-r--   0 root         (0) root         (0)     1360 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/semantic-segmentation.json
+-rw-rw-r--   0 root         (0) root         (0)     1346 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/seq2seq.json
+-rw-rw-r--   0 root         (0) root         (0)     4098 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/sklearn.json
+-rw-rw-r--   0 root         (0) root         (0)     4262 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/spark.json
+-rw-rw-r--   0 root         (0) root         (0)     2553 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/sparkml-serving.json
+-rw-rw-r--   0 root         (0) root         (0)   129904 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/tensorflow.json
+-rw-rw-r--   0 root         (0) root         (0)      857 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/vw.json
+-rw-rw-r--   0 root         (0) root         (0)     1294 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/xgboost-neo.json
+-rw-rw-r--   0 root         (0) root         (0)    10665 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uri_config/xgboost.json
+-rw-rw-r--   0 root         (0) root         (0)    21478 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/image_uris.py
+-rw-rw-r--   0 root         (0) root         (0)     9531 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/inputs.py
+-rw-rw-r--   0 root         (0) root         (0)     2522 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/instance_group.py
+-rw-rw-r--   0 root         (0) root         (0)    12032 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/job.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/
+-rw-rw-r--   0 root         (0) root         (0)        0 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     7181 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/accessors.py
+-rw-rw-r--   0 root         (0) root         (0)    15343 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/artifacts.py
+-rw-rw-r--   0 root         (0) root         (0)    15917 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/cache.py
+-rw-rw-r--   0 root         (0) root         (0)     4834 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/constants.py
+-rw-rw-r--   0 root         (0) root         (0)     2292 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/enums.py
+-rw-rw-r--   0 root         (0) root         (0)     4758 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/exceptions.py
+-rw-rw-r--   0 root         (0) root         (0)    16623 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/filters.py
+-rw-rw-r--   0 root         (0) root         (0)    17765 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/notebook_utils.py
+-rw-rw-r--   0 root         (0) root         (0)      948 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/parameters.py
+-rw-rw-r--   0 root         (0) root         (0)    14964 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/types.py
+-rw-rw-r--   0 root         (0) root         (0)    15366 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/utils.py
+-rw-rw-r--   0 root         (0) root         (0)    10388 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/jumpstart/validators.py
+-rw-rw-r--   0 root         (0) root         (0)    10629 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lambda_helper.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/lineage/
+-rw-rw-r--   0 root         (0) root         (0)      589 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     7032 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/_api_types.py
+-rw-rw-r--   0 root         (0) root         (0)     2110 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/_utils.py
+-rw-rw-r--   0 root         (0) root         (0)    12422 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/action.py
+-rw-rw-r--   0 root         (0) root         (0)    24348 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/artifact.py
+-rw-rw-r--   0 root         (0) root         (0)     7024 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/association.py
+-rw-rw-r--   0 root         (0) root         (0)    18902 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/context.py
+-rw-rw-r--   0 root         (0) root         (0)     7655 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/lineage_trial_component.py
+-rw-rw-r--   0 root         (0) root         (0)    13330 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/query.py
+-rw-rw-r--   0 root         (0) root         (0)    13236 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/lineage/visualizer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/local/
+-rw-rw-r--   0 root         (0) root         (0)      766 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/local/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    12858 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/local/data.py
+-rw-rw-r--   0 root         (0) root         (0)    24836 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/local/entities.py
+-rw-rw-r--   0 root         (0) root         (0)    42493 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/local/image.py
+-rw-rw-r--   0 root         (0) root         (0)    21169 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/local/local_session.py
+-rw-rw-r--   0 root         (0) root         (0)     4881 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/local/utils.py
+-rw-rw-r--   0 root         (0) root         (0)     5916 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/logs.py
+-rw-rw-r--   0 root         (0) root         (0)     1951 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/metadata_properties.py
+-rw-rw-r--   0 root         (0) root         (0)    72929 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model.py
+-rw-rw-r--   0 root         (0) root         (0)     6417 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_metrics.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/
+-rw-rw-r--   0 root         (0) root         (0)     2310 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    60563 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/clarify_model_monitoring.py
+-rw-rw-r--   0 root         (0) root         (0)     2805 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/cron_expression_generator.py
+-rw-rw-r--   0 root         (0) root         (0)     4771 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/data_capture_config.py
+-rw-rw-r--   0 root         (0) root         (0)     2311 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/dataset_format.py
+-rw-rw-r--   0 root         (0) root         (0)   150925 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/model_monitoring.py
+-rw-rw-r--   0 root         (0) root         (0)    19947 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_monitor/monitoring_files.py
+-rw-rw-r--   0 root         (0) root         (0)     3100 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/model_uris.py
+-rw-rw-r--   0 root         (0) root         (0)    15258 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/multidatamodel.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/mxnet/
+-rw-rw-r--   0 root         (0) root         (0)      868 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/mxnet/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)      657 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/mxnet/defaults.py
+-rw-rw-r--   0 root         (0) root         (0)    14635 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/mxnet/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)    15129 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/mxnet/model.py
+-rw-rw-r--   0 root         (0) root         (0)     2674 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/mxnet/processing.py
+-rw-rw-r--   0 root         (0) root         (0)     3121 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/network.py
+-rw-rw-r--   0 root         (0) root         (0)     5910 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/parameter.py
+-rw-rw-r--   0 root         (0) root         (0)    20653 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/pipeline.py
+-rw-rw-r--   0 root         (0) root         (0)    23439 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/predictor.py
+-rw-rw-r--   0 root         (0) root         (0)    15745 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/predictor_async.py
+-rw-rw-r--   0 root         (0) root         (0)    82554 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/processing.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/pytorch/
+-rw-rw-r--   0 root         (0) root         (0)      870 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/pytorch/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)      657 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/pytorch/defaults.py
+-rw-rw-r--   0 root         (0) root         (0)    14537 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/pytorch/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)    15201 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/pytorch/model.py
+-rw-rw-r--   0 root         (0) root         (0)     2682 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/pytorch/processing.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/rl/
+-rw-rw-r--   0 root         (0) root         (0)      765 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/rl/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)    19305 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/rl/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)     7193 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/s3.py
+-rw-rw-r--   0 root         (0) root         (0)     2960 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/script_uris.py
+-rw-rw-r--   0 root         (0) root         (0)    13190 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/serializers.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/serverless/
+-rw-rw-r--   0 root         (0) root         (0)      877 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/serverless/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)      913 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/serverless/model.py
+-rw-rw-r--   0 root         (0) root         (0)      911 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/serverless/predictor.py
+-rw-rw-r--   0 root         (0) root         (0)     2316 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/serverless/serverless_inference_config.py
+-rw-rw-r--   0 root         (0) root         (0)   221483 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/session.py
+-rw-rw-r--   0 root         (0) root         (0)     1463 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/session_settings.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/sklearn/
+-rw-rw-r--   0 root         (0) root         (0)      875 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/sklearn/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)      653 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/sklearn/defaults.py
+-rw-rw-r--   0 root         (0) root         (0)    12581 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/sklearn/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)    14097 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/sklearn/model.py
+-rw-rw-r--   0 root         (0) root         (0)     4893 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/sklearn/processing.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/spark/
+-rw-rw-r--   0 root         (0) root         (0)      717 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/spark/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)      671 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/spark/defaults.py
+-rw-rw-r--   0 root         (0) root         (0)    52078 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/spark/processing.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/sparkml/
+-rw-rw-r--   0 root         (0) root         (0)      709 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/sparkml/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     4786 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/sparkml/model.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/
+-rw-rw-r--   0 root         (0) root         (0)     1035 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)      657 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/defaults.py
+-rw-rw-r--   0 root         (0) root         (0)    24728 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)    20027 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/model.py
+-rw-rw-r--   0 root         (0) root         (0)     2701 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/processing.py
+-rw-rw-r--   0 root         (0) root         (0)      940 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/serving.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/training_compiler/
+-rw-rw-r--   0 root         (0) root         (0)        0 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/training_compiler/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     4312 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tensorflow/training_compiler/config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/training_compiler/
+-rw-rw-r--   0 root         (0) root         (0)        0 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/training_compiler/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     7072 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/training_compiler/config.py
+-rw-rw-r--   0 root         (0) root         (0)    21613 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/transformer.py
+-rw-rw-r--   0 root         (0) root         (0)    78078 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/tuner.py
+-rw-rw-r--   0 root         (0) root         (0)     2081 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/user_agent.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/utilities/
+-rw-rw-r--   0 root         (0) root         (0)        0 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/utilities/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     6555 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/utilities/cache.py
+-rw-rw-r--   0 root         (0) root         (0)    26582 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/utils.py
+-rw-rw-r--   0 root         (0) root         (0)     4637 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/vpc_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/workflow/
+-rw-rw-r--   0 root         (0) root         (0)     1188 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     5095 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/_repack_model.py
+-rw-rw-r--   0 root         (0) root         (0)    21665 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/_utils.py
+-rw-rw-r--   0 root         (0) root         (0)    52545 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/airflow.py
+-rw-rw-r--   0 root         (0) root         (0)     5060 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/callback_step.py
+-rw-rw-r--   0 root         (0) root         (0)     7356 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/check_job_config.py
+-rw-rw-r--   0 root         (0) root         (0)    22203 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/clarify_check_step.py
+-rw-rw-r--   0 root         (0) root         (0)     5375 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/condition_step.py
+-rw-rw-r--   0 root         (0) root         (0)    11201 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/conditions.py
+-rw-rw-r--   0 root         (0) root         (0)     4704 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/emr_step.py
+-rw-rw-r--   0 root         (0) root         (0)     3540 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/entities.py
+-rw-rw-r--   0 root         (0) root         (0)     2336 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/execution_variables.py
+-rw-rw-r--   0 root         (0) root         (0)     3006 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/fail_step.py
+-rw-rw-r--   0 root         (0) root         (0)     3690 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/functions.py
+-rw-rw-r--   0 root         (0) root         (0)     5737 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/lambda_step.py
+-rw-rw-r--   0 root         (0) root         (0)    12629 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/model_step.py
+-rw-rw-r--   0 root         (0) root         (0)     1286 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/parallelism_config.py
+-rw-rw-r--   0 root         (0) root         (0)     7065 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/parameters.py
+-rw-rw-r--   0 root         (0) root         (0)    25886 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/pipeline.py
+-rw-rw-r--   0 root         (0) root         (0)     8330 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/pipeline_context.py
+-rw-rw-r--   0 root         (0) root         (0)     3148 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/pipeline_experiment_config.py
+-rw-rw-r--   0 root         (0) root         (0)     8233 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/properties.py
+-rw-rw-r--   0 root         (0) root         (0)    20621 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/quality_check_step.py
+-rw-rw-r--   0 root         (0) root         (0)     8667 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/retry.py
+-rw-rw-r--   0 root         (0) root         (0)    20368 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/step_collections.py
+-rw-rw-r--   0 root         (0) root         (0)    43310 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/steps.py
+-rw-rw-r--   0 root         (0) root         (0)     6751 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/workflow/utilities.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/wrangler/
+-rw-rw-r--   0 root         (0) root         (0)        0 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/wrangler/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     7151 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/wrangler/ingestion.py
+-rw-rw-r--   0 root         (0) root         (0)     7003 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/wrangler/processing.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker/xgboost/
+-rw-rw-r--   0 root         (0) root         (0)      936 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/xgboost/__init__.py
+-rw-rw-r--   0 root         (0) root         (0)     1067 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/xgboost/defaults.py
+-rw-rw-r--   0 root         (0) root         (0)    13230 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/xgboost/estimator.py
+-rw-rw-r--   0 root         (0) root         (0)     8290 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/xgboost/model.py
+-rw-rw-r--   0 root         (0) root         (0)     2681 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/xgboost/processing.py
+-rw-rw-r--   0 root         (0) root         (0)     1149 2022-07-07 23:43:14.000000 sagemaker-2.99.0/src/sagemaker/xgboost/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    12375 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    11361 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       99 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)      851 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       10 2022-07-08 05:22:37.000000 sagemaker-2.99.0/src/sagemaker.egg-info/top_level.txt
```

### Comparing `sagemaker-2.98.0/LICENSE.txt` & `sagemaker-2.99.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/PKG-INFO` & `sagemaker-2.99.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemaker
-Version: 2.98.0
+Version: 2.99.0
 Summary: Open source library for training and deploying models on Amazon SageMaker.
 Home-page: https://github.com/aws/sagemaker-python-sdk/
 Author: Amazon Web Services
 License: Apache License 2.0
 Description: .. image:: https://github.com/aws/sagemaker-python-sdk/raw/master/branding/icon/sagemaker-banner.png
             :height: 100px
             :alt: SageMaker
```

### Comparing `sagemaker-2.98.0/README.rst` & `sagemaker-2.99.0/README.rst`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/setup.py` & `sagemaker-2.99.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -43,15 +43,15 @@
     with open(os.path.abspath(filename)) as fp:
         deps = [line.strip() for line in fp.readlines()]
     return deps
 
 
 # Declare minimal set for installation
 required_packages = [
-    "attrs==20.3.0",
+    "attrs>=20.3.0,<22",
     "boto3>=1.20.21,<2.0",
     "google-pasta",
     "numpy>=1.9.0,<2.0",
     "protobuf>=3.1,<4.0",
     "protobuf3-to-dict>=0.1.5,<1.0",
     "smdebug_rulesconfig==1.0.1",
     "importlib-metadata>=1.4.0,<5.0",
```

### Comparing `sagemaker-2.98.0/src/sagemaker/__init__.py` & `sagemaker-2.99.0/src/sagemaker/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/_studio.py` & `sagemaker-2.99.0/src/sagemaker/_studio.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/algorithm.py` & `sagemaker-2.99.0/src/sagemaker/algorithm.py`

 * *Files 0% similar despite different names*

```diff
@@ -143,27 +143,27 @@
                 available (default: ``None``).
             **kwargs: Additional kwargs. This is unused. It's only added for AlgorithmEstimator
                 to ignore the irrelevant arguments.
         """
         self.algorithm_arn = algorithm_arn
         super(AlgorithmEstimator, self).__init__(
             role,
-            instance_count,
-            instance_type,
-            volume_size,
-            volume_kms_key,
-            max_run,
-            input_mode,
-            output_path,
-            output_kms_key,
-            base_job_name,
-            sagemaker_session,
-            tags,
-            subnets,
-            security_group_ids,
+            instance_count=instance_count,
+            instance_type=instance_type,
+            volume_size=volume_size,
+            volume_kms_key=volume_kms_key,
+            max_run=max_run,
+            input_mode=input_mode,
+            output_path=output_path,
+            output_kms_key=output_kms_key,
+            base_job_name=base_job_name,
+            sagemaker_session=sagemaker_session,
+            tags=tags,
+            subnets=subnets,
+            security_group_ids=security_group_ids,
             model_uri=model_uri,
             model_channel_name=model_channel_name,
             metric_definitions=metric_definitions,
             encrypt_inter_container_traffic=encrypt_inter_container_traffic,
             use_spot_instances=use_spot_instances,
             max_wait=max_wait,
         )
```

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/__init__.py` & `sagemaker-2.99.0/src/sagemaker/amazon/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/amazon_estimator.py` & `sagemaker-2.99.0/src/sagemaker/amazon/amazon_estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/common.py` & `sagemaker-2.99.0/src/sagemaker/amazon/common.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/factorization_machines.py` & `sagemaker-2.99.0/src/sagemaker/amazon/factorization_machines.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/hyperparameter.py` & `sagemaker-2.99.0/src/sagemaker/amazon/hyperparameter.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/ipinsights.py` & `sagemaker-2.99.0/src/sagemaker/amazon/ipinsights.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/kmeans.py` & `sagemaker-2.99.0/src/sagemaker/amazon/kmeans.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/knn.py` & `sagemaker-2.99.0/src/sagemaker/amazon/knn.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/lda.py` & `sagemaker-2.99.0/src/sagemaker/amazon/lda.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/linear_learner.py` & `sagemaker-2.99.0/src/sagemaker/amazon/linear_learner.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/ntm.py` & `sagemaker-2.99.0/src/sagemaker/amazon/ntm.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/object2vec.py` & `sagemaker-2.99.0/src/sagemaker/amazon/object2vec.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/pca.py` & `sagemaker-2.99.0/src/sagemaker/amazon/pca.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/randomcutforest.py` & `sagemaker-2.99.0/src/sagemaker/amazon/randomcutforest.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/record_pb2.py` & `sagemaker-2.99.0/src/sagemaker/amazon/record_pb2.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/amazon/validation.py` & `sagemaker-2.99.0/src/sagemaker/amazon/validation.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/analytics.py` & `sagemaker-2.99.0/src/sagemaker/analytics.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/apiutils/__init__.py` & `sagemaker-2.99.0/src/sagemaker/apiutils/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/apiutils/_base_types.py` & `sagemaker-2.99.0/src/sagemaker/apiutils/_base_types.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/apiutils/_boto_functions.py` & `sagemaker-2.99.0/src/sagemaker/apiutils/_boto_functions.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/apiutils/_utils.py` & `sagemaker-2.99.0/src/sagemaker/apiutils/_utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/async_inference/__init__.py` & `sagemaker-2.99.0/src/sagemaker/async_inference/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/async_inference/async_inference_config.py` & `sagemaker-2.99.0/src/sagemaker/async_inference/async_inference_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/async_inference/async_inference_response.py` & `sagemaker-2.99.0/src/sagemaker/async_inference/async_inference_response.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/async_inference/waiter_config.py` & `sagemaker-2.99.0/src/sagemaker/async_inference/waiter_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/automl/__init__.py` & `sagemaker-2.99.0/src/sagemaker/automl/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/automl/automl.py` & `sagemaker-2.99.0/src/sagemaker/automl/automl.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/automl/candidate_estimator.py` & `sagemaker-2.99.0/src/sagemaker/automl/candidate_estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/chainer/__init__.py` & `sagemaker-2.99.0/src/sagemaker/chainer/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/chainer/defaults.py` & `sagemaker-2.99.0/src/sagemaker/chainer/defaults.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/chainer/estimator.py` & `sagemaker-2.99.0/src/sagemaker/chainer/estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/chainer/model.py` & `sagemaker-2.99.0/src/sagemaker/chainer/model.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/clarify.py` & `sagemaker-2.99.0/src/sagemaker/clarify.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/__init__.py` & `sagemaker-2.99.0/src/sagemaker/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/__init__.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/__init__.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/ast_transformer.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/ast_transformer.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/files.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/files.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/__init__.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/airflow.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/airflow.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/deprecated_params.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/deprecated_params.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/framework_version.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/framework_version.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/image_uris.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/image_uris.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/matching.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/matching.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/modifier.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/modifier.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/parsing.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/parsing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/predictors.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/predictors.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/renamed_params.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/renamed_params.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/serde.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/serde.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/tf_legacy_mode.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/tf_legacy_mode.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/tfs.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/tfs.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/training_input.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/training_input.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/modifiers/training_params.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/modifiers/training_params.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/compatibility/v2/sagemaker_upgrade_v2.py` & `sagemaker-2.99.0/src/sagemaker/cli/compatibility/v2/sagemaker_upgrade_v2.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/cli/framework_upgrade.py` & `sagemaker-2.99.0/src/sagemaker/cli/framework_upgrade.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/content_types.py` & `sagemaker-2.99.0/src/sagemaker/content_types.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/dataset_definition/__init__.py` & `sagemaker-2.99.0/src/sagemaker/dataset_definition/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/dataset_definition/inputs.py` & `sagemaker-2.99.0/src/sagemaker/dataset_definition/inputs.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/debugger/__init__.py` & `sagemaker-2.99.0/src/sagemaker/debugger/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/debugger/debugger.py` & `sagemaker-2.99.0/src/sagemaker/debugger/debugger.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/debugger/framework_profile.py` & `sagemaker-2.99.0/src/sagemaker/debugger/framework_profile.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/debugger/metrics_config.py` & `sagemaker-2.99.0/src/sagemaker/debugger/metrics_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/debugger/profiler_config.py` & `sagemaker-2.99.0/src/sagemaker/debugger/profiler_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/debugger/profiler_constants.py` & `sagemaker-2.99.0/src/sagemaker/debugger/profiler_constants.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/debugger/utils.py` & `sagemaker-2.99.0/src/sagemaker/debugger/utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/deprecations.py` & `sagemaker-2.99.0/src/sagemaker/deprecations.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/deserializers.py` & `sagemaker-2.99.0/src/sagemaker/deserializers.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/drift_check_baselines.py` & `sagemaker-2.99.0/src/sagemaker/drift_check_baselines.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/environment_variables.py` & `sagemaker-2.99.0/src/sagemaker/environment_variables.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/estimator.py` & `sagemaker-2.99.0/src/sagemaker/estimator.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,17 +12,18 @@
 # language governing permissions and limitations under the License.
 """Placeholder docstring"""
 from __future__ import absolute_import, print_function
 
 import json
 import logging
 import os
+import re
 import uuid
 from abc import ABCMeta, abstractmethod
-from typing import Any, Dict
+from typing import Any, Dict, Union, Optional, List
 
 from six import string_types, with_metaclass
 from six.moves.urllib.parse import urlparse
 
 import sagemaker
 from sagemaker import git_utils, image_uris, vpc_utils
 from sagemaker.analytics import TrainingJobAnalytics
@@ -32,25 +33,26 @@
     FrameworkProfile,
     ProfilerConfig,
     ProfilerRule,
     Rule,
     TensorBoardOutputConfig,
     get_default_profiler_rule,
     get_rule_container_image_uri,
+    RuleBase,
 )
 from sagemaker.deprecations import removed_function, removed_kwargs, renamed_kwargs
 from sagemaker.fw_utils import (
     UploadedCode,
     _region_supports_debugger,
     _region_supports_profiler,
     get_mp_parameters,
     tar_and_upload_dir,
     validate_source_dir,
 )
-from sagemaker.inputs import TrainingInput
+from sagemaker.inputs import TrainingInput, FileSystemInput
 from sagemaker.job import _Job
 from sagemaker.jumpstart.utils import (
     add_jumpstart_tags,
     get_jumpstart_base_name_if_jumpstart_model,
     update_inference_tags_with_jumpstart_training_tags,
 )
 from sagemaker.local import LocalSession
@@ -71,14 +73,15 @@
     base_from_name,
     base_name_from_image,
     build_dict,
     get_config_value,
     name_from_base,
 )
 from sagemaker.workflow import is_pipeline_variable
+from sagemaker.workflow.entities import PipelineVariable
 from sagemaker.workflow.pipeline_context import (
     PipelineSession,
     runnable_by_pipeline,
 )
 
 logger = logging.getLogger(__name__)
 
@@ -101,66 +104,68 @@
     MPI_NUM_PROCESSES_PER_HOST = "sagemaker_mpi_num_of_processes_per_host"
     MPI_CUSTOM_MPI_OPTIONS = "sagemaker_mpi_custom_mpi_options"
     SM_DDP_CUSTOM_MPI_OPTIONS = "sagemaker_distributed_dataparallel_custom_mpi_options"
     CONTAINER_CODE_CHANNEL_SOURCEDIR_PATH = "/opt/ml/input/data/code/sourcedir.tar.gz"
 
     def __init__(
         self,
-        role,
-        instance_count=None,
-        instance_type=None,
-        volume_size=30,
-        volume_kms_key=None,
-        max_run=24 * 60 * 60,
-        input_mode="File",
-        output_path=None,
-        output_kms_key=None,
-        base_job_name=None,
-        sagemaker_session=None,
-        tags=None,
-        subnets=None,
-        security_group_ids=None,
-        model_uri=None,
-        model_channel_name="model",
-        metric_definitions=None,
-        encrypt_inter_container_traffic=False,
-        use_spot_instances=False,
-        max_wait=None,
-        checkpoint_s3_uri=None,
-        checkpoint_local_path=None,
-        rules=None,
-        debugger_hook_config=None,
-        tensorboard_output_config=None,
-        enable_sagemaker_metrics=None,
-        enable_network_isolation=False,
-        profiler_config=None,
-        disable_profiler=False,
-        environment=None,
-        max_retry_attempts=None,
-        source_dir=None,
-        git_config=None,
-        hyperparameters=None,
-        container_log_level=logging.INFO,
-        code_location=None,
-        entry_point=None,
-        dependencies=None,
+        role: str,
+        instance_count: Optional[Union[int, PipelineVariable]] = None,
+        instance_type: Optional[Union[str, PipelineVariable]] = None,
+        volume_size: Union[int, PipelineVariable] = 30,
+        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        max_run: Union[int, PipelineVariable] = 24 * 60 * 60,
+        input_mode: Union[str, PipelineVariable] = "File",
+        output_path: Optional[Union[str, PipelineVariable]] = None,
+        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        base_job_name: Optional[str] = None,
+        sagemaker_session: Optional[Session] = None,
+        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        subnets: Optional[List[Union[str, PipelineVariable]]] = None,
+        security_group_ids: Optional[List[Union[str, PipelineVariable]]] = None,
+        model_uri: Optional[str] = None,
+        model_channel_name: Union[str, PipelineVariable] = "model",
+        metric_definitions: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        encrypt_inter_container_traffic: Union[bool, PipelineVariable] = False,
+        use_spot_instances: Union[bool, PipelineVariable] = False,
+        max_wait: Optional[Union[int, PipelineVariable]] = None,
+        checkpoint_s3_uri: Optional[Union[str, PipelineVariable]] = None,
+        checkpoint_local_path: Optional[Union[str, PipelineVariable]] = None,
+        rules: Optional[List[RuleBase]] = None,
+        debugger_hook_config: Optional[Union[bool, DebuggerHookConfig]] = None,
+        tensorboard_output_config: Optional[TensorBoardOutputConfig] = None,
+        enable_sagemaker_metrics: Optional[Union[bool, PipelineVariable]] = None,
+        enable_network_isolation: Union[bool, PipelineVariable] = False,
+        profiler_config: Optional[ProfilerConfig] = None,
+        disable_profiler: bool = False,
+        environment: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        max_retry_attempts: Optional[Union[int, PipelineVariable]] = None,
+        source_dir: Optional[str] = None,
+        git_config: Optional[Dict[str, str]] = None,
+        hyperparameters: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        container_log_level: Union[int, PipelineVariable] = logging.INFO,
+        code_location: Optional[str] = None,
+        entry_point: Optional[str] = None,
+        dependencies: Optional[List[Union[str]]] = None,
+        instance_groups: Optional[Dict[str, Union[str, int]]] = None,
         **kwargs,
     ):
         """Initialize an ``EstimatorBase`` instance.
 
         Args:
             role (str): An AWS IAM role (either name or full ARN). The Amazon
                 SageMaker training jobs and APIs that create Amazon SageMaker
                 endpoints use this role to access training data and model
                 artifacts. After the endpoint is created, the inference code
                 might use the IAM role, if it needs to access an AWS resource.
             instance_count (int): Number of Amazon EC2 instances to use
-                for training.
+                for training. Required if instance_groups is not set.
             instance_type (str): Type of EC2 instance to use for training,
-                for example, 'ml.c4.xlarge'.
+                for example, ``'ml.c4.xlarge'``. Required if instance_groups is
+                not set.
             volume_size (int): Size in GB of the EBS volume to use for
                 storing input data during training (default: 30). Must be large
                 enough to store training data if File Mode is used (which is the
                 default).
             volume_kms_key (str): Optional. KMS key ID for encrypting EBS
                 volume attached to the training instance (default: None).
             max_run (int): Timeout in seconds for training (default: 24 *
@@ -226,15 +231,14 @@
                 don't use an Amazon algorithm.
             encrypt_inter_container_traffic (bool): Specifies whether traffic
                 between training containers is encrypted for the training job
                 (default: ``False``).
             use_spot_instances (bool): Specifies whether to use SageMaker
                 Managed Spot instances for training. If enabled then the
                 ``max_wait`` arg should also be set.
-
                 More information:
                 https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html
                 (default: ``False``).
             max_wait (int): Timeout in seconds waiting for spot training
                 job (default: None). After this amount of time Amazon
                 SageMaker will stop waiting for managed spot training job to
                 complete (default: None).
@@ -304,48 +308,46 @@
             source_dir (str): The absolute, relative, or  S3 URI Path to a directory
                 with any other training source code dependencies aside from the entry
                 point file (default: None). If ``source_dir`` is an S3 URI, it must
                 point to a tar.gz file. The structure within this directory is preserved
                 when training on Amazon SageMaker. If 'git_config' is provided,
                 'source_dir' should be a relative location to a directory in the Git
                 repo.
+                With the following GitHub repo directory structure:
 
-                .. admonition:: Example
+                .. code::
 
-                    With the following GitHub repo directory structure:
-
-                    >>> |----- README.md
-                    >>> |----- src
-                    >>>         |----- train.py
-                    >>>         |----- test.py
-
-                    if you need 'train.py' as the entry point and 'test.py' as
-                    the training source code, you can assign
-                    entry_point='train.py' and source_dir='src'.
+                    |----- README.md
+                    |----- src
+                             |----- train.py
+                             |----- test.py
+
+                if you need 'train.py' as the entry point and 'test.py' as
+                the training source code, you can assign
+                entry_point='train.py' and source_dir='src'.
             git_config (dict[str, str]): Git configurations used for cloning
                 files, including ``repo``, ``branch``, ``commit``,
                 ``2FA_enabled``, ``username``, ``password``, and ``token``. The
                 ``repo`` field is required. All other fields are optional.
                 ``repo`` specifies the Git repository where your training script
                 is stored. If you don't provide ``branch``, the default value
                 'master' is used. If you don't provide ``commit``, the latest
-                commit in the specified branch is used.
+                commit in the specified branch is used. For example, the following config:
 
-                .. admonition:: Example
-
-                    The following config:
-
-                    >>> git_config = {'repo': 'https://github.com/aws/sagemaker-python-sdk.git',
-                    >>>               'branch': 'test-branch-git-config',
-                    >>>               'commit': '329bfcf884482002c05ff7f44f62599ebc9f445a'}
-
-                    results in cloning the repo specified in 'repo', then
-                    checking out the 'master' branch, and checking out the specified
-                    commit.
+                .. code:: python
 
+                    git_config = {
+                        'repo': 'https://github.com/aws/sagemaker-python-sdk.git',
+                        'branch': 'test-branch-git-config',
+                        'commit': '329bfcf884482002c05ff7f44f62599ebc9f445a'
+                    }
+
+                results in cloning the repo specified in 'repo', then
+                checking out the 'master' branch, and checking out the specified
+                commit.
                 ``2FA_enabled``, ``username``, ``password``, and ``token`` are
                 used for authentication. For GitHub (or other Git) accounts, set
                 ``2FA_enabled`` to 'True' if two-factor authentication is
                 enabled for the account, otherwise set it to 'False'. If you do
                 not provide a value for ``2FA_enabled``, a default value of
                 'False' is used. CodeCommit does not support two-factor
                 authentication, so do not provide "2FA_enabled" with CodeCommit
@@ -418,15 +420,33 @@
 
                     >>> opt/ml/code
                     >>>     |------ train.py
                     >>>     |------ common
                     >>>     |------ virtual-env
 
                 This is not supported with "local code" in Local Mode.
-
+            instance_groups (list[:class:`sagemaker.instance_group.InstanceGroup`]):
+                Optional. A list of ``InstanceGroup`` objects
+                for launching a training job with a heterogeneous cluster.
+                For example:
+
+                .. code:: python
+
+                    instance_groups=[
+                        sagemaker.InstanceGroup(
+                            'instance_group_name_1', 'ml.p3dn.24xlarge', 64),
+                        sagemaker.InstanceGroup(
+                            'instance_group_name_2', 'ml.c5n.18xlarge', 64)]
+
+                For instructions on how to use ``InstanceGroup`` objects
+                to configure a heterogeneous cluster
+                through the SageMaker generic and framework estimator classes, see
+                `Train Using a Heterogeneous Cluster
+                <https://docs.aws.amazon.com/sagemaker/latest/dg/train-heterogeneous-cluster.html>`_
+                in the *Amazon SageMaker developer guide*.
         """
         instance_count = renamed_kwargs(
             "train_instance_count", "instance_count", instance_count, kwargs
         )
         instance_type = renamed_kwargs(
             "train_instance_type", "instance_type", instance_type, kwargs
         )
@@ -436,20 +456,18 @@
         )
         max_wait = renamed_kwargs("train_max_wait", "max_wait", max_wait, kwargs)
         volume_size = renamed_kwargs("train_volume_size", "volume_size", volume_size, kwargs)
         volume_kms_key = renamed_kwargs(
             "train_volume_kms_key", "volume_kms_key", volume_kms_key, kwargs
         )
 
-        if instance_count is None or instance_type is None:
-            raise ValueError("Both instance_count and instance_type are required.")
-
         self.role = role
         self.instance_count = instance_count
         self.instance_type = instance_type
+        self.instance_groups = instance_groups
         self.volume_size = volume_size
         self.volume_kms_key = volume_kms_key
         self.max_run = max_run
         self.input_mode = input_mode
         self.metric_definitions = metric_definitions
         self.model_uri = model_uri
         self.model_channel_name = model_channel_name
@@ -918,15 +936,22 @@
                 self.profiler_config.s3_output_path,
                 self.latest_training_job.name,
                 "profiler-output",
             )
         return None
 
     @runnable_by_pipeline
-    def fit(self, inputs=None, wait=True, logs="All", job_name=None, experiment_config=None):
+    def fit(
+        self,
+        inputs: Optional[Union[str, Dict, TrainingInput, FileSystemInput]] = None,
+        wait: bool = True,
+        logs: str = "All",
+        job_name: Optional[str] = None,
+        experiment_config: Optional[Dict[str, str]] = None,
+    ):
         """Train a model using the input training dataset.
 
         The API calls the Amazon SageMaker CreateTrainingJob API to start
         model training. The API uses configuration you provided to create the
         estimator and the specified input training data to send the
         CreatingTrainingJob request to Amazon SageMaker.
 
@@ -1297,14 +1322,20 @@
         approval_status=None,
         description=None,
         compile_model_family=None,
         model_name=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
         **kwargs,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
@@ -1330,14 +1361,26 @@
                 model will be used (default: None).
             model_name (str): User defined model name (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
             **kwargs: Passed to invocation of ``create_model()``. Implementations may customize
                 ``create_model()`` to accept ``**kwargs`` to customize model creation during
                 deploy. For more, see the implementation docs.
 
         Returns:
             str: A string of SageMaker Model Package ARN.
         """
@@ -1367,14 +1410,20 @@
             metadata_properties,
             marketplace_cert,
             approval_status,
             description,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
+            framework=framework,
+            framework_version=framework_version,
+            nearest_model_name=nearest_model_name,
+            data_input_configuration=data_input_configuration,
         )
 
     @property
     def model_data(self):
         """str: The model location in S3. Only set if Estimator has been ``fit()``."""
         if self.latest_training_job is not None and not isinstance(
             self.sagemaker_session, PipelineSession
@@ -1480,14 +1529,47 @@
                 "MaximumRetryAttempts"
             )
             max_wait = job_details.get("StoppingCondition", {}).get("MaxWaitTimeInSeconds")
             if max_wait:
                 init_params["max_wait"] = max_wait
         return init_params
 
+    def _get_instance_type(self):
+        """Determine the instance type to be used in the training_image_uri function.
+
+        Returns:
+            instance_type: The instance_type to be used.
+        """
+        if self.instance_type is not None:
+            return self.instance_type
+
+        if not isinstance(self.instance_groups, list) or len(self.instance_groups) == 0:
+            raise ValueError(
+                "instance_groups must be set if instance_type is not set and instance_groups "
+                "must be a list."
+            )
+
+        for instance_group in self.instance_groups:
+            instance_type = instance_group.instance_type
+            match = re.match(r"^ml[\._]([a-z\d]+)\.?\w*$", instance_type)
+
+            if match:
+                family = match[1]
+                if family[0] in ("g", "p"):
+                    return instance_type
+            else:
+                raise ValueError(
+                    "Invalid SageMaker instance type for training with heterogeneous clusters: {}. "
+                    "For options see: https://aws.amazon.com/sagemaker/pricing/instance-types".format(
+                        instance_type
+                    )
+                )
+
+        return self.instance_groups[0].instance_type
+
     def transformer(
         self,
         instance_count,
         instance_type,
         strategy=None,
         assemble_with=None,
         output_path=None,
@@ -1866,24 +1948,30 @@
             if "InputMode" in inputs.config:
                 logger.debug(
                     "Selecting TrainingInput's input_mode (%s) for TrainingInputMode.",
                     inputs.config["InputMode"],
                 )
                 train_args["input_mode"] = inputs.config["InputMode"]
 
+        # enable_network_isolation may be a pipeline variable place holder object
+        # which is parsed in execution time
         if estimator.enable_network_isolation():
-            train_args["enable_network_isolation"] = True
+            train_args["enable_network_isolation"] = estimator.enable_network_isolation()
 
         if estimator.max_retry_attempts is not None:
             train_args["retry_strategy"] = {"MaximumRetryAttempts": estimator.max_retry_attempts}
         else:
             train_args["retry_strategy"] = None
 
+        # encrypt_inter_container_traffic may be a pipeline variable place holder object
+        # which is parsed in execution time
         if estimator.encrypt_inter_container_traffic:
-            train_args["encrypt_inter_container_traffic"] = True
+            train_args[
+                "encrypt_inter_container_traffic"
+            ] = estimator.encrypt_inter_container_traffic
 
         if isinstance(estimator, sagemaker.algorithm.AlgorithmEstimator):
             train_args["algorithm_arn"] = estimator.algorithm_arn
         else:
             train_args["image_uri"] = estimator.training_image_uri()
 
         if estimator.debugger_rule_configs:
@@ -2021,68 +2109,70 @@
     """A generic Estimator to train using any supplied algorithm.
 
     This class is designed for use with algorithms that don't have their own, custom class.
     """
 
     def __init__(
         self,
-        image_uri,
-        role,
-        instance_count=None,
-        instance_type=None,
-        volume_size=30,
-        volume_kms_key=None,
-        max_run=24 * 60 * 60,
-        input_mode="File",
-        output_path=None,
-        output_kms_key=None,
-        base_job_name=None,
-        sagemaker_session=None,
-        hyperparameters=None,
-        tags=None,
-        subnets=None,
-        security_group_ids=None,
-        model_uri=None,
-        model_channel_name="model",
-        metric_definitions=None,
-        encrypt_inter_container_traffic=False,
-        use_spot_instances=False,
-        max_wait=None,
-        checkpoint_s3_uri=None,
-        checkpoint_local_path=None,
-        enable_network_isolation=False,
-        rules=None,
-        debugger_hook_config=None,
-        tensorboard_output_config=None,
-        enable_sagemaker_metrics=None,
-        profiler_config=None,
-        disable_profiler=False,
-        environment=None,
-        max_retry_attempts=None,
-        source_dir=None,
-        git_config=None,
-        container_log_level=logging.INFO,
-        code_location=None,
-        entry_point=None,
-        dependencies=None,
+        image_uri: Union[str, PipelineVariable],
+        role: str,
+        instance_count: Optional[Union[int, PipelineVariable]] = None,
+        instance_type: Optional[Union[str, PipelineVariable]] = None,
+        volume_size: Union[int, PipelineVariable] = 30,
+        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        max_run: Union[int, PipelineVariable] = 24 * 60 * 60,
+        input_mode: Union[str, PipelineVariable] = "File",
+        output_path: Optional[Union[str, PipelineVariable]] = None,
+        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        base_job_name: Optional[str] = None,
+        sagemaker_session: Optional[Session] = None,
+        hyperparameters: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        subnets: Optional[List[Union[str, PipelineVariable]]] = None,
+        security_group_ids: Optional[List[Union[str, PipelineVariable]]] = None,
+        model_uri: Optional[str] = None,
+        model_channel_name: Union[str, PipelineVariable] = "model",
+        metric_definitions: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        encrypt_inter_container_traffic: Union[bool, PipelineVariable] = False,
+        use_spot_instances: Union[bool, PipelineVariable] = False,
+        max_wait: Optional[Union[int, PipelineVariable]] = None,
+        checkpoint_s3_uri: Optional[Union[str, PipelineVariable]] = None,
+        checkpoint_local_path: Optional[Union[str, PipelineVariable]] = None,
+        enable_network_isolation: Union[bool, PipelineVariable] = False,
+        rules: Optional[List[RuleBase]] = None,
+        debugger_hook_config: Optional[Union[DebuggerHookConfig, bool]] = None,
+        tensorboard_output_config: Optional[TensorBoardOutputConfig] = None,
+        enable_sagemaker_metrics: Optional[Union[bool, PipelineVariable]] = None,
+        profiler_config: Optional[ProfilerConfig] = None,
+        disable_profiler: bool = False,
+        environment: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        max_retry_attempts: Optional[Union[int, PipelineVariable]] = None,
+        source_dir: Optional[str] = None,
+        git_config: Optional[Dict[str, str]] = None,
+        container_log_level: Union[int, PipelineVariable] = logging.INFO,
+        code_location: Optional[str] = None,
+        entry_point: Optional[str] = None,
+        dependencies: Optional[List[str]] = None,
+        instance_groups: Optional[Dict[str, Union[str, int]]] = None,
         **kwargs,
     ):
         """Initialize an ``Estimator`` instance.
 
         Args:
             image_uri (str): The container image to use for training.
             role (str): An AWS IAM role (either name or full ARN). The Amazon
                 SageMaker training jobs and APIs that create Amazon SageMaker
                 endpoints use this role to access training data and model
                 artifacts. After the endpoint is created, the inference code
                 might use the IAM role, if it needs to access an AWS resource.
             instance_count (int): Number of Amazon EC2 instances to use
-                for training.
+                for training. Required if instance_groups is not set.
             instance_type (str): Type of EC2 instance to use for training,
-                for example, 'ml.c4.xlarge'.
+                for example, 'ml.c4.xlarge'. Required if instance_groups is
+                not set.
             volume_size (int): Size in GB of the EBS volume to use for
                 storing input data during training (default: 30). Must be large
                 enough to store training data if File Mode is used (which is the
                 default).
             volume_kms_key (str): Optional. KMS key ID for encrypting EBS
                 volume attached to the training instance (default: None).
             max_run (int): Timeout in seconds for training (default: 24 *
@@ -2336,14 +2426,33 @@
 
                     >>> opt/ml/code
                     >>>     |------ train.py
                     >>>     |------ common
                     >>>     |------ virtual-env
 
                 This is not supported with "local code" in Local Mode.
+            instance_groups (list[:class:`sagemaker.instance_group.InstanceGroup`]):
+                Optional. A list of ``InstanceGroup`` objects
+                for launching a training job with a heterogeneous cluster.
+                For example:
+
+                .. code:: python
+
+                    instance_groups=[
+                        sagemaker.InstanceGroup(
+                            'instance_group_name_1', 'ml.p3dn.24xlarge', 64),
+                        sagemaker.InstanceGroup(
+                            'instance_group_name_2', 'ml.c5n.18xlarge', 64)]
+
+                For instructions on how to use ``InstanceGroup`` objects
+                to configure a heterogeneous cluster
+                through the SageMaker generic and framework estimator classes, see
+                `Train Using a Heterogeneous Cluster
+                <https://docs.aws.amazon.com/sagemaker/latest/dg/train-heterogeneous-cluster.html>`_
+                in the *Amazon SageMaker developer guide*.
         """
         self.image_uri = image_uri
         self._hyperparameters = hyperparameters.copy() if hyperparameters else {}
         super(Estimator, self).__init__(
             role,
             instance_count,
             instance_type,
@@ -2378,14 +2487,15 @@
             container_log_level=container_log_level,
             source_dir=source_dir,
             git_config=git_config,
             code_location=code_location,
             entry_point=entry_point,
             dependencies=dependencies,
             hyperparameters=hyperparameters,
+            instance_groups=instance_groups,
             **kwargs,
         )
 
     def training_image_uri(self):
         """Returns the docker image to use for training.
 
         The fit() method, that does the model training, calls this method to
@@ -2484,26 +2594,26 @@
     such as training/deployment images and predictor instances.
     """
 
     _framework_name = None
 
     def __init__(
         self,
-        entry_point,
-        source_dir=None,
-        hyperparameters=None,
-        container_log_level=logging.INFO,
-        code_location=None,
-        image_uri=None,
-        dependencies=None,
-        enable_network_isolation=False,
-        git_config=None,
-        checkpoint_s3_uri=None,
-        checkpoint_local_path=None,
-        enable_sagemaker_metrics=None,
+        entry_point: str,
+        source_dir: Optional[str] = None,
+        hyperparameters: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        container_log_level: Union[int, PipelineVariable] = logging.INFO,
+        code_location: Optional[str] = None,
+        image_uri: Optional[Union[str, PipelineVariable]] = None,
+        dependencies: Optional[List[str]] = None,
+        enable_network_isolation: Union[bool, PipelineVariable] = False,
+        git_config: Optional[Dict[str, str]] = None,
+        checkpoint_s3_uri: Optional[Union[str, PipelineVariable]] = None,
+        checkpoint_local_path: Optional[Union[str, PipelineVariable]] = None,
+        enable_sagemaker_metrics: Optional[Union[bool, PipelineVariable]] = None,
         **kwargs,
     ):
         """Base class initializer.
 
         Subclasses which override ``__init__`` should invoke ``super()``.
 
         Args:
@@ -2850,15 +2960,15 @@
             framework_version=self.framework_version,  # pylint: disable=no-member
             py_version=self.py_version,  # pylint: disable=no-member
             image_uri=self.image_uri,
             distribution=getattr(self, "distribution", None),
             compiler_config=getattr(self, "compiler_config", None),
             tensorflow_version=getattr(self, "tensorflow_version", None),
             pytorch_version=getattr(self, "pytorch_version", None),
-            instance_type=self.instance_type,
+            instance_type=self._get_instance_type(),
         )
 
     @classmethod
     def attach(cls, training_job_name, sagemaker_session=None, model_channel_name="model"):
         """Attach to an existing training job.
 
         Create an Estimator bound to an existing training job, each subclass
@@ -3058,14 +3168,21 @@
             distribution (dict): A dictionary with information on how to run distributed training.
 
         Returns:
             dict that
         """
         distribution_config = {}
 
+        mpi_enabled = False
+        smdataparallel_enabled = False
+        if "instance_groups" in distribution:
+            distribution_config["sagemaker_distribution_instance_groups"] = distribution[
+                "instance_groups"
+            ]
+
         if "parameter_server" in distribution:
             ps_enabled = distribution.get("parameter_server").get("enabled", False)
             distribution_config[self.LAUNCH_PS_ENV_NAME] = ps_enabled
 
         if "mpi" in distribution:
             mpi_dict = distribution["mpi"]
             mpi_enabled = mpi_dict.get("enabled", False)
@@ -3093,14 +3210,21 @@
             distribution_config[self.LAUNCH_SM_DDP_ENV_NAME] = smdataparallel_enabled
             distribution_config[self.INSTANCE_TYPE] = self.instance_type
             if smdataparallel_enabled:
                 distribution_config[self.SM_DDP_CUSTOM_MPI_OPTIONS] = smdistributed[
                     "dataparallel"
                 ].get("custom_mpi_options", "")
 
+        if not (mpi_enabled or smdataparallel_enabled) and distribution_config.get(
+            "sagemaker_distribution_instance_groups"
+        ) not in [None, []]:
+            raise ValueError(
+                "Don't set training instance groups while no distribution strategies enabled!"
+            )
+
         return distribution_config
 
 
 def _s3_uri_prefix(channel_name, s3_data):
     """Placeholder docstring"""
     if isinstance(s3_data, TrainingInput):
         s3_uri = s3_data.config["DataSource"]["S3DataSource"]["S3Uri"]
```

### Comparing `sagemaker-2.98.0/src/sagemaker/exceptions.py` & `sagemaker-2.99.0/src/sagemaker/exceptions.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/feature_store/__init__.py` & `sagemaker-2.99.0/src/sagemaker/feature_store/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/feature_store/feature_definition.py` & `sagemaker-2.99.0/src/sagemaker/feature_store/feature_definition.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/feature_store/feature_group.py` & `sagemaker-2.99.0/src/sagemaker/feature_store/feature_group.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/feature_store/inputs.py` & `sagemaker-2.99.0/src/sagemaker/feature_store/inputs.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/fw_utils.py` & `sagemaker-2.99.0/src/sagemaker/tensorflow/estimator.py`

 * *Files 20% similar despite different names*

```diff
@@ -6,689 +6,545 @@
 #
 #     http://aws.amazon.com/apache2.0/
 #
 # or in the "license" file accompanying this file. This file is
 # distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
-"""Utility methods used by framework classes"""
+"""An estimator class for training with TensorFlow on Amazon SageMaker."""
 from __future__ import absolute_import
 
 import logging
-import os
-import re
-import time
-import shutil
-import tempfile
-from collections import namedtuple
-from typing import Optional
-
-import sagemaker.image_uris
-from sagemaker.session_settings import SessionSettings
-import sagemaker.utils
-from sagemaker.workflow import is_pipeline_variable
-
-from sagemaker.deprecations import renamed_warning
-
-logger = logging.getLogger(__name__)
-
-_TAR_SOURCE_FILENAME = "source.tar.gz"
-
-UploadedCode = namedtuple("UserCode", ["s3_prefix", "script_name"])
-"""sagemaker.fw_utils.UserCode: An object containing the S3 prefix and script name.
-This is for the source code used for the entry point with an ``Estimator``. It can be
-instantiated with positional or keyword arguments.
-"""
-
-PYTHON_2_DEPRECATION_WARNING = (
-    "{latest_supported_version} is the latest version of {framework} that supports "
-    "Python 2. Newer versions of {framework} will only be available for Python 3."
-    "Please set the argument \"py_version='py3'\" to use the Python 3 {framework} image."
-)
-PARAMETER_SERVER_MULTI_GPU_WARNING = (
-    "If you have selected a multi-GPU training instance type "
-    "and also enabled parameter server for distributed training, "
-    "distributed training with the default parameter server configuration will not "
-    "fully leverage all GPU cores; the parameter server will be configured to run "
-    "only one worker per host regardless of the number of GPUs."
-)
-
-DEBUGGER_UNSUPPORTED_REGIONS = ("us-iso-east-1",)
-PROFILER_UNSUPPORTED_REGIONS = ("us-iso-east-1",)
-
-SINGLE_GPU_INSTANCE_TYPES = ("ml.p2.xlarge", "ml.p3.2xlarge")
-SM_DATAPARALLEL_SUPPORTED_INSTANCE_TYPES = (
-    "ml.p3.16xlarge",
-    "ml.p3dn.24xlarge",
-    "ml.p4d.24xlarge",
-    "local_gpu",
-)
-SM_DATAPARALLEL_SUPPORTED_FRAMEWORK_VERSIONS = {
-    "tensorflow": [
-        "2.3",
-        "2.3.1",
-        "2.3.2",
-        "2.4",
-        "2.4.1",
-        "2.4.3",
-        "2.5",
-        "2.5.0",
-        "2.5.1",
-        "2.6",
-        "2.6.0",
-        "2.6.2",
-        "2.6.3",
-        "2.7",
-        "2.7.1",
-        "2.8",
-        "2.8.0",
-        "2.9",
-        "2.9.1",
-    ],
-    "pytorch": [
-        "1.6",
-        "1.6.0",
-        "1.7",
-        "1.7.1",
-        "1.8",
-        "1.8.0",
-        "1.8.1",
-        "1.9",
-        "1.9.0",
-        "1.9.1",
-        "1.10",
-        "1.10.0",
-        "1.10.2",
-        "1.11",
-        "1.11.0",
-    ],
-}
-SMDISTRIBUTED_SUPPORTED_STRATEGIES = ["dataparallel", "modelparallel"]
-
-
-def validate_source_dir(script, directory):
-    """Validate that the source directory exists and it contains the user script.
-
-    Args:
-        script (str): Script filename.
-        directory (str): Directory containing the source file.
-    Raises:
-        ValueError: If ``directory`` does not exist, is not a directory, or does
-            not contain ``script``.
-    """
-    if directory:
-        if not os.path.isfile(os.path.join(directory, script)):
-            raise ValueError(
-                'No file named "{}" was found in directory "{}".'.format(script, directory)
-            )
 
-    return True
+from packaging import version
 
+from sagemaker import image_uris, s3, utils
+from sagemaker.deprecations import renamed_kwargs
+from sagemaker.estimator import Framework, EstimatorBase
+import sagemaker.fw_utils as fw
+from sagemaker.tensorflow import defaults
+from sagemaker.tensorflow.model import TensorFlowModel
+from sagemaker.transformer import Transformer
+from sagemaker.vpc_utils import VPC_CONFIG_DEFAULT
+from sagemaker.workflow import is_pipeline_variable
+from sagemaker.tensorflow.training_compiler.config import TrainingCompilerConfig
 
-def get_mp_parameters(distribution):
-    """Get the model parallelism parameters provided by the user.
+logger = logging.getLogger("sagemaker")
 
-    Args:
-        distribution: distribution dictionary defined by the user.
 
-    Returns:
-        params: dictionary containing model parallelism parameters
-        used for training.
-    """
-    try:
-        mp_dict = distribution["smdistributed"]["modelparallel"]
-    except KeyError:
-        mp_dict = {}
-    if mp_dict.get("enabled", False) is True:
-        params = mp_dict.get("parameters", {})
-        validate_mp_config(params)
-        return params
-    return None
-
-
-def validate_mp_config(config):
-    """Validate the configuration dictionary for model parallelism.
-
-    Args:
-       config (dict): Dictionary holding configuration keys and values.
-
-    Raises:
-        ValueError: If any of the keys have incorrect values.
-    """
-
-    if "partitions" not in config:
-        raise ValueError("'partitions' is a required parameter.")
-
-    def validate_positive(key):
-        try:
-            if not isinstance(config[key], int) or config[key] < 1:
-                raise ValueError(f"The number of {key} must be a positive integer.")
-        except KeyError:
-            pass
-
-    def validate_in(key, vals):
-        try:
-            if config[key] not in vals:
-                raise ValueError(f"{key} must be a value in: {vals}.")
-        except KeyError:
-            pass
-
-    def validate_bool(keys):
-        validate_in(keys, [True, False])
-
-    validate_in("pipeline", ["simple", "interleaved", "_only_forward"])
-    validate_in("placement_strategy", ["spread", "cluster"])
-    validate_in("optimize", ["speed", "memory"])
-
-    for key in ["microbatches", "partitions", "active_microbatches"]:
-        validate_positive(key)
-
-    for key in [
-        "auto_partition",
-        "contiguous",
-        "load_partition",
-        "horovod",
-        "ddp",
-        "deterministic_server",
-    ]:
-        validate_bool(key)
-
-    if "partition_file" in config and not isinstance(config.get("partition_file"), str):
-        raise ValueError("'partition_file' must be a str.")
+class TensorFlow(Framework):
+    """Handle end-to-end training and deployment of user-provided TensorFlow code."""
 
-    if config.get("auto_partition") is False and "default_partition" not in config:
-        raise ValueError("default_partition must be supplied if auto_partition is set to False!")
+    _framework_name = "tensorflow"
 
-    if "default_partition" in config and config["default_partition"] >= config["partitions"]:
-        raise ValueError("default_partition must be less than the number of partitions!")
+    _HIGHEST_LEGACY_MODE_ONLY_VERSION = version.Version("1.10.0")
+    _HIGHEST_PYTHON_2_VERSION = version.Version("2.1.1")
 
-    if "memory_weight" in config and (
-        config["memory_weight"] > 1.0 or config["memory_weight"] < 0.0
+    def __init__(
+        self,
+        py_version=None,
+        framework_version=None,
+        model_dir=None,
+        image_uri=None,
+        distribution=None,
+        compiler_config=None,
+        **kwargs,
     ):
-        raise ValueError("memory_weight must be between 0.0 and 1.0!")
-
-    if "ddp_port" in config and "ddp" not in config:
-        raise ValueError("`ddp_port` needs `ddp` to be set as well")
-
-    if "ddp_dist_backend" in config and "ddp" not in config:
-        raise ValueError("`ddp_dist_backend` needs `ddp` to be set as well")
-
-    if "ddp_port" in config:
-        if not isinstance(config["ddp_port"], int) or config["ddp_port"] < 0:
-            value = config["ddp_port"]
-            raise ValueError(f"Invalid port number {value}.")
-
-    if config.get("horovod", False) and config.get("ddp", False):
-        raise ValueError("'ddp' and 'horovod' cannot be simultaneously enabled.")
-
-
-def tar_and_upload_dir(
-    session,
-    bucket,
-    s3_key_prefix,
-    script,
-    directory=None,
-    dependencies=None,
-    kms_key=None,
-    s3_resource=None,
-    settings: Optional[SessionSettings] = None,
-):
-    """Package source files and upload a compress tar file to S3.
-
-    The S3 location will be ``s3://<bucket>/s3_key_prefix/sourcedir.tar.gz``.
-    If directory is an S3 URI, an UploadedCode object will be returned, but
-    nothing will be uploaded to S3 (this allow reuse of code already in S3).
-    If directory is None, the script will be added to the archive at
-    ``./<basename of script>``. If directory is not None, the (recursive) contents
-    of the directory will be added to the archive. directory is treated as the base
-    path of the archive, and the script name is assumed to be a filename or relative path
-    inside the directory.
-
-    Args:
-        session (boto3.Session): Boto session used to access S3.
-        bucket (str): S3 bucket to which the compressed file is uploaded.
-        s3_key_prefix (str): Prefix for the S3 key.
-        script (str): Script filename or path.
-        directory (str): Optional. Directory containing the source file. If it
-            starts with "s3://", no action is taken.
-        dependencies (List[str]): Optional. A list of paths to directories
-            (absolute or relative) containing additional libraries that will be
-            copied into /opt/ml/lib
-        kms_key (str): Optional. KMS key ID used to upload objects to the bucket
-            (default: None).
-        s3_resource (boto3.resource("s3")): Optional. Pre-instantiated Boto3 Resource
-            for S3 connections, can be used to customize the configuration,
-            e.g. set the endpoint URL (default: None).
-        settings (sagemaker.session_settings.SessionSettings): Optional. The settings
-            of the SageMaker ``Session``, can be used to override the default encryption
-            behavior (default: None).
-    Returns:
-        sagemaker.fw_utils.UserCode: An object with the S3 bucket and key (S3 prefix) and
-            script name.
-    """
-    if directory and directory.lower().startswith("s3://"):
-        return UploadedCode(s3_prefix=directory, script_name=script)
-
-    script_name = script if directory else os.path.basename(script)
-    dependencies = dependencies or []
-    key = "%s/sourcedir.tar.gz" % s3_key_prefix
-    tmp = tempfile.mkdtemp()
-    encrypt_artifact = True if settings is None else settings.encrypt_repacked_artifacts
-
-    try:
-        source_files = _list_files_to_compress(script, directory) + dependencies
-        tar_file = sagemaker.utils.create_tar_file(
-            source_files, os.path.join(tmp, _TAR_SOURCE_FILENAME)
-        )
-
-        if kms_key:
-            extra_args = {"ServerSideEncryption": "aws:kms", "SSEKMSKeyId": kms_key}
-        elif encrypt_artifact:
-            # encrypt the tarball at rest in S3 with the default AWS managed KMS key for S3
-            # see https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html#API_PutObject_RequestSyntax
-            extra_args = {"ServerSideEncryption": "aws:kms"}
-        else:
-            extra_args = None
-
-        if s3_resource is None:
-            s3_resource = session.resource("s3", region_name=session.region_name)
-        else:
-            print("Using provided s3_resource")
-
-        s3_resource.Object(bucket, key).upload_file(tar_file, ExtraArgs=extra_args)
-    finally:
-        shutil.rmtree(tmp)
-
-    return UploadedCode(s3_prefix="s3://%s/%s" % (bucket, key), script_name=script_name)
-
-
-def _list_files_to_compress(script, directory):
-    """Placeholder docstring"""
-    if directory is None:
-        return [script]
-
-    basedir = directory if directory else os.path.dirname(script)
-    return [os.path.join(basedir, name) for name in os.listdir(basedir)]
-
-
-def framework_name_from_image(image_uri):
-    # noinspection LongLine
-    """Extract the framework and Python version from the image name.
-
-    Args:
-        image_uri (str): Image URI, which should be one of the following forms:
-            legacy:
-            '<account>.dkr.ecr.<region>.amazonaws.com/sagemaker-<fw>-<py_ver>-<device>:<container_version>'
-            legacy:
-            '<account>.dkr.ecr.<region>.amazonaws.com/sagemaker-<fw>-<py_ver>-<device>:<fw_version>-<device>-<py_ver>'
-            current:
-            '<account>.dkr.ecr.<region>.amazonaws.com/sagemaker-<fw>:<fw_version>-<device>-<py_ver>'
-            current:
-            '<account>.dkr.ecr.<region>.amazonaws.com/sagemaker-rl-<fw>:<rl_toolkit><rl_version>-<device>-<py_ver>'
-            current:
-            '<account>.dkr.ecr.<region>.amazonaws.com/<fw>-<image_scope>:<fw_version>-<device>-<py_ver>'
-
-    Returns:
-        tuple: A tuple containing:
-
-            - str: The framework name
-            - str: The Python version
-            - str: The image tag
-            - str: If the TensorFlow image is script mode
-    """
-    sagemaker_pattern = re.compile(sagemaker.utils.ECR_URI_PATTERN)
-    sagemaker_match = sagemaker_pattern.match(image_uri)
-    if sagemaker_match is None:
-        return None, None, None, None
-
-    # extract framework, python version and image tag
-    # We must support both the legacy and current image name format.
-    name_pattern = re.compile(
-        r"""^(?:sagemaker(?:-rl)?-)?
-        (tensorflow|mxnet|chainer|pytorch|scikit-learn|xgboost
-        |huggingface-tensorflow|huggingface-pytorch
-        |huggingface-tensorflow-trcomp|huggingface-pytorch-trcomp)(?:-)?
-        (scriptmode|training)?
-        :(.*)-(.*?)-(py2|py3\d*)(?:.*)$""",
-        re.VERBOSE,
-    )
-    name_match = name_pattern.match(sagemaker_match.group(9))
-    if name_match is not None:
-        fw, scriptmode, ver, device, py = (
-            name_match.group(1),
-            name_match.group(2),
-            name_match.group(3),
-            name_match.group(4),
-            name_match.group(5),
-        )
-        return fw, py, "{}-{}-{}".format(ver, device, py), scriptmode
-
-    legacy_name_pattern = re.compile(r"^sagemaker-(tensorflow|mxnet)-(py2|py3)-(cpu|gpu):(.*)$")
-    legacy_match = legacy_name_pattern.match(sagemaker_match.group(9))
-    if legacy_match is not None:
-        return (legacy_match.group(1), legacy_match.group(2), legacy_match.group(4), None)
-    return None, None, None, None
-
-
-def framework_version_from_tag(image_tag):
-    """Extract the framework version from the image tag.
-
-    Args:
-        image_tag (str): Image tag, which should take the form
-            '<framework_version>-<device>-<py_version>'
-
-    Returns:
-        str: The framework version.
-    """
-    tag_pattern = re.compile(r"^(.*)-(cpu|gpu)-(py2|py3\d*)$")
-    tag_match = tag_pattern.match(image_tag)
-    return None if tag_match is None else tag_match.group(1)
-
-
-def model_code_key_prefix(code_location_key_prefix, model_name, image):
-    """Returns the s3 key prefix for uploading code during model deployment.
-
-    The location returned is a potential concatenation of 2 parts
-        1. code_location_key_prefix if it exists
-        2. model_name or a name derived from the image
-
-    Args:
-        code_location_key_prefix (str): the s3 key prefix from code_location
-        model_name (str): the name of the model
-        image (str): the image from which a default name can be extracted
-
-    Returns:
-        str: the key prefix to be used in uploading code
-    """
-    name_from_image = f"/model_code/{int(time.time())}"
-    if not is_pipeline_variable(image):
-        name_from_image = sagemaker.utils.name_from_image(image)
-    return "/".join(filter(None, [code_location_key_prefix, model_name or name_from_image]))
-
-
-def warn_if_parameter_server_with_multi_gpu(training_instance_type, distribution):
-    """Warn the user about training when it doesn't leverage all the GPU cores.
-
-    Warn the user that training will not fully leverage all the GPU
-    cores if parameter server is enabled and a multi-GPU instance is selected.
-    Distributed training with the default parameter server setup doesn't
-    support multi-GPU instances.
-
-    Args:
-        training_instance_type (str): A string representing the type of training instance selected.
-        distribution (dict): A dictionary with information to enable distributed training.
-            (Defaults to None if distributed training is not enabled.) For example:
+        """Initialize a ``TensorFlow`` estimator.
 
-            .. code:: python
-
-                {
-                    "parameter_server": {
-                        "enabled": True
-                    }
-                }
-
-
-    """
-    if training_instance_type == "local" or distribution is None:
-        return
-    if is_pipeline_variable(training_instance_type):
-        # The training_instance_type is not available in compile time.
-        # Rather, it's given in Pipeline execution time
-        return
-
-    is_multi_gpu_instance = (
-        training_instance_type == "local_gpu"
-        or training_instance_type.split(".")[1].startswith("p")
-    ) and training_instance_type not in SINGLE_GPU_INSTANCE_TYPES
-
-    ps_enabled = "parameter_server" in distribution and distribution["parameter_server"].get(
-        "enabled", False
-    )
-
-    if is_multi_gpu_instance and ps_enabled:
-        logger.warning(PARAMETER_SERVER_MULTI_GPU_WARNING)
+        Args:
+            py_version (str): Python version you want to use for executing your model training
+                code. Defaults to ``None``. Required unless ``image_uri`` is provided.
+            framework_version (str): TensorFlow version you want to use for executing your model
+                training code. Defaults to ``None``. Required unless ``image_uri`` is provided.
+                List of supported versions:
+                https://github.com/aws/sagemaker-python-sdk#tensorflow-sagemaker-estimators.
+            model_dir (str): S3 location where the checkpoint data and models can be exported to
+                during training (default: None). It will be passed in the training script as one of
+                the command line arguments. If not specified, one is provided based on
+                your training configuration:
+
+                * *distributed training with SMDistributed or MPI with Horovod* - ``/opt/ml/model``
+                * *single-machine training or distributed training without MPI* - \
+                    ``s3://{output_path}/model``
+                * *Local Mode with local sources (file:// instead of s3://)* - \
+                    ``/opt/ml/shared/model``
+
+                To disable having ``model_dir`` passed to your training script,
+                set ``model_dir=False``.
+            image_uri (str): If specified, the estimator will use this image for training and
+                hosting, instead of selecting the appropriate SageMaker official image based on
+                framework_version and py_version. It can be an ECR url or dockerhub image and tag.
+
+                Examples:
+                    123.dkr.ecr.us-west-2.amazonaws.com/my-custom-image:1.0
+                    custom-image:latest.
+
+                If ``framework_version`` or ``py_version`` are ``None``, then
+                ``image_uri`` is required. If also ``None``, then a ``ValueError``
+                will be raised.
+            distribution (dict): A dictionary with information on how to run distributed training
+                (default: None). Currently, the following are supported:
+                distributed training with parameter servers, SageMaker Distributed (SMD) Data
+                and Model Parallelism, and MPI. SMD Model Parallelism can only be used with MPI.
+
+                **To enable the SageMaker distributed data parallelism:**
+
+                    .. code:: python
+
+                        { "smdistributed": { "dataparallel": { "enabled": True } } }
+
+                    .. seealso::
+
+                        To learn more, see :ref:`sdp_api_docs_toc`.
+
+                **To enable the SageMaker distributed model parallelism:**
+
+                    .. code:: python
+
+                        {
+                            "smdistributed": {
+                                "modelparallel": {
+                                    "enabled":True,
+                                    "parameters": {
+                                        "partitions": 2,
+                                        "microbatches": 4,
+                                        "placement_strategy": "spread",
+                                        "pipeline": "interleaved",
+                                        "optimize": "speed",
+                                        "ddp": True,
+                                    }
+                            },
+                            "mpi": {
+                                "enabled" : True,
+                                "processes_per_host" : 8,
+                            }
+                        }
 
+                    .. note::
 
-def validate_smdistributed(
-    instance_type, framework_name, framework_version, py_version, distribution, image_uri=None
-):
-    """Check if smdistributed strategy is correctly invoked by the user.
+                        The SageMaker distributed model parallel library internally uses MPI.
+                        In order to use model parallelism, MPI also must be enabled.
 
-    Currently, two strategies are supported: `dataparallel` or `modelparallel`.
-    Validate if the user requested strategy is supported.
+                    .. seealso::
 
-    Currently, only one strategy can be specified at a time. Validate if the user has requested
-    more than one strategy simultaneously.
+                        To learn more, see :ref:`smp_api_docs_toc`.
 
-    Validate if the smdistributed dict arg is syntactically correct.
+                    .. seealso::
 
-    Additionally, perform strategy-specific validations.
+                        To find a complete list of parameters for SageMaker model parallelism,
+                        see :ref:`sm-sdk-modelparallel-general`.
 
-    Args:
-        instance_type (str): A string representing the type of training instance selected.
-        framework_name (str): A string representing the name of framework selected.
-        framework_version (str): A string representing the framework version selected.
-        py_version (str): A string representing the python version selected.
-        distribution (dict): A dictionary with information to enable distributed training.
-            (Defaults to None if distributed training is not enabled.) For example:
+                **To enable MPI:**
 
-            .. code:: python
+                    .. code:: python
 
-                {
-                    "smdistributed": {
-                        "dataparallel": {
-                            "enabled": True
+                        {
+                            "mpi": {
+                                "enabled": True
+                            }
                         }
-                    }
-                }
-        image_uri (str): A string representing a Docker image URI.
-
-    Raises:
-        ValueError: if distribution dictionary isn't correctly formatted or
-            multiple strategies are requested simultaneously or
-            an unsupported strategy is requested or
-            strategy-specific inputs are incorrect/unsupported
-    """
-    if "smdistributed" not in distribution:
-        # Distribution strategy other than smdistributed is selected
-        return
-    if is_pipeline_variable(instance_type):
-        # The instance_type is not available in compile time.
-        # Rather, it's given in Pipeline execution time
-        return
-
-    # distribution contains smdistributed
-    smdistributed = distribution["smdistributed"]
-    if not isinstance(smdistributed, dict):
-        raise ValueError("smdistributed strategy requires a dictionary")
-
-    if len(smdistributed) > 1:
-        # more than 1 smdistributed strategy requested by the user
-        err_msg = (
-            "Cannot use more than 1 smdistributed strategy. \n"
-            "Choose one of the following supported strategies:"
-            f"{SMDISTRIBUTED_SUPPORTED_STRATEGIES}"
-        )
-        raise ValueError(err_msg)
 
-    # validate if smdistributed strategy is supported
-    # currently this for loop essentially checks for only 1 key
-    for strategy in smdistributed:
-        if strategy not in SMDISTRIBUTED_SUPPORTED_STRATEGIES:
-            err_msg = (
-                f"Invalid smdistributed strategy provided: {strategy} \n"
-                f"Supported strategies: {SMDISTRIBUTED_SUPPORTED_STRATEGIES}"
-            )
-            raise ValueError(err_msg)
+                    To learn more, see `Training with Horovod
+                    <https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html#training-with-horovod>`_.
 
-    # smdataparallel-specific input validation
-    if "dataparallel" in smdistributed:
-        _validate_smdataparallel_args(
-            instance_type, framework_name, framework_version, py_version, distribution, image_uri
-        )
+                **To enable parameter server:**
 
+                    .. code:: python
 
-def _validate_smdataparallel_args(
-    instance_type, framework_name, framework_version, py_version, distribution, image_uri=None
-):
-    """Check if request is using unsupported arguments.
-
-    Validate if user specifies a supported instance type, framework version, and python
-    version.
-
-    Args:
-        instance_type (str): A string representing the type of training instance selected. Ex: `ml.p3.16xlarge`
-        framework_name (str): A string representing the name of framework selected. Ex: `tensorflow`
-        framework_version (str): A string representing the framework version selected. Ex: `2.3.1`
-        py_version (str): A string representing the python version selected. Ex: `py3`
-        distribution (dict): A dictionary with information to enable distributed training.
-            (Defaults to None if distributed training is not enabled.) Ex:
-
-            .. code:: python
-
-                {
-                    "smdistributed": {
-                        "dataparallel": {
-                            "enabled": True
+                        {
+                            "parameter_server": {
+                                "enabled": True
+                            }
                         }
-                    }
-                }
-        image_uri (str): A string representing a Docker image URI.
-
-    Raises:
-        ValueError: if
-            (`instance_type` is not in SM_DATAPARALLEL_SUPPORTED_INSTANCE_TYPES or
-            `py_version` is not python3 or
-            `framework_version` is not in SM_DATAPARALLEL_SUPPORTED_FRAMEWORK_VERSION
-    """
-    smdataparallel_enabled = (
-        distribution.get("smdistributed").get("dataparallel").get("enabled", False)
-    )
-
-    if not smdataparallel_enabled:
-        return
-
-    is_instance_type_supported = instance_type in SM_DATAPARALLEL_SUPPORTED_INSTANCE_TYPES
-
-    err_msg = ""
-
-    if not is_instance_type_supported:
-        # instance_type is required
-        err_msg += (
-            f"Provided instance_type {instance_type} is not supported by smdataparallel.\n"
-            "Please specify one of the supported instance types:"
-            f"{SM_DATAPARALLEL_SUPPORTED_INSTANCE_TYPES}\n"
+
+                    To learn more, see `Training with parameter servers
+                    <https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html#training-with-parameter-servers>`_.
+            compiler_config (:class:`~sagemaker.tensorflow.TrainingCompilerConfig`):
+                Configures SageMaker Training Compiler to accelerate training.
+
+            **kwargs: Additional kwargs passed to the Framework constructor.
+
+        .. tip::
+
+            You can find additional parameters for initializing this class at
+            :class:`~sagemaker.estimator.Framework` and
+            :class:`~sagemaker.estimator.EstimatorBase`.
+        """
+        distribution = renamed_kwargs("distributions", "distribution", distribution, kwargs)
+        instance_type = renamed_kwargs(
+            "train_instance_type", "instance_type", kwargs.get("instance_type"), kwargs
         )
+        fw.validate_version_or_image_args(framework_version, py_version, image_uri)
+        if py_version == "py2":
+            logger.warning(
+                fw.python_deprecation_warning(self._framework_name, defaults.LATEST_PY2_VERSION)
+            )
+        self.framework_version = framework_version
+        self.py_version = py_version
+        self.instance_type = instance_type
+
+        if "enable_sagemaker_metrics" not in kwargs:
+            # enable sagemaker metrics for TF v1.15 or greater:
+            if framework_version and version.Version(framework_version) >= version.Version("1.15"):
+                kwargs["enable_sagemaker_metrics"] = True
+
+        super(TensorFlow, self).__init__(image_uri=image_uri, **kwargs)
+        if distribution is not None:
+            distribution = fw.validate_distribution(
+                distribution,
+                self.instance_groups,
+                self._framework_name,
+                framework_version,
+                py_version,
+                image_uri,
+                kwargs,
+            )
+        self.model_dir = model_dir
+        self.distribution = distribution or {}
 
-    if not image_uri:
-        # ignore framework_version & py_version if image_uri is set
-        # in case image_uri is not set, then both are mandatory
-        supported = SM_DATAPARALLEL_SUPPORTED_FRAMEWORK_VERSIONS[framework_name]
-        if framework_version not in supported:
-            err_msg += (
-                f"Provided framework_version {framework_version} is not supported by"
-                " smdataparallel.\n"
-                f"Please specify one of the supported framework versions: {supported} \n"
+        self._validate_args(py_version=py_version)
+        if compiler_config is not None:
+            if not isinstance(compiler_config, TrainingCompilerConfig):
+                error_string = (
+                    f"Expected instance of type {TrainingCompilerConfig}"
+                    f"for argument compiler_config. "
+                    f"Instead got {type(compiler_config)}"
+                )
+                raise ValueError(error_string)
+            if compiler_config:
+                compiler_config.validate(self)
+        self.compiler_config = compiler_config
+
+    def _validate_args(self, py_version):
+        """Placeholder docstring"""
+
+        if py_version == "py2" and self._only_python_3_supported():
+            msg = (
+                "Python 2 containers are only available with {} and lower versions. "
+                "Please use a Python 3 container.".format(defaults.LATEST_PY2_VERSION)
             )
+            raise AttributeError(msg)
 
-        if "py3" not in py_version:
-            err_msg += (
-                f"Provided py_version {py_version} is not supported by smdataparallel.\n"
-                "Please specify py_version>=py3"
+        if self.image_uri is None and self._only_legacy_mode_supported():
+            legacy_image_uri = image_uris.retrieve(
+                "tensorflow",
+                self.sagemaker_session.boto_region_name,
+                instance_type=self.instance_type,
+                version=self.framework_version,
+                py_version=self.py_version,
+                image_scope="training",
             )
 
-    if err_msg:
-        raise ValueError(err_msg)
+            msg = (
+                "TF {} supports only legacy mode. Please supply the image URI directly with "
+                "'image_uri={}' and set 'model_dir=False'. If you are using any legacy parameters "
+                "(training_steps, evaluation_steps, checkpoint_path, requirements_file), "
+                "make sure to pass them directly as hyperparameters instead. For more, see "
+                "https://sagemaker.readthedocs.io/en/v2.0.0.rc0/frameworks/tensorflow/upgrade_from_legacy.html."
+            ).format(self.framework_version, legacy_image_uri)
+
+            raise ValueError(msg)
+
+    def _only_legacy_mode_supported(self):
+        """Placeholder docstring"""
+        return version.Version(self.framework_version) <= self._HIGHEST_LEGACY_MODE_ONLY_VERSION
+
+    def _only_python_3_supported(self):
+        """Placeholder docstring"""
+        return version.Version(self.framework_version) > self._HIGHEST_PYTHON_2_VERSION
+
+    @classmethod
+    def _prepare_init_params_from_job_description(cls, job_details, model_channel_name=None):
+        """Convert the job description to init params that can be handled by the class constructor
+
+        Args:
+            job_details: the returned job details from a describe_training_job API call.
+
+        Returns:
+             dictionary: The transformed init_params
+
+        """
+        init_params = super(TensorFlow, cls)._prepare_init_params_from_job_description(
+            job_details, model_channel_name
+        )
 
+        image_uri = init_params.pop("image_uri")
+        framework, py_version, tag, script_mode = fw.framework_name_from_image(image_uri)
 
-def python_deprecation_warning(framework, latest_supported_version):
-    """Placeholder docstring"""
-    return PYTHON_2_DEPRECATION_WARNING.format(
-        framework=framework, latest_supported_version=latest_supported_version
-    )
+        if not framework:
+            # If we were unable to parse the framework name from the image, it is not one of our
+            # officially supported images, so just add the image to the init params.
+            init_params["image_uri"] = image_uri
+            return init_params
+
+        model_dir = init_params["hyperparameters"].pop("model_dir", None)
+        if model_dir:
+            init_params["model_dir"] = model_dir
+        elif script_mode is None:
+            init_params["model_dir"] = False
+
+        init_params["py_version"] = py_version
+
+        # We switched image tagging scheme from regular image version (e.g. '1.0') to more
+        # expressive containing framework version, device type and python version
+        # (e.g. '1.5-gpu-py2'). For backward compatibility map deprecated image tag '1.0' to a
+        # '1.4' framework version otherwise extract framework version from the tag itself.
+        init_params["framework_version"] = (
+            "1.4" if tag == "1.0" else fw.framework_version_from_tag(tag)
+        )
 
+        # Legacy images are required to be passed in explicitly.
+        if not script_mode:
+            init_params["image_uri"] = image_uri
 
-def _region_supports_debugger(region_name):
-    """Returns boolean indicating whether the region supports Amazon SageMaker Debugger.
+        if framework != cls._framework_name:
+            raise ValueError(
+                "Training job: {} didn't use image for requested framework".format(
+                    job_details["TrainingJobName"]
+                )
+            )
 
-    Args:
-        region_name (str): Name of the region to check against.
+        return init_params
 
-    Returns:
-        bool: Whether or not the region supports Amazon SageMaker Debugger.
+    def create_model(
+        self,
+        role=None,
+        vpc_config_override=VPC_CONFIG_DEFAULT,
+        entry_point=None,
+        source_dir=None,
+        dependencies=None,
+        **kwargs,
+    ):
+        """Creates ``TensorFlowModel`` object to be used for creating SageMaker model entities.
 
-    """
-    return region_name.lower() not in DEBUGGER_UNSUPPORTED_REGIONS
+        This can be done by deploying it to a SageMaker endpoint,
+        or starting SageMaker Batch Transform jobs.
 
+        Args:
+            role (str): The ``TensorFlowModel``, which is also used during transform jobs.
+                If not specified, the role from the Estimator is used.
+            vpc_config_override (dict[str, list[str]]): Optional override for VpcConfig set on the
+                model. Default: use subnets and security groups from this Estimator.
+
+                * 'Subnets' (list[str]): List of subnet ids.
+                * 'SecurityGroupIds' (list[str]): List of security group ids.
+
+            entry_point (str): Path (absolute or relative) to the local Python source file which
+                should be executed as the entry point to training. If ``source_dir`` is specified,
+                then ``entry_point`` must point to a file located at the root of ``source_dir``.
+                If not specified and ``endpoint_type`` is 'tensorflow-serving',
+                no entry point is used. If ``endpoint_type`` is also ``None``,
+                then the training entry point is used.
+            source_dir (str): Path (absolute or relative or an S3 URI) to a directory with any other
+                serving source code dependencies aside from the entry point file (default: None).
+            dependencies (list[str]): A list of paths to directories (absolute or relative) with
+                any additional libraries that will be exported to the container (default: None).
+            **kwargs: Additional kwargs passed to
+                :class:`~sagemaker.tensorflow.model.TensorFlowModel`.
+
+        Returns:
+            sagemaker.tensorflow.model.TensorFlowModel: A ``TensorFlowModel`` object.
+                See :class:`~sagemaker.tensorflow.model.TensorFlowModel` for full details.
+        """
+        kwargs["name"] = self._get_or_create_name(kwargs.get("name"))
+
+        if "image_uri" not in kwargs:
+            kwargs["image_uri"] = self.image_uri
+
+        if "enable_network_isolation" not in kwargs:
+            kwargs["enable_network_isolation"] = self.enable_network_isolation()
+
+        return TensorFlowModel(
+            model_data=self.model_data,
+            role=role or self.role,
+            container_log_level=self.container_log_level,
+            framework_version=self.framework_version,
+            sagemaker_session=self.sagemaker_session,
+            vpc_config=self.get_vpc_config(vpc_config_override),
+            entry_point=entry_point,
+            source_dir=source_dir,
+            dependencies=dependencies,
+            **kwargs,
+        )
 
-def _region_supports_profiler(region_name):
-    """Returns bool indicating whether region supports Amazon SageMaker Debugger profiling feature.
+    def hyperparameters(self):
+        """Return hyperparameters used by your custom TensorFlow code during model training."""
+        hyperparameters = super(TensorFlow, self).hyperparameters()
+        additional_hyperparameters = self._distribution_configuration(self.distribution)
+
+        if self.model_dir is not False:
+            self.model_dir = self.model_dir or self._default_s3_path(
+                "model", mpi=additional_hyperparameters.get(self.LAUNCH_MPI_ENV_NAME, False)
+            )
+            additional_hyperparameters["model_dir"] = self.model_dir
 
-    Args:
-        region_name (str): Name of the region to check against.
+        hyperparameters.update(
+            EstimatorBase._json_encode_hyperparameters(additional_hyperparameters)
+        )
 
-    Returns:
-        bool: Whether or not the region supports Amazon SageMaker Debugger profiling feature.
+        if self.compiler_config:
+            training_compiler_hyperparameters = self.compiler_config._to_hyperparameter_dict()
+            hyperparameters.update(
+                EstimatorBase._json_encode_hyperparameters(training_compiler_hyperparameters)
+            )
 
-    """
-    return region_name.lower() not in PROFILER_UNSUPPORTED_REGIONS
+        return hyperparameters
 
+    def _default_s3_path(self, directory, mpi=False):
+        """Placeholder docstring"""
+        local_code = utils.get_config_value("local.local_code", self.sagemaker_session.config)
+        if self.sagemaker_session.local_mode and local_code:
+            return "/opt/ml/shared/{}".format(directory)
+        if mpi:
+            return "/opt/ml/model"
+        if self._current_job_name:
+            if is_pipeline_variable(self.output_path):
+                output_path = "s3://{}".format(self.sagemaker_session.default_bucket())
+                return s3.s3_path_join(output_path, self._current_job_name, directory)
+            return s3.s3_path_join(self.output_path, self._current_job_name, directory)
+        return None
+
+    def _validate_and_set_debugger_configs(self):
+        """Disable Debugger Hook Config for ParameterServer (PS) as it is not supported in smdebug.
+
+        Else, set default HookConfig
+        """
+        super(TensorFlow, self)._validate_and_set_debugger_configs()
+        ps_enabled = "parameter_server" in self.distribution and self.distribution[
+            "parameter_server"
+        ].get("enabled", False)
+        if ps_enabled:
+            if self.debugger_hook_config is not None or self.debugger_rule_configs is not None:
+                logger.info(
+                    "Amazon SageMaker Debugger does not currently support "
+                    "Parameter Server distribution"
+                )
+            self.debugger_hook_config = None
+            self.debugger_rule_configs = None
+
+    def transformer(
+        self,
+        instance_count,
+        instance_type,
+        strategy=None,
+        assemble_with=None,
+        output_path=None,
+        output_kms_key=None,
+        accept=None,
+        env=None,
+        max_concurrent_transforms=None,
+        max_payload=None,
+        tags=None,
+        role=None,
+        volume_kms_key=None,
+        entry_point=None,
+        vpc_config_override=VPC_CONFIG_DEFAULT,
+        enable_network_isolation=None,
+        model_name=None,
+    ):
+        """Return a ``Transformer`` that uses a SageMaker Model based on the training job.
 
-def validate_version_or_image_args(framework_version, py_version, image_uri):
-    """Checks if version or image arguments are specified.
+        It reuses the SageMaker Session and base job name used by the Estimator.
 
-    Validates framework and model arguments to enforce version or image specification.
+        Args:
+            instance_count (int): Number of EC2 instances to use.
+            instance_type (str): Type of EC2 instance to use, for example, 'ml.c4.xlarge'.
+            strategy (str): The strategy used to decide how to batch records in a single request
+                (default: None). Valid values: 'MultiRecord' and 'SingleRecord'.
+            assemble_with (str): How the output is assembled (default: None). Valid values: 'Line'
+                or 'None'.
+            output_path (str): S3 location for saving the transform result. If not specified,
+                results are stored to a default bucket.
+            output_kms_key (str): Optional. KMS key ID for encrypting the transform output
+                (default: None).
+            accept (str): The accept header passed by the client to
+                the inference endpoint. If it is supported by the endpoint,
+                it will be the format of the batch transform output.
+            env (dict): Environment variables to be set for use during the transform job
+                (default: None).
+            max_concurrent_transforms (int): The maximum number of HTTP requests to be made to
+                each individual transform container at one time.
+            max_payload (int): Maximum size of the payload in a single HTTP request to the
+                container in MB.
+            tags (list[dict]): List of tags for labeling a transform job. If none specified, then
+                the tags used for the training job are used for the transform job.
+            role (str): The IAM Role ARN for the ``TensorFlowModel``, which is also used
+                during transform jobs. If not specified, the role from the Estimator is used.
+            volume_kms_key (str): Optional. KMS key ID for encrypting the volume attached to the ML
+                compute instance (default: None).
+            entry_point (str): Path (absolute or relative) to the local Python source file which
+                should be executed as the entry point to training. If ``source_dir`` is specified,
+                then ``entry_point`` must point to a file located at the root of ``source_dir``.
+                If not specified and ``endpoint_type`` is 'tensorflow-serving',
+                no entry point is used. If ``endpoint_type`` is also ``None``,
+                then the training entry point is used.
+            vpc_config_override (dict[str, list[str]]): Optional override for
+                the VpcConfig set on the model.
+                Default: use subnets and security groups from this Estimator.
+
+                * 'Subnets' (list[str]): List of subnet ids.
+                * 'SecurityGroupIds' (list[str]): List of security group ids.
+
+            enable_network_isolation (bool): Specifies whether container will
+                run in network isolation mode. Network isolation mode restricts
+                the container access to outside networks (such as the internet).
+                The container does not make any inbound or outbound network
+                calls. If True, a channel named "code" will be created for any
+                user entry script for inference. Also known as Internet-free mode.
+                If not specified, this setting is taken from the estimator's
+                current configuration.
+            model_name (str): Name to use for creating an Amazon SageMaker
+                model. If not specified, the estimator generates a default job name
+                based on the training image name and current timestamp.
+        """
+        role = role or self.role
+        model_name = self._get_or_create_name(model_name)
+
+        if self.latest_training_job is None:
+            logger.warning(
+                "No finished training job found associated with this estimator. Please make sure "
+                "this estimator is only used for building workflow config"
+            )
+            return Transformer(
+                model_name,
+                instance_count,
+                instance_type,
+                strategy=strategy,
+                assemble_with=assemble_with,
+                output_path=output_path,
+                output_kms_key=output_kms_key,
+                accept=accept,
+                max_concurrent_transforms=max_concurrent_transforms,
+                max_payload=max_payload,
+                env=env or {},
+                tags=tags,
+                base_transform_job_name=self.base_job_name,
+                volume_kms_key=volume_kms_key,
+                sagemaker_session=self.sagemaker_session,
+            )
 
-    Args:
-        framework_version (str): The version of the framework.
-        py_version (str): The version of Python.
-        image_uri (str): The URI of the image.
+        if enable_network_isolation is None:
+            enable_network_isolation = self.enable_network_isolation()
 
-    Raises:
-        ValueError: if `image_uri` is None and either `framework_version` or `py_version` is
-            None.
-    """
-    if (framework_version is None or py_version is None) and image_uri is None:
-        raise ValueError(
-            "framework_version or py_version was None, yet image_uri was also None. "
-            "Either specify both framework_version and py_version, or specify image_uri."
+        model = self.create_model(
+            role=role,
+            vpc_config_override=vpc_config_override,
+            entry_point=entry_point,
+            enable_network_isolation=enable_network_isolation,
+            name=model_name,
         )
 
-
-def create_image_uri(
-    region,
-    framework,
-    instance_type,
-    framework_version,
-    py_version=None,
-    account=None,  # pylint: disable=W0613
-    accelerator_type=None,
-    optimized_families=None,  # pylint: disable=W0613
-):
-    """Deprecated method. Please use sagemaker.image_uris.retrieve().
-
-    Args:
-        region (str): AWS region where the image is uploaded.
-        framework (str): framework used by the image.
-        instance_type (str): SageMaker instance type. Used to determine device
-            type (cpu/gpu/family-specific optimized).
-        framework_version (str): The version of the framework.
-        py_version (str): Optional. Python version. If specified, should be one
-            of 'py2' or 'py3'. If not specified, image uri will not include a
-            python component.
-        account (str): AWS account that contains the image. (default:
-            '520713654638')
-        accelerator_type (str): SageMaker Elastic Inference accelerator type.
-        optimized_families (str): Deprecated. A no-op argument.
-
-    Returns:
-        the image uri
-    """
-    renamed_warning("The method create_image_uri")
-    return sagemaker.image_uris.retrieve(
-        framework=framework,
-        region=region,
-        version=framework_version,
-        py_version=py_version,
-        instance_type=instance_type,
-        accelerator_type=accelerator_type,
-    )
+        return model.transformer(
+            instance_count,
+            instance_type,
+            strategy=strategy,
+            assemble_with=assemble_with,
+            output_path=output_path,
+            output_kms_key=output_kms_key,
+            accept=accept,
+            env=env,
+            max_concurrent_transforms=max_concurrent_transforms,
+            max_payload=max_payload,
+            tags=tags,
+            volume_kms_key=volume_kms_key,
+        )
```

### Comparing `sagemaker-2.98.0/src/sagemaker/git_utils.py` & `sagemaker-2.99.0/src/sagemaker/git_utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/huggingface/__init__.py` & `sagemaker-2.99.0/src/sagemaker/huggingface/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/huggingface/estimator.py` & `sagemaker-2.99.0/src/sagemaker/huggingface/estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/huggingface/model.py` & `sagemaker-2.99.0/src/sagemaker/huggingface/model.py`

 * *Files 3% similar despite different names*

```diff
@@ -302,14 +302,20 @@
         metadata_properties=None,
         marketplace_cert=False,
         approval_status=None,
         description=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
             inference_instances (list): A list of the instance types that are used to
@@ -333,14 +339,26 @@
                 or "PendingManualApproval". Defaults to ``PendingManualApproval``.
             description (str): Model Package description. Defaults to ``None``.
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
 
         Returns:
             A `sagemaker.model.ModelPackage` instance.
         """
         instance_type = inference_instances[0] if inference_instances else None
         self._init_sagemaker_session_if_does_not_exist(instance_type)
 
@@ -363,14 +381,20 @@
             metadata_properties,
             marketplace_cert,
             approval_status,
             description,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
+            framework=framework,
+            framework_version=framework_version,
+            nearest_model_name=nearest_model_name,
+            data_input_configuration=data_input_configuration,
         )
 
     def prepare_container_def(
         self, instance_type=None, accelerator_type=None, serverless_inference_config=None
     ):
         """A container definition with framework configuration set in model environment variables.
```

### Comparing `sagemaker-2.98.0/src/sagemaker/huggingface/processing.py` & `sagemaker-2.99.0/src/sagemaker/huggingface/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/huggingface/training_compiler/config.py` & `sagemaker-2.99.0/src/sagemaker/huggingface/training_compiler/config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/hyperparameters.py` & `sagemaker-2.99.0/src/sagemaker/hyperparameters.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/autogluon.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/autogluon.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/blazingtext.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/blazingtext.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/chainer.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/chainer.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/clarify.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/clarify.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/coach-mxnet.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/coach-mxnet.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/coach-tensorflow.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/coach-tensorflow.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/data-wrangler.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/data-wrangler.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/debugger.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/debugger.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/factorization-machines.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/factorization-machines.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/forecasting-deepar.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/forecasting-deepar.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/huggingface-neuron.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/huggingface-neuron.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/huggingface-training-compiler.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/huggingface-training-compiler.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/huggingface.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/huggingface.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/image-classification-neo.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/image-classification-neo.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/image-classification.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/image-classification.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/inferentia-mxnet.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/inferentia-mxnet.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/inferentia-pytorch.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/inferentia-pytorch.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/inferentia-tensorflow.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/inferentia-tensorflow.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/ipinsights.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/ipinsights.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/kmeans.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/kmeans.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/knn.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/knn.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/lda.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/lda.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/linear-learner.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/linear-learner.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/model-monitor.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/model-monitor.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/mxnet.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/mxnet.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/neo-mxnet.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/neo-mxnet.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/neo-pytorch.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/neo-pytorch.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/neo-tensorflow.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/neo-tensorflow.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/ntm.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/ntm.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/object-detection.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/object-detection.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/object2vec.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/object2vec.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/pca.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/pca.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/pytorch.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/pytorch.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/randomcutforest.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/randomcutforest.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/ray-pytorch.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/ray-pytorch.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/ray-tensorflow.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/ray-tensorflow.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/semantic-segmentation.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/semantic-segmentation.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/seq2seq.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/seq2seq.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/sklearn.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/sklearn.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/spark.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/spark.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/sparkml-serving.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/sparkml-serving.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/tensorflow.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/tensorflow.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/vw.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/vw.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/xgboost-neo.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/xgboost-neo.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uri_config/xgboost.json` & `sagemaker-2.99.0/src/sagemaker/image_uri_config/xgboost.json`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/image_uris.py` & `sagemaker-2.99.0/src/sagemaker/image_uris.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/inputs.py` & `sagemaker-2.99.0/src/sagemaker/inputs.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,39 +31,51 @@
         self,
         s3_data,
         distribution=None,
         compression=None,
         content_type=None,
         record_wrapping=None,
         s3_data_type="S3Prefix",
+        instance_groups=None,
         input_mode=None,
         attribute_names=None,
         target_attribute_name=None,
         shuffle_config=None,
     ):
-        """Create a definition for input data used by an SageMaker training job.
+        r"""Create a definition for input data used by an SageMaker training job.
 
-        See AWS documentation on the ``CreateTrainingJob`` API for more details on the parameters.
+        See AWS documentation on the ``CreateTrainingJob`` API for more details
+        on the parameters.
 
         Args:
-            s3_data (str): Defines the location of s3 data to train on.
-            distribution (str): Valid values: 'FullyReplicated', 'ShardedByS3Key'
-                (default: 'FullyReplicated').
-            compression (str): Valid values: 'Gzip', None (default: None). This is used only in
+            s3_data (str): Defines the location of S3 data to train on.
+            distribution (str): Valid values: ``'FullyReplicated'``,
+            ``'ShardedByS3Key'``
+                (default: ``'FullyReplicated'``).
+            compression (str): Valid values: ``'Gzip'``, ``None`` (default: None).
+            This is used only in
                 Pipe input mode.
             content_type (str): MIME type of the input data (default: None).
             record_wrapping (str): Valid values: 'RecordIO' (default: None).
-            s3_data_type (str): Valid values: 'S3Prefix', 'ManifestFile', 'AugmentedManifestFile'.
-                If 'S3Prefix', ``s3_data`` defines a prefix of s3 objects to train on.
+            s3_data_type (str): Valid values: ``'S3Prefix'``, ``'ManifestFile'``,
+            ``'AugmentedManifestFile'``.
+                If ``'S3Prefix'``, ``s3_data`` defines a prefix of s3 objects to train on.
                 All objects with s3 keys beginning with ``s3_data`` will be used to train.
-                If 'ManifestFile' or 'AugmentedManifestFile', then ``s3_data`` defines a
-                single S3 manifest file or augmented manifest file (respectively),
+                If ``'ManifestFile'`` or ``'AugmentedManifestFile'``,
+                then ``s3_data`` defines a
+                single S3 manifest file or augmented manifest file respectively,
                 listing the S3 data to train on. Both the ManifestFile and
-                AugmentedManifestFile formats are described in the SageMaker API documentation:
-                https://docs.aws.amazon.com/sagemaker/latest/dg/API_S3DataSource.html
+                AugmentedManifestFile formats are described at `S3DataSource
+                <https://docs.aws.amazon.com/sagemaker/latest/dg/API_S3DataSource.html>`_
+                in the `Amazon SageMaker API reference`.
+            instance_groups (list[str]): Optional. A list of ``instance_group_name``\ s
+                of a heterogeneous cluster that's configured using the
+                :class:`sagemaker.instance_group.InstanceGroup`.
+                S3 data will be sent to all instance groups in the specified list.
+                (default: None)
             input_mode (str): Optional override for this channel's input mode (default: None).
                 By default, channels will use the input mode defined on
                 ``sagemaker.estimator.EstimatorBase.input_mode``, but they will ignore
                 that setting if this parameter is set.
 
                     * None - Amazon SageMaker will use the input mode specified in the ``Estimator``
                     * 'File' - Amazon SageMaker copies the training dataset from the S3 location to
@@ -93,14 +105,16 @@
 
         if compression is not None:
             self.config["CompressionType"] = compression
         if content_type is not None:
             self.config["ContentType"] = content_type
         if record_wrapping is not None:
             self.config["RecordWrapperType"] = record_wrapping
+        if instance_groups is not None:
+            self.config["DataSource"]["S3DataSource"]["InstanceGroupNames"] = instance_groups
         if input_mode is not None:
             self.config["InputMode"] = input_mode
         if attribute_names is not None:
             self.config["DataSource"]["S3DataSource"]["AttributeNames"] = attribute_names
         if target_attribute_name is not None:
             self.config["TargetAttributeName"] = target_attribute_name
         if shuffle_config is not None:
```

### Comparing `sagemaker-2.98.0/src/sagemaker/job.py` & `sagemaker-2.99.0/src/sagemaker/job.py`

 * *Files 12% similar despite different names*

```diff
@@ -70,14 +70,15 @@
             if expand_role
             else estimator.role
         )
         output_config = _Job._prepare_output_config(estimator.output_path, estimator.output_kms_key)
         resource_config = _Job._prepare_resource_config(
             estimator.instance_count,
             estimator.instance_type,
+            estimator.instance_groups,
             estimator.volume_size,
             estimator.volume_kms_key,
         )
         stop_condition = _Job._prepare_stop_condition(estimator.max_run, estimator.max_wait)
         vpc_config = estimator.get_vpc_config()
 
         model_channel = _Job._prepare_channel(
@@ -279,23 +280,39 @@
         """Placeholder docstring"""
         config = {"S3OutputPath": s3_path}
         if kms_key_id is not None:
             config["KmsKeyId"] = kms_key_id
         return config
 
     @staticmethod
-    def _prepare_resource_config(instance_count, instance_type, volume_size, volume_kms_key):
+    def _prepare_resource_config(
+        instance_count, instance_type, instance_groups, volume_size, volume_kms_key
+    ):
         """Placeholder docstring"""
         resource_config = {
-            "InstanceCount": instance_count,
-            "InstanceType": instance_type,
             "VolumeSizeInGB": volume_size,
         }
         if volume_kms_key is not None:
             resource_config["VolumeKmsKeyId"] = volume_kms_key
+        if instance_groups is not None:
+            if instance_count is not None or instance_type is not None:
+                raise ValueError(
+                    "instance_count and instance_type cannot be set when instance_groups is set"
+                )
+
+            resource_config["InstanceGroups"] = [
+                group._to_request_dict() for group in instance_groups
+            ]
+        else:
+            if instance_count is None or instance_type is None:
+                raise ValueError(
+                    "instance_count and instance_type must be set if instance_groups is not set"
+                )
+            resource_config["InstanceCount"] = instance_count
+            resource_config["InstanceType"] = instance_type
 
         return resource_config
 
     @staticmethod
     def _prepare_stop_condition(max_run, max_wait):
         """Placeholder docstring"""
         if max_wait:
```

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/accessors.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/accessors.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/artifacts.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/artifacts.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/cache.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/cache.py`

 * *Files 1% similar despite different names*

```diff
@@ -211,15 +211,15 @@
                 f"'{sm_version_to_use}' so you can use version "
                 f"'{model_version_to_use_incompatible_with_sagemaker}' of '{model_id}'."
             )
             raise KeyError(error_msg)
 
         error_msg = f"Unable to find model manifest for '{model_id}' with version '{version}'. "
         error_msg += (
-            "Visit https://sagemaker.readthedocs.io/en/stable/doc_utils/jumpstart.html"
+            "Visit https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html"
             " for updated list of models. "
         )
 
         other_model_id_version = self._select_version(
             "*", versions_incompatible_with_sagemaker
         )  # all versions here are incompatible with sagemaker
         if other_model_id_version is not None:
```

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/constants.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/constants.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/enums.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/enums.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/exceptions.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/exceptions.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/filters.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/filters.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/notebook_utils.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/notebook_utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/parameters.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/parameters.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/types.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/types.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/utils.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/jumpstart/validators.py` & `sagemaker-2.99.0/src/sagemaker/jumpstart/validators.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lambda_helper.py` & `sagemaker-2.99.0/src/sagemaker/lambda_helper.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/__init__.py` & `sagemaker-2.99.0/src/sagemaker/lineage/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/_api_types.py` & `sagemaker-2.99.0/src/sagemaker/lineage/_api_types.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/_utils.py` & `sagemaker-2.99.0/src/sagemaker/lineage/_utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/action.py` & `sagemaker-2.99.0/src/sagemaker/lineage/action.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/artifact.py` & `sagemaker-2.99.0/src/sagemaker/lineage/artifact.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/association.py` & `sagemaker-2.99.0/src/sagemaker/lineage/association.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/context.py` & `sagemaker-2.99.0/src/sagemaker/lineage/context.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/lineage_trial_component.py` & `sagemaker-2.99.0/src/sagemaker/lineage/lineage_trial_component.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/query.py` & `sagemaker-2.99.0/src/sagemaker/lineage/query.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/lineage/visualizer.py` & `sagemaker-2.99.0/src/sagemaker/lineage/visualizer.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/local/__init__.py` & `sagemaker-2.99.0/src/sagemaker/local/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/local/data.py` & `sagemaker-2.99.0/src/sagemaker/local/data.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/local/entities.py` & `sagemaker-2.99.0/src/sagemaker/local/entities.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/local/image.py` & `sagemaker-2.99.0/src/sagemaker/local/image.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/local/local_session.py` & `sagemaker-2.99.0/src/sagemaker/local/local_session.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/local/utils.py` & `sagemaker-2.99.0/src/sagemaker/local/utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/logs.py` & `sagemaker-2.99.0/src/sagemaker/logs.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/metadata_properties.py` & `sagemaker-2.99.0/src/sagemaker/metadata_properties.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model.py` & `sagemaker-2.99.0/src/sagemaker/model.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,15 +31,18 @@
     git_utils,
 )
 from sagemaker.deprecations import removed_kwargs
 from sagemaker.predictor import PredictorBase
 from sagemaker.serverless import ServerlessInferenceConfig
 from sagemaker.transformer import Transformer
 from sagemaker.jumpstart.utils import add_jumpstart_tags, get_jumpstart_base_name_if_jumpstart_model
-from sagemaker.utils import unique_name_from_base
+from sagemaker.utils import (
+    unique_name_from_base,
+    update_container_with_inference_params,
+)
 from sagemaker.async_inference import AsyncInferenceConfig
 from sagemaker.predictor_async import AsyncPredictor
 from sagemaker.workflow import is_pipeline_variable
 from sagemaker.workflow.pipeline_context import runnable_by_pipeline, PipelineSession
 
 LOGGER = logging.getLogger("sagemaker")
 
@@ -306,14 +309,20 @@
         marketplace_cert=False,
         approval_status=None,
         description=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         validation_specification=None,
         domain=None,
+        task=None,
+        sample_payload_url=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
             inference_instances (list): A list of the instance types that are used to
@@ -335,28 +344,52 @@
                 or "PendingManualApproval" (default: "PendingManualApproval").
             description (str): Model Package description (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
 
         Returns:
             A `sagemaker.model.ModelPackage` instance or pipeline step arguments
             in case the Model instance is built with
             :class:`~sagemaker.workflow.pipeline_context.PipelineSession`
         """
         if self.model_data is None:
             raise ValueError("SageMaker Model Package cannot be created without model data.")
         if image_uri is not None:
             self.image_uri = image_uri
+
         if model_package_group_name is not None:
             container_def = self.prepare_container_def()
+            update_container_with_inference_params(
+                framework=framework,
+                framework_version=framework_version,
+                nearest_model_name=nearest_model_name,
+                data_input_configuration=data_input_configuration,
+                container_obj=container_def,
+            )
         else:
-            container_def = {"Image": self.image_uri, "ModelDataUrl": self.model_data}
+            container_def = {
+                "Image": self.image_uri,
+                "ModelDataUrl": self.model_data,
+            }
+
         model_pkg_args = sagemaker.get_model_package_args(
             content_types,
             response_types,
             inference_instances=inference_instances,
             transform_instances=transform_instances,
             model_package_name=model_package_name,
             model_package_group_name=model_package_group_name,
@@ -366,14 +399,16 @@
             approval_status=approval_status,
             description=description,
             container_def_list=[container_def],
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             validation_specification=validation_specification,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
         )
         model_package = self.sagemaker_session.create_model_package_from_containers(
             **model_pkg_args
         )
         if isinstance(self.sagemaker_session, PipelineSession):
             return None
         return ModelPackage(
```

### Comparing `sagemaker-2.98.0/src/sagemaker/model_metrics.py` & `sagemaker-2.99.0/src/sagemaker/model_metrics.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_monitor/__init__.py` & `sagemaker-2.99.0/src/sagemaker/model_monitor/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_monitor/clarify_model_monitoring.py` & `sagemaker-2.99.0/src/sagemaker/model_monitor/clarify_model_monitoring.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_monitor/cron_expression_generator.py` & `sagemaker-2.99.0/src/sagemaker/model_monitor/cron_expression_generator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_monitor/data_capture_config.py` & `sagemaker-2.99.0/src/sagemaker/model_monitor/data_capture_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_monitor/dataset_format.py` & `sagemaker-2.99.0/src/sagemaker/model_monitor/dataset_format.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_monitor/model_monitoring.py` & `sagemaker-2.99.0/src/sagemaker/model_monitor/model_monitoring.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_monitor/monitoring_files.py` & `sagemaker-2.99.0/src/sagemaker/model_monitor/monitoring_files.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/model_uris.py` & `sagemaker-2.99.0/src/sagemaker/model_uris.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/multidatamodel.py` & `sagemaker-2.99.0/src/sagemaker/multidatamodel.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/mxnet/__init__.py` & `sagemaker-2.99.0/src/sagemaker/mxnet/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/mxnet/defaults.py` & `sagemaker-2.99.0/src/sagemaker/mxnet/defaults.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/mxnet/estimator.py` & `sagemaker-2.99.0/src/sagemaker/mxnet/estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/mxnet/model.py` & `sagemaker-2.99.0/src/sagemaker/mxnet/model.py`

 * *Files 11% similar despite different names*

```diff
@@ -155,14 +155,20 @@
         metadata_properties=None,
         marketplace_cert=False,
         approval_status=None,
         description=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
             inference_instances (list): A list of the instance types that are used to
@@ -184,14 +190,26 @@
                 or "PendingManualApproval" (default: "PendingManualApproval").
             description (str): Model Package description (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
 
         Returns:
             A `sagemaker.model.ModelPackage` instance.
         """
         instance_type = inference_instances[0] if inference_instances else None
         self._init_sagemaker_session_if_does_not_exist(instance_type)
 
@@ -214,14 +232,20 @@
             metadata_properties,
             marketplace_cert,
             approval_status,
             description,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
+            framework=framework,
+            framework_version=framework_version,
+            nearest_model_name=nearest_model_name,
+            data_input_configuration=data_input_configuration,
         )
 
     def prepare_container_def(
         self, instance_type=None, accelerator_type=None, serverless_inference_config=None
     ):
         """Return a container definition with framework configuration.
```

### Comparing `sagemaker-2.98.0/src/sagemaker/mxnet/processing.py` & `sagemaker-2.99.0/src/sagemaker/mxnet/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/network.py` & `sagemaker-2.99.0/src/sagemaker/network.py`

 * *Files 12% similar despite different names*

```diff
@@ -12,27 +12,31 @@
 # language governing permissions and limitations under the License.
 """This file contains code related to network configuration.
 
 It also includes encryption, network isolation, and VPC configurations.
 """
 from __future__ import absolute_import
 
+from typing import Union, Optional, List
+
+from sagemaker.workflow.entities import PipelineVariable
+
 
 class NetworkConfig(object):
     """Accepts network configuration parameters for conversion to request dict.
 
     The `_to_request_dict` provides a method to turn the parameters into a dict.
     """
 
     def __init__(
         self,
-        enable_network_isolation=False,
-        security_group_ids=None,
-        subnets=None,
-        encrypt_inter_container_traffic=None,
+        enable_network_isolation: Union[bool, PipelineVariable] = False,
+        security_group_ids: Optional[List[Union[str, PipelineVariable]]] = None,
+        subnets: Optional[List[Union[str, PipelineVariable]]] = None,
+        encrypt_inter_container_traffic: Optional[Union[bool, PipelineVariable]] = None,
     ):
         """Initialize a ``NetworkConfig`` instance.
 
         NetworkConfig accepts network configuration parameters and provides a method to turn
         these parameters into a dictionary.
 
         Args:
```

### Comparing `sagemaker-2.98.0/src/sagemaker/parameter.py` & `sagemaker-2.99.0/src/sagemaker/parameter.py`

 * *Files 5% similar despite different names*

```diff
@@ -10,28 +10,35 @@
 # distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
 """Placeholder docstring"""
 from __future__ import absolute_import
 
 import json
+from typing import Union
 
 from sagemaker.workflow import is_pipeline_variable
+from sagemaker.workflow.entities import PipelineVariable
 
 
 class ParameterRange(object):
     """Base class for representing parameter ranges.
 
     This is used to define what hyperparameters to tune for an Amazon SageMaker
     hyperparameter tuning job and to verify hyperparameters for Marketplace Algorithms.
     """
 
     __all_types__ = ("Continuous", "Categorical", "Integer")
 
-    def __init__(self, min_value, max_value, scaling_type="Auto"):
+    def __init__(
+        self,
+        min_value: Union[int, float, PipelineVariable],
+        max_value: Union[int, float, PipelineVariable],
+        scaling_type: Union[str, PipelineVariable] = "Auto",
+    ):
         """Initialize a parameter range.
 
         Args:
             min_value (float or int): The minimum value for the range.
             max_value (float or int): The maximum value for the range.
             scaling_type (str): The scale used for searching the range during
                 tuning (default: 'Auto'). Valid values: 'Auto', 'Linear',
```

### Comparing `sagemaker-2.98.0/src/sagemaker/pipeline.py` & `sagemaker-2.99.0/src/sagemaker/pipeline.py`

 * *Files 3% similar despite different names*

```diff
@@ -16,15 +16,18 @@
 from typing import Optional, Dict
 
 import sagemaker
 from sagemaker import ModelMetrics
 from sagemaker.drift_check_baselines import DriftCheckBaselines
 from sagemaker.metadata_properties import MetadataProperties
 from sagemaker.session import Session
-from sagemaker.utils import name_from_image
+from sagemaker.utils import (
+    name_from_image,
+    update_container_with_inference_params,
+)
 from sagemaker.transformer import Transformer
 from sagemaker.workflow.pipeline_context import runnable_by_pipeline
 
 
 class PipelineModel(object):
     """A pipeline of SageMaker `Model` instances.
 
@@ -275,14 +278,20 @@
         metadata_properties: Optional[MetadataProperties] = None,
         marketplace_cert: bool = False,
         approval_status: Optional[str] = None,
         description: Optional[str] = None,
         drift_check_baselines: Optional[DriftCheckBaselines] = None,
         customer_metadata_properties: Optional[Dict[str, str]] = None,
         domain: Optional[str] = None,
+        sample_payload_url: Optional[str] = None,
+        task: Optional[str] = None,
+        framework: Optional[str] = None,
+        framework_version: Optional[str] = None,
+        nearest_model_name: Optional[str] = None,
+        data_input_configuration: Optional[str] = None,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
             inference_instances (list): A list of the instance types that are used to
@@ -304,25 +313,44 @@
                 or "PendingManualApproval" (default: "PendingManualApproval").
             description (str): Model Package description (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
 
         Returns:
             A `sagemaker.model.ModelPackage` instance.
         """
         for model in self.models:
             if model.model_data is None:
                 raise ValueError("SageMaker Model Package cannot be created without model data.")
         if model_package_group_name is not None:
             container_def = self.pipeline_container_def(
                 inference_instances[0] if inference_instances else None
             )
+            update_container_with_inference_params(
+                framework=framework,
+                framework_version=framework_version,
+                nearest_model_name=nearest_model_name,
+                data_input_configuration=data_input_configuration,
+                container_list=container_def,
+            )
         else:
             container_def = [
                 {
                     "Image": image_uri or model.image_uri,
                     "ModelDataUrl": model.model_data,
                 }
                 for model in self.models
@@ -340,14 +368,16 @@
             marketplace_cert=marketplace_cert,
             approval_status=approval_status,
             description=description,
             container_def_list=container_def,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
         )
 
         self.sagemaker_session.create_model_package_from_containers(**model_pkg_args)
 
     def transformer(
         self,
         instance_count,
```

### Comparing `sagemaker-2.98.0/src/sagemaker/predictor.py` & `sagemaker-2.99.0/src/sagemaker/predictor.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/predictor_async.py` & `sagemaker-2.99.0/src/sagemaker/predictor_async.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/processing.py` & `sagemaker-2.99.0/src/sagemaker/processing.py`

 * *Files 4% similar despite different names*

```diff
@@ -18,53 +18,55 @@
 """
 from __future__ import print_function, absolute_import
 
 import os
 import pathlib
 import logging
 from textwrap import dedent
-from typing import Dict, List, Optional
+from typing import Dict, List, Optional, Union
 
 import attr
 
 from six.moves.urllib.parse import urlparse
 from six.moves.urllib.request import url2pathname
 from sagemaker import s3
 from sagemaker.job import _Job
 from sagemaker.local import LocalSession
+from sagemaker.network import NetworkConfig
 from sagemaker.utils import base_name_from_image, get_config_value, name_from_base
 from sagemaker.session import Session
 from sagemaker.workflow import is_pipeline_variable
 from sagemaker.workflow.pipeline_context import runnable_by_pipeline
+from sagemaker.workflow.entities import PipelineVariable
 from sagemaker.dataset_definition.inputs import S3Input, DatasetDefinition
 from sagemaker.apiutils._base_types import ApiObject
 from sagemaker.s3 import S3Uploader
 
 logger = logging.getLogger(__name__)
 
 
 class Processor(object):
     """Handles Amazon SageMaker Processing tasks."""
 
     def __init__(
         self,
-        role,
-        image_uri,
-        instance_count,
-        instance_type,
-        entrypoint=None,
-        volume_size_in_gb=30,
-        volume_kms_key=None,
-        output_kms_key=None,
-        max_runtime_in_seconds=None,
-        base_job_name=None,
-        sagemaker_session=None,
-        env=None,
-        tags=None,
-        network_config=None,
+        role: str,
+        image_uri: Union[str, PipelineVariable],
+        instance_count: Union[int, PipelineVariable],
+        instance_type: Union[str, PipelineVariable],
+        entrypoint: Optional[List[Union[str, PipelineVariable]]] = None,
+        volume_size_in_gb: Union[int, PipelineVariable] = 30,
+        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        max_runtime_in_seconds: Optional[Union[int, PipelineVariable]] = None,
+        base_job_name: Optional[str] = None,
+        sagemaker_session: Optional[Session] = None,
+        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        network_config: Optional[NetworkConfig] = None,
     ):
         """Initializes a ``Processor`` instance.
 
         The ``Processor`` handles Amazon SageMaker Processing tasks.
 
         Args:
             role (str): An AWS IAM role name or ARN. Amazon SageMaker Processing
@@ -129,22 +131,22 @@
                 sagemaker_session = LocalSession(disable_local_code=True)
 
         self.sagemaker_session = sagemaker_session or Session()
 
     @runnable_by_pipeline
     def run(
         self,
-        inputs=None,
-        outputs=None,
-        arguments=None,
-        wait=True,
-        logs=True,
-        job_name=None,
-        experiment_config=None,
-        kms_key=None,
+        inputs: Optional[List["ProcessingInput"]] = None,
+        outputs: Optional[List["ProcessingOutput"]] = None,
+        arguments: Optional[List[Union[str, PipelineVariable]]] = None,
+        wait: bool = True,
+        logs: bool = True,
+        job_name: Optional[str] = None,
+        experiment_config: Optional[Dict[str, str]] = None,
+        kms_key: Optional[str] = None,
     ):
         """Runs a processing job.
 
         Args:
             inputs (list[:class:`~sagemaker.processing.ProcessingInput`]): Input files for
                 the processing job. These must be provided as
                 :class:`~sagemaker.processing.ProcessingInput` objects (default: None).
@@ -384,28 +386,28 @@
 
 
 class ScriptProcessor(Processor):
     """Handles Amazon SageMaker processing tasks for jobs using a machine learning framework."""
 
     def __init__(
         self,
-        role,
-        image_uri,
-        command,
-        instance_count,
-        instance_type,
-        volume_size_in_gb=30,
-        volume_kms_key=None,
-        output_kms_key=None,
-        max_runtime_in_seconds=None,
-        base_job_name=None,
-        sagemaker_session=None,
-        env=None,
-        tags=None,
-        network_config=None,
+        role: str,
+        image_uri: Union[str, PipelineVariable],
+        command: List[str],
+        instance_count: Union[int, PipelineVariable],
+        instance_type: Union[str, PipelineVariable],
+        volume_size_in_gb: Union[int, PipelineVariable] = 30,
+        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        max_runtime_in_seconds: Optional[Union[int, PipelineVariable]] = None,
+        base_job_name: Optional[str] = None,
+        sagemaker_session: Optional[Session] = None,
+        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        network_config: Optional[NetworkConfig] = None,
     ):
         """Initializes a ``ScriptProcessor`` instance.
 
         The ``ScriptProcessor`` handles Amazon SageMaker Processing tasks for jobs
         using a machine learning framework, which allows for providing a script to be
         run as part of the Processing Job.
 
@@ -494,23 +496,23 @@
                 processing job (default: None).
         """
         return RunArgs(code=code, inputs=inputs, outputs=outputs, arguments=arguments)
 
     @runnable_by_pipeline
     def run(
         self,
-        code,
-        inputs=None,
-        outputs=None,
-        arguments=None,
-        wait=True,
-        logs=True,
-        job_name=None,
-        experiment_config=None,
-        kms_key=None,
+        code: str,
+        inputs: Optional[List["ProcessingInput"]] = None,
+        outputs: Optional[List["ProcessingOutput"]] = None,
+        arguments: Optional[List[Union[str, PipelineVariable]]] = None,
+        wait: bool = True,
+        logs: bool = True,
+        job_name: Optional[str] = None,
+        experiment_config: Optional[Dict[str, str]] = None,
+        kms_key: Optional[str] = None,
     ):
         """Runs a processing job.
 
         Args:
             code (str): This can be an S3 URI or a local path to
                 a file with the framework script to run.
             inputs (list[:class:`~sagemaker.processing.ProcessingInput`]): Input files for
@@ -533,14 +535,16 @@
                 * If `ExperimentName` is supplied but `TrialName` is not a Trial will be
                 automatically created and the job's Trial Component associated with the Trial.
                 * If `TrialName` is supplied and the Trial already exists the job's Trial Component
                 will be associated with the Trial.
                 * If both `ExperimentName` and `TrialName` are not supplied the trial component
                 will be unassociated.
                 * `TrialComponentDisplayName` is used for display in Studio.
+            kms_key (str): The ARN of the KMS key that is used to encrypt the
+                user code file (default: None).
         """
         normalized_inputs, normalized_outputs = self._normalize_args(
             job_name=job_name,
             arguments=arguments,
             inputs=inputs,
             outputs=outputs,
             code=code,
@@ -1068,24 +1072,24 @@
     """Accepts parameters that specify an Amazon S3 input for a processing job.
 
     Also provides a method to turn those parameters into a dictionary.
     """
 
     def __init__(
         self,
-        source=None,
-        destination=None,
-        input_name=None,
-        s3_data_type="S3Prefix",
-        s3_input_mode="File",
-        s3_data_distribution_type="FullyReplicated",
-        s3_compression_type="None",
-        s3_input=None,
-        dataset_definition=None,
-        app_managed=False,
+        source: Optional[Union[str, PipelineVariable]] = None,
+        destination: Optional[Union[str, PipelineVariable]] = None,
+        input_name: Optional[Union[str, PipelineVariable]] = None,
+        s3_data_type: Union[str, PipelineVariable] = "S3Prefix",
+        s3_input_mode: Union[str, PipelineVariable] = "File",
+        s3_data_distribution_type: Union[str, PipelineVariable] = "FullyReplicated",
+        s3_compression_type: Union[str, PipelineVariable] = "None",
+        s3_input: Optional[S3Input] = None,
+        dataset_definition: Optional[DatasetDefinition] = None,
+        app_managed: Union[bool, PipelineVariable] = False,
     ):
         """Initializes a ``ProcessingInput`` instance.
 
         ``ProcessingInput`` accepts parameters that specify an Amazon S3 input
         for a processing job and provides a method to turn those parameters into a dictionary.
 
         Args:
@@ -1175,20 +1179,20 @@
     """Accepts parameters that specify an Amazon S3 output for a processing job.
 
     It also provides a method to turn those parameters into a dictionary.
     """
 
     def __init__(
         self,
-        source=None,
-        destination=None,
-        output_name=None,
-        s3_upload_mode="EndOfJob",
-        app_managed=False,
-        feature_store_output=None,
+        source: Optional[Union[str, PipelineVariable]] = None,
+        destination: Optional[Union[str, PipelineVariable]] = None,
+        output_name: Optional[Union[str, PipelineVariable]] = None,
+        s3_upload_mode: Union[str, PipelineVariable] = "EndOfJob",
+        app_managed: Union[bool, PipelineVariable] = False,
+        feature_store_output: Optional["FeatureStoreOutput"] = None,
     ):
         """Initializes a ``ProcessingOutput`` instance.
 
         ``ProcessingOutput`` accepts parameters that specify an Amazon S3 output for a
         processing job and provides a method to turn those parameters into a dictionary.
 
         Args:
@@ -1273,32 +1277,32 @@
     """Handles Amazon SageMaker processing tasks for jobs using a machine learning framework."""
 
     framework_entrypoint_command = ["/bin/bash"]
 
     # Added new (kw)args for estimator. The rest are from ScriptProcessor with same defaults.
     def __init__(
         self,
-        estimator_cls,
-        framework_version,
-        role,
-        instance_count,
-        instance_type,
-        py_version="py3",
-        image_uri=None,
-        command=None,
-        volume_size_in_gb=30,
-        volume_kms_key=None,
-        output_kms_key=None,
-        code_location=None,
-        max_runtime_in_seconds=None,
-        base_job_name=None,
-        sagemaker_session=None,
-        env=None,
-        tags=None,
-        network_config=None,
+        estimator_cls: type,
+        framework_version: str,
+        role: str,
+        instance_count: Union[int, PipelineVariable],
+        instance_type: Union[str, PipelineVariable],
+        py_version: str = "py3",
+        image_uri: Optional[Union[str, PipelineVariable]] = None,
+        command: Optional[List[str]] = None,
+        volume_size_in_gb: Union[int, PipelineVariable] = 30,
+        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        code_location: Optional[str] = None,
+        max_runtime_in_seconds: Optional[Union[int, PipelineVariable]] = None,
+        base_job_name: Optional[str] = None,
+        sagemaker_session: Optional[Session] = None,
+        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        network_config: Optional[NetworkConfig] = None,
     ):
         """Initializes a ``FrameworkProcessor`` instance.
 
         The ``FrameworkProcessor`` handles Amazon SageMaker Processing tasks for jobs
         using a machine learning framework, which allows for a set of Python scripts
         to be run as part of the Processing Job.
 
@@ -1482,26 +1486,26 @@
             inputs=inputs,
             outputs=outputs,
             arguments=arguments,
         )
 
     def run(  # type: ignore[override]
         self,
-        code,
-        source_dir=None,
-        dependencies=None,
-        git_config=None,
-        inputs=None,
-        outputs=None,
-        arguments=None,
-        wait=True,
-        logs=True,
-        job_name=None,
-        experiment_config=None,
-        kms_key=None,
+        code: str,
+        source_dir: Optional[str] = None,
+        dependencies: Optional[List[str]] = None,
+        git_config: Optional[Dict[str, str]] = None,
+        inputs: Optional[List[ProcessingInput]] = None,
+        outputs: Optional[List[ProcessingOutput]] = None,
+        arguments: Optional[List[Union[str, PipelineVariable]]] = None,
+        wait: bool = True,
+        logs: bool = True,
+        job_name: Optional[str] = None,
+        experiment_config: Optional[Dict[str, str]] = None,
+        kms_key: Optional[str] = None,
     ):
         """Runs a processing job.
 
         Args:
             code (str): This can be an S3 URI or a local path to a file with the
                 framework script to run.Path (absolute or relative) to the local
                 Python source file which should be executed as the entry point
```

### Comparing `sagemaker-2.98.0/src/sagemaker/pytorch/__init__.py` & `sagemaker-2.99.0/src/sagemaker/pytorch/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/pytorch/defaults.py` & `sagemaker-2.99.0/src/sagemaker/pytorch/defaults.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/pytorch/estimator.py` & `sagemaker-2.99.0/src/sagemaker/pytorch/estimator.py`

 * *Files 4% similar despite different names*

```diff
@@ -13,23 +13,21 @@
 """Placeholder docstring"""
 from __future__ import absolute_import
 
 import logging
 
 from packaging.version import Version
 
-from sagemaker.deprecations import renamed_kwargs
 from sagemaker.estimator import Framework, EstimatorBase
 from sagemaker.fw_utils import (
     framework_name_from_image,
     framework_version_from_tag,
     python_deprecation_warning,
     validate_version_or_image_args,
-    warn_if_parameter_server_with_multi_gpu,
-    validate_smdistributed,
+    validate_distribution,
 )
 from sagemaker.pytorch import defaults
 from sagemaker.pytorch.model import PyTorchModel
 from sagemaker.vpc_utils import VPC_CONFIG_DEFAULT
 
 logger = logging.getLogger("sagemaker")
 
@@ -192,40 +190,33 @@
         if py_version == "py2":
             logger.warning(
                 python_deprecation_warning(self._framework_name, defaults.LATEST_PY2_VERSION)
             )
         self.framework_version = framework_version
         self.py_version = py_version
 
-        if distribution is not None:
-            instance_type = renamed_kwargs(
-                "train_instance_type", "instance_type", kwargs.get("instance_type"), kwargs
-            )
-
-            validate_smdistributed(
-                instance_type=instance_type,
-                framework_name=self._framework_name,
-                framework_version=framework_version,
-                py_version=py_version,
-                distribution=distribution,
-                image_uri=image_uri,
-            )
-
-            warn_if_parameter_server_with_multi_gpu(
-                training_instance_type=instance_type, distribution=distribution
-            )
-
         if "enable_sagemaker_metrics" not in kwargs:
             # enable sagemaker metrics for PT v1.3 or greater:
             if self.framework_version and Version(self.framework_version) >= Version("1.3"):
                 kwargs["enable_sagemaker_metrics"] = True
 
         super(PyTorch, self).__init__(
             entry_point, source_dir, hyperparameters, image_uri=image_uri, **kwargs
         )
+        if distribution is not None:
+            distribution = validate_distribution(
+                distribution,
+                self.instance_groups,
+                self._framework_name,
+                framework_version,
+                py_version,
+                image_uri,
+                kwargs,
+            )
+
         self.distribution = distribution or {}
 
     def hyperparameters(self):
         """Return hyperparameters used by your custom PyTorch code during model training."""
         hyperparameters = super(PyTorch, self).hyperparameters()
         additional_hyperparameters = self._distribution_configuration(
             distribution=self.distribution
```

### Comparing `sagemaker-2.98.0/src/sagemaker/pytorch/model.py` & `sagemaker-2.99.0/src/sagemaker/pytorch/model.py`

 * *Files 4% similar despite different names*

```diff
@@ -156,14 +156,20 @@
         metadata_properties=None,
         marketplace_cert=False,
         approval_status=None,
         description=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
             inference_instances (list): A list of the instance types that are used to
@@ -185,14 +191,26 @@
                 or "PendingManualApproval" (default: "PendingManualApproval").
             description (str): Model Package description (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
 
         Returns:
             A `sagemaker.model.ModelPackage` instance.
         """
         instance_type = inference_instances[0] if inference_instances else None
         self._init_sagemaker_session_if_does_not_exist(instance_type)
 
@@ -215,14 +233,20 @@
             metadata_properties,
             marketplace_cert,
             approval_status,
             description,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
+            framework=framework,
+            framework_version=framework_version,
+            nearest_model_name=nearest_model_name,
+            data_input_configuration=data_input_configuration,
         )
 
     def prepare_container_def(
         self, instance_type=None, accelerator_type=None, serverless_inference_config=None
     ):
         """A container definition with framework configuration set in model environment variables.
```

### Comparing `sagemaker-2.98.0/src/sagemaker/pytorch/processing.py` & `sagemaker-2.99.0/src/sagemaker/pytorch/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/rl/__init__.py` & `sagemaker-2.99.0/src/sagemaker/rl/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/rl/estimator.py` & `sagemaker-2.99.0/src/sagemaker/rl/estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/s3.py` & `sagemaker-2.99.0/src/sagemaker/s3.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/script_uris.py` & `sagemaker-2.99.0/src/sagemaker/script_uris.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/serializers.py` & `sagemaker-2.99.0/src/sagemaker/serializers.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/serverless/__init__.py` & `sagemaker-2.99.0/src/sagemaker/serverless/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/serverless/model.py` & `sagemaker-2.99.0/src/sagemaker/serverless/model.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/serverless/predictor.py` & `sagemaker-2.99.0/src/sagemaker/serverless/predictor.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/serverless/serverless_inference_config.py` & `sagemaker-2.99.0/src/sagemaker/serverless/serverless_inference_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/session.py` & `sagemaker-2.99.0/src/sagemaker/session.py`

 * *Files 1% similar despite different names*

```diff
@@ -2818,14 +2818,16 @@
         marketplace_cert=False,
         approval_status="PendingManualApproval",
         description=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         validation_specification=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
     ):
         """Get request dictionary for CreateModelPackage API.
 
         Args:
             containers (list): A list of inference containers that can be used for inference
                 specifications of Model Package (default: None).
             content_types (list): The supported MIME types for the input data (default: None).
@@ -2847,14 +2849,19 @@
                 or "PendingManualApproval" (default: "PendingManualApproval").
             description (str): Model Package description (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
         """
 
         model_pkg_request = get_create_model_package_request(
             model_package_name,
             model_package_group_name,
             containers,
             content_types,
@@ -2866,14 +2873,16 @@
             marketplace_cert,
             approval_status,
             description,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             validation_specification=validation_specification,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
         )
 
         def submit(request):
             if model_package_group_name is not None:
                 try:
                     self.sagemaker_client.describe_model_package_group(
                         ModelPackageGroupName=request["ModelPackageGroupName"]
@@ -4237,14 +4246,16 @@
     description=None,
     tags=None,
     container_def_list=None,
     drift_check_baselines=None,
     customer_metadata_properties=None,
     validation_specification=None,
     domain=None,
+    sample_payload_url=None,
+    task=None,
 ):
     """Get arguments for create_model_package method.
 
     Args:
         content_types (list): The supported MIME types for the input data.
         response_types (list): The supported MIME types for the output data.
         inference_instances (list): A list of the instance types that are used to
@@ -4269,14 +4280,19 @@
             (default: None).
         container_def_list (list): A list of container defintiions (default: None).
         drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
         customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
             metadata properties (default: None).
         domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
             "MACHINE_LEARNING" (default: None).
+        sample_payload_url (str): The S3 path where the sample payload is stored (default: None).
+        task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+            "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+            "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+
     Returns:
         dict: A dictionary of method argument names and values.
     """
     if container_def_list is not None:
         containers = container_def_list
     else:
         container = {
@@ -4312,14 +4328,18 @@
         model_package_args["tags"] = tags
     if customer_metadata_properties is not None:
         model_package_args["customer_metadata_properties"] = customer_metadata_properties
     if validation_specification is not None:
         model_package_args["validation_specification"] = validation_specification
     if domain is not None:
         model_package_args["domain"] = domain
+    if sample_payload_url is not None:
+        model_package_args["sample_payload_url"] = sample_payload_url
+    if task is not None:
+        model_package_args["task"] = task
     return model_package_args
 
 
 def get_create_model_package_request(
     model_package_name=None,
     model_package_group_name=None,
     containers=None,
@@ -4333,14 +4353,16 @@
     approval_status="PendingManualApproval",
     description=None,
     tags=None,
     drift_check_baselines=None,
     customer_metadata_properties=None,
     validation_specification=None,
     domain=None,
+    sample_payload_url=None,
+    task=None,
 ):
     """Get request dictionary for CreateModelPackage API.
 
     Args:
         model_package_name (str): Model Package name, exclusive to `model_package_group_name`,
             using `model_package_name` makes the Model Package un-versioned (default: None).
         model_package_group_name (str): Model Package Group name, exclusive to
@@ -4363,14 +4385,18 @@
         tags (List[dict[str, str]]): A list of dictionaries containing key-value pairs
             (default: None).
         drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
         customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
             metadata properties (default: None).
         domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
             "MACHINE_LEARNING" (default: None).
+        sample_payload_url (str): The S3 path where the sample payload is stored (default: None).
+        task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+            "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+            "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
     """
 
     if all([model_package_name, model_package_group_name]):
         raise ValueError(
             "model_package_name and model_package_group_name cannot be present at the " "same time."
         )
     request_dict = {}
@@ -4390,14 +4416,18 @@
         request_dict["MetadataProperties"] = metadata_properties
     if customer_metadata_properties is not None:
         request_dict["CustomerMetadataProperties"] = customer_metadata_properties
     if validation_specification:
         request_dict["ValidationSpecification"] = validation_specification
     if domain is not None:
         request_dict["Domain"] = domain
+    if sample_payload_url is not None:
+        request_dict["SamplePayloadUrl"] = sample_payload_url
+    if task is not None:
+        request_dict["Task"] = task
     if containers is not None:
         if not all([content_types, response_types]):
             raise ValueError(
                 "content_types and response_types " "must be provided if containers is present."
             )
         inference_specification = {
             "Containers": containers,
```

### Comparing `sagemaker-2.98.0/src/sagemaker/session_settings.py` & `sagemaker-2.99.0/src/sagemaker/session_settings.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/sklearn/__init__.py` & `sagemaker-2.99.0/src/sagemaker/sklearn/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/sklearn/defaults.py` & `sagemaker-2.99.0/src/sagemaker/sklearn/defaults.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/sklearn/estimator.py` & `sagemaker-2.99.0/src/sagemaker/sklearn/estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/sklearn/model.py` & `sagemaker-2.99.0/src/sagemaker/sklearn/model.py`

 * *Files 12% similar despite different names*

```diff
@@ -150,14 +150,20 @@
         metadata_properties=None,
         marketplace_cert=False,
         approval_status=None,
         description=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
             inference_instances (list): A list of the instance types that are used to
@@ -179,14 +185,26 @@
                 or "PendingManualApproval" (default: "PendingManualApproval").
             description (str): Model Package description (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
 
         Returns:
             A `sagemaker.model.ModelPackage` instance.
         """
         instance_type = inference_instances[0] if inference_instances else None
         self._init_sagemaker_session_if_does_not_exist(instance_type)
 
@@ -209,14 +227,20 @@
             metadata_properties,
             marketplace_cert,
             approval_status,
             description,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
+            framework=framework,
+            framework_version=framework_version,
+            nearest_model_name=nearest_model_name,
+            data_input_configuration=data_input_configuration,
         )
 
     def prepare_container_def(
         self, instance_type=None, accelerator_type=None, serverless_inference_config=None
     ):
         """Container definition with framework configuration set in model environment variables.
```

### Comparing `sagemaker-2.98.0/src/sagemaker/sklearn/processing.py` & `sagemaker-2.99.0/src/sagemaker/sklearn/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/spark/__init__.py` & `sagemaker-2.99.0/src/sagemaker/spark/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/spark/defaults.py` & `sagemaker-2.99.0/src/sagemaker/spark/defaults.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/spark/processing.py` & `sagemaker-2.99.0/src/sagemaker/spark/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/sparkml/__init__.py` & `sagemaker-2.99.0/src/sagemaker/sparkml/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/sparkml/model.py` & `sagemaker-2.99.0/src/sagemaker/sparkml/model.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/tensorflow/__init__.py` & `sagemaker-2.99.0/src/sagemaker/tensorflow/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/tensorflow/defaults.py` & `sagemaker-2.99.0/src/sagemaker/tensorflow/defaults.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/tensorflow/estimator.py` & `sagemaker-2.99.0/src/sagemaker/workflow/_utils.py`

 * *Files 25% similar despite different names*

```diff
@@ -6,548 +6,461 @@
 #
 #     http://aws.amazon.com/apache2.0/
 #
 # or in the "license" file accompanying this file. This file is
 # distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
-"""An estimator class for training with TensorFlow on Amazon SageMaker."""
+"""Scrapper utilities to support repacking of models."""
 from __future__ import absolute_import
 
-import logging
-
-from packaging import version
-
-from sagemaker import image_uris, s3, utils
-from sagemaker.deprecations import renamed_kwargs
-from sagemaker.estimator import Framework, EstimatorBase
-import sagemaker.fw_utils as fw
-from sagemaker.tensorflow import defaults
-from sagemaker.tensorflow.model import TensorFlowModel
-from sagemaker.transformer import Transformer
-from sagemaker.vpc_utils import VPC_CONFIG_DEFAULT
-from sagemaker.workflow import is_pipeline_variable
-from sagemaker.tensorflow.training_compiler.config import TrainingCompilerConfig
-
-logger = logging.getLogger("sagemaker")
-
-
-class TensorFlow(Framework):
-    """Handle end-to-end training and deployment of user-provided TensorFlow code."""
-
-    _framework_name = "tensorflow"
-
-    _HIGHEST_LEGACY_MODE_ONLY_VERSION = version.Version("1.10.0")
-    _HIGHEST_PYTHON_2_VERSION = version.Version("2.1.1")
+import os
+import shutil
+import tarfile
+import tempfile
+from typing import List, Union, Optional, TYPE_CHECKING
+from sagemaker import image_uris
+from sagemaker.inputs import TrainingInput
+from sagemaker.estimator import EstimatorBase
+from sagemaker.sklearn.estimator import SKLearn
+from sagemaker.workflow.entities import RequestType
+from sagemaker.workflow.properties import Properties
+from sagemaker.session import get_create_model_package_request, get_model_package_args
+from sagemaker.workflow.steps import (
+    StepTypeEnum,
+    TrainingStep,
+    Step,
+    ConfigurableRetryStep,
+)
+from sagemaker.utils import _save_model, download_file_from_url
+from sagemaker.workflow.retry import RetryPolicy
+
+if TYPE_CHECKING:
+    from sagemaker.workflow.step_collections import StepCollection
+
+FRAMEWORK_VERSION = "0.23-1"
+INSTANCE_TYPE = "ml.m5.large"
+REPACK_SCRIPT = "_repack_model.py"
+
+
+class _RepackModelStep(TrainingStep):
+    """Repacks model artifacts with custom inference entry points.
+
+    The SDK automatically adds this step to pipelines that have RegisterModelSteps with models
+    that have a custom entry point.
+    """
 
     def __init__(
         self,
-        py_version=None,
-        framework_version=None,
-        model_dir=None,
-        image_uri=None,
-        distribution=None,
-        compiler_config=None,
+        name: str,
+        sagemaker_session,
+        role,
+        model_data: str,
+        entry_point: str,
+        display_name: str = None,
+        description: str = None,
+        source_dir: str = None,
+        dependencies: List = None,
+        depends_on: Optional[List[Union[str, Step, "StepCollection"]]] = None,
+        retry_policies: List[RetryPolicy] = None,
+        subnets=None,
+        security_group_ids=None,
         **kwargs,
     ):
-        """Initialize a ``TensorFlow`` estimator.
-
-        Args:
-            py_version (str): Python version you want to use for executing your model training
-                code. Defaults to ``None``. Required unless ``image_uri`` is provided.
-            framework_version (str): TensorFlow version you want to use for executing your model
-                training code. Defaults to ``None``. Required unless ``image_uri`` is provided.
-                List of supported versions:
-                https://github.com/aws/sagemaker-python-sdk#tensorflow-sagemaker-estimators.
-            model_dir (str): S3 location where the checkpoint data and models can be exported to
-                during training (default: None). It will be passed in the training script as one of
-                the command line arguments. If not specified, one is provided based on
-                your training configuration:
-
-                * *distributed training with SMDistributed or MPI with Horovod* - ``/opt/ml/model``
-                * *single-machine training or distributed training without MPI* - \
-                    ``s3://{output_path}/model``
-                * *Local Mode with local sources (file:// instead of s3://)* - \
-                    ``/opt/ml/shared/model``
-
-                To disable having ``model_dir`` passed to your training script,
-                set ``model_dir=False``.
-            image_uri (str): If specified, the estimator will use this image for training and
-                hosting, instead of selecting the appropriate SageMaker official image based on
-                framework_version and py_version. It can be an ECR url or dockerhub image and tag.
-
-                Examples:
-                    123.dkr.ecr.us-west-2.amazonaws.com/my-custom-image:1.0
-                    custom-image:latest.
-
-                If ``framework_version`` or ``py_version`` are ``None``, then
-                ``image_uri`` is required. If also ``None``, then a ``ValueError``
-                will be raised.
-            distribution (dict): A dictionary with information on how to run distributed training
-                (default: None). Currently, the following are supported:
-                distributed training with parameter servers, SageMaker Distributed (SMD) Data
-                and Model Parallelism, and MPI. SMD Model Parallelism can only be used with MPI.
-
-                **To enable the SageMaker distributed data parallelism:**
-
-                    .. code:: python
-
-                        { "smdistributed": { "dataparallel": { "enabled": True } } }
-
-                    .. seealso::
-
-                        To learn more, see :ref:`sdp_api_docs_toc`.
-
-                **To enable the SageMaker distributed model parallelism:**
-
-                    .. code:: python
-
-                        {
-                            "smdistributed": {
-                                "modelparallel": {
-                                    "enabled":True,
-                                    "parameters": {
-                                        "partitions": 2,
-                                        "microbatches": 4,
-                                        "placement_strategy": "spread",
-                                        "pipeline": "interleaved",
-                                        "optimize": "speed",
-                                        "ddp": True,
-                                    }
-                            },
-                            "mpi": {
-                                "enabled" : True,
-                                "processes_per_host" : 8,
-                            }
-                        }
-
-                    .. note::
-
-                        The SageMaker distributed model parallel library internally uses MPI.
-                        In order to use model parallelism, MPI also must be enabled.
-
-                    .. seealso::
-
-                        To learn more, see :ref:`smp_api_docs_toc`.
-
-                    .. seealso::
-
-                        To find a complete list of parameters for SageMaker model parallelism,
-                        see :ref:`sm-sdk-modelparallel-general`.
-
-                **To enable MPI:**
-
-                    .. code:: python
-
-                        {
-                            "mpi": {
-                                "enabled": True
-                            }
-                        }
-
-                    To learn more, see `Training with Horovod
-                    <https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html#training-with-horovod>`_.
-
-                **To enable parameter server:**
-
-                    .. code:: python
-
-                        {
-                            "parameter_server": {
-                                "enabled": True
-                            }
-                        }
-
-                    To learn more, see `Training with parameter servers
-                    <https://sagemaker.readthedocs.io/en/stable/frameworks/tensorflow/using_tf.html#training-with-parameter-servers>`_.
-            compiler_config (:class:`~sagemaker.tensorflow.TrainingCompilerConfig`):
-                Configures SageMaker Training Compiler to accelerate training.
-
-            **kwargs: Additional kwargs passed to the Framework constructor.
-
-        .. tip::
-
-            You can find additional parameters for initializing this class at
-            :class:`~sagemaker.estimator.Framework` and
-            :class:`~sagemaker.estimator.EstimatorBase`.
-        """
-        distribution = renamed_kwargs("distributions", "distribution", distribution, kwargs)
-        instance_type = renamed_kwargs(
-            "train_instance_type", "instance_type", kwargs.get("instance_type"), kwargs
-        )
-        fw.validate_version_or_image_args(framework_version, py_version, image_uri)
-        if py_version == "py2":
-            logger.warning(
-                fw.python_deprecation_warning(self._framework_name, defaults.LATEST_PY2_VERSION)
-            )
-        self.framework_version = framework_version
-        self.py_version = py_version
-        self.instance_type = instance_type
-
-        if distribution is not None:
-            fw.warn_if_parameter_server_with_multi_gpu(
-                training_instance_type=instance_type, distribution=distribution
-            )
-            fw.validate_smdistributed(
-                instance_type=instance_type,
-                framework_name=self._framework_name,
-                framework_version=framework_version,
-                py_version=py_version,
-                distribution=distribution,
-                image_uri=image_uri,
-            )
-
-        if "enable_sagemaker_metrics" not in kwargs:
-            # enable sagemaker metrics for TF v1.15 or greater:
-            if framework_version and version.Version(framework_version) >= version.Version("1.15"):
-                kwargs["enable_sagemaker_metrics"] = True
-
-        super(TensorFlow, self).__init__(image_uri=image_uri, **kwargs)
-        self.model_dir = model_dir
-        self.distribution = distribution or {}
-
-        self._validate_args(py_version=py_version)
-        if compiler_config is not None:
-            if not isinstance(compiler_config, TrainingCompilerConfig):
-                error_string = (
-                    f"Expected instance of type {TrainingCompilerConfig}"
-                    f"for argument compiler_config. "
-                    f"Instead got {type(compiler_config)}"
-                )
-                raise ValueError(error_string)
-            if compiler_config:
-                compiler_config.validate(self)
-        self.compiler_config = compiler_config
-
-    def _validate_args(self, py_version):
-        """Placeholder docstring"""
-
-        if py_version == "py2" and self._only_python_3_supported():
-            msg = (
-                "Python 2 containers are only available with {} and lower versions. "
-                "Please use a Python 3 container.".format(defaults.LATEST_PY2_VERSION)
-            )
-            raise AttributeError(msg)
-
-        if self.image_uri is None and self._only_legacy_mode_supported():
-            legacy_image_uri = image_uris.retrieve(
-                "tensorflow",
-                self.sagemaker_session.boto_region_name,
-                instance_type=self.instance_type,
-                version=self.framework_version,
-                py_version=self.py_version,
-                image_scope="training",
-            )
-
-            msg = (
-                "TF {} supports only legacy mode. Please supply the image URI directly with "
-                "'image_uri={}' and set 'model_dir=False'. If you are using any legacy parameters "
-                "(training_steps, evaluation_steps, checkpoint_path, requirements_file), "
-                "make sure to pass them directly as hyperparameters instead. For more, see "
-                "https://sagemaker.readthedocs.io/en/v2.0.0.rc0/frameworks/tensorflow/upgrade_from_legacy.html."
-            ).format(self.framework_version, legacy_image_uri)
-
-            raise ValueError(msg)
-
-    def _only_legacy_mode_supported(self):
-        """Placeholder docstring"""
-        return version.Version(self.framework_version) <= self._HIGHEST_LEGACY_MODE_ONLY_VERSION
-
-    def _only_python_3_supported(self):
-        """Placeholder docstring"""
-        return version.Version(self.framework_version) > self._HIGHEST_PYTHON_2_VERSION
-
-    @classmethod
-    def _prepare_init_params_from_job_description(cls, job_details, model_channel_name=None):
-        """Convert the job description to init params that can be handled by the class constructor
+        """Base class initializer.
 
         Args:
-            job_details: the returned job details from a describe_training_job API call.
-
-        Returns:
-             dictionary: The transformed init_params
-
+            name (str): The name of the training step.
+            sagemaker_session (sagemaker.session.Session): Session object which manages
+                    interactions with Amazon SageMaker APIs and any other AWS services needed. If
+                    not specified, the estimator creates one using the default
+                    AWS configuration chain.
+            role (str): An AWS IAM role (either name or full ARN). The Amazon
+                    SageMaker training jobs and APIs that create Amazon SageMaker
+                    endpoints use this role to access training data and model
+                    artifacts. After the endpoint is created, the inference code
+                    might use the IAM role, if it needs to access an AWS resource.
+            model_data (str): The S3 location of a SageMaker model data `.tar.gz` file.
+            entry_point (str): Path (absolute or relative) to the local Python
+                    source file which should be executed as the entry point to
+                    inference. If ``source_dir`` is specified, then ``entry_point``
+                    must point to a file located at the root of ``source_dir``.
+                    If 'git_config' is provided, 'entry_point' should be
+                    a relative location to the Python source file in the Git repo.
+
+                    Example:
+                        With the following GitHub repo directory structure:
+
+                        >>> |----- README.md
+                        >>> |----- src
+                        >>>         |----- train.py
+                        >>>         |----- test.py
+
+                        You can assign entry_point='src/train.py'.
+            display_name (str): The display name of this `_RepackModelStep` step (default: None).
+            description (str): The description of this `_RepackModelStep` (default: None).
+            source_dir (str): A relative location to a directory with other training
+                or model hosting source code dependencies aside from the entry point
+                file in the Git repo (default: None). Structure within this
+                directory are preserved when training on Amazon SageMaker.
+            dependencies (list[str]): A list of paths to directories (absolute
+                    or relative) with any additional libraries that will be exported
+                    to the container (default: []). The library folders will be
+                    copied to SageMaker in the same folder where the entrypoint is
+                    copied. If 'git_config' is provided, 'dependencies' should be a
+                    list of relative locations to directories with any additional
+                    libraries needed in the Git repo.
+
+                    .. admonition:: Example
+
+                        The following call
+
+                        >>> Estimator(entry_point='train.py',
+                        ...           dependencies=['my/libs/common', 'virtual-env'])
+
+                        results in the following inside the container:
+
+                        >>> $ ls
+
+                        >>> opt/ml/code
+                        >>>     |------ train.py
+                        >>>     |------ common
+                        >>>     |------ virtual-env
+
+                    This is not supported with "local code" in Local Mode.
+            depends_on (List[Union[str, Step, StepCollection]]): The list of `Step`/`StepCollection`
+                names or `Step` instances or `StepCollection` instances that the current `Step`
+                depends on (default: None).
+            retry_policies (List[RetryPolicy]): The list of retry policies for the current step
+                (default: None).
+            subnets (list[str]): List of subnet ids. If not specified, the re-packing
+                    job will be created without VPC config (default: None).
+            security_group_ids (list[str]): List of security group ids. If not
+                specified, the re-packing job will be created without VPC config (default: None).
+            **kwargs: additional arguments for the repacking job.
         """
-        init_params = super(TensorFlow, cls)._prepare_init_params_from_job_description(
-            job_details, model_channel_name
+        self._model_data = model_data
+        self.sagemaker_session = sagemaker_session
+        self.role = role
+        self._entry_point = entry_point
+        self._entry_point_basename = os.path.basename(self._entry_point)
+        self._source_dir = source_dir
+        self._dependencies = dependencies
+
+        # convert dependencies array into space-delimited string
+        dependencies_hyperparameter = None
+        if self._dependencies:
+            dependencies_hyperparameter = " ".join(self._dependencies)
+
+        # the real estimator and inputs
+        repacker = SKLearn(
+            framework_version=FRAMEWORK_VERSION,
+            instance_type=INSTANCE_TYPE,
+            entry_point=REPACK_SCRIPT,
+            source_dir=self._source_dir,
+            dependencies=self._dependencies,
+            sagemaker_session=self.sagemaker_session,
+            role=self.role,
+            hyperparameters={
+                "inference_script": self._entry_point_basename,
+                "model_archive": self._model_data,
+                "dependencies": dependencies_hyperparameter,
+                "source_dir": self._source_dir,
+            },
+            subnets=subnets,
+            security_group_ids=security_group_ids,
+            **kwargs,
         )
+        repacker.disable_profiler = True
+        inputs = TrainingInput(self._model_data)
 
-        image_uri = init_params.pop("image_uri")
-        framework, py_version, tag, script_mode = fw.framework_name_from_image(image_uri)
-
-        if not framework:
-            # If we were unable to parse the framework name from the image, it is not one of our
-            # officially supported images, so just add the image to the init params.
-            init_params["image_uri"] = image_uri
-            return init_params
-
-        model_dir = init_params["hyperparameters"].pop("model_dir", None)
-        if model_dir:
-            init_params["model_dir"] = model_dir
-        elif script_mode is None:
-            init_params["model_dir"] = False
-
-        init_params["py_version"] = py_version
-
-        # We switched image tagging scheme from regular image version (e.g. '1.0') to more
-        # expressive containing framework version, device type and python version
-        # (e.g. '1.5-gpu-py2'). For backward compatibility map deprecated image tag '1.0' to a
-        # '1.4' framework version otherwise extract framework version from the tag itself.
-        init_params["framework_version"] = (
-            "1.4" if tag == "1.0" else fw.framework_version_from_tag(tag)
+        # super!
+        super(_RepackModelStep, self).__init__(
+            name=name,
+            display_name=display_name,
+            description=description,
+            depends_on=depends_on,
+            retry_policies=retry_policies,
+            estimator=repacker,
+            inputs=inputs,
         )
 
-        # Legacy images are required to be passed in explicitly.
-        if not script_mode:
-            init_params["image_uri"] = image_uri
-
-        if framework != cls._framework_name:
-            raise ValueError(
-                "Training job: {} didn't use image for requested framework".format(
-                    job_details["TrainingJobName"]
-                )
-            )
-
-        return init_params
-
-    def create_model(
-        self,
-        role=None,
-        vpc_config_override=VPC_CONFIG_DEFAULT,
-        entry_point=None,
-        source_dir=None,
-        dependencies=None,
-        **kwargs,
-    ):
-        """Creates ``TensorFlowModel`` object to be used for creating SageMaker model entities.
-
-        This can be done by deploying it to a SageMaker endpoint,
-        or starting SageMaker Batch Transform jobs.
-
-        Args:
-            role (str): The ``TensorFlowModel``, which is also used during transform jobs.
-                If not specified, the role from the Estimator is used.
-            vpc_config_override (dict[str, list[str]]): Optional override for VpcConfig set on the
-                model. Default: use subnets and security groups from this Estimator.
-
-                * 'Subnets' (list[str]): List of subnet ids.
-                * 'SecurityGroupIds' (list[str]): List of security group ids.
-
-            entry_point (str): Path (absolute or relative) to the local Python source file which
-                should be executed as the entry point to training. If ``source_dir`` is specified,
-                then ``entry_point`` must point to a file located at the root of ``source_dir``.
-                If not specified and ``endpoint_type`` is 'tensorflow-serving',
-                no entry point is used. If ``endpoint_type`` is also ``None``,
-                then the training entry point is used.
-            source_dir (str): Path (absolute or relative or an S3 URI) to a directory with any other
-                serving source code dependencies aside from the entry point file (default: None).
-            dependencies (list[str]): A list of paths to directories (absolute or relative) with
-                any additional libraries that will be exported to the container (default: None).
-            **kwargs: Additional kwargs passed to
-                :class:`~sagemaker.tensorflow.model.TensorFlowModel`.
-
-        Returns:
-            sagemaker.tensorflow.model.TensorFlowModel: A ``TensorFlowModel`` object.
-                See :class:`~sagemaker.tensorflow.model.TensorFlowModel` for full details.
+    def _prepare_for_repacking(self):
+        """Prepares the source for the estimator."""
+        if self._source_dir is None:
+            self._establish_source_dir()
+
+        self._inject_repack_script()
+
+    def _establish_source_dir(self):
+        """If the source_dir is None, creates it for the repacking job.
+
+        It performs the following:
+            1) creates a source directory
+            2) copies the inference_entry_point inside it
+            3) copies the repack_model.py inside it
+            4) sets the source dir for the repacking estimator
         """
-        kwargs["name"] = self._get_or_create_name(kwargs.get("name"))
-
-        if "image_uri" not in kwargs:
-            kwargs["image_uri"] = self.image_uri
-
-        if "enable_network_isolation" not in kwargs:
-            kwargs["enable_network_isolation"] = self.enable_network_isolation()
-
-        return TensorFlowModel(
-            model_data=self.model_data,
-            role=role or self.role,
-            container_log_level=self.container_log_level,
-            framework_version=self.framework_version,
-            sagemaker_session=self.sagemaker_session,
-            vpc_config=self.get_vpc_config(vpc_config_override),
-            entry_point=entry_point,
-            source_dir=source_dir,
-            dependencies=dependencies,
-            **kwargs,
-        )
+        self._source_dir = tempfile.mkdtemp()
+        self.estimator.source_dir = self._source_dir
 
-    def hyperparameters(self):
-        """Return hyperparameters used by your custom TensorFlow code during model training."""
-        hyperparameters = super(TensorFlow, self).hyperparameters()
-        additional_hyperparameters = self._distribution_configuration(self.distribution)
-
-        if self.model_dir is not False:
-            self.model_dir = self.model_dir or self._default_s3_path(
-                "model", mpi=additional_hyperparameters.get(self.LAUNCH_MPI_ENV_NAME, False)
-            )
-            additional_hyperparameters["model_dir"] = self.model_dir
+        shutil.copy2(self._entry_point, os.path.join(self._source_dir, self._entry_point_basename))
+        self._entry_point = self._entry_point_basename
 
-        hyperparameters.update(
-            EstimatorBase._json_encode_hyperparameters(additional_hyperparameters)
-        )
+    def _inject_repack_script(self):
+        """Injects the _repack_model.py script into S3 or local source directory.
 
-        if self.compiler_config:
-            training_compiler_hyperparameters = self.compiler_config._to_hyperparameter_dict()
-            hyperparameters.update(
-                EstimatorBase._json_encode_hyperparameters(training_compiler_hyperparameters)
-            )
+        If the source_dir is an S3 path:
+            1) downloads the source_dir tar.gz
+            2) extracts it
+            3) copies the _repack_model.py script into the extracted directory
+            4) rezips the directory
+            5) overwrites the S3 source_dir with the new tar.gz
 
-        return hyperparameters
+        If the source_dir is a local path:
+            1) copies the _repack_model.py script into the source dir
+        """
+        fname = os.path.join(os.path.dirname(__file__), REPACK_SCRIPT)
+        if self._source_dir.lower().startswith("s3://"):
+            with tempfile.TemporaryDirectory() as tmp:
+                targz_contents_dir = os.path.join(tmp, "extracted")
+
+                old_targz_path = os.path.join(tmp, "old.tar.gz")
+                download_file_from_url(self._source_dir, old_targz_path, self.sagemaker_session)
+
+                with tarfile.open(name=old_targz_path, mode="r:gz") as t:
+                    t.extractall(path=targz_contents_dir)
+
+                shutil.copy2(fname, os.path.join(targz_contents_dir, REPACK_SCRIPT))
+
+                new_targz_path = os.path.join(tmp, "new.tar.gz")
+                with tarfile.open(new_targz_path, mode="w:gz") as t:
+                    t.add(targz_contents_dir, arcname=os.path.sep)
+
+                _save_model(self._source_dir, new_targz_path, self.sagemaker_session, kms_key=None)
+        else:
+            shutil.copy2(fname, os.path.join(self._source_dir, REPACK_SCRIPT))
+
+    @property
+    def arguments(self) -> RequestType:
+        """The arguments dict that are used to call `create_training_job`.
+
+        This first prepares the source bundle for repackinglby placing artifacts
+        in locations which the training container will make available to the
+        repacking script and then gets the arguments for the training job.
+        """
+        self._prepare_for_repacking()
+        return super(_RepackModelStep, self).arguments
 
-    def _default_s3_path(self, directory, mpi=False):
-        """Placeholder docstring"""
-        local_code = utils.get_config_value("local.local_code", self.sagemaker_session.config)
-        if self.sagemaker_session.local_mode and local_code:
-            return "/opt/ml/shared/{}".format(directory)
-        if mpi:
-            return "/opt/ml/model"
-        if self._current_job_name:
-            if is_pipeline_variable(self.output_path):
-                output_path = "s3://{}".format(self.sagemaker_session.default_bucket())
-                return s3.s3_path_join(output_path, self._current_job_name, directory)
-            return s3.s3_path_join(self.output_path, self._current_job_name, directory)
-        return None
+    @property
+    def properties(self):
+        """A Properties object representing the DescribeTrainingJobResponse data model."""
+        return self._properties
 
-    def _validate_and_set_debugger_configs(self):
-        """Disable Debugger Hook Config for ParameterServer (PS) as it is not supported in smdebug.
 
-        Else, set default HookConfig
-        """
-        super(TensorFlow, self)._validate_and_set_debugger_configs()
-        ps_enabled = "parameter_server" in self.distribution and self.distribution[
-            "parameter_server"
-        ].get("enabled", False)
-        if ps_enabled:
-            if self.debugger_hook_config is not None or self.debugger_rule_configs is not None:
-                logger.info(
-                    "Amazon SageMaker Debugger does not currently support "
-                    "Parameter Server distribution"
-                )
-            self.debugger_hook_config = None
-            self.debugger_rule_configs = None
+class _RegisterModelStep(ConfigurableRetryStep):
+    """Register model step in workflow that creates a model package."""
 
-    def transformer(
+    def __init__(
         self,
-        instance_count,
-        instance_type,
-        strategy=None,
-        assemble_with=None,
-        output_path=None,
-        output_kms_key=None,
-        accept=None,
-        env=None,
-        max_concurrent_transforms=None,
-        max_payload=None,
+        name: str,
+        step_args: Optional[dict] = None,
+        content_types: Optional[list] = None,
+        response_types: Optional[list] = None,
+        inference_instances: Optional[list] = None,
+        transform_instances: Optional[list] = None,
+        estimator: EstimatorBase = None,
+        model_data=None,
+        model_package_group_name=None,
+        model_metrics=None,
+        metadata_properties=None,
+        approval_status="PendingManualApproval",
+        image_uri=None,
+        compile_model_family=None,
+        display_name: str = None,
+        description=None,
+        depends_on: Optional[List[Union[str, Step, "StepCollection"]]] = None,
+        retry_policies: Optional[List[RetryPolicy]] = None,
         tags=None,
-        role=None,
-        volume_kms_key=None,
-        entry_point=None,
-        vpc_config_override=VPC_CONFIG_DEFAULT,
-        enable_network_isolation=None,
-        model_name=None,
+        container_def_list=None,
+        drift_check_baselines=None,
+        customer_metadata_properties=None,
+        domain=None,
+        sample_payload_url=None,
+        task=None,
+        **kwargs,
     ):
-        """Return a ``Transformer`` that uses a SageMaker Model based on the training job.
-
-        It reuses the SageMaker Session and base job name used by the Estimator.
+        """Constructor of a register model step.
 
         Args:
-            instance_count (int): Number of EC2 instances to use.
-            instance_type (str): Type of EC2 instance to use, for example, 'ml.c4.xlarge'.
-            strategy (str): The strategy used to decide how to batch records in a single request
-                (default: None). Valid values: 'MultiRecord' and 'SingleRecord'.
-            assemble_with (str): How the output is assembled (default: None). Valid values: 'Line'
-                or 'None'.
-            output_path (str): S3 location for saving the transform result. If not specified,
-                results are stored to a default bucket.
-            output_kms_key (str): Optional. KMS key ID for encrypting the transform output
+            name (str): The name of the training step.
+            step_args (dict): The arguments for this `_RegisterModelStep` definition
+                (default: None).
+            content_types (list): The supported MIME types for the input data (default: None).
+            response_types (list): The supported MIME types for the output data (default: None).
+            inference_instances (list): A list of the instance types that are used to
+                generate inferences in real-time (default: None).
+            transform_instances (list): A list of the instance types on which a
+                transformation job can be run or on which an endpoint
+                can be deployed (default: None).
+            estimator (EstimatorBase): A `sagemaker.estimator.EstimatorBase` instance
                 (default: None).
-            accept (str): The accept header passed by the client to
-                the inference endpoint. If it is supported by the endpoint,
-                it will be the format of the batch transform output.
-            env (dict): Environment variables to be set for use during the transform job
+            model_data: the S3 URI to the model data from training (default: None).
+            model_package_group_name (str): Model Package Group name, exclusive to
+                `model_package_name`, using `model_package_group_name`
+                makes the Model Package versioned (default: None).
+            model_metrics (ModelMetrics): ModelMetrics object (default: None).
+            metadata_properties (MetadataProperties): MetadataProperties object (default: None).
+            approval_status (str): Model Approval Status, values can be "Approved",
+                "Rejected", or "PendingManualApproval" (default: "PendingManualApproval").
+            image_uri (str): The container image uri for Model Package, if not specified,
+                Estimator's training container image will be used (default: None).
+            compile_model_family (str): Instance family for compiled model,
+                if specified, a compiled model will be used (default: None).
+            display_name (str): The display name of this `_RegisterModelStep` step (default: None).
+            description (str): Model Package description (default: None).
+            depends_on (List[Union[str, Step, StepCollection]]): The list of `Step`/`StepCollection`
+                names or `Step` instances or `StepCollection` instances that the current `Step`
+                depends on (default: None).
+            retry_policies (List[RetryPolicy]): The list of retry policies for the current step
                 (default: None).
-            max_concurrent_transforms (int): The maximum number of HTTP requests to be made to
-                each individual transform container at one time.
-            max_payload (int): Maximum size of the payload in a single HTTP request to the
-                container in MB.
-            tags (list[dict]): List of tags for labeling a transform job. If none specified, then
-                the tags used for the training job are used for the transform job.
-            role (str): The IAM Role ARN for the ``TensorFlowModel``, which is also used
-                during transform jobs. If not specified, the role from the Estimator is used.
-            volume_kms_key (str): Optional. KMS key ID for encrypting the volume attached to the ML
-                compute instance (default: None).
-            entry_point (str): Path (absolute or relative) to the local Python source file which
-                should be executed as the entry point to training. If ``source_dir`` is specified,
-                then ``entry_point`` must point to a file located at the root of ``source_dir``.
-                If not specified and ``endpoint_type`` is 'tensorflow-serving',
-                no entry point is used. If ``endpoint_type`` is also ``None``,
-                then the training entry point is used.
-            vpc_config_override (dict[str, list[str]]): Optional override for
-                the VpcConfig set on the model.
-                Default: use subnets and security groups from this Estimator.
-
-                * 'Subnets' (list[str]): List of subnet ids.
-                * 'SecurityGroupIds' (list[str]): List of security group ids.
-
-            enable_network_isolation (bool): Specifies whether container will
-                run in network isolation mode. Network isolation mode restricts
-                the container access to outside networks (such as the internet).
-                The container does not make any inbound or outbound network
-                calls. If True, a channel named "code" will be created for any
-                user entry script for inference. Also known as Internet-free mode.
-                If not specified, this setting is taken from the estimator's
-                current configuration.
-            model_name (str): Name to use for creating an Amazon SageMaker
-                model. If not specified, the estimator generates a default job name
-                based on the training image name and current timestamp.
+            tags (List[dict[str, str]]): A list of dictionaries containing key-value pairs used to
+                configure the create model package request (default: None).
+            container_def_list (list): A list of container definitions (default: None).
+            drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
+            customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
+                metadata properties (default: None).
+            domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
+                "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            **kwargs: additional arguments to `create_model`.
         """
-        role = role or self.role
-        model_name = self._get_or_create_name(model_name)
-
-        if self.latest_training_job is None:
-            logger.warning(
-                "No finished training job found associated with this estimator. Please make sure "
-                "this estimator is only used for building workflow config"
-            )
-            return Transformer(
-                model_name,
-                instance_count,
-                instance_type,
-                strategy=strategy,
-                assemble_with=assemble_with,
-                output_path=output_path,
-                output_kms_key=output_kms_key,
-                accept=accept,
-                max_concurrent_transforms=max_concurrent_transforms,
-                max_payload=max_payload,
-                env=env or {},
-                tags=tags,
-                base_transform_job_name=self.base_job_name,
-                volume_kms_key=volume_kms_key,
-                sagemaker_session=self.sagemaker_session,
+        super(_RegisterModelStep, self).__init__(
+            name, StepTypeEnum.REGISTER_MODEL, display_name, description, depends_on, retry_policies
+        )
+        deprecated_args_missing = (
+            content_types is None
+            or response_types is None
+            or inference_instances is None
+            or transform_instances is None
+        )
+        if not (step_args is None) ^ deprecated_args_missing:
+            raise ValueError(
+                "step_args and the set of (content_types, response_types, "
+                "inference_instances, transform_instances) are mutually exclusive. "
+                "Either of them should be provided."
             )
 
-        if enable_network_isolation is None:
-            enable_network_isolation = self.enable_network_isolation()
-
-        model = self.create_model(
-            role=role,
-            vpc_config_override=vpc_config_override,
-            entry_point=entry_point,
-            enable_network_isolation=enable_network_isolation,
-            name=model_name,
-        )
+        self.step_args = step_args
+        self.estimator = estimator
+        self.model_data = model_data
+        self.content_types = content_types
+        self.response_types = response_types
+        self.inference_instances = inference_instances
+        self.transform_instances = transform_instances
+        self.model_package_group_name = model_package_group_name
+        self.tags = tags
+        self.model_metrics = model_metrics
+        self.drift_check_baselines = drift_check_baselines
+        self.customer_metadata_properties = customer_metadata_properties
+        self.domain = domain
+        self.sample_payload_url = sample_payload_url
+        self.task = task
+        self.metadata_properties = metadata_properties
+        self.approval_status = approval_status
+        self.image_uri = image_uri
+        self.compile_model_family = compile_model_family
+        self.description = description
+        self.tags = tags
+        self.kwargs = kwargs
+        self.container_def_list = container_def_list
+
+        self._properties = Properties(step_name=name, shape_name="DescribeModelPackageOutput")
+
+    @property
+    def arguments(self) -> RequestType:
+        """The arguments dict that are used to call `create_model_package`."""
+        model_name = self.name
+
+        if self.step_args:
+            request_dict = self.step_args
+        else:
+            if self.container_def_list is None:
+                if self.compile_model_family:
+                    model = self.estimator._compiled_models[self.compile_model_family]
+                    self.model_data = model.model_data
+                else:
+                    # create_model wants the estimator to have a model_data attribute...
+                    self.estimator._current_job_name = model_name
+
+                    # placeholder. replaced with model_data later
+                    output_path = self.estimator.output_path
+                    self.estimator.output_path = "/tmp"
+
+                    # create the model, but custom funky framework stuff going on in some places
+                    if self.image_uri:
+                        model = self.estimator.create_model(image_uri=self.image_uri, **self.kwargs)
+                    else:
+                        model = self.estimator.create_model(**self.kwargs)
+                        self.image_uri = model.image_uri
+
+                    if self.model_data is None:
+                        self.model_data = model.model_data
+
+                    # reset placeholder
+                    self.estimator.output_path = output_path
+
+                    # yeah, there is some framework stuff going on that we need to pull in here
+                    if self.image_uri is None:
+                        region_name = self.estimator.sagemaker_session.boto_session.region_name
+                        self.image_uri = image_uris.retrieve(
+                            model._framework_name,
+                            region_name,
+                            version=model.framework_version,
+                            py_version=model.py_version if hasattr(model, "py_version") else None,
+                            instance_type=self.kwargs.get(
+                                "instance_type", self.estimator.instance_type
+                            ),
+                            accelerator_type=self.kwargs.get("accelerator_type"),
+                            image_scope="inference",
+                        )
+                        model.name = model_name
+                        model.model_data = self.model_data
+
+            model_package_args = get_model_package_args(
+                content_types=self.content_types,
+                response_types=self.response_types,
+                inference_instances=self.inference_instances,
+                transform_instances=self.transform_instances,
+                model_package_group_name=self.model_package_group_name,
+                model_data=self.model_data,
+                image_uri=self.image_uri,
+                model_metrics=self.model_metrics,
+                drift_check_baselines=self.drift_check_baselines,
+                metadata_properties=self.metadata_properties,
+                approval_status=self.approval_status,
+                description=self.description,
+                tags=self.tags,
+                container_def_list=self.container_def_list,
+                customer_metadata_properties=self.customer_metadata_properties,
+                domain=self.domain,
+                sample_payload_url=self.sample_payload_url,
+                task=self.task,
+            )
 
-        return model.transformer(
-            instance_count,
-            instance_type,
-            strategy=strategy,
-            assemble_with=assemble_with,
-            output_path=output_path,
-            output_kms_key=output_kms_key,
-            accept=accept,
-            env=env,
-            max_concurrent_transforms=max_concurrent_transforms,
-            max_payload=max_payload,
-            tags=tags,
-            volume_kms_key=volume_kms_key,
-        )
+            request_dict = get_create_model_package_request(**model_package_args)
+        # these are not available in the workflow service and will cause rejection
+        if "CertifyForMarketplace" in request_dict:
+            request_dict.pop("CertifyForMarketplace")
+        if "Description" in request_dict:
+            request_dict.pop("Description")
+
+        return request_dict
+
+    @property
+    def properties(self):
+        """A Properties object representing the DescribeModelPackageOutput data model."""
+        return self._properties
```

### Comparing `sagemaker-2.98.0/src/sagemaker/tensorflow/model.py` & `sagemaker-2.99.0/src/sagemaker/tensorflow/model.py`

 * *Files 6% similar despite different names*

```diff
@@ -202,14 +202,20 @@
         metadata_properties=None,
         marketplace_cert=False,
         approval_status=None,
         description=None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
     ):
         """Creates a model package for creating SageMaker models or listing on Marketplace.
 
         Args:
             content_types (list): The supported MIME types for the input data.
             response_types (list): The supported MIME types for the output data.
             inference_instances (list): A list of the instance types that are used to
@@ -231,14 +237,26 @@
                 or "PendingManualApproval" (default: "PendingManualApproval").
             description (str): Model Package description (default: None).
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
 
         Returns:
             A `sagemaker.model.ModelPackage` instance.
         """
         instance_type = inference_instances[0] if inference_instances else None
         self._init_sagemaker_session_if_does_not_exist(instance_type)
 
@@ -261,14 +279,20 @@
             metadata_properties,
             marketplace_cert,
             approval_status,
             description,
             drift_check_baselines=drift_check_baselines,
             customer_metadata_properties=customer_metadata_properties,
             domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
+            framework=framework,
+            framework_version=framework_version,
+            nearest_model_name=nearest_model_name,
+            data_input_configuration=data_input_configuration,
         )
 
     def deploy(
         self,
         initial_instance_count=None,
         instance_type=None,
         serializer=None,
```

### Comparing `sagemaker-2.98.0/src/sagemaker/tensorflow/processing.py` & `sagemaker-2.99.0/src/sagemaker/tensorflow/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/tensorflow/serving.py` & `sagemaker-2.99.0/src/sagemaker/tensorflow/serving.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/tensorflow/training_compiler/config.py` & `sagemaker-2.99.0/src/sagemaker/tensorflow/training_compiler/config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/training_compiler/config.py` & `sagemaker-2.99.0/src/sagemaker/training_compiler/config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/transformer.py` & `sagemaker-2.99.0/src/sagemaker/transformer.py`

 * *Files 6% similar despite different names*

```diff
@@ -9,43 +9,46 @@
 # or in the "license" file accompanying this file. This file is
 # distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
 """Placeholder docstring"""
 from __future__ import absolute_import
 
+from typing import Union, Optional, List, Dict
+
 from botocore import exceptions
 
 from sagemaker.job import _Job
 from sagemaker.session import Session
+from sagemaker.workflow.entities import PipelineVariable
 from sagemaker.workflow.pipeline_context import runnable_by_pipeline
 from sagemaker.workflow import is_pipeline_variable
 from sagemaker.utils import base_name_from_image, name_from_base
 
 
 class Transformer(object):
     """A class for handling creating and interacting with Amazon SageMaker transform jobs."""
 
     def __init__(
         self,
-        model_name,
-        instance_count,
-        instance_type,
-        strategy=None,
-        assemble_with=None,
-        output_path=None,
-        output_kms_key=None,
-        accept=None,
-        max_concurrent_transforms=None,
-        max_payload=None,
-        tags=None,
-        env=None,
-        base_transform_job_name=None,
-        sagemaker_session=None,
-        volume_kms_key=None,
+        model_name: Union[str, PipelineVariable],
+        instance_count: Union[int, PipelineVariable],
+        instance_type: Union[str, PipelineVariable],
+        strategy: Optional[Union[str, PipelineVariable]] = None,
+        assemble_with: Optional[Union[str, PipelineVariable]] = None,
+        output_path: Optional[Union[str, PipelineVariable]] = None,
+        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
+        accept: Optional[Union[str, PipelineVariable]] = None,
+        max_concurrent_transforms: Optional[Union[int, PipelineVariable]] = None,
+        max_payload: Optional[Union[int, PipelineVariable]] = None,
+        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        base_transform_job_name: Optional[str] = None,
+        sagemaker_session: Optional[Session] = None,
+        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
     ):
         """Initialize a ``Transformer``.
 
         Args:
             model_name (str): Name of the SageMaker model being used for the
                 transform job.
             instance_count (int): Number of EC2 instances to use.
@@ -107,27 +110,27 @@
         self._reset_output_path = False
 
         self.sagemaker_session = sagemaker_session or Session()
 
     @runnable_by_pipeline
     def transform(
         self,
-        data,
-        data_type="S3Prefix",
-        content_type=None,
-        compression_type=None,
-        split_type=None,
-        job_name=None,
-        input_filter=None,
-        output_filter=None,
-        join_source=None,
-        experiment_config=None,
-        model_client_config=None,
-        wait=True,
-        logs=True,
+        data: Union[str, PipelineVariable],
+        data_type: Union[str, PipelineVariable] = "S3Prefix",
+        content_type: Optional[Union[str, PipelineVariable]] = None,
+        compression_type: Optional[Union[str, PipelineVariable]] = None,
+        split_type: Optional[Union[str, PipelineVariable]] = None,
+        job_name: Optional[str] = None,
+        input_filter: Optional[Union[str, PipelineVariable]] = None,
+        output_filter: Optional[Union[str, PipelineVariable]] = None,
+        join_source: Optional[Union[str, PipelineVariable]] = None,
+        experiment_config: Optional[Dict[str, str]] = None,
+        model_client_config: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
+        wait: bool = True,
+        logs: bool = True,
     ):
         """Start a new transform job.
 
         Args:
             data (str): Input data location in S3.
             data_type (str): What the S3 location defines (default: 'S3Prefix').
                 Valid values:
```

### Comparing `sagemaker-2.98.0/src/sagemaker/tuner.py` & `sagemaker-2.99.0/src/sagemaker/tuner.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,34 +15,36 @@
 
 import importlib
 import inspect
 import json
 import logging
 
 from enum import Enum
+from typing import Union, Dict, Optional, List, Set
 
 import sagemaker
 from sagemaker.amazon.amazon_estimator import (
     RecordSet,
     AmazonAlgorithmEstimatorBase,
     FileSystemRecordSet,
 )
 from sagemaker.amazon.hyperparameter import Hyperparameter as hp  # noqa
 from sagemaker.analytics import HyperparameterTuningJobAnalytics
 from sagemaker.deprecations import removed_function
-from sagemaker.estimator import Framework
-from sagemaker.inputs import TrainingInput
+from sagemaker.estimator import Framework, EstimatorBase
+from sagemaker.inputs import TrainingInput, FileSystemInput
 from sagemaker.job import _Job
 from sagemaker.jumpstart.utils import add_jumpstart_tags, get_jumpstart_base_name_if_jumpstart_model
 from sagemaker.parameter import (
     CategoricalParameter,
     ContinuousParameter,
     IntegerParameter,
     ParameterRange,
 )
+from sagemaker.workflow.entities import PipelineVariable
 from sagemaker.workflow.pipeline_context import runnable_by_pipeline
 
 from sagemaker.session import Session
 from sagemaker.utils import base_from_name, base_name_from_image, name_from_base
 from sagemaker.workflow import is_pipeline_variable
 
 AMAZON_ESTIMATOR_MODULE = "sagemaker"
@@ -91,15 +93,19 @@
         >>>                         type=WarmStartTypes.TransferLearning, parents={"p1","p2"})
         >>> warm_start_config.type
         "TransferLearning"
         >>> warm_start_config.parents
         {"p1","p2"}
     """
 
-    def __init__(self, warm_start_type, parents):
+    def __init__(
+        self,
+        warm_start_type: WarmStartTypes,
+        parents: Set[Union[str, PipelineVariable]],
+    ):
         """Creates a ``WarmStartConfig`` with provided ``WarmStartTypes`` and parents.
 
         Args:
             warm_start_type (sagemaker.tuner.WarmStartTypes): This should be one
                 of the supported warm start types in WarmStartType
             parents (set{str}): Set of parent tuning jobs which will be used to
                 warm start the new tuning job.
@@ -204,27 +210,27 @@
     SAGEMAKER_ESTIMATOR_CLASS_NAME = "sagemaker_estimator_class_name"
 
     DEFAULT_ESTIMATOR_MODULE = "sagemaker.estimator"
     DEFAULT_ESTIMATOR_CLS_NAME = "Estimator"
 
     def __init__(
         self,
-        estimator,
-        objective_metric_name,
-        hyperparameter_ranges,
-        metric_definitions=None,
-        strategy="Bayesian",
-        objective_type="Maximize",
-        max_jobs=1,
-        max_parallel_jobs=1,
-        tags=None,
-        base_tuning_job_name=None,
-        warm_start_config=None,
-        early_stopping_type="Off",
-        estimator_name=None,
+        estimator: EstimatorBase,
+        objective_metric_name: Union[str, PipelineVariable],
+        hyperparameter_ranges: Dict[str, ParameterRange],
+        metric_definitions: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        strategy: Union[str, PipelineVariable] = "Bayesian",
+        objective_type: Union[str, PipelineVariable] = "Maximize",
+        max_jobs: Union[int, PipelineVariable] = 1,
+        max_parallel_jobs: Union[int, PipelineVariable] = 1,
+        tags: Optional[List[Dict[str, Union[str, PipelineVariable]]]] = None,
+        base_tuning_job_name: Optional[str] = None,
+        warm_start_config: Optional[WarmStartConfig] = None,
+        early_stopping_type: Union[str, PipelineVariable] = "Off",
+        estimator_name: Optional[str] = None,
     ):
         """Creates a ``HyperparameterTuner`` instance.
 
         It takes an estimator to obtain configuration information for training
         jobs that are created as the result of a hyperparameter tuning job.
 
         Args:
@@ -423,19 +429,21 @@
             )
 
         return static_hyperparameters
 
     @runnable_by_pipeline
     def fit(
         self,
-        inputs=None,
-        job_name=None,
-        include_cls_metadata=False,
-        estimator_kwargs=None,
-        wait=True,
+        inputs: Optional[
+            Union[str, Dict, List, TrainingInput, FileSystemInput, RecordSet, FileSystemRecordSet]
+        ] = None,
+        job_name: Optional[str] = None,
+        include_cls_metadata: Union[bool, Dict[str, bool]] = False,
+        estimator_kwargs: Optional[Dict[str, dict]] = None,
+        wait: bool = True,
         **kwargs
     ):
         """Start a hyperparameter tuning job.
 
         Args:
             inputs: Information about the training data. Please refer to the
                 ``fit()`` method of the associated estimator, as this can take
```

### Comparing `sagemaker-2.98.0/src/sagemaker/user_agent.py` & `sagemaker-2.99.0/src/sagemaker/user_agent.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/utilities/cache.py` & `sagemaker-2.99.0/src/sagemaker/utilities/cache.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/utils.py` & `sagemaker-2.99.0/src/sagemaker/utils.py`

 * *Files 8% similar despite different names*

```diff
@@ -718,7 +718,63 @@
 
         config = self.fetch_data_config()
         region = region_requested if region_requested else self.sagemaker_session.boto_region_name
         return config[region] if region in config.keys() else config["default"]
 
 
 get_ecr_image_uri_prefix = deprecations.removed_function("get_ecr_image_uri_prefix")
+
+
+def update_container_with_inference_params(
+    framework=None,
+    framework_version=None,
+    nearest_model_name=None,
+    data_input_configuration=None,
+    container_obj=None,
+    container_list=None,
+):
+    """Function to check if inference recommender parameters exist and update container.
+
+    Args:
+        framework (str): Machine learning framework of the model package container image
+                (default: None).
+        framework_version (str): Framework version of the Model Package Container Image
+            (default: None).
+        nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+            Amazon SageMaker Inference Recommender (default: None).
+        data_input_configuration (str): Input object for the model (default: None).
+        container_obj (dict): object to be updated.
+        container_list (list): list to be updated.
+
+    Returns:
+        dict: dict with inference recommender params
+    """
+
+    if (
+        framework is not None
+        and framework_version is not None
+        and nearest_model_name is not None
+        and data_input_configuration is not None
+    ):
+        if container_list is not None:
+            for obj in container_list:
+                obj.update(
+                    {
+                        "Framework": framework,
+                        "FrameworkVersion": framework_version,
+                        "NearestModelName": nearest_model_name,
+                        "ModelInput": {
+                            "DataInputConfig": data_input_configuration,
+                        },
+                    }
+                )
+        if container_obj is not None:
+            container_obj.update(
+                {
+                    "Framework": framework,
+                    "FrameworkVersion": framework_version,
+                    "NearestModelName": nearest_model_name,
+                    "ModelInput": {
+                        "DataInputConfig": data_input_configuration,
+                    },
+                }
+            )
```

### Comparing `sagemaker-2.98.0/src/sagemaker/vpc_utils.py` & `sagemaker-2.99.0/src/sagemaker/vpc_utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/__init__.py` & `sagemaker-2.99.0/src/sagemaker/workflow/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/_repack_model.py` & `sagemaker-2.99.0/src/sagemaker/workflow/_repack_model.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/_utils.py` & `sagemaker-2.99.0/src/sagemaker/workflow/step_collections.py`

 * *Files 19% similar despite different names*

```diff
@@ -6,450 +6,457 @@
 #
 #     http://aws.amazon.com/apache2.0/
 #
 # or in the "license" file accompanying this file. This file is
 # distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
-"""Scrapper utilities to support repacking of models."""
+"""The step definitions for workflow."""
 from __future__ import absolute_import
 
-import os
-import shutil
-import tarfile
-import tempfile
-from typing import List, Union, Optional, TYPE_CHECKING
-from sagemaker import image_uris
-from sagemaker.inputs import TrainingInput
+import warnings
+from typing import List, Union, Optional
+
+import attr
+
 from sagemaker.estimator import EstimatorBase
-from sagemaker.sklearn.estimator import SKLearn
+from sagemaker.model import Model
+from sagemaker import PipelineModel
+from sagemaker.predictor import Predictor
+from sagemaker.transformer import Transformer
 from sagemaker.workflow.entities import RequestType
-from sagemaker.workflow.properties import Properties
-from sagemaker.session import get_create_model_package_request, get_model_package_args
-from sagemaker.workflow.steps import (
-    StepTypeEnum,
-    TrainingStep,
-    Step,
-    ConfigurableRetryStep,
-)
-from sagemaker.utils import _save_model, download_file_from_url
+from sagemaker.workflow.steps import Step, CreateModelStep, TransformStep
+from sagemaker.workflow._utils import _RegisterModelStep, _RepackModelStep
 from sagemaker.workflow.retry import RetryPolicy
+from sagemaker.utils import update_container_with_inference_params
 
-if TYPE_CHECKING:
-    from sagemaker.workflow.step_collections import StepCollection
-
-FRAMEWORK_VERSION = "0.23-1"
-INSTANCE_TYPE = "ml.m5.large"
-REPACK_SCRIPT = "_repack_model.py"
 
+@attr.s
+class StepCollection:
+    """A wrapper of pipeline steps for workflow.
 
-class _RepackModelStep(TrainingStep):
-    """Repacks model artifacts with custom inference entry points.
-
-    The SDK automatically adds this step to pipelines that have RegisterModelSteps with models
-    that have a custom entry point.
+    Attributes:
+        name (str): The name of the `StepCollection`.
+        steps (List[Step]): A list of steps.
     """
 
-    def __init__(
-        self,
-        name: str,
-        sagemaker_session,
-        role,
-        model_data: str,
-        entry_point: str,
-        display_name: str = None,
-        description: str = None,
-        source_dir: str = None,
-        dependencies: List = None,
-        depends_on: Optional[List[Union[str, Step, "StepCollection"]]] = None,
-        retry_policies: List[RetryPolicy] = None,
-        subnets=None,
-        security_group_ids=None,
-        **kwargs,
-    ):
-        """Base class initializer.
-
-        Args:
-            name (str): The name of the training step.
-            sagemaker_session (sagemaker.session.Session): Session object which manages
-                    interactions with Amazon SageMaker APIs and any other AWS services needed. If
-                    not specified, the estimator creates one using the default
-                    AWS configuration chain.
-            role (str): An AWS IAM role (either name or full ARN). The Amazon
-                    SageMaker training jobs and APIs that create Amazon SageMaker
-                    endpoints use this role to access training data and model
-                    artifacts. After the endpoint is created, the inference code
-                    might use the IAM role, if it needs to access an AWS resource.
-            model_data (str): The S3 location of a SageMaker model data `.tar.gz` file.
-            entry_point (str): Path (absolute or relative) to the local Python
-                    source file which should be executed as the entry point to
-                    inference. If ``source_dir`` is specified, then ``entry_point``
-                    must point to a file located at the root of ``source_dir``.
-                    If 'git_config' is provided, 'entry_point' should be
-                    a relative location to the Python source file in the Git repo.
-
-                    Example:
-                        With the following GitHub repo directory structure:
-
-                        >>> |----- README.md
-                        >>> |----- src
-                        >>>         |----- train.py
-                        >>>         |----- test.py
-
-                        You can assign entry_point='src/train.py'.
-            display_name (str): The display name of this `_RepackModelStep` step (default: None).
-            description (str): The description of this `_RepackModelStep` (default: None).
-            source_dir (str): A relative location to a directory with other training
-                or model hosting source code dependencies aside from the entry point
-                file in the Git repo (default: None). Structure within this
-                directory are preserved when training on Amazon SageMaker.
-            dependencies (list[str]): A list of paths to directories (absolute
-                    or relative) with any additional libraries that will be exported
-                    to the container (default: []). The library folders will be
-                    copied to SageMaker in the same folder where the entrypoint is
-                    copied. If 'git_config' is provided, 'dependencies' should be a
-                    list of relative locations to directories with any additional
-                    libraries needed in the Git repo.
-
-                    .. admonition:: Example
-
-                        The following call
-
-                        >>> Estimator(entry_point='train.py',
-                        ...           dependencies=['my/libs/common', 'virtual-env'])
-
-                        results in the following inside the container:
-
-                        >>> $ ls
-
-                        >>> opt/ml/code
-                        >>>     |------ train.py
-                        >>>     |------ common
-                        >>>     |------ virtual-env
-
-                    This is not supported with "local code" in Local Mode.
-            depends_on (List[Union[str, Step, StepCollection]]): The list of `Step`/`StepCollection`
-                names or `Step` instances or `StepCollection` instances that the current `Step`
-                depends on (default: None).
-            retry_policies (List[RetryPolicy]): The list of retry policies for the current step
-                (default: None).
-            subnets (list[str]): List of subnet ids. If not specified, the re-packing
-                    job will be created without VPC config (default: None).
-            security_group_ids (list[str]): List of security group ids. If not
-                specified, the re-packing job will be created without VPC config (default: None).
-            **kwargs: additional arguments for the repacking job.
-        """
-        self._model_data = model_data
-        self.sagemaker_session = sagemaker_session
-        self.role = role
-        self._entry_point = entry_point
-        self._entry_point_basename = os.path.basename(self._entry_point)
-        self._source_dir = source_dir
-        self._dependencies = dependencies
-
-        # convert dependencies array into space-delimited string
-        dependencies_hyperparameter = None
-        if self._dependencies:
-            dependencies_hyperparameter = " ".join(self._dependencies)
-
-        # the real estimator and inputs
-        repacker = SKLearn(
-            framework_version=FRAMEWORK_VERSION,
-            instance_type=INSTANCE_TYPE,
-            entry_point=REPACK_SCRIPT,
-            source_dir=self._source_dir,
-            dependencies=self._dependencies,
-            sagemaker_session=self.sagemaker_session,
-            role=self.role,
-            hyperparameters={
-                "inference_script": self._entry_point_basename,
-                "model_archive": self._model_data,
-                "dependencies": dependencies_hyperparameter,
-                "source_dir": self._source_dir,
-            },
-            subnets=subnets,
-            security_group_ids=security_group_ids,
-            **kwargs,
-        )
-        repacker.disable_profiler = True
-        inputs = TrainingInput(self._model_data)
-
-        # super!
-        super(_RepackModelStep, self).__init__(
-            name=name,
-            display_name=display_name,
-            description=description,
-            depends_on=depends_on,
-            retry_policies=retry_policies,
-            estimator=repacker,
-            inputs=inputs,
-        )
-
-    def _prepare_for_repacking(self):
-        """Prepares the source for the estimator."""
-        if self._source_dir is None:
-            self._establish_source_dir()
-
-        self._inject_repack_script()
-
-    def _establish_source_dir(self):
-        """If the source_dir is None, creates it for the repacking job.
-
-        It performs the following:
-            1) creates a source directory
-            2) copies the inference_entry_point inside it
-            3) copies the repack_model.py inside it
-            4) sets the source dir for the repacking estimator
-        """
-        self._source_dir = tempfile.mkdtemp()
-        self.estimator.source_dir = self._source_dir
+    name: str = attr.ib()
+    steps: List[Step] = attr.ib(factory=list)
 
-        shutil.copy2(self._entry_point, os.path.join(self._source_dir, self._entry_point_basename))
-        self._entry_point = self._entry_point_basename
-
-    def _inject_repack_script(self):
-        """Injects the _repack_model.py script into S3 or local source directory.
-
-        If the source_dir is an S3 path:
-            1) downloads the source_dir tar.gz
-            2) extracts it
-            3) copies the _repack_model.py script into the extracted directory
-            4) rezips the directory
-            5) overwrites the S3 source_dir with the new tar.gz
-
-        If the source_dir is a local path:
-            1) copies the _repack_model.py script into the source dir
-        """
-        fname = os.path.join(os.path.dirname(__file__), REPACK_SCRIPT)
-        if self._source_dir.lower().startswith("s3://"):
-            with tempfile.TemporaryDirectory() as tmp:
-                targz_contents_dir = os.path.join(tmp, "extracted")
-
-                old_targz_path = os.path.join(tmp, "old.tar.gz")
-                download_file_from_url(self._source_dir, old_targz_path, self.sagemaker_session)
-
-                with tarfile.open(name=old_targz_path, mode="r:gz") as t:
-                    t.extractall(path=targz_contents_dir)
-
-                shutil.copy2(fname, os.path.join(targz_contents_dir, REPACK_SCRIPT))
-
-                new_targz_path = os.path.join(tmp, "new.tar.gz")
-                with tarfile.open(new_targz_path, mode="w:gz") as t:
-                    t.add(targz_contents_dir, arcname=os.path.sep)
-
-                _save_model(self._source_dir, new_targz_path, self.sagemaker_session, kms_key=None)
-        else:
-            shutil.copy2(fname, os.path.join(self._source_dir, REPACK_SCRIPT))
-
-    @property
-    def arguments(self) -> RequestType:
-        """The arguments dict that are used to call `create_training_job`.
-
-        This first prepares the source bundle for repackinglby placing artifacts
-        in locations which the training container will make available to the
-        repacking script and then gets the arguments for the training job.
-        """
-        self._prepare_for_repacking()
-        return super(_RepackModelStep, self).arguments
+    def request_dicts(self) -> List[RequestType]:
+        """Get the request structure for workflow service calls."""
+        return [step.to_request() for step in self.steps]
 
     @property
     def properties(self):
-        """A Properties object representing the DescribeTrainingJobResponse data model."""
-        return self._properties
+        """The properties of the particular `StepCollection`."""
+        if not self.steps:
+            return None
+        return self.steps[-1].properties
 
 
-class _RegisterModelStep(ConfigurableRetryStep):
-    """Register model step in workflow that creates a model package."""
+class RegisterModel(StepCollection):  # pragma: no cover
+    """Register Model step collection for workflow."""
 
     def __init__(
         self,
         name: str,
-        step_args: Optional[dict] = None,
-        content_types: Optional[list] = None,
-        response_types: Optional[list] = None,
-        inference_instances: Optional[list] = None,
-        transform_instances: Optional[list] = None,
+        content_types,
+        response_types,
+        inference_instances=None,
+        transform_instances=None,
         estimator: EstimatorBase = None,
         model_data=None,
+        depends_on: Optional[List[Union[str, Step, StepCollection]]] = None,
+        repack_model_step_retry_policies: List[RetryPolicy] = None,
+        register_model_step_retry_policies: List[RetryPolicy] = None,
         model_package_group_name=None,
         model_metrics=None,
-        metadata_properties=None,
-        approval_status="PendingManualApproval",
+        approval_status=None,
         image_uri=None,
         compile_model_family=None,
-        display_name: str = None,
+        display_name=None,
         description=None,
-        depends_on: Optional[List[Union[str, Step, "StepCollection"]]] = None,
-        retry_policies: Optional[List[RetryPolicy]] = None,
         tags=None,
-        container_def_list=None,
+        model: Union[Model, PipelineModel] = None,
         drift_check_baselines=None,
         customer_metadata_properties=None,
         domain=None,
+        sample_payload_url=None,
+        task=None,
+        framework=None,
+        framework_version=None,
+        nearest_model_name=None,
+        data_input_configuration=None,
         **kwargs,
     ):
-        """Constructor of a register model step.
+        """Construct steps `_RepackModelStep` and `_RegisterModelStep` based on the estimator.
 
         Args:
             name (str): The name of the training step.
-            step_args (dict): The arguments for this `_RegisterModelStep` definition
-                (default: None).
+            estimator: The estimator instance.
+            model_data: The S3 uri to the model data from training.
             content_types (list): The supported MIME types for the input data (default: None).
             response_types (list): The supported MIME types for the output data (default: None).
             inference_instances (list): A list of the instance types that are used to
                 generate inferences in real-time (default: None).
-            transform_instances (list): A list of the instance types on which a
-                transformation job can be run or on which an endpoint
-                can be deployed (default: None).
-            estimator (EstimatorBase): A `sagemaker.estimator.EstimatorBase` instance
-                (default: None).
-            model_data: the S3 URI to the model data from training (default: None).
-            model_package_group_name (str): Model Package Group name, exclusive to
-                `model_package_name`, using `model_package_group_name`
-                makes the Model Package versioned (default: None).
+            transform_instances (list): A list of the instance types on which a transformation
+                job can be run or on which an endpoint can be deployed (default: None).
+            depends_on (List[Union[str, Step, StepCollection]]): The list of `Step`/`StepCollection`
+                names or `Step` instances or `StepCollection` instances that the first step
+                in the collection depends on (default: None).
+            repack_model_step_retry_policies (List[RetryPolicy]): The list of retry policies
+                for the repack model step
+            register_model_step_retry_policies (List[RetryPolicy]): The list of retry policies
+                for register model step
+            model_package_group_name (str): The Model Package Group name or Arn, exclusive to
+                `model_package_name`, using `model_package_group_name` makes the Model Package
+                versioned (default: None).
             model_metrics (ModelMetrics): ModelMetrics object (default: None).
-            metadata_properties (MetadataProperties): MetadataProperties object (default: None).
-            approval_status (str): Model Approval Status, values can be "Approved",
-                "Rejected", or "PendingManualApproval" (default: "PendingManualApproval").
+            approval_status (str): Model Approval Status, values can be "Approved", "Rejected",
+                or "PendingManualApproval" (default: "PendingManualApproval").
             image_uri (str): The container image uri for Model Package, if not specified,
-                Estimator's training container image will be used (default: None).
-            compile_model_family (str): Instance family for compiled model,
-                if specified, a compiled model will be used (default: None).
-            display_name (str): The display name of this `_RegisterModelStep` step (default: None).
+                Estimator's training container image is used (default: None).
+            compile_model_family (str): The instance family for the compiled model. If
+                specified, a compiled model is used (default: None).
             description (str): Model Package description (default: None).
-            depends_on (List[Union[str, Step, StepCollection]]): The list of `Step`/`StepCollection`
-                names or `Step` instances or `StepCollection` instances that the current `Step`
-                depends on (default: None).
-            retry_policies (List[RetryPolicy]): The list of retry policies for the current step
-                (default: None).
-            tags (List[dict[str, str]]): A list of dictionaries containing key-value pairs used to
-                configure the create model package request (default: None).
-            container_def_list (list): A list of container definitions (default: None).
+            tags (List[dict[str, str]]): The list of tags to attach to the model package group. Note
+                that tags will only be applied to newly created model package groups; if the
+                name of an existing group is passed to "model_package_group_name",
+                tags will not be applied.
+            model (object or Model): A PipelineModel object that comprises a list of models
+                which gets executed as a serial inference pipeline or a Model object.
             drift_check_baselines (DriftCheckBaselines): DriftCheckBaselines object (default: None).
             customer_metadata_properties (dict[str, str]): A dictionary of key-value paired
                 metadata properties (default: None).
             domain (str): Domain values can be "COMPUTER_VISION", "NATURAL_LANGUAGE_PROCESSING",
                 "MACHINE_LEARNING" (default: None).
+            sample_payload_url (str): The S3 path where the sample payload is stored
+                (default: None).
+            task (str): Task values which are supported by Inference Recommender are "FILL_MASK",
+                "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_GENERATION", "IMAGE_SEGMENTATION",
+                "CLASSIFICATION", "REGRESSION", "OTHER" (default: None).
+            framework (str): Machine learning framework of the model package container image
+                (default: None).
+            framework_version (str): Framework version of the Model Package Container Image
+                (default: None).
+            nearest_model_name (str): Name of a pre-trained machine learning benchmarked by
+                Amazon SageMaker Inference Recommender (default: None).
+            data_input_configuration (str): Input object for the model (default: None).
+
             **kwargs: additional arguments to `create_model`.
         """
-        super(_RegisterModelStep, self).__init__(
-            name, StepTypeEnum.REGISTER_MODEL, display_name, description, depends_on, retry_policies
+        self.name = name
+        steps: List[Step] = []
+        repack_model = False
+        self.model_list = None
+        self.container_def_list = None
+        subnets = None
+        security_group_ids = None
+
+        if estimator is not None:
+            subnets = estimator.subnets
+            security_group_ids = estimator.security_group_ids
+        elif model is not None and model.vpc_config is not None:
+            subnets = model.vpc_config["Subnets"]
+            security_group_ids = model.vpc_config["SecurityGroupIds"]
+
+        if "entry_point" in kwargs:
+            repack_model = True
+            entry_point = kwargs.pop("entry_point", None)
+            source_dir = kwargs.pop("source_dir", None)
+            dependencies = kwargs.pop("dependencies", None)
+            kwargs = dict(**kwargs, output_kms_key=kwargs.pop("model_kms_key", None))
+
+            repack_model_step = _RepackModelStep(
+                name=f"{name}RepackModel",
+                depends_on=depends_on,
+                retry_policies=repack_model_step_retry_policies,
+                sagemaker_session=estimator.sagemaker_session,
+                role=estimator.role,
+                model_data=model_data,
+                entry_point=entry_point,
+                source_dir=source_dir,
+                dependencies=dependencies,
+                tags=tags,
+                subnets=subnets,
+                security_group_ids=security_group_ids,
+                description=description,
+                display_name=display_name,
+                **kwargs,
+            )
+            steps.append(repack_model_step)
+            model_data = repack_model_step.properties.ModelArtifacts.S3ModelArtifacts
+
+            # remove kwargs consumed by model repacking step
+            kwargs.pop("output_kms_key", None)
+
+        elif model is not None:
+            if isinstance(model, PipelineModel):
+                self.model_list = model.models
+            elif isinstance(model, Model):
+                self.model_list = [model]
+
+            for model_entity in self.model_list:
+                if estimator is not None:
+                    sagemaker_session = estimator.sagemaker_session
+                    role = estimator.role
+                else:
+                    sagemaker_session = model_entity.sagemaker_session
+                    role = model_entity.role
+                if hasattr(model_entity, "entry_point") and model_entity.entry_point is not None:
+                    repack_model = True
+                    entry_point = model_entity.entry_point
+                    source_dir = model_entity.source_dir
+                    dependencies = model_entity.dependencies
+                    kwargs = dict(**kwargs, output_kms_key=model_entity.model_kms_key)
+                    model_name = model_entity.name or model_entity._framework_name
+
+                    repack_model_step = _RepackModelStep(
+                        name=f"{model_name}RepackModel",
+                        depends_on=depends_on,
+                        retry_policies=repack_model_step_retry_policies,
+                        sagemaker_session=sagemaker_session,
+                        role=role,
+                        model_data=model_entity.model_data,
+                        entry_point=entry_point,
+                        source_dir=source_dir,
+                        dependencies=dependencies,
+                        tags=tags,
+                        subnets=subnets,
+                        security_group_ids=security_group_ids,
+                        description=description,
+                        display_name=display_name,
+                        **kwargs,
+                    )
+                    steps.append(repack_model_step)
+                    model_entity.model_data = (
+                        repack_model_step.properties.ModelArtifacts.S3ModelArtifacts
+                    )
+
+                    # remove kwargs consumed by model repacking step
+                    kwargs.pop("output_kms_key", None)
+
+            if isinstance(model, PipelineModel):
+                self.container_def_list = model.pipeline_container_def(
+                    inference_instances[0] if inference_instances else None
+                )
+            elif isinstance(model, Model):
+                self.container_def_list = [
+                    model.prepare_container_def(
+                        inference_instances[0] if inference_instances else None
+                    )
+                ]
+
+            update_container_with_inference_params(
+                framework=framework,
+                framework_version=framework_version,
+                nearest_model_name=nearest_model_name,
+                data_input_configuration=data_input_configuration,
+                container_list=self.container_def_list,
+            )
+
+        register_model_step = _RegisterModelStep(
+            name=name,
+            estimator=estimator,
+            model_data=model_data,
+            content_types=content_types,
+            response_types=response_types,
+            inference_instances=inference_instances,
+            transform_instances=transform_instances,
+            model_package_group_name=model_package_group_name,
+            model_metrics=model_metrics,
+            drift_check_baselines=drift_check_baselines,
+            approval_status=approval_status,
+            image_uri=image_uri,
+            compile_model_family=compile_model_family,
+            description=description,
+            display_name=display_name,
+            tags=tags,
+            container_def_list=self.container_def_list,
+            retry_policies=register_model_step_retry_policies,
+            customer_metadata_properties=customer_metadata_properties,
+            domain=domain,
+            sample_payload_url=sample_payload_url,
+            task=task,
+            **kwargs,
         )
-        deprecated_args_missing = (
-            content_types is None
-            or response_types is None
-            or inference_instances is None
-            or transform_instances is None
+        if not repack_model:
+            register_model_step.add_depends_on(depends_on)
+
+        steps.append(register_model_step)
+        self.steps = steps
+
+        warnings.warn(
+            (
+                "We are deprecating the use of RegisterModel. "
+                "Please use the ModelStep instead. For more, see: "
+                "https://sagemaker.readthedocs.io/en/stable/"
+                "amazon_sagemaker_model_building_pipeline.html#model-step"
+            ),
+            DeprecationWarning,
         )
-        if not (step_args is None) ^ deprecated_args_missing:
-            raise ValueError(
-                "step_args and the set of (content_types, response_types, "
-                "inference_instances, transform_instances) are mutually exclusive. "
-                "Either of them should be provided."
-            )
 
-        self.step_args = step_args
-        self.estimator = estimator
-        self.model_data = model_data
-        self.content_types = content_types
-        self.response_types = response_types
-        self.inference_instances = inference_instances
-        self.transform_instances = transform_instances
-        self.model_package_group_name = model_package_group_name
-        self.tags = tags
-        self.model_metrics = model_metrics
-        self.drift_check_baselines = drift_check_baselines
-        self.customer_metadata_properties = customer_metadata_properties
-        self.domain = domain
-        self.metadata_properties = metadata_properties
-        self.approval_status = approval_status
-        self.image_uri = image_uri
-        self.compile_model_family = compile_model_family
-        self.description = description
-        self.tags = tags
-        self.kwargs = kwargs
-        self.container_def_list = container_def_list
 
-        self._properties = Properties(step_name=name, shape_name="DescribeModelPackageOutput")
+class EstimatorTransformer(StepCollection):
+    """Creates a Transformer step collection for workflow."""
 
-    @property
-    def arguments(self) -> RequestType:
-        """The arguments dict that are used to call `create_model_package`."""
-        model_name = self.name
-
-        if self.step_args:
-            request_dict = self.step_args
-        else:
-            if self.container_def_list is None:
-                if self.compile_model_family:
-                    model = self.estimator._compiled_models[self.compile_model_family]
-                    self.model_data = model.model_data
-                else:
-                    # create_model wants the estimator to have a model_data attribute...
-                    self.estimator._current_job_name = model_name
+    def __init__(
+        self,
+        name: str,
+        estimator: EstimatorBase,
+        model_data,
+        model_inputs,
+        instance_count,
+        instance_type,
+        transform_inputs,
+        description: str = None,
+        display_name: str = None,
+        # model arguments
+        image_uri=None,
+        predictor_cls=None,
+        env=None,
+        # transformer arguments
+        strategy=None,
+        assemble_with=None,
+        output_path=None,
+        output_kms_key=None,
+        accept=None,
+        max_concurrent_transforms=None,
+        max_payload=None,
+        tags=None,
+        volume_kms_key=None,
+        depends_on: Optional[List[Union[str, Step, StepCollection]]] = None,
+        # step retry policies
+        repack_model_step_retry_policies: List[RetryPolicy] = None,
+        model_step_retry_policies: List[RetryPolicy] = None,
+        transform_step_retry_policies: List[RetryPolicy] = None,
+        **kwargs,
+    ):
+        """Construct steps required for a Transformer step collection:
 
-                    # placeholder. replaced with model_data later
-                    output_path = self.estimator.output_path
-                    self.estimator.output_path = "/tmp"
-
-                    # create the model, but custom funky framework stuff going on in some places
-                    if self.image_uri:
-                        model = self.estimator.create_model(image_uri=self.image_uri, **self.kwargs)
-                    else:
-                        model = self.estimator.create_model(**self.kwargs)
-                        self.image_uri = model.image_uri
-
-                    if self.model_data is None:
-                        self.model_data = model.model_data
-
-                    # reset placeholder
-                    self.estimator.output_path = output_path
-
-                    # yeah, there is some framework stuff going on that we need to pull in here
-                    if self.image_uri is None:
-                        region_name = self.estimator.sagemaker_session.boto_session.region_name
-                        self.image_uri = image_uris.retrieve(
-                            model._framework_name,
-                            region_name,
-                            version=model.framework_version,
-                            py_version=model.py_version if hasattr(model, "py_version") else None,
-                            instance_type=self.kwargs.get(
-                                "instance_type", self.estimator.instance_type
-                            ),
-                            accelerator_type=self.kwargs.get("accelerator_type"),
-                            image_scope="inference",
-                        )
-                        model.name = model_name
-                        model.model_data = self.model_data
-
-            model_package_args = get_model_package_args(
-                content_types=self.content_types,
-                response_types=self.response_types,
-                inference_instances=self.inference_instances,
-                transform_instances=self.transform_instances,
-                model_package_group_name=self.model_package_group_name,
-                model_data=self.model_data,
-                image_uri=self.image_uri,
-                model_metrics=self.model_metrics,
-                drift_check_baselines=self.drift_check_baselines,
-                metadata_properties=self.metadata_properties,
-                approval_status=self.approval_status,
-                description=self.description,
-                tags=self.tags,
-                container_def_list=self.container_def_list,
-                customer_metadata_properties=self.customer_metadata_properties,
-                domain=self.domain,
+        An estimator-centric step collection. It models what happens in workflows
+        when invoking the `transform()` method on an estimator instance:
+        First, if custom
+        model artifacts are required, a `_RepackModelStep` is included.
+        Second, a
+        `CreateModelStep` with the model data passed in from a training step or other
+        training job output.
+        Finally, a `TransformerStep`.
+
+        If repacking
+        the model artifacts is not necessary, only the CreateModelStep and TransformerStep
+        are in the step collection.
+
+        Args:
+            name (str): The name of the Transform Step.
+            estimator: The estimator instance.
+            instance_count (int): The number of EC2 instances to use.
+            instance_type (str): The type of EC2 instance to use.
+            strategy (str): The strategy used to decide how to batch records in
+                a single request (default: None). Valid values: 'MultiRecord'
+                and 'SingleRecord'.
+            assemble_with (str): How the output is assembled (default: None).
+                Valid values: 'Line' or 'None'.
+            output_path (str): The S3 location for saving the transform result. If
+                not specified, results are stored to a default bucket.
+            output_kms_key (str): Optional. A KMS key ID for encrypting the
+                transform output (default: None).
+            accept (str): The accept header passed by the client to
+                the inference endpoint. If it is supported by the endpoint,
+                it will be the format of the batch transform output.
+            env (dict): The Environment variables to be set for use during the
+                transform job (default: None).
+            depends_on (List[Union[str, Step, StepCollection]]): The list of `Step`/`StepCollection`
+                names or `Step` instances or `StepCollection` instances that the first step
+                in the collection depends on (default: None).
+            repack_model_step_retry_policies (List[RetryPolicy]): The list of retry policies
+                for the repack model step
+            model_step_retry_policies (List[RetryPolicy]): The list of retry policies for
+                model step
+            transform_step_retry_policies (List[RetryPolicy]): The list of retry policies for
+                transform step
+        """
+        self.name = name
+        steps = []
+        if "entry_point" in kwargs:
+            entry_point = kwargs.get("entry_point", None)
+            source_dir = kwargs.get("source_dir", None)
+            dependencies = kwargs.get("dependencies", None)
+            repack_model_step = _RepackModelStep(
+                name=f"{name}RepackModel",
+                depends_on=depends_on,
+                retry_policies=repack_model_step_retry_policies,
+                sagemaker_session=estimator.sagemaker_session,
+                role=estimator.role,
+                model_data=model_data,
+                entry_point=entry_point,
+                source_dir=source_dir,
+                dependencies=dependencies,
+                tags=tags,
+                subnets=estimator.subnets,
+                security_group_ids=estimator.security_group_ids,
+                description=description,
+                display_name=display_name,
             )
+            steps.append(repack_model_step)
+            model_data = repack_model_step.properties.ModelArtifacts.S3ModelArtifacts
 
-            request_dict = get_create_model_package_request(**model_package_args)
-        # these are not available in the workflow service and will cause rejection
-        if "CertifyForMarketplace" in request_dict:
-            request_dict.pop("CertifyForMarketplace")
-        if "Description" in request_dict:
-            request_dict.pop("Description")
+        def predict_wrapper(endpoint, session):
+            return Predictor(endpoint, session)
 
-        return request_dict
+        predictor_cls = predictor_cls or predict_wrapper
 
-    @property
-    def properties(self):
-        """A Properties object representing the DescribeModelPackageOutput data model."""
-        return self._properties
+        model = Model(
+            image_uri=image_uri or estimator.training_image_uri(),
+            model_data=model_data,
+            predictor_cls=predictor_cls,
+            vpc_config=None,
+            sagemaker_session=estimator.sagemaker_session,
+            role=estimator.role,
+            env=kwargs.get("env", None),
+            name=kwargs.get("name", None),
+            enable_network_isolation=kwargs.get("enable_network_isolation", None),
+            model_kms_key=kwargs.get("model_kms_key", None),
+            image_config=kwargs.get("image_config", None),
+        )
+        model_step = CreateModelStep(
+            name=f"{name}CreateModelStep",
+            model=model,
+            inputs=model_inputs,
+            description=description,
+            display_name=display_name,
+            retry_policies=model_step_retry_policies,
+        )
+        if "entry_point" not in kwargs and depends_on:
+            # if the CreateModelStep is the first step in the collection
+            model_step.add_depends_on(depends_on)
+        steps.append(model_step)
+
+        transformer = Transformer(
+            model_name=model_step.properties.ModelName,
+            instance_count=instance_count,
+            instance_type=instance_type,
+            strategy=strategy,
+            assemble_with=assemble_with,
+            output_path=output_path,
+            output_kms_key=output_kms_key,
+            accept=accept,
+            max_concurrent_transforms=max_concurrent_transforms,
+            max_payload=max_payload,
+            env=env,
+            tags=tags,
+            base_transform_job_name=name,
+            volume_kms_key=volume_kms_key,
+            sagemaker_session=estimator.sagemaker_session,
+        )
+        transform_step = TransformStep(
+            name=f"{name}TransformStep",
+            transformer=transformer,
+            inputs=transform_inputs,
+            description=description,
+            display_name=display_name,
+            retry_policies=transform_step_retry_policies,
+        )
+        steps.append(transform_step)
+
+        self.steps = steps
```

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/airflow.py` & `sagemaker-2.99.0/src/sagemaker/workflow/airflow.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/callback_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/callback_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/check_job_config.py` & `sagemaker-2.99.0/src/sagemaker/workflow/check_job_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/clarify_check_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/clarify_check_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/condition_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/condition_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/conditions.py` & `sagemaker-2.99.0/src/sagemaker/workflow/conditions.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/emr_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/emr_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/entities.py` & `sagemaker-2.99.0/src/sagemaker/workflow/entities.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/execution_variables.py` & `sagemaker-2.99.0/src/sagemaker/workflow/execution_variables.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/fail_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/fail_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/functions.py` & `sagemaker-2.99.0/src/sagemaker/workflow/functions.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/lambda_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/lambda_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/model_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/model_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/parallelism_config.py` & `sagemaker-2.99.0/src/sagemaker/workflow/parallelism_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/parameters.py` & `sagemaker-2.99.0/src/sagemaker/workflow/parameters.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/pipeline.py` & `sagemaker-2.99.0/src/sagemaker/workflow/pipeline.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/pipeline_context.py` & `sagemaker-2.99.0/src/sagemaker/workflow/pipeline_context.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/pipeline_experiment_config.py` & `sagemaker-2.99.0/src/sagemaker/workflow/pipeline_experiment_config.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/properties.py` & `sagemaker-2.99.0/src/sagemaker/workflow/properties.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/quality_check_step.py` & `sagemaker-2.99.0/src/sagemaker/workflow/quality_check_step.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/retry.py` & `sagemaker-2.99.0/src/sagemaker/workflow/retry.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/steps.py` & `sagemaker-2.99.0/src/sagemaker/workflow/steps.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/workflow/utilities.py` & `sagemaker-2.99.0/src/sagemaker/workflow/utilities.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/wrangler/ingestion.py` & `sagemaker-2.99.0/src/sagemaker/wrangler/ingestion.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/wrangler/processing.py` & `sagemaker-2.99.0/src/sagemaker/wrangler/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/xgboost/__init__.py` & `sagemaker-2.99.0/src/sagemaker/xgboost/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/xgboost/defaults.py` & `sagemaker-2.99.0/src/sagemaker/xgboost/defaults.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/xgboost/estimator.py` & `sagemaker-2.99.0/src/sagemaker/xgboost/estimator.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/xgboost/model.py` & `sagemaker-2.99.0/src/sagemaker/xgboost/model.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/xgboost/processing.py` & `sagemaker-2.99.0/src/sagemaker/xgboost/processing.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker/xgboost/utils.py` & `sagemaker-2.99.0/src/sagemaker/xgboost/utils.py`

 * *Files identical despite different names*

### Comparing `sagemaker-2.98.0/src/sagemaker.egg-info/PKG-INFO` & `sagemaker-2.99.0/src/sagemaker.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemaker
-Version: 2.98.0
+Version: 2.99.0
 Summary: Open source library for training and deploying models on Amazon SageMaker.
 Home-page: https://github.com/aws/sagemaker-python-sdk/
 Author: Amazon Web Services
 License: Apache License 2.0
 Description: .. image:: https://github.com/aws/sagemaker-python-sdk/raw/master/branding/icon/sagemaker-banner.png
             :height: 100px
             :alt: SageMaker
```

### Comparing `sagemaker-2.98.0/src/sagemaker.egg-info/SOURCES.txt` & `sagemaker-2.99.0/src/sagemaker.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -28,14 +28,15 @@
 src/sagemaker/estimator.py
 src/sagemaker/exceptions.py
 src/sagemaker/fw_utils.py
 src/sagemaker/git_utils.py
 src/sagemaker/hyperparameters.py
 src/sagemaker/image_uris.py
 src/sagemaker/inputs.py
+src/sagemaker/instance_group.py
 src/sagemaker/job.py
 src/sagemaker/lambda_helper.py
 src/sagemaker/logs.py
 src/sagemaker/metadata_properties.py
 src/sagemaker/model.py
 src/sagemaker/model_metrics.py
 src/sagemaker/model_uris.py
```

### Comparing `sagemaker-2.98.0/src/sagemaker.egg-info/requires.txt` & `sagemaker-2.99.0/src/sagemaker.egg-info/requires.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-attrs==20.3.0
+attrs<22,>=20.3.0
 boto3<2.0,>=1.20.21
 google-pasta
 numpy<2.0,>=1.9.0
 protobuf<4.0,>=3.1
 protobuf3-to-dict<1.0,>=0.1.5
 smdebug_rulesconfig==1.0.1
 importlib-metadata<5.0,>=1.4.0
```

