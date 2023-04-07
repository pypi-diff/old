# Comparing `tmp/trademaster408-0.0.1.tar.gz` & `tmp/trademaster408-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "trademaster408-0.0.1.tar", last modified: Fri Apr  7 06:53:05 2023, max compression
+gzip compressed data, was "trademaster408-0.0.2.tar", last modified: Fri Apr  7 06:57:43 2023, max compression
```

## Comparing `trademaster408-0.0.1.tar` & `trademaster408-0.0.2.tar`

### file list

```diff
@@ -1,168 +1,168 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.206802 trademaster408-0.0.1/
--rwxr-xr-x   0 root         (0) root         (0)    11558 2023-04-07 06:25:50.000000 trademaster408-0.0.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)    16279 2023-04-07 06:53:05.206802 trademaster408-0.0.1/PKG-INFO
--rwxr-xr-x   0 root         (0) root         (0)    15691 2023-04-07 06:25:50.000000 trademaster408-0.0.1/README.md
--rw-r--r--   0 root         (0) root         (0)      283 2023-04-07 06:53:04.000000 trademaster408-0.0.1/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       74 2023-04-07 06:53:05.207802 trademaster408-0.0.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1176 2023-04-07 06:51:29.000000 trademaster408-0.0.1/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.185800 trademaster408-0.0.1/trademaster408/
--rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.187800 trademaster408-0.0.1/trademaster408/agents/
--rwxr-xr-x   0 root         (0) root         (0)      523 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.187800 trademaster408-0.0.1/trademaster408/agents/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       38 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     8135 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/algorithmic_trading/dqn.py
--rwxr-xr-x   0 root         (0) root         (0)      281 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      125 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.187800 trademaster408-0.0.1/trademaster408/agents/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       42 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9993 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/high_frequency_trading/ddqn.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.188800 trademaster408-0.0.1/trademaster408/agents/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)       70 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     8536 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/order_execution/eteo.py
--rwxr-xr-x   0 root         (0) root         (0)    15383 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/order_execution/pd.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.188800 trademaster408-0.0.1/trademaster408/agents/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      164 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    15287 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/portfolio_management/deeptrader.py
--rwxr-xr-x   0 root         (0) root         (0)     6631 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/portfolio_management/eiie.py
--rwxr-xr-x   0 root         (0) root         (0)     2239 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/agents/portfolio_management/investor_imitator.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.189800 trademaster408-0.0.1/trademaster408/collector/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/__init__.py
--rw-r--r--   0 root         (0) root         (0)      415 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/binance.py
--rwxr-xr-x   0 root         (0) root         (0)      300 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      130 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.190800 trademaster408-0.0.1/trademaster408/collector/helper/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/helper/__init__.py
--rw-r--r--   0 root         (0) root         (0)       95 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/helper/celery_app.py
--rw-r--r--   0 root         (0) root         (0)      344 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/helper/celery_config.py
--rw-r--r--   0 root         (0) root         (0)      968 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/helper/pika_connection.py
--rw-r--r--   0 root         (0) root         (0)      157 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/helper/run_celery.py
--rw-r--r--   0 root         (0) root         (0)      794 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/helper/websocket_consumer.py
--rw-r--r--   0 root         (0) root         (0)     3391 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/collector/helper/websocket_producer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.190800 trademaster408-0.0.1/trademaster408/datasets/
--rwxr-xr-x   0 root         (0) root         (0)      340 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.191800 trademaster408-0.0.1/trademaster408/datasets/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     3502 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/algorithmic_trading/dataset.py
--rwxr-xr-x   0 root         (0) root         (0)      290 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      320 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.191800 trademaster408-0.0.1/trademaster408/datasets/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       48 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3693 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/high_frequency_trading/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.191800 trademaster408-0.0.1/trademaster408/datasets/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)       42 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     3963 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/order_execution/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.192800 trademaster408-0.0.1/trademaster408/datasets/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)       47 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     4053 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/datasets/portfolio_management/dataset.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.192800 trademaster408-0.0.1/trademaster408/environments/
--rwxr-xr-x   0 root         (0) root         (0)      855 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.192800 trademaster408-0.0.1/trademaster408/environments/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       54 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    14512 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/algorithmic_trading/environment.py
--rwxr-xr-x   0 root         (0) root         (0)      321 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      191 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.193800 trademaster408-0.0.1/trademaster408/environments/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)      122 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)    32810 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/high_frequency_trading/environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.193800 trademaster408-0.0.1/trademaster408/environments/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)      116 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    21527 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/order_execution/eteo_environment.py
--rwxr-xr-x   0 root         (0) root         (0)     8469 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/order_execution/pd_environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.194800 trademaster408-0.0.1/trademaster408/environments/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      357 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    10053 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/portfolio_management/deeptrader_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    11513 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/portfolio_management/eiie_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    10348 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/portfolio_management/environment.py
--rwxr-xr-x   0 root         (0) root         (0)    19345 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/portfolio_management/inverstor_imitator_environment.py
--rwxr-xr-x   0 root         (0) root         (0)    14016 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/environments/portfolio_management/sarl_environment.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.194800 trademaster408-0.0.1/trademaster408/evaluation/
--rw-r--r--   0 root         (0) root         (0)       56 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/evaluation/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.195801 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/
--rw-r--r--   0 root         (0) root         (0)      178 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/__init__.py
--rw-r--r--   0 root         (0) root         (0)      380 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/builder.py
--rw-r--r--   0 root         (0) root         (0)      163 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.196801 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/model/
--rw-r--r--   0 root         (0) root         (0)       54 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/model/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4479 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/model/linear_model.py
--rw-r--r--   0 root         (0) root         (0)     4332 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/model/run_linear_model.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.196801 trademaster408-0.0.1/trademaster408/imputation/
--rw-r--r--   0 root         (0) root         (0)      128 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/imputation/__init__.py
--rw-r--r--   0 root         (0) root         (0)      309 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/imputation/builder.py
--rw-r--r--   0 root         (0) root         (0)      282 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/imputation/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.197801 trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/
--rw-r--r--   0 root         (0) root         (0)       39 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7601 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/dataset.py
--rw-r--r--   0 root         (0) root         (0)    11328 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/imputation.py
--rw-r--r--   0 root         (0) root         (0)     6923 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.198801 trademaster408-0.0.1/trademaster408/losses/
--rwxr-xr-x   0 root         (0) root         (0)      118 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/losses/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      274 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/losses/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      381 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/losses/custom.py
--rw-r--r--   0 root         (0) root         (0)      583 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/losses/hft_loss.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.199801 trademaster408-0.0.1/trademaster408/nets/
--rwxr-xr-x   0 root         (0) root         (0)     9591 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/ASU.py
--rwxr-xr-x   0 root         (0) root         (0)     1570 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/MSU.py
--rwxr-xr-x   0 root         (0) root         (0)      366 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      263 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      159 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/custom.py
--rwxr-xr-x   0 root         (0) root         (0)    10598 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/deeptrader.py
--rwxr-xr-x   0 root         (0) root         (0)     1179 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/dqn.py
--rwxr-xr-x   0 root         (0) root         (0)     2423 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/eiie.py
--rwxr-xr-x   0 root         (0) root         (0)     1615 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/eteo.py
--rw-r--r--   0 root         (0) root         (0)     2075 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/high_frequency_trading_dqn.py
--rwxr-xr-x   0 root         (0) root         (0)     1401 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/investor_imitator.py
--rwxr-xr-x   0 root         (0) root         (0)     1393 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/pd.py
--rwxr-xr-x   0 root         (0) root         (0)     1930 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/nets/sarl.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.200801 trademaster408-0.0.1/trademaster408/optimizers/
--rwxr-xr-x   0 root         (0) root         (0)      166 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/optimizers/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      307 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/optimizers/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      708 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/optimizers/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.200801 trademaster408-0.0.1/trademaster408/preprocessor/
--rw-r--r--   0 root         (0) root         (0)      136 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/preprocessor/__init__.py
--rw-r--r--   0 root         (0) root         (0)      308 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/preprocessor/builder.py
--rw-r--r--   0 root         (0) root         (0)      299 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/preprocessor/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.201801 trademaster408-0.0.1/trademaster408/preprocessor/yfinance_preprocessor/
--rw-r--r--   0 root         (0) root         (0)       43 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/preprocessor/yfinance_preprocessor/__init__.py
--rw-r--r--   0 root         (0) root         (0)    34430 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/preprocessor/yfinance_preprocessor/processor.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.201801 trademaster408-0.0.1/trademaster408/pretrained/
--rwxr-xr-x   0 root         (0) root         (0)      335 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/pretrained/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.201801 trademaster408-0.0.1/trademaster408/trainers/
--rwxr-xr-x   0 root         (0) root         (0)      761 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.202801 trademaster408-0.0.1/trademaster408/trainers/algorithmic_trading/
--rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/algorithmic_trading/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    16027 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/algorithmic_trading/trainer.py
--rwxr-xr-x   0 root         (0) root         (0)      271 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/builder.py
--rwxr-xr-x   0 root         (0) root         (0)      154 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.202801 trademaster408-0.0.1/trademaster408/trainers/high_frequency_trading/
--rw-r--r--   0 root         (0) root         (0)       48 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/high_frequency_trading/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9153 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/high_frequency_trading/trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.203801 trademaster408-0.0.1/trademaster408/trainers/order_execution/
--rwxr-xr-x   0 root         (0) root         (0)      100 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/order_execution/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    10583 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/order_execution/eteo_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    12102 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/order_execution/pd_trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.204801 trademaster408-0.0.1/trademaster408/trainers/portfolio_management/
--rwxr-xr-x   0 root         (0) root         (0)      316 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/portfolio_management/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)    13698 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/portfolio_management/deeptrader_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    10768 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/portfolio_management/eiie_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)     7023 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/portfolio_management/investor_imitator_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)    11751 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/portfolio_management/sarl_trainer.py
--rwxr-xr-x   0 root         (0) root         (0)     6616 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/trainers/portfolio_management/trainer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.204801 trademaster408-0.0.1/trademaster408/transition/
--rwxr-xr-x   0 root         (0) root         (0)      106 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/transition/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)      314 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/transition/builder.py
--rwxr-xr-x   0 root         (0) root         (0)     1520 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/transition/custom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.206802 trademaster408-0.0.1/trademaster408/utils/
--rwxr-xr-x   0 root         (0) root         (0)      879 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/utils/__init__.py
--rwxr-xr-x   0 root         (0) root         (0)     4048 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/utils/general_replay_buffer.py
--rw-r--r--   0 root         (0) root         (0)    18681 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/utils/labeling_util.py
--rwxr-xr-x   0 root         (0) root         (0)     1057 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/utils/layers.py
--rwxr-xr-x   0 root         (0) root         (0)    17416 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/utils/misc.py
--rw-r--r--   0 root         (0) root         (0)    13758 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/utils/replay_buffer.py
--rwxr-xr-x   0 root         (0) root         (0)    19116 2023-04-07 06:25:54.000000 trademaster408-0.0.1/trademaster408/utils/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:53:05.186800 trademaster408-0.0.1/trademaster408.egg-info/
--rw-r--r--   0 root         (0) root         (0)    16279 2023-04-07 06:53:05.000000 trademaster408-0.0.1/trademaster408.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     5919 2023-04-07 06:53:05.000000 trademaster408-0.0.1/trademaster408.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 06:53:05.000000 trademaster408-0.0.1/trademaster408.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      264 2023-04-07 06:53:05.000000 trademaster408-0.0.1/trademaster408.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       15 2023-04-07 06:53:05.000000 trademaster408-0.0.1/trademaster408.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.238321 trademaster408-0.0.2/
+-rwxr-xr-x   0 root         (0) root         (0)    11558 2023-04-07 06:25:50.000000 trademaster408-0.0.2/LICENSE
+-rw-r--r--   0 root         (0) root         (0)    16279 2023-04-07 06:57:43.238321 trademaster408-0.0.2/PKG-INFO
+-rwxr-xr-x   0 root         (0) root         (0)    15691 2023-04-07 06:25:50.000000 trademaster408-0.0.2/README.md
+-rw-r--r--   0 root         (0) root         (0)      283 2023-04-07 06:56:40.000000 trademaster408-0.0.2/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       74 2023-04-07 06:57:43.238321 trademaster408-0.0.2/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1176 2023-04-07 06:57:17.000000 trademaster408-0.0.2/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.217319 trademaster408-0.0.2/trademaster408/
+-rwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.218320 trademaster408-0.0.2/trademaster408/agents/
+-rwxr-xr-x   0 root         (0) root         (0)      523 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.219319 trademaster408-0.0.2/trademaster408/agents/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       38 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     8135 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/algorithmic_trading/dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)      281 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      125 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.219319 trademaster408-0.0.2/trademaster408/agents/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       42 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9993 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/high_frequency_trading/ddqn.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.219319 trademaster408-0.0.2/trademaster408/agents/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)       70 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     8536 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/order_execution/eteo.py
+-rwxr-xr-x   0 root         (0) root         (0)    15383 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/order_execution/pd.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.220320 trademaster408-0.0.2/trademaster408/agents/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      164 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    15287 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/portfolio_management/deeptrader.py
+-rwxr-xr-x   0 root         (0) root         (0)     6631 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/portfolio_management/eiie.py
+-rwxr-xr-x   0 root         (0) root         (0)     2239 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/agents/portfolio_management/investor_imitator.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.221320 trademaster408-0.0.2/trademaster408/collector/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      415 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/binance.py
+-rwxr-xr-x   0 root         (0) root         (0)      300 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      130 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.222320 trademaster408-0.0.2/trademaster408/collector/helper/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/helper/__init__.py
+-rw-r--r--   0 root         (0) root         (0)       95 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/helper/celery_app.py
+-rw-r--r--   0 root         (0) root         (0)      344 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/helper/celery_config.py
+-rw-r--r--   0 root         (0) root         (0)      968 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/helper/pika_connection.py
+-rw-r--r--   0 root         (0) root         (0)      157 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/helper/run_celery.py
+-rw-r--r--   0 root         (0) root         (0)      794 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/helper/websocket_consumer.py
+-rw-r--r--   0 root         (0) root         (0)     3391 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/collector/helper/websocket_producer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.222320 trademaster408-0.0.2/trademaster408/datasets/
+-rwxr-xr-x   0 root         (0) root         (0)      340 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.223320 trademaster408-0.0.2/trademaster408/datasets/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     3502 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/algorithmic_trading/dataset.py
+-rwxr-xr-x   0 root         (0) root         (0)      290 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      320 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.223320 trademaster408-0.0.2/trademaster408/datasets/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       48 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3693 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/high_frequency_trading/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.223320 trademaster408-0.0.2/trademaster408/datasets/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)       42 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     3963 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/order_execution/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.224320 trademaster408-0.0.2/trademaster408/datasets/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)       47 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     4053 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/datasets/portfolio_management/dataset.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.224320 trademaster408-0.0.2/trademaster408/environments/
+-rwxr-xr-x   0 root         (0) root         (0)      855 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.224320 trademaster408-0.0.2/trademaster408/environments/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       54 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    14512 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/algorithmic_trading/environment.py
+-rwxr-xr-x   0 root         (0) root         (0)      321 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      191 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.225320 trademaster408-0.0.2/trademaster408/environments/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)      122 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    32810 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/high_frequency_trading/environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.225320 trademaster408-0.0.2/trademaster408/environments/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)      116 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    21527 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/order_execution/eteo_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)     8469 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/order_execution/pd_environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.226320 trademaster408-0.0.2/trademaster408/environments/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      357 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    10053 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/portfolio_management/deeptrader_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    11513 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/portfolio_management/eiie_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    10348 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/portfolio_management/environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    19345 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/portfolio_management/inverstor_imitator_environment.py
+-rwxr-xr-x   0 root         (0) root         (0)    14016 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/environments/portfolio_management/sarl_environment.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.226320 trademaster408-0.0.2/trademaster408/evaluation/
+-rw-r--r--   0 root         (0) root         (0)       56 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/evaluation/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.227320 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/
+-rw-r--r--   0 root         (0) root         (0)      178 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      380 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/builder.py
+-rw-r--r--   0 root         (0) root         (0)      163 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.227320 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/model/
+-rw-r--r--   0 root         (0) root         (0)       54 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/model/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4479 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/model/linear_model.py
+-rw-r--r--   0 root         (0) root         (0)     4332 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/model/run_linear_model.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.228320 trademaster408-0.0.2/trademaster408/imputation/
+-rw-r--r--   0 root         (0) root         (0)      128 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/imputation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      309 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/imputation/builder.py
+-rw-r--r--   0 root         (0) root         (0)      282 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/imputation/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.229320 trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/
+-rw-r--r--   0 root         (0) root         (0)       39 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7601 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/dataset.py
+-rw-r--r--   0 root         (0) root         (0)    11328 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/imputation.py
+-rw-r--r--   0 root         (0) root         (0)     6923 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.229320 trademaster408-0.0.2/trademaster408/losses/
+-rwxr-xr-x   0 root         (0) root         (0)      118 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/losses/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      274 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/losses/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      381 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/losses/custom.py
+-rw-r--r--   0 root         (0) root         (0)      583 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/losses/hft_loss.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.232321 trademaster408-0.0.2/trademaster408/nets/
+-rwxr-xr-x   0 root         (0) root         (0)     9591 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/ASU.py
+-rwxr-xr-x   0 root         (0) root         (0)     1570 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/MSU.py
+-rwxr-xr-x   0 root         (0) root         (0)      366 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      263 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      159 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/custom.py
+-rwxr-xr-x   0 root         (0) root         (0)    10598 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/deeptrader.py
+-rwxr-xr-x   0 root         (0) root         (0)     1179 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)     2423 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/eiie.py
+-rwxr-xr-x   0 root         (0) root         (0)     1615 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/eteo.py
+-rw-r--r--   0 root         (0) root         (0)     2075 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/high_frequency_trading_dqn.py
+-rwxr-xr-x   0 root         (0) root         (0)     1401 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/investor_imitator.py
+-rwxr-xr-x   0 root         (0) root         (0)     1393 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/pd.py
+-rwxr-xr-x   0 root         (0) root         (0)     1930 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/nets/sarl.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.232321 trademaster408-0.0.2/trademaster408/optimizers/
+-rwxr-xr-x   0 root         (0) root         (0)      166 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/optimizers/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      307 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/optimizers/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      708 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/optimizers/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.233321 trademaster408-0.0.2/trademaster408/preprocessor/
+-rw-r--r--   0 root         (0) root         (0)      136 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/preprocessor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      308 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/preprocessor/builder.py
+-rw-r--r--   0 root         (0) root         (0)      299 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/preprocessor/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.233321 trademaster408-0.0.2/trademaster408/preprocessor/yfinance_preprocessor/
+-rw-r--r--   0 root         (0) root         (0)       43 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/preprocessor/yfinance_preprocessor/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    34430 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/preprocessor/yfinance_preprocessor/processor.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.233321 trademaster408-0.0.2/trademaster408/pretrained/
+-rwxr-xr-x   0 root         (0) root         (0)      335 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/pretrained/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.234321 trademaster408-0.0.2/trademaster408/trainers/
+-rwxr-xr-x   0 root         (0) root         (0)      761 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.234321 trademaster408-0.0.2/trademaster408/trainers/algorithmic_trading/
+-rwxr-xr-x   0 root         (0) root         (0)       46 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/algorithmic_trading/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    16027 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/algorithmic_trading/trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)      271 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)      154 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.234321 trademaster408-0.0.2/trademaster408/trainers/high_frequency_trading/
+-rw-r--r--   0 root         (0) root         (0)       48 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/high_frequency_trading/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9153 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/high_frequency_trading/trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.235321 trademaster408-0.0.2/trademaster408/trainers/order_execution/
+-rwxr-xr-x   0 root         (0) root         (0)      100 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/order_execution/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    10583 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/order_execution/eteo_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    12102 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/order_execution/pd_trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.236321 trademaster408-0.0.2/trademaster408/trainers/portfolio_management/
+-rwxr-xr-x   0 root         (0) root         (0)      316 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/portfolio_management/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)    13698 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/portfolio_management/deeptrader_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    10768 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/portfolio_management/eiie_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)     7023 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/portfolio_management/investor_imitator_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)    11751 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/portfolio_management/sarl_trainer.py
+-rwxr-xr-x   0 root         (0) root         (0)     6616 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/trainers/portfolio_management/trainer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.236321 trademaster408-0.0.2/trademaster408/transition/
+-rwxr-xr-x   0 root         (0) root         (0)      106 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/transition/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)      314 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/transition/builder.py
+-rwxr-xr-x   0 root         (0) root         (0)     1520 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/transition/custom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.237321 trademaster408-0.0.2/trademaster408/utils/
+-rwxr-xr-x   0 root         (0) root         (0)      879 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/utils/__init__.py
+-rwxr-xr-x   0 root         (0) root         (0)     4048 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/utils/general_replay_buffer.py
+-rw-r--r--   0 root         (0) root         (0)    18681 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/utils/labeling_util.py
+-rwxr-xr-x   0 root         (0) root         (0)     1057 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/utils/layers.py
+-rwxr-xr-x   0 root         (0) root         (0)    17416 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/utils/misc.py
+-rw-r--r--   0 root         (0) root         (0)    13758 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/utils/replay_buffer.py
+-rwxr-xr-x   0 root         (0) root         (0)    19116 2023-04-07 06:25:54.000000 trademaster408-0.0.2/trademaster408/utils/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 06:57:43.218320 trademaster408-0.0.2/trademaster408.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    16279 2023-04-07 06:57:43.000000 trademaster408-0.0.2/trademaster408.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     5919 2023-04-07 06:57:43.000000 trademaster408-0.0.2/trademaster408.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 06:57:43.000000 trademaster408-0.0.2/trademaster408.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      233 2023-04-07 06:57:43.000000 trademaster408-0.0.2/trademaster408.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       15 2023-04-07 06:57:43.000000 trademaster408-0.0.2/trademaster408.egg-info/top_level.txt
```

### Comparing `trademaster408-0.0.1/LICENSE` & `trademaster408-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/PKG-INFO` & `trademaster408-0.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster408
-Version: 0.0.1
+Version: 0.0.2
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: NTU_trademaster <TradeMaster.NTU@gmail.com>
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `trademaster408-0.0.1/README.md` & `trademaster408-0.0.2/README.md`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/setup.py` & `trademaster408-0.0.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     long_description = fh.read()
 
 with open("requirements.txt", "r", encoding="utf-8") as fr:
     requirements = fr.readlines()
 
 setup(
     name="trademaster408",
-    version="0.0.1",
+    version="0.0.2",
     description="TradeMaster - A platform for algorithmic trading",
     long_description=long_description,
     long_description_content_type="text/markdown",
     author="NTU_trademaster",
     author_email="TradeMaster.NTU@gmail.com",
     url="https://github.com/TradeMaster-NTU/TradeMaster",
     packages=find_packages(include=["trademaster*"]),
```

### Comparing `trademaster408-0.0.1/trademaster408/agents/__init__.py` & `trademaster408-0.0.2/trademaster408/agents/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/agents/algorithmic_trading/dqn.py` & `trademaster408-0.0.2/trademaster408/agents/algorithmic_trading/dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/agents/high_frequency_trading/ddqn.py` & `trademaster408-0.0.2/trademaster408/agents/high_frequency_trading/ddqn.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/agents/order_execution/eteo.py` & `trademaster408-0.0.2/trademaster408/agents/order_execution/eteo.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/agents/order_execution/pd.py` & `trademaster408-0.0.2/trademaster408/agents/order_execution/pd.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/agents/portfolio_management/deeptrader.py` & `trademaster408-0.0.2/trademaster408/agents/portfolio_management/deeptrader.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/agents/portfolio_management/eiie.py` & `trademaster408-0.0.2/trademaster408/agents/portfolio_management/eiie.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/agents/portfolio_management/investor_imitator.py` & `trademaster408-0.0.2/trademaster408/agents/portfolio_management/investor_imitator.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/collector/helper/pika_connection.py` & `trademaster408-0.0.2/trademaster408/collector/helper/pika_connection.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/collector/helper/websocket_consumer.py` & `trademaster408-0.0.2/trademaster408/collector/helper/websocket_consumer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/collector/helper/websocket_producer.py` & `trademaster408-0.0.2/trademaster408/collector/helper/websocket_producer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/datasets/algorithmic_trading/dataset.py` & `trademaster408-0.0.2/trademaster408/datasets/algorithmic_trading/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/datasets/high_frequency_trading/dataset.py` & `trademaster408-0.0.2/trademaster408/datasets/high_frequency_trading/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/datasets/order_execution/dataset.py` & `trademaster408-0.0.2/trademaster408/datasets/order_execution/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/datasets/portfolio_management/dataset.py` & `trademaster408-0.0.2/trademaster408/datasets/portfolio_management/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/__init__.py` & `trademaster408-0.0.2/trademaster408/environments/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/algorithmic_trading/environment.py` & `trademaster408-0.0.2/trademaster408/environments/algorithmic_trading/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/high_frequency_trading/environment.py` & `trademaster408-0.0.2/trademaster408/environments/high_frequency_trading/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/order_execution/eteo_environment.py` & `trademaster408-0.0.2/trademaster408/environments/order_execution/eteo_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/order_execution/pd_environment.py` & `trademaster408-0.0.2/trademaster408/environments/order_execution/pd_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/portfolio_management/deeptrader_environment.py` & `trademaster408-0.0.2/trademaster408/environments/portfolio_management/deeptrader_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/portfolio_management/eiie_environment.py` & `trademaster408-0.0.2/trademaster408/environments/portfolio_management/eiie_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/portfolio_management/environment.py` & `trademaster408-0.0.2/trademaster408/environments/portfolio_management/environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/portfolio_management/inverstor_imitator_environment.py` & `trademaster408-0.0.2/trademaster408/environments/portfolio_management/inverstor_imitator_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/environments/portfolio_management/sarl_environment.py` & `trademaster408-0.0.2/trademaster408/environments/portfolio_management/sarl_environment.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/model/linear_model.py` & `trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/model/linear_model.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/evaluation/market_dynamics_labeling/model/run_linear_model.py` & `trademaster408-0.0.2/trademaster408/evaluation/market_dynamics_labeling/model/run_linear_model.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/dataset.py` & `trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/dataset.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/imputation.py` & `trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/imputation.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/imputation/missing_value_imputation/utils.py` & `trademaster408-0.0.2/trademaster408/imputation/missing_value_imputation/utils.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/losses/hft_loss.py` & `trademaster408-0.0.2/trademaster408/losses/hft_loss.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/ASU.py` & `trademaster408-0.0.2/trademaster408/nets/ASU.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/MSU.py` & `trademaster408-0.0.2/trademaster408/nets/MSU.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/deeptrader.py` & `trademaster408-0.0.2/trademaster408/nets/deeptrader.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/dqn.py` & `trademaster408-0.0.2/trademaster408/nets/dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/eiie.py` & `trademaster408-0.0.2/trademaster408/nets/eiie.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/eteo.py` & `trademaster408-0.0.2/trademaster408/nets/eteo.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/high_frequency_trading_dqn.py` & `trademaster408-0.0.2/trademaster408/nets/high_frequency_trading_dqn.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/investor_imitator.py` & `trademaster408-0.0.2/trademaster408/nets/investor_imitator.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/pd.py` & `trademaster408-0.0.2/trademaster408/nets/pd.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/nets/sarl.py` & `trademaster408-0.0.2/trademaster408/nets/sarl.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/optimizers/custom.py` & `trademaster408-0.0.2/trademaster408/optimizers/custom.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/preprocessor/yfinance_preprocessor/processor.py` & `trademaster408-0.0.2/trademaster408/preprocessor/yfinance_preprocessor/processor.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/__init__.py` & `trademaster408-0.0.2/trademaster408/trainers/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/algorithmic_trading/trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/algorithmic_trading/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/high_frequency_trading/trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/high_frequency_trading/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/order_execution/eteo_trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/order_execution/eteo_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/order_execution/pd_trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/order_execution/pd_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/portfolio_management/deeptrader_trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/portfolio_management/deeptrader_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/portfolio_management/eiie_trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/portfolio_management/eiie_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/portfolio_management/investor_imitator_trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/portfolio_management/investor_imitator_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/portfolio_management/sarl_trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/portfolio_management/sarl_trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/trainers/portfolio_management/trainer.py` & `trademaster408-0.0.2/trademaster408/trainers/portfolio_management/trainer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/transition/custom.py` & `trademaster408-0.0.2/trademaster408/transition/custom.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/utils/__init__.py` & `trademaster408-0.0.2/trademaster408/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/utils/general_replay_buffer.py` & `trademaster408-0.0.2/trademaster408/utils/general_replay_buffer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/utils/labeling_util.py` & `trademaster408-0.0.2/trademaster408/utils/labeling_util.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/utils/layers.py` & `trademaster408-0.0.2/trademaster408/utils/layers.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/utils/misc.py` & `trademaster408-0.0.2/trademaster408/utils/misc.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/utils/replay_buffer.py` & `trademaster408-0.0.2/trademaster408/utils/replay_buffer.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408/utils/utils.py` & `trademaster408-0.0.2/trademaster408/utils/utils.py`

 * *Files identical despite different names*

### Comparing `trademaster408-0.0.1/trademaster408.egg-info/PKG-INFO` & `trademaster408-0.0.2/trademaster408.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster408
-Version: 0.0.1
+Version: 0.0.2
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: NTU_trademaster <TradeMaster.NTU@gmail.com>
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `trademaster408-0.0.1/trademaster408.egg-info/SOURCES.txt` & `trademaster408-0.0.2/trademaster408.egg-info/SOURCES.txt`

 * *Files identical despite different names*

