# Comparing `tmp/akshare-1.9.8.tar.gz` & `tmp/akshare-1.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "akshare-1.9.8.tar", last modified: Thu Mar  9 14:50:14 2023, max compression
+gzip compressed data, was "akshare-1.9.9.tar", last modified: Thu Mar  9 15:07:22 2023, max compression
```

## Comparing `akshare-1.9.8.tar` & `akshare-1.9.9.tar`

### file list

```diff
@@ -1,396 +1,396 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.689692 akshare-1.9.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-03-09 14:50:00.000000 akshare-1.9.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    14801 2023-03-09 14:50:14.689692 akshare-1.9.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    13964 2023-03-09 14:50:00.000000 akshare-1.9.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.641689 akshare-1.9.8/akshare/
--rw-r--r--   0 runner    (1001) docker     (123)   148994 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.645689 akshare-1.9.8/akshare/air/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/air/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4423 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/air/air_hebei.py
--rw-r--r--   0 runner    (1001) docker     (123)    10809 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/air/air_zhenqi.py
--rw-r--r--   0 runner    (1001) docker     (123)     9771 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/air/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)     8443 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/air/crypto.js
--rw-r--r--   0 runner    (1001) docker     (123)   142353 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/air/outcrypto.js
--rw-r--r--   0 runner    (1001) docker     (123)     4004 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/air/sunrise_tad.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.645689 akshare-1.9.8/akshare/article/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/article/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/article/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)     1748 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/article/epu_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     4106 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/article/ff_factor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/article/fred_md.py
--rw-r--r--   0 runner    (1001) docker     (123)    13162 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/article/risk_rv.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.645689 akshare-1.9.8/akshare/bank/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bank/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6196 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bank/bank_cbirc_2020.py
--rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bank/cons.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.649689 akshare-1.9.8/akshare/bond/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2929 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_bank.py
--rw-r--r--   0 runner    (1001) docker     (123)     6301 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_cbond.py
--rw-r--r--   0 runner    (1001) docker     (123)     4537 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_china_money.py
--rw-r--r--   0 runner    (1001) docker     (123)    10777 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     4343 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2326 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_futures.py
--rw-r--r--   0 runner    (1001) docker     (123)     7517 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_info_cm.py
--rw-r--r--   0 runner    (1001) docker     (123)     4990 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_investing.py
--rw-r--r--   0 runner    (1001) docker     (123)    21295 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_issue_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     3581 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_summary.py
--rw-r--r--   0 runner    (1001) docker     (123)    23003 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_zh_cov_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     4098 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/bond_zh_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     6550 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/china_bond.py
--rw-r--r--   0 runner    (1001) docker     (123)     1432 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/china_repo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1792 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/bond/cons.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.649689 akshare-1.9.8/akshare/cost/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/cost/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2005 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/cost/cost_living.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.649689 akshare-1.9.8/akshare/crypto/
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/crypto/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1885 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/crypto/crypto_bitcoin_cme.py
--rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/crypto/crypto_crix.py
--rw-r--r--   0 runner    (1001) docker     (123)     9748 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/crypto/crypto_hist_investing.py
--rw-r--r--   0 runner    (1001) docker     (123)     3890 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/crypto/crypto_hold.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.649689 akshare-1.9.8/akshare/currency/
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/currency/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5419 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/currency/currency.py
--rw-r--r--   0 runner    (1001) docker     (123)     3641 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/currency/currency_china_bank_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/currency/currency_safe.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.649689 akshare-1.9.8/akshare/data/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   209327 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/data/covid.js
--rw-r--r--   0 runner    (1001) docker     (123)   122225 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/data/crypto_info.zip
--rw-r--r--   0 runner    (1001) docker     (123)    39664 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/data/ths.js
--rw-r--r--   0 runner    (1001) docker     (123)     1631 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/datasets.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.653689 akshare-1.9.8/akshare/economic/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16594 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)    10801 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_australia.py
--rw-r--r--   0 runner    (1001) docker     (123)    31987 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_bank.py
--rw-r--r--   0 runner    (1001) docker     (123)    15195 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_canada.py
--rw-r--r--   0 runner    (1001) docker     (123)   177779 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_china.py
--rw-r--r--   0 runner    (1001) docker     (123)    11765 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_china_hk.py
--rw-r--r--   0 runner    (1001) docker     (123)     8083 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_constitute.py
--rw-r--r--   0 runner    (1001) docker     (123)    40919 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_euro.py
--rw-r--r--   0 runner    (1001) docker     (123)     5912 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_germany.py
--rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_japan.py
--rw-r--r--   0 runner    (1001) docker     (123)     6954 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_other.py
--rw-r--r--   0 runner    (1001) docker     (123)     4403 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_swiss.py
--rw-r--r--   0 runner    (1001) docker     (123)     8469 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_uk.py
--rw-r--r--   0 runner    (1001) docker     (123)   121523 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/macro_usa.py
--rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/economic/marco_cnbs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.653689 akshare-1.9.8/akshare/energy/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/energy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11913 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/energy/energy_carbon.py
--rw-r--r--   0 runner    (1001) docker     (123)     3775 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/energy/energy_oil_em.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.653689 akshare-1.9.8/akshare/event/
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/event/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12807 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/event/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)    38159 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/event/covid.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.653689 akshare-1.9.8/akshare/file_fold/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/file_fold/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   112983 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/file_fold/calendar.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.653689 akshare-1.9.8/akshare/fortune/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fortune/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4117 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fortune/fortune_500.py
--rw-r--r--   0 runner    (1001) docker     (123)     3673 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fortune/fortune_bloomberg.py
--rw-r--r--   0 runner    (1001) docker     (123)     1437 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fortune/fortune_forbes_500.py
--rw-r--r--   0 runner    (1001) docker     (123)    11776 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fortune/fortune_hurun.py
--rw-r--r--   0 runner    (1001) docker     (123)     3257 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fortune/fortune_it_juzi.py
--rw-r--r--   0 runner    (1001) docker     (123)     1827 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fortune/fortune_xincaifu_500.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.657690 akshare-1.9.8/akshare/fund/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    31404 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_amac.py
--rw-r--r--   0 runner    (1001) docker     (123)     3186 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_aum_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    40110 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    11943 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_etf_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     4917 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_etf_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     5546 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_fhsp_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2141 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_init_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    10413 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_portfolio_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     3235 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_position_lg.py
--rw-r--r--   0 runner    (1001) docker     (123)    12325 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_rank_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     8886 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_rating.py
--rw-r--r--   0 runner    (1001) docker     (123)     9254 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_report_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4010 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_scale_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     8092 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fund/fund_scale_sina.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.661690 akshare-1.9.8/akshare/futures/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16982 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)    48820 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/cot.py
--rw-r--r--   0 runner    (1001) docker     (123)    13386 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_basis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_comex.py
--rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_comm_qihuo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1135 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_contract_detail.py
--rw-r--r--   0 runner    (1001) docker     (123)    26034 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_daily_bar.py
--rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_foreign.py
--rw-r--r--   0 runner    (1001) docker     (123)     8418 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_hq_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     4479 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_index_ccidx.py
--rw-r--r--   0 runner    (1001) docker     (123)     6946 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_international.py
--rw-r--r--   0 runner    (1001) docker     (123)     8410 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_inventory_99.py
--rw-r--r--   0 runner    (1001) docker     (123)     2340 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_inventory_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     1531 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_news_baidu.py
--rw-r--r--   0 runner    (1001) docker     (123)     2462 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_news_shmet.py
--rw-r--r--   0 runner    (1001) docker     (123)     6272 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_roll_yield.py
--rw-r--r--   0 runner    (1001) docker     (123)     1471 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_rule.py
--rw-r--r--   0 runner    (1001) docker     (123)     2238 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_sgx_daily.py
--rw-r--r--   0 runner    (1001) docker     (123)     3297 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_spot_stock_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    10509 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_to_spot.py
--rw-r--r--   0 runner    (1001) docker     (123)     6388 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_warehouse_receipt.py
--rw-r--r--   0 runner    (1001) docker     (123)    23910 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/futures_zh_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     4097 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/inventory_data.py
--rw-r--r--   0 runner    (1001) docker     (123)    19049 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/receipt.py
--rw-r--r--   0 runner    (1001) docker     (123)     2770 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/requests_fun.py
--rw-r--r--   0 runner    (1001) docker     (123)     5148 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures/symbol_var.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.661690 akshare-1.9.8/akshare/futures_derivative/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5927 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)     4819 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/futures_egg.py
--rw-r--r--   0 runner    (1001) docker     (123)    14308 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/futures_hog.py
--rw-r--r--   0 runner    (1001) docker     (123)     2052 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/futures_index_price_nh.py
--rw-r--r--   0 runner    (1001) docker     (123)     1563 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/futures_index_return_nh.py
--rw-r--r--   0 runner    (1001) docker     (123)     1561 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/futures_index_volatility_nh.py
--rw-r--r--   0 runner    (1001) docker     (123)     4255 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/futures_other_index_nh.py
--rw-r--r--   0 runner    (1001) docker     (123)     1386 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/futures_sina_cot.py
--rw-r--r--   0 runner    (1001) docker     (123)     5439 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/sina_futures_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     3537 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/futures_derivative/sys_spot_futures.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.661690 akshare-1.9.8/akshare/fx/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fx/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      585 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fx/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)    12574 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fx/currency_investing.py
--rw-r--r--   0 runner    (1001) docker     (123)     3427 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fx/fx_quote.py
--rw-r--r--   0 runner    (1001) docker     (123)     2314 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/fx/fx_quote_baidu.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.661690 akshare-1.9.8/akshare/hf/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/hf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1206 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/hf/hf_sp500.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.665690 akshare-1.9.8/akshare/index/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3551 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)     5432 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/dailydata.py
--rw-r--r--   0 runner    (1001) docker     (123)     2986 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/drewry_index.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    53902 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_baidu.py
--rw-r--r--   0 runner    (1001) docker     (123)     4263 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_cflp.py
--rw-r--r--   0 runner    (1001) docker     (123)     7478 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_cni.py
--rw-r--r--   0 runner    (1001) docker     (123)     8742 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_cons.py
--rw-r--r--   0 runner    (1001) docker     (123)    11943 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_cx.py
--rw-r--r--   0 runner    (1001) docker     (123)     1768 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_eri.py
--rw-r--r--   0 runner    (1001) docker     (123)     1636 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_google.py
--rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_hog.py
--rw-r--r--   0 runner    (1001) docker     (123)    12177 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_investing.py
--rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_kq_fz.py
--rw-r--r--   0 runner    (1001) docker     (123)     3294 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_kq_ss.py
--rw-r--r--   0 runner    (1001) docker     (123)     1680 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_spot.py
--rw-r--r--   0 runner    (1001) docker     (123)     9688 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_stock_zh.py
--rw-r--r--   0 runner    (1001) docker     (123)     4566 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_sugar.py
--rw-r--r--   0 runner    (1001) docker     (123)    29465 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_sw.py
--rw-r--r--   0 runner    (1001) docker     (123)    16818 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_sw_research.py
--rw-r--r--   0 runner    (1001) docker     (123)     2261 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_weibo.py
--rw-r--r--   0 runner    (1001) docker     (123)     3411 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_yw.py
--rw-r--r--   0 runner    (1001) docker     (123)    15811 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/index_zh_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    23023 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/request.py
--rw-r--r--   0 runner    (1001) docker     (123)     7971 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/index/stock_zh_index_csindex.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.665690 akshare-1.9.8/akshare/interest_rate/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/interest_rate/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4385 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/interest_rate/interbank_rate_em.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.665690 akshare-1.9.8/akshare/movie/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/movie/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3710 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/movie/artist_yien.py
--rw-r--r--   0 runner    (1001) docker     (123)   117172 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/movie/jm.js
--rw-r--r--   0 runner    (1001) docker     (123)    12312 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/movie/movie_yien.py
--rw-r--r--   0 runner    (1001) docker     (123)     3404 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/movie/video_yien.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.669691 akshare-1.9.8/akshare/news/
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/news/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7642 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/news/news_baidu.py
--rw-r--r--   0 runner    (1001) docker     (123)     7387 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/news/news_cctv.py
--rw-r--r--   0 runner    (1001) docker     (123)     2874 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/news/news_stock.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.669691 akshare-1.9.8/akshare/nlp/
--rw-r--r--   0 runner    (1001) docker     (123)       79 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/nlp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1858 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/nlp/nlp_interface.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.669691 akshare-1.9.8/akshare/option/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4352 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)    13817 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_commodity.py
--rw-r--r--   0 runner    (1001) docker     (123)     7776 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_commodity_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     1812 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_czce.py
--rw-r--r--   0 runner    (1001) docker     (123)     3031 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     8548 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_finance.py
--rw-r--r--   0 runner    (1001) docker     (123)    34775 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_finance_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     8417 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_lhb_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_premium_analysis_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_qvix.py
--rw-r--r--   0 runner    (1001) docker     (123)     2505 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_risk_analysis_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2444 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_risk_indicator_sse.py
--rw-r--r--   0 runner    (1001) docker     (123)     2487 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/option/option_value_analysis_em.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.669691 akshare-1.9.8/akshare/other/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/other/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4301 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/other/other_car.py
--rw-r--r--   0 runner    (1001) docker     (123)     5661 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/other/other_game.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.669691 akshare-1.9.8/akshare/pro/
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/pro/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2248 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/pro/client.py
--rw-r--r--   0 runner    (1001) docker     (123)      244 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/pro/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)      830 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/pro/data_pro.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.669691 akshare-1.9.8/akshare/qhkc/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/qhkc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8235 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/qhkc/qhkc_api.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.669691 akshare-1.9.8/akshare/qhkc_web/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/qhkc_web/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17400 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/qhkc_web/qhkc_fund.py
--rw-r--r--   0 runner    (1001) docker     (123)     9109 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/qhkc_web/qhkc_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     9083 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/qhkc_web/qhkc_tool.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.673691 akshare-1.9.8/akshare/rate/
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/rate/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2018 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/rate/repo_rate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.673691 akshare-1.9.8/akshare/reits/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/reits/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4137 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/reits/reits_basic.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.673691 akshare-1.9.8/akshare/sport/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/sport/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      818 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/sport/sport_olympic.py
--rw-r--r--   0 runner    (1001) docker     (123)     1473 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/sport/sport_olympic_winter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.673691 akshare-1.9.8/akshare/spot/
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/spot/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6899 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/spot/spot_sge.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.677691 akshare-1.9.8/akshare/stock/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    35986 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)     6946 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_allotment_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)    12289 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_board_concept_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    12597 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_board_industry_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     4202 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_cg_equity_mortgage.py
--rw-r--r--   0 runner    (1001) docker     (123)     4637 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_cg_guarantee.py
--rw-r--r--   0 runner    (1001) docker     (123)     4212 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_cg_lawsuit.py
--rw-r--r--   0 runner    (1001) docker     (123)     3983 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_dividents_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)    20519 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_dzjy_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    22924 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_fund.py
--rw-r--r--   0 runner    (1001) docker     (123)     6056 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_fund_hold.py
--rw-r--r--   0 runner    (1001) docker     (123)     4114 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_hist_163.py
--rw-r--r--   0 runner    (1001) docker     (123)     8298 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_hk_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     7821 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_hold_control_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4434 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_hold_num_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     7130 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_hot_rank_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_hot_search_baidu.py
--rw-r--r--   0 runner    (1001) docker     (123)     5568 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_industry.py
--rw-r--r--   0 runner    (1001) docker     (123)     7321 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_industry_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     5068 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_industry_pe_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)    15590 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     2414 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_info_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     6290 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_new_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4070 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_profile_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4022 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_rank_forecast.py
--rw-r--r--   0 runner    (1001) docker     (123)     5000 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_repurchase_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     5653 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_share_changes_cninfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1185 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_stop.py
--rw-r--r--   0 runner    (1001) docker     (123)    16473 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_summary.py
--rw-r--r--   0 runner    (1001) docker     (123)     3585 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_us_famous.py
--rw-r--r--   0 runner    (1001) docker     (123)     2502 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_us_js.py
--rw-r--r--   0 runner    (1001) docker     (123)     3047 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_us_pink.py
--rw-r--r--   0 runner    (1001) docker     (123)     9816 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_us_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     5046 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_us_zh_hx.py
--rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_weibo_nlp.py
--rw-r--r--   0 runner    (1001) docker     (123)    17824 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_zh_a_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)    10290 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_zh_a_special.py
--rw-r--r--   0 runner    (1001) docker     (123)     6660 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_zh_a_tick_tx_163.py
--rw-r--r--   0 runner    (1001) docker     (123)     8923 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_zh_ah_tx.py
--rw-r--r--   0 runner    (1001) docker     (123)    16109 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_zh_b_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     2879 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_zh_kcb_report.py
--rw-r--r--   0 runner    (1001) docker     (123)     9033 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock/stock_zh_kcb_sina.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.685692 akshare-1.9.8/akshare/stock_feature/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/cons.py
--rw-r--r--   0 runner    (1001) docker     (123)     2042 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_a_below_net_asset_statistics.py
--rw-r--r--   0 runner    (1001) docker     (123)     1872 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_a_high_low.py
--rw-r--r--   0 runner    (1001) docker     (123)     3953 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_a_indicator.py
--rw-r--r--   0 runner    (1001) docker     (123)    12741 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_a_pb.py
--rw-r--r--   0 runner    (1001) docker     (123)    13917 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_a_pe.py
--rw-r--r--   0 runner    (1001) docker     (123)    17360 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_a_pe_and_pb.py
--rw-r--r--   0 runner    (1001) docker     (123)     2934 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_account_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    10733 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_all_pb.py
--rw-r--r--   0 runner    (1001) docker     (123)     9309 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_analyst_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     1427 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_average_position_lg.py
--rw-r--r--   0 runner    (1001) docker     (123)    14242 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_board_concept_ths.py
--rw-r--r--   0 runner    (1001) docker     (123)    23657 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_board_industry_ths.py
--rw-r--r--   0 runner    (1001) docker     (123)     1487 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_buffett_index_lg.py
--rw-r--r--   0 runner    (1001) docker     (123)     3210 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_classify_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     4095 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_cls_alerts.py
--rw-r--r--   0 runner    (1001) docker     (123)     2800 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_cninfo_yjyg.py
--rw-r--r--   0 runner    (1001) docker     (123)    12659 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_comment_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     1148 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_congestion_lg.py
--rw-r--r--   0 runner    (1001) docker     (123)    16608 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_dxsyl_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     1563 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_ebs_lg.py
--rw-r--r--   0 runner    (1001) docker     (123)     4171 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_fhps_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    18221 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_fund_flow.py
--rw-r--r--   0 runner    (1001) docker     (123)    36227 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_gdfx_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     8447 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_gdhs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4426 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_gdzjc_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    16520 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_gpzy_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_gxl_lg.py
--rw-r--r--   0 runner    (1001) docker     (123)    63731 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_hist_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     1715 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_hk_valuation_baidu.py
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_hot_tgb.py
--rw-r--r--   0 runner    (1001) docker     (123)     7557 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_hot_xq.py
--rw-r--r--   0 runner    (1001) docker     (123)    66043 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_hsgt_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     6838 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_hsgt_exchange_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_inner_trade_xq.py
--rw-r--r--   0 runner    (1001) docker     (123)     6003 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_jgdy_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2817 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_lh_yybpm.py
--rw-r--r--   0 runner    (1001) docker     (123)    18522 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_lhb_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     8762 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_lhb_sina.py
--rw-r--r--   0 runner    (1001) docker     (123)     1711 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_market_legu.py
--rw-r--r--   0 runner    (1001) docker     (123)     5285 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_pankou_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     3913 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_qsjy_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    12443 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_report_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_sse_margin.py
--rw-r--r--   0 runner    (1001) docker     (123)    17445 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_sy_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     6260 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_szse_margin.py
--rw-r--r--   0 runner    (1001) docker     (123)    29642 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_technology_ths.py
--rw-r--r--   0 runner    (1001) docker     (123)     2016 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_tfp_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    15959 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_three_report_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    10733 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_ttm_lyr.py
--rw-r--r--   0 runner    (1001) docker     (123)     7577 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_us_hist_futunn.py
--rw-r--r--   0 runner    (1001) docker     (123)     3576 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_wencai.py
--rw-r--r--   0 runner    (1001) docker     (123)     4275 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_yjbb_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    11683 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_yjyg_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_yzxdr_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     5818 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_zf_pg.py
--rw-r--r--   0 runner    (1001) docker     (123)     1613 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_zh_valuation_baidu.py
--rw-r--r--   0 runner    (1001) docker     (123)     1761 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_zh_vote_baidu.py
--rw-r--r--   0 runner    (1001) docker     (123)    15358 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/stock_ztb_em.py
--rw-r--r--   0 runner    (1001) docker     (123)    39664 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_feature/ths.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.689692 akshare-1.9.8/akshare/stock_fundamental/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    23011 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_finance.py
--rw-r--r--   0 runner    (1001) docker     (123)     5980 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_finance_hk.py
--rw-r--r--   0 runner    (1001) docker     (123)     4778 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_hold.py
--rw-r--r--   0 runner    (1001) docker     (123)     1809 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_ipo_declare.py
--rw-r--r--   0 runner    (1001) docker     (123)      940 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_kcb_detail_sse.py
--rw-r--r--   0 runner    (1001) docker     (123)     1534 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_kcb_sse.py
--rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_mda_ym.py
--rw-r--r--   0 runner    (1001) docker     (123)     3627 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_notice.py
--rw-r--r--   0 runner    (1001) docker     (123)     5166 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_profit_forecast_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_profit_forecast_ths.py
--rw-r--r--   0 runner    (1001) docker     (123)     4501 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_recommend.py
--rw-r--r--   0 runner    (1001) docker     (123)     9407 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_register.py
--rw-r--r--   0 runner    (1001) docker     (123)    12906 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_restricted_em.py
--rw-r--r--   0 runner    (1001) docker     (123)     4390 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_zygc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1524 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/stock_fundamental/stock_zyjs_ths.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.689692 akshare-1.9.8/akshare/tool/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/tool/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1408 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/tool/trade_date_hist.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.689692 akshare-1.9.8/akshare/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      944 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/utils/ak_session.py
--rw-r--r--   0 runner    (1001) docker     (123)   241609 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/utils/demjson.py
--rw-r--r--   0 runner    (1001) docker     (123)      666 2023-03-09 14:50:00.000000 akshare-1.9.8/akshare/utils/token_process.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.645689 akshare-1.9.8/akshare.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    14801 2023-03-09 14:50:14.000000 akshare-1.9.8/akshare.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    11770 2023-03-09 14:50:14.000000 akshare-1.9.8/akshare.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-09 14:50:14.000000 akshare-1.9.8/akshare.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      286 2023-03-09 14:50:14.000000 akshare-1.9.8/akshare.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-03-09 14:50:14.000000 akshare-1.9.8/akshare.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      189 2023-03-09 14:50:00.000000 akshare-1.9.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-09 14:50:14.689692 akshare-1.9.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2325 2023-03-09 14:50:00.000000 akshare-1.9.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 14:50:14.689692 akshare-1.9.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 14:50:00.000000 akshare-1.9.8/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      941 2023-03-09 14:50:00.000000 akshare-1.9.8/tests/test_func.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.187285 akshare-1.9.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-03-09 15:07:07.000000 akshare-1.9.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    14801 2023-03-09 15:07:22.187285 akshare-1.9.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    13964 2023-03-09 15:07:07.000000 akshare-1.9.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.147284 akshare-1.9.9/akshare/
+-rw-r--r--   0 runner    (1001) docker     (123)   149135 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.151284 akshare-1.9.9/akshare/air/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/air/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4423 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/air/air_hebei.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10809 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/air/air_zhenqi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9771 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/air/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8443 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/air/crypto.js
+-rw-r--r--   0 runner    (1001) docker     (123)   142353 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/air/outcrypto.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4004 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/air/sunrise_tad.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.151284 akshare-1.9.9/akshare/article/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/article/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/article/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1748 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/article/epu_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4106 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/article/ff_factor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/article/fred_md.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13162 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/article/risk_rv.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.151284 akshare-1.9.9/akshare/bank/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bank/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6196 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bank/bank_cbirc_2020.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bank/cons.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.151284 akshare-1.9.9/akshare/bond/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2929 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_bank.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6301 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_cbond.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4537 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_china_money.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10777 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4343 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2326 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_futures.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7517 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_info_cm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4990 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_investing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21295 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_issue_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3581 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_summary.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23003 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_zh_cov_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4098 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/bond_zh_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6550 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/china_bond.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1432 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/china_repo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1792 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/bond/cons.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.151284 akshare-1.9.9/akshare/cost/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/cost/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2005 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/cost/cost_living.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.151284 akshare-1.9.9/akshare/crypto/
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/crypto/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1885 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/crypto/crypto_bitcoin_cme.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/crypto/crypto_crix.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9748 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/crypto/crypto_hist_investing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3890 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/crypto/crypto_hold.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.151284 akshare-1.9.9/akshare/currency/
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/currency/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5419 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/currency/currency.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3641 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/currency/currency_china_bank_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/currency/currency_safe.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.155284 akshare-1.9.9/akshare/data/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   209327 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/data/covid.js
+-rw-r--r--   0 runner    (1001) docker     (123)   122225 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/data/crypto_info.zip
+-rw-r--r--   0 runner    (1001) docker     (123)    39664 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/data/ths.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1631 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/datasets.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.155284 akshare-1.9.9/akshare/economic/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16594 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10801 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_australia.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31987 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_bank.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15195 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_canada.py
+-rw-r--r--   0 runner    (1001) docker     (123)   181223 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_china.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11765 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_china_hk.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8083 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_constitute.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40919 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_euro.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5912 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_germany.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_japan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6954 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_other.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4403 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_swiss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8469 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_uk.py
+-rw-r--r--   0 runner    (1001) docker     (123)   121523 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/macro_usa.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/economic/marco_cnbs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.155284 akshare-1.9.9/akshare/energy/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/energy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11913 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/energy/energy_carbon.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3775 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/energy/energy_oil_em.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.155284 akshare-1.9.9/akshare/event/
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/event/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12807 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/event/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38159 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/event/covid.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.155284 akshare-1.9.9/akshare/file_fold/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/file_fold/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   112983 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/file_fold/calendar.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.155284 akshare-1.9.9/akshare/fortune/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fortune/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4117 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fortune/fortune_500.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3673 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fortune/fortune_bloomberg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1437 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fortune/fortune_forbes_500.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11776 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fortune/fortune_hurun.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3257 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fortune/fortune_it_juzi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1827 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fortune/fortune_xincaifu_500.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.159284 akshare-1.9.9/akshare/fund/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31404 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_amac.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3186 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_aum_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40110 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11943 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_etf_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4917 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_etf_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5546 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_fhsp_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2141 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_init_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10413 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_portfolio_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3235 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_position_lg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12325 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_rank_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8886 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_rating.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9254 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_report_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4010 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_scale_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8092 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fund/fund_scale_sina.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.163284 akshare-1.9.9/akshare/futures/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16982 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    48820 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/cot.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13386 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_basis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_comex.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_comm_qihuo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1135 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_contract_detail.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26034 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_daily_bar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_foreign.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8418 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_hq_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4479 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_index_ccidx.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6946 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_international.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8410 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_inventory_99.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2340 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_inventory_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1531 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_news_baidu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2462 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_news_shmet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6272 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_roll_yield.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1471 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_rule.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2238 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_sgx_daily.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3297 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_spot_stock_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10509 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_to_spot.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6388 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_warehouse_receipt.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23910 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/futures_zh_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4097 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/inventory_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19049 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/receipt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2770 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/requests_fun.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5148 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures/symbol_var.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.163284 akshare-1.9.9/akshare/futures_derivative/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5927 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4819 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/futures_egg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14308 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/futures_hog.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2052 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/futures_index_price_nh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1563 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/futures_index_return_nh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1561 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/futures_index_volatility_nh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4255 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/futures_other_index_nh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1386 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/futures_sina_cot.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5439 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/sina_futures_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3537 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/futures_derivative/sys_spot_futures.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.163284 akshare-1.9.9/akshare/fx/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fx/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      585 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fx/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12574 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fx/currency_investing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3427 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fx/fx_quote.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2314 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/fx/fx_quote_baidu.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.163284 akshare-1.9.9/akshare/hf/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/hf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1206 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/hf/hf_sp500.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.167284 akshare-1.9.9/akshare/index/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3551 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5432 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/dailydata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2986 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/drewry_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    53902 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_baidu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4263 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_cflp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7478 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_cni.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8742 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11943 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_cx.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1768 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_eri.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1636 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_google.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_hog.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12177 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_investing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_kq_fz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3294 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_kq_ss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1680 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_spot.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9688 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_stock_zh.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4566 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_sugar.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29465 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_sw.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16818 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_sw_research.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2261 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_weibo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3411 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_yw.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15811 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/index_zh_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23023 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7971 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/index/stock_zh_index_csindex.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.167284 akshare-1.9.9/akshare/interest_rate/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/interest_rate/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4385 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/interest_rate/interbank_rate_em.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.167284 akshare-1.9.9/akshare/movie/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/movie/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3710 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/movie/artist_yien.py
+-rw-r--r--   0 runner    (1001) docker     (123)   117172 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/movie/jm.js
+-rw-r--r--   0 runner    (1001) docker     (123)    12312 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/movie/movie_yien.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3404 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/movie/video_yien.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.167284 akshare-1.9.9/akshare/news/
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/news/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7642 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/news/news_baidu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7387 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/news/news_cctv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2874 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/news/news_stock.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.167284 akshare-1.9.9/akshare/nlp/
+-rw-r--r--   0 runner    (1001) docker     (123)       79 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/nlp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1858 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/nlp/nlp_interface.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/option/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4352 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13817 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_commodity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7776 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_commodity_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1812 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_czce.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3031 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8548 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_finance.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34775 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_finance_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8417 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_lhb_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_premium_analysis_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_qvix.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2505 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_risk_analysis_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2444 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_risk_indicator_sse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2487 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/option/option_value_analysis_em.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/other/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/other/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4301 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/other/other_car.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5661 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/other/other_game.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/pro/
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/pro/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2248 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/pro/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      244 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/pro/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)      830 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/pro/data_pro.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/qhkc/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/qhkc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8235 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/qhkc/qhkc_api.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/qhkc_web/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/qhkc_web/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17400 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/qhkc_web/qhkc_fund.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9109 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/qhkc_web/qhkc_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9083 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/qhkc_web/qhkc_tool.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/rate/
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/rate/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2018 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/rate/repo_rate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/reits/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/reits/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4137 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/reits/reits_basic.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/sport/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/sport/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      818 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/sport/sport_olympic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1473 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/sport/sport_olympic_winter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.171284 akshare-1.9.9/akshare/spot/
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/spot/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6899 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/spot/spot_sge.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.175284 akshare-1.9.9/akshare/stock/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35986 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6946 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_allotment_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12289 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_board_concept_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12597 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_board_industry_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4202 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_cg_equity_mortgage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4637 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_cg_guarantee.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4212 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_cg_lawsuit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3983 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_dividents_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20519 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_dzjy_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22924 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_fund.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6056 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_fund_hold.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4114 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_hist_163.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8298 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_hk_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7821 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_hold_control_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4434 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_hold_num_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7130 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_hot_rank_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_hot_search_baidu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5568 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_industry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7321 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_industry_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5068 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_industry_pe_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15590 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2414 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_info_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6290 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_new_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4070 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_profile_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4022 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_rank_forecast.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5000 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_repurchase_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5653 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_share_changes_cninfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1185 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_stop.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16473 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_summary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3585 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_us_famous.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2502 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_us_js.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3047 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_us_pink.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9816 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_us_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5046 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_us_zh_hx.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_weibo_nlp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17824 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_zh_a_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10290 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_zh_a_special.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6660 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_zh_a_tick_tx_163.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8923 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_zh_ah_tx.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16109 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_zh_b_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2879 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_zh_kcb_report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9033 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock/stock_zh_kcb_sina.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.183284 akshare-1.9.9/akshare/stock_feature/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/cons.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2042 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_a_below_net_asset_statistics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1872 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_a_high_low.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3953 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_a_indicator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12741 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_a_pb.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13917 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_a_pe.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17360 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_a_pe_and_pb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2934 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_account_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10733 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_all_pb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9309 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_analyst_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1427 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_average_position_lg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14242 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_board_concept_ths.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23657 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_board_industry_ths.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1487 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_buffett_index_lg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3210 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_classify_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4095 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_cls_alerts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2800 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_cninfo_yjyg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12659 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_comment_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1148 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_congestion_lg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16608 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_dxsyl_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1563 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_ebs_lg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4171 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_fhps_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18221 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_fund_flow.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36227 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_gdfx_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8447 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_gdhs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4426 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_gdzjc_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16520 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_gpzy_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_gxl_lg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63731 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_hist_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1715 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_hk_valuation_baidu.py
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_hot_tgb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7557 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_hot_xq.py
+-rw-r--r--   0 runner    (1001) docker     (123)    66043 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_hsgt_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6838 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_hsgt_exchange_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2490 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_inner_trade_xq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6003 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_jgdy_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2817 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_lh_yybpm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18522 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_lhb_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8762 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_lhb_sina.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1711 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_market_legu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5285 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_pankou_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3913 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_qsjy_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12443 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_report_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4099 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_sse_margin.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17445 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_sy_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6260 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_szse_margin.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29642 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_technology_ths.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2016 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_tfp_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15959 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_three_report_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10733 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_ttm_lyr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7577 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_us_hist_futunn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3576 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_wencai.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4275 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_yjbb_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11683 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_yjyg_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_yzxdr_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5818 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_zf_pg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1613 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_zh_valuation_baidu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1761 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_zh_vote_baidu.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15358 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/stock_ztb_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39664 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_feature/ths.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.187285 akshare-1.9.9/akshare/stock_fundamental/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23011 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_finance.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5980 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_finance_hk.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4778 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_hold.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1809 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_ipo_declare.py
+-rw-r--r--   0 runner    (1001) docker     (123)      940 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_kcb_detail_sse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1534 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_kcb_sse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_mda_ym.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3627 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_notice.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5166 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_profit_forecast_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2716 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_profit_forecast_ths.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4501 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_recommend.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9407 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_register.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12906 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_restricted_em.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4390 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_zygc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1524 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/stock_fundamental/stock_zyjs_ths.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.187285 akshare-1.9.9/akshare/tool/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/tool/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1408 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/tool/trade_date_hist.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.187285 akshare-1.9.9/akshare/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      944 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/utils/ak_session.py
+-rw-r--r--   0 runner    (1001) docker     (123)   241609 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/utils/demjson.py
+-rw-r--r--   0 runner    (1001) docker     (123)      666 2023-03-09 15:07:07.000000 akshare-1.9.9/akshare/utils/token_process.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.147284 akshare-1.9.9/akshare.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    14801 2023-03-09 15:07:22.000000 akshare-1.9.9/akshare.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    11770 2023-03-09 15:07:22.000000 akshare-1.9.9/akshare.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-09 15:07:22.000000 akshare-1.9.9/akshare.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      286 2023-03-09 15:07:22.000000 akshare-1.9.9/akshare.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-03-09 15:07:22.000000 akshare-1.9.9/akshare.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      189 2023-03-09 15:07:07.000000 akshare-1.9.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-09 15:07:22.187285 akshare-1.9.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2325 2023-03-09 15:07:07.000000 akshare-1.9.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:07:22.187285 akshare-1.9.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-09 15:07:07.000000 akshare-1.9.9/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      941 2023-03-09 15:07:07.000000 akshare-1.9.9/tests/test_func.py
```

### Comparing `akshare-1.9.8/LICENSE` & `akshare-1.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/PKG-INFO` & `akshare-1.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: akshare
-Version: 1.9.8
+Version: 1.9.9
 Summary: AKShare is an elegant and simple financial data interface library for Python, built for human beings!
 Home-page: https://github.com/akfamily/akshare
 Author: AKFamily
 Author-email: akfamily.akshare@gmail.com
 License: MIT
 Keywords: stock,option,futures,fund,bond,index,air,finance,spider,quant,quantitative,investment,trading,algotrading,data
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `akshare-1.9.8/README.md` & `akshare-1.9.9/README.md`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/__init__.py` & `akshare-1.9.9/akshare/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -2320,17 +2320,18 @@
 1.9.2 fix: fix stock_xgsglb_em interface
 1.9.3 fix: fix fx_quote_baidu interface
 1.9.4 fix: fix drewry_wci_index interface
 1.9.5 fix: fix stock_info_a_code_name interface
 1.9.6 fix: fix futures_hog_info interface
 1.9.7 add: add stock_profit_forecast_ths interface
 1.9.8 fix: fix stock_hk_valuation_baidu interface
+1.9.9 add: add macro_shipping_bci interface
 """
 
-__version__ = "1.9.8"
+__version__ = "1.9.9"
 __author__ = "AKFamily"
 
 import sys
 import warnings
 
 if sys.version_info < (3, 8):
     warnings.warn("为了支持更多 AKShare 特性，请尽快升级 Python 到 3.8 以上版本")
@@ -4484,14 +4485,18 @@
     macro_china_supply_of_money,
     macro_china_swap_rate,
     macro_china_foreign_exchange_gold,
     macro_china_retail_price_index,
     macro_china_real_estate,
     macro_china_qyspjg,
     macro_china_fdi,
+    macro_shipping_bci,
+    macro_shipping_bcti,
+    macro_shipping_bdi,
+    macro_shipping_bpi,
 )
 
 """
 全球期货
 """
 from akshare.futures.futures_international import (
     futures_global_commodity_hist,
```

### Comparing `akshare-1.9.8/akshare/air/air_hebei.py` & `akshare-1.9.9/akshare/air/air_hebei.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/air/air_zhenqi.py` & `akshare-1.9.9/akshare/air/air_zhenqi.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/air/cons.py` & `akshare-1.9.9/akshare/air/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/air/crypto.js` & `akshare-1.9.9/akshare/air/crypto.js`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/air/outcrypto.js` & `akshare-1.9.9/akshare/air/outcrypto.js`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/air/sunrise_tad.py` & `akshare-1.9.9/akshare/air/sunrise_tad.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/article/epu_index.py` & `akshare-1.9.9/akshare/article/epu_index.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/article/ff_factor.py` & `akshare-1.9.9/akshare/article/ff_factor.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/article/fred_md.py` & `akshare-1.9.9/akshare/article/fred_md.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/article/risk_rv.py` & `akshare-1.9.9/akshare/article/risk_rv.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bank/bank_cbirc_2020.py` & `akshare-1.9.9/akshare/bank/bank_cbirc_2020.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bank/cons.py` & `akshare-1.9.9/akshare/bank/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_bank.py` & `akshare-1.9.9/akshare/bond/bond_bank.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_cbond.py` & `akshare-1.9.9/akshare/bond/bond_cbond.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_china_money.py` & `akshare-1.9.9/akshare/bond/bond_china_money.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_convert.py` & `akshare-1.9.9/akshare/bond/bond_convert.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_em.py` & `akshare-1.9.9/akshare/bond/bond_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_futures.py` & `akshare-1.9.9/akshare/bond/bond_futures.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_info_cm.py` & `akshare-1.9.9/akshare/bond/bond_info_cm.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_investing.py` & `akshare-1.9.9/akshare/bond/bond_investing.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_issue_cninfo.py` & `akshare-1.9.9/akshare/bond/bond_issue_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_summary.py` & `akshare-1.9.9/akshare/bond/bond_summary.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_zh_cov_sina.py` & `akshare-1.9.9/akshare/bond/bond_zh_cov_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/bond_zh_sina.py` & `akshare-1.9.9/akshare/bond/bond_zh_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/china_bond.py` & `akshare-1.9.9/akshare/bond/china_bond.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/china_repo.py` & `akshare-1.9.9/akshare/bond/china_repo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/bond/cons.py` & `akshare-1.9.9/akshare/bond/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/cost/cost_living.py` & `akshare-1.9.9/akshare/cost/cost_living.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/crypto/crypto_bitcoin_cme.py` & `akshare-1.9.9/akshare/crypto/crypto_bitcoin_cme.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/crypto/crypto_crix.py` & `akshare-1.9.9/akshare/crypto/crypto_crix.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/crypto/crypto_hist_investing.py` & `akshare-1.9.9/akshare/crypto/crypto_hist_investing.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/crypto/crypto_hold.py` & `akshare-1.9.9/akshare/crypto/crypto_hold.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/currency/currency.py` & `akshare-1.9.9/akshare/currency/currency.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/currency/currency_china_bank_sina.py` & `akshare-1.9.9/akshare/currency/currency_china_bank_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/currency/currency_safe.py` & `akshare-1.9.9/akshare/currency/currency_safe.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/data/covid.js` & `akshare-1.9.9/akshare/data/covid.js`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/data/crypto_info.zip` & `akshare-1.9.9/akshare/data/crypto_info.zip`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/data/ths.js` & `akshare-1.9.9/akshare/data/ths.js`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/datasets.py` & `akshare-1.9.9/akshare/datasets.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/cons.py` & `akshare-1.9.9/akshare/economic/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_australia.py` & `akshare-1.9.9/akshare/economic/macro_australia.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_bank.py` & `akshare-1.9.9/akshare/economic/macro_bank.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_canada.py` & `akshare-1.9.9/akshare/economic/macro_canada.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_china.py` & `akshare-1.9.9/akshare/economic/macro_china.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 """
-Date: 2022/11/27 12:20
+Date: 2023/3/9 22:20
 Desc: 宏观数据-中国
 """
 import json
 import math
 import time
 
 import pandas as pd
@@ -2486,14 +2486,109 @@
     big_df["近2年涨跌幅"] = pd.to_numeric(big_df["近2年涨跌幅"])
     big_df["近3年涨跌幅"] = pd.to_numeric(big_df["近3年涨跌幅"])
     big_df.sort_values(["日期"], inplace=True)
     big_df.reset_index(inplace=True, drop=True)
     return big_df
 
 
+def _em_macro_1(em_id) -> pd.DataFrame:
+    """
+    获取东财宏观数据的一种通用函数1
+    """
+    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
+    ind_id = '"' + em_id + '"'
+    params = {
+        "sortColumns": "REPORT_DATE",
+        "sortTypes": "-1",
+        "pageSize": "500",
+        "pageNumber": "1",
+        "reportName": "RPT_INDUSTRY_INDEX",
+        "columns": "REPORT_DATE,INDICATOR_VALUE,CHANGE_RATE,CHANGERATE_3M,CHANGERATE_6M,CHANGERATE_1Y,CHANGERATE_2Y,CHANGERATE_3Y",
+        "filter": '(INDICATOR_ID=' + ind_id + ')',
+        "source": "WEB",
+        "client": "WEB",
+    }
+    r = requests.get(url, params=params)
+    data_json = r.json()
+    total_page = data_json["result"]["pages"]
+    big_df = pd.DataFrame()
+    for page in tqdm(range(1, total_page + 1), leave=False):
+        params.update({"pageNumber": page})
+        r = requests.get(url, params=params)
+        data_json = r.json()
+        temp_df = pd.DataFrame(data_json["result"]["data"])
+        big_df = pd.concat([big_df, temp_df], ignore_index=True)
+    big_df.drop_duplicates(inplace=True)
+    big_df.columns = [
+        "日期",
+        "最新值",
+        "涨跌幅",
+        "近3月涨跌幅",
+        "近6月涨跌幅",
+        "近1年涨跌幅",
+        "近2年涨跌幅",
+        "近3年涨跌幅",
+    ]
+    big_df["日期"] = pd.to_datetime(big_df["日期"]).dt.date
+    big_df["最新值"] = pd.to_numeric(big_df["最新值"])
+    big_df["涨跌幅"] = pd.to_numeric(big_df["涨跌幅"])
+    big_df["近3月涨跌幅"] = pd.to_numeric(big_df["近3月涨跌幅"])
+    big_df["近6月涨跌幅"] = pd.to_numeric(big_df["近6月涨跌幅"])
+    big_df["近1年涨跌幅"] = pd.to_numeric(big_df["近1年涨跌幅"])
+    big_df["近2年涨跌幅"] = pd.to_numeric(big_df["近2年涨跌幅"])
+    big_df["近3年涨跌幅"] = pd.to_numeric(big_df["近3年涨跌幅"])
+    big_df.sort_values(["日期"], inplace=True)
+    big_df.reset_index(inplace=True, drop=True)
+    return big_df
+
+
+def macro_shipping_bci() -> pd.DataFrame:
+    """
+    海岬型运费指数（BCI）
+    https://data.eastmoney.com/cjsj/hyzs_list_EMI00107666.html
+    :return: 海岬型运费指数
+    :rtype: pandas.DataFrame
+    """
+    ts = _em_macro_1("EMI00107666")
+    return ts
+
+
+def macro_shipping_bdi() -> pd.DataFrame:
+    """
+    波罗的海干散货指数(BDI)
+    https://data.eastmoney.com/cjsj/hyzs_list_EMI00107664.html
+    :return: 波罗的海干散货指数
+    :rtype: pandas.DataFrame
+    """
+    ts = _em_macro_1("EMI00107664")
+    return ts
+
+
+def macro_shipping_bpi() -> pd.DataFrame:
+    """
+    巴拿马型运费指数(BPI)
+    https://data.eastmoney.com/cjsj/hyzs_list_EMI00107665.html
+    :return: 巴拿马型运费指数
+    :rtype: pandas.DataFrame
+    """
+    ts = _em_macro_1("EMI00107665")
+    return ts
+
+
+def macro_shipping_bcti() -> pd.DataFrame:
+    """
+    成品油运输指数（BCTI）
+    https://data.eastmoney.com/cjsj/hyzs_list_EMI00107669.html
+    :return: 成品油运输指数
+    :rtype: pandas.DataFrame
+    """
+    ts = _em_macro_1("EMI00107669")
+    return ts
+
+
 def macro_china_new_financial_credit() -> pd.DataFrame:
     """
     中国-新增信贷数据
     https://data.eastmoney.com/cjsj/xzxd.html
     :return: 新增信贷数据
     :rtype: pandas.DataFrame
     """
@@ -4407,7 +4502,19 @@
     print(macro_china_foreign_exchange_gold_df)
 
     macro_china_retail_price_index_df = macro_china_retail_price_index()
     print(macro_china_retail_price_index_df)
 
     macro_china_real_estate_df = macro_china_real_estate()
     print(macro_china_real_estate_df)
+
+    macro_shipping_bci_df = macro_shipping_bci()
+    print(macro_shipping_bci_df)
+
+    macro_shipping_bdi_df = macro_shipping_bdi()
+    print(macro_shipping_bdi_df)
+
+    macro_shipping_bpi_df = macro_shipping_bpi()
+    print(macro_shipping_bpi_df)
+
+    macro_shipping_bcti_df = macro_shipping_bcti()
+    print(macro_shipping_bcti_df)
```

### Comparing `akshare-1.9.8/akshare/economic/macro_china_hk.py` & `akshare-1.9.9/akshare/economic/macro_china_hk.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_constitute.py` & `akshare-1.9.9/akshare/economic/macro_constitute.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_euro.py` & `akshare-1.9.9/akshare/economic/macro_euro.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_germany.py` & `akshare-1.9.9/akshare/economic/macro_germany.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_japan.py` & `akshare-1.9.9/akshare/economic/macro_japan.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_other.py` & `akshare-1.9.9/akshare/economic/macro_other.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_swiss.py` & `akshare-1.9.9/akshare/economic/macro_swiss.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_uk.py` & `akshare-1.9.9/akshare/economic/macro_uk.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/macro_usa.py` & `akshare-1.9.9/akshare/economic/macro_usa.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/economic/marco_cnbs.py` & `akshare-1.9.9/akshare/economic/marco_cnbs.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/energy/energy_carbon.py` & `akshare-1.9.9/akshare/energy/energy_carbon.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/energy/energy_oil_em.py` & `akshare-1.9.9/akshare/energy/energy_oil_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/event/cons.py` & `akshare-1.9.9/akshare/event/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/event/covid.py` & `akshare-1.9.9/akshare/event/covid.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/file_fold/calendar.json` & `akshare-1.9.9/akshare/file_fold/calendar.json`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fortune/fortune_500.py` & `akshare-1.9.9/akshare/fortune/fortune_500.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fortune/fortune_bloomberg.py` & `akshare-1.9.9/akshare/fortune/fortune_bloomberg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fortune/fortune_forbes_500.py` & `akshare-1.9.9/akshare/fortune/fortune_forbes_500.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fortune/fortune_hurun.py` & `akshare-1.9.9/akshare/fortune/fortune_hurun.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fortune/fortune_it_juzi.py` & `akshare-1.9.9/akshare/fortune/fortune_it_juzi.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fortune/fortune_xincaifu_500.py` & `akshare-1.9.9/akshare/fortune/fortune_xincaifu_500.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_amac.py` & `akshare-1.9.9/akshare/fund/fund_amac.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_aum_em.py` & `akshare-1.9.9/akshare/fund/fund_aum_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_em.py` & `akshare-1.9.9/akshare/fund/fund_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_etf_em.py` & `akshare-1.9.9/akshare/fund/fund_etf_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_etf_sina.py` & `akshare-1.9.9/akshare/fund/fund_etf_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_fhsp_em.py` & `akshare-1.9.9/akshare/fund/fund_fhsp_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_init_em.py` & `akshare-1.9.9/akshare/fund/fund_init_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_manager.py` & `akshare-1.9.9/akshare/fund/fund_manager.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_portfolio_em.py` & `akshare-1.9.9/akshare/fund/fund_portfolio_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_position_lg.py` & `akshare-1.9.9/akshare/fund/fund_position_lg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_rank_em.py` & `akshare-1.9.9/akshare/fund/fund_rank_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_rating.py` & `akshare-1.9.9/akshare/fund/fund_rating.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_report_cninfo.py` & `akshare-1.9.9/akshare/fund/fund_report_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_scale_em.py` & `akshare-1.9.9/akshare/fund/fund_scale_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fund/fund_scale_sina.py` & `akshare-1.9.9/akshare/fund/fund_scale_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/cons.py` & `akshare-1.9.9/akshare/futures/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/cot.py` & `akshare-1.9.9/akshare/futures/cot.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_basis.py` & `akshare-1.9.9/akshare/futures/futures_basis.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_comex.py` & `akshare-1.9.9/akshare/futures/futures_comex.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_comm_qihuo.py` & `akshare-1.9.9/akshare/futures/futures_comm_qihuo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_contract_detail.py` & `akshare-1.9.9/akshare/futures/futures_contract_detail.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_daily_bar.py` & `akshare-1.9.9/akshare/futures/futures_daily_bar.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_foreign.py` & `akshare-1.9.9/akshare/futures/futures_foreign.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_hq_sina.py` & `akshare-1.9.9/akshare/futures/futures_hq_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_index_ccidx.py` & `akshare-1.9.9/akshare/futures/futures_index_ccidx.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_international.py` & `akshare-1.9.9/akshare/futures/futures_international.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_inventory_99.py` & `akshare-1.9.9/akshare/futures/futures_inventory_99.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_inventory_em.py` & `akshare-1.9.9/akshare/futures/futures_inventory_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_news_baidu.py` & `akshare-1.9.9/akshare/futures/futures_news_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_news_shmet.py` & `akshare-1.9.9/akshare/futures/futures_news_shmet.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_roll_yield.py` & `akshare-1.9.9/akshare/futures/futures_roll_yield.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_rule.py` & `akshare-1.9.9/akshare/futures/futures_rule.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_sgx_daily.py` & `akshare-1.9.9/akshare/futures/futures_sgx_daily.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_spot_stock_em.py` & `akshare-1.9.9/akshare/futures/futures_spot_stock_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_to_spot.py` & `akshare-1.9.9/akshare/futures/futures_to_spot.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_warehouse_receipt.py` & `akshare-1.9.9/akshare/futures/futures_warehouse_receipt.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/futures_zh_sina.py` & `akshare-1.9.9/akshare/futures/futures_zh_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/inventory_data.py` & `akshare-1.9.9/akshare/futures/inventory_data.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/receipt.py` & `akshare-1.9.9/akshare/futures/receipt.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/requests_fun.py` & `akshare-1.9.9/akshare/futures/requests_fun.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures/symbol_var.py` & `akshare-1.9.9/akshare/futures/symbol_var.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/cons.py` & `akshare-1.9.9/akshare/futures_derivative/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/futures_egg.py` & `akshare-1.9.9/akshare/futures_derivative/futures_egg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/futures_hog.py` & `akshare-1.9.9/akshare/futures_derivative/futures_hog.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/futures_index_price_nh.py` & `akshare-1.9.9/akshare/futures_derivative/futures_index_price_nh.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/futures_index_return_nh.py` & `akshare-1.9.9/akshare/futures_derivative/futures_index_return_nh.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/futures_index_volatility_nh.py` & `akshare-1.9.9/akshare/futures_derivative/futures_index_volatility_nh.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/futures_other_index_nh.py` & `akshare-1.9.9/akshare/futures_derivative/futures_other_index_nh.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/futures_sina_cot.py` & `akshare-1.9.9/akshare/futures_derivative/futures_sina_cot.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/sina_futures_index.py` & `akshare-1.9.9/akshare/futures_derivative/sina_futures_index.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/futures_derivative/sys_spot_futures.py` & `akshare-1.9.9/akshare/futures_derivative/sys_spot_futures.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fx/cons.py` & `akshare-1.9.9/akshare/fx/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fx/currency_investing.py` & `akshare-1.9.9/akshare/fx/currency_investing.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fx/fx_quote.py` & `akshare-1.9.9/akshare/fx/fx_quote.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/fx/fx_quote_baidu.py` & `akshare-1.9.9/akshare/fx/fx_quote_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/hf/hf_sp500.py` & `akshare-1.9.9/akshare/hf/hf_sp500.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/cons.py` & `akshare-1.9.9/akshare/index/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/dailydata.py` & `akshare-1.9.9/akshare/index/dailydata.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/drewry_index.py` & `akshare-1.9.9/akshare/index/drewry_index.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_baidu.py` & `akshare-1.9.9/akshare/index/index_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_cflp.py` & `akshare-1.9.9/akshare/index/index_cflp.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_cni.py` & `akshare-1.9.9/akshare/index/index_cni.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_cons.py` & `akshare-1.9.9/akshare/index/index_cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_cx.py` & `akshare-1.9.9/akshare/index/index_cx.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_eri.py` & `akshare-1.9.9/akshare/index/index_eri.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_google.py` & `akshare-1.9.9/akshare/index/index_google.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_hog.py` & `akshare-1.9.9/akshare/index/index_hog.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_investing.py` & `akshare-1.9.9/akshare/index/index_investing.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_kq_fz.py` & `akshare-1.9.9/akshare/index/index_kq_fz.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_kq_ss.py` & `akshare-1.9.9/akshare/index/index_kq_ss.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_spot.py` & `akshare-1.9.9/akshare/index/index_spot.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_stock_zh.py` & `akshare-1.9.9/akshare/index/index_stock_zh.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_sugar.py` & `akshare-1.9.9/akshare/index/index_sugar.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_sw.py` & `akshare-1.9.9/akshare/index/index_sw.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_sw_research.py` & `akshare-1.9.9/akshare/index/index_sw_research.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_weibo.py` & `akshare-1.9.9/akshare/index/index_weibo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_yw.py` & `akshare-1.9.9/akshare/index/index_yw.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/index_zh_em.py` & `akshare-1.9.9/akshare/index/index_zh_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/request.py` & `akshare-1.9.9/akshare/index/request.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/index/stock_zh_index_csindex.py` & `akshare-1.9.9/akshare/index/stock_zh_index_csindex.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/interest_rate/interbank_rate_em.py` & `akshare-1.9.9/akshare/interest_rate/interbank_rate_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/movie/artist_yien.py` & `akshare-1.9.9/akshare/movie/artist_yien.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/movie/jm.js` & `akshare-1.9.9/akshare/movie/jm.js`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/movie/movie_yien.py` & `akshare-1.9.9/akshare/movie/movie_yien.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/movie/video_yien.py` & `akshare-1.9.9/akshare/movie/video_yien.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/news/news_baidu.py` & `akshare-1.9.9/akshare/news/news_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/news/news_cctv.py` & `akshare-1.9.9/akshare/news/news_cctv.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/news/news_stock.py` & `akshare-1.9.9/akshare/news/news_stock.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/nlp/nlp_interface.py` & `akshare-1.9.9/akshare/nlp/nlp_interface.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/cons.py` & `akshare-1.9.9/akshare/option/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_commodity.py` & `akshare-1.9.9/akshare/option/option_commodity.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_commodity_sina.py` & `akshare-1.9.9/akshare/option/option_commodity_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_czce.py` & `akshare-1.9.9/akshare/option/option_czce.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_em.py` & `akshare-1.9.9/akshare/option/option_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_finance.py` & `akshare-1.9.9/akshare/option/option_finance.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_finance_sina.py` & `akshare-1.9.9/akshare/option/option_finance_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_lhb_em.py` & `akshare-1.9.9/akshare/option/option_lhb_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_premium_analysis_em.py` & `akshare-1.9.9/akshare/option/option_premium_analysis_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_qvix.py` & `akshare-1.9.9/akshare/option/option_qvix.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_risk_analysis_em.py` & `akshare-1.9.9/akshare/option/option_risk_analysis_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_risk_indicator_sse.py` & `akshare-1.9.9/akshare/option/option_risk_indicator_sse.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/option/option_value_analysis_em.py` & `akshare-1.9.9/akshare/option/option_value_analysis_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/other/other_car.py` & `akshare-1.9.9/akshare/other/other_car.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/other/other_game.py` & `akshare-1.9.9/akshare/other/other_game.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/pro/client.py` & `akshare-1.9.9/akshare/pro/client.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/pro/data_pro.py` & `akshare-1.9.9/akshare/pro/data_pro.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/qhkc/qhkc_api.py` & `akshare-1.9.9/akshare/qhkc/qhkc_api.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/qhkc_web/qhkc_fund.py` & `akshare-1.9.9/akshare/qhkc_web/qhkc_fund.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/qhkc_web/qhkc_index.py` & `akshare-1.9.9/akshare/qhkc_web/qhkc_index.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/qhkc_web/qhkc_tool.py` & `akshare-1.9.9/akshare/qhkc_web/qhkc_tool.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/rate/repo_rate.py` & `akshare-1.9.9/akshare/rate/repo_rate.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/reits/reits_basic.py` & `akshare-1.9.9/akshare/reits/reits_basic.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/sport/sport_olympic.py` & `akshare-1.9.9/akshare/sport/sport_olympic.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/sport/sport_olympic_winter.py` & `akshare-1.9.9/akshare/sport/sport_olympic_winter.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/spot/spot_sge.py` & `akshare-1.9.9/akshare/spot/spot_sge.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/cons.py` & `akshare-1.9.9/akshare/stock/cons.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_allotment_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_allotment_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_board_concept_em.py` & `akshare-1.9.9/akshare/stock/stock_board_concept_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_board_industry_em.py` & `akshare-1.9.9/akshare/stock/stock_board_industry_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_cg_equity_mortgage.py` & `akshare-1.9.9/akshare/stock/stock_cg_equity_mortgage.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_cg_guarantee.py` & `akshare-1.9.9/akshare/stock/stock_cg_guarantee.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_cg_lawsuit.py` & `akshare-1.9.9/akshare/stock/stock_cg_lawsuit.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_dividents_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_dividents_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_dzjy_em.py` & `akshare-1.9.9/akshare/stock/stock_dzjy_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_fund.py` & `akshare-1.9.9/akshare/stock/stock_fund.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_fund_hold.py` & `akshare-1.9.9/akshare/stock/stock_fund_hold.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_hist_163.py` & `akshare-1.9.9/akshare/stock/stock_hist_163.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_hk_sina.py` & `akshare-1.9.9/akshare/stock/stock_hk_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_hold_control_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_hold_control_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_hold_num_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_hold_num_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_hot_rank_em.py` & `akshare-1.9.9/akshare/stock/stock_hot_rank_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_hot_search_baidu.py` & `akshare-1.9.9/akshare/stock/stock_hot_search_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_industry.py` & `akshare-1.9.9/akshare/stock/stock_industry.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_industry_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_industry_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_industry_pe_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_industry_pe_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_info.py` & `akshare-1.9.9/akshare/stock/stock_info.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_info_em.py` & `akshare-1.9.9/akshare/stock/stock_info_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_new_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_new_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_profile_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_profile_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_rank_forecast.py` & `akshare-1.9.9/akshare/stock/stock_rank_forecast.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_repurchase_em.py` & `akshare-1.9.9/akshare/stock/stock_repurchase_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_share_changes_cninfo.py` & `akshare-1.9.9/akshare/stock/stock_share_changes_cninfo.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_stop.py` & `akshare-1.9.9/akshare/stock/stock_stop.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_summary.py` & `akshare-1.9.9/akshare/stock/stock_summary.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_us_famous.py` & `akshare-1.9.9/akshare/stock/stock_us_famous.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_us_js.py` & `akshare-1.9.9/akshare/stock/stock_us_js.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_us_pink.py` & `akshare-1.9.9/akshare/stock/stock_us_pink.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_us_sina.py` & `akshare-1.9.9/akshare/stock/stock_us_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_us_zh_hx.py` & `akshare-1.9.9/akshare/stock/stock_us_zh_hx.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_weibo_nlp.py` & `akshare-1.9.9/akshare/stock/stock_weibo_nlp.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_zh_a_sina.py` & `akshare-1.9.9/akshare/stock/stock_zh_a_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_zh_a_special.py` & `akshare-1.9.9/akshare/stock/stock_zh_a_special.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_zh_a_tick_tx_163.py` & `akshare-1.9.9/akshare/stock/stock_zh_a_tick_tx_163.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_zh_ah_tx.py` & `akshare-1.9.9/akshare/stock/stock_zh_ah_tx.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_zh_b_sina.py` & `akshare-1.9.9/akshare/stock/stock_zh_b_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_zh_kcb_report.py` & `akshare-1.9.9/akshare/stock/stock_zh_kcb_report.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock/stock_zh_kcb_sina.py` & `akshare-1.9.9/akshare/stock/stock_zh_kcb_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_a_below_net_asset_statistics.py` & `akshare-1.9.9/akshare/stock_feature/stock_a_below_net_asset_statistics.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_a_high_low.py` & `akshare-1.9.9/akshare/stock_feature/stock_a_high_low.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_a_indicator.py` & `akshare-1.9.9/akshare/stock_feature/stock_a_indicator.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_a_pb.py` & `akshare-1.9.9/akshare/stock_feature/stock_a_pb.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_a_pe.py` & `akshare-1.9.9/akshare/stock_feature/stock_a_pe.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_a_pe_and_pb.py` & `akshare-1.9.9/akshare/stock_feature/stock_a_pe_and_pb.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_account_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_account_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_all_pb.py` & `akshare-1.9.9/akshare/stock_feature/stock_all_pb.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_analyst_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_analyst_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_average_position_lg.py` & `akshare-1.9.9/akshare/stock_feature/stock_average_position_lg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_board_concept_ths.py` & `akshare-1.9.9/akshare/stock_feature/stock_board_concept_ths.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_board_industry_ths.py` & `akshare-1.9.9/akshare/stock_feature/stock_board_industry_ths.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_buffett_index_lg.py` & `akshare-1.9.9/akshare/stock_feature/stock_buffett_index_lg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_classify_sina.py` & `akshare-1.9.9/akshare/stock_feature/stock_classify_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_cls_alerts.py` & `akshare-1.9.9/akshare/stock_feature/stock_cls_alerts.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_cninfo_yjyg.py` & `akshare-1.9.9/akshare/stock_feature/stock_cninfo_yjyg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_comment_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_comment_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_congestion_lg.py` & `akshare-1.9.9/akshare/stock_feature/stock_congestion_lg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_dxsyl_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_dxsyl_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_ebs_lg.py` & `akshare-1.9.9/akshare/stock_feature/stock_ebs_lg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_fhps_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_fhps_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_fund_flow.py` & `akshare-1.9.9/akshare/stock_feature/stock_fund_flow.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_gdfx_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_gdfx_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_gdhs.py` & `akshare-1.9.9/akshare/stock_feature/stock_gdhs.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_gdzjc_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_gdzjc_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_gpzy_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_gpzy_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_gxl_lg.py` & `akshare-1.9.9/akshare/stock_feature/stock_gxl_lg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_hist_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_hist_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_hk_valuation_baidu.py` & `akshare-1.9.9/akshare/stock_feature/stock_hk_valuation_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_hot_tgb.py` & `akshare-1.9.9/akshare/stock_feature/stock_hot_tgb.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_hot_xq.py` & `akshare-1.9.9/akshare/stock_feature/stock_hot_xq.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_hsgt_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_hsgt_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_hsgt_exchange_rate.py` & `akshare-1.9.9/akshare/stock_feature/stock_hsgt_exchange_rate.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_inner_trade_xq.py` & `akshare-1.9.9/akshare/stock_feature/stock_inner_trade_xq.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_jgdy_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_jgdy_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_lh_yybpm.py` & `akshare-1.9.9/akshare/stock_feature/stock_lh_yybpm.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_lhb_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_lhb_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_lhb_sina.py` & `akshare-1.9.9/akshare/stock_feature/stock_lhb_sina.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_market_legu.py` & `akshare-1.9.9/akshare/stock_feature/stock_market_legu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_pankou_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_pankou_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_qsjy_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_qsjy_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_report_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_report_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_sse_margin.py` & `akshare-1.9.9/akshare/stock_feature/stock_sse_margin.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_sy_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_sy_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_szse_margin.py` & `akshare-1.9.9/akshare/stock_feature/stock_szse_margin.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_technology_ths.py` & `akshare-1.9.9/akshare/stock_feature/stock_technology_ths.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_tfp_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_tfp_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_three_report_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_three_report_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_ttm_lyr.py` & `akshare-1.9.9/akshare/stock_feature/stock_ttm_lyr.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_us_hist_futunn.py` & `akshare-1.9.9/akshare/stock_feature/stock_us_hist_futunn.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_wencai.py` & `akshare-1.9.9/akshare/stock_feature/stock_wencai.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_yjbb_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_yjbb_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_yjyg_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_yjyg_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_yzxdr_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_yzxdr_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_zf_pg.py` & `akshare-1.9.9/akshare/stock_feature/stock_zf_pg.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_zh_valuation_baidu.py` & `akshare-1.9.9/akshare/stock_feature/stock_zh_valuation_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_zh_vote_baidu.py` & `akshare-1.9.9/akshare/stock_feature/stock_zh_vote_baidu.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/stock_ztb_em.py` & `akshare-1.9.9/akshare/stock_feature/stock_ztb_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_feature/ths.js` & `akshare-1.9.9/akshare/stock_feature/ths.js`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_finance.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_finance.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_finance_hk.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_finance_hk.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_hold.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_hold.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_ipo_declare.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_ipo_declare.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_kcb_detail_sse.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_kcb_detail_sse.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_kcb_sse.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_kcb_sse.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_mda_ym.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_mda_ym.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_notice.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_notice.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_profit_forecast_em.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_profit_forecast_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_profit_forecast_ths.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_profit_forecast_ths.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_recommend.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_recommend.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_register.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_register.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_restricted_em.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_restricted_em.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_zygc.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_zygc.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/stock_fundamental/stock_zyjs_ths.py` & `akshare-1.9.9/akshare/stock_fundamental/stock_zyjs_ths.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/tool/trade_date_hist.py` & `akshare-1.9.9/akshare/tool/trade_date_hist.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/utils/ak_session.py` & `akshare-1.9.9/akshare/utils/ak_session.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/utils/demjson.py` & `akshare-1.9.9/akshare/utils/demjson.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare/utils/token_process.py` & `akshare-1.9.9/akshare/utils/token_process.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/akshare.egg-info/PKG-INFO` & `akshare-1.9.9/akshare.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: akshare
-Version: 1.9.8
+Version: 1.9.9
 Summary: AKShare is an elegant and simple financial data interface library for Python, built for human beings!
 Home-page: https://github.com/akfamily/akshare
 Author: AKFamily
 Author-email: akfamily.akshare@gmail.com
 License: MIT
 Keywords: stock,option,futures,fund,bond,index,air,finance,spider,quant,quantitative,investment,trading,algotrading,data
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `akshare-1.9.8/akshare.egg-info/SOURCES.txt` & `akshare-1.9.9/akshare.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/setup.py` & `akshare-1.9.9/setup.py`

 * *Files identical despite different names*

### Comparing `akshare-1.9.8/tests/test_func.py` & `akshare-1.9.9/tests/test_func.py`

 * *Files identical despite different names*

