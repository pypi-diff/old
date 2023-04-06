# Comparing `tmp/sharingiscaring-0.2.8.tar.gz` & `tmp/sharingiscaring-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sharingiscaring-0.2.8.tar", last modified: Tue Apr  4 11:13:08 2023, max compression
+gzip compressed data, was "sharingiscaring-0.2.9.tar", last modified: Tue Apr  4 11:18:24 2023, max compression
```

## Comparing `sharingiscaring-0.2.8.tar` & `sharingiscaring-0.2.9.tar`

### file list

```diff
@@ -1,140 +1,140 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.806892 sharingiscaring-0.2.8/
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-04 11:13:08.806892 sharingiscaring-0.2.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-04 11:13:08.806892 sharingiscaring-0.2.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      806 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.782892 sharingiscaring-0.2.8/sharingiscaring/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.786892 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.786892 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/CCD_Types/
--rw-r--r--   0 runner    (1001) docker     (123)    31985 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/CCD_Types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5575 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.786892 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.786892 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/health/
--rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/health/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.786892 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/v2/
--rw-r--r--   0 runner    (1001) docker     (123)   221467 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/v2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1239 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/health_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3029 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/health_pb2_grpc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.790892 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/
--rw-r--r--   0 runner    (1001) docker     (123)    11045 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetAccountInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetAccountList.py
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetAnonymityRevokers.py
--rw-r--r--   0 runner    (1001) docker     (123)      959 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBakerList.py
--rw-r--r--   0 runner    (1001) docker     (123)     6922 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockChainParameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     5380 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockPendingUpdates.py
--rw-r--r--   0 runner    (1001) docker     (123)     4666 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockSpecialEvents.py
--rw-r--r--   0 runner    (1001) docker     (123)    34853 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockTransactionEvents.py
--rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlocksAtHeight.py
--rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetElectionInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetFinalizedBlocks.py
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetIdentityProviders.py
--rw-r--r--   0 runner    (1001) docker     (123)     2745 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetInstanceInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)      979 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetInstanceList.py
--rw-r--r--   0 runner    (1001) docker     (123)     2598 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetModuleSource.py
--rw-r--r--   0 runner    (1001) docker     (123)     1491 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPassiveDelegationInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPassiveDelegators.py
--rw-r--r--   0 runner    (1001) docker     (123)     1331 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPassiveDelegatorsRewardPeriod.py
--rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPoolDelegators.py
--rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPoolDelegatorsRewardPeriod.py
--rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPoolInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     2620 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetTokenomicsInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)    23824 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_SharedConverters.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    84238 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)   105670 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/types_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/types_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    13038 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/GRPCClient/wadze.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3636 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/account.py
--rw-r--r--   0 runner    (1001) docker     (123)     1031 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/block.py
--rw-r--r--   0 runner    (1001) docker     (123)     2644 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.794892 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13433 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_accountByAddress.py
--rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_accounts.py
--rw-r--r--   0 runner    (1001) docker     (123)     5160 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_bakerByBakerId.py
--rw-r--r--   0 runner    (1001) docker     (123)     5638 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_bakers.py
--rw-r--r--   0 runner    (1001) docker     (123)    20212 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_blockByBlockHash.py
--rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_blocks.py
--rw-r--r--   0 runner    (1001) docker     (123)     3277 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_passiveDelegation.py
--rw-r--r--   0 runner    (1001) docker     (123)     5258 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_paydayStatus.py
--rw-r--r--   0 runner    (1001) docker     (123)     1800 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_poolRewardMetricsForBakerPool.py
--rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_poolRewardMetricsForPassiveDelegation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2326 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_rewardMetricsForAccount.py
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_search.py
--rw-r--r--   0 runner    (1001) docker     (123)      828 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_transactionByTransactionHash.py
--rw-r--r--   0 runner    (1001) docker     (123)      964 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_transactionMetrics.py
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/enums.py
--rw-r--r--   0 runner    (1001) docker     (123)     5260 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/exchange_account_updates.py
--rw-r--r--   0 runner    (1001) docker     (123)     3109 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/ql_support.py
--rw-r--r--   0 runner    (1001) docker     (123)    16041 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/client.py
--rw-r--r--   0 runner    (1001) docker     (123)    16275 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/cns.py
--rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/credential.py
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/enums.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.798892 sharingiscaring-0.2.8/sharingiscaring/grpcclient/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.798892 sharingiscaring-0.2.8/sharingiscaring/grpcclient/CCD_Types/
--rw-r--r--   0 runner    (1001) docker     (123)    31985 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/CCD_Types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5575 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.798892 sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.798892 sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/health/
--rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/health/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.798892 sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/v2/
--rw-r--r--   0 runner    (1001) docker     (123)   221467 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/v2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1239 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/health_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3029 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/health_pb2_grpc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.802892 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/
--rw-r--r--   0 runner    (1001) docker     (123)    11045 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetAccountInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetAccountList.py
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetAnonymityRevokers.py
--rw-r--r--   0 runner    (1001) docker     (123)      959 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBakerList.py
--rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     5380 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockPendingUpdates.py
--rw-r--r--   0 runner    (1001) docker     (123)     4666 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockSpecialEvents.py
--rw-r--r--   0 runner    (1001) docker     (123)    34853 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockTransactionEvents.py
--rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlocksAtHeight.py
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetFinalizedBlocks.py
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetIdentityProviders.py
--rw-r--r--   0 runner    (1001) docker     (123)     2745 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetInstanceInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)      979 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetInstanceList.py
--rw-r--r--   0 runner    (1001) docker     (123)     1491 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPassiveDelegationInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPassiveDelegators.py
--rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPoolDelegators.py
--rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPoolDelegatorsRewardPeriod.py
--rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPoolInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)     2620 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetTokenomicsInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)    23824 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_SharedConverters.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/service_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)    84238 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/service_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)   105670 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/types_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/grpcclient/types_pb2_grpc.py
--rw-r--r--   0 runner    (1001) docker     (123)    11575 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/mongodb.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.806892 sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13285 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_apy_calculations.py
--rw-r--r--   0 runner    (1001) docker     (123)      512 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_baker_distributions.py
--rw-r--r--   0 runner    (1001) docker     (123)    17563 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_search_transfers.py
--rw-r--r--   0 runner    (1001) docker     (123)    14572 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_store_block.py
--rw-r--r--   0 runner    (1001) docker     (123)     1351 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_subscriptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1665 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/node.py
--rw-r--r--   0 runner    (1001) docker     (123)     1860 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)      203 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/rewards.py
--rw-r--r--   0 runner    (1001) docker     (123)     3159 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/tooter.py
--rw-r--r--   0 runner    (1001) docker     (123)    45046 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/transaction.py
--rw-r--r--   0 runner    (1001) docker     (123)    13833 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/sharingiscaring/user.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.782892 sharingiscaring-0.2.8/sharingiscaring.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-04 11:13:08.000000 sharingiscaring-0.2.8/sharingiscaring.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5663 2023-04-04 11:13:08.000000 sharingiscaring-0.2.8/sharingiscaring.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 11:13:08.000000 sharingiscaring-0.2.8/sharingiscaring.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-04 11:13:08.000000 sharingiscaring-0.2.8/sharingiscaring.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-04 11:13:08.000000 sharingiscaring-0.2.8/sharingiscaring.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:13:08.806892 sharingiscaring-0.2.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/tests/test_namehash.py
--rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/tests/test_pool.py
--rw-r--r--   0 runner    (1001) docker     (123)     6803 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/tests/test_txs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4444 2023-04-04 11:12:51.000000 sharingiscaring-0.2.8/tests/test_user.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.884919 sharingiscaring-0.2.9/
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-04 11:18:24.884919 sharingiscaring-0.2.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-04 11:18:24.884919 sharingiscaring-0.2.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      806 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.868919 sharingiscaring-0.2.9/sharingiscaring/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.872919 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.872919 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/CCD_Types/
+-rw-r--r--   0 runner    (1001) docker     (123)    31985 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/CCD_Types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5575 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.872919 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.872919 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/health/
+-rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/health/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.872919 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/v2/
+-rw-r--r--   0 runner    (1001) docker     (123)   221467 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/v2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1239 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/health_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3029 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/health_pb2_grpc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.876919 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/
+-rw-r--r--   0 runner    (1001) docker     (123)    11045 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetAccountInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetAccountList.py
+-rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetAnonymityRevokers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      959 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBakerList.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6922 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockChainParameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5380 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockPendingUpdates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4666 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockSpecialEvents.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34853 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockTransactionEvents.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlocksAtHeight.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetElectionInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1141 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetFinalizedBlocks.py
+-rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetIdentityProviders.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2745 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetInstanceInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      979 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetInstanceList.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2598 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetModuleSource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1491 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPassiveDelegationInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPassiveDelegators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1342 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPassiveDelegatorsRewardPeriod.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPoolDelegators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPoolDelegatorsRewardPeriod.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPoolInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2620 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetTokenomicsInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23824 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_SharedConverters.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    84238 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)   105670 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/types_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/types_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13038 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/GRPCClient/wadze.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3636 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/account.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1031 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/block.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2644 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.876919 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13433 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_accountByAddress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_accounts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5160 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_bakerByBakerId.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5638 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_bakers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20212 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_blockByBlockHash.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_blocks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3277 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_passiveDelegation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5258 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_paydayStatus.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1800 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_poolRewardMetricsForBakerPool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_poolRewardMetricsForPassiveDelegation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2326 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_rewardMetricsForAccount.py
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)      828 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_transactionByTransactionHash.py
+-rw-r--r--   0 runner    (1001) docker     (123)      964 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_transactionMetrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5260 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/exchange_account_updates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3109 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/ql_support.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16041 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16275 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/cns.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/credential.py
+-rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/enums.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.880919 sharingiscaring-0.2.9/sharingiscaring/grpcclient/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.880919 sharingiscaring-0.2.9/sharingiscaring/grpcclient/CCD_Types/
+-rw-r--r--   0 runner    (1001) docker     (123)    31985 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/CCD_Types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5575 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.880919 sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.880919 sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/health/
+-rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/health/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.880919 sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/v2/
+-rw-r--r--   0 runner    (1001) docker     (123)   221467 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/v2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1239 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/health_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3029 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/health_pb2_grpc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.880919 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/
+-rw-r--r--   0 runner    (1001) docker     (123)    11045 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetAccountInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetAccountList.py
+-rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetAnonymityRevokers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      959 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBakerList.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5380 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockPendingUpdates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4666 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockSpecialEvents.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34853 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockTransactionEvents.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlocksAtHeight.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1141 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetFinalizedBlocks.py
+-rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetIdentityProviders.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2745 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetInstanceInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      979 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetInstanceList.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1491 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPassiveDelegationInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPassiveDelegators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPoolDelegators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPoolDelegatorsRewardPeriod.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPoolInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2620 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetTokenomicsInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23824 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_SharedConverters.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/service_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    84238 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/service_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)   105670 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/types_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/grpcclient/types_pb2_grpc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11575 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/mongodb.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.884919 sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13285 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_apy_calculations.py
+-rw-r--r--   0 runner    (1001) docker     (123)      512 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_baker_distributions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17563 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_search_transfers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14572 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_store_block.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1351 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_subscriptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1665 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/node.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1860 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)      203 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/rewards.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3159 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/tooter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45046 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/transaction.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13833 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/sharingiscaring/user.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.868919 sharingiscaring-0.2.9/sharingiscaring.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-04 11:18:24.000000 sharingiscaring-0.2.9/sharingiscaring.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5663 2023-04-04 11:18:24.000000 sharingiscaring-0.2.9/sharingiscaring.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 11:18:24.000000 sharingiscaring-0.2.9/sharingiscaring.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-04 11:18:24.000000 sharingiscaring-0.2.9/sharingiscaring.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-04 11:18:24.000000 sharingiscaring-0.2.9/sharingiscaring.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:24.884919 sharingiscaring-0.2.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/tests/test_namehash.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/tests/test_pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6803 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/tests/test_txs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4444 2023-04-04 11:18:13.000000 sharingiscaring-0.2.9/tests/test_user.py
```

### Comparing `sharingiscaring-0.2.8/setup.py` & `sharingiscaring-0.2.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 
 setup(
     name="sharingiscaring",
-    version="0.2.8",
+    version="0.2.9",
     author="Sander de Ruiter",
     author_email="sdr@concordium-explorer.nl",
     description="Shared code for Concordium Explorer (Bot)",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/sderuiter/sharingiscaring",
     project_urls={},
```

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/CCD_Types/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/CCD_Types/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/health/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/health/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/concordium/v2/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/concordium/v2/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/health_pb2.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/health_pb2.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/health_pb2_grpc.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/health_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetAccountInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetAccountInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetAccountList.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetAccountList.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetAnonymityRevokers.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetAnonymityRevokers.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBakerList.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBakerList.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockChainParameters.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockChainParameters.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockPendingUpdates.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockPendingUpdates.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockSpecialEvents.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockSpecialEvents.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlockTransactionEvents.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlockTransactionEvents.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetBlocksAtHeight.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetBlocksAtHeight.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetElectionInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetElectionInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetFinalizedBlocks.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetFinalizedBlocks.py`

 * *Files 7% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 from sharingiscaring.GRPCClient.types_pb2 import *
 from sharingiscaring.GRPCClient.service_pb2_grpc import QueriesStub
 from sharingiscaring.GRPCClient.queries._SharedConverters import (
     Mixin as _SharedConverters,
 )
 from typing import Iterator
 from typing import TYPE_CHECKING
+import sys
 
 if TYPE_CHECKING:
     from sharingiscaring.GRPCClient import GRPCClient
 from sharingiscaring.GRPCClient.CCD_Types import *
 from rich import print
```

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetIdentityProviders.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetIdentityProviders.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetInstanceInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetInstanceInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetInstanceList.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetInstanceList.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetModuleSource.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetModuleSource.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPassiveDelegationInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPassiveDelegationInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPassiveDelegators.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPassiveDelegators.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPassiveDelegatorsRewardPeriod.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPassiveDelegatorsRewardPeriod.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,14 +3,15 @@
 from sharingiscaring.GRPCClient.service_pb2_grpc import QueriesStub
 from sharingiscaring.GRPCClient.queries._SharedConverters import (
     Mixin as _SharedConverters,
 )
 from typing import Iterator
 from sharingiscaring.GRPCClient.CCD_Types import CCD_DelegatorRewardPeriodInfo
 from typing import TYPE_CHECKING
+import sys
 
 if TYPE_CHECKING:
     from sharingiscaring.GRPCClient import GRPCClient
 
 
 class Mixin(_SharedConverters):
     def get_delegators_for_passive_delegation_in_reward_period(
```

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPoolDelegators.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPoolDelegators.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPoolDelegatorsRewardPeriod.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPoolDelegatorsRewardPeriod.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetPoolInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetPoolInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_GetTokenomicsInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_GetTokenomicsInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/queries/_SharedConverters.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/queries/_SharedConverters.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/service_pb2.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/service_pb2.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/service_pb2_grpc.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/types_pb2.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/types_pb2.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/GRPCClient/wadze.py` & `sharingiscaring-0.2.9/sharingiscaring/GRPCClient/wadze.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/account.py` & `sharingiscaring-0.2.9/sharingiscaring/account.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/block.py` & `sharingiscaring-0.2.9/sharingiscaring/block.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_accountByAddress.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_accountByAddress.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_accounts.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_accounts.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_bakerByBakerId.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_bakerByBakerId.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_bakers.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_bakers.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_blockByBlockHash.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_blockByBlockHash.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_blocks.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_blocks.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_passiveDelegation.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_passiveDelegation.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_paydayStatus.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_paydayStatus.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_poolRewardMetricsForBakerPool.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_poolRewardMetricsForBakerPool.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_poolRewardMetricsForPassiveDelegation.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_poolRewardMetricsForPassiveDelegation.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_rewardMetricsForAccount.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_rewardMetricsForAccount.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_search.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_search.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_transactionByTransactionHash.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_transactionByTransactionHash.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/_transactionMetrics.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/_transactionMetrics.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/exchange_account_updates.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/exchange_account_updates.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/ccdscan_queries/ql_support.py` & `sharingiscaring-0.2.9/sharingiscaring/ccdscan_queries/ql_support.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/client.py` & `sharingiscaring-0.2.9/sharingiscaring/client.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/cns.py` & `sharingiscaring-0.2.9/sharingiscaring/cns.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/credential.py` & `sharingiscaring-0.2.9/sharingiscaring/credential.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/CCD_Types/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/CCD_Types/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/health/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/health/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/concordium/v2/__init__.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/concordium/v2/__init__.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/health_pb2.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/health_pb2.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/health_pb2_grpc.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/health_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetAccountInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetAccountInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetAccountList.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetAccountList.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetAnonymityRevokers.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetAnonymityRevokers.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBakerList.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBakerList.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockPendingUpdates.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockPendingUpdates.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockSpecialEvents.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockSpecialEvents.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlockTransactionEvents.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlockTransactionEvents.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetBlocksAtHeight.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetBlocksAtHeight.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetFinalizedBlocks.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetFinalizedBlocks.py`

 * *Files 7% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 from sharingiscaring.GRPCClient.types_pb2 import *
 from sharingiscaring.GRPCClient.service_pb2_grpc import QueriesStub
 from sharingiscaring.GRPCClient.queries._SharedConverters import (
     Mixin as _SharedConverters,
 )
 from typing import Iterator
 from typing import TYPE_CHECKING
+import sys
 
 if TYPE_CHECKING:
     from sharingiscaring.GRPCClient import GRPCClient
 from sharingiscaring.GRPCClient.CCD_Types import *
 from rich import print
```

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetIdentityProviders.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetIdentityProviders.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetInstanceInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetInstanceInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetInstanceList.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetInstanceList.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPassiveDelegationInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPassiveDelegationInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPassiveDelegators.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPassiveDelegators.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPoolDelegators.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPoolDelegators.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPoolDelegatorsRewardPeriod.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPoolDelegatorsRewardPeriod.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetPoolInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetPoolInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_GetTokenomicsInfo.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_GetTokenomicsInfo.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/queries/_SharedConverters.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/queries/_SharedConverters.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/service_pb2.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/service_pb2.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/service_pb2_grpc.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/grpcclient/types_pb2.py` & `sharingiscaring-0.2.9/sharingiscaring/grpcclient/types_pb2.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/mongodb.py` & `sharingiscaring-0.2.9/sharingiscaring/mongodb.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_apy_calculations.py` & `sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_apy_calculations.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_baker_distributions.py` & `sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_baker_distributions.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_search_transfers.py` & `sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_search_transfers.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_store_block.py` & `sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_store_block.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/mongodb_queries/_subscriptions.py` & `sharingiscaring-0.2.9/sharingiscaring/mongodb_queries/_subscriptions.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/node.py` & `sharingiscaring-0.2.9/sharingiscaring/node.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/pool.py` & `sharingiscaring-0.2.9/sharingiscaring/pool.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/tooter.py` & `sharingiscaring-0.2.9/sharingiscaring/tooter.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/transaction.py` & `sharingiscaring-0.2.9/sharingiscaring/transaction.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring/user.py` & `sharingiscaring-0.2.9/sharingiscaring/user.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/sharingiscaring.egg-info/SOURCES.txt` & `sharingiscaring-0.2.9/sharingiscaring.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/tests/test_pool.py` & `sharingiscaring-0.2.9/tests/test_pool.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/tests/test_txs.py` & `sharingiscaring-0.2.9/tests/test_txs.py`

 * *Files identical despite different names*

### Comparing `sharingiscaring-0.2.8/tests/test_user.py` & `sharingiscaring-0.2.9/tests/test_user.py`

 * *Files identical despite different names*

