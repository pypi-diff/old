# Comparing `tmp/transpose_data-3.1.2.tar.gz` & `tmp/transpose_data-4.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "transpose_data-3.1.2.tar", last modified: Wed Jan  4 14:44:45 2023, max compression
+gzip compressed data, was "transpose_data-4.0.0.tar", last modified: Thu Apr  6 22:05:38 2023, max compression
```

## Comparing `transpose_data-3.1.2.tar` & `transpose_data-4.0.0.tar`

### file list

```diff
@@ -1,97 +1,103 @@
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.223363 transpose_data-3.1.2/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     1066 2022-05-27 16:10:33.000000 transpose_data-3.1.2/LICENSE
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        9 2022-06-01 23:37:24.000000 transpose_data-3.1.2/MANIFEST.in
--rw-r--r--   0 jonathanbecker   (501) staff       (20)    16122 2023-01-04 14:44:45.222976 transpose_data-3.1.2/PKG-INFO
--rw-r--r--   0 jonathanbecker   (501) staff       (20)    15252 2022-11-27 15:12:34.000000 transpose_data-3.1.2/README.md
--rw-r--r--   0 jonathanbecker   (501) staff       (20)       38 2023-01-04 14:44:45.223416 transpose_data-3.1.2/setup.cfg
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     1562 2023-01-04 14:44:34.000000 transpose_data-3.1.2/setup.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.204485 transpose_data-3.1.2/transpose/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      201 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/__init__.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-06-01 22:54:03.000000 transpose_data-3.1.2/transpose/__main__.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.204826 transpose_data-3.1.2/transpose/extras/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      220 2022-06-28 17:30:52.000000 transpose_data-3.1.2/transpose/extras/__init__.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     6916 2022-06-16 15:05:28.000000 transpose_data-3.1.2/transpose/extras/plot.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.205149 transpose_data-3.1.2/transpose/models/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      103 2022-06-28 17:30:34.000000 transpose_data-3.1.2/transpose/models/__init__.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.205496 transpose_data-3.1.2/transpose/src/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:48.000000 transpose_data-3.1.2/transpose/src/__init__.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.205933 transpose_data-3.1.2/transpose/src/api/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 17:29:51.000000 transpose_data-3.1.2/transpose/src/api/__init__.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.209260 transpose_data-3.1.2/transpose/src/api/block/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:56.000000 transpose_data-3.1.2/transpose/src/api/block/__init__.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      405 2022-06-02 15:28:23.000000 transpose_data-3.1.2/transpose/src/api/block/_accounts_by_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      599 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/block/_accounts_by_date_created.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      451 2022-10-31 15:56:44.000000 transpose_data-3.1.2/transpose/src/api/block/_blocks_by_date.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      458 2022-10-31 02:07:41.000000 transpose_data-3.1.2/transpose/src/api/block/_blocks_by_number.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      589 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/block/_contracts_by_creator.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      744 2022-05-31 20:16:32.000000 transpose_data-3.1.2/transpose/src/api/block/_logs_by_block.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      431 2022-05-31 21:53:19.000000 transpose_data-3.1.2/transpose/src/api/block/_logs_by_transaction.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      480 2023-01-04 14:43:27.000000 transpose_data-3.1.2/transpose/src/api/block/_transactions_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      483 2022-05-31 18:41:18.000000 transpose_data-3.1.2/transpose/src/api/block/_transactions_by_block.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      495 2022-05-31 18:41:08.000000 transpose_data-3.1.2/transpose/src/api/block/_transactions_by_date.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      405 2022-05-31 21:53:33.000000 transpose_data-3.1.2/transpose/src/api/block/_transactions_by_hash.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     6752 2023-01-04 14:43:27.000000 transpose_data-3.1.2/transpose/src/api/block/base.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     6114 2022-10-31 15:56:30.000000 transpose_data-3.1.2/transpose/src/api/constants.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.211431 transpose_data-3.1.2/transpose/src/api/ens/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:55.000000 transpose_data-3.1.2/transpose/src/api/ens/__init__.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      228 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/ens/_records_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      533 2022-05-27 21:18:51.000000 transpose_data-3.1.2/transpose/src/api/ens/_records_by_date.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      355 2022-05-31 21:50:53.000000 transpose_data-3.1.2/transpose/src/api/ens/_records_by_name.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      284 2022-05-27 20:41:28.000000 transpose_data-3.1.2/transpose/src/api/ens/_records_by_owner.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      388 2022-05-27 22:44:42.000000 transpose_data-3.1.2/transpose/src/api/ens/_records_by_token_id.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      583 2022-12-21 18:57:18.000000 transpose_data-3.1.2/transpose/src/api/ens/_transfers_by_name.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      591 2022-12-21 18:57:29.000000 transpose_data-3.1.2/transpose/src/api/ens/_transfers_by_token_id.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     3988 2022-12-21 18:57:46.000000 transpose_data-3.1.2/transpose/src/api/ens/base.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.216413 transpose_data-3.1.2/transpose/src/api/nft/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:54.000000 transpose_data-3.1.2/transpose/src/api/nft/__init__.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      436 2022-05-31 22:08:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_collections_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      718 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_collections_by_date_created.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      325 2022-07-26 20:53:53.000000 transpose_data-3.1.2/transpose/src/api/nft/_collections_by_name.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      337 2022-07-26 20:54:17.000000 transpose_data-3.1.2/transpose/src/api/nft/_collections_by_symbol.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      319 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_nfts_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      646 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_nfts_by_date_minted.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      297 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_nfts_by_name.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      422 2022-05-31 22:52:06.000000 transpose_data-3.1.2/transpose/src/api/nft/_nfts_by_owner.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      632 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_nfts_by_token_id.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      325 2022-05-31 23:09:34.000000 transpose_data-3.1.2/transpose/src/api/nft/_owners_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      385 2022-05-31 23:11:35.000000 transpose_data-3.1.2/transpose/src/api/nft/_owners_by_token_id.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      396 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_sales.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      541 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_sales_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      520 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_sales_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      552 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_sales_by_token_id.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      457 2022-12-21 18:58:22.000000 transpose_data-3.1.2/transpose/src/api/nft/_transfers.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      603 2022-12-21 18:57:56.000000 transpose_data-3.1.2/transpose/src/api/nft/_transfers_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      660 2022-12-21 18:58:03.000000 transpose_data-3.1.2/transpose/src/api/nft/_transfers_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      683 2022-12-21 18:58:12.000000 transpose_data-3.1.2/transpose/src/api/nft/_transfers_by_token_id.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)    10684 2022-12-21 18:58:37.000000 transpose_data-3.1.2/transpose/src/api/nft/base.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.220723 transpose_data-3.1.2/transpose/src/api/token/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:53.000000 transpose_data-3.1.2/transpose/src/api/token/__init__.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      434 2022-06-01 20:16:47.000000 transpose_data-3.1.2/transpose/src/api/token/_native_token_balances_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      526 2022-06-01 20:11:31.000000 transpose_data-3.1.2/transpose/src/api/token/_native_token_transfers.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      805 2022-06-01 20:12:47.000000 transpose_data-3.1.2/transpose/src/api/token/_native_token_transfers_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      331 2022-06-02 17:25:00.000000 transpose_data-3.1.2/transpose/src/api/token/_owners_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      423 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/token/_swaps.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      558 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/token/_swaps_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      649 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/token/_swaps_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      581 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/token/_swaps_by_pair.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      430 2022-06-01 19:06:51.000000 transpose_data-3.1.2/transpose/src/api/token/_tokens_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      712 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/api/token/_tokens_by_date_created.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      300 2022-07-26 20:55:18.000000 transpose_data-3.1.2/transpose/src/api/token/_tokens_by_name.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      434 2022-06-01 19:44:57.000000 transpose_data-3.1.2/transpose/src/api/token/_tokens_by_owner.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      312 2022-07-26 20:55:27.000000 transpose_data-3.1.2/transpose/src/api/token/_tokens_by_symbol.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      461 2022-12-21 18:58:59.000000 transpose_data-3.1.2/transpose/src/api/token/_transfers.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      607 2022-12-21 18:58:45.000000 transpose_data-3.1.2/transpose/src/api/token/_transfers_by_account.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      664 2022-12-21 18:58:53.000000 transpose_data-3.1.2/transpose/src/api/token/_transfers_by_contract_address.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     9696 2022-12-21 18:59:10.000000 transpose_data-3.1.2/transpose/src/api/token/base.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     4259 2022-11-27 15:12:34.000000 transpose_data-3.1.2/transpose/src/base.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.221566 transpose_data-3.1.2/transpose/src/util/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:52.000000 transpose_data-3.1.2/transpose/src/util/__init__.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     2315 2022-10-31 01:46:12.000000 transpose_data-3.1.2/transpose/src/util/errors.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)      410 2022-05-27 19:56:33.000000 transpose_data-3.1.2/transpose/src/util/io.py
--rw-r--r--   0 jonathanbecker   (501) staff       (20)    18327 2023-01-04 14:32:45.000000 transpose_data-3.1.2/transpose/src/util/models.py
-drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-01-04 14:44:45.222696 transpose_data-3.1.2/transpose_data.egg-info/
--rw-r--r--   0 jonathanbecker   (501) staff       (20)    16122 2023-01-04 14:44:45.000000 transpose_data-3.1.2/transpose_data.egg-info/PKG-INFO
--rw-r--r--   0 jonathanbecker   (501) staff       (20)     3347 2023-01-04 14:44:45.000000 transpose_data-3.1.2/transpose_data.egg-info/SOURCES.txt
--rw-r--r--   0 jonathanbecker   (501) staff       (20)        1 2023-01-04 14:44:45.000000 transpose_data-3.1.2/transpose_data.egg-info/dependency_links.txt
--rw-r--r--   0 jonathanbecker   (501) staff       (20)       23 2023-01-04 14:44:45.000000 transpose_data-3.1.2/transpose_data.egg-info/requires.txt
--rw-r--r--   0 jonathanbecker   (501) staff       (20)       10 2023-01-04 14:44:45.000000 transpose_data-3.1.2/transpose_data.egg-info/top_level.txt
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.085889 transpose_data-4.0.0/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     1066 2022-05-27 16:10:33.000000 transpose_data-4.0.0/LICENSE
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        9 2022-06-01 23:37:24.000000 transpose_data-4.0.0/MANIFEST.in
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)    15881 2023-04-06 22:05:38.085349 transpose_data-4.0.0/PKG-INFO
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)    15011 2023-04-06 21:38:19.000000 transpose_data-4.0.0/README.md
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)       38 2023-04-06 22:05:38.086033 transpose_data-4.0.0/setup.cfg
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     1562 2023-04-06 22:04:16.000000 transpose_data-4.0.0/setup.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.039327 transpose_data-4.0.0/transpose/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      201 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-06-01 22:54:03.000000 transpose_data-4.0.0/transpose/__main__.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.040121 transpose_data-4.0.0/transpose/extras/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      220 2022-06-28 17:30:52.000000 transpose_data-4.0.0/transpose/extras/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     6916 2022-06-16 15:05:28.000000 transpose_data-4.0.0/transpose/extras/plot.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.040696 transpose_data-4.0.0/transpose/models/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      103 2022-06-28 17:30:34.000000 transpose_data-4.0.0/transpose/models/__init__.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.041702 transpose_data-4.0.0/transpose/src/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:48.000000 transpose_data-4.0.0/transpose/src/__init__.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.042691 transpose_data-4.0.0/transpose/src/api/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 17:29:51.000000 transpose_data-4.0.0/transpose/src/api/__init__.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.051250 transpose_data-4.0.0/transpose/src/api/block/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:56.000000 transpose_data-4.0.0/transpose/src/api/block/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      405 2022-06-02 15:28:23.000000 transpose_data-4.0.0/transpose/src/api/block/_accounts_by_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      599 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/block/_accounts_by_date_created.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      451 2022-10-31 15:56:44.000000 transpose_data-4.0.0/transpose/src/api/block/_blocks_by_date.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      458 2022-10-31 02:07:41.000000 transpose_data-4.0.0/transpose/src/api/block/_blocks_by_number.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      589 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/block/_contracts_by_creator.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      744 2022-05-31 20:16:32.000000 transpose_data-4.0.0/transpose/src/api/block/_logs_by_block.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      431 2022-05-31 21:53:19.000000 transpose_data-4.0.0/transpose/src/api/block/_logs_by_transaction.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      480 2023-01-04 14:43:27.000000 transpose_data-4.0.0/transpose/src/api/block/_transactions_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      483 2022-05-31 18:41:18.000000 transpose_data-4.0.0/transpose/src/api/block/_transactions_by_block.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      495 2022-05-31 18:41:08.000000 transpose_data-4.0.0/transpose/src/api/block/_transactions_by_date.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      405 2022-05-31 21:53:33.000000 transpose_data-4.0.0/transpose/src/api/block/_transactions_by_hash.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     6752 2023-01-04 14:43:27.000000 transpose_data-4.0.0/transpose/src/api/block/base.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     6114 2022-10-31 15:56:30.000000 transpose_data-4.0.0/transpose/src/api/constants.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.052245 transpose_data-4.0.0/transpose/src/api/endpoint/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 17:42:25.000000 transpose_data-4.0.0/transpose/src/api/endpoint/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     1247 2023-04-06 18:06:39.000000 transpose_data-4.0.0/transpose/src/api/endpoint/base.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.056745 transpose_data-4.0.0/transpose/src/api/ens/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:55.000000 transpose_data-4.0.0/transpose/src/api/ens/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      228 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/ens/_records_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      533 2022-05-27 21:18:51.000000 transpose_data-4.0.0/transpose/src/api/ens/_records_by_date.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      355 2022-05-31 21:50:53.000000 transpose_data-4.0.0/transpose/src/api/ens/_records_by_name.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      284 2022-05-27 20:41:28.000000 transpose_data-4.0.0/transpose/src/api/ens/_records_by_owner.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      388 2022-05-27 22:44:42.000000 transpose_data-4.0.0/transpose/src/api/ens/_records_by_token_id.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      583 2022-12-21 18:57:18.000000 transpose_data-4.0.0/transpose/src/api/ens/_transfers_by_name.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      591 2022-12-21 18:57:29.000000 transpose_data-4.0.0/transpose/src/api/ens/_transfers_by_token_id.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     3988 2022-12-21 18:57:46.000000 transpose_data-4.0.0/transpose/src/api/ens/base.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.068014 transpose_data-4.0.0/transpose/src/api/nft/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:54.000000 transpose_data-4.0.0/transpose/src/api/nft/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      436 2022-05-31 22:08:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_collections_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      718 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_collections_by_date_created.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      325 2022-07-26 20:53:53.000000 transpose_data-4.0.0/transpose/src/api/nft/_collections_by_name.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      337 2022-07-26 20:54:17.000000 transpose_data-4.0.0/transpose/src/api/nft/_collections_by_symbol.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      319 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_nfts_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      646 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_nfts_by_date_minted.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      297 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_nfts_by_name.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      422 2022-05-31 22:52:06.000000 transpose_data-4.0.0/transpose/src/api/nft/_nfts_by_owner.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      632 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_nfts_by_token_id.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      325 2022-05-31 23:09:34.000000 transpose_data-4.0.0/transpose/src/api/nft/_owners_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      385 2022-05-31 23:11:35.000000 transpose_data-4.0.0/transpose/src/api/nft/_owners_by_token_id.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      396 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_sales.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      541 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_sales_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      520 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_sales_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      552 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_sales_by_token_id.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      457 2022-12-21 18:58:22.000000 transpose_data-4.0.0/transpose/src/api/nft/_transfers.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      603 2022-12-21 18:57:56.000000 transpose_data-4.0.0/transpose/src/api/nft/_transfers_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      660 2022-12-21 18:58:03.000000 transpose_data-4.0.0/transpose/src/api/nft/_transfers_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      683 2022-12-21 18:58:12.000000 transpose_data-4.0.0/transpose/src/api/nft/_transfers_by_token_id.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)    10684 2022-12-21 18:58:37.000000 transpose_data-4.0.0/transpose/src/api/nft/base.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.068960 transpose_data-4.0.0/transpose/src/api/sql/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 17:19:08.000000 transpose_data-4.0.0/transpose/src/api/sql/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     1220 2023-04-06 17:36:35.000000 transpose_data-4.0.0/transpose/src/api/sql/base.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.079662 transpose_data-4.0.0/transpose/src/api/token/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:53.000000 transpose_data-4.0.0/transpose/src/api/token/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      434 2022-06-01 20:16:47.000000 transpose_data-4.0.0/transpose/src/api/token/_native_token_balances_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      526 2022-06-01 20:11:31.000000 transpose_data-4.0.0/transpose/src/api/token/_native_token_transfers.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      805 2022-06-01 20:12:47.000000 transpose_data-4.0.0/transpose/src/api/token/_native_token_transfers_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      331 2022-06-02 17:25:00.000000 transpose_data-4.0.0/transpose/src/api/token/_owners_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      423 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/token/_swaps.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      558 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/token/_swaps_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      649 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/token/_swaps_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      581 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/token/_swaps_by_pair.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      430 2022-06-01 19:06:51.000000 transpose_data-4.0.0/transpose/src/api/token/_tokens_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      712 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/api/token/_tokens_by_date_created.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      300 2022-07-26 20:55:18.000000 transpose_data-4.0.0/transpose/src/api/token/_tokens_by_name.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      434 2022-06-01 19:44:57.000000 transpose_data-4.0.0/transpose/src/api/token/_tokens_by_owner.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      312 2022-07-26 20:55:27.000000 transpose_data-4.0.0/transpose/src/api/token/_tokens_by_symbol.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      461 2022-12-21 18:58:59.000000 transpose_data-4.0.0/transpose/src/api/token/_transfers.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      607 2022-12-21 18:58:45.000000 transpose_data-4.0.0/transpose/src/api/token/_transfers_by_account.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      664 2022-12-21 18:58:53.000000 transpose_data-4.0.0/transpose/src/api/token/_transfers_by_contract_address.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     9696 2022-12-21 18:59:10.000000 transpose_data-4.0.0/transpose/src/api/token/base.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     6097 2023-04-06 18:02:55.000000 transpose_data-4.0.0/transpose/src/base.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.081750 transpose_data-4.0.0/transpose/src/util/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        0 2022-05-27 16:33:52.000000 transpose_data-4.0.0/transpose/src/util/__init__.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     2315 2022-10-31 01:46:12.000000 transpose_data-4.0.0/transpose/src/util/errors.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)      410 2022-05-27 19:56:33.000000 transpose_data-4.0.0/transpose/src/util/io.py
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)    18327 2023-04-06 16:49:24.000000 transpose_data-4.0.0/transpose/src/util/models.py
+drwxr-xr-x   0 jonathanbecker   (501) staff       (20)        0 2023-04-06 22:05:38.084633 transpose_data-4.0.0/transpose_data.egg-info/
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)    15881 2023-04-06 22:05:38.000000 transpose_data-4.0.0/transpose_data.egg-info/PKG-INFO
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)     3485 2023-04-06 22:05:38.000000 transpose_data-4.0.0/transpose_data.egg-info/SOURCES.txt
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)        1 2023-04-06 22:05:38.000000 transpose_data-4.0.0/transpose_data.egg-info/dependency_links.txt
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)       23 2023-04-06 22:05:38.000000 transpose_data-4.0.0/transpose_data.egg-info/requires.txt
+-rw-r--r--   0 jonathanbecker   (501) staff       (20)       10 2023-04-06 22:05:38.000000 transpose_data-4.0.0/transpose_data.egg-info/top_level.txt
```

### Comparing `transpose_data-3.1.2/LICENSE` & `transpose_data-4.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/PKG-INFO` & `transpose_data-4.0.0/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: transpose_data
-Version: 3.1.2
+Version: 4.0.0
 Summary: Web3 Data Made Simple. Powerful APIs for accessing human-readable blockchain data at scale: from blocks and transactions to NFTs and tokens.
 Home-page: https://github.com/TransposeData/transpose-python-sdk
 Author: Michael Calvey (michaeljohncalvey), Alex Langshur (alangshur), Jonathan Becker (jon-becker)
 Author-email: michael@transpose.io, alex@transpose.io, jon@transpose.io
 License: MIT
 Keywords: web3,data,ethereum,web3 data,ethereum data
 Classifier: Development Status :: 3 - Alpha
@@ -22,15 +22,15 @@
 # Welcome to the Transpose Python SDK
 ![Deployment Tests](https://github.com/TransposeData/transpose-python-sdk/actions/workflows/deployment_tests.yml/badge.svg) ![PyPI version](https://badge.fury.io/py/transpose-data.svg) ![Installations](https://img.shields.io/pypi/dd/transpose-data?color=g)
 
 A modern python wrapper for the Transpose API Suite.
 
 ## Getting an API Key
 
-To obtain a free Open Alpha Transpose API key, sign up on our [website](https://www.transpose.io/). API Keys are rate limited to 1 request per second and 100,000 requests per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord!
+To obtain a free Transpose API key, sign up on our [website](https://www.transpose.io/). Free tier keys have a rate limit of 1 request per second and 250,000 credits per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord or upgrade your tier directly in the webapp!
 
 Join our [Discord](https://discord.gg/AKguqp3U57) to ask technical questions, share what you're building, and chat with others in the community.
 
 ## Installation
 
 **Python 3.8 or higher is recommended**
 
@@ -40,20 +40,22 @@
 ```
 
 ---
 
 ## Documentation
 You can find specific documentation on a per-product basis below.
 
-|                                                                            Product                                                                            | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
-| :-----------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
-| <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628ebc9704701b4d5610ac1a_Blockchain_Logo_Solid.png" width="50" height="50"><br> Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
-|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628d465b6551e284a9ae73e4_Wallet_Logo_ENS.png" width="50" height="50"><br> ENS API     | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
-|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/6286795ef57a1412d6d767fc_NFT_Logo_Solid.png" width="50" height="50"><br> NFT API      | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
-|   <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628fb0f77f6279a920577119_Token_Logo2_Solid.png" width="50" height="50"><br>Token API    | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
+|  Product  | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
+| :-------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
+| Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
+|  ENS API  | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
+|  NFT API  | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
+| Token API | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
+| SQL API | The SQL API provides direct SQL access to our entire ecosystem of indexed blockchain data. Paired with our robust indexing pipeline, SQL access gives unlimited flexibility in how you mix, aggregate, and query activity across the blockchain.  | [SQL API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/sql.md) |
+| Endpoint API | The Endpoint API provides customized REST endpoints that you ca n create, version, and use directly in your production applications. | [Endpoint API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/endpoint.md) |
 
 ## SDK Documentation
 You can learn more about the Transpose SDK and how it works below.
 
 
 ### SDK Classes
 The Transpose SDK uses custom classes to represent API responses:
@@ -189,15 +191,15 @@
 | requests_per_second | No       | The number of requests per second to make                     | ``int``  |
 | results_to_fetch    | No       | The number of results to fetch                                | ``int``  |
 
 #### Responses
 | Code | Title                 | Model                                                                                                        |
 | ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
 | 200  | Success               | Data Model                                                                                                   |
-| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) 
+| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 401  | Unauthorized          | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 
 Here is an example of how to use ``bulk_request``:
 
@@ -339,10 +341,11 @@
     "is_expired":false,
     "last_refreshed":"2022-06-01T09:51:23Z"
   }
 ]
 ```
 
 ## Links
+
 - [SDK Examples](https://github.com/TransposeData/transpose-python-sdk/tree/main/demo)
 - [Transpose Documentation](https://docs.transpose.io)
 - [Official Discord Server](https://discord.gg/AKguqp3U57)
```

### Comparing `transpose_data-3.1.2/README.md` & `transpose_data-4.0.0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # Welcome to the Transpose Python SDK
 ![Deployment Tests](https://github.com/TransposeData/transpose-python-sdk/actions/workflows/deployment_tests.yml/badge.svg) ![PyPI version](https://badge.fury.io/py/transpose-data.svg) ![Installations](https://img.shields.io/pypi/dd/transpose-data?color=g)
 
 A modern python wrapper for the Transpose API Suite.
 
 ## Getting an API Key
 
-To obtain a free Open Alpha Transpose API key, sign up on our [website](https://www.transpose.io/). API Keys are rate limited to 1 request per second and 100,000 requests per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord!
+To obtain a free Transpose API key, sign up on our [website](https://www.transpose.io/). Free tier keys have a rate limit of 1 request per second and 250,000 credits per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord or upgrade your tier directly in the webapp!
 
 Join our [Discord](https://discord.gg/AKguqp3U57) to ask technical questions, share what you're building, and chat with others in the community.
 
 ## Installation
 
 **Python 3.8 or higher is recommended**
 
@@ -21,20 +21,22 @@
 ```
 
 ---
 
 ## Documentation
 You can find specific documentation on a per-product basis below.
 
-|                                                                            Product                                                                            | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
-| :-----------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
-| <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628ebc9704701b4d5610ac1a_Blockchain_Logo_Solid.png" width="50" height="50"><br> Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
-|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628d465b6551e284a9ae73e4_Wallet_Logo_ENS.png" width="50" height="50"><br> ENS API     | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
-|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/6286795ef57a1412d6d767fc_NFT_Logo_Solid.png" width="50" height="50"><br> NFT API      | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
-|   <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628fb0f77f6279a920577119_Token_Logo2_Solid.png" width="50" height="50"><br>Token API    | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
+|  Product  | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
+| :-------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
+| Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
+|  ENS API  | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
+|  NFT API  | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
+| Token API | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
+| SQL API | The SQL API provides direct SQL access to our entire ecosystem of indexed blockchain data. Paired with our robust indexing pipeline, SQL access gives unlimited flexibility in how you mix, aggregate, and query activity across the blockchain.  | [SQL API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/sql.md) |
+| Endpoint API | The Endpoint API provides customized REST endpoints that you ca n create, version, and use directly in your production applications. | [Endpoint API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/endpoint.md) |
 
 ## SDK Documentation
 You can learn more about the Transpose SDK and how it works below.
 
 
 ### SDK Classes
 The Transpose SDK uses custom classes to represent API responses:
@@ -170,15 +172,15 @@
 | requests_per_second | No       | The number of requests per second to make                     | ``int``  |
 | results_to_fetch    | No       | The number of results to fetch                                | ``int``  |
 
 #### Responses
 | Code | Title                 | Model                                                                                                        |
 | ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
 | 200  | Success               | Data Model                                                                                                   |
-| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) 
+| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 401  | Unauthorized          | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 
 Here is an example of how to use ``bulk_request``:
 
@@ -320,10 +322,11 @@
     "is_expired":false,
     "last_refreshed":"2022-06-01T09:51:23Z"
   }
 ]
 ```
 
 ## Links
+
 - [SDK Examples](https://github.com/TransposeData/transpose-python-sdk/tree/main/demo)
 - [Transpose Documentation](https://docs.transpose.io)
 - [Official Discord Server](https://discord.gg/AKguqp3U57)
```

### Comparing `transpose_data-3.1.2/setup.py` & `transpose_data-4.0.0/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     long_description = f.read()
     
 setup(
     name='transpose_data',
     
     # version compliant with PEP440
     # https://peps.python.org/pep-0440/
-    version='3.1.2',
+    version='4.0.0',
     
     # project meta
     long_description = long_description,
     long_description_content_type="text/markdown",
     include_package_data = True,
     description='Web3 Data Made Simple. Powerful APIs for accessing human-readable blockchain data at scale: from blocks and transactions to NFTs and tokens.',
     keywords=['web3', 'data', 'ethereum', 'web3 data', 'ethereum data'],
```

### Comparing `transpose_data-3.1.2/transpose/extras/plot.py` & `transpose_data-4.0.0/transpose/extras/plot.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/block/_accounts_by_date_created.py` & `transpose_data-4.0.0/transpose/src/api/block/_accounts_by_date_created.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/block/_contracts_by_creator.py` & `transpose_data-4.0.0/transpose/src/api/block/_contracts_by_creator.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/block/_logs_by_block.py` & `transpose_data-4.0.0/transpose/src/api/block/_logs_by_block.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/block/base.py` & `transpose_data-4.0.0/transpose/src/api/block/base.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/constants.py` & `transpose_data-4.0.0/transpose/src/api/constants.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/ens/_records_by_date.py` & `transpose_data-4.0.0/transpose/src/api/ens/_records_by_date.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/ens/_transfers_by_name.py` & `transpose_data-4.0.0/transpose/src/api/ens/_transfers_by_name.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/ens/_transfers_by_token_id.py` & `transpose_data-4.0.0/transpose/src/api/ens/_transfers_by_token_id.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/ens/base.py` & `transpose_data-4.0.0/transpose/src/api/ens/base.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_collections_by_date_created.py` & `transpose_data-4.0.0/transpose/src/api/nft/_collections_by_date_created.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_nfts_by_date_minted.py` & `transpose_data-4.0.0/transpose/src/api/nft/_nfts_by_date_minted.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_nfts_by_token_id.py` & `transpose_data-4.0.0/transpose/src/api/nft/_nfts_by_token_id.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_sales_by_account.py` & `transpose_data-4.0.0/transpose/src/api/nft/_sales_by_account.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_sales_by_contract_address.py` & `transpose_data-4.0.0/transpose/src/api/nft/_sales_by_contract_address.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_sales_by_token_id.py` & `transpose_data-4.0.0/transpose/src/api/nft/_sales_by_token_id.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_transfers_by_account.py` & `transpose_data-4.0.0/transpose/src/api/nft/_transfers_by_account.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_transfers_by_contract_address.py` & `transpose_data-4.0.0/transpose/src/api/nft/_transfers_by_contract_address.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/_transfers_by_token_id.py` & `transpose_data-4.0.0/transpose/src/api/nft/_transfers_by_token_id.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/nft/base.py` & `transpose_data-4.0.0/transpose/src/api/nft/base.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_native_token_transfers.py` & `transpose_data-4.0.0/transpose/src/api/token/_native_token_transfers.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_native_token_transfers_by_account.py` & `transpose_data-4.0.0/transpose/src/api/token/_native_token_transfers_by_account.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_swaps_by_account.py` & `transpose_data-4.0.0/transpose/src/api/token/_swaps_by_account.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_swaps_by_contract_address.py` & `transpose_data-4.0.0/transpose/src/api/token/_swaps_by_contract_address.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_swaps_by_pair.py` & `transpose_data-4.0.0/transpose/src/api/token/_swaps_by_pair.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_tokens_by_date_created.py` & `transpose_data-4.0.0/transpose/src/api/token/_tokens_by_date_created.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_transfers_by_account.py` & `transpose_data-4.0.0/transpose/src/api/token/_transfers_by_account.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/_transfers_by_contract_address.py` & `transpose_data-4.0.0/transpose/src/api/token/_transfers_by_contract_address.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/api/token/base.py` & `transpose_data-4.0.0/transpose/src/api/token/base.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/base.py` & `transpose_data-4.0.0/transpose/src/base.py`

 * *Files 21% similar despite different names*

```diff
@@ -4,15 +4,16 @@
 from ..src.util.models import *
 
 from ..src.util.errors import *
 from ..src.api.ens.base import ENS
 from ..src.api.nft.base import NFT
 from ..src.api.block.base import Block
 from ..src.api.token.base import Token
-
+from ..src.api.sql.base import SQL
+from ..src.api.endpoint.base import Endpoint
 
 # base class for the Transpose python SDK
 class Transpose:
     def __init__(
         self,
         api_key: str,
         debug: bool=False,
@@ -42,14 +43,16 @@
             self.api_key = api_key
                         
         # define the subclasses
         self.ens   = ENS(self)
         self.nft   = NFT(self)
         self.block = Block(self)
         self.token = Token(self)
+        self.sql   = SQL(self)
+        self.endpoint = Endpoint(self)
         
         # deprecated in favor of the new API
         self.ENS = self.ens
         self.NFT = self.nft
         self.Block = self.block
         self.Token = self.token
     
@@ -114,8 +117,48 @@
             
             # if we are in json mode, return the raw json
             if self.json:
                 return response
 
             return list(model(dict(each)) for each in response['results'])
         else:
+            raise_custom_error(request.status_code, request.json()['message'])
+    
+    # the base function for performing authorized requests to the Transpose API suite
+    def perform_authorized_request(self, model: type, endpoint: str, api_key: str=None):
+        if endpoint is None: 
+            return None
+        
+        # build the request
+        request_headers = {
+            'x-api-key': api_key if api_key else self.api_key,
+            'Accept': 'application/json',
+        }
+        
+        # add chain_id to the request
+        endpoint += f'&chain_id={self.chain_id}'
+        
+        # if in verbose mode, log the endpoint
+        print("\n{}\n  {}\n".format(endpoint.replace("https://api.transpose.io", self.host).split("?")[0], "\n  ".join(endpoint.split("?")[1].split("&")))) if self.verbose else None
+        request = requests.get(endpoint.replace("https://api.transpose.io", self.host), headers=request_headers)
+        
+        # check for a successful response
+        if request.status_code == 200:
+            
+            response = request.json()
+            
+            # If the response contains a paginator, set the paginator's next endpoint
+            if 'next' in response:
+                if response['next'] is None:
+                    self._next = None
+                    self._next_class_name = None
+                else: 
+                    self._next = response['next']
+                    self._next_class_name = model
+            
+            # if we are in json mode, return the raw json
+            if self.json:
+                return response
+
+            return list(model(dict(each)) for each in response['results'])
+        else:
             raise_custom_error(request.status_code, request.json()['message'])
```

### Comparing `transpose_data-3.1.2/transpose/src/util/errors.py` & `transpose_data-4.0.0/transpose/src/util/errors.py`

 * *Files identical despite different names*

### Comparing `transpose_data-3.1.2/transpose/src/util/models.py` & `transpose_data-4.0.0/transpose/src/util/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -265,15 +265,15 @@
         self.token_id: int = None
         self.owner: str = None
         self.balance: int = None
         
         super().__init__(_data)
         
     def __repr__(self) -> str:
-        return '<NFTOwnerObject:  owner="{}"  contract_address="{}"  token_id="{}">'.format(self.contract_address, self.token_id, self.owner)
+        return '<NFTOwnerObject:  owner="{}"  contract_address="{}"  token_id="{}">'.format(self.owner, self.contract_address, self.token_id)
         
 class NFTTransfer(TransposeModel):
     def __init__(self, _data: object):
         self.contract_address: str = None
         self.token_id: int = None
         self.block_number: int = None
         self.log_index: int = None
```

### Comparing `transpose_data-3.1.2/transpose_data.egg-info/PKG-INFO` & `transpose_data-4.0.0/transpose_data.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: transpose-data
-Version: 3.1.2
+Version: 4.0.0
 Summary: Web3 Data Made Simple. Powerful APIs for accessing human-readable blockchain data at scale: from blocks and transactions to NFTs and tokens.
 Home-page: https://github.com/TransposeData/transpose-python-sdk
 Author: Michael Calvey (michaeljohncalvey), Alex Langshur (alangshur), Jonathan Becker (jon-becker)
 Author-email: michael@transpose.io, alex@transpose.io, jon@transpose.io
 License: MIT
 Keywords: web3,data,ethereum,web3 data,ethereum data
 Classifier: Development Status :: 3 - Alpha
@@ -22,15 +22,15 @@
 # Welcome to the Transpose Python SDK
 ![Deployment Tests](https://github.com/TransposeData/transpose-python-sdk/actions/workflows/deployment_tests.yml/badge.svg) ![PyPI version](https://badge.fury.io/py/transpose-data.svg) ![Installations](https://img.shields.io/pypi/dd/transpose-data?color=g)
 
 A modern python wrapper for the Transpose API Suite.
 
 ## Getting an API Key
 
-To obtain a free Open Alpha Transpose API key, sign up on our [website](https://www.transpose.io/). API Keys are rate limited to 1 request per second and 100,000 requests per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord!
+To obtain a free Transpose API key, sign up on our [website](https://www.transpose.io/). Free tier keys have a rate limit of 1 request per second and 250,000 credits per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord or upgrade your tier directly in the webapp!
 
 Join our [Discord](https://discord.gg/AKguqp3U57) to ask technical questions, share what you're building, and chat with others in the community.
 
 ## Installation
 
 **Python 3.8 or higher is recommended**
 
@@ -40,20 +40,22 @@
 ```
 
 ---
 
 ## Documentation
 You can find specific documentation on a per-product basis below.
 
-|                                                                            Product                                                                            | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
-| :-----------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
-| <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628ebc9704701b4d5610ac1a_Blockchain_Logo_Solid.png" width="50" height="50"><br> Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
-|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628d465b6551e284a9ae73e4_Wallet_Logo_ENS.png" width="50" height="50"><br> ENS API     | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
-|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/6286795ef57a1412d6d767fc_NFT_Logo_Solid.png" width="50" height="50"><br> NFT API      | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
-|   <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628fb0f77f6279a920577119_Token_Logo2_Solid.png" width="50" height="50"><br>Token API    | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
+|  Product  | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
+| :-------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
+| Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
+|  ENS API  | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
+|  NFT API  | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
+| Token API | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
+| SQL API | The SQL API provides direct SQL access to our entire ecosystem of indexed blockchain data. Paired with our robust indexing pipeline, SQL access gives unlimited flexibility in how you mix, aggregate, and query activity across the blockchain.  | [SQL API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/sql.md) |
+| Endpoint API | The Endpoint API provides customized REST endpoints that you ca n create, version, and use directly in your production applications. | [Endpoint API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/endpoint.md) |
 
 ## SDK Documentation
 You can learn more about the Transpose SDK and how it works below.
 
 
 ### SDK Classes
 The Transpose SDK uses custom classes to represent API responses:
@@ -189,15 +191,15 @@
 | requests_per_second | No       | The number of requests per second to make                     | ``int``  |
 | results_to_fetch    | No       | The number of results to fetch                                | ``int``  |
 
 #### Responses
 | Code | Title                 | Model                                                                                                        |
 | ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
 | 200  | Success               | Data Model                                                                                                   |
-| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) 
+| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 401  | Unauthorized          | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 | 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
 
 Here is an example of how to use ``bulk_request``:
 
@@ -339,10 +341,11 @@
     "is_expired":false,
     "last_refreshed":"2022-06-01T09:51:23Z"
   }
 ]
 ```
 
 ## Links
+
 - [SDK Examples](https://github.com/TransposeData/transpose-python-sdk/tree/main/demo)
 - [Transpose Documentation](https://docs.transpose.io)
 - [Official Discord Server](https://discord.gg/AKguqp3U57)
```

### Comparing `transpose_data-3.1.2/transpose_data.egg-info/SOURCES.txt` & `transpose_data-4.0.0/transpose_data.egg-info/SOURCES.txt`

 * *Files 7% similar despite different names*

```diff
@@ -20,14 +20,16 @@
 transpose/src/api/block/_logs_by_block.py
 transpose/src/api/block/_logs_by_transaction.py
 transpose/src/api/block/_transactions_by_account.py
 transpose/src/api/block/_transactions_by_block.py
 transpose/src/api/block/_transactions_by_date.py
 transpose/src/api/block/_transactions_by_hash.py
 transpose/src/api/block/base.py
+transpose/src/api/endpoint/__init__.py
+transpose/src/api/endpoint/base.py
 transpose/src/api/ens/__init__.py
 transpose/src/api/ens/_records_by_account.py
 transpose/src/api/ens/_records_by_date.py
 transpose/src/api/ens/_records_by_name.py
 transpose/src/api/ens/_records_by_owner.py
 transpose/src/api/ens/_records_by_token_id.py
 transpose/src/api/ens/_transfers_by_name.py
@@ -50,14 +52,16 @@
 transpose/src/api/nft/_sales_by_contract_address.py
 transpose/src/api/nft/_sales_by_token_id.py
 transpose/src/api/nft/_transfers.py
 transpose/src/api/nft/_transfers_by_account.py
 transpose/src/api/nft/_transfers_by_contract_address.py
 transpose/src/api/nft/_transfers_by_token_id.py
 transpose/src/api/nft/base.py
+transpose/src/api/sql/__init__.py
+transpose/src/api/sql/base.py
 transpose/src/api/token/__init__.py
 transpose/src/api/token/_native_token_balances_by_account.py
 transpose/src/api/token/_native_token_transfers.py
 transpose/src/api/token/_native_token_transfers_by_account.py
 transpose/src/api/token/_owners_by_contract_address.py
 transpose/src/api/token/_swaps.py
 transpose/src/api/token/_swaps_by_account.py
```

