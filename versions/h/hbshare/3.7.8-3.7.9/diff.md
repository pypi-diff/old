# Comparing `tmp/hbshare-3.7.8.tar.gz` & `tmp/hbshare-3.7.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hbshare-3.7.8.tar", last modified: Fri Mar  3 07:50:04 2023, max compression
+gzip compressed data, was "hbshare-3.7.9.tar", last modified: Fri Mar  3 09:15:16 2023, max compression
```

## Comparing `hbshare-3.7.8.tar` & `hbshare-3.7.9.tar`

### file list

```diff
@@ -1,368 +1,368 @@
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.448318 hbshare-3.7.8/
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1472 2023-02-14 03:34:22.000000 hbshare-3.7.8/LICENSE
--rw-r--r--   0 tomcat     (501) tomcat     (501)       57 2023-02-14 03:34:22.000000 hbshare-3.7.8/MANIFEST.in
--rw-r--r--   0 tomcat     (501) tomcat     (501)      906 2023-03-03 07:50:04.447318 hbshare-3.7.8/PKG-INFO
--rw-r--r--   0 tomcat     (501) tomcat     (501)       35 2023-02-14 03:34:22.000000 hbshare-3.7.8/README.md
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.288318 hbshare-3.7.8/hbshare/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        5 2023-03-03 07:49:48.000000 hbshare-3.7.8/hbshare/VERSION.txt
--rw-r--r--   0 tomcat     (501) tomcat     (501)      983 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.295318 hbshare-3.7.8/hbshare/base/
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3240 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/BaseIndex.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      330 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/QueryException.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1519 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/data_api.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      596 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/data_pro.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2803 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/dateu.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6604 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/formula.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1133 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/upass.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      397 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/base/vars.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.296318 hbshare-3.7.8/hbshare/db/
--rw-r--r--   0 tomcat     (501) tomcat     (501)    25575 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/db/ApiCfg.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2846 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/db/ApiUtils.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.298318 hbshare-3.7.8/hbshare/db/fund/
--rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/fund/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2655 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/fund/cons.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3689 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/fund/nav.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1758 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/fund/product.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.299318 hbshare-3.7.8/hbshare/db/loader/
--rw-r--r--   0 tomcat     (501) tomcat     (501)      212 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/loader/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1707 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/loader/data_query.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3151 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/loader/data_save.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.302318 hbshare-3.7.8/hbshare/db/simu/
--rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/simu/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5383 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/simu/cons.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2443 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/simu/corp.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5579 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/simu/fund_rolling_calculator.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2000 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/simu/nav.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1580 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/simu/simu_index.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4013 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/db/simu/valuation.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.302318 hbshare-3.7.8/hbshare/fe/
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.303318 hbshare-3.7.8/hbshare/fe/AAM/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/AAM/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.304318 hbshare-3.7.8/hbshare/fe/AAM/blmodel/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/AAM/blmodel/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18855 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/AAM/blmodel/blmodel.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2166 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/AAM/blmodel/zep_test.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.305318 hbshare-3.7.8/hbshare/fe/FOF/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/FOF/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   137134 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/FOF/fof_analysis.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.306318 hbshare-3.7.8/hbshare/fe/Fund_classifier/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/Fund_classifier/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   116813 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/Fund_classifier/classification.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.307318 hbshare-3.7.8/hbshare/fe/Machine_learning/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/Machine_learning/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4312 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/Machine_learning/classifier.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.309318 hbshare-3.7.8/hbshare/fe/XZ/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/XZ/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.310318 hbshare-3.7.8/hbshare/fe/XZ/config/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/XZ/config/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5235 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/XZ/config/config_pfa.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    15088 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/XZ/db_engine.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    38505 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/XZ/functionality.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    41682 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/XZ/project.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.316318 hbshare-3.7.8/hbshare/fe/asset_allocation/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    35493 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/black_litterman.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1652 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/black_litterman_solver.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3999 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/data_loader.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4831 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/data_loader_db.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    22974 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/efficient_frontier.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6344 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/efficient_frontier_solver.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2751 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/efficient_frontier_solver_ori.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    44363 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/mean_variance.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     8276 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/mean_variance_solver.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    27130 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/risk_parity_budget.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4078 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/risk_parity_budget_solver.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    11645 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/asset_allocation/simple.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.317318 hbshare-3.7.8/hbshare/fe/brinson_attr/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/brinson_attr/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5799 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/brinson_attr/brinson_attribution_check.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    19214 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/brinson_attr/equity_brinson_attribution.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.318318 hbshare-3.7.8/hbshare/fe/common/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.323318 hbshare-3.7.8/hbshare/fe/common/util/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5310 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/config.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    56342 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/data_loader.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      643 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/exception.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10012 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/helper_func.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1180 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/logger.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5574 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/nav_util.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      860 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/omega_math.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    14308 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/plot_util.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4680 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/regressions.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5545 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/common/util/verifier.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.325318 hbshare-3.7.8/hbshare/fe/factor_analysis/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/factor_analysis/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5936 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/factor_analysis/multi_factors_model.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9204 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/factor_analysis/pool_mantainance.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    30762 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/factor_analysis/simple_factor_generator.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    24013 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/factor_analysis/single_factor_analysis.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.325318 hbshare-3.7.8/hbshare/fe/fund_manager/
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.327318 hbshare-3.7.8/hbshare/fe/fund_manager/Example/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/Example/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1695 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/Example/analysis_example.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1092 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/Example/database_operate_example.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.327318 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.328318 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/Analysis/
--rw-r--r--   0 tomcat     (501) tomcat     (501)       52 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/Analysis/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      190 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/Analysis/functions.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    16544 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/Analysis/manager_life_net_worth.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)       24 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.330318 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/
--rw-r--r--   0 tomcat     (501) tomcat     (501)       32 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      678 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/database_connection.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1515 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/database_dictionary.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     8636 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/database_operate.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_manager/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.333318 hbshare-3.7.8/hbshare/fe/fund_style/
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10562 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_style/MorningStarStyleBox.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_style/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2752 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/fund_style/morning_star_box_check.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.335318 hbshare-3.7.8/hbshare/fe/industry/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/industry/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    50231 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/industry/industry_analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   165421 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/industry/industry_analysis_data.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    17746 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/industry/industry_crowding.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   144633 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/industry/industry_tracking.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.347318 hbshare-3.7.8/hbshare/fe/mutual_analysis/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    66381 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/filter_engine.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   216898 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/fund_report.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   203254 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/fund_report_external.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   261798 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/holdind_based.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   117726 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/holding_analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    25589 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/holding_analysis_plot.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    88464 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/holding_compare_analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   190481 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/jj_picturing.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      139 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/main.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   140407 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/manager_report_external.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18943 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/mutual_fund_selection.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   198544 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/nav_based.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   122750 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/pool_analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    14153 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/mutual_analysis/theme_cluster.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.349318 hbshare-3.7.8/hbshare/fe/nav_attr/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/nav_attr/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    38357 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/nav_attr/bond_campisi_attribution.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3892 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/nav_attr/nav_attr_check.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18949 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/nav_attr/nav_attribution.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.349318 hbshare-3.7.8/hbshare/fe/sector_cluster/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/sector_cluster/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2437 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/sector_cluster/sector_factor_calculator.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.352318 hbshare-3.7.8/hbshare/fe/timing/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/timing/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   161697 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/timing/taa.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    48330 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/timing/timing_analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    90474 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/timing/timing_data.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.352318 hbshare-3.7.8/hbshare/fe/xwq/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.353318 hbshare-3.7.8/hbshare/fe/xwq/analysis/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.354318 hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6012 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/downward_volatility.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4787 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/lasso.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5310 2023-03-03 07:49:46.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/turnover.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.357318 hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1224 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/config.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    20217 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/fedb.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    41903 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/hbdb.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3255 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/http_request.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2881 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/plot.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.369318 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    34833 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/fund_holding_analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   100808 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/holder_structure.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   113144 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/holding_analysis_ori.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    27644 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/holding_analysis_plot_ori.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    20556 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/index_construction.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    17616 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/index_construction_885001.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3700 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/index_corr.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     8035 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_analysis_old.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    14307 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_tracking.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    13545 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_tracking_old.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    52970 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_tracking_report.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    25254 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/jc_comparasion.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4675 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/jgcg.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18022 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/new_high.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5649 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/pdf.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    35928 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/performance_comparison.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   199229 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/quantitative_report_external_ori.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1321 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/shift_cen_ratio_rank.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9195 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/style_index.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    13074 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/valuation.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    22440 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/valuation_earning_contribution.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2834 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/service/wenbo_holding_indu.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.376318 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2579 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/const_var.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     7699 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/data_processor.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2160 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/file_reader.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2177 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/file_writer.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1348 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/http_request.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      406 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/logger_utils.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1599 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/post.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4058 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/preprocess.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2837 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/send_email.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      340 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/singleton.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9361 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/timedelta_utils.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.377318 hbshare-3.7.8/hbshare/fe/xwq/test/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/fe/xwq/test/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.377318 hbshare-3.7.8/hbshare/quant/
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.384318 hbshare-3.7.8/hbshare/quant/CChen/
--rw-r--r--   0 tomcat     (501) tomcat     (501)      322 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6885 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cons.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.388318 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/
--rw-r--r--   0 tomcat     (501) tomcat     (501)      177 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5092 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     8754 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/const.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    57700 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/factor_algo.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    19031 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/factor_func.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10479 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/factor_index.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    16723 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/hsjy_func.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18530 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/hsjy_to_local.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2055 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/run.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6604 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/cta_factor/zep.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.391318 hbshare-3.7.8/hbshare/quant/CChen/data/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/data/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    22201 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/data/data.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1271 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/data/hsjy_data.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1795 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/data/run_wind.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2027 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/data/wind_cons.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    16186 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/data/wind_data.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2656 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/db_const.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.392318 hbshare-3.7.8/hbshare/quant/CChen/fof/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fof/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    12572 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fof/bt_engine.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4128 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/func.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.394318 hbshare-3.7.8/hbshare/quant/CChen/fund_stats/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fund_stats/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6926 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fund_stats/db.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18689 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fund_stats/perf.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    36104 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fund_stats/to_xl.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3274 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fund_stats/xl_cons.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    13605 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/fut.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.395318 hbshare-3.7.8/hbshare/quant/CChen/gzb/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/gzb/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10289 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/gzb/read_gzb.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9290 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/opt.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    61992 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/output.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1808 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/run_market.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1383 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/sql_cons.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10789 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/CChen/stk.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.396318 hbshare-3.7.8/hbshare/quant/Kevin/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.399318 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/
--rw-r--r--   0 tomcat     (501) tomcat     (501)     7571 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/EconomicCycle.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1138 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/denoising.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    24038 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.412318 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2521 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/bond_trading.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3805 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/credit.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     7293 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/currency.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6103 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/eco_increase.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5217 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/future_data.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5630 2023-02-16 05:03:54.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/index_update.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3328 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/inflation.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   206199 2023-02-16 05:03:54.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/main.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3018 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/processed_market_index.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6214 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/rates_and_price.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4342 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cash_flow.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4746 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_concept.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6500 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cross_section_vol.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9550 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_market.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3367 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_share_price_index_futures.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4646 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_momentum.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4422 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_spread.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3606 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_time_series_vol.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6065 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4877 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading_cr.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3238 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/treasury_yield.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1272 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/util.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1704 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/marco_write_to_db.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10005 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/portfolio_index_calculator.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.416318 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/
--rw-r--r--   0 tomcat     (501) tomcat     (501)    11797 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/CBMarketIV.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9874 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_iv_by_bs.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3273 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_pricing_BS.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5546 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_pricing_MC.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3358 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_pricing_Tree.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2058 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/group_test.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     8148 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/valuation_test.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.439318 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/
--rw-r--r--   0 tomcat     (501) tomcat     (501)    13770 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/AlphaMonitor.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10515 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/AlphaPerformance.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6219 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/AlphaResearch.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1972 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Arbitrage_Strategy.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3381 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Arbitrage_backtest.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10600 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Arbitrage_with_Neutral.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    11453 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/CapIndex.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5300 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/CapRotation.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9003 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/CtaNavAttribution.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    12772 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/FundNavAnalysor.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1764 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/HedgeCalcultor.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    11089 2023-02-16 05:03:54.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/HoldingToDB.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18179 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/IndexActiveStyleAnalyse.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4377 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/IndexPEvsfuture_ret.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9824 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/IndexReturnAttr.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    16698 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/LocalNavComparer.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    27131 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MarketStructure.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    59707 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MarketStructure_Weekly.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4260 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MarketStructure_sample.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6662 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Multi-Strategy-Compare.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3952 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Multi-Strategy.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.443318 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1888 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/data_config.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4373 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/data_loader.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)      650 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/util_func.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     7240 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Neutral_Tracker.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10021 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/PrivateFundNavAttr.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    32585 2023-02-16 05:03:54.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/PrivateHoldingAnalysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9790 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/QuarterAssetAllocationReport.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    20926 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/RiskControlReport.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     8125 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/S&P_Access_China_Analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     6639 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/SAR_Indicator.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)   110836 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Subjective_Strategy_Analysis.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4813 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/ThemeSector.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    19389 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_backtest.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5396 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_elasticity.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     9490 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_sourcing.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     7924 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_tracker.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1534 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/benchmark_nav_attr.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    18564 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/daily_nav_attr.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4940 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/data_prepare.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    20396 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/factor_crowd.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     7762 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/factor_crowd_plot.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     5979 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/portfolio_test.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4558 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/snow_ball.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     3025 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/stock_liq.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2243 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/strategy_index.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    20732 2023-02-16 05:03:54.000000 hbshare-3.7.8/hbshare/quant/Kevin/quant_room/tracker.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.445318 hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1679 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/config.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    21667 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/equity_brinson_attribution_datayes.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)    10215 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/factor_return.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     4517 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/risk_model_check.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.8/hbshare/quant/__init__.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.291318 hbshare-3.7.8/hbshare.egg-info/
--rw-r--r--   0 tomcat     (501) tomcat     (501)      906 2023-03-03 07:50:04.000000 hbshare-3.7.8/hbshare.egg-info/PKG-INFO
--rw-r--r--   0 tomcat     (501) tomcat     (501)    13792 2023-03-03 07:50:04.000000 hbshare-3.7.8/hbshare.egg-info/SOURCES.txt
--rw-r--r--   0 tomcat     (501) tomcat     (501)        1 2023-03-03 07:50:04.000000 hbshare-3.7.8/hbshare.egg-info/dependency_links.txt
--rw-r--r--   0 tomcat     (501) tomcat     (501)       50 2023-03-03 07:50:04.000000 hbshare-3.7.8/hbshare.egg-info/requires.txt
--rw-r--r--   0 tomcat     (501) tomcat     (501)       13 2023-03-03 07:50:04.000000 hbshare-3.7.8/hbshare.egg-info/top_level.txt
--rw-r--r--   0 tomcat     (501) tomcat     (501)       38 2023-03-03 07:50:04.448318 hbshare-3.7.8/setup.cfg
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2986 2023-02-14 03:34:22.000000 hbshare-3.7.8/setup.py
-drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 07:50:04.447318 hbshare-3.7.8/test/
--rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.8/test/__init__.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2485 2023-02-14 03:34:22.000000 hbshare-3.7.8/test/db_data_save_test.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     2112 2023-02-14 03:34:22.000000 hbshare-3.7.8/test/fund_nav_test.py
--rw-r--r--   0 tomcat     (501) tomcat     (501)     1307 2023-02-14 03:34:22.000000 hbshare-3.7.8/test/simu_index_test.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.090709 hbshare-3.7.9/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1472 2023-02-14 03:34:22.000000 hbshare-3.7.9/LICENSE
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       57 2023-02-14 03:34:22.000000 hbshare-3.7.9/MANIFEST.in
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      906 2023-03-03 09:15:16.089709 hbshare-3.7.9/PKG-INFO
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       35 2023-02-14 03:34:22.000000 hbshare-3.7.9/README.md
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.898709 hbshare-3.7.9/hbshare/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        5 2023-03-03 09:15:03.000000 hbshare-3.7.9/hbshare/VERSION.txt
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      983 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.906709 hbshare-3.7.9/hbshare/base/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3240 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/BaseIndex.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      330 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/QueryException.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1519 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/data_api.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      596 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/data_pro.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2803 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/dateu.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6604 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/formula.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1133 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/upass.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      397 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/base/vars.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.907709 hbshare-3.7.9/hbshare/db/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    25454 2023-03-03 09:15:02.000000 hbshare-3.7.9/hbshare/db/ApiCfg.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2754 2023-03-03 09:15:02.000000 hbshare-3.7.9/hbshare/db/ApiUtils.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.909709 hbshare-3.7.9/hbshare/db/fund/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/fund/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2655 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/fund/cons.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3689 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/fund/nav.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1758 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/fund/product.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.911709 hbshare-3.7.9/hbshare/db/loader/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      212 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/loader/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1707 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/loader/data_query.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3151 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/loader/data_save.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.914709 hbshare-3.7.9/hbshare/db/simu/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/simu/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5383 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/simu/cons.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2443 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/simu/corp.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5579 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/simu/fund_rolling_calculator.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2000 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/simu/nav.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1580 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/simu/simu_index.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4013 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/db/simu/valuation.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.915709 hbshare-3.7.9/hbshare/fe/
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.915709 hbshare-3.7.9/hbshare/fe/AAM/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/AAM/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.918709 hbshare-3.7.9/hbshare/fe/AAM/blmodel/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/AAM/blmodel/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18855 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/AAM/blmodel/blmodel.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2166 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/AAM/blmodel/zep_test.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.919709 hbshare-3.7.9/hbshare/fe/FOF/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/FOF/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   137134 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/FOF/fof_analysis.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.921709 hbshare-3.7.9/hbshare/fe/Fund_classifier/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/Fund_classifier/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   116813 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/Fund_classifier/classification.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.922709 hbshare-3.7.9/hbshare/fe/Machine_learning/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/Machine_learning/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4312 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/Machine_learning/classifier.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.925709 hbshare-3.7.9/hbshare/fe/XZ/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/XZ/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.926709 hbshare-3.7.9/hbshare/fe/XZ/config/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/XZ/config/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5235 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/XZ/config/config_pfa.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    15088 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/XZ/db_engine.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    38505 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/XZ/functionality.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    41682 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/XZ/project.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.933709 hbshare-3.7.9/hbshare/fe/asset_allocation/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    35493 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/black_litterman.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1652 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/black_litterman_solver.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3999 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/data_loader.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4831 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/data_loader_db.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    22974 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/efficient_frontier.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6344 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/efficient_frontier_solver.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2751 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/efficient_frontier_solver_ori.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    44363 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/mean_variance.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     8276 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/mean_variance_solver.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    27130 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/risk_parity_budget.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4078 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/risk_parity_budget_solver.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    11645 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/asset_allocation/simple.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.934709 hbshare-3.7.9/hbshare/fe/brinson_attr/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/brinson_attr/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5799 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/brinson_attr/brinson_attribution_check.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    19214 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/brinson_attr/equity_brinson_attribution.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.936709 hbshare-3.7.9/hbshare/fe/common/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.941709 hbshare-3.7.9/hbshare/fe/common/util/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5310 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/config.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    56342 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/data_loader.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      643 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/exception.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10012 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/helper_func.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1180 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/logger.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5574 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/nav_util.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      860 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/omega_math.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    14308 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/plot_util.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4680 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/regressions.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5545 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/common/util/verifier.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.944709 hbshare-3.7.9/hbshare/fe/factor_analysis/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/factor_analysis/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5936 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/factor_analysis/multi_factors_model.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9204 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/factor_analysis/pool_mantainance.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    30762 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/factor_analysis/simple_factor_generator.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    24013 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/factor_analysis/single_factor_analysis.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.945709 hbshare-3.7.9/hbshare/fe/fund_manager/
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.946709 hbshare-3.7.9/hbshare/fe/fund_manager/Example/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/Example/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1695 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/Example/analysis_example.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1092 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/Example/database_operate_example.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.947709 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.949709 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/Analysis/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       52 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/Analysis/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      190 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/Analysis/functions.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    16544 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/Analysis/manager_life_net_worth.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       24 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.951709 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       32 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      678 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/database_connection.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1515 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/database_dictionary.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     8636 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/database_operate.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_manager/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.953709 hbshare-3.7.9/hbshare/fe/fund_style/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10562 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_style/MorningStarStyleBox.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_style/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2752 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/fund_style/morning_star_box_check.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.956709 hbshare-3.7.9/hbshare/fe/industry/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/industry/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    50231 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/industry/industry_analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   165421 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/industry/industry_analysis_data.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    17746 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/industry/industry_crowding.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   144633 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/industry/industry_tracking.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.969709 hbshare-3.7.9/hbshare/fe/mutual_analysis/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    66381 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/filter_engine.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   216898 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/fund_report.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   203254 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/fund_report_external.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   261798 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/holdind_based.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   117726 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/holding_analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    25589 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/holding_analysis_plot.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    88464 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/holding_compare_analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   190481 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/jj_picturing.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      139 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/main.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   140407 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/manager_report_external.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18943 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/mutual_fund_selection.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   198544 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/nav_based.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   122750 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/pool_analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    14153 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/mutual_analysis/theme_cluster.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.973709 hbshare-3.7.9/hbshare/fe/nav_attr/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/nav_attr/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    38357 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/nav_attr/bond_campisi_attribution.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3892 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/nav_attr/nav_attr_check.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18949 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/nav_attr/nav_attribution.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.974709 hbshare-3.7.9/hbshare/fe/sector_cluster/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/sector_cluster/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2437 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/sector_cluster/sector_factor_calculator.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.976709 hbshare-3.7.9/hbshare/fe/timing/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/timing/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   161697 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/timing/taa.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    48330 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/timing/timing_analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    90474 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/timing/timing_data.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.977709 hbshare-3.7.9/hbshare/fe/xwq/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.978709 hbshare-3.7.9/hbshare/fe/xwq/analysis/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.982709 hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6012 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/downward_volatility.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4787 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/lasso.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5310 2023-03-03 07:49:46.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/turnover.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.985709 hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1224 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/config.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    20217 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/fedb.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    41903 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/hbdb.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3255 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/http_request.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2881 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/plot.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.999709 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    34833 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/fund_holding_analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   100808 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/holder_structure.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   113144 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/holding_analysis_ori.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    27644 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/holding_analysis_plot_ori.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    20556 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/index_construction.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    17616 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/index_construction_885001.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3700 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/index_corr.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     8035 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_analysis_old.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    14307 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_tracking.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    13545 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_tracking_old.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    52970 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_tracking_report.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    25254 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/jc_comparasion.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4675 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/jgcg.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18022 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/new_high.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5649 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/pdf.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    35928 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/performance_comparison.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   199229 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/quantitative_report_external_ori.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1321 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/shift_cen_ratio_rank.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9195 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/style_index.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    13074 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/valuation.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    22440 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/valuation_earning_contribution.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2834 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/service/wenbo_holding_indu.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.007709 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2579 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/const_var.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     7699 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/data_processor.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2160 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/file_reader.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2177 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/file_writer.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1348 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/http_request.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      406 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/logger_utils.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1599 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/post.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4058 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/preprocess.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2837 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/send_email.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      340 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/singleton.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9361 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/timedelta_utils.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.008709 hbshare-3.7.9/hbshare/fe/xwq/test/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/fe/xwq/test/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.008709 hbshare-3.7.9/hbshare/quant/
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.016709 hbshare-3.7.9/hbshare/quant/CChen/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      322 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6885 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cons.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.021709 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      177 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5092 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     8754 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/const.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    57700 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/factor_algo.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    19031 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/factor_func.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10479 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/factor_index.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    16723 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/hsjy_func.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18530 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/hsjy_to_local.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2055 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/run.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6604 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/cta_factor/zep.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.024709 hbshare-3.7.9/hbshare/quant/CChen/data/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/data/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    22201 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/data/data.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1271 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/data/hsjy_data.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1795 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/data/run_wind.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2027 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/data/wind_cons.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    16186 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/data/wind_data.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2656 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/db_const.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.025709 hbshare-3.7.9/hbshare/quant/CChen/fof/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fof/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    12572 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fof/bt_engine.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4128 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/func.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.028709 hbshare-3.7.9/hbshare/quant/CChen/fund_stats/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fund_stats/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6926 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fund_stats/db.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18689 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fund_stats/perf.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    36104 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fund_stats/to_xl.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3274 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fund_stats/xl_cons.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    13605 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/fut.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.030709 hbshare-3.7.9/hbshare/quant/CChen/gzb/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/gzb/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10289 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/gzb/read_gzb.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9290 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/opt.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    61992 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/output.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1808 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/run_market.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1383 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/sql_cons.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10789 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/CChen/stk.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.031709 hbshare-3.7.9/hbshare/quant/Kevin/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.034709 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     7571 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/EconomicCycle.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1138 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/denoising.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    24038 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.049709 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2521 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/bond_trading.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3805 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/credit.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     7293 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/currency.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6103 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/eco_increase.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5217 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/future_data.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5630 2023-02-16 05:03:54.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/index_update.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3328 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/inflation.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   206199 2023-02-16 05:03:54.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/main.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3018 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/processed_market_index.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6214 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/rates_and_price.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4342 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cash_flow.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4746 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_concept.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6500 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cross_section_vol.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9550 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_market.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3367 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_share_price_index_futures.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4646 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_momentum.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4422 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_spread.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3606 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_time_series_vol.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6065 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4877 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading_cr.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3238 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/treasury_yield.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1272 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/util.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1704 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/marco_write_to_db.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10005 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/portfolio_index_calculator.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.053709 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    11797 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/CBMarketIV.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9874 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_iv_by_bs.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3273 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_pricing_BS.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5546 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_pricing_MC.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3358 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_pricing_Tree.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2058 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/group_test.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     8148 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/valuation_test.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.079709 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    13770 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/AlphaMonitor.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10515 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/AlphaPerformance.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6219 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/AlphaResearch.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1972 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Arbitrage_Strategy.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3381 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Arbitrage_backtest.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10600 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Arbitrage_with_Neutral.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    11453 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/CapIndex.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5300 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/CapRotation.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9003 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/CtaNavAttribution.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    12772 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/FundNavAnalysor.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1764 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/HedgeCalcultor.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    11089 2023-02-16 05:03:54.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/HoldingToDB.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18179 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/IndexActiveStyleAnalyse.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4377 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/IndexPEvsfuture_ret.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9824 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/IndexReturnAttr.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    16698 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/LocalNavComparer.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    27131 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MarketStructure.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    59707 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MarketStructure_Weekly.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4260 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MarketStructure_sample.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6662 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Multi-Strategy-Compare.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3952 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Multi-Strategy.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.084709 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1888 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/data_config.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4373 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/data_loader.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      650 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/util_func.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     7240 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Neutral_Tracker.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10021 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/PrivateFundNavAttr.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    32585 2023-02-16 05:03:54.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/PrivateHoldingAnalysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9790 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/QuarterAssetAllocationReport.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    20926 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/RiskControlReport.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     8125 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/S&P_Access_China_Analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     6639 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/SAR_Indicator.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)   110836 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Subjective_Strategy_Analysis.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4813 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/ThemeSector.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    19389 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_backtest.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5396 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_elasticity.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     9490 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_sourcing.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     7924 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_tracker.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1534 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/benchmark_nav_attr.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    18564 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/daily_nav_attr.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4940 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/data_prepare.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    20396 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/factor_crowd.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     7762 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/factor_crowd_plot.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     5979 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/portfolio_test.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4558 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/snow_ball.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     3025 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/stock_liq.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2243 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/strategy_index.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    20732 2023-02-16 05:03:54.000000 hbshare-3.7.9/hbshare/quant/Kevin/quant_room/tracker.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.086709 hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1679 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/config.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    21667 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/equity_brinson_attribution_datayes.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    10215 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/factor_return.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     4517 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/risk_model_check.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        0 2023-02-14 03:34:22.000000 hbshare-3.7.9/hbshare/quant/__init__.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:15.901709 hbshare-3.7.9/hbshare.egg-info/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      906 2023-03-03 09:15:15.000000 hbshare-3.7.9/hbshare.egg-info/PKG-INFO
+-rw-r--r--   0 tomcat     (501) tomcat     (501)    13792 2023-03-03 09:15:15.000000 hbshare-3.7.9/hbshare.egg-info/SOURCES.txt
+-rw-r--r--   0 tomcat     (501) tomcat     (501)        1 2023-03-03 09:15:15.000000 hbshare-3.7.9/hbshare.egg-info/dependency_links.txt
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       50 2023-03-03 09:15:15.000000 hbshare-3.7.9/hbshare.egg-info/requires.txt
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       13 2023-03-03 09:15:15.000000 hbshare-3.7.9/hbshare.egg-info/top_level.txt
+-rw-r--r--   0 tomcat     (501) tomcat     (501)       38 2023-03-03 09:15:16.090709 hbshare-3.7.9/setup.cfg
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2986 2023-02-14 03:34:22.000000 hbshare-3.7.9/setup.py
+drwxr-xr-x   0 tomcat     (501) tomcat     (501)        0 2023-03-03 09:15:16.088709 hbshare-3.7.9/test/
+-rw-r--r--   0 tomcat     (501) tomcat     (501)      213 2023-02-14 03:34:22.000000 hbshare-3.7.9/test/__init__.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2485 2023-02-14 03:34:22.000000 hbshare-3.7.9/test/db_data_save_test.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     2112 2023-02-14 03:34:22.000000 hbshare-3.7.9/test/fund_nav_test.py
+-rw-r--r--   0 tomcat     (501) tomcat     (501)     1307 2023-02-14 03:34:22.000000 hbshare-3.7.9/test/simu_index_test.py
```

### Comparing `hbshare-3.7.8/LICENSE` & `hbshare-3.7.9/LICENSE`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/PKG-INFO` & `hbshare-3.7.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: hbshare
-Version: 3.7.8
+Version: 3.7.9
 Summary: Howbuy Quantitative Research SDK.Fund product data query and withdrawal tools provided by Howbuy fund company for investment research
 Home-page: https://www.howbuy.com
 Author: meng.lv
 Author-email: 49007952@qq.com
 Maintainer: meng.lv
 Maintainer-email: 49007952@qq.com
 License: BSD
```

### Comparing `hbshare-3.7.8/hbshare/__init__.py` & `hbshare-3.7.9/hbshare/__init__.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/base/BaseIndex.py` & `hbshare-3.7.9/hbshare/base/BaseIndex.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/base/data_api.py` & `hbshare-3.7.9/hbshare/base/data_api.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/base/data_pro.py` & `hbshare-3.7.9/hbshare/base/data_pro.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/base/dateu.py` & `hbshare-3.7.9/hbshare/base/dateu.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/base/formula.py` & `hbshare-3.7.9/hbshare/base/formula.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/base/upass.py` & `hbshare-3.7.9/hbshare/base/upass.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/ApiCfg.py` & `hbshare-3.7.9/hbshare/db/ApiCfg.py`

 * *Files 5% similar despite different names*

```diff
@@ -78,22 +78,19 @@
                            'endTime': y['endDate']
                         },
                        supportFields=('hb1n', 'hb1y', 'hb1z', 'hb2n', "hb3n","hb3y","hb5n",
                                       "hb6y","hbcl","hbjn","jjsl","jyrq","scdm","spjg","tjrq","zqdm"
                                       )
                        )
     ''' 查询指数行情收盘价格 '''
-    # cplx枚举类型:
-    # "MUTUAL_INDEX" 公募策略指数  
-    # "PRIVATE_INDEX" 私募策略指数
-    # "MARKET_INDEX" 市场指数
-    # "MARKET_INDEX" 风格主题指数
     MARKET_SPJG_BATCH = UrlCfg('http://%s/data/zs/spj/batch', 'post', 'ams',
                         lambda x: {
-                           'products': x['products'],
+                           'sczs': x.get('sczs'),
+                           'gmclzs': x.get('gmclzs'),
+                           'smclzs': x.get('smclzs'),
                            'startTime': x['startDate'],
                            'endTime': x['endDate'],
                            'fields': x['fields']
                         },
                         lambda y: {},
                        supportFields=('hb1n', 'hb1y', 'hb1z', 'hb2n', "hb3n","hb3y","hb5n",
                                       "hb6y","hbcl","hbjn","jjsl","jyrq","scdm","spjg","tjrq","zqdm"
@@ -114,21 +111,19 @@
                             'startTime': y['startDate'],
                             'endTime': y['endDate']
                         },
                        supportFields=('jzrq', 'jjdm', 'jjjz', 'ljjz', 'hbcl','hbdr','fqdwjz')
                        )
     '''公募基金净值'''
     # 公募基金净值多基金代码
-    # cplx枚举类型:
-    # "MUTUAL_FUND" 公募基金
-    # "PRIVATE_FUND" 私募基金
 
     ALL_JJJZ = UrlCfg('http://%s/data/all/jz', 'post', 'ams',
                        lambda x: {
-                            'products': x['products'],
+                            'gmdm': x.get('gmdm'),
+                            'smdm': x.get('smdm'),
                             'startTime': x['startDate'],
                             'endTime': x['endDate'],
                             'fields': x['fields']
                        },
                        lambda y: {},
                        supportFields=('jzrq', 'jjdm', 'jjjz', 'ljjz', 'hbcl','hbdr','fqdwjz')
                        )
```

### Comparing `hbshare-3.7.8/hbshare/db/ApiUtils.py` & `hbshare-3.7.9/hbshare/db/ApiUtils.py`

 * *Files 12% similar despite different names*

```diff
@@ -77,11 +77,11 @@
         data.append(body)
     prod_df = pd.DataFrame(data, columns=kwargs['fields'])
     return prod_df
 
 
 if __name__ == '__main__':
 
-    data = commonQuery('MARKET_SPJG_BATCH',
-                       products =[{'cpdm':'000300','cplx':'MARKET_INDEX'},{'cpdm':'HM0002','cplx':'MUTUAL_INDEX'}],
+    data = commonQuery('ALL_JJJZ',gmdm=['000001'],smdm=['HM0002'],
                        startDate= '20150214',endDate='20160812')
     print(data)
+
```

### Comparing `hbshare-3.7.8/hbshare/db/fund/cons.py` & `hbshare-3.7.9/hbshare/db/fund/cons.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/fund/nav.py` & `hbshare-3.7.9/hbshare/db/fund/nav.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/fund/product.py` & `hbshare-3.7.9/hbshare/db/fund/product.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/loader/data_query.py` & `hbshare-3.7.9/hbshare/db/loader/data_query.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/loader/data_save.py` & `hbshare-3.7.9/hbshare/db/loader/data_save.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/simu/cons.py` & `hbshare-3.7.9/hbshare/db/simu/cons.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/simu/corp.py` & `hbshare-3.7.9/hbshare/db/simu/corp.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/simu/fund_rolling_calculator.py` & `hbshare-3.7.9/hbshare/db/simu/fund_rolling_calculator.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/simu/nav.py` & `hbshare-3.7.9/hbshare/db/simu/nav.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/simu/simu_index.py` & `hbshare-3.7.9/hbshare/db/simu/simu_index.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/db/simu/valuation.py` & `hbshare-3.7.9/hbshare/db/simu/valuation.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/AAM/blmodel/blmodel.py` & `hbshare-3.7.9/hbshare/fe/AAM/blmodel/blmodel.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/AAM/blmodel/zep_test.py` & `hbshare-3.7.9/hbshare/fe/AAM/blmodel/zep_test.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/FOF/fof_analysis.py` & `hbshare-3.7.9/hbshare/fe/FOF/fof_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/Fund_classifier/classification.py` & `hbshare-3.7.9/hbshare/fe/Fund_classifier/classification.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/Machine_learning/classifier.py` & `hbshare-3.7.9/hbshare/fe/Machine_learning/classifier.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/XZ/config/config_pfa.py` & `hbshare-3.7.9/hbshare/fe/XZ/config/config_pfa.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/XZ/db_engine.py` & `hbshare-3.7.9/hbshare/fe/XZ/db_engine.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/XZ/functionality.py` & `hbshare-3.7.9/hbshare/fe/XZ/functionality.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/XZ/project.py` & `hbshare-3.7.9/hbshare/fe/XZ/project.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/black_litterman.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/black_litterman.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/black_litterman_solver.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/black_litterman_solver.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/data_loader.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/data_loader.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/data_loader_db.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/data_loader_db.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/efficient_frontier.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/efficient_frontier.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/efficient_frontier_solver.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/efficient_frontier_solver.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/efficient_frontier_solver_ori.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/efficient_frontier_solver_ori.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/mean_variance.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/mean_variance.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/mean_variance_solver.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/mean_variance_solver.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/risk_parity_budget.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/risk_parity_budget.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/risk_parity_budget_solver.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/risk_parity_budget_solver.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/asset_allocation/simple.py` & `hbshare-3.7.9/hbshare/fe/asset_allocation/simple.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/brinson_attr/brinson_attribution_check.py` & `hbshare-3.7.9/hbshare/fe/brinson_attr/brinson_attribution_check.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/brinson_attr/equity_brinson_attribution.py` & `hbshare-3.7.9/hbshare/fe/brinson_attr/equity_brinson_attribution.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/config.py` & `hbshare-3.7.9/hbshare/fe/common/util/config.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/data_loader.py` & `hbshare-3.7.9/hbshare/fe/common/util/data_loader.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/exception.py` & `hbshare-3.7.9/hbshare/fe/common/util/exception.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/helper_func.py` & `hbshare-3.7.9/hbshare/fe/common/util/helper_func.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/logger.py` & `hbshare-3.7.9/hbshare/fe/common/util/logger.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/nav_util.py` & `hbshare-3.7.9/hbshare/fe/common/util/nav_util.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/omega_math.py` & `hbshare-3.7.9/hbshare/fe/common/util/omega_math.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/plot_util.py` & `hbshare-3.7.9/hbshare/fe/common/util/plot_util.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/regressions.py` & `hbshare-3.7.9/hbshare/fe/common/util/regressions.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/common/util/verifier.py` & `hbshare-3.7.9/hbshare/fe/common/util/verifier.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/factor_analysis/multi_factors_model.py` & `hbshare-3.7.9/hbshare/fe/factor_analysis/multi_factors_model.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/factor_analysis/pool_mantainance.py` & `hbshare-3.7.9/hbshare/fe/factor_analysis/pool_mantainance.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/factor_analysis/simple_factor_generator.py` & `hbshare-3.7.9/hbshare/fe/factor_analysis/simple_factor_generator.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/factor_analysis/single_factor_analysis.py` & `hbshare-3.7.9/hbshare/fe/factor_analysis/single_factor_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_manager/Example/analysis_example.py` & `hbshare-3.7.9/hbshare/fe/fund_manager/Example/analysis_example.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_manager/Example/database_operate_example.py` & `hbshare-3.7.9/hbshare/fe/fund_manager/Example/database_operate_example.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/Analysis/manager_life_net_worth.py` & `hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/Analysis/manager_life_net_worth.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/database_connection.py` & `hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/database_connection.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/database_dictionary.py` & `hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/database_dictionary.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_manager/FundManager/database/database_operate.py` & `hbshare-3.7.9/hbshare/fe/fund_manager/FundManager/database/database_operate.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_style/MorningStarStyleBox.py` & `hbshare-3.7.9/hbshare/fe/fund_style/MorningStarStyleBox.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/fund_style/morning_star_box_check.py` & `hbshare-3.7.9/hbshare/fe/fund_style/morning_star_box_check.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/industry/industry_analysis.py` & `hbshare-3.7.9/hbshare/fe/industry/industry_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/industry/industry_analysis_data.py` & `hbshare-3.7.9/hbshare/fe/industry/industry_analysis_data.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/industry/industry_crowding.py` & `hbshare-3.7.9/hbshare/fe/industry/industry_crowding.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/industry/industry_tracking.py` & `hbshare-3.7.9/hbshare/fe/industry/industry_tracking.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/filter_engine.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/filter_engine.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/fund_report.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/fund_report.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/fund_report_external.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/fund_report_external.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/holdind_based.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/holdind_based.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/holding_analysis.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/holding_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/holding_analysis_plot.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/holding_analysis_plot.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/holding_compare_analysis.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/holding_compare_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/jj_picturing.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/jj_picturing.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/manager_report_external.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/manager_report_external.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/mutual_fund_selection.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/mutual_fund_selection.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/nav_based.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/nav_based.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/pool_analysis.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/pool_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/mutual_analysis/theme_cluster.py` & `hbshare-3.7.9/hbshare/fe/mutual_analysis/theme_cluster.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/nav_attr/bond_campisi_attribution.py` & `hbshare-3.7.9/hbshare/fe/nav_attr/bond_campisi_attribution.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/nav_attr/nav_attr_check.py` & `hbshare-3.7.9/hbshare/fe/nav_attr/nav_attr_check.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/nav_attr/nav_attribution.py` & `hbshare-3.7.9/hbshare/fe/nav_attr/nav_attribution.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/sector_cluster/sector_factor_calculator.py` & `hbshare-3.7.9/hbshare/fe/sector_cluster/sector_factor_calculator.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/timing/taa.py` & `hbshare-3.7.9/hbshare/fe/timing/taa.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/timing/timing_analysis.py` & `hbshare-3.7.9/hbshare/fe/timing/timing_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/timing/timing_data.py` & `hbshare-3.7.9/hbshare/fe/timing/timing_data.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/downward_volatility.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/downward_volatility.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/lasso.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/lasso.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/institution_demand/turnover.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/institution_demand/turnover.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/config.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/config.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/fedb.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/fedb.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/hbdb.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/hbdb.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/http_request.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/http_request.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/orm/plot.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/orm/plot.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/fund_holding_analysis.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/fund_holding_analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/holder_structure.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/holder_structure.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/holding_analysis_ori.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/holding_analysis_ori.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/holding_analysis_plot_ori.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/holding_analysis_plot_ori.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/index_construction.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/index_construction.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/index_construction_885001.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/index_construction_885001.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/index_corr.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/index_corr.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_analysis_old.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_analysis_old.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_tracking.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_tracking.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_tracking_old.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_tracking_old.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/industry_tracking_report.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/industry_tracking_report.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/jc_comparasion.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/jc_comparasion.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/jgcg.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/jgcg.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/new_high.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/new_high.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/pdf.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/pdf.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/performance_comparison.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/performance_comparison.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/quantitative_report_external_ori.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/quantitative_report_external_ori.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/shift_cen_ratio_rank.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/shift_cen_ratio_rank.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/style_index.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/style_index.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/valuation.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/valuation.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/valuation_earning_contribution.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/valuation_earning_contribution.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/service/wenbo_holding_indu.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/service/wenbo_holding_indu.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/const_var.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/const_var.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/data_processor.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/data_processor.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/file_reader.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/file_reader.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/file_writer.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/file_writer.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/http_request.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/http_request.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/post.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/post.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/preprocess.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/preprocess.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/send_email.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/send_email.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/fe/xwq/analysis/utils/timedelta_utils.py` & `hbshare-3.7.9/hbshare/fe/xwq/analysis/utils/timedelta_utils.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cons.py` & `hbshare-3.7.9/hbshare/quant/CChen/cons.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/analysis.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/const.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/const.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/factor_algo.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/factor_algo.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/factor_func.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/factor_func.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/factor_index.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/factor_index.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/hsjy_func.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/hsjy_func.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/hsjy_to_local.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/hsjy_to_local.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/run.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/run.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/cta_factor/zep.py` & `hbshare-3.7.9/hbshare/quant/CChen/cta_factor/zep.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/data/data.py` & `hbshare-3.7.9/hbshare/quant/CChen/data/data.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/data/hsjy_data.py` & `hbshare-3.7.9/hbshare/quant/CChen/data/hsjy_data.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/data/run_wind.py` & `hbshare-3.7.9/hbshare/quant/CChen/data/run_wind.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/data/wind_cons.py` & `hbshare-3.7.9/hbshare/quant/CChen/data/wind_cons.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/data/wind_data.py` & `hbshare-3.7.9/hbshare/quant/CChen/data/wind_data.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/db_const.py` & `hbshare-3.7.9/hbshare/quant/CChen/db_const.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/fof/bt_engine.py` & `hbshare-3.7.9/hbshare/quant/CChen/fof/bt_engine.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/func.py` & `hbshare-3.7.9/hbshare/quant/CChen/func.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/fund_stats/db.py` & `hbshare-3.7.9/hbshare/quant/CChen/fund_stats/db.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/fund_stats/perf.py` & `hbshare-3.7.9/hbshare/quant/CChen/fund_stats/perf.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/fund_stats/to_xl.py` & `hbshare-3.7.9/hbshare/quant/CChen/fund_stats/to_xl.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/fund_stats/xl_cons.py` & `hbshare-3.7.9/hbshare/quant/CChen/fund_stats/xl_cons.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/fut.py` & `hbshare-3.7.9/hbshare/quant/CChen/fut.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/gzb/read_gzb.py` & `hbshare-3.7.9/hbshare/quant/CChen/gzb/read_gzb.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/opt.py` & `hbshare-3.7.9/hbshare/quant/CChen/opt.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/output.py` & `hbshare-3.7.9/hbshare/quant/CChen/output.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/run_market.py` & `hbshare-3.7.9/hbshare/quant/CChen/run_market.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/sql_cons.py` & `hbshare-3.7.9/hbshare/quant/CChen/sql_cons.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/CChen/stk.py` & `hbshare-3.7.9/hbshare/quant/CChen/stk.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/EconomicCycle.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/EconomicCycle.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/denoising.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/denoising.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/bond_trading.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/bond_trading.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/credit.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/credit.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/currency.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/currency.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/eco_increase.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/eco_increase.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/future_data.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/future_data.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/index_update.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/index_update.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/inflation.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/inflation.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/main.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/main.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/processed_market_index.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/processed_market_index.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/rates_and_price.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/rates_and_price.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cash_flow.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cash_flow.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_concept.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_concept.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cross_section_vol.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_cross_section_vol.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_market.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_market.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_share_price_index_futures.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_share_price_index_futures.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_momentum.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_momentum.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_spread.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_style_spread.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_time_series_vol.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_time_series_vol.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading_cr.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/stock_trading_cr.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/treasury_yield.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/treasury_yield.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/macro_index/util.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/macro_index/util.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/marco_write_to_db.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/marco_write_to_db.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/asset_allocation/portfolio_index_calculator.py` & `hbshare-3.7.9/hbshare/quant/Kevin/asset_allocation/portfolio_index_calculator.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/CBMarketIV.py` & `hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/CBMarketIV.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_iv_by_bs.py` & `hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_iv_by_bs.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_pricing_BS.py` & `hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_pricing_BS.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_pricing_MC.py` & `hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_pricing_MC.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/cb_pricing_Tree.py` & `hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/cb_pricing_Tree.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/group_test.py` & `hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/group_test.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/convertible_bond/valuation_test.py` & `hbshare-3.7.9/hbshare/quant/Kevin/convertible_bond/valuation_test.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/AlphaMonitor.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/AlphaMonitor.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/AlphaPerformance.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/AlphaPerformance.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/AlphaResearch.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/AlphaResearch.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Arbitrage_Strategy.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Arbitrage_Strategy.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Arbitrage_backtest.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Arbitrage_backtest.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Arbitrage_with_Neutral.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Arbitrage_with_Neutral.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/CapIndex.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/CapIndex.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/CapRotation.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/CapRotation.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/CtaNavAttribution.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/CtaNavAttribution.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/FundNavAnalysor.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/FundNavAnalysor.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/HedgeCalcultor.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/HedgeCalcultor.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/HoldingToDB.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/HoldingToDB.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/IndexActiveStyleAnalyse.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/IndexActiveStyleAnalyse.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/IndexPEvsfuture_ret.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/IndexPEvsfuture_ret.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/IndexReturnAttr.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/IndexReturnAttr.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/LocalNavComparer.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/LocalNavComparer.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MarketStructure.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MarketStructure.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MarketStructure_Weekly.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MarketStructure_Weekly.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MarketStructure_sample.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MarketStructure_sample.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Multi-Strategy-Compare.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Multi-Strategy-Compare.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Multi-Strategy.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Multi-Strategy.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/data_config.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/data_config.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/data_loader.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/data_loader.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/MyUtil/util_func.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/MyUtil/util_func.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Neutral_Tracker.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Neutral_Tracker.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/PrivateFundNavAttr.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/PrivateFundNavAttr.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/PrivateHoldingAnalysis.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/PrivateHoldingAnalysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/QuarterAssetAllocationReport.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/QuarterAssetAllocationReport.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/RiskControlReport.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/RiskControlReport.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/S&P_Access_China_Analysis.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/S&P_Access_China_Analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/SAR_Indicator.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/SAR_Indicator.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/Subjective_Strategy_Analysis.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/Subjective_Strategy_Analysis.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/ThemeSector.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/ThemeSector.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_backtest.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_backtest.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_elasticity.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_elasticity.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_sourcing.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_sourcing.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/alpha_tracker.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/alpha_tracker.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/benchmark_nav_attr.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/benchmark_nav_attr.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/daily_nav_attr.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/daily_nav_attr.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/data_prepare.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/data_prepare.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/factor_crowd.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/factor_crowd.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/factor_crowd_plot.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/factor_crowd_plot.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/portfolio_test.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/portfolio_test.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/snow_ball.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/snow_ball.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/stock_liq.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/stock_liq.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/strategy_index.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/strategy_index.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/quant_room/tracker.py` & `hbshare-3.7.9/hbshare/quant/Kevin/quant_room/tracker.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/config.py` & `hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/config.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/equity_brinson_attribution_datayes.py` & `hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/equity_brinson_attribution_datayes.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/factor_return.py` & `hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/factor_return.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare/quant/Kevin/rm_associated/risk_model_check.py` & `hbshare-3.7.9/hbshare/quant/Kevin/rm_associated/risk_model_check.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/hbshare.egg-info/PKG-INFO` & `hbshare-3.7.9/hbshare.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: hbshare
-Version: 3.7.8
+Version: 3.7.9
 Summary: Howbuy Quantitative Research SDK.Fund product data query and withdrawal tools provided by Howbuy fund company for investment research
 Home-page: https://www.howbuy.com
 Author: meng.lv
 Author-email: 49007952@qq.com
 Maintainer: meng.lv
 Maintainer-email: 49007952@qq.com
 License: BSD
```

### Comparing `hbshare-3.7.8/hbshare.egg-info/SOURCES.txt` & `hbshare-3.7.9/hbshare.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/setup.py` & `hbshare-3.7.9/setup.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/test/db_data_save_test.py` & `hbshare-3.7.9/test/db_data_save_test.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/test/fund_nav_test.py` & `hbshare-3.7.9/test/fund_nav_test.py`

 * *Files identical despite different names*

### Comparing `hbshare-3.7.8/test/simu_index_test.py` & `hbshare-3.7.9/test/simu_index_test.py`

 * *Files identical despite different names*

