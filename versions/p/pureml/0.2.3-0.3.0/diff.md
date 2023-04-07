# Comparing `tmp/pureml-0.2.3.tar.gz` & `tmp/pureml-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pureml-0.2.3.tar", max compression
+gzip compressed data, was "pureml-0.3.0.tar", max compression
```

## Comparing `pureml-0.2.3.tar` & `pureml-0.3.0.tar`

### file list

```diff
@@ -1,77 +1,103 @@
--rw-r--r--   0        0        0     9950 2023-02-10 14:59:50.806242 pureml-0.2.3/README.md
--rw-r--r--   0        0        0      583 2023-02-28 18:31:10.554920 pureml-0.2.3/pureml/__init__.py
--rw-r--r--   0        0        0     2534 2023-02-10 14:59:50.822240 pureml-0.2.3/pureml/cli/__init__.py
--rw-r--r--   0        0        0     5749 2023-02-28 18:31:10.586922 pureml-0.2.3/pureml/cli/auth.py
--rw-r--r--   0        0        0      669 2023-01-10 08:50:07.932557 pureml-0.2.3/pureml/cli/main.py
--rw-r--r--   0        0        0      451 2023-01-10 08:50:07.936557 pureml-0.2.3/pureml/cli/public.pem
--rw-r--r--   0        0        0     2710 2023-01-10 08:50:07.936557 pureml-0.2.3/pureml/cli/secrets.py
--rw-r--r--   0        0        0     1553 2023-02-28 18:31:10.634926 pureml-0.2.3/pureml/components/__init__.py
--rw-r--r--   0        0        0     7073 2023-02-28 18:31:10.654928 pureml-0.2.3/pureml/components/arrays.py
--rw-r--r--   0        0        0     6852 2023-02-28 18:31:10.666929 pureml-0.2.3/pureml/components/artifacts.py
--rw-r--r--   0        0        0     6830 2023-02-28 18:31:10.690931 pureml-0.2.3/pureml/components/audio.py
--rw-r--r--   0        0        0     1748 2023-02-28 18:31:10.702932 pureml-0.2.3/pureml/components/auth.py
--rw-r--r--   0        0        0    15323 2023-02-28 18:31:10.798939 pureml-0.2.3/pureml/components/dataset.py
--rw-r--r--   0        0        0     8503 2023-02-28 18:31:10.866945 pureml-0.2.3/pureml/components/figure.py
--rw-r--r--   0        0        0     6801 2023-02-28 18:31:10.886947 pureml-0.2.3/pureml/components/image.py
--rw-r--r--   0        0        0     1923 2023-02-10 14:59:50.882233 pureml-0.2.3/pureml/components/log.py
--rw-r--r--   0        0        0     5351 2023-02-28 18:31:10.918949 pureml-0.2.3/pureml/components/metrics.py
--rw-r--r--   0        0        0    13094 2023-02-28 18:31:10.930950 pureml-0.2.3/pureml/components/model.py
--rw-r--r--   0        0        0     5343 2023-02-28 18:31:10.938951 pureml-0.2.3/pureml/components/params.py
--rw-r--r--   0        0        0     6909 2023-02-28 18:31:10.942951 pureml-0.2.3/pureml/components/tabular.py
--rw-r--r--   0        0        0     6308 2023-02-28 18:31:10.954952 pureml-0.2.3/pureml/components/video.py
--rw-r--r--   0        0        0        0 2023-01-10 08:50:07.988555 pureml-0.2.3/pureml/config/__init__.py
--rw-r--r--   0        0        0     3753 2023-01-10 08:50:07.988555 pureml-0.2.3/pureml/config/parser.py
--rw-r--r--   0        0        0      123 2023-01-10 08:50:07.988555 pureml-0.2.3/pureml/decorators/__init__.py
--rw-r--r--   0        0        0     1478 2023-02-10 14:59:50.926228 pureml-0.2.3/pureml/decorators/dataset.py
--rw-r--r--   0        0        0      597 2023-01-10 08:50:07.992555 pureml-0.2.3/pureml/decorators/load_data.py
--rw-r--r--   0        0        0     1956 2023-02-10 14:59:50.934228 pureml-0.2.3/pureml/decorators/model.py
--rw-r--r--   0        0        0      607 2023-01-10 08:50:07.992555 pureml-0.2.3/pureml/decorators/pip_requirements.py
--rw-r--r--   0        0        0      838 2023-01-10 08:50:08.012554 pureml-0.2.3/pureml/decorators/predict.py
--rw-r--r--   0        0        0      634 2023-01-10 08:50:08.012554 pureml-0.2.3/pureml/decorators/transformer.py
--rw-r--r--   0        0        0        0 2023-01-10 08:50:08.012554 pureml-0.2.3/pureml/deploy/__init__.py
--rw-r--r--   0        0        0     4491 2023-02-28 18:31:10.954952 pureml-0.2.3/pureml/deploy/docker.py
--rw-r--r--   0        0        0     7866 2023-02-28 18:31:10.954952 pureml-0.2.3/pureml/deploy/fastapi.py
--rw-r--r--   0        0        0        0 2023-02-10 14:59:50.954225 pureml-0.2.3/pureml/lineage/__init__.py
--rw-r--r--   0        0        0        0 2023-02-10 14:59:50.954225 pureml-0.2.3/pureml/lineage/data/__init__.py
--rw-r--r--   0        0        0     2614 2023-02-28 18:31:10.962953 pureml-0.2.3/pureml/lineage/data/create_lineage.py
--rw-r--r--   0        0        0      902 2023-02-10 14:59:50.994221 pureml-0.2.3/pureml/packaging/__init__.py
--rw-r--r--   0        0        0      496 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/errors.py
--rw-r--r--   0        0        0     2245 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_framework.py
--rw-r--r--   0        0        0        0 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/__init__.py
--rw-r--r--   0        0        0      973 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/catboost.py
--rw-r--r--   0        0        0     1103 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/custom.py
--rw-r--r--   0        0        0      965 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/keras.py
--rw-r--r--   0        0        0      976 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/lightgbm.py
--rw-r--r--   0        0        0     1075 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/pytorch.py
--rw-r--r--   0        0        0     1146 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/pytorch_tabnet.py
--rw-r--r--   0        0        0     2163 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/sklearn.py
--rw-r--r--   0        0        0     1028 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/tensorflow.py
--rw-r--r--   0        0        0     1021 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/model_packaging/xgboost.py
--rw-r--r--   0        0        0     4006 2023-02-28 18:31:10.974954 pureml-0.2.3/pureml/packaging/packaging.py
--rw-r--r--   0        0        0     1381 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/packaging/packaging_utils.py
--rw-r--r--   0        0        0        0 2023-02-28 18:31:10.974954 pureml-0.2.3/pureml/predictor/__init__.py
--rw-r--r--   0        0        0      951 2023-02-28 18:31:10.982954 pureml-0.2.3/pureml/predictor/predictor.py
--rw-r--r--   0        0        0      285 2023-02-28 18:31:10.986955 pureml-0.2.3/pureml/schema/__init__.py
--rw-r--r--   0        0        0      286 2023-02-28 18:31:10.994955 pureml-0.2.3/pureml/schema/backend.py
--rw-r--r--   0        0        0      330 2023-02-28 18:31:11.006956 pureml-0.2.3/pureml/schema/dataset.py
--rw-r--r--   0        0        0      248 2023-02-28 18:31:11.014957 pureml-0.2.3/pureml/schema/log.py
--rw-r--r--   0        0        0      396 2023-02-28 18:31:11.018957 pureml-0.2.3/pureml/schema/model.py
--rw-r--r--   0        0        0     1048 2023-02-28 18:31:11.018957 pureml-0.2.3/pureml/schema/packaging.py
--rw-r--r--   0        0        0     2528 2023-02-28 18:31:11.018957 pureml-0.2.3/pureml/schema/paths.py
--rw-r--r--   0        0        0      656 2023-02-28 18:31:11.030958 pureml-0.2.3/pureml/schema/prediction.py
--rw-r--r--   0        0        0      385 2023-02-28 18:31:11.038959 pureml-0.2.3/pureml/schema/singleton.py
--rw-r--r--   0        0        0      348 2023-02-28 18:31:11.050960 pureml-0.2.3/pureml/schema/storage.py
--rw-r--r--   0        0        0        0 2023-01-10 08:50:08.016554 pureml-0.2.3/pureml/utils/__init__.py
--rw-r--r--   0        0        0     1061 2023-02-28 18:31:11.062961 pureml-0.2.3/pureml/utils/config.py
--rw-r--r--   0        0        0     2234 2023-02-28 18:31:11.062961 pureml-0.2.3/pureml/utils/constants.py
--rw-r--r--   0        0        0     1877 2023-02-02 14:56:03.901033 pureml-0.2.3/pureml/utils/deploy.py
--rw-r--r--   0        0        0     2998 2023-02-28 18:31:11.074962 pureml-0.2.3/pureml/utils/hash.py
--rw-r--r--   0        0        0      522 2023-02-10 14:59:51.046215 pureml-0.2.3/pureml/utils/log_utils.py
--rw-r--r--   0        0        0     8071 2023-02-28 18:31:11.086963 pureml-0.2.3/pureml/utils/pipeline.py
--rw-r--r--   0        0        0        0 2023-02-28 18:31:11.086963 pureml-0.2.3/pureml/utils/prediction.py
--rw-r--r--   0        0        0      815 2023-02-10 14:59:51.066213 pureml-0.2.3/pureml/utils/readme.py
--rw-r--r--   0        0        0      137 2023-01-10 08:50:08.036553 pureml-0.2.3/pureml/utils/source_code.py
--rw-r--r--   0        0        0        0 2023-02-28 18:31:11.086963 pureml-0.2.3/pureml/utils/types.py
--rw-r--r--   0        0        0     1843 2023-02-28 18:31:11.098964 pureml-0.2.3/pyproject.toml
--rw-r--r--   0        0        0    11704 2023-02-28 18:31:35.412561 pureml-0.2.3/setup.py
--rw-r--r--   0        0        0    11501 2023-02-28 18:31:35.413231 pureml-0.2.3/PKG-INFO
+-rw-r--r--   0        0        0    11370 2023-04-05 12:44:15.330474 pureml-0.3.0/README.md
+-rw-r--r--   0        0        0      734 2023-04-05 12:44:15.330474 pureml-0.3.0/pureml/__init__.py
+-rw-r--r--   0        0        0     2534 2023-02-10 14:59:50.822240 pureml-0.3.0/pureml/cli/__init__.py
+-rw-r--r--   0        0        0    11745 2023-04-06 11:08:34.084115 pureml-0.3.0/pureml/cli/auth.py
+-rw-r--r--   0        0        0        0 2023-04-06 11:08:34.084115 pureml-0.3.0/pureml/cli/config.py
+-rw-r--r--   0        0        0      669 2023-01-10 08:50:07.932557 pureml-0.3.0/pureml/cli/main.py
+-rw-r--r--   0        0        0      451 2023-01-10 08:50:07.936557 pureml-0.3.0/pureml/cli/public.pem
+-rw-r--r--   0        0        0     6501 2023-04-05 12:44:15.330474 pureml-0.3.0/pureml/cli/secrets.py
+-rw-r--r--   0        0        0     1552 2023-04-05 12:44:15.330474 pureml-0.3.0/pureml/components/__init__.py
+-rw-r--r--   0        0        0     1748 2023-03-15 11:32:06.993246 pureml-0.3.0/pureml/components/auth.py
+-rw-r--r--   0        0        0    15689 2023-04-05 12:45:28.052176 pureml-0.3.0/pureml/components/dataset.py
+-rw-r--r--   0        0        0       99 2023-04-05 12:44:15.342474 pureml-0.3.0/pureml/components/log/__init__.py
+-rw-r--r--   0        0        0     7073 2023-04-05 12:44:15.702483 pureml-0.3.0/pureml/components/log/arrays.py
+-rw-r--r--   0        0        0     6852 2023-04-05 12:44:15.702483 pureml-0.3.0/pureml/components/log/artifacts.py
+-rw-r--r--   0        0        0     6830 2023-04-05 12:44:15.702483 pureml-0.3.0/pureml/components/log/audio.py
+-rw-r--r--   0        0        0     9667 2023-04-05 12:44:15.702483 pureml-0.3.0/pureml/components/log/figure.py
+-rw-r--r--   0        0        0     6801 2023-04-05 12:44:15.702483 pureml-0.3.0/pureml/components/log/image.py
+-rw-r--r--   0        0        0     2052 2023-04-05 12:44:15.358475 pureml-0.3.0/pureml/components/log/log.py
+-rw-r--r--   0        0        0     6045 2023-04-05 12:44:15.702483 pureml-0.3.0/pureml/components/log/metrics.py
+-rw-r--r--   0        0        0     6016 2023-04-05 12:44:15.702483 pureml-0.3.0/pureml/components/log/params.py
+-rw-r--r--   0        0        0     6196 2023-04-05 12:44:15.358475 pureml-0.3.0/pureml/components/log/pip_requirement.py
+-rw-r--r--   0        0        0     6213 2023-04-05 12:44:15.358475 pureml-0.3.0/pureml/components/log/predict.py
+-rw-r--r--   0        0        0     6029 2023-04-05 12:44:15.358475 pureml-0.3.0/pureml/components/log/resources.py
+-rw-r--r--   0        0        0     6909 2023-04-05 12:44:15.698483 pureml-0.3.0/pureml/components/log/tabular.py
+-rw-r--r--   0        0        0     6308 2023-04-05 12:44:15.698483 pureml-0.3.0/pureml/components/log/video.py
+-rw-r--r--   0        0        0    13619 2023-04-05 12:44:15.358475 pureml-0.3.0/pureml/components/model.py
+-rw-r--r--   0        0        0        0 2023-01-10 08:50:07.988555 pureml-0.3.0/pureml/config/__init__.py
+-rw-r--r--   0        0        0     3753 2023-01-10 08:50:07.988555 pureml-0.3.0/pureml/config/parser.py
+-rw-r--r--   0        0        0      123 2023-04-06 11:08:21.812260 pureml-0.3.0/pureml/decorators/__init__.py
+-rw-r--r--   0        0        0     2219 2023-04-06 11:08:21.812260 pureml-0.3.0/pureml/decorators/dataset.py
+-rw-r--r--   0        0        0      856 2023-04-05 12:44:15.358475 pureml-0.3.0/pureml/decorators/load_data.py
+-rw-r--r--   0        0        0     2720 2023-04-05 12:44:15.358475 pureml-0.3.0/pureml/decorators/model.py
+-rw-r--r--   0        0        0      607 2023-01-10 08:50:07.992555 pureml-0.3.0/pureml/decorators/pip_requirements.py
+-rw-r--r--   0        0        0      838 2023-01-10 08:50:08.012554 pureml-0.3.0/pureml/decorators/predict.py
+-rw-r--r--   0        0        0      895 2023-04-05 12:44:15.362475 pureml-0.3.0/pureml/decorators/transformer.py
+-rw-r--r--   0        0        0       49 2023-04-05 12:44:15.362475 pureml-0.3.0/pureml/evaluate/__init__.py
+-rw-r--r--   0        0        0     1489 2023-04-05 12:44:15.362475 pureml-0.3.0/pureml/evaluate/classification.py
+-rw-r--r--   0        0        0     1766 2023-04-05 12:44:15.362475 pureml-0.3.0/pureml/evaluate/eval.py
+-rw-r--r--   0        0        0     1665 2023-04-05 12:44:15.370475 pureml-0.3.0/pureml/evaluate/grade.py
+-rw-r--r--   0        0        0      227 2023-04-05 12:44:15.382475 pureml-0.3.0/pureml/evaluate/metrics/__init__.py
+-rw-r--r--   0        0        0      633 2023-04-05 12:44:15.398476 pureml-0.3.0/pureml/evaluate/metrics/accuracy.py
+-rw-r--r--   0        0        0        0 2023-04-05 12:44:15.398476 pureml-0.3.0/pureml/evaluate/metrics/base.py
+-rw-r--r--   0        0        0      673 2023-04-05 12:44:15.402476 pureml-0.3.0/pureml/evaluate/metrics/confusion_matrix.py
+-rw-r--r--   0        0        0      699 2023-04-05 12:44:15.406476 pureml-0.3.0/pureml/evaluate/metrics/f1.py
+-rw-r--r--   0        0        0      629 2023-04-05 12:44:15.406476 pureml-0.3.0/pureml/evaluate/metrics/mae.py
+-rw-r--r--   0        0        0      686 2023-04-05 12:44:15.410476 pureml-0.3.0/pureml/evaluate/metrics/mse.py
+-rw-r--r--   0        0        0      802 2023-04-05 12:44:15.418476 pureml-0.3.0/pureml/evaluate/metrics/precision.py
+-rw-r--r--   0        0        0      787 2023-04-05 12:44:15.434476 pureml-0.3.0/pureml/evaluate/metrics/recall.py
+-rw-r--r--   0        0        0     1225 2023-04-05 12:44:15.434476 pureml-0.3.0/pureml/evaluate/metrics/roc_auc.py
+-rw-r--r--   0        0        0      654 2023-04-05 12:44:15.434476 pureml-0.3.0/pureml/evaluate/regression.py
+-rw-r--r--   0        0        0        0 2023-02-10 14:59:50.954225 pureml-0.3.0/pureml/lineage/__init__.py
+-rw-r--r--   0        0        0        0 2023-02-10 14:59:50.954225 pureml-0.3.0/pureml/lineage/data/__init__.py
+-rw-r--r--   0        0        0     2852 2023-04-05 12:44:15.434476 pureml-0.3.0/pureml/lineage/data/create_lineage.py
+-rw-r--r--   0        0        0        0 2023-03-15 11:32:07.345247 pureml-0.3.0/pureml/package/__init__.py
+-rw-r--r--   0        0        0     4251 2023-04-05 12:44:15.466477 pureml-0.3.0/pureml/package/docker.py
+-rw-r--r--   0        0        0     5913 2023-04-05 12:44:15.486478 pureml-0.3.0/pureml/package/fastapi.py
+-rw-r--r--   0        0        0      876 2023-03-15 11:32:07.429247 pureml-0.3.0/pureml/packaging/__init__.py
+-rw-r--r--   0        0        0      496 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/errors.py
+-rw-r--r--   0        0        0     2245 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_framework.py
+-rw-r--r--   0        0        0        0 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/__init__.py
+-rw-r--r--   0        0        0      973 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/catboost.py
+-rw-r--r--   0        0        0     1103 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/custom.py
+-rw-r--r--   0        0        0      965 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/keras.py
+-rw-r--r--   0        0        0      976 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/lightgbm.py
+-rw-r--r--   0        0        0     1075 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/pytorch.py
+-rw-r--r--   0        0        0     1146 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/pytorch_tabnet.py
+-rw-r--r--   0        0        0     2163 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/sklearn.py
+-rw-r--r--   0        0        0     1028 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/tensorflow.py
+-rw-r--r--   0        0        0     1021 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/model_packaging/xgboost.py
+-rw-r--r--   0        0        0     4006 2023-03-15 11:32:07.457247 pureml-0.3.0/pureml/packaging/packaging.py
+-rw-r--r--   0        0        0     1381 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/packaging/packaging_utils.py
+-rw-r--r--   0        0        0        0 2023-03-15 11:32:07.457247 pureml-0.3.0/pureml/predictor/__init__.py
+-rw-r--r--   0        0        0      778 2023-03-15 11:32:07.545248 pureml-0.3.0/pureml/predictor/predictor.py
+-rw-r--r--   0        0        0      365 2023-04-05 12:44:15.486478 pureml-0.3.0/pureml/schema/__init__.py
+-rw-r--r--   0        0        0      897 2023-04-06 11:08:34.088115 pureml-0.3.0/pureml/schema/backend.py
+-rw-r--r--   0        0        0      350 2023-04-05 12:44:15.486478 pureml-0.3.0/pureml/schema/config.py
+-rw-r--r--   0        0        0      330 2023-03-15 11:32:07.669248 pureml-0.3.0/pureml/schema/dataset.py
+-rw-r--r--   0        0        0      474 2023-04-05 12:44:15.510478 pureml-0.3.0/pureml/schema/log.py
+-rw-r--r--   0        0        0      396 2023-03-15 11:32:07.681248 pureml-0.3.0/pureml/schema/model.py
+-rw-r--r--   0        0        0     1042 2023-04-05 12:44:15.510478 pureml-0.3.0/pureml/schema/packaging.py
+-rw-r--r--   0        0        0     2528 2023-03-15 11:32:07.685248 pureml-0.3.0/pureml/schema/paths.py
+-rw-r--r--   0        0        0     1048 2023-04-05 12:44:15.650482 pureml-0.3.0/pureml/schema/predict.py
+-rw-r--r--   0        0        0      385 2023-03-15 11:32:07.733248 pureml-0.3.0/pureml/schema/singleton.py
+-rw-r--r--   0        0        0      243 2023-04-05 12:44:15.510478 pureml-0.3.0/pureml/schema/storage.py
+-rw-r--r--   0        0        0      177 2023-03-15 11:32:07.789248 pureml-0.3.0/pureml/schema/types.py
+-rw-r--r--   0        0        0       66 2023-04-05 12:44:15.510478 pureml-0.3.0/pureml/settings/__init__.py
+-rw-r--r--   0        0        0      278 2023-04-05 12:44:15.510478 pureml-0.3.0/pureml/settings/backend.py
+-rw-r--r--   0        0        0      376 2023-04-05 12:44:15.510478 pureml-0.3.0/pureml/settings/storage.py
+-rw-r--r--   0        0        0        0 2023-01-10 08:50:08.016554 pureml-0.3.0/pureml/utils/__init__.py
+-rw-r--r--   0        0        0     1751 2023-04-05 12:44:15.510478 pureml-0.3.0/pureml/utils/config.py
+-rw-r--r--   0        0        0     2234 2023-03-15 11:32:07.789248 pureml-0.3.0/pureml/utils/constants.py
+-rw-r--r--   0        0        0     2998 2023-03-15 11:32:07.825248 pureml-0.3.0/pureml/utils/hash.py
+-rw-r--r--   0        0        0      522 2023-02-10 14:59:51.046215 pureml-0.3.0/pureml/utils/log_utils.py
+-rw-r--r--   0        0        0     1985 2023-03-15 11:32:07.865248 pureml-0.3.0/pureml/utils/package.py
+-rw-r--r--   0        0        0    12921 2023-04-05 12:48:59.157035 pureml-0.3.0/pureml/utils/pipeline.py
+-rw-r--r--   0        0        0     2868 2023-04-05 12:44:15.642481 pureml-0.3.0/pureml/utils/predict.py
+-rw-r--r--   0        0        0      815 2023-02-10 14:59:51.066213 pureml-0.3.0/pureml/utils/readme.py
+-rw-r--r--   0        0        0     1393 2023-04-05 12:44:15.542479 pureml-0.3.0/pureml/utils/resources.py
+-rw-r--r--   0        0        0      137 2023-01-10 08:50:08.036553 pureml-0.3.0/pureml/utils/source_code.py
+-rw-r--r--   0        0        0        0 2023-03-15 11:32:08.013249 pureml-0.3.0/pureml/utils/types.py
+-rw-r--r--   0        0        0      698 2023-03-15 11:32:08.013249 pureml-0.3.0/pureml/utils/version_utils.py
+-rw-r--r--   0        0        0     1903 2023-04-07 14:26:49.418937 pureml-0.3.0/pyproject.toml
+-rw-r--r--   0        0        0    13246 1970-01-01 00:00:00.000000 pureml-0.3.0/PKG-INFO
```

### Comparing `pureml-0.2.3/README.md` & `pureml-0.3.0/README.md`

 * *Files 9% similar despite different names*

```diff
@@ -1,33 +1,20 @@
-<h1 align="center">
-  <a href="https://pureml.com">
-    <img
-      align="center"
-      alt="PureML"
-      src="https://github.com/PureML-Inc/PureML/blob/main/assets/coverImg.jpeg"
-      style="width:100%;"
-    />
-  </a>
-</h1>
-
+[![PureML](/assets/SDKCoverImg.png)](https://pureml.com)
 
-
-
-<div align="center">
+<h align="center">
 
 # Track, version, compare and review your data and models.
 
-</div>
-
+</h>
 
 # ⛳ Quick Access
 
 <p align="center">
   <a
-    href="https://docs.pureml.com"
+    href="https://pureml.mintlify.app"
   ><b>Documentation</b></a>
   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
   <a
     href="https://www.youtube.com/watch?v=HdzLFEWS4s8&t=1s"
   ><b>Watch Demo</b></a>
   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
   <a
@@ -40,20 +27,17 @@
   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
   <a
     href="https://app.pureml.com/auth/signup"
   ><b>Sign Up for free</b></a>
 
 </p>
 
-
-
 </br>
 </br>
 
-
 <div align="center">
   <a
     href="https://pypi.org/project/pureml/"
   >
     <img alt="PyPi" src="https://img.shields.io/pypi/v/pureml?color=green&logo=pureml" />
   </a>
   &nbsp;
@@ -95,24 +79,19 @@
   &nbsp;
   <a
     href="https://pypi.org/project/pureml/"
   >
     <img alt="Coverage" src="https://img.shields.io/github/stars/pureml-inc/pureml?style=social">
   </a>
 
-
-
 </div>
 
-
 </br>
 </br>
 
-
-
 # 💎 Intro
 
 PureML is an open-source version control for machine learning.
 
 1. [Quick start](#quick-start)
 1. [How it works](#how-it-works)
 1. [Demo](#demo)
@@ -124,64 +103,68 @@
 
 <br />
 
 # ⏱ Quick start
 
 You can install and run PureML using `pip`.
 
-
 Install PureML
+
 ```bash
 pip install pureml
 ```
 
 <br />
 
 # 📋 How it works
+
 Just add a few lines of code. You don't need to change the way you work.
 
 PureML is a Python library that uploads metadata to S3.
 
 ### Generating Data Lineage
 
 1. Load Data
+
 ```python
 @load_data(name='loading data')
 def loading_data():
-    
+
     return pd.read_csv('churn.csv')
 ```
 
 2. Transform Data
+
 ```python
 @transformer(name='fill missing values')
 def fill_missing_values(df):
     return df.fillna()
-    
+
 
 @transformer(name='encode ordinal')
 def encode_ordinal(df):
     col_ord = ['state', 'phone number']
     df_ord = df[col_ord]
-    feat = OrdinalEncoder().fit_transform(df_ord)    
+    feat = OrdinalEncoder().fit_transform(df_ord)
     df[col_ord] = feat
-    
+
     return df
 
 @transformer(name='encode binary')
 def encode_binary(df):
 
     df['voice mail plan'] = df['voice mail plan'].map({'yes':1, 'no':0})
     df['international plan'] = df['international plan'].map({'yes':1, 'no':0})
     df['churn'] = df['churn'].map({True:1, False:0})
 
     return df
 ```
 
 3. Register Dataset
+
 ```python
 @dataset(name='telecom churn', parent='encode binary')
 def build_dataset():
     df = loading_data()
 
     df = fill_missing_values(df)
 
@@ -209,119 +192,113 @@
 
 # 💻 Demo
 
 ### Live demo
 
 Build and run a PureML project to create data lineage and a model with our <b>[demo colab link](https://colab.research.google.com/drive/1LlrpaKiREwgesaRcnwkJP-w2MPesXf1t?usp=sharing)</b>.
 
-
 ### Demo video (2 min)
+
 PureML quick start demo
 
 [![PureML Demo Video](https://img.youtube.com/vi/HdzLFEWS4s8/0.jpg)](https://www.youtube.com/watch?v=HdzLFEWS4s8 "PureML Demo Video")
 
-
-
 <sub><i>Click the image to play video</i></sub>
 
 <br />
 
-
 # 📍 [Main Features](https://docs.pureml.com/)
-|   |   |
-| --- | --- |
-| Data Lineage | Automatic generation of data lineage|
-| Dataset Versioning | Object-based Automatic Semantic Versioning of datasets |
-| Model Versioning | Object-based Automatic Semantic Versioning of models |
-| Comparision | Comparing different versions of models or datasets
-| Branches (*Coming Soon*) | Separation between experimentation and production ready models using branches |
-| Review (*Coming Soon*) | Review and approve models, and datasets to production ready branch|
 
-<br />
+|                          |                                                                               |
+| ------------------------ | ----------------------------------------------------------------------------- |
+| Data Lineage             | Automatic generation of data lineage                                          |
+| Dataset Versioning       | Object-based Automatic Semantic Versioning of datasets                        |
+| Model Versioning         | Object-based Automatic Semantic Versioning of models                          |
+| Comparision              | Comparing different versions of models or datasets                            |
+| Branches (_Coming Soon_) | Separation between experimentation and production ready models using branches |
+| Review (_Coming Soon_)   | Review and approve models, and datasets to production ready branch            |
 
+<br />
 
 # 🔮 Core design principles
 
-|   |   |
-| --- | --- |
-| Easy developer experience | An intuitive open source package aimed to bridge the gaps in data science teams |
-| Engineering best practices built-in | Integrating PureML functionalities in your code doesnot disrupt your workflow |
-| Object Versioning | A reliable object versioning mechanism to track changes to your datasets, and models |
-| Data is a first-class citizen | Your data is secure. It will never leave your system. |
-| Reduce Friction | Have access to operations performed on data using data lineage without having to spend time on lengthy meetings |
-
-
+|                                     |                                                                                                                 |
+| ----------------------------------- | --------------------------------------------------------------------------------------------------------------- |
+| Easy developer experience           | An intuitive open source package aimed to bridge the gaps in data science teams                                 |
+| Engineering best practices built-in | Integrating PureML functionalities in your code doesnot disrupt your workflow                                   |
+| Object Versioning                   | A reliable object versioning mechanism to track changes to your datasets, and models                            |
+| Data is a first-class citizen       | Your data is secure. It will never leave your system.                                                           |
+| Reduce Friction                     | Have access to operations performed on data using data lineage without having to spend time on lengthy meetings |
 
 <br />
 
 # ⚙ Core abstractions
 
 These are the fundamental concepts that PureML uses to operate.
 
-|   |   |
-| --- | --- |
-| [Project](https://docs.pureml.com/docs/projects/about_projects) | A data science project. This is where you store datasets, models, and their related objects. It is similar to a github repository with object storage.|
-| [Lineage](https://docs.pureml.com/docs/data/register_data_pipeline) | Contains a series of transformations performed on data to generate a dataset.|
-| Data Versioning | Versioning of the data should be comprehensible to the user and should encapsulate the changes in the data, its creation mechanism, among others.|
-| Model Versioning| Versioning of the model should be comprehensible to the user and should encapuslate the changes in training data, model architecture, hyper parameters.|
-| Fetch | This functionality is used to fetch registered Models, and Datasets.|
-
+|                                                                     |                                                                                                                                                         |
+| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| [Project](https://docs.pureml.com/docs/projects/about_projects)     | A data science project. This is where you store datasets, models, and their related objects. It is similar to a github repository with object storage.  |
+| [Lineage](https://docs.pureml.com/docs/data/register_data_pipeline) | Contains a series of transformations performed on data to generate a dataset.                                                                           |
+| Data Versioning                                                     | Versioning of the data should be comprehensible to the user and should encapsulate the changes in the data, its creation mechanism, among others.       |
+| Model Versioning                                                    | Versioning of the model should be comprehensible to the user and should encapuslate the changes in training data, model architecture, hyper parameters. |
+| Fetch                                                               | This functionality is used to fetch registered Models, and Datasets.                                                                                    |
 
 <br />
 
 # 🤝 Why to get involved
+
 Version control is much more common in software than in machine learning. So why isn’t everyone using Git? Git doesn’t work well with machine learning. It can’t handle large files, it can’t handle key/value metadata like metrics, and it can’t record information automatically from inside a training script.
 
 GitHub wasn’t designed with data as a core project component. This along with a number of other differences between AI and more traditional software projects makes GitHub a bad fit for artificial intelligence, contributing to the reproducibility crisis in machine learning.
 
 From manually tracking models to git based versioning systems that do not follow an intuitive versioning mechanism, there is no standardized way to track objects. Using these mechanisms, it is hard enough to track or get your model from a month ago running, let alone of a teammates!
 
 We are trying to build a version control system for machine learning objects. A mechanism that is object dependant and intuitive for users.
 
 Lets build this together. If you have faced this issue or have worked out a similar solution for yourself, please join us to help build a better system for everyone.
 
 <br />
 
-
 # 🧮 Tutorials
 
 - [Registering Data lineage](https://docs.pureml.com/docs/data/register_data_pipeline)
 - [Registering models](https://docs.pureml.com/docs/models/register_models)
 - [Quick Start: Tabular](https://docs.pureml.com/docs/get-started/quickstart_tabular)
 - [Quick Start: Computer Vision](https://docs.pureml.com/docs/get-started/quickstart_cv)
 - [Quick Start: NLP](https://docs.pureml.com/docs/get-started/quickstart_nlp)
 - [Logging](https://docs.pureml.com/docs/log/overview)
 
-
 <br />
 
 # 🐞 Reporting Bugs
+
 To report any bugs you have faced while using PureML package, please
+
 1. Report it in [Discord](https://discord.gg/xNUHt9yguJ) channel
 1. Open an [issue](https://github.com/PureML-Inc/PureML/issues)
 
 <br />
 
 # ⌨ Contributing and Developing
+
 Lets work together to improve the features for everyone. For more details, please look at out [Contributing Guide](./CONTRIBUTING.md)
 
 Work with mutual respect.
 
-
 <br />
 
 # 👨‍👩‍👧‍👦 Community
+
 To get quick updates, feature release for PureML follow us on
-|   |
+| |
 | --- |
 | [<img alt="Twitter" height="20" src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/getPureML) |
 [<img alt="LinkedIn" height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/company/pureml-inc/) |
 | [<img alt="GitHub" height="20" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/PureML-Inc/PureML) |
 | [<img alt="GitHub" height="20" src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" />](https://discord.gg/DBvedzGu) |
 
-
 # 📄 License
-See the [Apache-2.0](./License) file for licensing information.
-
 
+See the [Apache-2.0](./License) file for licensing information.
 
 <br />
```

### Comparing `pureml-0.2.3/pureml/cli/__init__.py` & `pureml-0.3.0/pureml/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/cli/auth.py` & `pureml-0.3.0/pureml/components/log/predict.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,222 +1,231 @@
+import json
 import os
-from pathlib import Path
-from typing import Optional
-import jwt
+from urllib.parse import urljoin
+
+import numpy as np
 import requests
-import typer
-from rich import print
-from rich.syntax import Syntax
+from joblib import Parallel, delayed
 
-from pureml.components import get_org_id, get_token
-from rich.console import Console
-from rich.table import Table
-from urllib.parse import urljoin
-import json
-from pureml.schema import BackendSchema, PathSchema
+from pureml.utils.pipeline import add_pred_to_config
+from pureml.schema import (
+    PathSchema,
+    BackendSchema,
+    StorageSchema,
+    LogSchema,
+    ConfigKeys,
+)
+from rich import print
+from . import get_org_id, get_token, pip_requirement, resources
+import shutil
+from pureml.utils.version_utils import parse_version_label
+from pureml.utils.config import reset_config
 
 
 path_schema = PathSchema().get_instance()
 backend_schema = BackendSchema().get_instance()
-app = typer.Typer()
+post_key_predict = LogSchema().key.predict.value
+post_key_requirements = LogSchema().key.requirements.value
+post_key_resources = LogSchema().key.resources.value
+config_keys = ConfigKeys
+storage = StorageSchema().get_instance()
+
+
+def post_predict(file_paths, model_name: str, model_branch: str, model_version: str):
+    user_token = get_token()
+    org_id = get_org_id()
 
+    url = "org/{}/model/{}/branch/{}/version/{}/logfile".format(
+        org_id, model_name, model_branch, model_version
+    )
+    url = urljoin(backend_schema.BASE_URL, url)
 
-def save_auth(org_id: str = None, access_token: str = None, email=None):
-    token_path = path_schema.PATH_USER_TOKEN
+    headers = {"Authorization": "Bearer {}".format(user_token)}
 
-    token_dir = os.path.dirname(token_path)
-    os.makedirs(token_dir, exist_ok=True)
+    files = []
+    for file_name, file_path in file_paths.items():
+        # print("filename", file_name)
 
-    token = {"org_id": org_id, "accessToken": access_token, "email": email}
+        if os.path.isfile(file_path):
+            files.append(("file", (file_name, open(file_path, "rb"))))
 
-    token = json.dumps(token)
+        else:
+            print("[bold red] Predict", file_name, "doesnot exist at the given path")
 
-    with open(token_path, "w") as token_file:
-        token_file.write(token)
+    data = {
+        "data": file_paths,
+        "key": post_key_predict,
+        "storage": storage.STORAGE,
+    }
 
-    print("[green]User token is stored")
+    # data = json.dumps(data)
 
+    response = requests.post(url, data=data, files=files, headers=headers)
 
-@app.command()
-def details():
-    token = get_token()
-    org_id = get_org_id()
+    if response.ok:
+        print(f"[bold green]Predict Function has been registered!")
+        reset_config(key=config_keys.pred_function.value)
 
-    print("Org Id: ", org_id)
-    print("Access Token: ", token)
+    else:
+        print(f"[bold red]Predict Function has not been registered!")
 
+    return response
 
-@app.callback()
-def callback():
-    """
-    Authentication user command
-
-    Use with status, signup, login or logout option
-
-    status - Checks current authenticated user
-    signup - Creates new user
-    login - Logs in user
-    logout - Logs out user
-    """
-
-
-@app.command()
-def signup():
-    print("\n[bold]Create a new account[/bold]\n")
-    email: str = typer.prompt("Enter new email")
-    handle: str = typer.prompt("Enter new user handle")
-    name: str = typer.prompt("Enter new user name")
-    password: str = typer.prompt(
-        "Enter new password", confirmation_prompt=True, hide_input=True
-    )
-    # organization_id: str = typer.prompt("Enter Organization id")
-    # data = {"email": email, "password": password, "org": organization_id}
-    data = {"email": email, "password": password, "handle": handle, "name": name}
 
-    url_path_1 = "user/signup"
-    url = urljoin(backend_schema.BASE_URL, url_path_1)
+def add(label: str = None, paths: dict = None) -> str:
 
-    response = requests.post(url, json=data)
+    model_name, model_branch, model_version = parse_version_label(label)
 
-    if not response.ok:
-        print(f"[bold red]Could not create account! Please try again later")
-        return
-    print(
-        f"[bold green]Successfully created your account! You can now login using ```pure auth login```"
-    )
+    pred_path = paths[post_key_predict]
 
+    if post_key_requirements in paths.keys():
+        pip_requirement.add(label, path=paths[post_key_requirements])
 
-def list_org(access_token):
+    if post_key_resources in paths.keys():
+        resources.add(label, path=paths[post_key_resources])
 
-    url_path = "org"
-    url = urljoin(backend_schema.BASE_URL, url_path)
+    file_paths = {post_key_predict: pred_path}
+
+    add_pred_to_config(
+        values=pred_path,
+        model_name=model_name,
+        model_branch=model_branch,
+        model_version=model_version,
+    )
+
+    if (
+        model_name is not None
+        and model_version is not None
+        and model_version is not None
+    ):
+        response = post_predict(
+            file_paths=file_paths,
+            model_name=model_name,
+            model_branch=model_branch,
+            model_version=model_version,
+        )
+
+        print(response.text)
+
+    # return response.text
+
+
+def details(label: str):
+    model_name, model_branch, model_version = parse_version_label(label)
+    user_token = get_token()
+    org_id = get_org_id()
+
+    url = "org/{}/model/{}/branch/{}/version/{}/log".format(
+        org_id, model_name, model_branch, model_version
+    )
+    url = urljoin(backend_schema.BASE_URL, url)
 
     headers = {
         "accept": "application/json",
-        "Authorization": "Bearer {}".format(access_token),
+        "Authorization": "Bearer {}".format(user_token),
     }
 
     response = requests.get(url, headers=headers)
 
     if response.ok:
-        print()
-        print("[bold green]Select the Organization from the list below!")
-        org_all = response.json()["data"]
-
-        console = Console()
-
-        table = Table("User Handle", "Organization Id")
-        for org in org_all:
-            table.add_row(org["org"]["handle"], org["org"]["uuid"])
+        # T-1161 standardize api response to contains Models as a list
+        response_text = response.json()
+        details = response_text["data"]
 
-        console.print(table)
-        print()
-
-    else:
-        print("[bold red]Unable to fetch existing Organizations!")
+        # print(model_details)
 
+        return details
 
-def check_org_status(access_token):
+    else:
+        print(f"[bold red]Unable to fetch Predict!")
+        return
 
-    org_id: str = typer.prompt("Enter your Org Id")
 
-    url_path = "org/id/{}".format(org_id)
-    url = urljoin(backend_schema.BASE_URL, url_path)
+def fetch(label: str):
+    model_name, model_branch, model_version = parse_version_label(label)
 
-    headers = {
-        "accept": "application/json",
-        "Authorization": "Bearer {}".format(access_token),
-    }
+    user_token = get_token()
+    org_id = get_org_id()
 
-    response = requests.get(url, headers=headers)
+    def fetch_predict(file_details):
 
-    if response.ok:
-        print("[bold green]Organization Exists!")
-        return org_id
-    else:
-        print("[bold red]Organization doesnot Exists!")
-        return None
+        file_name, url = file_details
 
+        save_path = os.path.join(path_schema.PATH_PREDICT_DIR, file_name)
+        # print("save path", save_path)
 
-@app.command()
-def login():
+        headers = {
+            "Content-Type": "application/x-www-form-urlencoded",
+            "Authorization": "Bearer {}".format(user_token),
+        }
 
-    print(f"\n[bold]Enter your credentials to login[/bold]\n")
-    email: str = typer.prompt("Enter your email")
-    password: str = typer.prompt("Enter your password", hide_input=True)
-    data = {"email": email, "password": password}
+        # print("figure url", url)
 
-    url_path = "user/login"
-    url = urljoin(backend_schema.BASE_URL, url_path)
+        response = requests.get(url)
 
-    response = requests.post(url, json=data)
+        # print(response.status_code)
 
-    if response.ok:
-        token = response.text
-        token = json.loads(token)["data"][0]
+        if response.ok:
+            print("[bold green] predict file {} has been fetched".format(file_name))
 
-        access_token = token["accessToken"]
-        email = token["email"]
+            save_dir = os.path.dirname(save_path)
 
-        list_org(access_token=access_token)
+            os.makedirs(save_dir, exist_ok=True)
 
-        org_id = check_org_status(access_token=access_token)
+            predict_bytes = response.content
 
-        if org_id is not None:
+            open(save_path, "wb").write(predict_bytes)
 
-            save_auth(org_id=org_id, access_token=access_token, email=email)
-            print(f"[bold green]Successfully logged in to your account!")
+            # print(
+            #     "[bold green] predict file {} has been stored at {}".format(
+            #         file_name, save_path
+            #     )
+            # )
 
-            print("org_id:", org_id)
-            print("accessToken:", access_token)
+            return response.text
         else:
-            print(f"[bold red]Unable to login to your account!")
+            print("[bold red] Unable to fetch the predict function")
 
-    else:
-        print(f"[bold red]Unable to login to your account!")
+            return response.text
 
+    predict_details = details(label=label)
 
-# @app.command()
-# def status():
-#     print()
-#     path = PATH_USER_TOKEN
+    if predict_details is None:
+        return
 
-#     curr_path = Path(__file__).parent.resolve()
-#     if os.path.exists(path):
-#         token = open(path, "r").read()
-#         public_key = open(f"{curr_path}/public.pem", "rb").read()
-#         payload = jwt.decode(token, public_key, algorithms=["RS256"])
-#         print(f"[bold green]You are currently logged in as {payload['email']}")
-#     else:
-#         print("[bold red]You are not logged in!")
+    # pred_urls = give_predict_urls(details=predict_details)
+    pred_urls = give_predict_url(details=predict_details, key=post_key_predict)
 
+    if len(pred_urls) == 1:
 
-def statusHelper():
-    path = path_schema.PATH_USER_TOKEN
+        res_text = fetch_predict(pred_urls[0])
 
-    if os.path.exists(path):
-        return open(path, "r").read()
     else:
-        return None
+        res_text = Parallel(n_jobs=-1)(
+            delayed(fetch_predict)(pred_url) for pred_url in pred_urls
+        )
+
+
+def give_predict_url(details, key: str):
+    predict_paths = []
+    # file_url = None
+    source_path = None
+    file_url = None
+    # print(details)
+
+    if details is not None:
+
+        for det in details:
+            # print(det["key"])
+            if det["key"] == key:
+                source_path = det["key"]
+                file_url = det["data"]
+                source_path = ".".join([source_path, "py"])
+                # source_path = os.path.join(path_schema.PATH_PREDICT_DIR, source_path)
+                predict_paths.append([source_path, file_url])
 
+                # print(source_path, file_url)
 
-def auth_validate():
-    token = statusHelper()
-    if not token:
-        print("[bold red]You are not logged in!")
-        raise typer.Exit()
-    return token
-
-
-# @app.command()
-# def logout():
-#     print()
-#     path = PATH_USER_TOKEN
-
-#     if os.path.exists(path):
-#         os.remove(path)
-#         print(f"[bold yellow]Successfully logged out!")
-#     else:
-#         print(f"[bold red]You are not logged in!")
+                return predict_paths
+    print("[bold red] Unable to find the predict file")
 
-if __name__ == "__main__":
-    app()
+    return predict_paths
```

### Comparing `pureml-0.2.3/pureml/cli/main.py` & `pureml-0.3.0/pureml/cli/main.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/components/__init__.py` & `pureml-0.3.0/pureml/components/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,10 @@
 import os, json
 from pureml.schema import PathSchema
 
-
 path_schema = PathSchema().get_instance()
 
 
 def get_token():
     """It checks if the token exists in the user's home directory. If it does, it returns the token. If it
     doesn't, it returns None
```

### Comparing `pureml-0.2.3/pureml/components/arrays.py` & `pureml-0.3.0/pureml/components/log/arrays.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/components/artifacts.py` & `pureml-0.3.0/pureml/components/log/artifacts.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/components/audio.py` & `pureml-0.3.0/pureml/components/log/audio.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/components/auth.py` & `pureml-0.3.0/pureml/components/auth.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/components/dataset.py` & `pureml-0.3.0/pureml/components/dataset.py`

 * *Files 9% similar despite different names*

```diff
@@ -2,42 +2,43 @@
 import os
 from urllib.parse import urljoin
 import time
 import joblib
 import pandas as pd
 import requests
 
-# from pureml.utils.constants import (
-#     BASE_URL,
-#     PATH_DATASET_DIR,
-#     PATH_DATASET_README,
-#     STORAGE,
-# )
-from pureml.schema import DatasetSchema, StorageSchema
+from pureml.schema import DatasetSchema, StorageSchema, ConfigKeys
 from pureml.utils.hash import generate_hash_for_file
 from pureml.utils.readme import load_readme
 from rich import print
 
 from . import get_org_id, get_token
+from pureml.utils.version_utils import parse_version_label
+from pureml.utils.config import reset_config
 
+config_keys = ConfigKeys
+storage = StorageSchema().get_instance()
+
+
+def init_branch(label: str):
+    name, branch, _ = parse_version_label(label)
 
-def init_branch(branch: str, dataset_name: str):
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
-    url = "org/{}/dataset/{}/branch/create".format(org_id, dataset_name)
+    url = "org/{}/dataset/{}/branch/create".format(org_id, name)
     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/json",
         "Authorization": "Bearer {}".format(user_token),
     }
 
-    data = {"dataset_name": dataset_name, "branchName": branch}
+    data = {"dataset_name": name, "branchName": branch}
 
     data = json.dumps(data)
 
     response = requests.post(url, data=data, headers=headers)
 
     if response.ok:
         print(f"[bold green]Branch has been created!")
@@ -46,45 +47,49 @@
 
     else:
         print(f"[bold red]Branch has not been created!")
 
         return False
 
 
-def check_dataset_hash(hash: str, name: str, branch: str):
+def check_dataset_hash(hash: str, label: str):
+
+    name, branch, _ = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
-    url = "org/{}/dataset/{}/branch/{}/hash-status".format(org_id, branch, name)
+    url = "org/{}/dataset/{}/branch/{}/hash-status".format(org_id, name, branch)
     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
     headers = {"Authorization": "Bearer {}".format(user_token)}
 
     data = {"hash": hash, "branch": branch}
 
     data = json.dumps(data)
 
     response = requests.post(url, data=data, headers=headers)
 
     hash_exists = False
 
     if response.ok:
-        hash_exists = response.json()["data"]
+        hash_exists = response.json()["data"][0]
 
     return hash_exists
 
 
-def branch_details(branch: str, dataset_name: str):
+def branch_details(label: str):
+    name, branch, _ = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
-    url = "org/{}/dataset/{}/branch/{}".format(org_id, dataset_name, branch)
+    url = "org/{}/dataset/{}/branch/{}".format(org_id, name, branch)
     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
@@ -101,31 +106,32 @@
         return details
 
     else:
         print(f"[bold red]Branch details details have not been found")
         return
 
 
-def branch_status(branch: str, dataset_name: str):
+def branch_status(label: str):
 
-    details = branch_details(branch=branch, dataset_name=dataset_name)
+    details = branch_details(label=label)
 
     if details:
         return True
     else:
         return False
 
 
-def branch_delete(branch: str, dataset_name: str) -> str:
+def branch_delete(label: str) -> str:
+    name, branch, _ = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
-    url = "org/{}/dataset/{}/branch/{}/delete".format(org_id, dataset_name, branch)
+    url = "org/{}/dataset/{}/branch/{}/delete".format(org_id, name, branch)
     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
@@ -136,21 +142,23 @@
 
     else:
         print(f"[bold red]Unable to delete Model branch")
 
     return response.text
 
 
-def branch_list(dataset_name: str) -> str:
+def branch_list(label: str) -> str:
+
+    name, _, _ = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
-    url = "org/{}/dataset/{}/branch".format(org_id, dataset_name)
+    url = "org/{}/dataset/{}/branch".format(org_id, name)
     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
@@ -201,15 +209,18 @@
         return dataset_list
     else:
         print(f"[bold red]Unable to obtain the list of dataset!")
 
     return
 
 
-def init(name: str, readme: str = None, branch: str = None):
+def init(label: str, readme: str = None):
+
+    name, branch, _ = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
     if readme is None:
         readme = dataset_schema.PATH_DATASET_README
 
@@ -261,35 +272,29 @@
 
     # dataset.to_parquet(save_path)
     joblib.dump(dataset, save_path)
 
     return save_path
 
 
-def register(
-    dataset,
-    name: str,
-    lineage,
-    branch: str,
-    is_empty: bool = False,
-    storage: str = StorageSchema().STORAGE,
-) -> str:
+def register(dataset, label: str, lineage, is_empty: bool = False) -> str:
     """The function takes in a dataset, a name and a version and saves the dataset locally, then uploads the
     dataset to the PureML server
 
     Parameters
     ----------
     dataset
         The dataset you want to register
     name : str
         The name of the dataset.
     version: str, optional
         The version of the dataset.
 
     """
+    name, branch, _ = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
     dataset_path = save_dataset(dataset, name)
     name_with_ext = dataset_path.split("/")[-1]
@@ -298,42 +303,40 @@
         file_path=dataset_path, name=name, branch=branch, is_empty=is_empty
     )
 
     if is_empty:
         dataset_path = save_dataset(dataset=None, name=name)
         name_with_ext = dataset_path.split("/")[-1]
 
-    dataset_exists = dataset_status(name)
+    dataset_exists = dataset_status(label)
     # print('Dataset status', dataset_exists)
 
     if not dataset_exists:
-        dataset_created = init(name=name, branch=branch)
+        dataset_created = init(label=label)
         # print('dataset_created', dataset_created)
         if not dataset_created:
             print("[bold red] Unable to register the dataset")
             return False, dataset_hash, None
     else:
         print("[bold green] Connected to Dataset")
 
-    branch_exists = branch_status(branch=branch, dataset_name=name)
+    branch_exists = branch_status(label=label)
     # print('Branch status', branch_exists)
 
     if not branch_exists:
-        branch_created = init_branch(branch=branch, dataset_name=name)
+        branch_created = init_branch(label=label)
         # print('branch_created', branch_created)
 
         if not branch_created:
             print("[bold red] Unable to register the dataset")
             return False, dataset_hash, None
     else:
         print("[bold green] Connected to Branch")
 
-    dataset_exists_remote = check_dataset_hash(
-        hash=dataset_hash, name=name, branch=branch
-    )
+    dataset_exists_remote = check_dataset_hash(hash=dataset_hash, label=label)
 
     if dataset_exists_remote:
 
         print(f"[bold red]Dataset already exists. Not registering a new version!")
         return True, dataset_hash, "latest"
     else:
 
@@ -351,15 +354,15 @@
 
         data = {
             "name": name,
             "branch": branch,
             "hash": dataset_hash,
             "lineage": lineage,
             "is_empty": is_empty,
-            "storage": storage,
+            "storage": storage.STORAGE,
         }
 
         # data = json.dumps(data)
 
         response = requests.post(url, files=files, data=data, headers=headers)
 
         if response.ok:
@@ -370,14 +373,16 @@
                 print("Version: ", dataset_version)
 
                 if is_empty:
                     print(f"[bold green]Lineage has been registered!")
                 else:
                     print(f"[bold green]Dataset and lineage have been registered!")
 
+                # reset_config(key=config_keys.dataset.value)
+
             except Exception as e:
                 print(
                     "[bold red] Incorrect json response. Dataset has not been registered"
                 )
                 print(e)
                 dataset_version = None
 
@@ -385,26 +390,28 @@
         else:
             print(f"[bold red]Dataset has not been registered!")
             print(response.text)
 
             return True, dataset_hash, None
 
 
-def dataset_status(name: str):
+def dataset_status(label: str):
+
+    name, _, _ = parse_version_label(label)
 
-    dataset_details = details(name=name)
+    dataset_details = details(label=label)
 
     if dataset_details:
         return True
     else:
         return False
 
 
 def details(
-    name: str,
+    label: str,
 ):
     """It fetches the details of a dataset.
 
     Parameters
     ----------
     name : str
         The name of the dataset
@@ -412,14 +419,16 @@
         The version of the dataset
     Returns
     -------
         The details of the dataset.
 
     """
 
+    name, _, _ = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
     url = "org/{}/dataset/{}".format(org_id, name)
     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
@@ -438,29 +447,31 @@
         return dataset_details
 
     else:
         print(f"[bold red]Dataset details have not been found")
         return
 
 
-def version_details(name: str, branch: str, version: str = "latest"):
+def version_details(label: str):
     """It fetches the details of a dataset.
 
     Parameters
     ----------
     name : str
         The name of the dataset
     version: str
         The version of the dataset
     Returns
     -------
         The details of the dataset.
 
     """
 
+    name, branch, version = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
     url = "org/{}/dataset/{}/branch/{}/version/{}".format(org_id, name, branch, version)
     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
@@ -480,15 +491,15 @@
         return dataset_details
 
     else:
         print(f"[bold red]Dataset details have not been found")
         return
 
 
-def fetch(name: str, branch: str, version: str = "latest"):
+def fetch(label: str):
     """This function fetches a dataset from the server and returns it as a dataframe object
 
     Parameters
     ----------
     name : str, optional
         The name of the dataset you want to fetch.
     version: str
@@ -496,34 +507,38 @@
 
     Returns
     -------
         The dataset dataframe is being returned.
 
     """
 
+    name, branch, version = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     dataset_schema = DatasetSchema()
 
-    dataset_details = version_details(name=name, branch=branch, version=version)
+    dataset_details = version_details(label=label)
 
     if dataset_details is None:
         print(f"[bold red]Unable to fetch Dataset version")
         return
 
     is_empty = dataset_details["is_empty"]
 
     if is_empty:
         print("[bold orange]Dataset file is not registered to the version")
         return
 
-    storage_path = dataset_details["path"]["source_path"]
-    storage_source_type = dataset_details["path"]["source_type"]["public_url"]
+    # storage_path = dataset_details["path"]["source_path"]
+    # storage_source_type = dataset_details["path"]["source_type"]["public_url"]
+
+    # dataset_url = urljoin(storage_source_type, storage_path)
 
-    dataset_url = urljoin(storage_source_type, storage_path)
+    dataset_url = dataset_details["path"]
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
     # print('url', dataset_url)
@@ -544,44 +559,46 @@
         print(f"[bold red]Unable to fetch Dataset")
         # print(response.status_code)
         # print(response.text)
         # print(response.url)
         return
 
 
-def delete(name: str, version: str = "latest") -> str:
-    """This function deletes a dataset from the project
+# def delete(label: str) -> str:
+#     """This function deletes a dataset from the project
 
-    Parameters
-    ----------
-    name : str
-        The name of the dataset you want to delete
-    version : str
-        The version of the dataset to delete.
+#     Parameters
+#     ----------
+#     name : str
+#         The name of the dataset you want to delete
+#     version : str
+#         The version of the dataset to delete.
 
-    """
+#     """
 
-    user_token = get_token()
-    org_id = get_org_id()
-    dataset_schema = DatasetSchema()
+#     name, branch, version = parse_version_label(label)
 
-    url = "org/{}/dataset/{}/delete".format(org_id, name)
-    url = urljoin(dataset_schema.backend.BASE_URL, url)
+#     user_token = get_token()
+#     org_id = get_org_id()
+#     dataset_schema = DatasetSchema()
 
-    headers = {
-        "Content-Type": "application/x-www-form-urlencoded",
-        "Authorization": "Bearer {}".format(user_token),
-    }
+#     url = "org/{}/dataset/{}/delete".format(org_id, name)
+#     url = urljoin(dataset_schema.backend.BASE_URL, url)
 
-    data = {"version": version}
+#     headers = {
+#         "Content-Type": "application/x-www-form-urlencoded",
+#         "Authorization": "Bearer {}".format(user_token),
+#     }
 
-    data = json.dumps(data)
+#     data = {"version": version}
 
-    response = requests.delete(url, headers=headers, data=data)
+#     data = json.dumps(data)
 
-    if response.ok:
-        print(f"[bold green]Dataset has been deleted")
+#     response = requests.delete(url, headers=headers, data=data)
 
-    else:
-        print(f"[bold red]Unable to delete Dataset")
+#     if response.ok:
+#         print(f"[bold green]Dataset has been deleted")
 
-    return response.text
+#     else:
+#         print(f"[bold red]Unable to delete Dataset")
+
+#     return response.text
```

### Comparing `pureml-0.2.3/pureml/components/figure.py` & `pureml-0.3.0/pureml/components/log/figure.py`

 * *Files 10% similar despite different names*

```diff
@@ -3,33 +3,47 @@
 from urllib.parse import urljoin
 
 import numpy as np
 import requests
 from joblib import Parallel, delayed
 from PIL import Image
 
-# from pureml.utils.constants import BASE_URL, PATH_FIGURE_DIR
 from pureml.utils.pipeline import add_figures_to_config
-from pureml.schema import PathSchema, BackendSchema
+from pureml.schema import (
+    PathSchema,
+    BackendSchema,
+    StorageSchema,
+    LogSchema,
+    ConfigKeys,
+)
 from rich import print
-
 from . import get_org_id, get_token
 
+from pureml.utils.version_utils import parse_version_label
+from pureml.utils.config import reset_config
+
+
 path_schema = PathSchema().get_instance()
 backend_schema = BackendSchema().get_instance()
+post_key_figure = LogSchema().key.figure.value
+config_keys = ConfigKeys
+storage = StorageSchema().get_instance()
 
 
 def save_images(figure):
 
     os.makedirs(path_schema.PATH_FIGURE_DIR, exist_ok=True)
     figure_paths = {}
     for figure_key, figure_value in figure.items():
-        save_name = os.path.join(
-            path_schema.PATH_FIGURE_DIR, ".".join([figure_key, "png"])
-        )
+        if figure_key.rsplit(".", 1)[-1] == "png":
+            save_name = figure_key
+        else:
+            save_name = os.path.join(
+                path_schema.PATH_FIGURE_DIR, ".".join([figure_key, "png"])
+            )
 
         canvas = figure_value.canvas
         canvas.draw()
         data = np.frombuffer(canvas.tostring_rgb(), dtype=np.uint8)
         rgb_array = data.reshape(canvas.get_width_height()[::-1] + (3,))
 
         data = Image.fromarray(rgb_array)
@@ -42,60 +56,56 @@
 
 def post_figures(figure_paths, model_name: str, model_branch: str, model_version: str):
     user_token = get_token()
     org_id = get_org_id()
 
     # print('figure_paths', figure_paths)
 
-    url = "org/{}/model/{}/branch/{}/version/{}/log".format(
+    url = "org/{}/model/{}/branch/{}/version/{}/logfile".format(
         org_id, model_name, model_branch, model_version
     )
     url = urljoin(backend_schema.BASE_URL, url)
 
     headers = {"Authorization": "Bearer {}".format(user_token)}
 
-    files = {}
+    files = []
     for file_name, file_path in figure_paths.items():
+        # print("filename", file_name)
 
         if os.path.isfile(file_path):
-            files[file_name] = open(file_path, "rb")
+            files.append(("file", (file_name, open(file_path, "rb"))))
+
         else:
             print("[bold red] figure", file_name, "doesnot exist at the given path")
 
     data = {
-        "name_path_mapping": figure_paths,
-        "model_name": model_name,
-        "model_version": model_branch,
-        "model_version": model_version,
+        "data": figure_paths,
+        "key": "figure",
+        "storage": storage.STORAGE,
     }
 
     # data = json.dumps(data)
 
     # try:
 
     response = requests.post(url, data=data, files=files, headers=headers)
 
     if response.ok:
         print(f"[bold green]Figures have been registered!")
+        reset_config(key=config_keys.figure.value)
 
     else:
         print(f"[bold red]Figures have not been registered!")
 
     return response
     # except Exception as e:
     #     return
 
 
-def add(
-    figure: dict = None,
-    model_name: str = None,
-    model_branch: str = None,
-    model_version: str = "latest",
-    file_paths: dict = None,
-) -> str:
+def add(label: str = None, figure: dict = None, file_paths: dict = None) -> str:
     """`add` function takes in the path of the figure, name of the figure and the model name and
     registers the figure
 
     Parameters
     ----------
     figure : dict
         Key is the figure name, value is the matplotlib figure object
@@ -107,26 +117,29 @@
         The version of the model
 
     Returns
     -------
         The response is a JSON object
 
     """
+    model_name, model_branch, model_version = parse_version_label(label)
+    # print(model_name, model_branch, model_version)
     # print('file_paths', file_paths)
     # print('figure', figure)
 
     if file_paths is None:
         file_paths = save_images(figure)
         # print('figre paths', figure_paths)
-        add_figures_to_config(
-            values=file_paths,
-            model_name=model_name,
-            model_branch=model_branch,
-            model_version=model_version,
-        )
+
+    add_figures_to_config(
+        values=file_paths,
+        model_name=model_name,
+        model_branch=model_branch,
+        model_version=model_version,
+    )
 
     if (
         model_name is not None
         and model_version is not None
         and model_version is not None
     ):
         response = post_figures(
@@ -137,15 +150,16 @@
         )
 
         # print(response.text)
 
     # return response.text
 
 
-def details(model_name: str, model_branch: str, model_version: str = "latest"):
+def details(label: str):
+    model_name, model_branch, model_version = parse_version_label(label)
     user_token = get_token()
     org_id = get_org_id()
 
     url = "org/{}/model/{}/branch/{}/version/{}/log".format(
         org_id, model_name, model_branch, model_version
     )
     url = urljoin(backend_schema.BASE_URL, url)
@@ -163,19 +177,19 @@
         details = response_text["data"]
 
         # print(model_details)
 
         return details
 
     else:
-        print(f"[bold red]Branch details details have not been found")
+        print(f"[bold red]Unable to fetch Figure!")
         return
 
 
-def fetch(model_name: str, model_branch: str, model_version: str = "latest"):
+def fetch(label: str, key: str):
     """It fetches the figure from the server and stores it in the local directory
 
     Parameters
     ----------
     model_name : str
         The name of the model you want to fetch the figure from.
     model_version: str
@@ -184,36 +198,37 @@
         The name of the figure to be fetched. If not specified, all figures will be fetched.
 
     Returns
     -------
         The response text is being returned.
 
     """
+    model_name, model_branch, model_version = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
 
     def fetch_figure(file_details):
 
         file_name, url = file_details
 
         save_path = os.path.join(path_schema.PATH_FIGURE_DIR, file_name)
-        print("save path", save_path)
+        # print("save path in fetching", save_path)
 
         headers = {
             "Content-Type": "application/x-www-form-urlencoded",
             "Authorization": "Bearer {}".format(user_token),
         }
 
-        print("figure url", url)
+        # print("figure url", url)
 
         # response = requests.get(url, headers=headers)
         response = requests.get(url)
 
-        print(response.status_code)
+        # print(response.status_code)
 
         if response.ok:
             print("[bold green] figure {} has been fetched".format(file_name))
 
             save_dir = os.path.dirname(save_path)
 
             os.makedirs(save_dir, exist_ok=True)
@@ -230,58 +245,83 @@
 
             return response.text
         else:
             print("[bold red] Unable to fetch the figure")
 
             return response.text
 
-    figure_details = details(
-        model_name=model_name, model_branch=model_branch, model_version=model_version
-    )
+    figure_details = details(label=label)
 
     if figure_details is None:
         return
 
-    fig_urls = give_fig_urls(details=figure_details)
+    # fig_urls = give_fig_urls(details=figure_details)
+    fig_urls = give_fig_url(details=figure_details, key=key)
 
-    if len(fig_urls) <= 1:
+    if len(fig_urls) == 1:
 
         res_text = fetch_figure(fig_urls[0])
 
     else:
         res_text = Parallel(n_jobs=-1)(
             delayed(fetch_figure)(fig_url) for fig_url in fig_urls
         )
 
-    return res_text
+    # return res_text
 
 
-def give_fig_urls(details):
-
-    fig_paths = None
+def give_fig_url(details, key: str):
+    fig_paths = []
+    # file_url = None
+    source_path = None
+    file_url = None
+    # print(details)
 
     if details is not None:
 
-        details = details[0]["data"]
-        if "figure" in details.keys():
-            fig_paths = []
-
-            fig_details_all = details["figure"]
-
-            for fig_key, path in fig_details_all.items():
-                source_path = fig_details_all[fig_key]["path"]["source_path"]
-                source_url = fig_details_all[fig_key]["path"]["source_type"][
-                    "public_url"
-                ]
-                file_url = urljoin(source_url, source_path)
+        for det in details:
+            # print(det["key"])
+            if det["key"] == key:
+                source_path = det["key"]
+                file_url = det["data"]
+                source_path = ".".join([source_path, "jpg"])
+                # source_path = os.path.join(path_schema.PATH_FIGURE_DIR, source_path)
                 fig_paths.append([source_path, file_url])
 
+                # print(source_path, file_url)
+
+                return fig_paths
+    print("[bold red] Unable to find the figure")
+
     return fig_paths
 
 
+# def give_fig_urls(details):
+
+#     fig_paths = None
+
+#     if details is not None:
+
+#         details = details[0]["data"]
+#         if "figure" in details.keys():
+#             fig_paths = []
+
+#             fig_details_all = details["figure"]
+
+#             for fig_key, path in fig_details_all.items():
+#                 source_path = fig_details_all[fig_key]["path"]["source_path"]
+#                 source_url = fig_details_all[fig_key]["path"]["source_type"][
+#                     "public_url"
+#                 ]
+#                 file_url = urljoin(source_url, source_path)
+#                 fig_paths.append([source_path, file_url])
+
+#     return fig_paths
+
+
 # def delete(name:str, model_name:str,  model_version:str='latest') -> str:
 #     '''`delete()` deletes an figure from a model
 
 #     Parameters
 #     ----------
 #     name : str
 #         The name of the figure you want to delete.
```

### Comparing `pureml-0.2.3/pureml/components/image.py` & `pureml-0.3.0/pureml/components/log/image.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/components/model.py` & `pureml-0.3.0/pureml/components/model.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,38 +1,44 @@
 import requests
 from rich import print
 
-
 import os
 import json
 
-
 from . import get_token, get_org_id
-from pureml.schema import ModelSchema, StorageSchema
+from pureml.schema import ModelSchema, StorageSchema, ConfigKeys
 from pureml import save_model, load_model
 from urllib.parse import urljoin
 import joblib
 from pureml.utils.hash import generate_hash_for_file
 from pureml.utils.readme import load_readme
+from pureml.utils.version_utils import parse_version_label
+from pureml.utils.config import reset_config
+
+
+config_keys = ConfigKeys
+storage = StorageSchema().get_instance()
+
 
+def init_branch(label):
+    name, branch, _ = parse_version_label(label)
 
-def init_branch(branch: str, model_name: str):
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
-    url = "org/{}/model/{}/branch/create".format(org_id, model_name)
+    url = "org/{}/model/{}/branch/create".format(org_id, name)
     url = urljoin(model_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/json",
         "Authorization": "Bearer {}".format(user_token),
     }
 
-    data = {"model_name": model_name, "branchName": branch}
+    data = {"model_name": name, "branchName": branch}
 
     data = json.dumps(data)
 
     response = requests.post(url, data=data, headers=headers)
 
     if response.ok:
         print(f"[bold green]Branch has been created!")
@@ -41,45 +47,49 @@
 
     else:
         print(f"[bold red]Branch has not been created!")
 
         return False
 
 
-def check_model_hash(hash: str, name: str, branch: str):
+def check_model_hash(hash: str, label: str):
+
+    name, branch, _ = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
-    url = "org/{}/model/{}/branch/{}/hash-status".format(org_id, branch, name)
+    url = "org/{}/model/{}/branch/{}/hash-status".format(org_id, name, branch)
     url = urljoin(model_schema.backend.BASE_URL, url)
 
     headers = {"Authorization": "Bearer {}".format(user_token)}
 
     data = {"hash": hash, "branch": branch}
 
     data = json.dumps(data)
 
     response = requests.post(url, data=data, headers=headers)
 
     hash_exists = False
 
     if response.ok:
-        hash_exists = response.json()["data"]
+        hash_exists = response.json()["data"][0]
 
     return hash_exists
 
 
-def branch_details(branch: str, model_name: str):
+def branch_details(label: str):
+    name, branch, _ = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
-    url = "org/{}/model/{}/branch/{}".format(org_id, model_name, branch)
+    url = "org/{}/model/{}/branch/{}".format(org_id, name, branch)
     url = urljoin(model_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
@@ -96,31 +106,32 @@
         return details
 
     else:
         print(f"[bold red]Branch details details have not been found")
         return
 
 
-def branch_status(branch: str, model_name: str):
+def branch_status(label: str):
 
-    details = branch_details(branch=branch, model_name=model_name)
+    details = branch_details(label=label)
 
     if details:
         return True
     else:
         return False
 
 
-def branch_delete(branch: str, model_name: str) -> str:
+def branch_delete(label: str) -> str:
+    name, branch, _ = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
-    url = "org/{}/model/{}/branch/{}/delete".format(org_id, model_name, branch)
+    url = "org/{}/model/{}/branch/{}/delete".format(org_id, name, branch)
     url = urljoin(model_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
@@ -131,21 +142,23 @@
 
     else:
         print(f"[bold red]Unable to delete Model branch")
 
     return response.text
 
 
-def branch_list(model_name: str) -> str:
+def branch_list(label: str) -> str:
+
+    name, _, _ = parse_version_label(label)
 
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
-    url = "org/{}/model/{}/branch".format(org_id, model_name)
+    url = "org/{}/model/{}/branch".format(org_id, name)
     url = urljoin(model_schema.backend.BASE_URL, url)
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
@@ -196,15 +209,18 @@
         return model_list
     else:
         print(f"[bold red]Unable to obtain the list of models!")
 
     return
 
 
-def init(name: str, readme: str = None, branch: str = None):
+def init(label: str, readme: str = None):
+
+    name, branch, _ = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
     if readme is None:
         readme = ModelSchema().PATH_MODEL_README
 
@@ -242,19 +258,20 @@
         print(f"[bold red]Model has not been created!")
 
         return False
 
 
 def register(
     model,
-    name: str,
-    branch: str,
+    label,
     is_empty: bool = False,
-    storage: str = StorageSchema().STORAGE,
 ):
+
+    name, branch, _ = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
     model_file_name = ".".join([name, "pkl"])
     model_path = os.path.join(model_schema.paths.PATH_MODEL_DIR, model_file_name)
 
@@ -262,35 +279,35 @@
 
     save_model(model, name, model_path=model_path)
 
     model_hash = generate_hash_for_file(
         file_path=model_path, name=name, branch=branch, is_empty=is_empty
     )
 
-    model_exists = model_status(name)
+    model_exists = model_status(label)
 
     if not model_exists:
-        model_created = init(name=name, branch=branch)
+        model_created = init(label)
         print("model_created", model_created)
         if not model_created:
             print("[bold red] Unable to register the model")
             return False, model_hash, "latest"
 
-    branch_exists = branch_status(branch=branch, model_name=name)
+    branch_exists = branch_status(label)
     print("branch_exists", branch_exists)
 
     if not branch_exists:
-        branch_created = init_branch(branch=branch, model_name=name)
+        branch_created = init_branch(label)
         print("branch_created", branch_created)
 
         if not branch_created:
             print("[bold red] Unable to register the model")
             return False, model_hash, "latest"
 
-    model_exists_remote = check_model_hash(hash=model_hash, name=name, branch=branch)
+    model_exists_remote = check_model_hash(hash=model_hash, label=label)
 
     if model_exists_remote:
         print(f"[bold red]Model already exists. Not registering a new version!")
         return True, model_hash, "latest"
     else:
         url = "org/{}/model/{}/branch/{}/register".format(org_id, name, branch)
         url = urljoin(model_schema.backend.BASE_URL, url)
@@ -300,58 +317,64 @@
         files = {"file": (model_file_name, open(model_path, "rb"))}
 
         data = {
             "name": name,
             "branch": branch,
             "hash": model_hash,
             "is_empty": is_empty,
-            "storage": storage,
+            "storage": storage.STORAGE,
         }
 
         response = requests.post(url, files=files, data=data, headers=headers)
 
         if response.ok:
             print(f"[bold green]Model has been registered!")
 
             model_version = response.json()["data"][0]["version"]
             print("Model Version: ", model_version)
 
+            # reset_config(key=config_keys.model.value)
+
             return True, model_hash, model_version
 
         else:
             print(f"[bold red]Model has not been registered!")
 
         return False, model_hash, None
 
 
-def model_status(name: str):
+def model_status(label: str):
+
+    name, _, _ = parse_version_label(label)
 
-    model_details = details(name=name)
+    model_details = details(label=label)
 
     if model_details:
         return True
     else:
         return False
 
 
-def details(name: str):
+def details(label: str):
     """It fetches the details of a model.
 
     Parameters
     ----------
     name : str
         The name of the model
     version: str
         The version of the model
     Returns
     -------
         The details of the model.
 
     """
 
+    name, _, _ = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
     url = "org/{}/model/{}".format(org_id, name)
     url = urljoin(model_schema.backend.BASE_URL, url)
 
@@ -373,29 +396,31 @@
         return model_details
 
     else:
         print(f"[bold red]Model details have not been found")
         return
 
 
-def version_details(name: str, branch: str, version: str = "latest"):
+def version_details(label: str):
     """It fetches the details of a model.
 
     Parameters
     ----------
     name : str
         The name of the model
     version: str
         The version of the model
     Returns
     -------
         The details of the model.
 
     """
 
+    name, branch, version = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
     model_schema = ModelSchema()
 
     url = "org/{}/model/{}/branch/{}/version/{}".format(org_id, name, branch, version)
     url = urljoin(model_schema.backend.BASE_URL, url)
 
@@ -415,15 +440,15 @@
         return model_details
 
     else:
         print(f"[bold red]Model details have not been found")
         return
 
 
-def fetch(name: str, branch: str, version: str = "latest"):
+def fetch(label: str):
     """This function fetches a model from the server and returns it as a `Model` object
 
     Parameters
     ----------
     name : str, optional
         The name of the model you want to fetch.
     version: str
@@ -431,33 +456,37 @@
 
     Returns
     -------
         The model is being returned.
 
     """
 
+    name, branch, version = parse_version_label(label)
+
     user_token = get_token()
     org_id = get_org_id()
 
-    model_details = version_details(name=name, branch=branch, version=version)
+    model_details = version_details(label=label)
 
     if model_details is None:
         print(f"[bold red]Unable to fetch Model version")
         return
 
     is_empty = model_details["is_empty"]
 
     if is_empty:
         print("[bold orange]Model file is not registered to the version")
         return
 
-    storage_path = model_details["path"]["source_path"]
-    storage_source_type = model_details["path"]["source_type"]["public_url"]
+    # storage_path = model_details["path"]["source_path"]
+    # storage_source_type = model_details["path"]["source_type"]["public_url"]
+
+    # model_url = urljoin(storage_source_type, storage_path)
 
-    model_url = urljoin(storage_source_type, storage_path)
+    model_url = model_details["path"]
 
     headers = {
         "Content-Type": "application/x-www-form-urlencoded",
         "Authorization": "Bearer {}".format(user_token),
     }
 
     response = requests.get(model_url)
@@ -474,44 +503,46 @@
         print(f"[bold red]Unable to fetch Model version")
         # print(response.status_code)
         # print(response.text)
         # print(response.url)
         return
 
 
-def delete(name: str) -> str:
-    """This function deletes a model from the project
+# def delete(label: str) -> str:
+#     """This function deletes a model from the project
 
-    Parameters
-    ----------
-    name : str
-        The name of the model you want to delete
-    version : str
-        The version of the model to delete.
+#     Parameters
+#     ----------
+#     name : str
+#         The name of the model you want to delete
+#     version : str
+#         The version of the model to delete.
 
-    """
+#     """
 
-    user_token = get_token()
-    org_id = get_org_id()
-    model_schema = ModelSchema()
+#     name, _, _ = parse_version_label(label)
 
-    url = "org/{}/model/{}/delete".format(org_id, name)
-    url = urljoin(model_schema.backend.BASE_URL, url)
+#     user_token = get_token()
+#     org_id = get_org_id()
+#     model_schema = ModelSchema()
 
-    headers = {
-        "Content-Type": "application/x-www-form-urlencoded",
-        "Authorization": "Bearer {}".format(user_token),
-    }
+#     url = "org/{}/model/{}/delete".format(org_id, name)
+#     url = urljoin(model_schema.backend.BASE_URL, url)
 
-    response = requests.delete(url, headers=headers)
+#     headers = {
+#         "Content-Type": "application/x-www-form-urlencoded",
+#         "Authorization": "Bearer {}".format(user_token),
+#     }
 
-    if response.ok:
-        print(f"[bold green]Model has been deleted")
+#     response = requests.delete(url, headers=headers)
 
-    else:
-        print(f"[bold red]Unable to delete Model")
+#     if response.ok:
+#         print(f"[bold green]Model has been deleted")
 
-    return response.text
+#     else:
+#         print(f"[bold red]Unable to delete Model")
+
+#     return response.text
 
 
 def serve_model():
     pass
```

### Comparing `pureml-0.2.3/pureml/components/params.py` & `pureml-0.3.0/pureml/components/log/metrics.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,210 +1,232 @@
 import json
 from urllib.parse import urljoin
 
 import requests
-from pureml.schema.log import LogSchema
+from pureml.schema import BackendSchema, LogSchema, ConfigKeys
 from pureml.utils.log_utils import merge_step_with_value
-from pureml.utils.pipeline import add_params_to_config
+from pureml.utils.pipeline import add_metrics_to_config
 from rich import print
 
 from . import convert_values_to_string, get_org_id, get_token
+from pureml.utils.version_utils import parse_version_label
+from pureml.utils.config import reset_config
 
 
-def post_params(params, model_name: str, model_branch: str, model_version: str):
+backend_schema = BackendSchema().get_instance()
+post_key_predict = LogSchema().key.metrics.value
+config_keys = ConfigKeys
+
+
+def post_metrics(metrics, model_name: str, model_branch: str, model_version: str):
+
     user_token = get_token()
     org_id = get_org_id()
-    log_schema = LogSchema()
 
     url = "org/{}/model/{}/branch/{}/version/{}/log".format(
         org_id, model_name, model_branch, model_version
     )
-    url = urljoin(log_schema.backend.BASE_URL, url)
+    url = urljoin(backend_schema.BASE_URL, url)
 
     headers = {
-        "Content-Type": "application/x-www-form-urlencoded",
+        "accept": "application/json",
+        "Content-Type": "*/*",
         "Authorization": "Bearer {}".format(user_token),
     }
 
-    params = json.dumps(params)
-
-    data = {"data": params, "key": "params"}
+    metrics = json.dumps(metrics)
+    data = {"data": metrics, "key": post_key_predict}
 
     data = json.dumps(data)
 
     response = requests.post(url, data=data, headers=headers)
 
     if response.ok:
-        print(f"[bold green]Params have been registered!")
+        print(f"[bold green]Metrics have been registered!")
+        reset_config(key=config_keys.metrics.value)
 
     else:
-        print(f"[bold red]Params have not been registered!")
+        print(f"[bold red]Metrics have not been registered!")
 
     return response
 
 
 def add(
-    params,
-    model_name: str = None,
-    model_branch: str = None,
-    model_version: str = "latest",
+    metrics,
+    label: str = None,
     step=1,
 ) -> str:
-    """`add()` takes a dictionary of parameters and a model name as input and returns a string
+    """`add()` takes a dictionary of metrics and a model name as input and returns a string
 
     Parameters
     ----------
-    params : dict
-        a dictionary of parameters
+    metrics
+        a dictionary of metrics
     model_name : str
-        The name of the model you want to add parameters to.
+        The name of the model you want to add metrics to.
     model_version: str
         The version of the model
 
     Returns
     -------
         The response.text is being returned.
 
     """
+    model_name, model_branch, model_version = parse_version_label(label)
 
-    params = convert_values_to_string(logged_dict=params)
-    # params = merge_step_with_value(values_dict=params, step=step)
+    metrics = convert_values_to_string(logged_dict=metrics)
+    # metrics = merge_step_with_value(values_dict=metrics, step=step)
 
-    add_params_to_config(
-        values=params,
+    add_metrics_to_config(
+        values=metrics,
         model_name=model_name,
         model_branch=model_branch,
         model_version=model_version,
     )
 
     if (
         model_name is not None
         and model_branch is not None
         and model_version is not None
     ):
-        response = post_params(
-            params=params,
+        response = post_metrics(
+            metrics=metrics,
             model_name=model_name,
             model_branch=model_branch,
             model_version=model_version,
         )
 
-    #     return response.text
+        # return response.text
 
     # return
 
 
-# @app.command()
-def fetch(
-    model_name: str, model_branch: str, model_version: str = "latest", param: str = ""
-) -> str:
-    """
-
-    This function fetches the parameters of a model
-
-    Parameters
-    ----------
-    model_name : str
-        The name of the model you want to fetch the parameters for.
-    model_version: str
-        The version of the model
-    param : str
-        The name of the parameter to fetch. If not specified, all parameters are returned.
-
-    Returns
-    -------
-        The params that are fetched
-
-    """
+def details(label: str):
+    model_name, model_branch, model_version = parse_version_label(label)
     user_token = get_token()
     org_id = get_org_id()
-    log_schema = LogSchema()
 
     url = "org/{}/model/{}/branch/{}/version/{}/log".format(
         org_id, model_name, model_branch, model_version
     )
-    url = urljoin(log_schema.backend.BASE_URL, url)
+    url = urljoin(backend_schema.BASE_URL, url)
 
     headers = {
-        "Content-Type": "application/x-www-form-urlencoded",
+        "accept": "application/json",
         "Authorization": "Bearer {}".format(user_token),
     }
 
-    request_params = {"key": "params"}
-    request_params = json.dumps(request_params)
-
-    response = requests.get(url, headers=headers, params=params)
+    response = requests.get(url, headers=headers)
 
     if response.ok:
-        res_text = json.loads(response.text)
+        # T-1161 standardize api response to contains Models as a list
+        response_text = response.json()
+        details = response_text["data"]
 
-        if param == "":
+        # print(model_details)
 
-            params = res_text
+        return details
 
-            # print(f"[bold green]Params have been fetched")
-            # print(params)
-
-            return params
+    else:
+        print(f"[bold red]Unable to fetch logs!")
+        return
 
-        else:
-            if "param" in res_text.keys() and "value" in res_text.keys():
-                params = res_text["value"]
-                # params = json.loads(params)
 
-                # print(f"[bold green]Params have been fetched")
-                # print(res_text['param'], ':', res_text['value'])
+def get_value_from_log(details, key_log=post_key_predict, key=None):
+    value = None
+    if details is not None:
+        # print(details)
+
+        for det in details:
+            # print(det)
+            # print(det["key"])
+            if det["key"] == key_log:
+                value = det["data"]
+                # print(value)
+                value = json.loads(value)
+
+                if key is not None:
+                    if key in value.keys():
+                        value = value[key]
+                    else:
+                        print(
+                            "[bold red]{} : {} is not available for the model!".format(
+                                key_log, key
+                            )
+                        )
+
+                return value
 
-                return params
+    print("[bold red] Unable to find the {}".format(key))
 
-            else:
-                print(
-                    "[bold red]Param {} are not available for the model!".format(param)
-                )
-                # print(response.text)
-                return
+    return value
 
-    else:
-        print(f"[bold red]Unable to fetch Params!")
-        print(response.text)
-        return
 
-
-# @app.command()
-def delete(
-    param: str, model_name: str, model_branch: str, model_version: str = "latest"
-) -> str:
-    """This function deletes a parameter from a model
+def fetch(label: str, metric: str = None) -> str:
+    """This function fetches the metrics of a model
 
     Parameters
     ----------
     model_name : str
-        The name of the model you want to delete the parameter from.
-    param : str
-        The name of the parameter to delete.
+        The name of the model you want to fetch metrics for.
     model_version: str
         The version of the model
+    metric : str
+        The metric you want to fetch. If you want to fetch all the metrics, leave this parameter empty.
+
+    Returns
+    -------
+        The metrics that are fetched
 
     """
-    user_token = get_token()
-    org_id = get_org_id()
-    log_schema = LogSchema()
 
-    url = "org/{}/model/{}/branch/{}/version/{}/log/delete".format(
-        org_id, model_name, model_branch, model_version
-    )
-    url = urljoin(log_schema.backend.BASE_URL, url)
+    metric_details = details(label=label)
 
-    headers = {
-        "Content-Type": "application/x-www-form-urlencoded",
-        "Authorization": "Bearer {}".format(user_token),
-    }
+    if metric_details:
+
+        metrics = get_value_from_log(
+            details=metric_details, key_log=post_key_predict, key=metric
+        )
 
-    response = requests.delete(url, headers=headers)
+        return metrics
 
-    if response.ok:
-        print(f"[bold green]Param has been deleted")
+    return
 
-    else:
-        print(f"[bold red]Unable to delete Param")
 
-    return response.text
+# def delete(metric: str, label: str) -> str:
+#     """This function deletes a metric from a model
+
+#     Parameters
+#     ----------
+#     model_name : str
+#         The name of the model you want to delete the metric from
+#     metric : str
+#         The name of the metric to delete
+#     model_version: str
+#         The version of the model
+
+#     """
+#     model_name, model_branch, model_version = parse_version_label(label)
+
+#     user_token = get_token()
+#     org_id = get_org_id()
+#     log_schema = LogSchema()
+
+#     url = "org/{}/model/{}/branch/{}/version/{}/log/delete".format(
+#         org_id, model_name, model_branch, model_version
+#     )
+#     url = urljoin(log_schema.backend.BASE_URL, url)
+
+#     headers = {
+#         "Content-Type": "application/x-www-form-urlencoded",
+#         "Authorization": "Bearer {}".format(user_token),
+#     }
+
+#     response = requests.delete(url, headers=headers)
+
+#     if response.status_code == 200:
+#         print(f"[bold green]Metric has been deleted")
+
+#     else:
+#         print(f"[bold red]Unable to delete Metric")
+
+#     return response.text
```

### Comparing `pureml-0.2.3/pureml/components/tabular.py` & `pureml-0.3.0/pureml/components/log/tabular.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/components/video.py` & `pureml-0.3.0/pureml/components/log/video.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/config/parser.py` & `pureml-0.3.0/pureml/config/parser.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/decorators/pip_requirements.py` & `pureml-0.3.0/pureml/decorators/pip_requirements.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/decorators/predict.py` & `pureml-0.3.0/pureml/decorators/predict.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/deploy/docker.py` & `pureml-0.3.0/pureml/package/docker.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import os
 import docker
 from .fastapi import create_fastapi_file
-from pureml.schema import FastAPISchema, PredictionSchema, DockerSchema
+from pureml.schema import FastAPISchema, PredictSchema, DockerSchema
 
-prediction_schema = PredictionSchema()
+prediction_schema = PredictSchema()
 fastapi_schema = FastAPISchema()
 docker_schema = DockerSchema()
 
 
 def create_docker_file(org_id, access_token):
     # os.makedirs(PATH_DOCKER_DIR, exist_ok=True)
     os.makedirs(prediction_schema.paths.PATH_PREDICT_DIR, exist_ok=True)
@@ -124,35 +124,25 @@
         name=name,
     )
 
     return container
 
 
 def create(
-    model_name,
-    model_branch,
-    model_version,
+    label,
     org_id,
     access_token,
     image_tag=None,
     predict_path=None,
     requirements_path=None,
     container_name=None,
-    input: dict = None,
-    output: dict = None,
 ):
 
     create_fastapi_file(
-        model_name=model_name,
-        model_branch=model_branch,
-        model_version=model_version,
-        predict_path=predict_path,
-        requirements_path=requirements_path,
-        input=input,
-        output=output,
+        label=label, predict_path=predict_path, requirements_path=requirements_path
     )
 
     create_docker_file(org_id=org_id, access_token=access_token)
 
     image = create_docker_image(image_tag)
 
     if image is not None:
```

### Comparing `pureml-0.2.3/pureml/lineage/data/create_lineage.py` & `pureml-0.3.0/pureml/lineage/data/create_lineage.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,20 +1,23 @@
 from pureml.utils.config import load_config
 from collections import OrderedDict
 import json
+import time
 
 
 def create_nodes(components):
     # print(components)
 
     nodes = [
         {
             "id": component["name"],
             "text": component["name"],
             "nodeType": component["type"],
+            "desc": str(component["desc"]),
+            "time": str(component["time"]),
         }
         for component in components
     ]
 
     return nodes
 
 
@@ -22,15 +25,24 @@
     # print(components)
 
     node_nodes = [i["id"] for i in nodes]
     edge_nodes = sum([[i["from"]] + [i["to"]] for i in edges], [])
 
     extra_nodes = list(set([n for n in edge_nodes if n not in node_nodes]))
 
-    nodes = nodes + [{"id": n, "text": n, "nodeType": "unknown"} for n in extra_nodes]
+    nodes = nodes + [
+        {
+            "id": n,
+            "text": n,
+            "nodeType": "unknown",
+            "desc": str(None),
+            "time": str(time.time()),
+        }
+        for n in extra_nodes
+    ]
 
     return nodes
 
 
 def create_edges(components):
 
     edges = []
```

### Comparing `pureml-0.2.3/pureml/packaging/__init__.py` & `pureml-0.3.0/pureml/packaging/__init__.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,42 +1,39 @@
 import os
 from pathlib import Path
 from .packaging import Model
 
 
+def save_model(model, model_name, model_path) -> None:
+    """The function takes in a model and a model name, and saves the model to the default `models` directory.
 
-def save_model(model, model_name, model_path) -> None: 
-    ''' The function takes in a model and a model name, and saves the model to the default `models` directory. 
-    
     Parameters
     ----------
     model
         The model you want to save.
     model_name
         The name of the model.
-    
-    '''
+
+    """
     model_dir = os.path.dirname(model_path)
     # print(model_dir)
     # os.makedirs(model_dir, exist_ok=True)
 
     Model(model=model, model_name=model_name, model_path=model_path).save_model()
 
 
+def load_model(model_path: Path):
+    """Loads a model from a given path
 
-def load_model(model_path:Path):
-    ''' Loads a model from a given path
-    
     Parameters
     ----------
     model_path : Path
         The path to the model you want to load.
-    
+
     Returns
     -------
         The model is being returned.
-    
-    '''
+
+    """
     model = Model(model_path=model_path).load_model()
 
     return model
-
```

### Comparing `pureml-0.2.3/pureml/packaging/model_framework.py` & `pureml-0.3.0/pureml/packaging/model_framework.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/catboost.py` & `pureml-0.3.0/pureml/packaging/model_packaging/catboost.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/custom.py` & `pureml-0.3.0/pureml/packaging/model_packaging/custom.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/keras.py` & `pureml-0.3.0/pureml/packaging/model_packaging/keras.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/lightgbm.py` & `pureml-0.3.0/pureml/packaging/model_packaging/lightgbm.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/pytorch.py` & `pureml-0.3.0/pureml/packaging/model_packaging/pytorch.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/pytorch_tabnet.py` & `pureml-0.3.0/pureml/packaging/model_packaging/pytorch_tabnet.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/sklearn.py` & `pureml-0.3.0/pureml/packaging/model_packaging/sklearn.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/tensorflow.py` & `pureml-0.3.0/pureml/packaging/model_packaging/tensorflow.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/model_packaging/xgboost.py` & `pureml-0.3.0/pureml/packaging/model_packaging/xgboost.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/packaging.py` & `pureml-0.3.0/pureml/packaging/packaging.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/packaging/packaging_utils.py` & `pureml-0.3.0/pureml/packaging/packaging_utils.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/predictor/predictor.py` & `pureml-0.3.0/pureml/predictor/predictor.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,44 +1,38 @@
 from pydantic import BaseModel, Field
 import typing
 from typing import List, Any
 from abc import ABC, abstractmethod
-
+from pureml.schema import Input, Output
 from enum import Enum
 
 
-# class ModelDetails(str, Enum):
-#     name = ""
-#     branch = ""
-#     version = ""
-
-
 class BasePredictor(BaseModel, ABC):
-    # model_details: typing.Union[typing.List["str"], typing.List[typing.List["str"]]]
-    # model_details: typing.Union[ModelDetails, typing.List[ModelDetails]]
-    model_details: list
+    label: str
     model: Any = None
+    input: Input
+    output: Output = Output()
     requirements_py: list = None
     requirements_sys: list = None
 
     class Config:
         arbitrary_types_allowed = True
 
     @abstractmethod
+    def load_models(self):
+        pass
+
+    @abstractmethod
     def predict(self, **kwargs: typing.Any):
         pass
 
     # @abstractmethod
     def load_requirements_py(self):
         pass
 
     # @abstractmethod
     def load_requirements_sys(self):
         pass
 
-    @abstractmethod
-    def load_models(self):
-        pass
-
     # @abstractmethod
     def load_resources(self):
         pass
```

### Comparing `pureml-0.2.3/pureml/schema/packaging.py` & `pureml-0.3.0/pureml/schema/packaging.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from pydantic import BaseModel
 from .backend import BackendSchema
-from .prediction import PredictionSchema
+from .predict import PredictSchema
 
 import typing
 import os
 from .paths import PathSchema
 
 
 class FastAPISchema(BaseModel):
```

### Comparing `pureml-0.2.3/pureml/schema/paths.py` & `pureml-0.3.0/pureml/schema/paths.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/utils/constants.py` & `pureml-0.3.0/pureml/utils/constants.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/utils/deploy.py` & `pureml-0.3.0/pureml/utils/package.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,89 +1,83 @@
 import pandas as pd
 import numpy as np
 from PIL import Image
 import json
+from pureml.schema import DataTypes
 
 
 def process_input(input):
 
-    input_type = ''
+    input_type = ""
     input_shape = None
 
-
     if input is not None:
         input_keys = input.keys()
 
-        if 'type' in input_keys:
-            input_type = input['type']
-        if 'shape' in input_keys:
-            input_shape = input['shape']
-    
-    return input_type, input_shape
+        if "type" in input_keys:
+            input_type = input["type"]
+        if "shape" in input_keys:
+            input_shape = input["shape"]
 
+    return input_type, input_shape
 
 
 def process_output(output):
 
-    output_type = ''
+    output_type = ""
     output_shape = None
 
-
     if output is not None:
         output_keys = output.keys()
 
-        if 'type' in output_keys:
-            output_type = output['type']
-        if 'shape' in output_keys:
-            output_shape = output['shape']
-    
-    return output_type, output_shape
+        if "type" in output_keys:
+            output_type = output["type"]
+        if "shape" in output_keys:
+            output_shape = output["shape"]
 
+    return output_type, output_shape
 
 
 def parse_input(data, input_type, input_shape):
     # if input_type == 'json':
     #     data = data
 
-    if input_type == 'numpy ndarray':
+    if input_type == DataTypes.NUMPY_NDARRAY:
         if type(data) == str:
             data = json.loads(data)
         data = np.array(data)
         data = data.reshape(input_shape)
-    elif input_type == 'pandas dataframe':
+    elif input_type == DataTypes.PD_DATAFRAME:
         if type(data) == str:
             data = json.loads(data)
-        data =  pd.DataFrame.from_dict(data)
-    elif input_type == 'text':
+        data = pd.DataFrame.from_dict(data)
+    elif input_type == DataTypes.TEXT:
         data = json.loads(data)
-    elif input_type == 'image':
+    elif input_type == DataTypes.IMAGE:
         data = Image.open(data)
         data = np.array(data)
-        print(data.shape)
+        print("input image shape", data.shape)
     else:
         data = None
 
-    print(type(data))
+    print("input data type", type(data))
     # print(data)
 
     return data
 
+
 def parse_output(data, output_type, output_shape):
     # if input_type == 'json':
     #     data = data
 
-
-    if output_type == 'numpy ndarray':
+    if output_type == DataTypes.NUMPY_NDARRAY:
         data = data.tolist()
         data = json.dumps(data)
-    elif output_type == 'pandas dataframe':
+    elif output_type == DataTypes.PD_DATAFRAME:
         data = data.to_dict()
         data = json.dumps(data)
-    elif output_type == 'text':
+    elif output_type == DataTypes.TEXT:
         data = json.dumps(data)
     else:
         data = json.dumps(data)
 
-
-
     return data
-
```

### Comparing `pureml-0.2.3/pureml/utils/hash.py` & `pureml-0.3.0/pureml/utils/hash.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/utils/log_utils.py` & `pureml-0.3.0/pureml/utils/log_utils.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pureml/utils/readme.py` & `pureml-0.3.0/pureml/utils/readme.py`

 * *Files identical despite different names*

### Comparing `pureml-0.2.3/pyproject.toml` & `pureml-0.3.0/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pureml"
-version = "0.2.3"
+version = "0.3.0"
 description = ""
 license = "Apache-2.0"
 authors = ["vamsidhar muthireddy <vamsi.muthireddy@gmail.com>"]
 readme = "README.md"
 homepage = "https://pureml.com/"
 repository = "https://github.com/engageml-github/Pure"
 documentation = "https://docs.pureml.com"
@@ -34,14 +34,17 @@
 pandas = "^1.4.3"
 matplotlib = "^3.6.2"
 joblib = "^1.2.0"
 fastapi = "^0.88.0"
 uvicorn = "^0.20.0"
 docker = "^6.0.1"
 python-multipart = "^0.0.5"
+nest-asyncio = "^1.5.6"
+pyngrok = "^5.2.1"
+ipapi = "^1.0.4"
 
 [tool.poetry.dev-dependencies]
 ipykernel = "^6.19.2"
 lightgbm = "^3.3.2"
 xgboost = "^1.6.1"
 catboost = "^1.0.6"
 scikit-learn = "^1.1.1"
```

### Comparing `pureml-0.2.3/PKG-INFO` & `pureml-0.3.0/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,71 +1,65 @@
 Metadata-Version: 2.1
 Name: pureml
-Version: 0.2.3
+Version: 0.3.0
 Summary: 
 Home-page: https://pureml.com/
 License: Apache-2.0
 Keywords: pureml,model-store,machine-learning,python,model-registry,collabortion
 Author: vamsidhar muthireddy
 Author-email: vamsi.muthireddy@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Software Development :: Build Tools
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Requires-Dist: Pillow (>=9.3.0,<10.0.0)
 Requires-Dist: PyJWT (>=2.4.0,<3.0.0)
 Requires-Dist: PyYAML (>=6.0,<7.0)
 Requires-Dist: docker (>=6.0.1,<7.0.0)
 Requires-Dist: fastapi (>=0.88.0,<0.89.0)
+Requires-Dist: ipapi (>=1.0.4,<2.0.0)
 Requires-Dist: joblib (>=1.2.0,<2.0.0)
 Requires-Dist: matplotlib (>=3.6.2,<4.0.0)
+Requires-Dist: nest-asyncio (>=1.5.6,<2.0.0)
 Requires-Dist: numpy (>=1.23.1,<2.0.0)
 Requires-Dist: pandas (>=1.4.3,<2.0.0)
 Requires-Dist: pyarrow (>=8.0.0,<9.0.0)
 Requires-Dist: pydantic (>=1.9.1,<2.0.0)
+Requires-Dist: pyngrok (>=5.2.1,<6.0.0)
 Requires-Dist: python-dotenv (>=0.20.0,<0.21.0)
 Requires-Dist: python-multipart (>=0.0.5,<0.0.6)
 Requires-Dist: requests (>=2.28.1,<3.0.0)
 Requires-Dist: typer[all] (>=0.6.1,<0.7.0)
 Requires-Dist: uvicorn (>=0.20.0,<0.21.0)
 Project-URL: Documentation, https://docs.pureml.com
 Project-URL: Repository, https://github.com/engageml-github/Pure
 Description-Content-Type: text/markdown
 
-<h1 align="center">
-  <a href="https://pureml.com">
-    <img
-      align="center"
-      alt="PureML"
-      src="https://github.com/PureML-Inc/PureML/blob/main/assets/coverImg.jpeg"
-      style="width:100%;"
-    />
-  </a>
-</h1>
-
+[![PureML](/assets/SDKCoverImg.png)](https://pureml.com)
 
-
-
-<div align="center">
+<h align="center">
 
 # Track, version, compare and review your data and models.
 
-</div>
-
+</h>
 
 # ⛳ Quick Access
 
 <p align="center">
   <a
-    href="https://docs.pureml.com"
+    href="https://pureml.mintlify.app"
   ><b>Documentation</b></a>
   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
   <a
     href="https://www.youtube.com/watch?v=HdzLFEWS4s8&t=1s"
   ><b>Watch Demo</b></a>
   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
   <a
@@ -78,20 +72,17 @@
   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
   <a
     href="https://app.pureml.com/auth/signup"
   ><b>Sign Up for free</b></a>
 
 </p>
 
-
-
 </br>
 </br>
 
-
 <div align="center">
   <a
     href="https://pypi.org/project/pureml/"
   >
     <img alt="PyPi" src="https://img.shields.io/pypi/v/pureml?color=green&logo=pureml" />
   </a>
   &nbsp;
@@ -133,24 +124,19 @@
   &nbsp;
   <a
     href="https://pypi.org/project/pureml/"
   >
     <img alt="Coverage" src="https://img.shields.io/github/stars/pureml-inc/pureml?style=social">
   </a>
 
-
-
 </div>
 
-
 </br>
 </br>
 
-
-
 # 💎 Intro
 
 PureML is an open-source version control for machine learning.
 
 1. [Quick start](#quick-start)
 1. [How it works](#how-it-works)
 1. [Demo](#demo)
@@ -162,64 +148,68 @@
 
 <br />
 
 # ⏱ Quick start
 
 You can install and run PureML using `pip`.
 
-
 Install PureML
+
 ```bash
 pip install pureml
 ```
 
 <br />
 
 # 📋 How it works
+
 Just add a few lines of code. You don't need to change the way you work.
 
 PureML is a Python library that uploads metadata to S3.
 
 ### Generating Data Lineage
 
 1. Load Data
+
 ```python
 @load_data(name='loading data')
 def loading_data():
-    
+
     return pd.read_csv('churn.csv')
 ```
 
 2. Transform Data
+
 ```python
 @transformer(name='fill missing values')
 def fill_missing_values(df):
     return df.fillna()
-    
+
 
 @transformer(name='encode ordinal')
 def encode_ordinal(df):
     col_ord = ['state', 'phone number']
     df_ord = df[col_ord]
-    feat = OrdinalEncoder().fit_transform(df_ord)    
+    feat = OrdinalEncoder().fit_transform(df_ord)
     df[col_ord] = feat
-    
+
     return df
 
 @transformer(name='encode binary')
 def encode_binary(df):
 
     df['voice mail plan'] = df['voice mail plan'].map({'yes':1, 'no':0})
     df['international plan'] = df['international plan'].map({'yes':1, 'no':0})
     df['churn'] = df['churn'].map({True:1, False:0})
 
     return df
 ```
 
 3. Register Dataset
+
 ```python
 @dataset(name='telecom churn', parent='encode binary')
 def build_dataset():
     df = loading_data()
 
     df = fill_missing_values(df)
 
@@ -247,120 +237,114 @@
 
 # 💻 Demo
 
 ### Live demo
 
 Build and run a PureML project to create data lineage and a model with our <b>[demo colab link](https://colab.research.google.com/drive/1LlrpaKiREwgesaRcnwkJP-w2MPesXf1t?usp=sharing)</b>.
 
-
 ### Demo video (2 min)
+
 PureML quick start demo
 
 [![PureML Demo Video](https://img.youtube.com/vi/HdzLFEWS4s8/0.jpg)](https://www.youtube.com/watch?v=HdzLFEWS4s8 "PureML Demo Video")
 
-
-
 <sub><i>Click the image to play video</i></sub>
 
 <br />
 
-
 # 📍 [Main Features](https://docs.pureml.com/)
-|   |   |
-| --- | --- |
-| Data Lineage | Automatic generation of data lineage|
-| Dataset Versioning | Object-based Automatic Semantic Versioning of datasets |
-| Model Versioning | Object-based Automatic Semantic Versioning of models |
-| Comparision | Comparing different versions of models or datasets
-| Branches (*Coming Soon*) | Separation between experimentation and production ready models using branches |
-| Review (*Coming Soon*) | Review and approve models, and datasets to production ready branch|
 
-<br />
+|                          |                                                                               |
+| ------------------------ | ----------------------------------------------------------------------------- |
+| Data Lineage             | Automatic generation of data lineage                                          |
+| Dataset Versioning       | Object-based Automatic Semantic Versioning of datasets                        |
+| Model Versioning         | Object-based Automatic Semantic Versioning of models                          |
+| Comparision              | Comparing different versions of models or datasets                            |
+| Branches (_Coming Soon_) | Separation between experimentation and production ready models using branches |
+| Review (_Coming Soon_)   | Review and approve models, and datasets to production ready branch            |
 
+<br />
 
 # 🔮 Core design principles
 
-|   |   |
-| --- | --- |
-| Easy developer experience | An intuitive open source package aimed to bridge the gaps in data science teams |
-| Engineering best practices built-in | Integrating PureML functionalities in your code doesnot disrupt your workflow |
-| Object Versioning | A reliable object versioning mechanism to track changes to your datasets, and models |
-| Data is a first-class citizen | Your data is secure. It will never leave your system. |
-| Reduce Friction | Have access to operations performed on data using data lineage without having to spend time on lengthy meetings |
-
-
+|                                     |                                                                                                                 |
+| ----------------------------------- | --------------------------------------------------------------------------------------------------------------- |
+| Easy developer experience           | An intuitive open source package aimed to bridge the gaps in data science teams                                 |
+| Engineering best practices built-in | Integrating PureML functionalities in your code doesnot disrupt your workflow                                   |
+| Object Versioning                   | A reliable object versioning mechanism to track changes to your datasets, and models                            |
+| Data is a first-class citizen       | Your data is secure. It will never leave your system.                                                           |
+| Reduce Friction                     | Have access to operations performed on data using data lineage without having to spend time on lengthy meetings |
 
 <br />
 
 # ⚙ Core abstractions
 
 These are the fundamental concepts that PureML uses to operate.
 
-|   |   |
-| --- | --- |
-| [Project](https://docs.pureml.com/docs/projects/about_projects) | A data science project. This is where you store datasets, models, and their related objects. It is similar to a github repository with object storage.|
-| [Lineage](https://docs.pureml.com/docs/data/register_data_pipeline) | Contains a series of transformations performed on data to generate a dataset.|
-| Data Versioning | Versioning of the data should be comprehensible to the user and should encapsulate the changes in the data, its creation mechanism, among others.|
-| Model Versioning| Versioning of the model should be comprehensible to the user and should encapuslate the changes in training data, model architecture, hyper parameters.|
-| Fetch | This functionality is used to fetch registered Models, and Datasets.|
-
+|                                                                     |                                                                                                                                                         |
+| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| [Project](https://docs.pureml.com/docs/projects/about_projects)     | A data science project. This is where you store datasets, models, and their related objects. It is similar to a github repository with object storage.  |
+| [Lineage](https://docs.pureml.com/docs/data/register_data_pipeline) | Contains a series of transformations performed on data to generate a dataset.                                                                           |
+| Data Versioning                                                     | Versioning of the data should be comprehensible to the user and should encapsulate the changes in the data, its creation mechanism, among others.       |
+| Model Versioning                                                    | Versioning of the model should be comprehensible to the user and should encapuslate the changes in training data, model architecture, hyper parameters. |
+| Fetch                                                               | This functionality is used to fetch registered Models, and Datasets.                                                                                    |
 
 <br />
 
 # 🤝 Why to get involved
+
 Version control is much more common in software than in machine learning. So why isn’t everyone using Git? Git doesn’t work well with machine learning. It can’t handle large files, it can’t handle key/value metadata like metrics, and it can’t record information automatically from inside a training script.
 
 GitHub wasn’t designed with data as a core project component. This along with a number of other differences between AI and more traditional software projects makes GitHub a bad fit for artificial intelligence, contributing to the reproducibility crisis in machine learning.
 
 From manually tracking models to git based versioning systems that do not follow an intuitive versioning mechanism, there is no standardized way to track objects. Using these mechanisms, it is hard enough to track or get your model from a month ago running, let alone of a teammates!
 
 We are trying to build a version control system for machine learning objects. A mechanism that is object dependant and intuitive for users.
 
 Lets build this together. If you have faced this issue or have worked out a similar solution for yourself, please join us to help build a better system for everyone.
 
 <br />
 
-
 # 🧮 Tutorials
 
 - [Registering Data lineage](https://docs.pureml.com/docs/data/register_data_pipeline)
 - [Registering models](https://docs.pureml.com/docs/models/register_models)
 - [Quick Start: Tabular](https://docs.pureml.com/docs/get-started/quickstart_tabular)
 - [Quick Start: Computer Vision](https://docs.pureml.com/docs/get-started/quickstart_cv)
 - [Quick Start: NLP](https://docs.pureml.com/docs/get-started/quickstart_nlp)
 - [Logging](https://docs.pureml.com/docs/log/overview)
 
-
 <br />
 
 # 🐞 Reporting Bugs
+
 To report any bugs you have faced while using PureML package, please
+
 1. Report it in [Discord](https://discord.gg/xNUHt9yguJ) channel
 1. Open an [issue](https://github.com/PureML-Inc/PureML/issues)
 
 <br />
 
 # ⌨ Contributing and Developing
+
 Lets work together to improve the features for everyone. For more details, please look at out [Contributing Guide](./CONTRIBUTING.md)
 
 Work with mutual respect.
 
-
 <br />
 
 # 👨‍👩‍👧‍👦 Community
+
 To get quick updates, feature release for PureML follow us on
-|   |
+| |
 | --- |
 | [<img alt="Twitter" height="20" src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/getPureML) |
 [<img alt="LinkedIn" height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/company/pureml-inc/) |
 | [<img alt="GitHub" height="20" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/PureML-Inc/PureML) |
 | [<img alt="GitHub" height="20" src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" />](https://discord.gg/DBvedzGu) |
 
-
 # 📄 License
-See the [Apache-2.0](./License) file for licensing information.
-
 
+See the [Apache-2.0](./License) file for licensing information.
 
 <br />
```

