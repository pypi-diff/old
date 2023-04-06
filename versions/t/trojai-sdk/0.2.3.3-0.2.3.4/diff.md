# Comparing `tmp/trojai-sdk-0.2.3.3.tar.gz` & `tmp/trojai-sdk-0.2.3.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "C:\Users\Barrie Tomilson\Documents\github (2)\sdk\troj-sdk\dist\.tmp-juvv7ysb\trojai-sdk-0.2.3.3.tar", last modified: Mon Apr  3 16:22:58 2023, max compression
+gzip compressed data, was "C:\Users\Barrie Tomilson\Documents\github (2)\sdk\troj-sdk\dist\.tmp-kv1vjbs5\trojai-sdk-0.2.3.4.tar", last modified: Thu Apr  6 13:53:04 2023, max compression
```

## Comparing `trojai-sdk-0.2.3.3.tar` & `trojai-sdk-0.2.3.4.tar`

### file list

```diff
@@ -1,93 +1,92 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.984113 trojai-sdk-0.2.3.3/
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.356106 trojai-sdk-0.2.3.3/.github/
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.424104 trojai-sdk-0.2.3.3/.github/workflows/
--rw-rw-rw-   0        0        0     1213 2023-03-28 21:13:31.000000 trojai-sdk-0.2.3.3/.github/workflows/python-app.yml
--rw-rw-rw-   0        0        0       93 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/.gitignore
--rw-rw-rw-   0        0        0     1525 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/.gitlab-ci.yml
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.436103 trojai-sdk-0.2.3.3/.vscode/
--rw-rw-rw-   0        0        0      510 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/.vscode/launch.json
--rw-rw-rw-   0        0        0      167 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/MANIFEST.in
--rw-rw-rw-   0        0        0     3107 2023-04-03 16:22:58.984113 trojai-sdk-0.2.3.3/PKG-INFO
--rw-rw-rw-   0        0        0     2508 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/README.md
--rw-rw-rw-   0        0        0     3151 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/auth_config_dev.json
--rw-rw-rw-   0        0        0      102 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/requirements.txt
--rw-rw-rw-   0        0        0       42 2023-04-03 16:22:58.984113 trojai-sdk-0.2.3.3/setup.cfg
--rw-rw-rw-   0        0        0      995 2023-03-30 14:02:52.000000 trojai-sdk-0.2.3.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.360106 trojai-sdk-0.2.3.3/test_proj/
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.360106 trojai-sdk-0.2.3.3/test_proj/credit_dataset/
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.512106 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/
--rw-rw-rw-   0        0        0     1080 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/attacks.json
--rw-rw-rw-   0        0        0      154 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/auth.json
--rw-rw-rw-   0        0        0      938 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/base.json
--rw-rw-rw-   0        0        0      169 2023-03-31 16:34:26.000000 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/docker_config.json
--rw-rw-rw-   0        0        0      323 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/k8s_config.json
--rw-rw-rw-   0        0        0      122 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/model_config.json
--rw-rw-rw-   0        0        0      185 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/test_config.json
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.536105 trojai-sdk-0.2.3.3/trojai_sdk.egg-info/
--rw-rw-rw-   0        0        0     3107 2023-04-03 16:22:58.000000 trojai-sdk-0.2.3.3/trojai_sdk.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     2669 2023-04-03 16:22:58.000000 trojai-sdk-0.2.3.3/trojai_sdk.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 16:22:58.000000 trojai-sdk-0.2.3.3/trojai_sdk.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       42 2023-04-03 16:22:58.000000 trojai-sdk-0.2.3.3/trojai_sdk.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       95 2023-04-03 16:22:58.000000 trojai-sdk-0.2.3.3/trojai_sdk.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2023-04-03 16:22:58.000000 trojai-sdk-0.2.3.3/trojai_sdk.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.584108 trojai-sdk-0.2.3.3/trojsdk/
--rw-rw-rw-   0        0        0        0 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/__init__.py
--rw-rw-rw-   0        0        0     7328 2023-03-30 14:02:46.000000 trojai-sdk-0.2.3.3/trojsdk/client.py
--rw-rw-rw-   0        0        0     2937 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/cmd.py
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.636160 trojai-sdk-0.2.3.3/trojsdk/config/
--rw-rw-rw-   0        0        0        0 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/config/__init__.py
--rw-rw-rw-   0        0        0     4640 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/config/auth.py
--rw-rw-rw-   0        0        0     4558 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/config/base.py
--rw-rw-rw-   0        0        0     2064 2023-03-30 14:02:52.000000 trojai-sdk-0.2.3.3/trojsdk/config/nlp.py
--rw-rw-rw-   0        0        0     2067 2023-01-27 14:50:38.000000 trojai-sdk-0.2.3.3/trojsdk/config/tabular.py
--rw-rw-rw-   0        0        0     2818 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/config/vision.py
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.664142 trojai-sdk-0.2.3.3/trojsdk/configs/
--rw-rw-rw-   0        0        0     3239 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/auth_config.json
--rw-rw-rw-   0        0        0     2397 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/auth_config_dev.json
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.704103 trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/
--rw-rw-rw-   0        0        0     1080 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/all_pipe_transform_config.json
--rw-rw-rw-   0        0        0      414 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/s3_classification_config.json
--rw-rw-rw-   0        0        0      198 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/s3_starKNN_config.json
--rw-rw-rw-   0        0        0      383 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/s3_stars_validation_config.json
--rw-rw-rw-   0        0        0     3238 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/troj_dev_auth.json
--rw-rw-rw-   0        0        0     1173 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/configs/testing_config.json
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.756141 trojai-sdk-0.2.3.3/trojsdk/core/
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.768142 trojai-sdk-0.2.3.3/trojsdk/core/ExperimentTools/
--rw-rw-rw-   0        0        0        0 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/core/ExperimentTools/TrojExperiment.py
--rw-rw-rw-   0        0        0    13132 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/core/ExperimentTools/__init__.py
--rw-rw-rw-   0        0        0        0 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/core/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.772106 trojai-sdk-0.2.3.3/trojsdk/core/__pycache__/
--rw-rw-rw-   0        0        0     2730 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/core/__pycache__/data_utils.cpython-38.pyc
--rw-rw-rw-   0        0        0     7244 2023-03-30 14:02:46.000000 trojai-sdk-0.2.3.3/trojsdk/core/client_utils.py
--rw-rw-rw-   0        0        0     4613 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/core/data_utils.py
--rw-rw-rw-   0        0        0     2081 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/core/test_experiment_gen.py
--rw-rw-rw-   0        0        0     1431 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/core/troj_error.py
--rw-rw-rw-   0        0        0      330 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/core/troj_logging.py
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.852121 trojai-sdk-0.2.3.3/trojsdk/examples/
--rw-rw-rw-   0        0        0     3239 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/auth_config.json
--rw-rw-rw-   0        0        0      357 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/auth_config_dev.json
--rw-rw-rw-   0        0        0      216 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/examples/docker_meta.json
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.864107 trojai-sdk-0.2.3.3/trojsdk/examples/gcloud_tests/
--rw-rw-rw-   0        0        0      640 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/gcloud_tests/gcloud_auth.json
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.920104 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/
--rw-rw-rw-   0        0        0      280 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/attacks.json
--rw-rw-rw-   0        0        0     2337 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/label_map_num.json
--rw-rw-rw-   0        0        0      117 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/model_config.json
--rw-rw-rw-   0        0        0      276 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/test_config.json
--rw-rw-rw-   0        0        0      281 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/train_config.json
--rw-rw-rw-   0        0        0      572 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/troj_config.json
--rw-rw-rw-   0        0        0     4594 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil_test.json
--rw-rw-rw-   0        0        0     1855 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/nlp_test_main.json
--rw-rw-rw-   0        0        0    24617 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.3/trojsdk/examples/s3_small_classification_pt_config.json
--rw-rw-rw-   0        0        0     1562 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_SMOTETomek_logistic_base.json
--rw-rw-rw-   0        0        0     3380 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_medical_insurance_config.json
-drwxrwxrwx   0        0        0        0 2023-04-03 16:22:58.980107 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/
--rw-rw-rw-   0        0        0     1080 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/all_pipe_transform_config.json
--rw-rw-rw-   0        0        0      435 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/s3_classification_config.json
--rw-rw-rw-   0        0        0      212 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/s3_starKNN_config.json
--rw-rw-rw-   0        0        0      381 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/s3_stars_validation_config.json
--rw-rw-rw-   0        0        0     2006 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/tabular_test_main.json
--rw-rw-rw-   0        0        0     2406 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/troj_dev_auth.json
--rw-rw-rw-   0        0        0     1183 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/examples/testing_config.json
--rw-rw-rw-   0        0        0      989 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.3/trojsdk/setup.py
--rw-rw-rw-   0        0        0      743 2023-04-03 16:20:56.000000 trojai-sdk-0.2.3.3/trojsdk/test_sdk.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.709624 trojai-sdk-0.2.3.4/
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.480621 trojai-sdk-0.2.3.4/.github/
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.519622 trojai-sdk-0.2.3.4/.github/workflows/
+-rw-rw-rw-   0        0        0     1213 2023-03-28 21:13:31.000000 trojai-sdk-0.2.3.4/.github/workflows/python-app.yml
+-rw-rw-rw-   0        0        0      104 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/.gitignore
+-rw-rw-rw-   0        0        0     1525 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/.gitlab-ci.yml
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.521620 trojai-sdk-0.2.3.4/.vscode/
+-rw-rw-rw-   0        0        0      510 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/.vscode/launch.json
+-rw-rw-rw-   0        0        0      167 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/MANIFEST.in
+-rw-rw-rw-   0        0        0     3104 2023-04-06 13:53:04.708621 trojai-sdk-0.2.3.4/PKG-INFO
+-rw-rw-rw-   0        0        0     2505 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/README.md
+-rw-rw-rw-   0        0        0      372 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/auth_config_dev.json
+-rw-rw-rw-   0        0        0      102 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/requirements.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 13:53:04.710620 trojai-sdk-0.2.3.4/setup.cfg
+-rw-rw-rw-   0        0        0      995 2023-04-06 13:51:19.000000 trojai-sdk-0.2.3.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.484621 trojai-sdk-0.2.3.4/test_proj/
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.485622 trojai-sdk-0.2.3.4/test_proj/credit_dataset/
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.555620 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/
+-rw-rw-rw-   0        0        0     1296 2023-04-06 13:17:36.000000 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/attacks.json
+-rw-rw-rw-   0        0        0      154 2023-04-06 13:17:36.000000 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/auth.json
+-rw-rw-rw-   0        0        0      808 2023-04-06 13:17:36.000000 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/base.json
+-rw-rw-rw-   0        0        0      169 2023-04-06 13:17:36.000000 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/docker_config.json
+-rw-rw-rw-   0        0        0      266 2023-04-06 13:17:36.000000 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/k8s_config.json
+-rw-rw-rw-   0        0        0      257 2023-04-06 13:17:36.000000 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/model_config.json
+-rw-rw-rw-   0        0        0      356 2023-04-06 13:17:35.000000 trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/test_config.json
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.586618 trojai-sdk-0.2.3.4/trojai_sdk.egg-info/
+-rw-rw-rw-   0        0        0     3104 2023-04-06 13:53:04.000000 trojai-sdk-0.2.3.4/trojai_sdk.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     2623 2023-04-06 13:53:04.000000 trojai-sdk-0.2.3.4/trojai_sdk.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 13:53:04.000000 trojai-sdk-0.2.3.4/trojai_sdk.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 13:53:04.000000 trojai-sdk-0.2.3.4/trojai_sdk.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       95 2023-04-06 13:53:04.000000 trojai-sdk-0.2.3.4/trojai_sdk.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 13:53:04.000000 trojai-sdk-0.2.3.4/trojai_sdk.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.599619 trojai-sdk-0.2.3.4/trojsdk/
+-rw-rw-rw-   0        0        0        0 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/__init__.py
+-rw-rw-rw-   0        0        0     7328 2023-03-30 14:02:46.000000 trojai-sdk-0.2.3.4/trojsdk/client.py
+-rw-rw-rw-   0        0        0     2937 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/cmd.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.612619 trojai-sdk-0.2.3.4/trojsdk/config/
+-rw-rw-rw-   0        0        0        0 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/config/__init__.py
+-rw-rw-rw-   0        0        0     4640 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/config/auth.py
+-rw-rw-rw-   0        0        0     4558 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/config/base.py
+-rw-rw-rw-   0        0        0     2064 2023-03-30 14:02:52.000000 trojai-sdk-0.2.3.4/trojsdk/config/nlp.py
+-rw-rw-rw-   0        0        0     2067 2023-01-27 14:50:38.000000 trojai-sdk-0.2.3.4/trojsdk/config/tabular.py
+-rw-rw-rw-   0        0        0     2818 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/config/vision.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.618622 trojai-sdk-0.2.3.4/trojsdk/configs/
+-rw-rw-rw-   0        0        0     3239 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/auth_config.json
+-rw-rw-rw-   0        0        0     2397 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/auth_config_dev.json
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.631622 trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/
+-rw-rw-rw-   0        0        0     1080 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/all_pipe_transform_config.json
+-rw-rw-rw-   0        0        0      414 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/s3_classification_config.json
+-rw-rw-rw-   0        0        0      198 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/s3_starKNN_config.json
+-rw-rw-rw-   0        0        0      383 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/s3_stars_validation_config.json
+-rw-rw-rw-   0        0        0     3238 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/troj_dev_auth.json
+-rw-rw-rw-   0        0        0     1173 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/configs/testing_config.json
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.645621 trojai-sdk-0.2.3.4/trojsdk/core/
+-rw-rw-rw-   0        0        0        0 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/core/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.647621 trojai-sdk-0.2.3.4/trojsdk/core/__pycache__/
+-rw-rw-rw-   0        0        0     3398 2023-04-06 13:15:21.000000 trojai-sdk-0.2.3.4/trojsdk/core/__pycache__/data_utils.cpython-38.pyc
+-rw-rw-rw-   0        0        0     7244 2023-03-30 14:02:46.000000 trojai-sdk-0.2.3.4/trojsdk/core/client_utils.py
+-rw-rw-rw-   0        0        0     5401 2023-04-06 13:14:32.000000 trojai-sdk-0.2.3.4/trojsdk/core/data_utils.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.649618 trojai-sdk-0.2.3.4/trojsdk/core/experiment_tools/
+-rw-rw-rw-   0        0        0    14187 2023-04-06 13:17:07.000000 trojai-sdk-0.2.3.4/trojsdk/core/experiment_tools/__init__.py
+-rw-rw-rw-   0        0        0     3670 2023-04-06 13:12:22.000000 trojai-sdk-0.2.3.4/trojsdk/core/test_experiment_gen.py
+-rw-rw-rw-   0        0        0     1431 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/core/troj_error.py
+-rw-rw-rw-   0        0        0      330 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/core/troj_logging.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.675619 trojai-sdk-0.2.3.4/trojsdk/examples/
+-rw-rw-rw-   0        0        0     3239 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/auth_config.json
+-rw-rw-rw-   0        0        0      469 2023-04-05 17:56:30.000000 trojai-sdk-0.2.3.4/trojsdk/examples/auth_config_dev.json
+-rw-rw-rw-   0        0        0      216 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/examples/docker_meta.json
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.677619 trojai-sdk-0.2.3.4/trojsdk/examples/gcloud_tests/
+-rw-rw-rw-   0        0        0      640 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/gcloud_tests/gcloud_auth.json
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.689622 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/
+-rw-rw-rw-   0        0        0      280 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/attacks.json
+-rw-rw-rw-   0        0        0     2337 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/label_map_num.json
+-rw-rw-rw-   0        0        0      116 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/model_config.json
+-rw-rw-rw-   0        0        0      276 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/test_config.json
+-rw-rw-rw-   0        0        0      281 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/train_config.json
+-rw-rw-rw-   0        0        0      572 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/troj_config.json
+-rw-rw-rw-   0        0        0     4594 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil_test.json
+-rw-rw-rw-   0        0        0     1216 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/trojsdk/examples/nlp_test_main.json
+-rw-rw-rw-   0        0        0    24617 2023-03-28 21:13:25.000000 trojai-sdk-0.2.3.4/trojsdk/examples/s3_small_classification_pt_config.json
+-rw-rw-rw-   0        0        0     1524 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_SMOTETomek_logistic_base.json
+-rw-rw-rw-   0        0        0     3071 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_medical_insurance_config.json
+drwxrwxrwx   0        0        0        0 2023-04-06 13:53:04.705623 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/
+-rw-rw-rw-   0        0        0     1080 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/all_pipe_transform_config.json
+-rw-rw-rw-   0        0        0      435 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/s3_classification_config.json
+-rw-rw-rw-   0        0        0      212 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/s3_starKNN_config.json
+-rw-rw-rw-   0        0        0      381 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/s3_stars_validation_config.json
+-rw-rw-rw-   0        0        0     2006 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/tabular_test_main.json
+-rw-rw-rw-   0        0        0     2406 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/troj_dev_auth.json
+-rw-rw-rw-   0        0        0     1183 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/examples/testing_config.json
+-rw-rw-rw-   0        0        0      989 2023-01-18 17:57:56.000000 trojai-sdk-0.2.3.4/trojsdk/setup.py
+-rw-rw-rw-   0        0        0      745 2023-04-05 17:10:54.000000 trojai-sdk-0.2.3.4/trojsdk/test_sdk.py
```

### Comparing `trojai-sdk-0.2.3.3/.github/workflows/python-app.yml` & `trojai-sdk-0.2.3.4/.github/workflows/python-app.yml`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/.gitlab-ci.yml` & `trojai-sdk-0.2.3.4/.gitlab-ci.yml`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/PKG-INFO` & `trojai-sdk-0.2.3.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trojai-sdk
-Version: 0.2.3.3
+Version: 0.2.3.4
 Summary: TrojAI provides the troj Python convenience package to allow users to integrate TrojAI adversarial protections and robustness metrics seamlessly into their AI development pipelines.
 Home-page: https://troj.ai
 Author: TrojAI
 Author-email: stan.petley@troj.ai
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: License :: OSI Approved :: MIT License
@@ -29,15 +29,15 @@
 job_handler = client_utils.submit_evaluation("path/to/config.json")
 
 # Check the status of the job. Alternatively, use 'kubectl describe pod <trojeval job>' within your terminal, with the context set to the cluster.
 job_handler.check_job_status()
 ```
 `command line`
 ```bash
-trojsdk -c path/to/config.json
+tsdk -c path/to/config.json
 ```
 `python`
 ```python
 # Use the load_json_from_disk function to recursively load JSON data from a file, and its json sub-files, which can be specified by a path string.
 config_dict = data_utils.load_json_from_disk("path/to/config.json")
 # Create the config object and retrieve the dict containing the docker_metadata if it is present within the config dict.
 config, docker_metadata = data_utils.config_from_dict(config_dict)
@@ -52,15 +52,15 @@
 ```python
 from trojsdk.config.nlp import NLPTrojConfig
 from trojsdk.config.tabular import TabularTrojConfig
 from trojsdk.config.vision import VisionTrojConfig
 
 from trojsdk.config.auth import TrojAuthConfig
 ```
-For examples and explinations on configuring your config files, please visit our gitbook.
+For examples and explanations on configuring your config files, please visit our gitbook.
 <br/>[Intro to TrojAI](https://trojai.gitbook.io/trojai/)
 <br/>[NLP](https://trojai.gitbook.io/trojai/nlp/configuring-your-nlp-evaluation)
 <br/>[Tabular](https://trojai.gitbook.io/trojai/tabular/configuring-your-tabular-evaluation)
 
 
 ### Client
 ```python
```

### Comparing `trojai-sdk-0.2.3.3/README.md` & `trojai-sdk-0.2.3.4/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 job_handler = client_utils.submit_evaluation("path/to/config.json")
 
 # Check the status of the job. Alternatively, use 'kubectl describe pod <trojeval job>' within your terminal, with the context set to the cluster.
 job_handler.check_job_status()
 ```
 `command line`
 ```bash
-trojsdk -c path/to/config.json
+tsdk -c path/to/config.json
 ```
 `python`
 ```python
 # Use the load_json_from_disk function to recursively load JSON data from a file, and its json sub-files, which can be specified by a path string.
 config_dict = data_utils.load_json_from_disk("path/to/config.json")
 # Create the config object and retrieve the dict containing the docker_metadata if it is present within the config dict.
 config, docker_metadata = data_utils.config_from_dict(config_dict)
@@ -38,15 +38,15 @@
 ```python
 from trojsdk.config.nlp import NLPTrojConfig
 from trojsdk.config.tabular import TabularTrojConfig
 from trojsdk.config.vision import VisionTrojConfig
 
 from trojsdk.config.auth import TrojAuthConfig
 ```
-For examples and explinations on configuring your config files, please visit our gitbook.
+For examples and explanations on configuring your config files, please visit our gitbook.
 <br/>[Intro to TrojAI](https://trojai.gitbook.io/trojai/)
 <br/>[NLP](https://trojai.gitbook.io/trojai/nlp/configuring-your-nlp-evaluation)
 <br/>[Tabular](https://trojai.gitbook.io/trojai/tabular/configuring-your-tabular-evaluation)
 
 
 ### Client
 ```python
```

### Comparing `trojai-sdk-0.2.3.3/setup.py` & `trojai-sdk-0.2.3.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 
 setup(
     name="trojai-sdk",
-    version="0.2.3.3",
+    version="0.2.3.4",
     packages=find_packages(),
     author="TrojAI",
     author_email="stan.petley@troj.ai",
     description="TrojAI provides the troj Python convenience package to allow users to integrate TrojAI adversarial protections and robustness metrics seamlessly into their AI development pipelines.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://troj.ai",
```

### Comparing `trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/attacks.json` & `trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/all_pipe_transform_config.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/test_proj/credit_dataset/logistic_model/base.json` & `trojai-sdk-0.2.3.4/test_proj/credit_dataset/logistic_model/base.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.89375%*

 * *Differences: {"'k8s_metadata'": "{'k8s_metadata': {delete: ['node_selector']}}", 'delete': "['save_path']"}*

```diff
@@ -6,17 +6,14 @@
         "docker_image_url": "trojai/troj-engine-base-tabular:tabular-dev-latest",
         "docker_secret_name": "trojaicreds",
         "image_pull_policy": "IfNotPresent"
     },
     "k8s_metadata": {
         "k8s_metadata": {
             "container_port": 80,
-            "node_selector": {
-                "dedicated": "robustness-evaluation"
-            },
             "resources": {
                 "limits": {
                     "cpu": "500m",
                     "memory": "2000M"
                 },
                 "requests": {
                     "cpu": "250m",
@@ -31,11 +28,10 @@
                     "value": "robustness-evaluation"
                 }
             ]
         }
     },
     "model": "./test_proj/credit_dataset/logistic_model/model_config.json",
     "run_attacks_from_model_profile": true,
-    "save_path": "./test_proj/credit_dataset/logistic_model/audit_run.json",
     "task_type": "tabular",
     "test_run_name": "test_proj/credit_dataset/logistic_model/"
 }
```

### Comparing `trojai-sdk-0.2.3.3/trojai_sdk.egg-info/PKG-INFO` & `trojai-sdk-0.2.3.4/trojai_sdk.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trojai-sdk
-Version: 0.2.3.3
+Version: 0.2.3.4
 Summary: TrojAI provides the troj Python convenience package to allow users to integrate TrojAI adversarial protections and robustness metrics seamlessly into their AI development pipelines.
 Home-page: https://troj.ai
 Author: TrojAI
 Author-email: stan.petley@troj.ai
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: License :: OSI Approved :: MIT License
@@ -29,15 +29,15 @@
 job_handler = client_utils.submit_evaluation("path/to/config.json")
 
 # Check the status of the job. Alternatively, use 'kubectl describe pod <trojeval job>' within your terminal, with the context set to the cluster.
 job_handler.check_job_status()
 ```
 `command line`
 ```bash
-trojsdk -c path/to/config.json
+tsdk -c path/to/config.json
 ```
 `python`
 ```python
 # Use the load_json_from_disk function to recursively load JSON data from a file, and its json sub-files, which can be specified by a path string.
 config_dict = data_utils.load_json_from_disk("path/to/config.json")
 # Create the config object and retrieve the dict containing the docker_metadata if it is present within the config dict.
 config, docker_metadata = data_utils.config_from_dict(config_dict)
@@ -52,15 +52,15 @@
 ```python
 from trojsdk.config.nlp import NLPTrojConfig
 from trojsdk.config.tabular import TabularTrojConfig
 from trojsdk.config.vision import VisionTrojConfig
 
 from trojsdk.config.auth import TrojAuthConfig
 ```
-For examples and explinations on configuring your config files, please visit our gitbook.
+For examples and explanations on configuring your config files, please visit our gitbook.
 <br/>[Intro to TrojAI](https://trojai.gitbook.io/trojai/)
 <br/>[NLP](https://trojai.gitbook.io/trojai/nlp/configuring-your-nlp-evaluation)
 <br/>[Tabular](https://trojai.gitbook.io/trojai/tabular/configuring-your-tabular-evaluation)
 
 
 ### Client
 ```python
```

### Comparing `trojai-sdk-0.2.3.3/trojai_sdk.egg-info/SOURCES.txt` & `trojai-sdk-0.2.3.4/trojai_sdk.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -41,17 +41,16 @@
 trojsdk/configs/s3_test/troj_dev_auth.json
 trojsdk/core/__init__.py
 trojsdk/core/client_utils.py
 trojsdk/core/data_utils.py
 trojsdk/core/test_experiment_gen.py
 trojsdk/core/troj_error.py
 trojsdk/core/troj_logging.py
-trojsdk/core/ExperimentTools/TrojExperiment.py
-trojsdk/core/ExperimentTools/__init__.py
 trojsdk/core/__pycache__/data_utils.cpython-38.pyc
+trojsdk/core/experiment_tools/__init__.py
 trojsdk/examples/auth_config.json
 trojsdk/examples/auth_config_dev.json
 trojsdk/examples/docker_meta.json
 trojsdk/examples/nlp_phil_test.json
 trojsdk/examples/nlp_test_main.json
 trojsdk/examples/s3_small_classification_pt_config.json
 trojsdk/examples/tabular_SMOTETomek_logistic_base.json
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/client.py` & `trojai-sdk-0.2.3.4/trojsdk/client.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/cmd.py` & `trojai-sdk-0.2.3.4/trojsdk/cmd.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/config/auth.py` & `trojai-sdk-0.2.3.4/trojsdk/config/auth.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/config/base.py` & `trojai-sdk-0.2.3.4/trojsdk/config/base.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/config/nlp.py` & `trojai-sdk-0.2.3.4/trojsdk/config/nlp.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/config/tabular.py` & `trojai-sdk-0.2.3.4/trojsdk/config/tabular.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/config/vision.py` & `trojai-sdk-0.2.3.4/trojsdk/config/vision.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/configs/auth_config.json` & `trojai-sdk-0.2.3.4/trojsdk/configs/auth_config.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/configs/auth_config_dev.json` & `trojai-sdk-0.2.3.4/trojsdk/configs/auth_config_dev.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/all_pipe_transform_config.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/all_pipe_transform_config.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/configs/s3_test/troj_dev_auth.json` & `trojai-sdk-0.2.3.4/trojsdk/configs/s3_test/troj_dev_auth.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/configs/testing_config.json` & `trojai-sdk-0.2.3.4/trojsdk/configs/testing_config.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/core/ExperimentTools/__init__.py` & `trojai-sdk-0.2.3.4/trojsdk/core/experiment_tools/__init__.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,55 +1,47 @@
 import json
 from pathlib import Path
 import os
 import shutil
 import pickle
-import subprocess
-import shlex
+from trojsdk.core.data_utils import minio_upload
+
 
 class TrojExperimenter:
     #could use JSON lines here but meh
     '''
-    Used for making experiments more reproducible within the troj platform. Internal.
+    Used for making experiments more reproducible within the troj platform. 
 
     '''
     def __init__(self, auth_path):
-        #not the same as base troj auth, needs s3 bucket
         '''
         Takes in an authentication json which contains the api endpoint and keys for Troj, a bucket name, and a local
         path to save runs to. i.e
-
-        {
-            "api_endpoint": "http://localhost/api/v1",
-            "auth_keys": {
-                "id_token": token,
-                "refresh_token": token,
-                "api_key": key
-            },
-            "project_name": "SDKTESTPROJECT",
-            "dataset_name": "nlp_run",
-            "secrets": {
-                "AWS_ACCESS_KEY_ID": access,
-                "AWS_SECRET_ACCESS_KEY": secret
-            }
-        }
-
         :param auth_path: path to the authentication json.
-        :param bucket_region: The bucket region used if a bucket needs to be created. ca-central-1 by default.
         '''
         with open(auth_path, "r") as fp:
             data = json.load(fp)
         self.api_endpoint = data["api_endpoint"]
         self.auth_keys = data["auth_keys"]
         self.secrets = data["secrets"]
         self.docker_metadata = None
         self.k8s_metadata = None
         self.attacks = None
         self.test_data_conf = None
         self.train_data_conf = None
+        if "MINIO_ACCESS_KEY" in self.secrets:
+            self.minio_user = self.secrets["MINIO_ACCESS_KEY"]
+        else:
+            self.minio_user = None
+        if "MINIO_SECRET_KEY" in self.secrets:
+            self.minio_pass = self.secrets["MINIO_SECRET_KEY"]
+        else:
+            self.minio_pass = None
+        # Default local dev link
+        self.minio_url = "minioapi.trojaidev"
 
     def create_experiment(self, project_name, dataset_name, model_name, local_save_path = "./",subtask="classification", delete_existing=False):
         '''
         Creates the "experiment" folder locally and on S3
 
         :param project_name: Name of the project for the troj platform
         :param dataset_name: name of the dataset on the troj platform
@@ -64,84 +56,77 @@
         self.subtask = subtask
         self.model_name = model_name
         self.dataset_name = dataset_name
         self.project_name = project_name
         self.experiment_name = "{}/{}/{}/".format(project_name, dataset_name, model_name)
         self.local_exp_path = os.path.join(self.local, self.experiment_name)
         Path(self.local_exp_path).mkdir(parents=True, exist_ok=True, mode=777)
-    # def load_training_data(self, path_to_train_dset, out_file_name, train_dset_config = None, label_column_name = None, classes_dictionary = None, batch_size = 16, shuffle = False):
-    #     pass
-    #     # if train dset config is none, use the values passed to this function to assemble a dictionariy with the values
-    #     if train_dset_config is None:
-    #         # if all the right values are not none
-    #         if label_column_name is not None and classes_dictionary is not None:
-    #             # assemble config
-    #     # else
-    #     else:
-    #         pass
-    #         # load the train dset config
 
-    def log_data(self, new_file_name, data_file_path, label_column, split, classes_dictionary=None, batch_size=16, shuffle=False):
+
+    def log_data(self, data_file_path, label_column, split, classes_dictionary=None, batch_size=16, shuffle=False):
         '''
         Generic function for saving data to the appropriate run file for upload and creating config.
 
-        :param new_file_name: What to call the copy of file specified in path_to_file
-        :param path_to_file: local path to data.
+        :param data_file_path: path to data.
         :param label_column: The name of the label column.
         :param split: the split name, used in naming the dataset in the config.
         :param classes_dictionary: Dictionary of class names
         :param batch_size: Desired batch size in config.
         :param shuffle: Whether or not to shuffle the dataframe.
         :return:
         '''
-        #shutil.copyfile(path_to_file, os.path.join(self.local_exp_path, new_file_name))
-        # self.handler.upload_file(path_to_file, new_file_name, self.experiment_name)
+        if not data_file_path.startswith(("s3://", "gs://", "minio://")):
+            # upload data to minio, local data file
+            upload_res = minio_upload(data_file_path, upload_url = self.minio_url, project = self.project_name, dataset = self.dataset_name, model = self.model_name, minio_user=self.minio_user, minio_pass=self.minio_pass)
+            data_file_path = upload_res
         dloader_config = {"batch_size": batch_size, "shuffle":shuffle}
         data_config = {"name":self.dataset_name+"_"+split, "path_to_data":data_file_path,
                        "data_loader_config":dloader_config, "label_column":label_column}
         if classes_dictionary is not None:
             print("No classes dictionary supplied, loading from data config")
             try:
                 data_config["classes_dictionary"] = classes_dictionary
             except Exception as e:
                 print("No classes dictionary in data config")
                 raise(e)
+            
+
         return data_config
 
-    def log_training_data(self, out_file_name, path_to_dset_file, label_column, classes_dictionary=None, batch_size=16, shuffle=False):
+    def log_training_data(self, path_to_dset_file, label_column, classes_dictionary=None, batch_size=16, shuffle=False):
         '''
         Logs the training data and automatically sets the config.
 
         :param new_file_name:
         :param path_to_file:
         :param label_column:
         :param classes_dictionary:
         :param batch_size:
         :param shuffle:
         :return:
         '''
-        self.train_data_conf = self.log_data(out_file_name, path_to_dset_file, label_column,
+        self.train_data_conf = self.log_data(path_to_dset_file, label_column,
                                              classes_dictionary=classes_dictionary, batch_size=batch_size, shuffle=shuffle, split="train")
         save_path = os.path.join(self.local_exp_path, "train_config.json")
         with open(save_path, "w+") as fp:
             json.dump(self.train_data_conf, fp)
 
-    def log_testing_data(self, new_file_name, path_to_dset_file, label_column, classes_dictionary=None, batch_size=16, shuffle=False):
+    def log_testing_data(self, path_to_dset_file, label_column, classes_dictionary=None, batch_size=16, shuffle=False):
         '''
         logs testing data and automatically sets the config.
 
         :param new_file_name:
         :param path_to_file:
         :param label_column:
         :param classes_dictionary:
         :param batch_size:
         :param shuffle:
         :return:
         '''
-        self.test_data_conf = self.log_data(new_file_name, path_to_dset_file, label_column,
+        self.test_data_conf = self.log_data(path_to_dset_file, label_column,
                                              classes_dictionary=classes_dictionary, batch_size=batch_size, shuffle=shuffle, split="test")
         save_path = os.path.join(self.local_exp_path, "test_config.json")
         with open(save_path, "w+") as fp:
             json.dump(self.test_data_conf, fp)
 
 
     def log_model(self, model, model_wrapper_file, **model_kwargs):
@@ -149,24 +134,28 @@
         Saves model and makes the model config.
 
         :param model: Either a picklable model, or a path to a model file.
         :param model_wrapper_file: The path to the model wrapper file.
         :param model_kwargs: Any model keyword arguments
         :return: Saves model, and makes model json.
         '''
-        if "s3" not in model_wrapper_file and "mino" not in model_wrapper_file:
-            shutil.copyfile(model_wrapper_file, os.path.join(self.local_exp_path,"model_wrapper.py"))
-            if type(model)==str:
-                shutil.copyfile(model, os.path.join(self.local_exp_path, "{}.pkl".format(self.model_name)))
-            else:
-                pickle.dump(model, open(os.path.join(self.local_exp_path,"{}.pkl".format(self.model_name)), "wb"))
-            self.model_config = {"name":self.model_name, "path_to_model_file":"./model_wrapper.py", "model_args_dict":{**model_kwargs}}
-        else:
-            self.model_config = {"name":self.model_name, "path_to_model_file":model_wrapper_file, "model_args_dict":{**model_kwargs}}
+        model_file_res = model_wrapper_file
+        model_res = model
+
+        # if model not hosted on s3 or minio, upload to minio
+        if not model_wrapper_file.startswith(("s3://", "gs://", "minio://")):
+            model_file_res = minio_upload(model_wrapper_file, upload_url = self.minio_url, project = self.project_name, dataset = self.dataset_name, model = self.model_name, minio_user=self.minio_user, minio_pass=self.minio_pass)
+            if not model.startswith(("s3://", "gs://", "minio://")):
+                model_res = minio_upload(model, upload_url = self.minio_url, project = self.project_name, dataset = self.dataset_name, model = self.model_name, minio_user=self.minio_user, minio_pass=self.minio_pass)
+
+
+        self.model_config = {"name":self.model_name, "path_to_model_file":model_file_res, "model_args_dict":{**model_kwargs, "model_file": model_res}}
+
         save_path = os.path.join(self.local_exp_path, "model_config.json")
+
         with open(save_path, "w+") as fp:
             json.dump(self.model_config, fp)
 
 
 
     def log_docker_metadata(self, docker_image_url, docker_secret_name, image_pull_policy):
         docker_meta = {
@@ -207,47 +196,79 @@
             shutil.copyfile(attacks, os.path.join(self.local_exp_path, "attacks.json"))
         elif type(attacks) == dict:
             save_path = os.path.join(self.local_exp_path, "attacks.json")
             self.attacks = True
             with open(save_path, "w+") as fp:
                 json.dump(attacks, fp)
 
+    def log_checks(self, checks):
+        if type(checks) == str:
+            if checks.split(".")[-1] == "json":
+                self._set_checks_from_path(checks)
+            else:
+                self.checks_list.append(checks)
+        elif type(checks) == dict:
+            self.checks_list.append(checks)
+        elif type(checks) == list:
+            for i in checks:
+                self.checks_list.append(i)
+
+    def reset(self):
+        '''
+        Resets the internal values.
+        :return:
+        '''
+        self.base = {}
+        self.attack_list = []
+        self.checks_list = []
+        self.test_data_conf = None
+        self.train_data_conf = None
+        self.custom_checks = None
+        self.custom_eval = None
+        self.custom_eval_kwargs = None
+
     def create_auth(self, project_name=None, dataset_name=None):
         auth = {}
         auth["api_endpoint"] = self.api_endpoint
         auth["auth_keys"] = self.auth_keys
         if project_name==None:
             auth["project_name"] = self.project_name
             auth["dataset_name"] = self.dataset_name
         else:
             auth["project_name"] = project_name
             auth["dataset_name"] = dataset_name
         return auth
 
-    def construct_base_config(self, audit=True, run_attacks_from_profile=True):
+    def construct_base_config(self, audit=True, run_attacks_from_profile=True, task_type = None):
         base_conf = {}
         base_conf["test_run_name"] = self.experiment_name
-        base_conf["task_type"] = "tabular"
+        base_conf["task_type"] = task_type
         base_conf["audit"] = audit
         base_conf["run_attacks_from_model_profile"] = run_attacks_from_profile
         if self.test_data_conf is not None:
+            '''
+            if data file path is local, upload to minio, return the path to the minio upload as well to replace in config
+            '''
             base_conf["dataset"] = self.local_exp_path+"test_config.json"
         if self.train_data_conf is not None:
+            '''
+            if data file path is local, upload to minio, return the path to the minio upload as well to replace in config
+            '''
             base_conf["train_dataset"] = self.local_exp_path+"train_config.json"
         base_conf["model"] = self.local_exp_path+"model_config.json"
-        base_conf["save_path"] = self.local_exp_path+"audit_run.json"
         auth_dict = self.create_auth()
         save_path = os.path.join(self.local_exp_path, "auth.json")
         with open(save_path, "w+") as fp:
             json.dump(auth_dict, fp)
         base_conf["auth_config"] = self.local_exp_path+"auth.json"
         base_save_path = os.path.join(self.local_exp_path, "base.json")
         base_conf["docker_metadata"] = self.docker_metadata["docker_metadata"]
         if self.k8s_metadata is not None:
             base_conf["k8s_metadata"]  = self.k8s_metadata
+
         with open(base_save_path, "w+") as fp:
             json.dump(base_conf, fp)
         print("configs constructed!")
 
     def upload_experiment(self, delete_after_upload=False):
         # change this to send with tsdk to auth config api endpoint
         self.handler.upload_folder_contents(self.local_exp_path, self.experiment_name)
@@ -258,27 +279,34 @@
         auth_path = os.path.join(local_path, "auth.json")
         with open(auth_path, "r") as fp:
             current_auth = json.load(fp)
             current_auth["auth_keys"] = self.auth_keys
         with open(auth_path, "w+") as fp:
             json.dump(current_auth, fp)
 
+    
+    def _set_attacks_from_path(self, path):
+        attack_dict = json.load(path)
+        self.attack_list = self.attack_list + attack_dict["attacks"]
+
+    def _set_checks_from_path(self, path):
+        checks_dict = json.load(path)
+        self.checks_list = self.checks_list + checks_dict["integrity_checks"]
+
+
+    def set_custom_eval(self, file_path, args_dict=None):
+        shutil.copyfile(file_path, os.path.join(self.local_exp_path, "custom_attacks.py"))
+        self.custom_eval = "./custom_attacks.py"
+        self.custom_eval_kwargs = args_dict
+
+    def set_custom_checks(self, file_path):
+        shutil.copyfile(file_path, os.path.join(self.local_exp_path, "custom_checks.py"))
+        self.custom_checks = "./custom_checks.py"
 
 
-
-
-
-    def set_custom_eval(self):
-        #TODO
-        pass
-
-    def set_custom_checks(self):
-        #TODO
-        pass
-
     def set_integrity_checks(self):
         #TODO
         pass
 
     def run_troj_evaluation(self, project, dataset, model, no_ssl = False):
         import os
         from trojsdk.core import client_utils
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/core/__pycache__/data_utils.cpython-38.pyc` & `trojai-sdk-0.2.3.4/trojsdk/core/__pycache__/data_utils.cpython-38.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.8, timestamp-based, .py timestamp: Wed Jan 18 17:57:56 2023 UTC, .py size: 4613 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 12% similar despite different names*

```diff
@@ -1,171 +1,213 @@
-00000000: 550d 0d0a 0000 0000 2433 c863 0512 0000  U.......$3.c....
+00000000: 550d 0d0a 0000 0000 b8c5 2e64 1915 0000  U..........d....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
-00000020: 0005 0000 0040 0000 0073 5800 0000 6400  .....@...sX...d.
+00000020: 0007 0000 0040 0000 0073 7600 0000 6400  .....@...sv...d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6401 6c02 5a02 6400 6402 6c03 6d04 5a04  d.l.Z.d.d.l.m.Z.
 00000050: 0100 6400 6403 6c05 6d06 5a06 0100 6404  ..d.d.l.m.Z...d.
-00000060: 6405 6702 5a07 6406 6407 8400 5a08 640c  d.g.Z.d.d...Z.d.
+00000060: 6405 6702 5a07 6406 6407 8400 5a08 6414  d.g.Z.d.d...Z.d.
 00000070: 6504 6509 650a 6409 9c03 640a 640b 8405  e.e.e.d...d.d...
-00000080: 5a0b 6401 5300 290d e900 0000 004e 2901  Z.d.S.)......N).
-00000090: da04 5061 7468 2901 da0d 5472 6f6a 4a53  ..Path)...TrojJS
-000000a0: 4f4e 4572 726f 725a 1370 6174 685f 746f  ONErrorZ.path_to
-000000b0: 5f61 6e6e 6f74 6174 696f 6e73 da09 7361  _annotations..sa
-000000c0: 7665 5f70 6174 6863 0100 0000 0000 0000  ve_pathc........
-000000d0: 0000 0000 0900 0000 0500 0000 4300 0000  ............C...
-000000e0: 73d2 0000 0064 0164 006c 007d 0167 007d  s....d.d.l.}.g.}
-000000f0: 027c 0044 005d bc7d 037c 007c 0319 007d  .|.D.].}.|.|...}
-00000100: 047c 0364 026b 0272 2671 1074 017c 0483  .|.d.k.r&q.t.|..
-00000110: 0174 026b 0872 627c 0364 036b 0272 3c71  .t.k.rb|.d.k.r<q
-00000120: 1074 037c 0483 017d 057c 0567 006b 0372  .t.|...}.|.g.k.r
-00000130: cc7c 0544 005d 0e7d 067c 02a0 047c 06a1  .|.D.].}.|...|..
-00000140: 0101 0071 5071 1074 017c 0483 0174 056b  ...qPq.t.|...t.k
-00000150: 0872 107c 04a0 0664 04a1 0172 7a71 107c  .r.|...d...rzq.|
-00000160: 04a0 0764 05a1 017d 077c 0764 0619 0064  ...d...}.|.d...d
-00000170: 076b 0273 a87c 0764 0619 0064 086b 0273  .k.s.|.d...d.k.s
-00000180: a87c 0764 0619 0064 096b 0272 107c 0364  .|.d...d.k.r.|.d
-00000190: 0a6b 0272 b271 107c 016a 08a0 097c 04a1  .k.r.q.|.j...|..
-000001a0: 017d 087c 0873 107c 02a0 047c 04a1 0101  .}.|.s.|...|....
-000001b0: 0071 107c 0253 0029 0b4e 7201 0000 00da  .q.|.S.).Nr.....
-000001c0: 1263 6c61 7373 6573 5f64 6963 7469 6f6e  .classes_diction
-000001d0: 6172 79da 0961 7574 685f 6b65 7973 2903  ary..auth_keys).
-000001e0: 7a05 7333 3a2f 2f7a 0567 733a 2f2f 7a08  z.s3://z.gs://z.
-000001f0: 6d69 6e69 6f3a 2f2f da01 2ee9 ffff ffff  minio://........
-00000200: da04 6a73 6f6e 5a03 6373 76da 0270 7972  ..jsonZ.csv..pyr
-00000210: 0400 0000 290a da02 6f73 da04 7479 7065  ....)...os..type
-00000220: da04 6469 6374 da0a 7465 7374 5f70 6174  ..dict..test_pat
-00000230: 6873 da06 6170 7065 6e64 da03 7374 72da  hs..append..str.
-00000240: 0a73 7461 7274 7377 6974 68da 0573 706c  .startswith..spl
-00000250: 6974 da04 7061 7468 da06 6578 6973 7473  it..path..exists
-00000260: 2909 5a0a 696e 7075 745f 6469 6374 720b  ).Z.input_dictr.
-00000270: 0000 00da 0d69 6e76 616c 6964 5f70 6174  .....invalid_pat
-00000280: 6873 da03 6b65 79da 0576 616c 7565 5a09  hs..key..valueZ.
-00000290: 6469 6374 5f64 6174 615a 0864 6963 745f  dict_dataZ.dict_
-000002a0: 7661 6c5a 0973 706c 6974 5f73 7472 5a0a  valZ.split_strZ.
-000002b0: 7061 7468 5f76 616c 6964 a900 7218 0000  path_valid..r...
-000002c0: 00fa 5563 3a5c 7573 6572 735c 6261 7272  ..Uc:\users\barr
-000002d0: 6965 2074 6f6d 696c 736f 6e5c 646f 6375  ie tomilson\docu
-000002e0: 6d65 6e74 735c 6769 7468 7562 2028 3229  ments\github (2)
-000002f0: 5c73 646b 5c74 726f 6a2d 7364 6b5c 7472  \sdk\troj-sdk\tr
-00000300: 6f6a 7364 6b5c 636f 7265 5c64 6174 615f  ojsdk\core\data_
-00000310: 7574 696c 732e 7079 720e 0000 000c 0000  utils.pyr.......
-00000320: 0073 3a00 0000 0001 0803 0402 0802 0801  .s:.............
-00000330: 0801 0201 0c01 0801 0201 0801 0801 0801  ................
-00000340: 0e01 0c01 0a01 0201 0a03 0aff 0202 0afe  ................
-00000350: 0203 0afd 0205 0801 0202 0c02 0401 0c02  ................
-00000360: 720e 0000 0054 2903 da09 6a73 6f6e 5f70  r....T)...json_p
-00000370: 6174 68da 0973 7562 5f6a 736f 6e73 da06  ath..sub_jsons..
-00000380: 7265 7475 726e 6302 0000 0000 0000 0000  returnc.........
-00000390: 0000 0008 0000 000a 0000 0043 0000 0073  ...........C...s
-000003a0: 4001 0000 7acc 7c00 6a00 6401 6402 8d01  @...z.|.j.d.d...
-000003b0: 8fb6 7d02 7401 a002 7c02 a101 7d03 7c01  ..}.t...|...}.|.
-000003c0: 6403 6b08 72c0 7c03 a003 a100 a004 a100  d.k.r.|.........
-000003d0: 4400 5d90 5c02 7d04 7d05 7c04 7405 6b06  D.].\.}.}.|.t.k.
-000003e0: 7240 712e 7406 7c05 8301 7407 6b02 722e  r@q.t.|...t.k.r.
-000003f0: 7c05 6404 6405 8502 1900 6406 6b02 722e  |.d.d.....d.k.r.
-00000400: 7408 6a09 a00a 7c05 a101 722e 740b 740c  t.j...|...r.t.t.
-00000410: 7c05 8301 8301 7c03 7c04 3c00 7c04 6407  |.....|.|.<.|.d.
-00000420: 6b02 72be 740d 7c03 7c04 1900 740e 8302  k.r.t.|.|...t...
-00000430: 72be 740f 7c03 7c04 1900 8301 6408 6b02  r.t.|.|.....d.k.
-00000440: 72be 6407 7c03 7c04 1900 6b06 72be 7c03  r.d.|.|...k.r.|.
-00000450: 7c04 1900 6407 1900 7c03 7c04 3c00 712e  |...d...|.|.<.q.
-00000460: 712e 712e 5700 3500 5100 5200 5800 5700  q.q.W.5.Q.R.X.W.
-00000470: 6e58 0400 7410 6b0a 9001 7224 0100 7d06  nX..t.k...r$..}.
-00000480: 0100 7a38 7411 7c06 6409 8302 72f2 7c06  ..z8t.|.d...r.|.
-00000490: 6a12 7d07 6e1a 640a 7413 7c06 8301 9b00  j.}.n.d.t.|.....
-000004a0: 640b 7407 7c00 8301 9b00 640c 9d05 7d07  d.t.|.....d...}.
-000004b0: 7414 7c07 8301 8201 5700 3500 6405 7d06  t.|.....W.5.d.}.
-000004c0: 7e06 5800 5900 6e02 5800 7c03 9001 733c  ~.X.Y.n.X.|...s<
-000004d0: 7415 6a16 640d 7417 640e 640f 8d03 0100  t.j.d.t.d.d.....
-000004e0: 7c03 5300 2910 61ae 0200 000a 2020 2020  |.S.).a.....    
-000004f0: 4769 7665 6e20 6120 7061 7468 2074 6f20  Given a path to 
-00000500: 7468 6520 4a53 4f4e 2066 696c 6520 696e  the JSON file in
-00000510: 2070 6174 686c 6962 2e50 6174 6820 666f   pathlib.Path fo
-00000520: 726d 6174 2c20 2872 6563 7572 7369 7665  rmat, (recursive
-00000530: 6c79 2920 7265 6164 2061 6e64 2072 6574  ly) read and ret
-00000540: 7572 6e20 7468 650a 2020 2020 6469 6374  urn the.    dict
-00000550: 696f 6e61 7279 2073 746f 7265 6420 696e  ionary stored in
-00000560: 2074 6865 2066 696c 652e 0a0a 2020 2020   the file...    
-00000570: 4e6f 7465 2074 6861 7420 7768 656e 2073  Note that when s
-00000580: 7562 5f6a 736f 6e73 203d 3d20 5472 7565  ub_jsons == True
-00000590: 2061 6e64 2061 6e20 6578 636c 7564 6564   and an excluded
-000005a0: 206e 616d 6520 6973 2065 6e63 6f75 6e74   name is encount
-000005b0: 6572 6564 2c20 7468 6520 636f 6e74 656e  ered, the conten
-000005c0: 7473 206f 6620 7468 6520 4a53 4f4e 2066  ts of the JSON f
-000005d0: 696c 6520 7769 6c6c 206e 6f74 2062 650a  ile will not be.
-000005e0: 2020 2020 6c6f 6164 6564 2061 6e64 2074      loaded and t
-000005f0: 6865 2070 6174 6820 6974 7365 6c66 2077  he path itself w
-00000600: 696c 6c20 6265 2073 746f 7265 642e 0a0a  ill be stored...
-00000610: 2020 2020 3a70 6172 616d 206a 736f 6e5f      :param json_
-00000620: 7061 7468 3a20 7061 7468 2074 6f20 7468  path: path to th
-00000630: 6520 4a53 4f4e 2066 696c 6520 746f 206c  e JSON file to l
-00000640: 6f61 6420 6469 6374 696f 6e61 7279 2066  oad dictionary f
-00000650: 726f 6d20 2870 6174 686c 6962 2e50 6174  rom (pathlib.Pat
-00000660: 6829 0a20 2020 203a 7061 7261 6d20 7375  h).    :param su
-00000670: 625f 6a73 6f6e 733a 2069 6620 5472 7565  b_jsons: if True
-00000680: 2c20 7768 656e 2070 6174 6820 746f 2061  , when path to a
-00000690: 6e6f 7468 6572 2065 7869 7374 696e 6720  nother existing 
-000006a0: 4a53 4f4e 2066 696c 6520 6973 2065 6e63  JSON file is enc
-000006b0: 6f75 6e74 6572 6564 2c20 7468 6174 204a  ountered, that J
-000006c0: 534f 4e20 6669 6c65 2077 696c 6c20 6265  SON file will be
-000006d0: 206c 6f61 6465 640a 2020 2020 2020 2020   loaded.        
-000006e0: 2020 2020 2020 2020 2020 2020 7265 6375              recu
-000006f0: 7273 6976 656c 7920 696e 7374 6561 6420  rsively instead 
-00000700: 6f66 2073 6176 696e 6720 7468 6520 7061  of saving the pa
-00000710: 7468 2028 6e6f 7420 6170 706c 6965 6420  th (not applied 
-00000720: 746f 206e 616d 6573 2069 6e20 4a53 4f4e  to names in JSON
-00000730: 5f4c 4f41 4445 525f 4558 434c 5544 4544  _LOADER_EXCLUDED
-00000740: 5f4e 414d 4553 2928 626f 6f6c 6561 6e29  _NAMES)(boolean)
-00000750: 0a20 2020 203a 7265 7475 726e 3a20 6469  .    :return: di
-00000760: 6374 696f 6e61 7279 2063 6f6e 7374 7275  ctionary constru
-00000770: 6374 6564 2066 726f 6d20 7468 6520 6769  cted from the gi
-00000780: 7665 6e20 4a53 4f4e 2066 696c 6520 2864  ven JSON file (d
-00000790: 6963 7429 0a20 2020 20da 0172 2901 da04  ict).    ..r)...
-000007a0: 6d6f 6465 54e9 fbff ffff 4e7a 052e 6a73  modeT.....Nz..js
-000007b0: 6f6e da07 6174 7461 636b 73e9 0100 0000  on..attacks.....
-000007c0: da07 6d65 7373 6167 657a 110a 0a47 6f74  ..messagez...Got
-000007d0: 2074 6865 2065 7272 6f72 3a20 7a22 0a43   the error: z".C
-000007e0: 6f75 6c64 206e 6f74 206c 6f61 6420 636f  ould not load co
-000007f0: 6e74 656e 7473 206f 6620 6672 6f6d 3a20  ntents of from: 
-00000800: 7a5f 0a4d 616b 6520 7375 7265 2074 6861  z_.Make sure tha
-00000810: 7420 7468 6520 7061 7468 2074 6f20 796f  t the path to yo
-00000820: 7572 204a 534f 4e20 6669 6c65 2069 7320  ur JSON file is 
-00000830: 7661 6c69 6420 616e 6420 696e 7369 6465  valid and inside
-00000840: 2079 6f75 7220 4a53 4f4e 2069 7320 6120   your JSON is a 
-00000850: 7661 6c69 6420 6469 6374 696f 6e61 7279  valid dictionary
-00000860: 2e7a 414c 6f61 6465 6420 6469 6374 696f  .zALoaded dictio
-00000870: 6e61 7279 2066 726f 6d20 4a53 4f4e 2073  nary from JSON s
-00000880: 7563 6365 7373 6675 6c6c 7920 6275 7420  uccessfully but 
-00000890: 6469 6374 696f 6e61 7279 2069 7320 656d  dictionary is em
-000008a0: 7074 792e e902 0000 0029 01da 0a73 7461  pty......)...sta
-000008b0: 636b 6c65 7665 6c29 18da 046f 7065 6e72  cklevel)...openr
-000008c0: 0900 0000 da04 6c6f 6164 da04 636f 7079  ......load..copy
-000008d0: da05 6974 656d 73da 1a4a 534f 4e5f 4c4f  ..items..JSON_LO
-000008e0: 4144 4552 5f45 5843 4c55 4445 445f 4e41  ADER_EXCLUDED_NA
-000008f0: 4d45 5372 0c00 0000 7210 0000 0072 0b00  MESr....r....r..
-00000900: 0000 7213 0000 00da 0669 7366 696c 65da  ..r......isfile.
-00000910: 136c 6f61 645f 6a73 6f6e 5f66 726f 6d5f  .load_json_from_
-00000920: 6469 736b 7202 0000 00da 0a69 7369 6e73  diskr......isins
-00000930: 7461 6e63 6572 0d00 0000 da03 6c65 6eda  tancer......len.
-00000940: 0945 7863 6570 7469 6f6e da07 6861 7361  .Exception..hasa
-00000950: 7474 7272 2200 0000 da04 7265 7072 7203  ttrr".....reprr.
-00000960: 0000 00da 0877 6172 6e69 6e67 73da 0477  .....warnings..w
-00000970: 6172 6eda 0e52 756e 7469 6d65 5761 726e  arn..RuntimeWarn
-00000980: 696e 6729 0872 1a00 0000 721b 0000 00da  ing).r....r.....
-00000990: 0166 da09 6a73 6f6e 5f64 6174 6172 1600  .f..json_datar..
-000009a0: 0000 7217 0000 00da 0365 7272 7222 0000  ..r......errr"..
-000009b0: 0072 1800 0000 7218 0000 0072 1900 0000  .r....r....r....
-000009c0: 722b 0000 0033 0000 0073 4800 0000 000f  r+...3...sH.....
-000009d0: 0201 0e01 0a02 0801 1402 0802 0203 0aff  ................
-000009e0: 0202 0efe 0203 0afd 0207 1003 0802 0cff  ................
-000009f0: 0202 0efe 0203 0afd 0205 1203 1201 1201  ................
-00000a00: 0a01 0803 18ff 0208 1a02 0601 0401 0201  ................
-00000a10: 0201 02fd 0606 722b 0000 0029 0154 290c  ......r+...).T).
-00000a20: 720b 0000 0072 0900 0000 7231 0000 00da  r....r....r1....
-00000a30: 0770 6174 686c 6962 7202 0000 00da 1774  .pathlibr......t
-00000a40: 726f 6a73 646b 2e63 6f72 652e 7472 6f6a  rojsdk.core.troj
-00000a50: 5f65 7272 6f72 7203 0000 0072 2900 0000  _errorr....r)...
-00000a60: 720e 0000 00da 0462 6f6f 6c72 0d00 0000  r......boolr....
-00000a70: 722b 0000 0072 1800 0000 7218 0000 0072  r+...r....r....r
-00000a80: 1800 0000 7219 0000 00da 083c 6d6f 6475  ....r......<modu
-00000a90: 6c65 3e01 0000 0073 0e00 0000 0801 0801  le>....s........
-00000aa0: 0801 0c01 0c04 0803 0827                 .........'
+00000080: 5a0b 6400 640c 6c0c 6d0d 5a0d 0100 6400  Z.d.d.l.m.Z...d.
+00000090: 6401 6c00 5a00 6415 6412 6413 8401 5a0e  d.l.Z.d.d.d...Z.
+000000a0: 6401 5300 2916 e900 0000 004e 2901 da04  d.S.)......N)...
+000000b0: 5061 7468 2901 da0d 5472 6f6a 4a53 4f4e  Path)...TrojJSON
+000000c0: 4572 726f 725a 1370 6174 685f 746f 5f61  ErrorZ.path_to_a
+000000d0: 6e6e 6f74 6174 696f 6e73 da09 7361 7665  nnotations..save
+000000e0: 5f70 6174 6863 0100 0000 0000 0000 0000  _pathc..........
+000000f0: 0000 0900 0000 0500 0000 4300 0000 73d2  ..........C...s.
+00000100: 0000 0064 0164 006c 007d 0167 007d 027c  ...d.d.l.}.g.}.|
+00000110: 0044 005d bc7d 037c 007c 0319 007d 047c  .D.].}.|.|...}.|
+00000120: 0364 026b 0272 2671 1074 017c 0483 0174  .d.k.r&q.t.|...t
+00000130: 026b 0872 627c 0364 036b 0272 3c71 1074  .k.rb|.d.k.r<q.t
+00000140: 037c 0483 017d 057c 0567 006b 0372 cc7c  .|...}.|.g.k.r.|
+00000150: 0544 005d 0e7d 067c 02a0 047c 06a1 0101  .D.].}.|...|....
+00000160: 0071 5071 1074 017c 0483 0174 056b 0872  .qPq.t.|...t.k.r
+00000170: 107c 04a0 0664 04a1 0172 7a71 107c 04a0  .|...d...rzq.|..
+00000180: 0764 05a1 017d 077c 0764 0619 0064 076b  .d...}.|.d...d.k
+00000190: 0273 a87c 0764 0619 0064 086b 0273 a87c  .s.|.d...d.k.s.|
+000001a0: 0764 0619 0064 096b 0272 107c 0364 0a6b  .d...d.k.r.|.d.k
+000001b0: 0272 b271 107c 016a 08a0 097c 04a1 017d  .r.q.|.j...|...}
+000001c0: 087c 0873 107c 02a0 047c 04a1 0101 0071  .|.s.|...|.....q
+000001d0: 107c 0253 0029 0b4e 7201 0000 005a 1263  .|.S.).Nr....Z.c
+000001e0: 6c61 7373 6573 5f64 6963 7469 6f6e 6172  lasses_dictionar
+000001f0: 795a 0961 7574 685f 6b65 7973 2903 7a05  yZ.auth_keys).z.
+00000200: 7333 3a2f 2f7a 0567 733a 2f2f fa08 6d69  s3://z.gs://..mi
+00000210: 6e69 6f3a 2f2f da01 2ee9 ffff ffff da04  nio://..........
+00000220: 6a73 6f6e da03 6373 76da 0270 7972 0400  json..csv..pyr..
+00000230: 0000 290a da02 6f73 da04 7479 7065 da04  ..)...os..type..
+00000240: 6469 6374 da0a 7465 7374 5f70 6174 6873  dict..test_paths
+00000250: da06 6170 7065 6e64 da03 7374 72da 0a73  ..append..str..s
+00000260: 7461 7274 7377 6974 68da 0573 706c 6974  tartswith..split
+00000270: da04 7061 7468 da06 6578 6973 7473 2909  ..path..exists).
+00000280: 5a0a 696e 7075 745f 6469 6374 720b 0000  Z.input_dictr...
+00000290: 005a 0d69 6e76 616c 6964 5f70 6174 6873  .Z.invalid_paths
+000002a0: da03 6b65 79da 0576 616c 7565 5a09 6469  ..key..valueZ.di
+000002b0: 6374 5f64 6174 615a 0864 6963 745f 7661  ct_dataZ.dict_va
+000002c0: 6c5a 0973 706c 6974 5f73 7472 5a0a 7061  lZ.split_strZ.pa
+000002d0: 7468 5f76 616c 6964 a900 7217 0000 00fa  th_valid..r.....
+000002e0: 5543 3a5c 5573 6572 735c 4261 7272 6965  UC:\Users\Barrie
+000002f0: 2054 6f6d 696c 736f 6e5c 446f 6375 6d65   Tomilson\Docume
+00000300: 6e74 735c 6769 7468 7562 2028 3229 5c73  nts\github (2)\s
+00000310: 646b 5c74 726f 6a2d 7364 6b5c 7472 6f6a  dk\troj-sdk\troj
+00000320: 7364 6b5c 636f 7265 5c64 6174 615f 7574  sdk\core\data_ut
+00000330: 696c 732e 7079 720e 0000 000c 0000 0073  ils.pyr........s
+00000340: 3a00 0000 0001 0803 0402 0802 0801 0801  :...............
+00000350: 0201 0c01 0801 0201 0801 0801 0801 0e01  ................
+00000360: 0c01 0a01 0201 0a03 0aff 0202 0afe 0203  ................
+00000370: 0afd 0205 0801 0202 0c02 0401 0c02 720e  ..............r.
+00000380: 0000 0054 2903 da09 6a73 6f6e 5f70 6174  ...T)...json_pat
+00000390: 68da 0973 7562 5f6a 736f 6e73 da06 7265  h..sub_jsons..re
+000003a0: 7475 726e 6302 0000 0000 0000 0000 0000  turnc...........
+000003b0: 0008 0000 000a 0000 0043 0000 0073 4001  .........C...s@.
+000003c0: 0000 7acc 7c00 6a00 6401 6402 8d01 8fb6  ..z.|.j.d.d.....
+000003d0: 7d02 7401 a002 7c02 a101 7d03 7c01 6403  }.t...|...}.|.d.
+000003e0: 6b08 72c0 7c03 a003 a100 a004 a100 4400  k.r.|.........D.
+000003f0: 5d90 5c02 7d04 7d05 7c04 7405 6b06 7240  ].\.}.}.|.t.k.r@
+00000400: 712e 7406 7c05 8301 7407 6b02 722e 7c05  q.t.|...t.k.r.|.
+00000410: 6404 6405 8502 1900 6406 6b02 722e 7408  d.d.....d.k.r.t.
+00000420: 6a09 a00a 7c05 a101 722e 740b 740c 7c05  j...|...r.t.t.|.
+00000430: 8301 8301 7c03 7c04 3c00 7c04 6407 6b02  ....|.|.<.|.d.k.
+00000440: 72be 740d 7c03 7c04 1900 740e 8302 72be  r.t.|.|...t...r.
+00000450: 740f 7c03 7c04 1900 8301 6408 6b02 72be  t.|.|.....d.k.r.
+00000460: 6407 7c03 7c04 1900 6b06 72be 7c03 7c04  d.|.|...k.r.|.|.
+00000470: 1900 6407 1900 7c03 7c04 3c00 712e 712e  ..d...|.|.<.q.q.
+00000480: 712e 5700 3500 5100 5200 5800 5700 6e58  q.W.5.Q.R.X.W.nX
+00000490: 0400 7410 6b0a 9001 7224 0100 7d06 0100  ..t.k...r$..}...
+000004a0: 7a38 7411 7c06 6409 8302 72f2 7c06 6a12  z8t.|.d...r.|.j.
+000004b0: 7d07 6e1a 640a 7413 7c06 8301 9b00 640b  }.n.d.t.|.....d.
+000004c0: 7407 7c00 8301 9b00 640c 9d05 7d07 7414  t.|.....d...}.t.
+000004d0: 7c07 8301 8201 5700 3500 6405 7d06 7e06  |.....W.5.d.}.~.
+000004e0: 5800 5900 6e02 5800 7c03 9001 733c 7415  X.Y.n.X.|...s<t.
+000004f0: 6a16 640d 7417 640e 640f 8d03 0100 7c03  j.d.t.d.d.....|.
+00000500: 5300 2910 61ae 0200 000a 2020 2020 4769  S.).a.....    Gi
+00000510: 7665 6e20 6120 7061 7468 2074 6f20 7468  ven a path to th
+00000520: 6520 4a53 4f4e 2066 696c 6520 696e 2070  e JSON file in p
+00000530: 6174 686c 6962 2e50 6174 6820 666f 726d  athlib.Path form
+00000540: 6174 2c20 2872 6563 7572 7369 7665 6c79  at, (recursively
+00000550: 2920 7265 6164 2061 6e64 2072 6574 7572  ) read and retur
+00000560: 6e20 7468 650a 2020 2020 6469 6374 696f  n the.    dictio
+00000570: 6e61 7279 2073 746f 7265 6420 696e 2074  nary stored in t
+00000580: 6865 2066 696c 652e 0a0a 2020 2020 4e6f  he file...    No
+00000590: 7465 2074 6861 7420 7768 656e 2073 7562  te that when sub
+000005a0: 5f6a 736f 6e73 203d 3d20 5472 7565 2061  _jsons == True a
+000005b0: 6e64 2061 6e20 6578 636c 7564 6564 206e  nd an excluded n
+000005c0: 616d 6520 6973 2065 6e63 6f75 6e74 6572  ame is encounter
+000005d0: 6564 2c20 7468 6520 636f 6e74 656e 7473  ed, the contents
+000005e0: 206f 6620 7468 6520 4a53 4f4e 2066 696c   of the JSON fil
+000005f0: 6520 7769 6c6c 206e 6f74 2062 650a 2020  e will not be.  
+00000600: 2020 6c6f 6164 6564 2061 6e64 2074 6865    loaded and the
+00000610: 2070 6174 6820 6974 7365 6c66 2077 696c   path itself wil
+00000620: 6c20 6265 2073 746f 7265 642e 0a0a 2020  l be stored...  
+00000630: 2020 3a70 6172 616d 206a 736f 6e5f 7061    :param json_pa
+00000640: 7468 3a20 7061 7468 2074 6f20 7468 6520  th: path to the 
+00000650: 4a53 4f4e 2066 696c 6520 746f 206c 6f61  JSON file to loa
+00000660: 6420 6469 6374 696f 6e61 7279 2066 726f  d dictionary fro
+00000670: 6d20 2870 6174 686c 6962 2e50 6174 6829  m (pathlib.Path)
+00000680: 0a20 2020 203a 7061 7261 6d20 7375 625f  .    :param sub_
+00000690: 6a73 6f6e 733a 2069 6620 5472 7565 2c20  jsons: if True, 
+000006a0: 7768 656e 2070 6174 6820 746f 2061 6e6f  when path to ano
+000006b0: 7468 6572 2065 7869 7374 696e 6720 4a53  ther existing JS
+000006c0: 4f4e 2066 696c 6520 6973 2065 6e63 6f75  ON file is encou
+000006d0: 6e74 6572 6564 2c20 7468 6174 204a 534f  ntered, that JSO
+000006e0: 4e20 6669 6c65 2077 696c 6c20 6265 206c  N file will be l
+000006f0: 6f61 6465 640a 2020 2020 2020 2020 2020  oaded.          
+00000700: 2020 2020 2020 2020 2020 7265 6375 7273            recurs
+00000710: 6976 656c 7920 696e 7374 6561 6420 6f66  ively instead of
+00000720: 2073 6176 696e 6720 7468 6520 7061 7468   saving the path
+00000730: 2028 6e6f 7420 6170 706c 6965 6420 746f   (not applied to
+00000740: 206e 616d 6573 2069 6e20 4a53 4f4e 5f4c   names in JSON_L
+00000750: 4f41 4445 525f 4558 434c 5544 4544 5f4e  OADER_EXCLUDED_N
+00000760: 414d 4553 2928 626f 6f6c 6561 6e29 0a20  AMES)(boolean). 
+00000770: 2020 203a 7265 7475 726e 3a20 6469 6374     :return: dict
+00000780: 696f 6e61 7279 2063 6f6e 7374 7275 6374  ionary construct
+00000790: 6564 2066 726f 6d20 7468 6520 6769 7665  ed from the give
+000007a0: 6e20 4a53 4f4e 2066 696c 6520 2864 6963  n JSON file (dic
+000007b0: 7429 0a20 2020 20da 0172 2901 da04 6d6f  t).    ..r)...mo
+000007c0: 6465 54e9 fbff ffff 4e7a 052e 6a73 6f6e  deT.....Nz..json
+000007d0: 5a07 6174 7461 636b 73e9 0100 0000 da07  Z.attacks.......
+000007e0: 6d65 7373 6167 657a 110a 0a47 6f74 2074  messagez...Got t
+000007f0: 6865 2065 7272 6f72 3a20 7a22 0a43 6f75  he error: z".Cou
+00000800: 6c64 206e 6f74 206c 6f61 6420 636f 6e74  ld not load cont
+00000810: 656e 7473 206f 6620 6672 6f6d 3a20 7a5f  ents of from: z_
+00000820: 0a4d 616b 6520 7375 7265 2074 6861 7420  .Make sure that 
+00000830: 7468 6520 7061 7468 2074 6f20 796f 7572  the path to your
+00000840: 204a 534f 4e20 6669 6c65 2069 7320 7661   JSON file is va
+00000850: 6c69 6420 616e 6420 696e 7369 6465 2079  lid and inside y
+00000860: 6f75 7220 4a53 4f4e 2069 7320 6120 7661  our JSON is a va
+00000870: 6c69 6420 6469 6374 696f 6e61 7279 2e7a  lid dictionary.z
+00000880: 414c 6f61 6465 6420 6469 6374 696f 6e61  ALoaded dictiona
+00000890: 7279 2066 726f 6d20 4a53 4f4e 2073 7563  ry from JSON suc
+000008a0: 6365 7373 6675 6c6c 7920 6275 7420 6469  cessfully but di
+000008b0: 6374 696f 6e61 7279 2069 7320 656d 7074  ctionary is empt
+000008c0: 792e e902 0000 0029 01da 0a73 7461 636b  y......)...stack
+000008d0: 6c65 7665 6c29 18da 046f 7065 6e72 0800  level)...openr..
+000008e0: 0000 da04 6c6f 6164 da04 636f 7079 da05  ....load..copy..
+000008f0: 6974 656d 73da 1a4a 534f 4e5f 4c4f 4144  items..JSON_LOAD
+00000900: 4552 5f45 5843 4c55 4445 445f 4e41 4d45  ER_EXCLUDED_NAME
+00000910: 5372 0c00 0000 7210 0000 0072 0b00 0000  Sr....r....r....
+00000920: 7213 0000 00da 0669 7366 696c 65da 136c  r......isfile..l
+00000930: 6f61 645f 6a73 6f6e 5f66 726f 6d5f 6469  oad_json_from_di
+00000940: 736b 7202 0000 00da 0a69 7369 6e73 7461  skr......isinsta
+00000950: 6e63 6572 0d00 0000 da03 6c65 6eda 0945  ncer......len..E
+00000960: 7863 6570 7469 6f6e da07 6861 7361 7474  xception..hasatt
+00000970: 7272 2000 0000 da04 7265 7072 7203 0000  rr .....reprr...
+00000980: 00da 0877 6172 6e69 6e67 73da 0477 6172  ...warnings..war
+00000990: 6eda 0e52 756e 7469 6d65 5761 726e 696e  n..RuntimeWarnin
+000009a0: 6729 0872 1900 0000 721a 0000 00da 0166  g).r....r......f
+000009b0: 5a09 6a73 6f6e 5f64 6174 6172 1500 0000  Z.json_datar....
+000009c0: 7216 0000 00da 0365 7272 7220 0000 0072  r......errr ...r
+000009d0: 1700 0000 7217 0000 0072 1800 0000 7229  ....r....r....r)
+000009e0: 0000 0033 0000 0073 4800 0000 000f 0201  ...3...sH.......
+000009f0: 0e01 0a02 0801 1402 0802 0203 0aff 0202  ................
+00000a00: 0efe 0203 0afd 0207 1003 0802 0cff 0202  ................
+00000a10: 0efe 0203 0afd 0205 1203 1201 1201 0a01  ................
+00000a20: 0803 18ff 0208 1a02 0601 0401 0201 0201  ................
+00000a30: 02fd 0606 7229 0000 0029 01da 054d 696e  ....r)...)...Min
+00000a40: 696f fa12 6d69 6e69 6f61 7069 2e74 726f  io..minioapi.tro
+00000a50: 6a61 6964 6576 da04 7072 6f6a da07 6461  jaidev..proj..da
+00000a60: 7461 7365 74da 056d 6f64 656c fa12 7472  taset..model..tr
+00000a70: 6f6a 2d75 7365 722d 6461 7461 7365 7473  oj-user-datasets
+00000a80: 6308 0000 0000 0000 0000 0000 000a 0000  c...............
+00000a90: 0007 0000 0043 0000 0073 9000 0000 7c05  .....C...s....|.
+00000aa0: 6400 6b08 7214 7c06 6400 6b08 7214 6401  d.k.r.|.d.k.r.d.
+00000ab0: 8201 7400 7c01 7c05 7c06 6402 6400 6403  ..t.|.|.|.d.d.d.
+00000ac0: 8d05 7d08 7401 6a02 a003 7c00 a101 723e  ..}.t.j...|...r>
+00000ad0: 7401 6a02 a004 7c00 a101 7d09 7c08 a005  t.j...|...}.|...
+00000ae0: 7c07 6404 7c02 1700 6404 1700 7c03 1700  |.d.|...d...|...
+00000af0: 6404 1700 7c04 1700 6404 1700 7c09 1700  d...|...d...|...
+00000b00: 7c00 a103 0100 6405 7c07 1700 6404 1700  |.....d.|...d...
+00000b10: 7c02 1700 6404 1700 7c03 1700 6404 1700  |...d...|...d...
+00000b20: 7c04 1700 6404 1700 7c09 1700 5300 2906  |...d...|...S.).
+00000b30: 4e7a 6a4e 6f20 6d69 6e69 6f20 6372 6564  NzjNo minio cred
+00000b40: 656e 7469 616c 7320 7375 7070 6c69 6564  entials supplied
+00000b50: 2066 6f72 2065 7870 6572 696d 656e 7465   for experimente
+00000b60: 722e 2050 6c65 6173 6520 7061 7373 2074  r. Please pass t
+00000b70: 6865 206b 6579 7320 746f 2074 6865 2065  he keys to the e
+00000b80: 7870 6572 696d 656e 7465 7220 636c 6173  xperimenter clas
+00000b90: 732e 2045 7869 7469 6e67 2e2e 2e46 2902  s. Exiting...F).
+00000ba0: 5a06 7365 6375 7265 5a06 7265 6769 6f6e  Z.secureZ.region
+00000bb0: fa01 2f72 0500 0000 2906 7234 0000 0072  ../r....).r4...r
+00000bc0: 0b00 0000 7213 0000 0072 1400 0000 da08  ....r....r......
+00000bd0: 6261 7365 6e61 6d65 5a0b 6670 7574 5f6f  basenameZ.fput_o
+00000be0: 626a 6563 7429 0a5a 0f6c 6f63 616c 5f66  bject).Z.local_f
+00000bf0: 696c 655f 7061 7468 5a0a 7570 6c6f 6164  ile_pathZ.upload
+00000c00: 5f75 726c 5a07 7072 6f6a 6563 7472 3700  _urlZ.projectr7.
+00000c10: 0000 7238 0000 005a 0a6d 696e 696f 5f75  ..r8...Z.minio_u
+00000c20: 7365 725a 0a6d 696e 696f 5f70 6173 735a  serZ.minio_passZ
+00000c30: 0662 7563 6b65 745a 0663 6c69 656e 74da  .bucketZ.client.
+00000c40: 0966 696c 655f 6e61 6d65 7217 0000 0072  .file_namer....r
+00000c50: 1700 0000 7218 0000 00da 0c6d 696e 696f  ....r......minio
+00000c60: 5f75 706c 6f61 647f 0000 0073 0e00 0000  _upload....s....
+00000c70: 0001 1001 0401 1202 0c01 0c02 2a01 723d  ............*.r=
+00000c80: 0000 0029 0154 2907 7235 0000 0072 3600  ...).T).r5...r6.
+00000c90: 0000 7237 0000 0072 3800 0000 4e4e 7239  ..r7...r8...NNr9
+00000ca0: 0000 0029 0f72 0b00 0000 7208 0000 0072  ...).r....r....r
+00000cb0: 2f00 0000 da07 7061 7468 6c69 6272 0200  /.....pathlibr..
+00000cc0: 0000 5a17 7472 6f6a 7364 6b2e 636f 7265  ..Z.trojsdk.core
+00000cd0: 2e74 726f 6a5f 6572 726f 7272 0300 0000  .troj_errorr....
+00000ce0: 7227 0000 0072 0e00 0000 da04 626f 6f6c  r'...r......bool
+00000cf0: 720d 0000 0072 2900 0000 5a05 6d69 6e69  r....r)...Z.mini
+00000d00: 6f72 3400 0000 723d 0000 0072 1700 0000  or4...r=...r....
+00000d10: 7217 0000 0072 1700 0000 7218 0000 00da  r....r....r.....
+00000d20: 083c 6d6f 6475 6c65 3e01 0000 0073 1400  .<module>....s..
+00000d30: 0000 0801 0801 0801 0c01 0c04 0803 0827  ...............'
+00000d40: 1447 0c01 0804                           .G....
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/core/client_utils.py` & `trojai-sdk-0.2.3.4/trojsdk/core/client_utils.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/core/data_utils.py` & `trojai-sdk-0.2.3.4/trojsdk/core/data_utils.py`

 * *Files 12% similar despite different names*

```diff
@@ -112,7 +112,26 @@
         warnings.warn(
             "Loaded dictionary from JSON successfully but dictionary is empty.",
             RuntimeWarning,
             stacklevel=2,
         )
 
     return json_data
+
+
+
+from minio import Minio
+import os
+
+
+
+def minio_upload(local_file_path, upload_url = "minioapi.trojaidev", project = "proj", dataset = "dataset", model = "model",minio_user = None, minio_pass = None, bucket = "troj-user-datasets"):
+    if minio_user is None and minio_pass is None:
+        raise("No minio credentials supplied for experimenter. Please pass the keys to the experimenter class. Exiting...")
+    client = Minio(upload_url, minio_user, minio_pass, secure = False, region=None)
+
+    if os.path.exists(local_file_path):
+        file_name = os.path.basename(local_file_path)
+
+    client.fput_object(bucket, "/"+project +"/"+dataset +"/"+model +"/"+file_name, local_file_path)
+    return "minio://"+bucket+"/"+project +"/"+dataset +"/"+model +"/"+file_name
+
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/core/troj_error.py` & `trojai-sdk-0.2.3.4/trojsdk/core/troj_error.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/auth_config.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/auth_config.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/gcloud_tests/gcloud_auth.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/gcloud_tests/gcloud_auth.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/label_map_num.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/label_map_num.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil/troj_config.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil/troj_config.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/nlp_phil_test.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/nlp_phil_test.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/nlp_test_main.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/testing_config.json`

 * *Files 17% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.925%*

 * *Differences: {"'auth_config'": "'./trojsdk/examples/gcloud_tests/gcloud_auth.json'",*

 * * "'docker_metadata'": "{'docker_image_url': "*

 * *                      "'trojai/trojai-engine-master:10ba6f109b9843e2be008db01465de9e40fc2dc0', "*

 * *                      "delete: ['image_pull_policy']}"}*

```diff
@@ -2,45 +2,31 @@
     "attacks": [
         "QWERTYAttack",
         "DeletionAttack",
         "SynonymAttack",
         "QWERTYAugmentation",
         "DeletionAugmentation"
     ],
-    "auth_config": {
-        "api_endpoint": "http://localhost/api/v1",
-        "auth_keys": {
-            "api_key": "undefined",
-            "id_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMGI4MGFmNC00MDIxLTExZWQtYjg3OC0wMjQyYWMxMjAwMDIiLCJ1c2VybmFtZSI6InRyb2prOHMiLCJlbWFpbCI6Im5vcmVwbHlAdHJvai5haSIsImlhdCI6MTUxNjIzOTAyMn0._xCVejGSmTrgst2JQOSUzC9AHzvqjkO-YyXJCAyndE4",
-            "refresh_token": "undefined"
-        },
-        "dataset_name": "nlp_dset",
-        "project_name": "nlp_test",
-        "secrets": {
-            "AWS_ACCESS_KEY_ID": "AKIAQASF3SJBUF24YMZI",
-            "AWS_SECRET_ACCESS_KEY": "XKLUncdWCrYB9OoLxpSn5r/v638VRfgXZz5p/GOn"
-        }
-    },
+    "auth_config": "./trojsdk/examples/gcloud_tests/gcloud_auth.json",
     "compute_severity": true,
     "dataset": {
         "classes_dictionary": {
             "business": 2,
             "sports": 1,
             "technology": 3,
             "world": 0
         },
         "input_column": "input",
         "name": "test_nlp_dataset",
         "path_to_data": "s3://troj-coco-backup/nlp/dataset.csv",
         "target_column": "label"
     },
     "docker_metadata": {
-        "docker_image_url": "trojai/troj-engine-base-nlp:4b32477c7ca05dde671b1c953014a49ccf00981d",
-        "docker_secret_name": "trojaicreds",
-        "image_pull_policy": "IfNotPresent"
+        "docker_image_url": "trojai/trojai-engine-master:10ba6f109b9843e2be008db01465de9e40fc2dc0",
+        "docker_secret_name": "trojaicreds"
     },
     "model": {
         "metadata": [
             "meta1",
             "meta2"
         ],
         "model_args_dict": {},
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/s3_small_classification_pt_config.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/s3_small_classification_pt_config.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/tabular_SMOTETomek_logistic_base.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/tabular_SMOTETomek_logistic_base.json`

 * *Files 4% similar despite different names*

```diff
@@ -16,83 +16,81 @@
 000000f0: 6765 2f43 7265 6469 7441 7070 726f 7661  ge/CreditApprova
 00000100: 6c46 696c 6573 2f63 6c65 616e 6564 5f61  lFiles/cleaned_a
 00000110: 7070 726f 7661 6c5f 7465 7374 2e63 7376  pproval_test.csv
 00000120: 222c 0d0a 0909 2264 6174 615f 6c6f 6164  ",...."data_load
 00000130: 6572 5f63 6f6e 6669 6722 3a20 7b0d 0a09  er_config": {...
 00000140: 0909 2262 6174 6368 5f73 697a 6522 3a20  .."batch_size": 
 00000150: 3136 2c0d 0a09 0909 2273 6875 6666 6c65  16,....."shuffle
-00000160: 223a 2066 616c 7365 0d0a 0909 7d2c 0d0a  ": false....},..
-00000170: 097d 2c0d 0a09 2274 7261 696e 5f64 6174  .},..."train_dat
-00000180: 6173 6574 223a 207b 0d0a 0909 226e 616d  aset": {...."nam
-00000190: 6522 3a20 2263 6c65 616e 6564 5f63 7265  e": "cleaned_cre
-000001a0: 6469 745f 6170 7072 6f76 616c 5f74 7261  dit_approval_tra
-000001b0: 696e 222c 0d0a 0909 2270 6174 685f 746f  in",...."path_to
-000001c0: 5f64 6174 6122 3a20 2273 333a 2f2f 7472  _data": "s3://tr
-000001d0: 6f6a 6169 2d6f 626a 6563 742d 7374 6f72  ojai-object-stor
-000001e0: 6167 652f 4372 6564 6974 4170 7072 6f76  age/CreditApprov
-000001f0: 616c 4669 6c65 732f 636c 6561 6e65 645f  alFiles/cleaned_
-00000200: 6170 7072 6f76 616c 5f74 7261 696e 2e63  approval_train.c
-00000210: 7376 222c 0d0a 0909 2264 6174 615f 6c6f  sv",...."data_lo
-00000220: 6164 6572 5f63 6f6e 6669 6722 3a20 7b0d  ader_config": {.
-00000230: 0a09 0909 2262 6174 6368 5f73 697a 6522  ...."batch_size"
-00000240: 3a20 3136 2c0d 0a09 0909 2273 6875 6666  : 16,....."shuff
-00000250: 6c65 223a 2066 616c 7365 0d0a 0909 7d2c  le": false....},
-00000260: 0d0a 0909 226c 6162 656c 5f63 6f6c 756d  ...."label_colum
-00000270: 6e22 3a20 2274 6172 6765 7422 2c0d 0a09  n": "target",...
-00000280: 0922 636c 6173 7365 735f 6469 6374 696f  ."classes_dictio
-00000290: 6e61 7279 223a 207b 0d0a 0909 0922 4e6f  nary": {....."No
-000002a0: 223a 2030 2c0d 0a09 0909 2259 6573 223a  ": 0,....."Yes":
-000002b0: 2031 0d0a 0909 7d0d 0a09 7d2c 0d0a 0922   1....}...},..."
-000002c0: 6d6f 6465 6c22 3a20 7b0d 0a09 0922 6e61  model": {...."na
-000002d0: 6d65 223a 2022 534d 4f54 4554 6f6d 656b  me": "SMOTETomek
-000002e0: 5f6c 6f67 6973 7469 6322 2c0d 0a09 0922  _logistic",...."
-000002f0: 7061 7468 5f74 6f5f 6d6f 6465 6c5f 6669  path_to_model_fi
-00000300: 6c65 223a 2022 7333 3a2f 2f74 726f 6a61  le": "s3://troja
-00000310: 692d 6f62 6a65 6374 2d73 746f 7261 6765  i-object-storage
-00000320: 2f43 7265 6469 7441 7070 726f 7661 6c46  /CreditApprovalF
-00000330: 696c 6573 2f73 6b6c 6561 726e 5f77 7261  iles/sklearn_wra
-00000340: 7070 6572 2e70 7922 2c0d 0a09 0922 6d6f  pper.py",...."mo
-00000350: 6465 6c5f 6172 6773 5f64 6963 7422 3a20  del_args_dict": 
-00000360: 7b0d 0a09 0909 226d 6f64 656c 5f66 696c  {....."model_fil
-00000370: 6522 3a20 2273 333a 2f2f 7472 6f6a 6169  e": "s3://trojai
-00000380: 2d6f 626a 6563 742d 7374 6f72 6167 652f  -object-storage/
-00000390: 4372 6564 6974 4170 7072 6f76 616c 4669  CreditApprovalFi
-000003a0: 6c65 732f 534d 4f54 4554 6f6d 656b 5f6c  les/SMOTETomek_l
-000003b0: 6f67 6973 7469 632e 706b 6c22 0d0a 0909  ogistic.pkl"....
-000003c0: 7d0d 0a09 7d2c 0d0a 0922 6175 7468 5f63  }...},..."auth_c
-000003d0: 6f6e 6669 6722 3a20 7b0d 0a09 0922 6170  onfig": {...."ap
-000003e0: 695f 656e 6470 6f69 6e74 223a 2022 6874  i_endpoint": "ht
-000003f0: 7470 733a 2f2f 7472 6f6a 6169 6261 636b  tps://trojaiback
-00000400: 656e 642e 7472 6f6a 2e67 7265 656e 2f61  end.troj.green/a
-00000410: 7069 2f76 3122 2c0d 0a09 0922 6175 7468  pi/v1",...."auth
-00000420: 5f6b 6579 7322 3a20 7b0d 0a09 0909 2261  _keys": {....."a
-00000430: 7069 5f6b 6579 223a 2022 576c 6132 4644  pi_key": "Wla2FD
-00000440: 4462 6a4c 316a 5733 6669 6a68 7a36 4931  DbjL1jW3fijhz6I1
-00000450: 7032 5257 3478 5370 7645 3156 6162 6135  p2RW4xSpvE1Vaba5
-00000460: 3058 220d 0a09 097d 2c0d 0a09 0922 7365  0X"....},...."se
-00000470: 6372 6574 7322 3a20 7b0d 0a09 0909 2241  crets": {....."A
-00000480: 5753 5f41 4343 4553 535f 4b45 595f 4944  WS_ACCESS_KEY_ID
-00000490: 223a 2022 414b 4941 5141 5346 3353 4a42  ": "AKIAQASF3SJB
-000004a0: 5546 3234 594d 5a49 222c 0d0a 0909 0922  UF24YMZI",....."
-000004b0: 4157 535f 5345 4352 4554 5f41 4343 4553  AWS_SECRET_ACCES
-000004c0: 535f 4b45 5922 3a20 2258 4b4c 556e 6364  S_KEY": "XKLUncd
-000004d0: 5743 7259 4239 4f6f 4c78 7053 6e35 722f  WCrYB9OoLxpSn5r/
-000004e0: 7636 3338 5652 6667 585a 7a35 702f 474f  v638VRfgXZz5p/GO
-000004f0: 6e22 0d0a 0909 7d2c 0d0a 0909 2270 726f  n"....},...."pro
-00000500: 6a65 6374 5f6e 616d 6522 3a20 2263 7265  ject_name": "cre
-00000510: 6469 745f 6170 7072 6f76 616c 5f6d 6f64  dit_approval_mod
-00000520: 656c 5f63 6f6d 7061 7269 736f 6e22 2c0d  el_comparison",.
-00000530: 0a09 0922 6461 7461 7365 745f 6e61 6d65  ..."dataset_name
-00000540: 223a 2022 636c 6561 6e65 645f 6372 6564  ": "cleaned_cred
-00000550: 6974 5f61 7070 726f 7661 6c5f 6461 7461  it_approval_data
-00000560: 220d 0a09 7d2c 0d0a 0922 646f 636b 6572  "...},..."docker
-00000570: 5f6d 6574 6164 6174 6122 3a20 7b0d 0a09  _metadata": {...
-00000580: 0922 646f 636b 6572 5f69 6d61 6765 5f75  ."docker_image_u
-00000590: 726c 223a 2022 7472 6f6a 6169 2f74 726f  rl": "trojai/tro
-000005a0: 6a2d 656e 6769 6e65 2d62 6173 652d 7461  j-engine-base-ta
-000005b0: 6275 6c61 723a 7461 6275 6c61 722d 6465  bular:tabular-de
-000005c0: 762d 6c61 7465 7374 222c 0d0a 0909 2264  v-latest",...."d
-000005d0: 6f63 6b65 725f 7365 6372 6574 5f6e 616d  ocker_secret_nam
-000005e0: 6522 3a20 2274 726f 6a61 6963 7265 6473  e": "trojaicreds
-000005f0: 222c 0d0a 0909 2269 6d61 6765 5f70 756c  ",...."image_pul
-00000600: 6c5f 706f 6c69 6379 223a 2022 416c 7761  l_policy": "Alwa
-00000610: 7973 220d 0a09 7d0d 0a7d                 ys"...}..}
+00000160: 223a 2066 616c 7365 0d0a 0909 7d0d 0a09  ": false....}...
+00000170: 7d2c 0d0a 0922 7472 6169 6e5f 6461 7461  },..."train_data
+00000180: 7365 7422 3a20 7b0d 0a09 0922 6e61 6d65  set": {...."name
+00000190: 223a 2022 636c 6561 6e65 645f 6372 6564  ": "cleaned_cred
+000001a0: 6974 5f61 7070 726f 7661 6c5f 7472 6169  it_approval_trai
+000001b0: 6e22 2c0d 0a09 0922 7061 7468 5f74 6f5f  n",...."path_to_
+000001c0: 6461 7461 223a 2022 7333 3a2f 2f74 726f  data": "s3://tro
+000001d0: 6a61 692d 6f62 6a65 6374 2d73 746f 7261  jai-object-stora
+000001e0: 6765 2f43 7265 6469 7441 7070 726f 7661  ge/CreditApprova
+000001f0: 6c46 696c 6573 2f63 6c65 616e 6564 5f61  lFiles/cleaned_a
+00000200: 7070 726f 7661 6c5f 7472 6169 6e2e 6373  pproval_train.cs
+00000210: 7622 2c0d 0a09 0922 6461 7461 5f6c 6f61  v",...."data_loa
+00000220: 6465 725f 636f 6e66 6967 223a 207b 0d0a  der_config": {..
+00000230: 0909 0922 6261 7463 685f 7369 7a65 223a  ..."batch_size":
+00000240: 2031 362c 0d0a 0909 0922 7368 7566 666c   16,....."shuffl
+00000250: 6522 3a20 6661 6c73 650d 0a09 097d 2c0d  e": false....},.
+00000260: 0a09 0922 6c61 6265 6c5f 636f 6c75 6d6e  ..."label_column
+00000270: 223a 2022 7461 7267 6574 222c 0d0a 0909  ": "target",....
+00000280: 2263 6c61 7373 6573 5f64 6963 7469 6f6e  "classes_diction
+00000290: 6172 7922 3a20 7b0d 0a09 0909 224e 6f22  ary": {....."No"
+000002a0: 3a20 302c 0d0a 0909 0922 5965 7322 3a20  : 0,....."Yes": 
+000002b0: 310d 0a09 097d 0d0a 097d 2c0d 0a09 226d  1....}...},..."m
+000002c0: 6f64 656c 223a 207b 0d0a 0909 226e 616d  odel": {...."nam
+000002d0: 6522 3a20 2253 4d4f 5445 546f 6d65 6b5f  e": "SMOTETomek_
+000002e0: 6c6f 6769 7374 6963 222c 0d0a 0909 2270  logistic",...."p
+000002f0: 6174 685f 746f 5f6d 6f64 656c 5f66 696c  ath_to_model_fil
+00000300: 6522 3a20 2273 333a 2f2f 7472 6f6a 6169  e": "s3://trojai
+00000310: 2d6f 626a 6563 742d 7374 6f72 6167 652f  -object-storage/
+00000320: 4372 6564 6974 4170 7072 6f76 616c 4669  CreditApprovalFi
+00000330: 6c65 732f 736b 6c65 6172 6e5f 7772 6170  les/sklearn_wrap
+00000340: 7065 722e 7079 222c 0d0a 0909 226d 6f64  per.py",...."mod
+00000350: 656c 5f61 7267 735f 6469 6374 223a 207b  el_args_dict": {
+00000360: 0d0a 0909 0922 6d6f 6465 6c5f 6669 6c65  ....."model_file
+00000370: 223a 2022 7333 3a2f 2f74 726f 6a61 692d  ": "s3://trojai-
+00000380: 6f62 6a65 6374 2d73 746f 7261 6765 2f43  object-storage/C
+00000390: 7265 6469 7441 7070 726f 7661 6c46 696c  reditApprovalFil
+000003a0: 6573 2f53 4d4f 5445 546f 6d65 6b5f 6c6f  es/SMOTETomek_lo
+000003b0: 6769 7374 6963 2e70 6b6c 220d 0a09 097d  gistic.pkl"....}
+000003c0: 0d0a 097d 2c0d 0a09 2261 7574 685f 636f  ...},..."auth_co
+000003d0: 6e66 6967 223a 207b 0d0a 0909 2261 7069  nfig": {...."api
+000003e0: 5f65 6e64 706f 696e 7422 3a20 2268 7474  _endpoint": "htt
+000003f0: 7073 3a2f 2f74 726f 6a61 6962 6163 6b65  ps://trojaibacke
+00000400: 6e64 2e74 726f 6a2e 7265 642f 6170 692f  nd.troj.red/api/
+00000410: 7631 222c 0d0a 0909 2261 7574 685f 6b65  v1",...."auth_ke
+00000420: 7973 223a 207b 0d0a 0909 0922 6170 695f  ys": {....."api_
+00000430: 6b65 7922 3a20 2235 3535 3535 220d 0a09  key": "55555"...
+00000440: 097d 2c0d 0a09 0922 7365 6372 6574 7322  .},...."secrets"
+00000450: 3a20 7b0d 0a09 0909 2241 5753 5f41 4343  : {....."AWS_ACC
+00000460: 4553 535f 4b45 595f 4944 223a 2022 414b  ESS_KEY_ID": "AK
+00000470: 4941 5141 5346 3353 4a42 5546 3234 594d  IAQASF3SJBUF24YM
+00000480: 5a49 222c 0d0a 0909 0922 4157 535f 5345  ZI",....."AWS_SE
+00000490: 4352 4554 5f41 4343 4553 535f 4b45 5922  CRET_ACCESS_KEY"
+000004a0: 3a20 2258 4b4c 556e 6364 5743 7259 4239  : "XKLUncdWCrYB9
+000004b0: 4f6f 4c78 7053 6e35 722f 7636 3338 5652  OoLxpSn5r/v638VR
+000004c0: 6667 585a 7a35 702f 474f 6e22 0d0a 0909  fgXZz5p/GOn"....
+000004d0: 7d2c 0d0a 0909 2270 726f 6a65 6374 5f6e  },...."project_n
+000004e0: 616d 6522 3a20 2263 7265 6469 745f 6170  ame": "credit_ap
+000004f0: 7072 6f76 616c 5f6d 6f64 656c 5f63 6f6d  proval_model_com
+00000500: 7061 7269 736f 6e22 2c0d 0a09 0922 6461  parison",...."da
+00000510: 7461 7365 745f 6e61 6d65 223a 2022 636c  taset_name": "cl
+00000520: 6561 6e65 645f 6372 6564 6974 5f61 7070  eaned_credit_app
+00000530: 726f 7661 6c5f 6461 7461 220d 0a09 7d2c  roval_data"...},
+00000540: 0d0a 0922 646f 636b 6572 5f6d 6574 6164  ..."docker_metad
+00000550: 6174 6122 3a20 7b0d 0a09 0922 646f 636b  ata": {...."dock
+00000560: 6572 5f69 6d61 6765 5f75 726c 223a 2022  er_image_url": "
+00000570: 7472 6f6a 6169 2f74 726f 6a2d 656e 6769  trojai/troj-engi
+00000580: 6e65 2d62 6173 652d 7461 6275 6c61 723a  ne-base-tabular:
+00000590: 7461 6275 6c61 722d 6465 762d 6c61 7465  tabular-dev-late
+000005a0: 7374 222c 0d0a 0909 2264 6f63 6b65 725f  st",...."docker_
+000005b0: 7365 6372 6574 5f6e 616d 6522 3a20 2274  secret_name": "t
+000005c0: 726f 6a61 6963 7265 6473 222c 0d0a 0909  rojaicreds",....
+000005d0: 2269 6d61 6765 5f70 756c 6c5f 706f 6c69  "image_pull_poli
+000005e0: 6379 223a 2022 416c 7761 7973 220d 0a09  cy": "Always"...
+000005f0: 7d0d 0a7d                                }..}
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/tabular_medical_insurance_config.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/tabular_medical_insurance_config.json`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9642857142857143%*

 * *Differences: {"'auth_config'": "'./trojsdk/examples/auth_config_dev.json'"}*

```diff
@@ -48,26 +48,15 @@
             "column_names": [
                 "bmi"
             ],
             "display_name": "Scale shift attack on bmi feature"
         }
     ],
     "audit": true,
-    "auth_config": {
-        "api_endpoint": "https://trojaibackend.troj.red/api/v1",
-        "auth_keys": {
-            "api_key": "55555"
-        },
-        "dataset_name": "medical_insurance_data",
-        "project_name": "medical_insurance_estimation",
-        "secrets": {
-            "AWS_ACCESS_KEY_ID": "AKIAQASF3SJBUF24YMZI",
-            "AWS_SECRET_ACCESS_KEY": "XKLUncdWCrYB9OoLxpSn5r/v638VRfgXZz5p/GOn"
-        }
-    },
+    "auth_config": "./trojsdk/examples/auth_config_dev.json",
     "dataset": {
         "data_loader_config": {
             "batch_size": 3,
             "shuffle": false
         },
         "label_column": "charges",
         "name": "insurance_test_dataset",
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/tabular_test_main.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/tabular_test_main.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/tabular_test/troj_dev_auth.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/tabular_test/troj_dev_auth.json`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/examples/testing_config.json` & `trojai-sdk-0.2.3.4/trojsdk/examples/nlp_test_main.json`

 * *Files 23% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.925%*

 * *Differences: {"'auth_config'": "'trojsdk/examples/auth_config_dev.json'",*

 * * "'docker_metadata'": "{'docker_image_url': "*

 * *                      "'trojai/troj-engine-base-nlp:4b32477c7ca05dde671b1c953014a49ccf00981d', "*

 * *                      "'image_pull_policy': 'IfNotPresent'}"}*

```diff
@@ -2,31 +2,32 @@
     "attacks": [
         "QWERTYAttack",
         "DeletionAttack",
         "SynonymAttack",
         "QWERTYAugmentation",
         "DeletionAugmentation"
     ],
-    "auth_config": "./trojsdk/examples/gcloud_tests/gcloud_auth.json",
+    "auth_config": "trojsdk/examples/auth_config_dev.json",
     "compute_severity": true,
     "dataset": {
         "classes_dictionary": {
             "business": 2,
             "sports": 1,
             "technology": 3,
             "world": 0
         },
         "input_column": "input",
         "name": "test_nlp_dataset",
         "path_to_data": "s3://troj-coco-backup/nlp/dataset.csv",
         "target_column": "label"
     },
     "docker_metadata": {
-        "docker_image_url": "trojai/trojai-engine-master:10ba6f109b9843e2be008db01465de9e40fc2dc0",
-        "docker_secret_name": "trojaicreds"
+        "docker_image_url": "trojai/troj-engine-base-nlp:4b32477c7ca05dde671b1c953014a49ccf00981d",
+        "docker_secret_name": "trojaicreds",
+        "image_pull_policy": "IfNotPresent"
     },
     "model": {
         "metadata": [
             "meta1",
             "meta2"
         ],
         "model_args_dict": {},
```

### Comparing `trojai-sdk-0.2.3.3/trojsdk/setup.py` & `trojai-sdk-0.2.3.4/trojsdk/setup.py`

 * *Files identical despite different names*

### Comparing `trojai-sdk-0.2.3.3/trojsdk/test_sdk.py` & `trojai-sdk-0.2.3.4/trojsdk/test_sdk.py`

 * *Files 14% similar despite different names*

```diff
@@ -12,15 +12,15 @@
     except:
         assert True
 
 
 def test_sdk_pass_tabular():
 
     troj_job_handler = client_utils.submit_evaluation(
-        path_to_config="trojsdk/examples/tabular_medical_insurance_config.json", nossl=True
+        path_to_config="./trojsdk/examples/tabular_medical_insurance_config.json", nossl=True
     )
 
     import time
 
     time.sleep(2)
     try:
         troj_job_handler.check_job_status()
```

