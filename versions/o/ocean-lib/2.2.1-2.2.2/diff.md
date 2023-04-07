# Comparing `tmp/ocean-lib-2.2.1.tar.gz` & `tmp/ocean-lib-2.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ocean-lib-2.2.1.tar", last modified: Thu Mar 30 11:04:36 2023, max compression
+gzip compressed data, was "ocean-lib-2.2.2.tar", last modified: Fri Apr  7 11:53:17 2023, max compression
```

## Comparing `ocean-lib-2.2.1.tar` & `ocean-lib-2.2.2.tar`

### file list

```diff
@@ -1,83 +1,83 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.270955 ocean-lib-2.2.1/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     4558 2023-03-30 11:04:36.270955 ocean-lib-2.2.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3950 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.258955 ocean-lib-2.2.1/ocean_lib/
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.258955 ocean-lib-2.2.1/ocean_lib/agreements/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/agreements/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/agreements/consumable.py
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/agreements/service_types.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.258955 ocean-lib-2.2.1/ocean_lib/aquarius/
--rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/aquarius/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5252 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/aquarius/aquarius.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.258955 ocean-lib-2.2.1/ocean_lib/assets/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/assets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3300 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/assets/asset_downloader.py
--rw-r--r--   0 runner    (1001) docker     (123)     4142 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/assets/credentials.py
--rw-r--r--   0 runner    (1001) docker     (123)     7734 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/assets/ddo.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.262955 ocean-lib-2.2.1/ocean_lib/data_provider/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/data_provider/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11738 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/data_provider/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1746 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/data_provider/data_encryptor.py
--rw-r--r--   0 runner    (1001) docker     (123)    19463 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/data_provider/data_service_provider.py
--rw-r--r--   0 runner    (1001) docker     (123)     1699 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/data_provider/fileinfo_provider.py
--rw-r--r--   0 runner    (1001) docker     (123)     2652 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/example_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      599 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.262955 ocean-lib-2.2.1/ocean_lib/http_requests/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/http_requests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1354 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/http_requests/requests_session.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.262955 ocean-lib-2.2.1/ocean_lib/models/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1759 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/compute_input.py
--rw-r--r--   0 runner    (1001) docker     (123)    13329 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/data_nft.py
--rw-r--r--   0 runner    (1001) docker     (123)    13770 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/data_nft_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     8687 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/datatoken1.py
--rw-r--r--   0 runner    (1001) docker     (123)     4116 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/datatoken2.py
--rw-r--r--   0 runner    (1001) docker     (123)    15325 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/datatoken_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.262955 ocean-lib-2.2.1/ocean_lib/models/df/
--rw-r--r--   0 runner    (1001) docker     (123)      213 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/df/df_rewards.py
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/df/df_strategy_v1.py
--rw-r--r--   0 runner    (1001) docker     (123)     4496 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/dispenser.py
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/erc721_token_factory_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      221 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/factory_router.py
--rw-r--r--   0 runner    (1001) docker     (123)    16713 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/fixed_rate_exchange.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.266955 ocean-lib-2.2.1/ocean_lib/models/ve/
--rw-r--r--   0 runner    (1001) docker     (123)      231 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/ve/smart_wallet_checker.py
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/ve/ve_allocate.py
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/ve/ve_delegation.py
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/ve/ve_delegation_proxy.py
--rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/ve/ve_fee_distributor.py
--rw-r--r--   0 runner    (1001) docker     (123)      221 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/ve/ve_fee_estimate.py
--rw-r--r--   0 runner    (1001) docker     (123)      209 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/models/ve/ve_ocean.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.266955 ocean-lib-2.2.1/ocean_lib/ocean/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/ocean/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2277 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/ocean/crypto.py
--rw-r--r--   0 runner    (1001) docker     (123)     1259 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/ocean/mint_fake_ocean.py
--rw-r--r--   0 runner    (1001) docker     (123)     9355 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/ocean/ocean.py
--rw-r--r--   0 runner    (1001) docker     (123)    28559 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/ocean/ocean_assets.py
--rw-r--r--   0 runner    (1001) docker     (123)     5672 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/ocean/ocean_compute.py
--rw-r--r--   0 runner    (1001) docker     (123)     2276 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/ocean/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.266955 ocean-lib-2.2.1/ocean_lib/services/
--rw-r--r--   0 runner    (1001) docker     (123)     2468 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/services/consumer_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)    12053 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/services/service.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.266955 ocean-lib-2.2.1/ocean_lib/structures/
--rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/structures/abi_tuples.py
--rw-r--r--   0 runner    (1001) docker     (123)     2373 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/structures/algorithm_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     3200 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/structures/file_objects.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.270955 ocean-lib-2.2.1/ocean_lib/web3_internal/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/web3_internal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/web3_internal/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     1881 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/web3_internal/contract_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3103 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/web3_internal/contract_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3028 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/ocean_lib/web3_internal/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 11:04:36.258955 ocean-lib-2.2.1/ocean_lib.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4558 2023-03-30 11:04:36.000000 ocean-lib-2.2.1/ocean_lib.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2195 2023-03-30 11:04:36.000000 ocean-lib-2.2.1/ocean_lib.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 11:04:36.000000 ocean-lib-2.2.1/ocean_lib.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 11:04:36.000000 ocean-lib-2.2.1/ocean_lib.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      617 2023-03-30 11:04:36.000000 ocean-lib-2.2.1/ocean_lib.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-03-30 11:04:36.000000 ocean-lib-2.2.1/ocean_lib.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       45 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      354 2023-03-30 11:04:36.270955 ocean-lib-2.2.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2736 2023-03-30 11:04:21.000000 ocean-lib-2.2.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.804018 ocean-lib-2.2.2/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4558 2023-04-07 11:53:17.804018 ocean-lib-2.2.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3950 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.788018 ocean-lib-2.2.2/ocean_lib/
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.792018 ocean-lib-2.2.2/ocean_lib/agreements/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/agreements/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/agreements/consumable.py
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/agreements/service_types.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.792018 ocean-lib-2.2.2/ocean_lib/aquarius/
+-rw-r--r--   0 runner    (1001) docker     (123)      153 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/aquarius/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5252 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/aquarius/aquarius.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.792018 ocean-lib-2.2.2/ocean_lib/assets/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/assets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3300 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/assets/asset_downloader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4142 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/assets/credentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7734 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/assets/ddo.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.796018 ocean-lib-2.2.2/ocean_lib/data_provider/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/data_provider/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11738 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/data_provider/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1746 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/data_provider/data_encryptor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19463 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/data_provider/data_service_provider.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1699 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/data_provider/fileinfo_provider.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2652 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/example_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      599 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.796018 ocean-lib-2.2.2/ocean_lib/http_requests/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/http_requests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1354 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/http_requests/requests_session.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.796018 ocean-lib-2.2.2/ocean_lib/models/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1759 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/compute_input.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13329 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/data_nft.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13770 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/data_nft_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8687 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/datatoken1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4116 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/datatoken2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15325 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/datatoken_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.796018 ocean-lib-2.2.2/ocean_lib/models/df/
+-rw-r--r--   0 runner    (1001) docker     (123)      213 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/df/df_rewards.py
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/df/df_strategy_v1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4496 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/dispenser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/erc721_token_factory_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      221 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/factory_router.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16713 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/fixed_rate_exchange.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.800018 ocean-lib-2.2.2/ocean_lib/models/ve/
+-rw-r--r--   0 runner    (1001) docker     (123)      231 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/ve/smart_wallet_checker.py
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/ve/ve_allocate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/ve/ve_delegation.py
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/ve/ve_delegation_proxy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/ve/ve_fee_distributor.py
+-rw-r--r--   0 runner    (1001) docker     (123)      221 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/ve/ve_fee_estimate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      209 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/models/ve/ve_ocean.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.800018 ocean-lib-2.2.2/ocean_lib/ocean/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/ocean/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2277 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/ocean/crypto.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1259 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/ocean/mint_fake_ocean.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9355 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/ocean/ocean.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28559 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/ocean/ocean_assets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5672 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/ocean/ocean_compute.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2276 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/ocean/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.800018 ocean-lib-2.2.2/ocean_lib/services/
+-rw-r--r--   0 runner    (1001) docker     (123)     2468 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/services/consumer_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12053 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/services/service.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.800018 ocean-lib-2.2.2/ocean_lib/structures/
+-rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/structures/abi_tuples.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2373 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/structures/algorithm_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3200 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/structures/file_objects.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.804018 ocean-lib-2.2.2/ocean_lib/web3_internal/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/web3_internal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/web3_internal/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1881 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/web3_internal/contract_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3103 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/web3_internal/contract_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3028 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/ocean_lib/web3_internal/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:53:17.792018 ocean-lib-2.2.2/ocean_lib.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4558 2023-04-07 11:53:17.000000 ocean-lib-2.2.2/ocean_lib.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2195 2023-04-07 11:53:17.000000 ocean-lib-2.2.2/ocean_lib.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:53:17.000000 ocean-lib-2.2.2/ocean_lib.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:53:17.000000 ocean-lib-2.2.2/ocean_lib.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-07 11:53:17.000000 ocean-lib-2.2.2/ocean_lib.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 11:53:17.000000 ocean-lib-2.2.2/ocean_lib.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       45 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      354 2023-04-07 11:53:17.804018 ocean-lib-2.2.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2764 2023-04-07 11:53:06.000000 ocean-lib-2.2.2/setup.py
```

### Comparing `ocean-lib-2.2.1/LICENSE` & `ocean-lib-2.2.2/LICENSE`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/PKG-INFO` & `ocean-lib-2.2.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ocean-lib
-Version: 2.2.1
+Version: 2.2.2
 Summary: 🐳 Ocean protocol library.
 Home-page: https://github.com/oceanprotocol/ocean.py
 Author: ocean-core-team
 Author-email: devops@oceanprotocol.com
 License: Apache Software License 2.0
 Keywords: ocean-lib
 Classifier: Development Status :: 4 - Beta
```

### Comparing `ocean-lib-2.2.1/README.md` & `ocean-lib-2.2.2/README.md`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/agreements/consumable.py` & `ocean-lib-2.2.2/ocean_lib/agreements/consumable.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/aquarius/aquarius.py` & `ocean-lib-2.2.2/ocean_lib/aquarius/aquarius.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/assets/asset_downloader.py` & `ocean-lib-2.2.2/ocean_lib/assets/asset_downloader.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/assets/credentials.py` & `ocean-lib-2.2.2/ocean_lib/assets/credentials.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/assets/ddo.py` & `ocean-lib-2.2.2/ocean_lib/assets/ddo.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/data_provider/base.py` & `ocean-lib-2.2.2/ocean_lib/data_provider/base.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/data_provider/data_encryptor.py` & `ocean-lib-2.2.2/ocean_lib/data_provider/data_encryptor.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/data_provider/data_service_provider.py` & `ocean-lib-2.2.2/ocean_lib/data_provider/data_service_provider.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/data_provider/fileinfo_provider.py` & `ocean-lib-2.2.2/ocean_lib/data_provider/fileinfo_provider.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/example_config.py` & `ocean-lib-2.2.2/ocean_lib/example_config.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/exceptions.py` & `ocean-lib-2.2.2/ocean_lib/exceptions.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/http_requests/requests_session.py` & `ocean-lib-2.2.2/ocean_lib/http_requests/requests_session.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/compute_input.py` & `ocean-lib-2.2.2/ocean_lib/models/compute_input.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/data_nft.py` & `ocean-lib-2.2.2/ocean_lib/models/data_nft.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/data_nft_factory.py` & `ocean-lib-2.2.2/ocean_lib/models/data_nft_factory.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/datatoken1.py` & `ocean-lib-2.2.2/ocean_lib/models/datatoken1.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/datatoken2.py` & `ocean-lib-2.2.2/ocean_lib/models/datatoken2.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/datatoken_base.py` & `ocean-lib-2.2.2/ocean_lib/models/datatoken_base.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/dispenser.py` & `ocean-lib-2.2.2/ocean_lib/models/dispenser.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/models/fixed_rate_exchange.py` & `ocean-lib-2.2.2/ocean_lib/models/fixed_rate_exchange.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/ocean/crypto.py` & `ocean-lib-2.2.2/ocean_lib/ocean/crypto.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/ocean/mint_fake_ocean.py` & `ocean-lib-2.2.2/ocean_lib/ocean/mint_fake_ocean.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/ocean/ocean.py` & `ocean-lib-2.2.2/ocean_lib/ocean/ocean.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/ocean/ocean_assets.py` & `ocean-lib-2.2.2/ocean_lib/ocean/ocean_assets.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/ocean/ocean_compute.py` & `ocean-lib-2.2.2/ocean_lib/ocean/ocean_compute.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/ocean/util.py` & `ocean-lib-2.2.2/ocean_lib/ocean/util.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/services/consumer_parameters.py` & `ocean-lib-2.2.2/ocean_lib/services/consumer_parameters.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/services/service.py` & `ocean-lib-2.2.2/ocean_lib/services/service.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/structures/abi_tuples.py` & `ocean-lib-2.2.2/ocean_lib/structures/abi_tuples.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/structures/algorithm_metadata.py` & `ocean-lib-2.2.2/ocean_lib/structures/algorithm_metadata.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/structures/file_objects.py` & `ocean-lib-2.2.2/ocean_lib/structures/file_objects.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/web3_internal/contract_base.py` & `ocean-lib-2.2.2/ocean_lib/web3_internal/contract_base.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/web3_internal/contract_utils.py` & `ocean-lib-2.2.2/ocean_lib/web3_internal/contract_utils.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib/web3_internal/utils.py` & `ocean-lib-2.2.2/ocean_lib/web3_internal/utils.py`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib.egg-info/PKG-INFO` & `ocean-lib-2.2.2/ocean_lib.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ocean-lib
-Version: 2.2.1
+Version: 2.2.2
 Summary: 🐳 Ocean protocol library.
 Home-page: https://github.com/oceanprotocol/ocean.py
 Author: ocean-core-team
 Author-email: devops@oceanprotocol.com
 License: Apache Software License 2.0
 Keywords: ocean-lib
 Classifier: Development Status :: 4 - Beta
```

### Comparing `ocean-lib-2.2.1/ocean_lib.egg-info/SOURCES.txt` & `ocean-lib-2.2.2/ocean_lib.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ocean-lib-2.2.1/ocean_lib.egg-info/requires.txt` & `ocean-lib-2.2.2/ocean_lib.egg-info/requires.txt`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 ocean-contracts==1.1.12
 coloredlogs==15.0.1
 requests>=2.21.0
 pytz
 enforce-typing==1.0.0.post1
 eciespy==0.3.11
 eth-brownie==1.19.3
+cryptography==39.0.1
 yarl==1.8.1
 bitarray<3,>=2.6.0
 
 [dev]
 bumpversion==0.6.0
 pkginfo==1.9.6
 twine==4.0.2
```

### Comparing `ocean-lib-2.2.1/setup.py` & `ocean-lib-2.2.2/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -21,14 +21,15 @@
     "ocean-contracts==1.1.12",
     "coloredlogs==15.0.1",
     "requests>=2.21.0",
     "pytz",  # used minimally and unlikely to change, common dependency
     "enforce-typing==1.0.0.post1",
     "eciespy==0.3.11",
     "eth-brownie==1.19.3",
+    "cryptography==39.0.1",
     "yarl==1.8.1",
     "bitarray>=2.6.0,<3",
     # brownie requires web3.py, eth-abi, requests, and more,
     # so those will be installed too.
     # See https://github.com/ethereum/web3.py/blob/master/setup.py
 ]
 # Required to run setup.py:
@@ -86,11 +87,11 @@
     packages=packages,
     setup_requires=setup_requirements,
     test_suite="tests",
     tests_require=test_requirements,
     url="https://github.com/oceanprotocol/ocean.py",
     # fmt: off
     # bumpversion.sh needs single-quotes
-    version='2.2.1',
+    version='2.2.2',
     # fmt: on
     zip_safe=False,
 )
```

