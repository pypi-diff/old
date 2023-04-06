# Comparing `tmp/trademaster406-0.0.1.tar.gz` & `tmp/trademaster406-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "trademaster406-0.0.1.tar", last modified: Thu Apr  6 13:25:13 2023, max compression
+gzip compressed data, was "trademaster406-0.0.2.tar", last modified: Thu Apr  6 13:34:28 2023, max compression
```

## Comparing `trademaster406-0.0.1.tar` & `trademaster406-0.0.2.tar`

### file list

```diff
@@ -1,177 +1,176 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.412154 trademaster406-0.0.1/
--rwxr-xr-x   0 root         (0) root         (0)    11558 2023-04-06 13:00:15.000000 trademaster406-0.0.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)    15950 2023-04-06 13:25:13.413154 trademaster406-0.0.1/PKG-INFO
--rwxr-xr-x   0 root         (0) root         (0)    15691 2023-04-06 13:00:15.000000 trademaster406-0.0.1/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.391152 trademaster406-0.0.1/configs/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:15.000000 trademaster406-0.0.1/configs/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.391152 trademaster406-0.0.1/configs/_base_/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:15.000000 trademaster406-0.0.1/configs/_base_/__init__.py
--rw-r--r--   0 root         (0) root         (0)      100 2023-04-06 13:23:58.000000 trademaster406-0.0.1/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)      527 2023-04-06 13:25:13.413154 trademaster406-0.0.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1335 2023-04-06 13:25:11.000000 trademaster406-0.0.1/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.391152 trademaster406-0.0.1/tools/
--rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.1/tools/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.391152 trademaster406-0.0.1/trademaster406/
--rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.392152 trademaster406-0.0.1/trademaster406/agents/
--rwxr-xr-x   0 root         (0) root         (0)      523 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.393153 trademaster406-0.0.1/trademaster406/agents/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       38 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     8135 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/algorithmic_trading/dqn.py
--rwxr-xr-x   0 root         (0) root         (0)      281 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      125 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.393153 trademaster406-0.0.1/trademaster406/agents/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       42 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9993 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/high_frequency_trading/ddqn.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.393153 trademaster406-0.0.1/trademaster406/agents/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)       70 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     8536 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/order_execution/eteo.py
--rwxr-xr-x   0 root         (0) root         (0)    15383 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/order_execution/pd.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.394152 trademaster406-0.0.1/trademaster406/agents/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      164 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    15287 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/portfolio_management/deeptrader.py
--rwxr-xr-x   0 root         (0) root         (0)     6631 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/portfolio_management/eiie.py
--rwxr-xr-x   0 root         (0) root         (0)     2239 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/agents/portfolio_management/investor_imitator.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.395153 trademaster406-0.0.1/trademaster406/collector/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/__init__.py
--rw-r--r--   0 root         (0) root         (0)      415 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/binance.py
--rwxr-xr-x   0 root         (0) root         (0)      300 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      130 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.396153 trademaster406-0.0.1/trademaster406/collector/helper/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/helper/__init__.py
--rw-r--r--   0 root         (0) root         (0)       95 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/helper/celery_app.py
--rw-r--r--   0 root         (0) root         (0)      344 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/helper/celery_config.py
--rw-r--r--   0 root         (0) root         (0)      968 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/helper/pika_connection.py
--rw-r--r--   0 root         (0) root         (0)      157 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/helper/run_celery.py
--rw-r--r--   0 root         (0) root         (0)      794 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/helper/websocket_consumer.py
--rw-r--r--   0 root         (0) root         (0)     3391 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/collector/helper/websocket_producer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.396153 trademaster406-0.0.1/trademaster406/datasets/
--rwxr-xr-x   0 root         (0) root         (0)      340 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.397153 trademaster406-0.0.1/trademaster406/datasets/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     3502 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/algorithmic_trading/dataset.py
--rwxr-xr-x   0 root         (0) root         (0)      290 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      320 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.397153 trademaster406-0.0.1/trademaster406/datasets/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3693 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/high_frequency_trading/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.397153 trademaster406-0.0.1/trademaster406/datasets/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)       42 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     3963 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/order_execution/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.397153 trademaster406-0.0.1/trademaster406/datasets/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)       47 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     4053 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/datasets/portfolio_management/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.398153 trademaster406-0.0.1/trademaster406/environments/
--rwxr-xr-x   0 root         (0) root         (0)      855 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.398153 trademaster406-0.0.1/trademaster406/environments/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       54 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    14512 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/algorithmic_trading/environment.py
--rwxr-xr-x   0 root         (0) root         (0)      321 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      191 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.399153 trademaster406-0.0.1/trademaster406/environments/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)      122 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)    32810 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/high_frequency_trading/environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.399153 trademaster406-0.0.1/trademaster406/environments/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)      116 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    21527 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/order_execution/eteo_environment.py
--rwxr-xr-x   0 root         (0) root         (0)     8469 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/order_execution/pd_environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.400153 trademaster406-0.0.1/trademaster406/environments/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      357 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    10053 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/portfolio_management/deeptrader_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    11513 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/portfolio_management/eiie_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    10348 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/portfolio_management/environment.py
--rwxr-xr-x   0 root         (0) root         (0)    19345 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/portfolio_management/inverstor_imitator_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    14016 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/environments/portfolio_management/sarl_environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.400153 trademaster406-0.0.1/trademaster406/evaluation/
--rw-r--r--   0 root         (0) root         (0)       56 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/evaluation/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.401153 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/
--rw-r--r--   0 root         (0) root         (0)      178 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/__init__.py
--rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/builder.py
--rw-r--r--   0 root         (0) root         (0)      163 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.401153 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/model/
--rw-r--r--   0 root         (0) root         (0)       54 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/model/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4479 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/model/linear_model.py
--rw-r--r--   0 root         (0) root         (0)     4332 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/model/run_linear_model.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.402153 trademaster406-0.0.1/trademaster406/imputation/
--rw-r--r--   0 root         (0) root         (0)      128 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/imputation/__init__.py
--rw-r--r--   0 root         (0) root         (0)      309 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/imputation/builder.py
--rw-r--r--   0 root         (0) root         (0)      282 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/imputation/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.403154 trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/
--rw-r--r--   0 root         (0) root         (0)       39 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7601 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/dataset.py
--rw-r--r--   0 root         (0) root         (0)    11328 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/imputation.py
--rw-r--r--   0 root         (0) root         (0)     6923 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.403154 trademaster406-0.0.1/trademaster406/losses/
--rwxr-xr-x   0 root         (0) root         (0)      118 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/losses/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      274 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/losses/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      381 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/losses/custom.py
--rw-r--r--   0 root         (0) root         (0)      583 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/losses/hft_loss.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.405154 trademaster406-0.0.1/trademaster406/nets/
--rwxr-xr-x   0 root         (0) root         (0)     9591 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/ASU.py
--rwxr-xr-x   0 root         (0) root         (0)     1570 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/MSU.py
--rwxr-xr-x   0 root         (0) root         (0)      366 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      263 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      159 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/custom.py
--rwxr-xr-x   0 root         (0) root         (0)    10598 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/deeptrader.py
--rwxr-xr-x   0 root         (0) root         (0)     1179 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/dqn.py
--rwxr-xr-x   0 root         (0) root         (0)     2423 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/eiie.py
--rwxr-xr-x   0 root         (0) root         (0)     1615 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/eteo.py
--rw-r--r--   0 root         (0) root         (0)     2075 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/high_frequency_trading_dqn.py
--rwxr-xr-x   0 root         (0) root         (0)     1401 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/investor_imitator.py
--rwxr-xr-x   0 root         (0) root         (0)     1393 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/pd.py
--rwxr-xr-x   0 root         (0) root         (0)     1930 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/nets/sarl.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.406154 trademaster406-0.0.1/trademaster406/optimizers/
--rwxr-xr-x   0 root         (0) root         (0)      166 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/optimizers/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      307 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/optimizers/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      708 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/optimizers/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.406154 trademaster406-0.0.1/trademaster406/preprocessor/
--rw-r--r--   0 root         (0) root         (0)      136 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/preprocessor/__init__.py
--rw-r--r--   0 root         (0) root         (0)      308 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/preprocessor/builder.py
--rw-r--r--   0 root         (0) root         (0)      299 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/preprocessor/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.407154 trademaster406-0.0.1/trademaster406/preprocessor/yfinance_preprocessor/
--rw-r--r--   0 root         (0) root         (0)       43 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/preprocessor/yfinance_preprocessor/__init__.py
--rw-r--r--   0 root         (0) root         (0)    34430 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/preprocessor/yfinance_preprocessor/processor.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.407154 trademaster406-0.0.1/trademaster406/pretrained/
--rwxr-xr-x   0 root         (0) root         (0)      335 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/pretrained/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.407154 trademaster406-0.0.1/trademaster406/trainers/
--rwxr-xr-x   0 root         (0) root         (0)      761 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.408154 trademaster406-0.0.1/trademaster406/trainers/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    16027 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/algorithmic_trading/trainer.py
--rwxr-xr-x   0 root         (0) root         (0)      271 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      154 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.408154 trademaster406-0.0.1/trademaster406/trainers/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9153 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/high_frequency_trading/trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.408154 trademaster406-0.0.1/trademaster406/trainers/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)      100 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    10583 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/order_execution/eteo_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    12102 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/order_execution/pd_trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.410154 trademaster406-0.0.1/trademaster406/trainers/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      316 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    13698 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/portfolio_management/deeptrader_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    10768 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/portfolio_management/eiie_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)     7023 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/portfolio_management/investor_imitator_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    11751 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/portfolio_management/sarl_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)     6616 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/trainers/portfolio_management/trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.411154 trademaster406-0.0.1/trademaster406/transition/
--rwxr-xr-x   0 root         (0) root         (0)      106 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/transition/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      314 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/transition/builder.py
--rwxr-xr-x   0 root         (0) root         (0)     1520 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/transition/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.412154 trademaster406-0.0.1/trademaster406/utils/
--rwxr-xr-x   0 root         (0) root         (0)      879 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/utils/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     4048 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/utils/general_replay_buffer.py
--rw-r--r--   0 root         (0) root         (0)    18681 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/utils/labeling_util.py
--rwxr-xr-x   0 root         (0) root         (0)     1057 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/utils/layers.py
--rwxr-xr-x   0 root         (0) root         (0)    17416 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/utils/misc.py
--rw-r--r--   0 root         (0) root         (0)    13758 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/utils/replay_buffer.py
--rwxr-xr-x   0 root         (0) root         (0)    19116 2023-04-06 13:00:20.000000 trademaster406-0.0.1/trademaster406/utils/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.392152 trademaster406-0.0.1/trademaster406.egg-info/
--rw-r--r--   0 root         (0) root         (0)    15950 2023-04-06 13:25:13.000000 trademaster406-0.0.1/trademaster406.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     6035 2023-04-06 13:25:13.000000 trademaster406-0.0.1/trademaster406.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 13:25:13.000000 trademaster406-0.0.1/trademaster406.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      226 2023-04-06 13:25:13.000000 trademaster406-0.0.1/trademaster406.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       42 2023-04-06 13:25:13.000000 trademaster406-0.0.1/trademaster406.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:25:13.412154 trademaster406-0.0.1/unit_testing/
--rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.1/unit_testing/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      276 2023-04-06 13:00:20.000000 trademaster406-0.0.1/unit_testing/test_core.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.185865 trademaster406-0.0.2/
+-rwxr-xr-x   0 root         (0) root         (0)    11558 2023-04-06 13:00:15.000000 trademaster406-0.0.2/LICENSE
+-rw-r--r--   0 root         (0) root         (0)    15950 2023-04-06 13:34:28.185865 trademaster406-0.0.2/PKG-INFO
+-rwxr-xr-x   0 root         (0) root         (0)    15691 2023-04-06 13:00:15.000000 trademaster406-0.0.2/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.160863 trademaster406-0.0.2/configs/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:15.000000 trademaster406-0.0.2/configs/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.161863 trademaster406-0.0.2/configs/_base_/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:15.000000 trademaster406-0.0.2/configs/_base_/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      100 2023-04-06 13:23:58.000000 trademaster406-0.0.2/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)      527 2023-04-06 13:34:28.186865 trademaster406-0.0.2/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     3876 2023-04-06 13:34:15.000000 trademaster406-0.0.2/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.161863 trademaster406-0.0.2/tools/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.2/tools/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.161863 trademaster406-0.0.2/trademaster406/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.162863 trademaster406-0.0.2/trademaster406/agents/
+-rwxr-xr-x   0 root         (0) root         (0)      523 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.162863 trademaster406-0.0.2/trademaster406/agents/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       38 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     8135 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/algorithmic_trading/dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)      281 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      125 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.163863 trademaster406-0.0.2/trademaster406/agents/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       42 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9993 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/high_frequency_trading/ddqn.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.163863 trademaster406-0.0.2/trademaster406/agents/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)       70 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     8536 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/order_execution/eteo.py
+-rwxr-xr-x   0 root         (0) root         (0)    15383 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/order_execution/pd.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.164863 trademaster406-0.0.2/trademaster406/agents/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      164 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    15287 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/portfolio_management/deeptrader.py
+-rwxr-xr-x   0 root         (0) root         (0)     6631 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/portfolio_management/eiie.py
+-rwxr-xr-x   0 root         (0) root         (0)     2239 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/agents/portfolio_management/investor_imitator.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.164863 trademaster406-0.0.2/trademaster406/collector/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      415 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/binance.py
+-rwxr-xr-x   0 root         (0) root         (0)      300 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      130 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.165863 trademaster406-0.0.2/trademaster406/collector/helper/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/helper/__init__.py
+-rw-r--r--   0 root         (0) root         (0)       95 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/helper/celery_app.py
+-rw-r--r--   0 root         (0) root         (0)      344 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/helper/celery_config.py
+-rw-r--r--   0 root         (0) root         (0)      968 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/helper/pika_connection.py
+-rw-r--r--   0 root         (0) root         (0)      157 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/helper/run_celery.py
+-rw-r--r--   0 root         (0) root         (0)      794 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/helper/websocket_consumer.py
+-rw-r--r--   0 root         (0) root         (0)     3391 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/collector/helper/websocket_producer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.166864 trademaster406-0.0.2/trademaster406/datasets/
+-rwxr-xr-x   0 root         (0) root         (0)      340 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.166864 trademaster406-0.0.2/trademaster406/datasets/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     3502 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/algorithmic_trading/dataset.py
+-rwxr-xr-x   0 root         (0) root         (0)      290 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      320 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.167864 trademaster406-0.0.2/trademaster406/datasets/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3693 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/high_frequency_trading/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.167864 trademaster406-0.0.2/trademaster406/datasets/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)       42 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     3963 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/order_execution/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.167864 trademaster406-0.0.2/trademaster406/datasets/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)       47 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     4053 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/datasets/portfolio_management/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.168864 trademaster406-0.0.2/trademaster406/environments/
+-rwxr-xr-x   0 root         (0) root         (0)      855 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.168864 trademaster406-0.0.2/trademaster406/environments/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       54 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    14512 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/algorithmic_trading/environment.py
+-rwxr-xr-x   0 root         (0) root         (0)      321 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      191 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.169864 trademaster406-0.0.2/trademaster406/environments/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)      122 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    32810 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/high_frequency_trading/environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.170864 trademaster406-0.0.2/trademaster406/environments/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)      116 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    21527 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/order_execution/eteo_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)     8469 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/order_execution/pd_environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.171864 trademaster406-0.0.2/trademaster406/environments/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      357 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    10053 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/portfolio_management/deeptrader_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    11513 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/portfolio_management/eiie_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    10348 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/portfolio_management/environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    19345 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/portfolio_management/inverstor_imitator_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    14016 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/environments/portfolio_management/sarl_environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.171864 trademaster406-0.0.2/trademaster406/evaluation/
+-rw-r--r--   0 root         (0) root         (0)       56 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/evaluation/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.172864 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/
+-rw-r--r--   0 root         (0) root         (0)      178 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/builder.py
+-rw-r--r--   0 root         (0) root         (0)      163 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.173864 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/model/
+-rw-r--r--   0 root         (0) root         (0)       54 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/model/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4479 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/model/linear_model.py
+-rw-r--r--   0 root         (0) root         (0)     4332 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/model/run_linear_model.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.173864 trademaster406-0.0.2/trademaster406/imputation/
+-rw-r--r--   0 root         (0) root         (0)      128 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/imputation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      309 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/imputation/builder.py
+-rw-r--r--   0 root         (0) root         (0)      282 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/imputation/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.174864 trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/
+-rw-r--r--   0 root         (0) root         (0)       39 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7601 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/dataset.py
+-rw-r--r--   0 root         (0) root         (0)    11328 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/imputation.py
+-rw-r--r--   0 root         (0) root         (0)     6923 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.175864 trademaster406-0.0.2/trademaster406/losses/
+-rwxr-xr-x   0 root         (0) root         (0)      118 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/losses/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      274 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/losses/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      381 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/losses/custom.py
+-rw-r--r--   0 root         (0) root         (0)      583 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/losses/hft_loss.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.177864 trademaster406-0.0.2/trademaster406/nets/
+-rwxr-xr-x   0 root         (0) root         (0)     9591 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/ASU.py
+-rwxr-xr-x   0 root         (0) root         (0)     1570 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/MSU.py
+-rwxr-xr-x   0 root         (0) root         (0)      366 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      263 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      159 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/custom.py
+-rwxr-xr-x   0 root         (0) root         (0)    10598 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/deeptrader.py
+-rwxr-xr-x   0 root         (0) root         (0)     1179 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)     2423 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/eiie.py
+-rwxr-xr-x   0 root         (0) root         (0)     1615 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/eteo.py
+-rw-r--r--   0 root         (0) root         (0)     2075 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/high_frequency_trading_dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)     1401 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/investor_imitator.py
+-rwxr-xr-x   0 root         (0) root         (0)     1393 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/pd.py
+-rwxr-xr-x   0 root         (0) root         (0)     1930 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/nets/sarl.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.178865 trademaster406-0.0.2/trademaster406/optimizers/
+-rwxr-xr-x   0 root         (0) root         (0)      166 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/optimizers/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      307 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/optimizers/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      708 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/optimizers/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.178865 trademaster406-0.0.2/trademaster406/preprocessor/
+-rw-r--r--   0 root         (0) root         (0)      136 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/preprocessor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      308 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/preprocessor/builder.py
+-rw-r--r--   0 root         (0) root         (0)      299 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/preprocessor/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.179865 trademaster406-0.0.2/trademaster406/preprocessor/yfinance_preprocessor/
+-rw-r--r--   0 root         (0) root         (0)       43 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/preprocessor/yfinance_preprocessor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    34430 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/preprocessor/yfinance_preprocessor/processor.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.179865 trademaster406-0.0.2/trademaster406/pretrained/
+-rwxr-xr-x   0 root         (0) root         (0)      335 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/pretrained/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.179865 trademaster406-0.0.2/trademaster406/trainers/
+-rwxr-xr-x   0 root         (0) root         (0)      761 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.180865 trademaster406-0.0.2/trademaster406/trainers/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    16027 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/algorithmic_trading/trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)      271 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      154 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.180865 trademaster406-0.0.2/trademaster406/trainers/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9153 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/high_frequency_trading/trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.181865 trademaster406-0.0.2/trademaster406/trainers/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)      100 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    10583 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/order_execution/eteo_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    12102 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/order_execution/pd_trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.182865 trademaster406-0.0.2/trademaster406/trainers/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      316 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    13698 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/portfolio_management/deeptrader_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    10768 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/portfolio_management/eiie_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)     7023 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/portfolio_management/investor_imitator_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    11751 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/portfolio_management/sarl_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)     6616 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/trainers/portfolio_management/trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.183865 trademaster406-0.0.2/trademaster406/transition/
+-rwxr-xr-x   0 root         (0) root         (0)      106 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/transition/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      314 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/transition/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)     1520 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/transition/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.184865 trademaster406-0.0.2/trademaster406/utils/
+-rwxr-xr-x   0 root         (0) root         (0)      879 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/utils/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     4048 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/utils/general_replay_buffer.py
+-rw-r--r--   0 root         (0) root         (0)    18681 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/utils/labeling_util.py
+-rwxr-xr-x   0 root         (0) root         (0)     1057 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/utils/layers.py
+-rwxr-xr-x   0 root         (0) root         (0)    17416 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/utils/misc.py
+-rw-r--r--   0 root         (0) root         (0)    13758 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/utils/replay_buffer.py
+-rwxr-xr-x   0 root         (0) root         (0)    19116 2023-04-06 13:00:20.000000 trademaster406-0.0.2/trademaster406/utils/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.161863 trademaster406-0.0.2/trademaster406.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    15950 2023-04-06 13:34:27.000000 trademaster406-0.0.2/trademaster406.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     5998 2023-04-06 13:34:27.000000 trademaster406-0.0.2/trademaster406.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 13:34:27.000000 trademaster406-0.0.2/trademaster406.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       42 2023-04-06 13:34:27.000000 trademaster406-0.0.2/trademaster406.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:34:28.185865 trademaster406-0.0.2/unit_testing/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:00:20.000000 trademaster406-0.0.2/unit_testing/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      276 2023-04-06 13:00:20.000000 trademaster406-0.0.2/unit_testing/test_core.py
```

### Comparing `trademaster406-0.0.1/LICENSE` & `trademaster406-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/PKG-INFO` & `trademaster406-0.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster406
-Version: 0.0.1
+Version: 0.0.2
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: TradeMaster.NTU@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `trademaster406-0.0.1/README.md` & `trademaster406-0.0.2/README.md`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/setup.cfg` & `trademaster406-0.0.2/setup.cfg`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/__init__.py` & `trademaster406-0.0.2/trademaster406/agents/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/algorithmic_trading/dqn.py` & `trademaster406-0.0.2/trademaster406/agents/algorithmic_trading/dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/high_frequency_trading/ddqn.py` & `trademaster406-0.0.2/trademaster406/agents/high_frequency_trading/ddqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/order_execution/eteo.py` & `trademaster406-0.0.2/trademaster406/agents/order_execution/eteo.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/order_execution/pd.py` & `trademaster406-0.0.2/trademaster406/agents/order_execution/pd.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/portfolio_management/deeptrader.py` & `trademaster406-0.0.2/trademaster406/agents/portfolio_management/deeptrader.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/portfolio_management/eiie.py` & `trademaster406-0.0.2/trademaster406/agents/portfolio_management/eiie.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/agents/portfolio_management/investor_imitator.py` & `trademaster406-0.0.2/trademaster406/agents/portfolio_management/investor_imitator.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/collector/helper/pika_connection.py` & `trademaster406-0.0.2/trademaster406/collector/helper/pika_connection.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/collector/helper/websocket_consumer.py` & `trademaster406-0.0.2/trademaster406/collector/helper/websocket_consumer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/collector/helper/websocket_producer.py` & `trademaster406-0.0.2/trademaster406/collector/helper/websocket_producer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/datasets/algorithmic_trading/dataset.py` & `trademaster406-0.0.2/trademaster406/datasets/algorithmic_trading/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/datasets/high_frequency_trading/dataset.py` & `trademaster406-0.0.2/trademaster406/datasets/high_frequency_trading/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/datasets/order_execution/dataset.py` & `trademaster406-0.0.2/trademaster406/datasets/order_execution/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/datasets/portfolio_management/dataset.py` & `trademaster406-0.0.2/trademaster406/datasets/portfolio_management/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/__init__.py` & `trademaster406-0.0.2/trademaster406/environments/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/algorithmic_trading/environment.py` & `trademaster406-0.0.2/trademaster406/environments/algorithmic_trading/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/high_frequency_trading/environment.py` & `trademaster406-0.0.2/trademaster406/environments/high_frequency_trading/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/order_execution/eteo_environment.py` & `trademaster406-0.0.2/trademaster406/environments/order_execution/eteo_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/order_execution/pd_environment.py` & `trademaster406-0.0.2/trademaster406/environments/order_execution/pd_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/portfolio_management/deeptrader_environment.py` & `trademaster406-0.0.2/trademaster406/environments/portfolio_management/deeptrader_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/portfolio_management/eiie_environment.py` & `trademaster406-0.0.2/trademaster406/environments/portfolio_management/eiie_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/portfolio_management/environment.py` & `trademaster406-0.0.2/trademaster406/environments/portfolio_management/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/portfolio_management/inverstor_imitator_environment.py` & `trademaster406-0.0.2/trademaster406/environments/portfolio_management/inverstor_imitator_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/environments/portfolio_management/sarl_environment.py` & `trademaster406-0.0.2/trademaster406/environments/portfolio_management/sarl_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/model/linear_model.py` & `trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/model/linear_model.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/evaluation/market_dynamics_labeling/model/run_linear_model.py` & `trademaster406-0.0.2/trademaster406/evaluation/market_dynamics_labeling/model/run_linear_model.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/dataset.py` & `trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/imputation.py` & `trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/imputation.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/imputation/missing_value_imputation/utils.py` & `trademaster406-0.0.2/trademaster406/imputation/missing_value_imputation/utils.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/losses/hft_loss.py` & `trademaster406-0.0.2/trademaster406/losses/hft_loss.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/ASU.py` & `trademaster406-0.0.2/trademaster406/nets/ASU.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/MSU.py` & `trademaster406-0.0.2/trademaster406/nets/MSU.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/deeptrader.py` & `trademaster406-0.0.2/trademaster406/nets/deeptrader.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/dqn.py` & `trademaster406-0.0.2/trademaster406/nets/dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/eiie.py` & `trademaster406-0.0.2/trademaster406/nets/eiie.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/eteo.py` & `trademaster406-0.0.2/trademaster406/nets/eteo.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/high_frequency_trading_dqn.py` & `trademaster406-0.0.2/trademaster406/nets/high_frequency_trading_dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/investor_imitator.py` & `trademaster406-0.0.2/trademaster406/nets/investor_imitator.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/pd.py` & `trademaster406-0.0.2/trademaster406/nets/pd.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/nets/sarl.py` & `trademaster406-0.0.2/trademaster406/nets/sarl.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/optimizers/custom.py` & `trademaster406-0.0.2/trademaster406/optimizers/custom.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/preprocessor/yfinance_preprocessor/processor.py` & `trademaster406-0.0.2/trademaster406/preprocessor/yfinance_preprocessor/processor.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/__init__.py` & `trademaster406-0.0.2/trademaster406/trainers/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/algorithmic_trading/trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/algorithmic_trading/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/high_frequency_trading/trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/high_frequency_trading/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/order_execution/eteo_trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/order_execution/eteo_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/order_execution/pd_trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/order_execution/pd_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/portfolio_management/deeptrader_trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/portfolio_management/deeptrader_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/portfolio_management/eiie_trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/portfolio_management/eiie_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/portfolio_management/investor_imitator_trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/portfolio_management/investor_imitator_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/portfolio_management/sarl_trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/portfolio_management/sarl_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/trainers/portfolio_management/trainer.py` & `trademaster406-0.0.2/trademaster406/trainers/portfolio_management/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/transition/custom.py` & `trademaster406-0.0.2/trademaster406/transition/custom.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/utils/__init__.py` & `trademaster406-0.0.2/trademaster406/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/utils/general_replay_buffer.py` & `trademaster406-0.0.2/trademaster406/utils/general_replay_buffer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/utils/labeling_util.py` & `trademaster406-0.0.2/trademaster406/utils/labeling_util.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/utils/layers.py` & `trademaster406-0.0.2/trademaster406/utils/layers.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/utils/misc.py` & `trademaster406-0.0.2/trademaster406/utils/misc.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/utils/replay_buffer.py` & `trademaster406-0.0.2/trademaster406/utils/replay_buffer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406/utils/utils.py` & `trademaster406-0.0.2/trademaster406/utils/utils.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.1/trademaster406.egg-info/PKG-INFO` & `trademaster406-0.0.2/trademaster406.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster406
-Version: 0.0.1
+Version: 0.0.2
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: TradeMaster.NTU@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `trademaster406-0.0.1/trademaster406.egg-info/SOURCES.txt` & `trademaster406-0.0.2/trademaster406.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -6,15 +6,14 @@
 configs/__init__.py
 configs/_base_/__init__.py
 tools/__init__.py
 trademaster406/__init__.py
 trademaster406.egg-info/PKG-INFO
 trademaster406.egg-info/SOURCES.txt
 trademaster406.egg-info/dependency_links.txt
-trademaster406.egg-info/requires.txt
 trademaster406.egg-info/top_level.txt
 trademaster406/agents/__init__.py
 trademaster406/agents/builder.py
 trademaster406/agents/custom.py
 trademaster406/agents/algorithmic_trading/__init__.py
 trademaster406/agents/algorithmic_trading/dqn.py
 trademaster406/agents/high_frequency_trading/__init__.py
```

