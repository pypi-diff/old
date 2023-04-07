# Comparing `tmp/many_abis-0.1.4.1.tar.gz` & `tmp/many_abis-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "many_abis-0.1.4.1.tar", last modified: Fri Mar 24 08:15:18 2023, max compression
+gzip compressed data, was "many_abis-0.1.5.tar", last modified: Fri Apr  7 07:30:01 2023, max compression
```

## Comparing `many_abis-0.1.4.1.tar` & `many_abis-0.1.5.tar`

### file list

```diff
@@ -1,37 +1,82 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 08:15:18.125911 many_abis-0.1.4.1/
--rw-r--r--   0 runner    (1001) docker     (123)     5939 2023-03-24 08:15:18.125911 many_abis-0.1.4.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5570 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 08:15:18.121911 many_abis-0.1.4.1/many_abis/
--rw-r--r--   0 runner    (1001) docker     (123)      755 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 08:15:18.125911 many_abis-0.1.4.1/many_abis/chains/
--rw-r--r--   0 runner    (1001) docker     (123)      890 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   107206 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/_assets.py
--rw-r--r--   0 runner    (1001) docker     (123)     2990 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1378 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/arbitrum.py
--rw-r--r--   0 runner    (1001) docker     (123)     1633 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/avax.py
--rw-r--r--   0 runner    (1001) docker     (123)     3635 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/bsc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/bsc_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/cronos.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/eth.py
--rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/fantom.py
--rw-r--r--   0 runner    (1001) docker     (123)     1525 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/heco.py
--rw-r--r--   0 runner    (1001) docker     (123)     1157 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/kcc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/moonriver.py
--rw-r--r--   0 runner    (1001) docker     (123)     1707 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/okex.py
--rw-r--r--   0 runner    (1001) docker     (123)     2245 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/chains/polygon.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 08:15:18.125911 many_abis-0.1.4.1/many_abis/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/utils/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 08:15:18.125911 many_abis-0.1.4.1/many_abis/utils/enums/
--rw-r--r--   0 runner    (1001) docker     (123)      205 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/utils/enums/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      634 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/utils/enums/chain_rpc_enum.py
--rw-r--r--   0 runner    (1001) docker     (123)      622 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/utils/enums/chain_scan_enum.py
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/utils/enums/contract_api_enum.py
--rw-r--r--   0 runner    (1001) docker     (123)     1412 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/utils/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/many_abis/utils/tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 08:15:18.121911 many_abis-0.1.4.1/many_abis.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5939 2023-03-24 08:15:18.000000 many_abis-0.1.4.1/many_abis.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-03-24 08:15:18.000000 many_abis-0.1.4.1/many_abis.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 08:15:18.000000 many_abis-0.1.4.1/many_abis.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-03-24 08:15:18.000000 many_abis-0.1.4.1/many_abis.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 08:15:18.125911 many_abis-0.1.4.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      734 2023-03-24 08:15:06.000000 many_abis-0.1.4.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/
+-rw-r--r--   0 runner    (1001) docker     (123)     3592 2023-04-07 07:30:01.381301 many_abis-0.1.5/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3225 2023-04-07 07:29:51.000000 many_abis-0.1.5/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.373301 many_abis-0.1.5/many_abis/
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1481 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/abis.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.373301 many_abis-0.1.5/many_abis/assets/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.373301 many_abis-0.1.5/many_abis/assets/dex/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.373301 many_abis-0.1.5/many_abis/assets/dex/aave/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.377301 many_abis-0.1.5/many_abis/assets/dex/aave/v1/
+-rw-r--r--   0 runner    (1001) docker     (123)    16282 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v1/atoken.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    22101 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v1/lending_pool.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    11612 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v1/lending_pool_addresses_provider.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    34411 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v1/lending_pool_core.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.377301 many_abis-0.1.5/many_abis/assets/dex/aave/v2/
+-rw-r--r--   0 runner    (1001) docker     (123)     8138 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/collector.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    10795 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/incentives_controller.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    22079 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/lending_pool.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    34411 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/lending_pool_addresses_provider.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     2727 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/lending_pool_addresses_provider_registry.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     2683 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/lending_pool_collateral_manager.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    11894 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/lending_pool_configurator.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     2052 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/lending_rate_oracle.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    15658 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/pool_admin.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     4455 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/price_oracle.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     6350 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/protocal_data_provider.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    32705 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/ui_incentive_data_provider.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    12204 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/ui_pool_data_provider.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     5659 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/aave/v2/weth_gateway.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.373301 many_abis-0.1.5/many_abis/assets/dex/joe/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.377301 many_abis-0.1.5/many_abis/assets/dex/joe/v2/
+-rw-r--r--   0 runner    (1001) docker     (123)     3894 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/joe/v2/factory.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    12189 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/joe/v2/pair.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    19626 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/joe/v2/router.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.373301 many_abis-0.1.5/many_abis/assets/dex/pancake/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/
+-rw-r--r--   0 runner    (1001) docker     (123)     2187 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/IPeriphery_payments_with_fee.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    30717 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/master_chef_v3.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    24647 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/non_fungible_position_manager.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     4035 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/quoter.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     5983 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/quoter_v2.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    12082 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/router_v3.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/self_permit.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    14774 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/pancake/v3/staker.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.373301 many_abis-0.1.5/many_abis/assets/dex/uniswap/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/dex/uniswap/bsc/
+-rw-r--r--   0 runner    (1001) docker     (123)     9425 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/bsc/router.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/dex/uniswap/v1/
+-rw-r--r--   0 runner    (1001) docker     (123)    32705 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v1/exchange.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     2195 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v1/factory.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/dex/uniswap/v2/
+-rw-r--r--   0 runner    (1001) docker     (123)     3571 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v2/factory.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    13409 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v2/pair.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    19603 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v2/router.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/dex/uniswap/v3/
+-rw-r--r--   0 runner    (1001) docker     (123)     4419 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v3/factory.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     6431 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v3/multicall.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    24310 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v3/non_fungible_position_manage.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    19610 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v3/pool.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     3702 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v3/quoter.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    11745 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/dex/uniswap/v3/router.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/erc/
+-rw-r--r--   0 runner    (1001) docker     (123)     6181 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/erc/ERC1155.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     3685 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/erc/ERC20.abi
+-rw-r--r--   0 runner    (1001) docker     (123)     6450 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/erc/ERC721.abi
+-rw-r--r--   0 runner    (1001) docker     (123)    10960 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/erc/ERC777.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/tokens/
+-rw-r--r--   0 runner    (1001) docker     (123)     4612 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/tokens/weth9.abi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.381301 many_abis-0.1.5/many_abis/assets/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)    19567 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/assets/utils/chains.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1158 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/chains.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1958 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      666 2023-04-07 07:29:51.000000 many_abis-0.1.5/many_abis/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:30:01.377301 many_abis-0.1.5/many_abis.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3592 2023-04-07 07:30:01.000000 many_abis-0.1.5/many_abis.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2536 2023-04-07 07:30:01.000000 many_abis-0.1.5/many_abis.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:30:01.000000 many_abis-0.1.5/many_abis.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-07 07:30:01.000000 many_abis-0.1.5/many_abis.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 07:30:01.000000 many_abis-0.1.5/many_abis.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 07:30:01.381301 many_abis-0.1.5/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-04-07 07:29:51.000000 many_abis-0.1.5/setup.py
```

