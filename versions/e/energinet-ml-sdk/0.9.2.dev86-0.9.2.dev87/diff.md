# Comparing `tmp/energinet-ml-sdk-0.9.2.dev86.tar.gz` & `tmp/energinet-ml-sdk-0.9.2.dev87.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "energinet-ml-sdk-0.9.2.dev86.tar", last modified: Mon Feb 21 11:57:15 2022, max compression
+gzip compressed data, was "energinet-ml-sdk-0.9.2.dev87.tar", last modified: Thu Mar  3 11:38:06 2022, max compression
```

## Comparing `energinet-ml-sdk-0.9.2.dev86.tar` & `energinet-ml-sdk-0.9.2.dev87.tar`

### file list

```diff
@@ -1,137 +1,137 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/
--rw-r--r--   0 root         (0) root         (0)      592 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1733 2022-02-21 11:56:50.232928 energinet-ml-sdk-0.9.2.dev86/README
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.142928 energinet-ml-sdk-0.9.2.dev86/energinetml/
--rw-r--r--   0 root         (0) root         (0)     1708 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/__init__.py
--rw-r--r--   0 root         (0) root         (0)      122 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/__main__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.142928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/
--rw-r--r--   0 root         (0) root         (0)      210 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10809 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/backend.py
--rw-r--r--   0 root         (0) root         (0)     6295 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/datasets.py
--rw-r--r--   0 root         (0) root         (0)     4292 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/interactive.py
--rw-r--r--   0 root         (0) root         (0)     2130 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/logger.py
--rw-r--r--   0 root         (0) root         (0)     1135 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/submitting.py
--rw-r--r--   0 root         (0) root         (0)     7209 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/azure/training.py
--rw-r--r--   0 root         (0) root         (0)      190 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/backend.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.142928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/
--rw-r--r--   0 root         (0) root         (0)     1041 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.142928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/cluster/
--rw-r--r--   0 root         (0) root         (0)      382 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/cluster/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2038 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/cluster/change.py
--rw-r--r--   0 root         (0) root         (0)     6797 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/cluster/create.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.142928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/infrastructure/
--rw-r--r--   0 root         (0) root         (0)      351 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/infrastructure/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7297 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/infrastructure/init.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.162928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/
--rw-r--r--   0 root         (0) root         (0)      820 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/__init__.py
--rw-r--r--   0 root         (0) root         (0)      969 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/build.py
--rw-r--r--   0 root         (0) root         (0)      376 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/files.py
--rw-r--r--   0 root         (0) root         (0)     3885 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/init.py
--rw-r--r--   0 root         (0) root         (0)     2278 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/predict.py
--rw-r--r--   0 root         (0) root         (0)     5178 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/release.py
--rw-r--r--   0 root         (0) root         (0)     1041 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/serve.py
--rw-r--r--   0 root         (0) root         (0)     4081 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/submit.py
--rw-r--r--   0 root         (0) root         (0)     4674 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/train.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.162928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/project/
--rw-r--r--   0 root         (0) root         (0)      281 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/project/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2695 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/project/init.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.162928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/utils/
--rw-r--r--   0 root         (0) root         (0)      384 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9325 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/utils/decorators.py
--rw-r--r--   0 root         (0) root         (0)    10233 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/utils/projects.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.162928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/
--rw-r--r--   0 root         (0) root         (0)      410 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/__init__.py
--rw-r--r--   0 root         (0) root         (0)      562 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/build.py
--rw-r--r--   0 root         (0) root         (0)     4515 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/init.py
--rw-r--r--   0 root         (0) root         (0)      618 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/serve.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.172928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/
--rw-r--r--   0 root         (0) root         (0)       33 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4530 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/backend.py
--rw-r--r--   0 root         (0) root         (0)     3649 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/configurable.py
--rw-r--r--   0 root         (0) root         (0)     3079 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/docker.py
--rw-r--r--   0 root         (0) root         (0)     3022 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/files.py
--rw-r--r--   0 root         (0) root         (0)     7681 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/http.py
--rw-r--r--   0 root         (0) root         (0)     4419 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/insight.py
--rw-r--r--   0 root         (0) root         (0)     3802 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/logger.py
--rw-r--r--   0 root         (0) root         (0)    16093 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/model.py
--rw-r--r--   0 root         (0) root         (0)    11449 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/predicting.py
--rw-r--r--   0 root         (0) root         (0)     4144 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/project.py
--rw-r--r--   0 root         (0) root         (0)     1871 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/requirements.py
--rw-r--r--   0 root         (0) root         (0)      595 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/submitting.py
--rw-r--r--   0 root         (0) root         (0)     8722 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/templates.py
--rw-r--r--   0 root         (0) root         (0)     2867 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/training.py
--rw-r--r--   0 root         (0) root         (0)    13644 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/validation.py
--rw-r--r--   0 root         (0) root         (0)     1265 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/core/webapp.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.172928 energinet-ml-sdk-0.9.2.dev86/energinetml/meta/
--rw-r--r--   0 root         (0) root         (0)       12 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/meta/COMMAND_NAME
--rw-r--r--   0 root         (0) root         (0)       17 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/meta/PACKAGE_NAME
--rw-r--r--   0 root         (0) root         (0)       11 2022-02-21 11:57:14.502928 energinet-ml-sdk-0.9.2.dev86/energinetml/meta/PACKAGE_VERSION
--rw-r--r--   0 root         (0) root         (0)        4 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/meta/PYTHON_VERSION
--rw-r--r--   0 root         (0) root         (0)     2479 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/settings.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.172928 energinet-ml-sdk-0.9.2.dev86/energinetml/static/
--rw-r--r--   0 root         (0) root         (0)      531 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/static/Dockerfile
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.172928 energinet-ml-sdk-0.9.2.dev86/energinetml/static/model_template/
--rw-r--r--   0 root         (0) root         (0)      233 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/static/model_template/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2079 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/energinetml/static/model_template/model.py
--rw-r--r--   0 root         (0) root         (0)     4742 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.172928 energinet-ml-sdk-0.9.2.dev86/tests/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4730 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/conftest.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml/__init__.py
--rw-r--r--   0 root         (0) root         (0)      810 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml/model.py
--rw-r--r--   0 root         (0) root         (0)    15081 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml/smoke_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml_deployment/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml_deployment/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1091 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml_deployment/deployment_smoke_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/webapp_deployment/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/webapp_deployment/__init__.py
--rw-r--r--   0 root         (0) root         (0)      515 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/smoketest/webapp_deployment/deployment_smoke_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/azure_/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/azure_/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9598 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/azure_/backend_test.py
--rw-r--r--   0 root         (0) root         (0)     4350 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/azure_/datasets_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/cluster/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/cluster/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2892 2022-02-21 11:56:50.242928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/cluster/change_test.py
--rw-r--r--   0 root         (0) root         (0)     9457 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/cluster/create_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/infrastructure/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/infrastructure/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3517 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/infrastructure/init_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2371 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/build_test.py
--rw-r--r--   0 root         (0) root         (0)     2040 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/files_test.py
--rw-r--r--   0 root         (0) root         (0)     3739 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/init_test.py
--rw-r--r--   0 root         (0) root         (0)     6791 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/predict_test.py
--rw-r--r--   0 root         (0) root         (0)     2187 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/release_test.py
--rw-r--r--   0 root         (0) root         (0)     4562 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/submit_test.py
--rw-r--r--   0 root         (0) root         (0)     3424 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/train_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/project/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/project/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2310 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/project/init_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/utils/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4480 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/utils/decorators_test.py
--rw-r--r--   0 root         (0) root         (0)     7760 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/utils/projects_test.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-02-21 11:57:15.182928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/
--rw-r--r--   0 root         (0) root         (0)        0 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2945 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/backend_test.py
--rw-r--r--   0 root         (0) root         (0)     1126 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/configurable_test.py
--rw-r--r--   0 root         (0) root         (0)     1889 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/docker_test.py
--rw-r--r--   0 root         (0) root         (0)     1069 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/files_test.py
--rw-r--r--   0 root         (0) root         (0)    11355 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/http_test.py
--rw-r--r--   0 root         (0) root         (0)    13338 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/insight_test.py
--rw-r--r--   0 root         (0) root         (0)     2106 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/logger_test.py
--rw-r--r--   0 root         (0) root         (0)     9230 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/model_test.py
--rw-r--r--   0 root         (0) root         (0)     1638 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/predicting_test.py
--rw-r--r--   0 root         (0) root         (0)     2387 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/predicting_validator_test.py
--rw-r--r--   0 root         (0) root         (0)     2874 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/project_test.py
--rw-r--r--   0 root         (0) root         (0)     2378 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/requirements_test.py
--rw-r--r--   0 root         (0) root         (0)      812 2022-02-21 11:56:50.252928 energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/submitting_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.072668 energinet-ml-sdk-0.9.2.dev87/
+-rw-r--r--   0 root         (0) root         (0)      592 2022-03-03 11:38:06.072668 energinet-ml-sdk-0.9.2.dev87/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1733 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/README
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.032668 energinet-ml-sdk-0.9.2.dev87/energinetml/
+-rw-r--r--   0 root         (0) root         (0)     1708 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      122 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/__main__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.032668 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/
+-rw-r--r--   0 root         (0) root         (0)      210 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10809 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/backend.py
+-rw-r--r--   0 root         (0) root         (0)     6295 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/datasets.py
+-rw-r--r--   0 root         (0) root         (0)     4292 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/interactive.py
+-rw-r--r--   0 root         (0) root         (0)     2130 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/logger.py
+-rw-r--r--   0 root         (0) root         (0)     1135 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/submitting.py
+-rw-r--r--   0 root         (0) root         (0)     7209 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/azure/training.py
+-rw-r--r--   0 root         (0) root         (0)      190 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/backend.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.032668 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/
+-rw-r--r--   0 root         (0) root         (0)     1041 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.042668 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/cluster/
+-rw-r--r--   0 root         (0) root         (0)      382 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/cluster/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2038 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/cluster/change.py
+-rw-r--r--   0 root         (0) root         (0)     6797 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/cluster/create.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.042668 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/infrastructure/
+-rw-r--r--   0 root         (0) root         (0)      351 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/infrastructure/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7297 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/infrastructure/init.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.042668 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/
+-rw-r--r--   0 root         (0) root         (0)      820 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      969 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/build.py
+-rw-r--r--   0 root         (0) root         (0)      376 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/files.py
+-rw-r--r--   0 root         (0) root         (0)     3885 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/init.py
+-rw-r--r--   0 root         (0) root         (0)     2278 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/predict.py
+-rw-r--r--   0 root         (0) root         (0)     5178 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/release.py
+-rw-r--r--   0 root         (0) root         (0)     1041 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/serve.py
+-rw-r--r--   0 root         (0) root         (0)     4081 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/submit.py
+-rw-r--r--   0 root         (0) root         (0)     4674 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/train.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.042668 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/project/
+-rw-r--r--   0 root         (0) root         (0)      281 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/project/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2695 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/project/init.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.042668 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/utils/
+-rw-r--r--   0 root         (0) root         (0)      384 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9325 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/utils/decorators.py
+-rw-r--r--   0 root         (0) root         (0)    10233 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/utils/projects.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.052668 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/
+-rw-r--r--   0 root         (0) root         (0)      410 2022-03-03 11:37:41.192669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      562 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/build.py
+-rw-r--r--   0 root         (0) root         (0)     4515 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/init.py
+-rw-r--r--   0 root         (0) root         (0)      618 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/serve.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.052668 energinet-ml-sdk-0.9.2.dev87/energinetml/core/
+-rw-r--r--   0 root         (0) root         (0)       33 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4530 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/backend.py
+-rw-r--r--   0 root         (0) root         (0)     3649 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/configurable.py
+-rw-r--r--   0 root         (0) root         (0)     3079 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/docker.py
+-rw-r--r--   0 root         (0) root         (0)     3022 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/files.py
+-rw-r--r--   0 root         (0) root         (0)     7681 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/http.py
+-rw-r--r--   0 root         (0) root         (0)     4419 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/insight.py
+-rw-r--r--   0 root         (0) root         (0)     3802 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/logger.py
+-rw-r--r--   0 root         (0) root         (0)    16093 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/model.py
+-rw-r--r--   0 root         (0) root         (0)    11449 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/predicting.py
+-rw-r--r--   0 root         (0) root         (0)     4144 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/project.py
+-rw-r--r--   0 root         (0) root         (0)     1871 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/requirements.py
+-rw-r--r--   0 root         (0) root         (0)      595 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/submitting.py
+-rw-r--r--   0 root         (0) root         (0)     8722 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/templates.py
+-rw-r--r--   0 root         (0) root         (0)     2867 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/training.py
+-rw-r--r--   0 root         (0) root         (0)    13644 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/validation.py
+-rw-r--r--   0 root         (0) root         (0)     1265 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/core/webapp.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.052668 energinet-ml-sdk-0.9.2.dev87/energinetml/meta/
+-rw-r--r--   0 root         (0) root         (0)       12 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/meta/COMMAND_NAME
+-rw-r--r--   0 root         (0) root         (0)       17 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/meta/PACKAGE_NAME
+-rw-r--r--   0 root         (0) root         (0)       11 2022-03-03 11:38:05.522668 energinet-ml-sdk-0.9.2.dev87/energinetml/meta/PACKAGE_VERSION
+-rw-r--r--   0 root         (0) root         (0)        4 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/meta/PYTHON_VERSION
+-rw-r--r--   0 root         (0) root         (0)     2479 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/settings.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.052668 energinet-ml-sdk-0.9.2.dev87/energinetml/static/
+-rw-r--r--   0 root         (0) root         (0)      531 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/static/Dockerfile
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.052668 energinet-ml-sdk-0.9.2.dev87/energinetml/static/model_template/
+-rw-r--r--   0 root         (0) root         (0)      233 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/static/model_template/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2079 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/energinetml/static/model_template/model.py
+-rw-r--r--   0 root         (0) root         (0)     4742 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4730 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/conftest.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      810 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml/model.py
+-rw-r--r--   0 root         (0) root         (0)    15081 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml/smoke_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml_deployment/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml_deployment/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1091 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml_deployment/deployment_smoke_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/webapp_deployment/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/webapp_deployment/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      515 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/smoketest/webapp_deployment/deployment_smoke_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/azure_/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/azure_/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9598 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/azure_/backend_test.py
+-rw-r--r--   0 root         (0) root         (0)     4350 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/azure_/datasets_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/cluster/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/cluster/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2892 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/cluster/change_test.py
+-rw-r--r--   0 root         (0) root         (0)     9457 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/cluster/create_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.062668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/infrastructure/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/infrastructure/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3517 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/infrastructure/init_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.072668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2371 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/build_test.py
+-rw-r--r--   0 root         (0) root         (0)     2040 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/files_test.py
+-rw-r--r--   0 root         (0) root         (0)     3739 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/init_test.py
+-rw-r--r--   0 root         (0) root         (0)     6791 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/predict_test.py
+-rw-r--r--   0 root         (0) root         (0)     2187 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/release_test.py
+-rw-r--r--   0 root         (0) root         (0)     4562 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/submit_test.py
+-rw-r--r--   0 root         (0) root         (0)     3424 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/train_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.072668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/project/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/project/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2310 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/project/init_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.072668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/utils/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4480 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/utils/decorators_test.py
+-rw-r--r--   0 root         (0) root         (0)     7760 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/utils/projects_test.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-03 11:38:06.072668 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2945 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/backend_test.py
+-rw-r--r--   0 root         (0) root         (0)     1126 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/configurable_test.py
+-rw-r--r--   0 root         (0) root         (0)     1889 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/docker_test.py
+-rw-r--r--   0 root         (0) root         (0)     1069 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/files_test.py
+-rw-r--r--   0 root         (0) root         (0)    11355 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/http_test.py
+-rw-r--r--   0 root         (0) root         (0)    13338 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/insight_test.py
+-rw-r--r--   0 root         (0) root         (0)     2106 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/logger_test.py
+-rw-r--r--   0 root         (0) root         (0)     9230 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/model_test.py
+-rw-r--r--   0 root         (0) root         (0)     1638 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/predicting_test.py
+-rw-r--r--   0 root         (0) root         (0)     2387 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/predicting_validator_test.py
+-rw-r--r--   0 root         (0) root         (0)     2874 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/project_test.py
+-rw-r--r--   0 root         (0) root         (0)     2378 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/requirements_test.py
+-rw-r--r--   0 root         (0) root         (0)      812 2022-03-03 11:37:41.202669 energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/submitting_test.py
```

### Comparing `energinet-ml-sdk-0.9.2.dev86/README` & `energinet-ml-sdk-0.9.2.dev87/README`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/__init__.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/__init__.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/azure/backend.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/azure/backend.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/azure/datasets.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/azure/datasets.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/azure/interactive.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/azure/interactive.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/azure/logger.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/azure/logger.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/azure/submitting.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/azure/submitting.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/azure/training.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/azure/training.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/__init__.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/cluster/change.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/cluster/change.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/cluster/create.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/cluster/create.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/infrastructure/init.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/infrastructure/init.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/__init__.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/__init__.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/build.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/build.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/init.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/init.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/predict.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/predict.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/release.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/release.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/serve.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/serve.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/submit.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/submit.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/model/train.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/model/train.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/project/init.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/project/init.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/utils/decorators.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/utils/decorators.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/utils/projects.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/utils/projects.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/build.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/build.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/init.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/init.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/cli/webapp/serve.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/cli/webapp/serve.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/backend.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/backend.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/configurable.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/configurable.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/docker.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/docker.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/files.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/files.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/http.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/http.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/insight.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/insight.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/logger.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/logger.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/model.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/model.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/predicting.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/predicting.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/project.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/project.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/requirements.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/requirements.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/submitting.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/submitting.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/templates.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/templates.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/training.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/training.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/validation.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/validation.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/core/webapp.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/core/webapp.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/settings.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/settings.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/static/Dockerfile` & `energinet-ml-sdk-0.9.2.dev87/energinetml/static/Dockerfile`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/energinetml/static/model_template/model.py` & `energinet-ml-sdk-0.9.2.dev87/energinetml/static/model_template/model.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/setup.py` & `energinet-ml-sdk-0.9.2.dev87/setup.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/conftest.py` & `energinet-ml-sdk-0.9.2.dev87/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml/model.py` & `energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml/model.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml/smoke_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml/smoke_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/smoketest/ml_deployment/deployment_smoke_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/smoketest/ml_deployment/deployment_smoke_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/smoketest/webapp_deployment/deployment_smoke_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/smoketest/webapp_deployment/deployment_smoke_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/azure_/backend_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/azure_/backend_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/azure_/datasets_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/azure_/datasets_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/cluster/change_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/cluster/change_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/cluster/create_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/cluster/create_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/infrastructure/init_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/infrastructure/init_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/build_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/build_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/files_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/files_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/init_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/init_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/predict_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/predict_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/release_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/release_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/submit_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/submit_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/model/train_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/model/train_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/project/init_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/project/init_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/utils/decorators_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/utils/decorators_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/cli/utils/projects_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/cli/utils/projects_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/backend_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/backend_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/configurable_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/configurable_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/docker_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/docker_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/files_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/files_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/http_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/http_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/insight_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/insight_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/logger_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/logger_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/model_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/model_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/predicting_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/predicting_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/predicting_validator_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/predicting_validator_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/project_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/project_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/requirements_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/requirements_test.py`

 * *Files identical despite different names*

### Comparing `energinet-ml-sdk-0.9.2.dev86/tests/unittests/core/submitting_test.py` & `energinet-ml-sdk-0.9.2.dev87/tests/unittests/core/submitting_test.py`

 * *Files identical despite different names*

