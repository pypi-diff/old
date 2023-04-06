# Comparing `tmp/trademaster406-0.0.3.tar.gz` & `tmp/trademaster406-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "trademaster406-0.0.3.tar", last modified: Thu Apr  6 13:46:05 2023, max compression
+gzip compressed data, was "trademaster406-0.0.4.tar", last modified: Thu Apr  6 13:48:58 2023, max compression
```

## Comparing `trademaster406-0.0.3.tar` & `trademaster406-0.0.4.tar`

### file list

```diff
@@ -1,178 +1,178 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.474202 trademaster406-0.0.3/
--rwxr-xr-x   0 root         (0) root         (0)    11558 2023-04-06 13:40:00.000000 trademaster406-0.0.3/LICENSE
--rw-r--r--   0 root         (0) root         (0)    16179 2023-04-06 13:46:05.474202 trademaster406-0.0.3/PKG-INFO
--rwxr-xr-x   0 root         (0) root         (0)    15691 2023-04-06 13:40:00.000000 trademaster406-0.0.3/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.448199 trademaster406-0.0.3/configs/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:00.000000 trademaster406-0.0.3/configs/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.448199 trademaster406-0.0.3/configs/_base_/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:00.000000 trademaster406-0.0.3/configs/_base_/__init__.py
--rw-r--r--   0 root         (0) root         (0)      100 2023-04-06 13:45:52.000000 trademaster406-0.0.3/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 13:46:05.474202 trademaster406-0.0.3/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     7700 2023-04-06 13:46:02.000000 trademaster406-0.0.3/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.448199 trademaster406-0.0.3/tools/
--rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.3/tools/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.448199 trademaster406-0.0.3/trademaster/
--rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.449199 trademaster406-0.0.3/trademaster/agents/
--rwxr-xr-x   0 root         (0) root         (0)      523 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.449199 trademaster406-0.0.3/trademaster/agents/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       38 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     8135 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/algorithmic_trading/dqn.py
--rwxr-xr-x   0 root         (0) root         (0)      281 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      125 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.450199 trademaster406-0.0.3/trademaster/agents/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       42 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9993 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/high_frequency_trading/ddqn.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.450199 trademaster406-0.0.3/trademaster/agents/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)       70 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     8536 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/order_execution/eteo.py
--rwxr-xr-x   0 root         (0) root         (0)    15383 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/order_execution/pd.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.451200 trademaster406-0.0.3/trademaster/agents/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      164 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    15287 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/portfolio_management/deeptrader.py
--rwxr-xr-x   0 root         (0) root         (0)     6631 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/portfolio_management/eiie.py
--rwxr-xr-x   0 root         (0) root         (0)     2239 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/agents/portfolio_management/investor_imitator.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.451200 trademaster406-0.0.3/trademaster/collector/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/__init__.py
--rw-r--r--   0 root         (0) root         (0)      415 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/binance.py
--rwxr-xr-x   0 root         (0) root         (0)      300 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      130 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.453200 trademaster406-0.0.3/trademaster/collector/helper/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/helper/__init__.py
--rw-r--r--   0 root         (0) root         (0)       95 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/helper/celery_app.py
--rw-r--r--   0 root         (0) root         (0)      344 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/helper/celery_config.py
--rw-r--r--   0 root         (0) root         (0)      968 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/helper/pika_connection.py
--rw-r--r--   0 root         (0) root         (0)      157 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/helper/run_celery.py
--rw-r--r--   0 root         (0) root         (0)      794 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/helper/websocket_consumer.py
--rw-r--r--   0 root         (0) root         (0)     3391 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/collector/helper/websocket_producer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.453200 trademaster406-0.0.3/trademaster/datasets/
--rwxr-xr-x   0 root         (0) root         (0)      340 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.453200 trademaster406-0.0.3/trademaster/datasets/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     3502 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/algorithmic_trading/dataset.py
--rwxr-xr-x   0 root         (0) root         (0)      290 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      320 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.454200 trademaster406-0.0.3/trademaster/datasets/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3693 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/high_frequency_trading/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.455200 trademaster406-0.0.3/trademaster/datasets/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)       42 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     3963 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/order_execution/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.455200 trademaster406-0.0.3/trademaster/datasets/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)       47 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     4053 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/datasets/portfolio_management/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.455200 trademaster406-0.0.3/trademaster/environments/
--rwxr-xr-x   0 root         (0) root         (0)      855 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.456200 trademaster406-0.0.3/trademaster/environments/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       54 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    14512 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/algorithmic_trading/environment.py
--rwxr-xr-x   0 root         (0) root         (0)      321 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      191 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.456200 trademaster406-0.0.3/trademaster/environments/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)      122 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)    32810 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/high_frequency_trading/environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.457200 trademaster406-0.0.3/trademaster/environments/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)      116 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    21527 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/order_execution/eteo_environment.py
--rwxr-xr-x   0 root         (0) root         (0)     8469 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/order_execution/pd_environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.458200 trademaster406-0.0.3/trademaster/environments/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      357 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    10053 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/portfolio_management/deeptrader_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    11513 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/portfolio_management/eiie_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    10348 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/portfolio_management/environment.py
--rwxr-xr-x   0 root         (0) root         (0)    19345 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/portfolio_management/inverstor_imitator_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    14016 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/environments/portfolio_management/sarl_environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.458200 trademaster406-0.0.3/trademaster/evaluation/
--rw-r--r--   0 root         (0) root         (0)       56 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/evaluation/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.459200 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/
--rw-r--r--   0 root         (0) root         (0)      178 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/__init__.py
--rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/builder.py
--rw-r--r--   0 root         (0) root         (0)      163 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.460200 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/model/
--rw-r--r--   0 root         (0) root         (0)       54 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/model/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4479 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/model/linear_model.py
--rw-r--r--   0 root         (0) root         (0)     4332 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/model/run_linear_model.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.460200 trademaster406-0.0.3/trademaster/imputation/
--rw-r--r--   0 root         (0) root         (0)      128 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/imputation/__init__.py
--rw-r--r--   0 root         (0) root         (0)      309 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/imputation/builder.py
--rw-r--r--   0 root         (0) root         (0)      282 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/imputation/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.461200 trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/
--rw-r--r--   0 root         (0) root         (0)       39 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7601 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/dataset.py
--rw-r--r--   0 root         (0) root         (0)    11328 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/imputation.py
--rw-r--r--   0 root         (0) root         (0)     6923 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.462200 trademaster406-0.0.3/trademaster/losses/
--rwxr-xr-x   0 root         (0) root         (0)      118 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/losses/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      274 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/losses/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      381 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/losses/custom.py
--rw-r--r--   0 root         (0) root         (0)      583 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/losses/hft_loss.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.464201 trademaster406-0.0.3/trademaster/nets/
--rwxr-xr-x   0 root         (0) root         (0)     9591 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/ASU.py
--rwxr-xr-x   0 root         (0) root         (0)     1570 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/MSU.py
--rwxr-xr-x   0 root         (0) root         (0)      366 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      263 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      159 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/custom.py
--rwxr-xr-x   0 root         (0) root         (0)    10598 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/deeptrader.py
--rwxr-xr-x   0 root         (0) root         (0)     1179 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/dqn.py
--rwxr-xr-x   0 root         (0) root         (0)     2423 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/eiie.py
--rwxr-xr-x   0 root         (0) root         (0)     1615 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/eteo.py
--rw-r--r--   0 root         (0) root         (0)     2075 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/high_frequency_trading_dqn.py
--rwxr-xr-x   0 root         (0) root         (0)     1401 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/investor_imitator.py
--rwxr-xr-x   0 root         (0) root         (0)     1393 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/pd.py
--rwxr-xr-x   0 root         (0) root         (0)     1930 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/nets/sarl.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.464201 trademaster406-0.0.3/trademaster/optimizers/
--rwxr-xr-x   0 root         (0) root         (0)      166 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/optimizers/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      307 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/optimizers/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      708 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/optimizers/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.465201 trademaster406-0.0.3/trademaster/preprocessor/
--rw-r--r--   0 root         (0) root         (0)      136 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/preprocessor/__init__.py
--rw-r--r--   0 root         (0) root         (0)      308 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/preprocessor/builder.py
--rw-r--r--   0 root         (0) root         (0)      299 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/preprocessor/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.465201 trademaster406-0.0.3/trademaster/preprocessor/yfinance_preprocessor/
--rw-r--r--   0 root         (0) root         (0)       43 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/preprocessor/yfinance_preprocessor/__init__.py
--rw-r--r--   0 root         (0) root         (0)    34430 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/preprocessor/yfinance_preprocessor/processor.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.465201 trademaster406-0.0.3/trademaster/pretrained/
--rwxr-xr-x   0 root         (0) root         (0)      335 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/pretrained/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.466201 trademaster406-0.0.3/trademaster/trainers/
--rwxr-xr-x   0 root         (0) root         (0)      761 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.468201 trademaster406-0.0.3/trademaster/trainers/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    16027 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/algorithmic_trading/trainer.py
--rwxr-xr-x   0 root         (0) root         (0)      271 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      154 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.468201 trademaster406-0.0.3/trademaster/trainers/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9153 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/high_frequency_trading/trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.469201 trademaster406-0.0.3/trademaster/trainers/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)      100 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    10583 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/order_execution/eteo_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    12102 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/order_execution/pd_trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.470201 trademaster406-0.0.3/trademaster/trainers/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      316 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    13698 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/portfolio_management/deeptrader_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    10768 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/portfolio_management/eiie_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)     7023 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/portfolio_management/investor_imitator_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    11751 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/portfolio_management/sarl_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)     6616 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/trainers/portfolio_management/trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.470201 trademaster406-0.0.3/trademaster/transition/
--rwxr-xr-x   0 root         (0) root         (0)      106 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/transition/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      314 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/transition/builder.py
--rwxr-xr-x   0 root         (0) root         (0)     1520 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/transition/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.472201 trademaster406-0.0.3/trademaster/utils/
--rwxr-xr-x   0 root         (0) root         (0)      879 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/utils/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     4048 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/utils/general_replay_buffer.py
--rw-r--r--   0 root         (0) root         (0)    18681 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/utils/labeling_util.py
--rwxr-xr-x   0 root         (0) root         (0)     1057 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/utils/layers.py
--rwxr-xr-x   0 root         (0) root         (0)    17416 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/utils/misc.py
--rw-r--r--   0 root         (0) root         (0)    13758 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/utils/replay_buffer.py
--rwxr-xr-x   0 root         (0) root         (0)    19116 2023-04-06 13:40:04.000000 trademaster406-0.0.3/trademaster/utils/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.473201 trademaster406-0.0.3/trademaster406.egg-info/
--rw-r--r--   0 root         (0) root         (0)    16179 2023-04-06 13:46:05.000000 trademaster406-0.0.3/trademaster406.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     5705 2023-04-06 13:46:05.000000 trademaster406-0.0.3/trademaster406.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 13:46:05.000000 trademaster406-0.0.3/trademaster406.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 13:46:05.000000 trademaster406-0.0.3/trademaster406.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      264 2023-04-06 13:46:05.000000 trademaster406-0.0.3/trademaster406.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       39 2023-04-06 13:46:05.000000 trademaster406-0.0.3/trademaster406.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:46:05.473201 trademaster406-0.0.3/unit_testing/
--rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.3/unit_testing/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      276 2023-04-06 13:40:04.000000 trademaster406-0.0.3/unit_testing/test_core.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.205385 trademaster406-0.0.4/
+-rwxr-xr-x   0 root         (0) root         (0)    11558 2023-04-06 13:40:00.000000 trademaster406-0.0.4/LICENSE
+-rw-r--r--   0 root         (0) root         (0)    16179 2023-04-06 13:48:58.205385 trademaster406-0.0.4/PKG-INFO
+-rwxr-xr-x   0 root         (0) root         (0)    15691 2023-04-06 13:40:00.000000 trademaster406-0.0.4/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.189383 trademaster406-0.0.4/configs/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:00.000000 trademaster406-0.0.4/configs/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.189383 trademaster406-0.0.4/configs/_base_/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:00.000000 trademaster406-0.0.4/configs/_base_/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      100 2023-04-06 13:45:52.000000 trademaster406-0.0.4/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 13:48:58.205385 trademaster406-0.0.4/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     7700 2023-04-06 13:48:33.000000 trademaster406-0.0.4/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.189383 trademaster406-0.0.4/tools/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.4/tools/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.190384 trademaster406-0.0.4/trademaster406/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.191383 trademaster406-0.0.4/trademaster406/agents/
+-rwxr-xr-x   0 root         (0) root         (0)      523 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.191383 trademaster406-0.0.4/trademaster406/agents/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       38 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     8135 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/algorithmic_trading/dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)      281 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      125 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.191383 trademaster406-0.0.4/trademaster406/agents/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       42 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9993 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/high_frequency_trading/ddqn.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.191383 trademaster406-0.0.4/trademaster406/agents/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)       70 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     8536 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/order_execution/eteo.py
+-rwxr-xr-x   0 root         (0) root         (0)    15383 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/order_execution/pd.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.192384 trademaster406-0.0.4/trademaster406/agents/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      164 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    15287 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/portfolio_management/deeptrader.py
+-rwxr-xr-x   0 root         (0) root         (0)     6631 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/portfolio_management/eiie.py
+-rwxr-xr-x   0 root         (0) root         (0)     2239 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/agents/portfolio_management/investor_imitator.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.192384 trademaster406-0.0.4/trademaster406/collector/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      415 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/binance.py
+-rwxr-xr-x   0 root         (0) root         (0)      300 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      130 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.193384 trademaster406-0.0.4/trademaster406/collector/helper/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/helper/__init__.py
+-rw-r--r--   0 root         (0) root         (0)       95 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/helper/celery_app.py
+-rw-r--r--   0 root         (0) root         (0)      344 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/helper/celery_config.py
+-rw-r--r--   0 root         (0) root         (0)      968 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/helper/pika_connection.py
+-rw-r--r--   0 root         (0) root         (0)      157 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/helper/run_celery.py
+-rw-r--r--   0 root         (0) root         (0)      794 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/helper/websocket_consumer.py
+-rw-r--r--   0 root         (0) root         (0)     3391 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/collector/helper/websocket_producer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.193384 trademaster406-0.0.4/trademaster406/datasets/
+-rwxr-xr-x   0 root         (0) root         (0)      340 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.194384 trademaster406-0.0.4/trademaster406/datasets/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     3502 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/algorithmic_trading/dataset.py
+-rwxr-xr-x   0 root         (0) root         (0)      290 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      320 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.194384 trademaster406-0.0.4/trademaster406/datasets/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3693 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/high_frequency_trading/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.194384 trademaster406-0.0.4/trademaster406/datasets/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)       42 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     3963 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/order_execution/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.194384 trademaster406-0.0.4/trademaster406/datasets/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)       47 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     4053 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/datasets/portfolio_management/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.195384 trademaster406-0.0.4/trademaster406/environments/
+-rwxr-xr-x   0 root         (0) root         (0)      855 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.195384 trademaster406-0.0.4/trademaster406/environments/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       54 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    14512 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/algorithmic_trading/environment.py
+-rwxr-xr-x   0 root         (0) root         (0)      321 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      191 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.195384 trademaster406-0.0.4/trademaster406/environments/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)      122 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    32810 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/high_frequency_trading/environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.196384 trademaster406-0.0.4/trademaster406/environments/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)      116 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    21527 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/order_execution/eteo_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)     8469 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/order_execution/pd_environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.196384 trademaster406-0.0.4/trademaster406/environments/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      357 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    10053 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/portfolio_management/deeptrader_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    11513 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/portfolio_management/eiie_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    10348 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/portfolio_management/environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    19345 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/portfolio_management/inverstor_imitator_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    14016 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/environments/portfolio_management/sarl_environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.197384 trademaster406-0.0.4/trademaster406/evaluation/
+-rw-r--r--   0 root         (0) root         (0)       56 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/evaluation/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.197384 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/
+-rw-r--r--   0 root         (0) root         (0)      178 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/builder.py
+-rw-r--r--   0 root         (0) root         (0)      163 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.197384 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/model/
+-rw-r--r--   0 root         (0) root         (0)       54 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/model/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4479 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/model/linear_model.py
+-rw-r--r--   0 root         (0) root         (0)     4332 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/model/run_linear_model.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.198384 trademaster406-0.0.4/trademaster406/imputation/
+-rw-r--r--   0 root         (0) root         (0)      128 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/imputation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      309 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/imputation/builder.py
+-rw-r--r--   0 root         (0) root         (0)      282 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/imputation/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.198384 trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/
+-rw-r--r--   0 root         (0) root         (0)       39 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7601 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/dataset.py
+-rw-r--r--   0 root         (0) root         (0)    11328 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/imputation.py
+-rw-r--r--   0 root         (0) root         (0)     6923 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.199384 trademaster406-0.0.4/trademaster406/losses/
+-rwxr-xr-x   0 root         (0) root         (0)      118 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/losses/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      274 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/losses/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      381 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/losses/custom.py
+-rw-r--r--   0 root         (0) root         (0)      583 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/losses/hft_loss.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.200384 trademaster406-0.0.4/trademaster406/nets/
+-rwxr-xr-x   0 root         (0) root         (0)     9591 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/ASU.py
+-rwxr-xr-x   0 root         (0) root         (0)     1570 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/MSU.py
+-rwxr-xr-x   0 root         (0) root         (0)      366 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      263 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      159 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/custom.py
+-rwxr-xr-x   0 root         (0) root         (0)    10598 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/deeptrader.py
+-rwxr-xr-x   0 root         (0) root         (0)     1179 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)     2423 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/eiie.py
+-rwxr-xr-x   0 root         (0) root         (0)     1615 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/eteo.py
+-rw-r--r--   0 root         (0) root         (0)     2075 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/high_frequency_trading_dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)     1401 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/investor_imitator.py
+-rwxr-xr-x   0 root         (0) root         (0)     1393 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/pd.py
+-rwxr-xr-x   0 root         (0) root         (0)     1930 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/nets/sarl.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.200384 trademaster406-0.0.4/trademaster406/optimizers/
+-rwxr-xr-x   0 root         (0) root         (0)      166 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/optimizers/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      307 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/optimizers/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      708 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/optimizers/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.201384 trademaster406-0.0.4/trademaster406/preprocessor/
+-rw-r--r--   0 root         (0) root         (0)      136 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/preprocessor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      308 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/preprocessor/builder.py
+-rw-r--r--   0 root         (0) root         (0)      299 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/preprocessor/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.201384 trademaster406-0.0.4/trademaster406/preprocessor/yfinance_preprocessor/
+-rw-r--r--   0 root         (0) root         (0)       43 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/preprocessor/yfinance_preprocessor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    34430 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/preprocessor/yfinance_preprocessor/processor.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.201384 trademaster406-0.0.4/trademaster406/pretrained/
+-rwxr-xr-x   0 root         (0) root         (0)      335 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/pretrained/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.201384 trademaster406-0.0.4/trademaster406/trainers/
+-rwxr-xr-x   0 root         (0) root         (0)      761 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.202385 trademaster406-0.0.4/trademaster406/trainers/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    16027 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/algorithmic_trading/trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)      271 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      154 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.202385 trademaster406-0.0.4/trademaster406/trainers/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       48 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9153 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/high_frequency_trading/trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.202385 trademaster406-0.0.4/trademaster406/trainers/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)      100 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    10583 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/order_execution/eteo_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    12102 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/order_execution/pd_trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.203384 trademaster406-0.0.4/trademaster406/trainers/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      316 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    13698 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/portfolio_management/deeptrader_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    10768 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/portfolio_management/eiie_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)     7023 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/portfolio_management/investor_imitator_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    11751 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/portfolio_management/sarl_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)     6616 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/trainers/portfolio_management/trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.204385 trademaster406-0.0.4/trademaster406/transition/
+-rwxr-xr-x   0 root         (0) root         (0)      106 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/transition/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      314 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/transition/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)     1520 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/transition/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.204385 trademaster406-0.0.4/trademaster406/utils/
+-rwxr-xr-x   0 root         (0) root         (0)      879 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/utils/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     4048 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/utils/general_replay_buffer.py
+-rw-r--r--   0 root         (0) root         (0)    18681 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/utils/labeling_util.py
+-rwxr-xr-x   0 root         (0) root         (0)     1057 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/utils/layers.py
+-rwxr-xr-x   0 root         (0) root         (0)    17416 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/utils/misc.py
+-rw-r--r--   0 root         (0) root         (0)    13758 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/utils/replay_buffer.py
+-rwxr-xr-x   0 root         (0) root         (0)    19116 2023-04-06 13:40:04.000000 trademaster406-0.0.4/trademaster406/utils/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.190384 trademaster406-0.0.4/trademaster406.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    16179 2023-04-06 13:48:58.000000 trademaster406-0.0.4/trademaster406.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     6062 2023-04-06 13:48:58.000000 trademaster406-0.0.4/trademaster406.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 13:48:58.000000 trademaster406-0.0.4/trademaster406.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 13:46:05.000000 trademaster406-0.0.4/trademaster406.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      264 2023-04-06 13:48:58.000000 trademaster406-0.0.4/trademaster406.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       42 2023-04-06 13:48:58.000000 trademaster406-0.0.4/trademaster406.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:48:58.205385 trademaster406-0.0.4/unit_testing/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 13:40:04.000000 trademaster406-0.0.4/unit_testing/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      276 2023-04-06 13:40:04.000000 trademaster406-0.0.4/unit_testing/test_core.py
```

### Comparing `trademaster406-0.0.3/LICENSE` & `trademaster406-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/PKG-INFO` & `trademaster406-0.0.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster406
-Version: 0.0.3
+Version: 0.0.4
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: TradeMaster.NTU@gmail.com
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `trademaster406-0.0.3/README.md` & `trademaster406-0.0.4/README.md`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/setup.py` & `trademaster406-0.0.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -184,15 +184,15 @@
 with open('README.md', "r") as fh:
     long_description = fh.read()
 
 if __name__ == '__main__':
     add_mim_extension()
     setup(
       name='trademaster406',
-      version='0.0.3',
+      version='0.0.4',
       description='TradeMaster - A platform for algorithmic trading',
       long_description=long_description,
       long_description_content_type="text/markdown",
       author='NTU_trademaster',
       author_email='TradeMaster.NTU@gmail.com',
       url='https://github.com/TradeMaster-NTU/TradeMaster',
       packages=find_packages(),
```

### Comparing `trademaster406-0.0.3/trademaster/agents/__init__.py` & `trademaster406-0.0.4/trademaster406/agents/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/agents/algorithmic_trading/dqn.py` & `trademaster406-0.0.4/trademaster406/agents/algorithmic_trading/dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/agents/high_frequency_trading/ddqn.py` & `trademaster406-0.0.4/trademaster406/agents/high_frequency_trading/ddqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/agents/order_execution/eteo.py` & `trademaster406-0.0.4/trademaster406/agents/order_execution/eteo.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/agents/order_execution/pd.py` & `trademaster406-0.0.4/trademaster406/agents/order_execution/pd.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/agents/portfolio_management/deeptrader.py` & `trademaster406-0.0.4/trademaster406/agents/portfolio_management/deeptrader.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/agents/portfolio_management/eiie.py` & `trademaster406-0.0.4/trademaster406/agents/portfolio_management/eiie.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/agents/portfolio_management/investor_imitator.py` & `trademaster406-0.0.4/trademaster406/agents/portfolio_management/investor_imitator.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/collector/helper/pika_connection.py` & `trademaster406-0.0.4/trademaster406/collector/helper/pika_connection.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/collector/helper/websocket_consumer.py` & `trademaster406-0.0.4/trademaster406/collector/helper/websocket_consumer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/collector/helper/websocket_producer.py` & `trademaster406-0.0.4/trademaster406/collector/helper/websocket_producer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/datasets/algorithmic_trading/dataset.py` & `trademaster406-0.0.4/trademaster406/datasets/algorithmic_trading/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/datasets/high_frequency_trading/dataset.py` & `trademaster406-0.0.4/trademaster406/datasets/high_frequency_trading/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/datasets/order_execution/dataset.py` & `trademaster406-0.0.4/trademaster406/datasets/order_execution/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/datasets/portfolio_management/dataset.py` & `trademaster406-0.0.4/trademaster406/datasets/portfolio_management/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/__init__.py` & `trademaster406-0.0.4/trademaster406/environments/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/algorithmic_trading/environment.py` & `trademaster406-0.0.4/trademaster406/environments/algorithmic_trading/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/high_frequency_trading/environment.py` & `trademaster406-0.0.4/trademaster406/environments/high_frequency_trading/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/order_execution/eteo_environment.py` & `trademaster406-0.0.4/trademaster406/environments/order_execution/eteo_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/order_execution/pd_environment.py` & `trademaster406-0.0.4/trademaster406/environments/order_execution/pd_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/portfolio_management/deeptrader_environment.py` & `trademaster406-0.0.4/trademaster406/environments/portfolio_management/deeptrader_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/portfolio_management/eiie_environment.py` & `trademaster406-0.0.4/trademaster406/environments/portfolio_management/eiie_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/portfolio_management/environment.py` & `trademaster406-0.0.4/trademaster406/environments/portfolio_management/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/portfolio_management/inverstor_imitator_environment.py` & `trademaster406-0.0.4/trademaster406/environments/portfolio_management/inverstor_imitator_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/environments/portfolio_management/sarl_environment.py` & `trademaster406-0.0.4/trademaster406/environments/portfolio_management/sarl_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/model/linear_model.py` & `trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/model/linear_model.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/evaluation/market_dynamics_labeling/model/run_linear_model.py` & `trademaster406-0.0.4/trademaster406/evaluation/market_dynamics_labeling/model/run_linear_model.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/dataset.py` & `trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/imputation.py` & `trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/imputation.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/imputation/missing_value_imputation/utils.py` & `trademaster406-0.0.4/trademaster406/imputation/missing_value_imputation/utils.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/losses/hft_loss.py` & `trademaster406-0.0.4/trademaster406/losses/hft_loss.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/ASU.py` & `trademaster406-0.0.4/trademaster406/nets/ASU.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/MSU.py` & `trademaster406-0.0.4/trademaster406/nets/MSU.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/deeptrader.py` & `trademaster406-0.0.4/trademaster406/nets/deeptrader.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/dqn.py` & `trademaster406-0.0.4/trademaster406/nets/dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/eiie.py` & `trademaster406-0.0.4/trademaster406/nets/eiie.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/eteo.py` & `trademaster406-0.0.4/trademaster406/nets/eteo.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/high_frequency_trading_dqn.py` & `trademaster406-0.0.4/trademaster406/nets/high_frequency_trading_dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/investor_imitator.py` & `trademaster406-0.0.4/trademaster406/nets/investor_imitator.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/pd.py` & `trademaster406-0.0.4/trademaster406/nets/pd.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/nets/sarl.py` & `trademaster406-0.0.4/trademaster406/nets/sarl.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/optimizers/custom.py` & `trademaster406-0.0.4/trademaster406/optimizers/custom.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/preprocessor/yfinance_preprocessor/processor.py` & `trademaster406-0.0.4/trademaster406/preprocessor/yfinance_preprocessor/processor.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/__init__.py` & `trademaster406-0.0.4/trademaster406/trainers/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/algorithmic_trading/trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/algorithmic_trading/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/high_frequency_trading/trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/high_frequency_trading/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/order_execution/eteo_trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/order_execution/eteo_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/order_execution/pd_trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/order_execution/pd_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/portfolio_management/deeptrader_trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/portfolio_management/deeptrader_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/portfolio_management/eiie_trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/portfolio_management/eiie_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/portfolio_management/investor_imitator_trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/portfolio_management/investor_imitator_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/portfolio_management/sarl_trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/portfolio_management/sarl_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/trainers/portfolio_management/trainer.py` & `trademaster406-0.0.4/trademaster406/trainers/portfolio_management/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/transition/custom.py` & `trademaster406-0.0.4/trademaster406/transition/custom.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/utils/__init__.py` & `trademaster406-0.0.4/trademaster406/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/utils/general_replay_buffer.py` & `trademaster406-0.0.4/trademaster406/utils/general_replay_buffer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/utils/labeling_util.py` & `trademaster406-0.0.4/trademaster406/utils/labeling_util.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/utils/layers.py` & `trademaster406-0.0.4/trademaster406/utils/layers.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/utils/misc.py` & `trademaster406-0.0.4/trademaster406/utils/misc.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/utils/replay_buffer.py` & `trademaster406-0.0.4/trademaster406/utils/replay_buffer.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster/utils/utils.py` & `trademaster406-0.0.4/trademaster406/utils/utils.py`

 * *Files identical despite different names*

### Comparing `trademaster406-0.0.3/trademaster406.egg-info/PKG-INFO` & `trademaster406-0.0.4/trademaster406.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster406
-Version: 0.0.3
+Version: 0.0.4
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: TradeMaster.NTU@gmail.com
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `trademaster406-0.0.3/trademaster406.egg-info/SOURCES.txt` & `trademaster406-0.0.4/trademaster406.egg-info/SOURCES.txt`

 * *Files 23% similar despite different names*

```diff
@@ -1,134 +1,134 @@
 LICENSE
 README.md
 pyproject.toml
 setup.py
 configs/__init__.py
 configs/_base_/__init__.py
 tools/__init__.py
-trademaster/__init__.py
-trademaster/agents/__init__.py
-trademaster/agents/builder.py
-trademaster/agents/custom.py
-trademaster/agents/algorithmic_trading/__init__.py
-trademaster/agents/algorithmic_trading/dqn.py
-trademaster/agents/high_frequency_trading/__init__.py
-trademaster/agents/high_frequency_trading/ddqn.py
-trademaster/agents/order_execution/__init__.py
-trademaster/agents/order_execution/eteo.py
-trademaster/agents/order_execution/pd.py
-trademaster/agents/portfolio_management/__init__.py
-trademaster/agents/portfolio_management/deeptrader.py
-trademaster/agents/portfolio_management/eiie.py
-trademaster/agents/portfolio_management/investor_imitator.py
-trademaster/collector/__init__.py
-trademaster/collector/binance.py
-trademaster/collector/builder.py
-trademaster/collector/custom.py
-trademaster/collector/helper/__init__.py
-trademaster/collector/helper/celery_app.py
-trademaster/collector/helper/celery_config.py
-trademaster/collector/helper/pika_connection.py
-trademaster/collector/helper/run_celery.py
-trademaster/collector/helper/websocket_consumer.py
-trademaster/collector/helper/websocket_producer.py
-trademaster/datasets/__init__.py
-trademaster/datasets/builder.py
-trademaster/datasets/custom.py
-trademaster/datasets/algorithmic_trading/__init__.py
-trademaster/datasets/algorithmic_trading/dataset.py
-trademaster/datasets/high_frequency_trading/__init__.py
-trademaster/datasets/high_frequency_trading/dataset.py
-trademaster/datasets/order_execution/__init__.py
-trademaster/datasets/order_execution/dataset.py
-trademaster/datasets/portfolio_management/__init__.py
-trademaster/datasets/portfolio_management/dataset.py
-trademaster/environments/__init__.py
-trademaster/environments/builder.py
-trademaster/environments/custom.py
-trademaster/environments/algorithmic_trading/__init__.py
-trademaster/environments/algorithmic_trading/environment.py
-trademaster/environments/high_frequency_trading/__init__.py
-trademaster/environments/high_frequency_trading/environment.py
-trademaster/environments/order_execution/__init__.py
-trademaster/environments/order_execution/eteo_environment.py
-trademaster/environments/order_execution/pd_environment.py
-trademaster/environments/portfolio_management/__init__.py
-trademaster/environments/portfolio_management/deeptrader_environment.py
-trademaster/environments/portfolio_management/eiie_environment.py
-trademaster/environments/portfolio_management/environment.py
-trademaster/environments/portfolio_management/inverstor_imitator_environment.py
-trademaster/environments/portfolio_management/sarl_environment.py
-trademaster/evaluation/__init__.py
-trademaster/evaluation/market_dynamics_labeling/__init__.py
-trademaster/evaluation/market_dynamics_labeling/builder.py
-trademaster/evaluation/market_dynamics_labeling/custom.py
-trademaster/evaluation/market_dynamics_labeling/model/__init__.py
-trademaster/evaluation/market_dynamics_labeling/model/linear_model.py
-trademaster/evaluation/market_dynamics_labeling/model/run_linear_model.py
-trademaster/imputation/__init__.py
-trademaster/imputation/builder.py
-trademaster/imputation/custom.py
-trademaster/imputation/missing_value_imputation/__init__.py
-trademaster/imputation/missing_value_imputation/dataset.py
-trademaster/imputation/missing_value_imputation/imputation.py
-trademaster/imputation/missing_value_imputation/utils.py
-trademaster/losses/__init__.py
-trademaster/losses/builder.py
-trademaster/losses/custom.py
-trademaster/losses/hft_loss.py
-trademaster/nets/ASU.py
-trademaster/nets/MSU.py
-trademaster/nets/__init__.py
-trademaster/nets/builder.py
-trademaster/nets/custom.py
-trademaster/nets/deeptrader.py
-trademaster/nets/dqn.py
-trademaster/nets/eiie.py
-trademaster/nets/eteo.py
-trademaster/nets/high_frequency_trading_dqn.py
-trademaster/nets/investor_imitator.py
-trademaster/nets/pd.py
-trademaster/nets/sarl.py
-trademaster/optimizers/__init__.py
-trademaster/optimizers/builder.py
-trademaster/optimizers/custom.py
-trademaster/preprocessor/__init__.py
-trademaster/preprocessor/builder.py
-trademaster/preprocessor/custom.py
-trademaster/preprocessor/yfinance_preprocessor/__init__.py
-trademaster/preprocessor/yfinance_preprocessor/processor.py
-trademaster/pretrained/__init__.py
-trademaster/trainers/__init__.py
-trademaster/trainers/builder.py
-trademaster/trainers/custom.py
-trademaster/trainers/algorithmic_trading/__init__.py
-trademaster/trainers/algorithmic_trading/trainer.py
-trademaster/trainers/high_frequency_trading/__init__.py
-trademaster/trainers/high_frequency_trading/trainer.py
-trademaster/trainers/order_execution/__init__.py
-trademaster/trainers/order_execution/eteo_trainer.py
-trademaster/trainers/order_execution/pd_trainer.py
-trademaster/trainers/portfolio_management/__init__.py
-trademaster/trainers/portfolio_management/deeptrader_trainer.py
-trademaster/trainers/portfolio_management/eiie_trainer.py
-trademaster/trainers/portfolio_management/investor_imitator_trainer.py
-trademaster/trainers/portfolio_management/sarl_trainer.py
-trademaster/trainers/portfolio_management/trainer.py
-trademaster/transition/__init__.py
-trademaster/transition/builder.py
-trademaster/transition/custom.py
-trademaster/utils/__init__.py
-trademaster/utils/general_replay_buffer.py
-trademaster/utils/labeling_util.py
-trademaster/utils/layers.py
-trademaster/utils/misc.py
-trademaster/utils/replay_buffer.py
-trademaster/utils/utils.py
+trademaster406/__init__.py
 trademaster406.egg-info/PKG-INFO
 trademaster406.egg-info/SOURCES.txt
 trademaster406.egg-info/dependency_links.txt
 trademaster406.egg-info/not-zip-safe
 trademaster406.egg-info/requires.txt
 trademaster406.egg-info/top_level.txt
+trademaster406/agents/__init__.py
+trademaster406/agents/builder.py
+trademaster406/agents/custom.py
+trademaster406/agents/algorithmic_trading/__init__.py
+trademaster406/agents/algorithmic_trading/dqn.py
+trademaster406/agents/high_frequency_trading/__init__.py
+trademaster406/agents/high_frequency_trading/ddqn.py
+trademaster406/agents/order_execution/__init__.py
+trademaster406/agents/order_execution/eteo.py
+trademaster406/agents/order_execution/pd.py
+trademaster406/agents/portfolio_management/__init__.py
+trademaster406/agents/portfolio_management/deeptrader.py
+trademaster406/agents/portfolio_management/eiie.py
+trademaster406/agents/portfolio_management/investor_imitator.py
+trademaster406/collector/__init__.py
+trademaster406/collector/binance.py
+trademaster406/collector/builder.py
+trademaster406/collector/custom.py
+trademaster406/collector/helper/__init__.py
+trademaster406/collector/helper/celery_app.py
+trademaster406/collector/helper/celery_config.py
+trademaster406/collector/helper/pika_connection.py
+trademaster406/collector/helper/run_celery.py
+trademaster406/collector/helper/websocket_consumer.py
+trademaster406/collector/helper/websocket_producer.py
+trademaster406/datasets/__init__.py
+trademaster406/datasets/builder.py
+trademaster406/datasets/custom.py
+trademaster406/datasets/algorithmic_trading/__init__.py
+trademaster406/datasets/algorithmic_trading/dataset.py
+trademaster406/datasets/high_frequency_trading/__init__.py
+trademaster406/datasets/high_frequency_trading/dataset.py
+trademaster406/datasets/order_execution/__init__.py
+trademaster406/datasets/order_execution/dataset.py
+trademaster406/datasets/portfolio_management/__init__.py
+trademaster406/datasets/portfolio_management/dataset.py
+trademaster406/environments/__init__.py
+trademaster406/environments/builder.py
+trademaster406/environments/custom.py
+trademaster406/environments/algorithmic_trading/__init__.py
+trademaster406/environments/algorithmic_trading/environment.py
+trademaster406/environments/high_frequency_trading/__init__.py
+trademaster406/environments/high_frequency_trading/environment.py
+trademaster406/environments/order_execution/__init__.py
+trademaster406/environments/order_execution/eteo_environment.py
+trademaster406/environments/order_execution/pd_environment.py
+trademaster406/environments/portfolio_management/__init__.py
+trademaster406/environments/portfolio_management/deeptrader_environment.py
+trademaster406/environments/portfolio_management/eiie_environment.py
+trademaster406/environments/portfolio_management/environment.py
+trademaster406/environments/portfolio_management/inverstor_imitator_environment.py
+trademaster406/environments/portfolio_management/sarl_environment.py
+trademaster406/evaluation/__init__.py
+trademaster406/evaluation/market_dynamics_labeling/__init__.py
+trademaster406/evaluation/market_dynamics_labeling/builder.py
+trademaster406/evaluation/market_dynamics_labeling/custom.py
+trademaster406/evaluation/market_dynamics_labeling/model/__init__.py
+trademaster406/evaluation/market_dynamics_labeling/model/linear_model.py
+trademaster406/evaluation/market_dynamics_labeling/model/run_linear_model.py
+trademaster406/imputation/__init__.py
+trademaster406/imputation/builder.py
+trademaster406/imputation/custom.py
+trademaster406/imputation/missing_value_imputation/__init__.py
+trademaster406/imputation/missing_value_imputation/dataset.py
+trademaster406/imputation/missing_value_imputation/imputation.py
+trademaster406/imputation/missing_value_imputation/utils.py
+trademaster406/losses/__init__.py
+trademaster406/losses/builder.py
+trademaster406/losses/custom.py
+trademaster406/losses/hft_loss.py
+trademaster406/nets/ASU.py
+trademaster406/nets/MSU.py
+trademaster406/nets/__init__.py
+trademaster406/nets/builder.py
+trademaster406/nets/custom.py
+trademaster406/nets/deeptrader.py
+trademaster406/nets/dqn.py
+trademaster406/nets/eiie.py
+trademaster406/nets/eteo.py
+trademaster406/nets/high_frequency_trading_dqn.py
+trademaster406/nets/investor_imitator.py
+trademaster406/nets/pd.py
+trademaster406/nets/sarl.py
+trademaster406/optimizers/__init__.py
+trademaster406/optimizers/builder.py
+trademaster406/optimizers/custom.py
+trademaster406/preprocessor/__init__.py
+trademaster406/preprocessor/builder.py
+trademaster406/preprocessor/custom.py
+trademaster406/preprocessor/yfinance_preprocessor/__init__.py
+trademaster406/preprocessor/yfinance_preprocessor/processor.py
+trademaster406/pretrained/__init__.py
+trademaster406/trainers/__init__.py
+trademaster406/trainers/builder.py
+trademaster406/trainers/custom.py
+trademaster406/trainers/algorithmic_trading/__init__.py
+trademaster406/trainers/algorithmic_trading/trainer.py
+trademaster406/trainers/high_frequency_trading/__init__.py
+trademaster406/trainers/high_frequency_trading/trainer.py
+trademaster406/trainers/order_execution/__init__.py
+trademaster406/trainers/order_execution/eteo_trainer.py
+trademaster406/trainers/order_execution/pd_trainer.py
+trademaster406/trainers/portfolio_management/__init__.py
+trademaster406/trainers/portfolio_management/deeptrader_trainer.py
+trademaster406/trainers/portfolio_management/eiie_trainer.py
+trademaster406/trainers/portfolio_management/investor_imitator_trainer.py
+trademaster406/trainers/portfolio_management/sarl_trainer.py
+trademaster406/trainers/portfolio_management/trainer.py
+trademaster406/transition/__init__.py
+trademaster406/transition/builder.py
+trademaster406/transition/custom.py
+trademaster406/utils/__init__.py
+trademaster406/utils/general_replay_buffer.py
+trademaster406/utils/labeling_util.py
+trademaster406/utils/layers.py
+trademaster406/utils/misc.py
+trademaster406/utils/replay_buffer.py
+trademaster406/utils/utils.py
 unit_testing/__init__.py
 unit_testing/test_core.py
```

