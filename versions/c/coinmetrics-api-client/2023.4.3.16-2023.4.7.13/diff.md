# Comparing `tmp/coinmetrics_api_client-2023.4.3.16.tar.gz` & `tmp/coinmetrics_api_client-2023.4.7.13.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "coinmetrics_api_client-2023.4.3.16.tar", max compression
+gzip compressed data, was "coinmetrics_api_client-2023.4.7.13.tar", max compression
```

## Comparing `coinmetrics_api_client-2023.4.3.16.tar` & `coinmetrics_api_client-2023.4.7.13.tar`

### file list

```diff
@@ -1,39 +1,39 @@
--rw-r--r--   0        0        0     1088 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/LICENSE
--rw-r--r--   0        0        0    20460 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/README.md
--rw-r--r--   0        0        0       28 2023-04-03 18:18:14.308331 coinmetrics_api_client-2023.4.3.16/coinmetrics/__init__.py
--rw-r--r--   0        0        0    19494 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/coinmetrics/_catalogs.py
--rw-r--r--   0        0        0     8811 2023-04-03 15:19:14.595248 coinmetrics_api_client-2023.4.3.16/coinmetrics/_data_collection.py
--rw-r--r--   0        0        0     2328 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/coinmetrics/_exceptions.py
--rw-r--r--   0        0        0      699 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/coinmetrics/_typing.py
--rw-r--r--   0        0        0     3951 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/coinmetrics/_utils.py
--rw-r--r--   0        0        0   212756 2023-04-03 15:19:14.595248 coinmetrics_api_client-2023.4.3.16/coinmetrics/api_client.py
--rw-r--r--   0        0        0        0 2023-04-03 18:18:14.352331 coinmetrics_api_client-2023.4.3.16/coinmetrics/build.py
--rw-r--r--   0        0        0      148 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/coinmetrics/constants.py
--rw-r--r--   0        0        0    20520 2023-03-15 19:05:17.301418 coinmetrics_api_client-2023.4.3.16/coinmetrics/data_exporter.py
--rw-r--r--   0        0        0     8669 2023-03-08 17:11:59.698291 coinmetrics_api_client-2023.4.3.16/coinmetrics/typer_cli.py
--rw-r--r--   0        0        0     1236 2023-04-03 18:18:14.316331 coinmetrics_api_client-2023.4.3.16/pyproject.toml
--rw-r--r--   0        0        0        0 2023-04-03 18:18:14.360331 coinmetrics_api_client-2023.4.3.16/test/__init__.py
--rw-r--r--   0        0        0     1640 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_asset_pair_candles.csv
--rw-r--r--   0        0        0      412 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_asset_pairs.csv
--rw-r--r--   0        0        0     2097 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_assets_markets.csv
--rw-r--r--   0        0        0      605 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_assets_metrics.csv
--rw-r--r--   0        0        0      436 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_exchange_assets.csv
--rw-r--r--   0        0        0     3595 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_exchanges_markets.csv
--rw-r--r--   0        0        0      822 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_exchanges_metrics.csv
--rw-r--r--   0        0        0      556 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_indexes.csv
--rw-r--r--   0        0        0      223 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_institutions.csv
--rw-r--r--   0        0        0      178 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_market_orderbooks.csv
--rw-r--r--   0        0        0      254 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_market_quotes.csv
--rw-r--r--   0        0        0      297 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_market_trades.csv
--rw-r--r--   0        0        0      579 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_markets.csv
--rw-r--r--   0        0        0     2557 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/data/catalog_metrics.csv
--rw-r--r--   0        0        0    28915 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/test_api_client.py
--rw-r--r--   0        0        0    10311 2023-04-03 15:27:12.753395 coinmetrics_api_client-2023.4.3.16/test/test_api_methods.py
--rw-r--r--   0        0        0     2910 2023-03-15 19:17:25.360472 coinmetrics_api_client-2023.4.3.16/test/test_as_list.py
--rw-r--r--   0        0        0      973 2023-04-03 15:27:12.753395 coinmetrics_api_client-2023.4.3.16/test/test_blockchain_methods.py
--rw-r--r--   0        0        0     2273 2023-03-08 17:11:59.718292 coinmetrics_api_client-2023.4.3.16/test/test_custom_exceptions.py
--rw-r--r--   0        0        0    13462 2023-03-08 17:11:59.722292 coinmetrics_api_client-2023.4.3.16/test/test_data_exporter.py
--rw-r--r--   0        0        0     1015 2023-03-08 17:11:59.722292 coinmetrics_api_client-2023.4.3.16/test/test_debugging.py
--rw-r--r--   0        0        0    11173 2023-03-08 17:11:59.722292 coinmetrics_api_client-2023.4.3.16/test/test_to_dataframe.py
--rw-r--r--   0        0        0     5783 2023-04-03 15:19:14.595248 coinmetrics_api_client-2023.4.3.16/test/test_websocket_methods.py
--rw-r--r--   0        0        0    21648 1970-01-01 00:00:00.000000 coinmetrics_api_client-2023.4.3.16/PKG-INFO
+-rw-r--r--   0        0        0     1088 2023-03-13 17:44:25.880253 coinmetrics_api_client-2023.4.7.13/LICENSE
+-rw-r--r--   0        0        0    20460 2023-03-13 17:44:25.880253 coinmetrics_api_client-2023.4.7.13/README.md
+-rw-r--r--   0        0        0       28 2023-04-07 13:55:31.202856 coinmetrics_api_client-2023.4.7.13/coinmetrics/__init__.py
+-rw-r--r--   0        0        0    19494 2023-03-13 17:44:25.880253 coinmetrics_api_client-2023.4.7.13/coinmetrics/_catalogs.py
+-rw-r--r--   0        0        0     8811 2023-04-07 13:55:31.202856 coinmetrics_api_client-2023.4.7.13/coinmetrics/_data_collection.py
+-rw-r--r--   0        0        0     2328 2023-03-13 17:44:25.884253 coinmetrics_api_client-2023.4.7.13/coinmetrics/_exceptions.py
+-rw-r--r--   0        0        0      699 2023-03-13 17:44:25.884253 coinmetrics_api_client-2023.4.7.13/coinmetrics/_typing.py
+-rw-r--r--   0        0        0     3951 2023-03-13 17:44:25.884253 coinmetrics_api_client-2023.4.7.13/coinmetrics/_utils.py
+-rw-r--r--   0        0        0   219839 2023-04-07 13:55:31.202856 coinmetrics_api_client-2023.4.7.13/coinmetrics/api_client.py
+-rw-r--r--   0        0        0        0 2023-04-07 13:55:31.234856 coinmetrics_api_client-2023.4.7.13/coinmetrics/build.py
+-rw-r--r--   0        0        0      148 2023-03-13 17:44:25.884253 coinmetrics_api_client-2023.4.7.13/coinmetrics/constants.py
+-rw-r--r--   0        0        0    20520 2023-03-15 18:43:04.977129 coinmetrics_api_client-2023.4.7.13/coinmetrics/data_exporter.py
+-rw-r--r--   0        0        0     8669 2023-03-13 17:44:25.884253 coinmetrics_api_client-2023.4.7.13/coinmetrics/typer_cli.py
+-rw-r--r--   0        0        0     1236 2023-04-07 13:55:31.206856 coinmetrics_api_client-2023.4.7.13/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-07 13:55:31.246857 coinmetrics_api_client-2023.4.7.13/test/__init__.py
+-rw-r--r--   0        0        0     1640 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_asset_pair_candles.csv
+-rw-r--r--   0        0        0      412 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_asset_pairs.csv
+-rw-r--r--   0        0        0     2097 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_assets_markets.csv
+-rw-r--r--   0        0        0      605 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_assets_metrics.csv
+-rw-r--r--   0        0        0      436 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_exchange_assets.csv
+-rw-r--r--   0        0        0     3595 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_exchanges_markets.csv
+-rw-r--r--   0        0        0      822 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_exchanges_metrics.csv
+-rw-r--r--   0        0        0      556 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_indexes.csv
+-rw-r--r--   0        0        0      223 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_institutions.csv
+-rw-r--r--   0        0        0      178 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_market_orderbooks.csv
+-rw-r--r--   0        0        0      254 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_market_quotes.csv
+-rw-r--r--   0        0        0      297 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_market_trades.csv
+-rw-r--r--   0        0        0      579 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_markets.csv
+-rw-r--r--   0        0        0     2557 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/data/catalog_metrics.csv
+-rw-r--r--   0        0        0    28915 2023-03-13 17:44:25.900253 coinmetrics_api_client-2023.4.7.13/test/test_api_client.py
+-rw-r--r--   0        0        0    10311 2023-04-07 13:55:31.206856 coinmetrics_api_client-2023.4.7.13/test/test_api_methods.py
+-rw-r--r--   0        0        0     2910 2023-03-15 19:40:48.344687 coinmetrics_api_client-2023.4.7.13/test/test_as_list.py
+-rw-r--r--   0        0        0     1788 2023-04-07 13:55:31.206856 coinmetrics_api_client-2023.4.7.13/test/test_blockchain_methods.py
+-rw-r--r--   0        0        0     2273 2023-03-13 17:44:25.904253 coinmetrics_api_client-2023.4.7.13/test/test_custom_exceptions.py
+-rw-r--r--   0        0        0    13462 2023-03-13 17:44:25.904253 coinmetrics_api_client-2023.4.7.13/test/test_data_exporter.py
+-rw-r--r--   0        0        0     1015 2023-03-13 17:44:25.904253 coinmetrics_api_client-2023.4.7.13/test/test_debugging.py
+-rw-r--r--   0        0        0    11173 2023-03-13 17:44:25.904253 coinmetrics_api_client-2023.4.7.13/test/test_to_dataframe.py
+-rw-r--r--   0        0        0     5783 2023-04-07 13:55:31.206856 coinmetrics_api_client-2023.4.7.13/test/test_websocket_methods.py
+-rw-r--r--   0        0        0    21648 1970-01-01 00:00:00.000000 coinmetrics_api_client-2023.4.7.13/PKG-INFO
```

### Comparing `coinmetrics_api_client-2023.4.3.16/LICENSE` & `coinmetrics_api_client-2023.4.7.13/LICENSE`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/README.md` & `coinmetrics_api_client-2023.4.7.13/README.md`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/_catalogs.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/_catalogs.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/_data_collection.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/_data_collection.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/_exceptions.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/_exceptions.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/_typing.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/_typing.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/_utils.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/_utils.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/api_client.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/api_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -3847,14 +3847,40 @@
             List[Dict[str, Any]],
             self._get_data(
                 f"blockchain/{asset}/blocks/{block_hash}/transactions/{txid}",
                 params,
             ),
         )
 
+    def get_full_block(
+            self,
+            asset: str,
+            block_hash: str,
+    ) -> Dict[str, Any]:
+        """
+        :param asset: Asset name.
+        :type asset: str
+        :param block_hash: Block hash.
+        :type block_hash: str
+
+        :return: Blockchain full block.
+        :rtype: Dict[str, Any]
+        """
+        params: Dict[str, Any] = {
+            "asset": asset,
+            "block_hash": block_hash,
+        }
+        return cast(
+            Dict[str, Any],
+            self._get_data(
+                f"blockchain/{asset}/blocks/{block_hash}",
+                params,
+            ),
+        )
+
     def get_full_block_v2(
         self, asset: str, block_hash: str, include_sub_accounts: Optional[bool]
     ) -> List[Dict[str, Any]]:
         """
         Returns a full blockchain block with all transactions and balance updates.
 
         :param asset: Asset name
@@ -3956,14 +3982,102 @@
             List[Dict[str, Any]],
             self._get_data(
                 f"blockchain-v2/{asset}/blocks/{block_hash}/transactions/{txid}",
                 params,
             ),
         )
 
+    def get_list_of_balance_updates_for_account_v2(
+            self,
+            asset: str,
+            account: str,
+            txids: Optional[Union[str, List[str]]] = None,
+            block_hashes: Optional[Union[str, List[str]]] = None,
+            include_counterparties: Optional[bool] = None,
+            start_time: Optional[Union[datetime, date, str]] = None,
+            end_time: Optional[Union[datetime, date, str]] = None,
+            start_height: Optional[int] = None,
+            end_height: Optional[int] = None,
+            start_chain_sequence_number: Optional[int] = None,
+            end_chain_sequence_number: Optional[int] = None,
+            include_sub_accounts: Optional[bool] = None,
+            chain: Optional[str] = None,
+            start_inclusive: Optional[bool] = None,
+            end_inclusive: Optional[bool] = None,
+            timezone: Optional[str] = None,
+            page_size: Optional[int] = None,
+            paging_from: Optional[str] = None,
+            next_page_token: Optional[str] = None,
+    ) -> DataCollection:
+        """
+        :param asset: Asset name.
+        :type asset: Optional[str]
+        :param account: Account id.
+        :type account: Optional[str]
+        :param txids: Optional comma separated list of transaction identifiers (txid) to filter a response. The list must contain a single element for Community users.
+        :type txids: Union[str, List[str]]
+        :param block_hashes: Optional comma separated list of block hashes to filter a response. The list must contain a single element for Community users.
+        :type block_hashes: Union[str, List[str]]
+        :param include_counterparties: Include information about the counterparties balance updates.
+        :type include_counterparties: bool
+        :param start_time: Start of the time interval. This field refers to the `time` field in the response. Multiple formats of ISO 8601 are supported: `2006-01-20T00:00:00Z`, `2006-01-20T00:00:00.000Z`, `2006-01-20T00:00:00.123456Z`, `2006-01-20T00:00:00.123456789Z`, `2006-01-20`, `20060120`. Inclusive by default. Mutually exclusive with `start_height`. UTC timezone by default. `Z` suffix is optional and `timezone` parameter has a priority over it. If `start_time` is omitted, response will include time series from the **earliest** time available. This parameter is disabled for Community users.
+        :type start_time: str
+        :param end_time: End of the time interval. This field refers to the `time` field in the response. Multiple formats of ISO 8601 are supported: `2006-01-20T00:00:00Z`, `2006-01-20T00:00:00.000Z`, `2006-01-20T00:00:00.123456Z`, `2006-01-20T00:00:00.123456789Z`, `2006-01-20`, `20060120`. Inclusive by default. Mutually exclusive with `end_height`. UTC timezone by default. `Z` suffix is optional and `timezone` parameter has a priority over it. If `end_time` is omitted, response will include time series up to the **latest** time available. This parameter is disabled for Community users.
+        :type end_time: str
+        :param start_height: The start height indicates the beginning block height for the set of data that are returned. Inclusive by default. Mutually exclusive with `start_time`. This parameter is disabled for Community users.
+        :type start_height: int
+        :param end_height: The end height indicates the ending block height for the set of data that are returned. Inclusive by default. Mutually exclusive with `end_time`. This parameter is disabled for Community users.
+        :type end_height: int
+        :param start_chain_sequence_number: Start of the `chain_sequence_number` interval. This parameter is disabled for Community users.
+        :type start_chain_sequence_number: int
+        :param end_chain_sequence_number: End of the `chain_sequence_number` interval. This parameter is disabled for Community users.
+        :type end_chain_sequence_number: int
+        :param include_sub_accounts: Boolean indicating if the response should contain sub-accounts. This parameter is disabled for Community users.
+        :type include_sub_accounts: bool
+        :param chain: Chain type. Supported values are `main` and `all` (includes both main and stale). This parameter is disabled for Community users.
+        :type chain: str
+        :param start_inclusive: Inclusive or exclusive corresponding `start_*` parameters. This parameter is disabled for Community users.
+        :type start_inclusive: bool
+        :param end_inclusive: Inclusive or exclusive corresponding `end_*` parameters. This parameter is disabled for Community users.
+        :type end_inclusive: bool
+        :param timezone: Timezone name for `start_time` and `end_time` timestamps. This parameter does not modify the output times, which are always `UTC`. Format is defined by TZ database.
+        :type timezone: str
+        :param page_size: Number of items per single page of results. This parameter is disabled for Community users.
+        :type page_size: int
+        :param paging_from: Where does the first page start, at the start of the interval or at the end.
+        :type paging_from: str
+        :param next_page_token: Token for receiving the results from the next page of a query. Should not be used directly. To iterate through pages just use `next_page_url` response field.
+        :type next_page_token: str
+
+        :return: Blockchain balance updates for account.
+        :rtype: DataCollection
+        """
+        params: Dict[str, Any] = {
+            "asset": asset,
+            "account": account,
+            "txids": txids,
+            "block_hashes": block_hashes,
+            "include_counterparties": include_counterparties,
+            "start_time": start_time,
+            "end_time": end_time,
+            "start_height": start_height,
+            "end_height": end_height,
+            "start_chain_sequence_number": start_chain_sequence_number,
+            "end_chain_sequence_number": end_chain_sequence_number,
+            "include_sub_accounts": include_sub_accounts,
+            "chain": chain,
+            "start_inclusive": start_inclusive,
+            "end_inclusive": end_inclusive,
+            "timezone": timezone,
+            "page_size": page_size,
+            "paging_from": paging_from,
+            "next_page_token": next_page_token,
+        }
+        return DataCollection(self._get_data, f"/blockchain-v2/{asset}/accounts/{account}/balance-updates", params)
+
     def get_transaction_tracker(
         self,
         asset: str,
         txids: Optional[Union[List[str], str]] = None,
         replacements_for_txids: Optional[Union[List[str], str]] = None,
         replacements_only: Optional[bool] = None,
         page_size: Optional[int] = None,
```

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/data_exporter.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/data_exporter.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/coinmetrics/typer_cli.py` & `coinmetrics_api_client-2023.4.7.13/coinmetrics/typer_cli.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/pyproject.toml` & `coinmetrics_api_client-2023.4.7.13/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "coinmetrics-api-client"
-version = "2023.4.3.16"
+version = "2023.4.7.13"
 description = "Python client for Coin Metrics API v4."
 authors = ["Coin Metrics <info@coinmetrics.io>", "Oleksandr Buchkovskyi <oleksandr@coinmetrics.io>"]
 license = "MIT"
 readme = "README.md"
 homepage = "https://coinmetrics.github.io/api-client-python/site/index.html"
 repository = "https://github.com/coinmetrics/api-client-python"
 packages = [{include = "coinmetrics"}]
```

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_asset_pair_candles.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_asset_pair_candles.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_assets_markets.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_assets_markets.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_assets_metrics.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_assets_metrics.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_exchanges_markets.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_exchanges_markets.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_exchanges_metrics.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_exchanges_metrics.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_indexes.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_indexes.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_markets.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_markets.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/data/catalog_metrics.csv` & `coinmetrics_api_client-2023.4.7.13/test/data/catalog_metrics.csv`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_api_client.py` & `coinmetrics_api_client-2023.4.7.13/test/test_api_client.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_api_methods.py` & `coinmetrics_api_client-2023.4.7.13/test/test_api_methods.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_as_list.py` & `coinmetrics_api_client-2023.4.7.13/test/test_as_list.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_custom_exceptions.py` & `coinmetrics_api_client-2023.4.7.13/test/test_custom_exceptions.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_data_exporter.py` & `coinmetrics_api_client-2023.4.7.13/test/test_data_exporter.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_debugging.py` & `coinmetrics_api_client-2023.4.7.13/test/test_debugging.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_to_dataframe.py` & `coinmetrics_api_client-2023.4.7.13/test/test_to_dataframe.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/test/test_websocket_methods.py` & `coinmetrics_api_client-2023.4.7.13/test/test_websocket_methods.py`

 * *Files identical despite different names*

### Comparing `coinmetrics_api_client-2023.4.3.16/PKG-INFO` & `coinmetrics_api_client-2023.4.7.13/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coinmetrics-api-client
-Version: 2023.4.3.16
+Version: 2023.4.7.13
 Summary: Python client for Coin Metrics API v4.
 Home-page: https://coinmetrics.github.io/api-client-python/site/index.html
 License: MIT
 Keywords: coin metrics,coin,metrics,crypto,bitcoin,network-data,market-data,api,handy
 Author: Coin Metrics
 Author-email: info@coinmetrics.io
 Requires-Python: >=3.7.1,<4.0.0
```

