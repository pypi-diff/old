# Comparing `tmp/tellor_disputables-1.3.2.tar.gz` & `tmp/tellor_disputables-1.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tellor_disputables-1.3.2.tar", max compression
+gzip compressed data, was "tellor_disputables-1.4.1.tar", max compression
```

## Comparing `tellor_disputables-1.3.2.tar` & `tellor_disputables-1.4.1.tar`

### file list

```diff
@@ -1,12 +1,12 @@
--rw-r--r--   0        0        0     4938 2023-03-30 15:38:33.909046 tellor_disputables-1.3.2/README.md
--rw-r--r--   0        0        0      308 2023-03-30 15:38:33.913046 tellor_disputables-1.3.2/disputer-config.yaml
--rw-r--r--   0        0        0      995 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/pyproject.toml
--rw-r--r--   0        0        0     8930 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/src/tellor_disputables/__init__.py
--rw-r--r--   0        0        0     2397 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/src/tellor_disputables/alerts.py
--rw-r--r--   0        0        0     6935 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/src/tellor_disputables/cli.py
--rw-r--r--   0        0        0     3390 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/src/tellor_disputables/config.py
--rw-r--r--   0        0        0    13412 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/src/tellor_disputables/data.py
--rw-r--r--   0        0        0     4850 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/src/tellor_disputables/disputer.py
--rw-r--r--   0        0        0     3342 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/src/tellor_disputables/utils.py
--rw-r--r--   0        0        0      152 2023-03-30 15:38:33.917046 tellor_disputables-1.3.2/vars.example.sh
--rw-r--r--   0        0        0      814 1970-01-01 00:00:00.000000 tellor_disputables-1.3.2/PKG-INFO
+-rw-r--r--   0        0        0     9401 2023-04-06 18:49:29.235626 tellor_disputables-1.4.1/README.md
+-rw-r--r--   0        0        0      308 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/disputer-config.yaml
+-rw-r--r--   0        0        0      995 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/pyproject.toml
+-rw-r--r--   0        0        0     8930 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/src/tellor_disputables/__init__.py
+-rw-r--r--   0        0        0     2661 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/src/tellor_disputables/alerts.py
+-rw-r--r--   0        0        0     7573 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/src/tellor_disputables/cli.py
+-rw-r--r--   0        0        0     3390 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/src/tellor_disputables/config.py
+-rw-r--r--   0        0        0    13677 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/src/tellor_disputables/data.py
+-rw-r--r--   0        0        0     5596 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/src/tellor_disputables/disputer.py
+-rw-r--r--   0        0        0     3491 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/src/tellor_disputables/utils.py
+-rw-r--r--   0        0        0      152 2023-04-06 18:49:29.239626 tellor_disputables-1.4.1/vars.example.sh
+-rw-r--r--   0        0        0      814 1970-01-01 00:00:00.000000 tellor_disputables-1.4.1/PKG-INFO
```

### Comparing `tellor_disputables-1.3.2/pyproject.toml` & `tellor_disputables-1.4.1/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "tellor-disputables"
-version = "1.3.2"
+version = "1.4.1"
 description = "dashboard & text alerts for disputable values reported to Tellor oracles"
 authors = ["tallywiesenberg <info@tellor.io>"]
 license = "MIT"
 packages = [{ include = "tellor_disputables", from = "src" }]
 include = ["vars.example.sh", "README.md", "disputer-config.yaml"]
 
 [tool.poetry.dependencies]
```

### Comparing `tellor_disputables-1.3.2/src/tellor_disputables/__init__.py` & `tellor_disputables-1.4.1/src/tellor_disputables/__init__.py`

 * *Files identical despite different names*

### Comparing `tellor_disputables-1.3.2/src/tellor_disputables/alerts.py` & `tellor_disputables-1.4.1/src/tellor_disputables/alerts.py`

 * *Files 18% similar despite different names*

```diff
@@ -19,14 +19,23 @@
 def get_twilio_info() -> Tuple[Optional[str], Optional[List[str]]]:
     """Read the Twilio from number, client and phone numbers from the environment."""
     twilio_from = os.environ.get("TWILIO_FROM")
     phone_numbers = os.environ.get("ALERT_RECIPIENTS")
     return twilio_from, phone_numbers.split(",") if phone_numbers is not None else None
 
 
+def dispute_alert(msg: str, recipients: List[str], from_number: str) -> None:
+    """send an alert that the dispute was successful to the user"""
+
+    twilio_client = get_twilio_client()
+    send_text_msg(twilio_client, recipients, from_number, msg)
+
+    return
+
+
 def alert(all_values: bool, new_report: NewReport, recipients: List[str], from_number: str) -> None:
 
     twilio_client = get_twilio_client()
 
     if new_report.query_type in ALWAYS_ALERT_QUERY_TYPES:
         msg = generate_alert_msg(False, new_report.link)
         send_text_msg(twilio_client, recipients, from_number, msg)
```

### Comparing `tellor_disputables-1.3.2/src/tellor_disputables/cli.py` & `tellor_disputables-1.4.1/src/tellor_disputables/cli.py`

 * *Files 8% similar despite different names*

```diff
@@ -8,14 +8,15 @@
 from chained_accounts import ChainedAccount
 from hexbytes import HexBytes
 from telliot_core.apps.telliot_config import TelliotConfig
 from telliot_core.cli.utils import async_run
 
 from tellor_disputables import WAIT_PERIOD
 from tellor_disputables.alerts import alert
+from tellor_disputables.alerts import dispute_alert
 from tellor_disputables.alerts import generic_alert
 from tellor_disputables.alerts import get_twilio_info
 from tellor_disputables.config import AutoDisputerConfig
 from tellor_disputables.data import chain_events
 from tellor_disputables.data import get_events
 from tellor_disputables.data import parse_new_report_event
 from tellor_disputables.disputer import dispute
@@ -42,23 +43,39 @@
 @click.command()
 @click.option(
     "-av", "--all-values", is_flag=True, default=False, show_default=True, help="if set, get alerts for all values"
 )
 @click.option("-a", "--account-name", help="the name of a ChainedAccount to dispute with", type=str)
 @click.option("-w", "--wait", help="how long to wait between checks", type=int, default=WAIT_PERIOD)
 @click.option("-d", "--is-disputing", help="enable auto-disputing on chain", is_flag=True)
+@click.option(
+    "-c",
+    "--confidence-threshold",
+    help="set general confidence percentage threshold for monitoring only",
+    type=float,
+    default=0.1,
+)
 @async_run
-async def main(all_values: bool, wait: int, account_name: str, is_disputing: bool) -> None:
+async def main(all_values: bool, wait: int, account_name: str, is_disputing: bool, confidence_threshold: float) -> None:
     """CLI dashboard to display recent values reported to Tellor oracles."""
-    await start(all_values=all_values, wait=wait, account_name=account_name, is_disputing=is_disputing)
+    await start(
+        all_values=all_values,
+        wait=wait,
+        account_name=account_name,
+        is_disputing=is_disputing,
+        confidence_threshold=confidence_threshold,
+    )
 
 
-async def start(all_values: bool, wait: int, account_name: str, is_disputing: bool) -> None:
+async def start(
+    all_values: bool, wait: int, account_name: str, is_disputing: bool, confidence_threshold: float
+) -> None:
     """Start the CLI dashboard."""
     cfg = TelliotConfig()
+    cfg.main.chain_id = 1
     disp_cfg = AutoDisputerConfig()
     print_title_info()
 
     from_number, recipients = get_twilio_info()
     if from_number is None or recipients is None:
         logger.error("Missing phone numbers. See README for required environment variables. Exiting.")
         return
@@ -116,15 +133,18 @@
                     link = get_tx_explorer_url(cfg=cfg, tx_hash=event.transactionHash.hex())
                     msg = f"\n❗NEW ORACLE ADDRESS ALERT❗\n{link}"
                     generic_alert(from_number=from_number, recipients=recipients, msg=msg)
                     continue
 
                 try:
                     new_report = await parse_new_report_event(
-                        cfg=cfg, monitored_feeds=disp_cfg.monitored_feeds, log=event
+                        cfg=cfg,
+                        monitored_feeds=disp_cfg.monitored_feeds,
+                        log=event,
+                        confidence_threshold=confidence_threshold,
                     )
                 except Exception as e:
                     logger.error("unable to parse new report event! " + str(e))
                     continue
 
                 # Skip duplicate & missing events
                 if new_report is None or new_report.tx_hash in displayed_events:
@@ -136,16 +156,18 @@
                 print_title_info()
 
                 if is_disputing:
                     click.echo("...Now with auto-disputing!")
 
                 alert(all_values, new_report, recipients, from_number)
 
-                if is_disputing and account and new_report.disputable:
-                    await dispute(cfg, account, new_report)
+                if is_disputing and new_report.disputable:
+                    success_msg = await dispute(cfg, disp_cfg, account, new_report)
+                    if success_msg:
+                        dispute_alert(success_msg, recipients, from_number)
 
                 display_rows.append(
                     (
                         new_report.tx_hash,
                         new_report.submission_timestamp,
                         new_report.link,
                         new_report.query_type,
```

### Comparing `tellor_disputables-1.3.2/src/tellor_disputables/config.py` & `tellor_disputables-1.4.1/src/tellor_disputables/config.py`

 * *Files identical despite different names*

### Comparing `tellor_disputables-1.3.2/src/tellor_disputables/data.py` & `tellor_disputables-1.4.1/src/tellor_disputables/data.py`

 * *Files 3% similar despite different names*

```diff
@@ -19,14 +19,15 @@
 from telliot_feeds.queries.price.spot_price import SpotPrice
 from telliot_feeds.queries.query import OracleQuery
 from web3 import Web3
 from web3._utils.events import get_event_data
 from web3.types import LogReceipt
 
 from tellor_disputables import ALWAYS_ALERT_QUERY_TYPES
+from tellor_disputables import DATAFEED_LOOKUP
 from tellor_disputables import NEW_REPORT_ABI
 from tellor_disputables import WAIT_PERIOD
 from tellor_disputables.utils import disputable_str
 from tellor_disputables.utils import get_logger
 from tellor_disputables.utils import get_tx_explorer_url
 from tellor_disputables.utils import NewReport
 
@@ -275,14 +276,15 @@
     for endpoint in cfg.endpoints.endpoints:
         if endpoint.url.endswith("{INFURA_API_KEY}"):
             continue
         try:
             endpoint.connect()
         except Exception as e:
             logger.warning("unable to connect to endpoint: " + str(e))
+            continue
 
         w3 = endpoint.web3
 
         if not w3:
             continue
 
         addr, _ = get_contract_info(endpoint.chain_id, contract_name)
@@ -305,21 +307,22 @@
             pass
     return None
 
 
 async def parse_new_report_event(
     cfg: TelliotConfig,
     log: LogReceipt,
+    confidence_threshold: float,
     monitored_feeds: List[MonitoredFeed],
     see_all_values: bool = False,
 ) -> Optional[NewReport]:
     """Parse a NewReport event."""
 
     q_ids_to_monitored_feeds = {
-        "0x" + monitored_feed.feed.query.query_id.hex(): monitored_feed for monitored_feed in monitored_feeds
+        monitored_feed.feed.query.query_id.hex(): monitored_feed for monitored_feed in monitored_feeds
     }
 
     chain_id = cfg.main.chain_id
     endpoint = cfg.endpoints.find(chain_id=chain_id)[0]
 
     new_report = NewReport()
 
@@ -353,16 +356,18 @@
     new_report.submission_timestamp = event_data.args._time  # in unix time
 
     if new_report.query_type in ALWAYS_ALERT_QUERY_TYPES:
         new_report.status_str = "❗❗❗❗ VERY IMPORTANT DATA SUBMISSION ❗❗❗❗"
         return new_report
 
     if new_report.query_id not in q_ids_to_monitored_feeds:  # TODO ensure both has 0x or none have 0x
-        logger.info("skipping undesired NewReport event")
-        return None
+
+        # build a monitored feed for all feeds not auto-disputing for
+        threshold = Threshold(metric=Metrics.Percentage, amount=confidence_threshold)
+        monitored_feed = MonitoredFeed(DATAFEED_LOOKUP[new_report.query_id[2:]], threshold)
     else:
         monitored_feed = q_ids_to_monitored_feeds[new_report.query_id]
 
     if isinstance(q, SpotPrice):
         new_report.asset = q.asset.upper()
         new_report.currency = q.currency.upper()
     else:
```

### Comparing `tellor_disputables-1.3.2/src/tellor_disputables/disputer.py` & `tellor_disputables-1.4.1/src/tellor_disputables/disputer.py`

 * *Files 6% similar despite different names*

```diff
@@ -2,72 +2,85 @@
 from typing import Optional
 
 from chained_accounts import ChainedAccount
 from telliot_core.apps.telliot_config import TelliotConfig
 from telliot_core.gas.legacy_gas import fetch_gas_price
 from web3 import Web3
 
+from tellor_disputables.config import AutoDisputerConfig
 from tellor_disputables.data import get_contract
 from tellor_disputables.utils import get_logger
 from tellor_disputables.utils import NewReport
 
 logger = get_logger(__name__)
 
 
-async def dispute(cfg: TelliotConfig, account: ChainedAccount, new_report: NewReport) -> None:
+async def dispute(
+    cfg: TelliotConfig, disp_cfg: AutoDisputerConfig, account: Optional[ChainedAccount], new_report: NewReport
+) -> str:
     """Main dispute logic for auto-disputer"""
 
+    if not disp_cfg.monitored_feeds:
+        logger.info("Currently not auto-dispuing on any feeds. See ./disputer-config.yaml")
+        return ""
+
+    meant_to_dispute = new_report.query_id[2:] in [feed.feed.query.query_id.hex() for feed in disp_cfg.monitored_feeds]
+
+    if not meant_to_dispute:
+        logger.info("Found disputable new report outside selected Monitored Feeds, skipping dispute")
+        return ""
+
     if account is None:
         logger.info("No account provided, skipping eligible dispute")
-        return None
+        return ""
 
     cfg.main.chain_id = new_report.chain_id
 
     token = get_contract(cfg, name="trb-token", account=account)
     governance = get_contract(cfg, name="tellor-governance", account=account)
 
     if token is None:
         logger.error("Unable to find token contract")
-        return None
+        return ""
 
     if governance is None:
         logger.error("Unable to find governance contract")
-        return None
+        return ""
 
     # read balance of user and log it
     user_token_balance, status = await token.read("balanceOf", Web3.toChecksumAddress(account.address))
 
     if not status.ok:
         logger.error("Unable to retrieve Disputer account balance")
-        return None
+        return ""
 
     logger.info(f"Disputer ({account.address}) balance: " + str(user_token_balance))
 
     dispute_fee = await get_dispute_fee(cfg, new_report)
 
     if dispute_fee is None:
         logger.error("Unable to calculate Dispute Fee from contracts")
-        return None
+        return ""
 
     logger.info("Dispute Fee: " + str(dispute_fee / 1e18) + " TRB")
 
     # if balanceOf(user) < disputeFee, log "need more tokens to initiate dispute"
     if user_token_balance < dispute_fee:
         logger.info("User balance is below dispute fee: need more tokens to initiate dispute")
-        return None
+        return ""
 
     # write approve(governance contract, disputeFee) and log "token approved" if successful
     gas_price = await fetch_gas_price()
     tx_receipt, status = await token.write(
         "approve", spender=governance.address, amount=dispute_fee * 100, gas_limit=60000, legacy_gas_price=gas_price
     )
 
     if not status.ok:
         logger.error("unable to approve tokens for dispute fee: " + status.error)
-        return None
+        return ""
 
     logger.info("Approval Tx Hash: " + str(tx_receipt.transactionHash.hex()))
 
     tx_receipt, status = await governance.write(
         func_name="beginDispute",
         _queryId=new_report.query_id,
         _timestamp=new_report.submission_timestamp,
@@ -77,18 +90,25 @@
 
     if not status.ok:
         logger.error(
             f"unable to begin dispute on {new_report.query_id}"
             + f"at submission timestamp {new_report.submission_timestamp}:"
             + status.error
         )
-        return None
+        return ""
 
     new_report.status_str += ": disputed!"
-    logger.info("Dispute Tx Hash: " + str(tx_receipt.transactionHash.hex()))
+    explorer = cfg.get_endpoint().explorer
+    if not explorer:
+        dispute_tx_link = str(tx_receipt.transactionHash.hex())
+    else:
+        dispute_tx_link = explorer + str(tx_receipt.transactionHash.hex())
+
+    logger.info("Dispute Tx Link: " + dispute_tx_link)
+    return "Dispute Tx Link: " + dispute_tx_link
 
 
 async def get_dispute_fee(cfg: TelliotConfig, new_report: NewReport) -> Optional[int]:
     """Calculate dispute fee on a Tellor network"""
 
     governance = get_contract(cfg, name="tellor-governance", account=None)
     oracle = get_contract(cfg, name="tellor360-oracle", account=None)
```

### Comparing `tellor_disputables-1.3.2/src/tellor_disputables/utils.py` & `tellor_disputables-1.4.1/src/tellor_disputables/utils.py`

 * *Files 9% similar despite different names*

```diff
@@ -3,16 +3,16 @@
 import os
 from dataclasses import dataclass
 from typing import Optional
 from typing import Union
 
 import click
 from chained_accounts import ChainedAccount
+from chained_accounts import find_accounts
 from telliot_core.apps.telliot_config import TelliotConfig
-from telliot_feeds.utils.cfg import check_accounts
 from telliot_feeds.utils.cfg import setup_account
 
 
 def get_tx_explorer_url(tx_hash: str, cfg: TelliotConfig) -> str:
     """Get transaction explorer URL."""
     explorer: str = cfg.get_endpoint().explorer
     if explorer is not None:
@@ -67,28 +67,29 @@
     if os.name == "nt":
         _ = os.system("cls")
     # mac, linux (name=="posix")
     else:
         _ = os.system("clear")
 
 
-def select_account(cfg: TelliotConfig, account: str) -> Optional[ChainedAccount]:
-
-    cfg.main.chain_id = 1
+def select_account(cfg: TelliotConfig, account: Optional[str]) -> Optional[ChainedAccount]:
+    """Select an account for disputing, allow no account to be chosen."""
 
     if account is not None:
-        accounts = check_accounts(cfg, account)
+        accounts = find_accounts(name=account)
         click.echo(f"Your account name: {accounts[0].name if accounts else None}")
     else:
-        account = setup_account(cfg.main.chain_id)
-        if account is not None:
-            click.echo(f"{account.name} selected!")
-            return account
+        run_alerts_only = click.confirm("Missing an account to send disputes. Run alerts only?")
+        if not run_alerts_only:
+            new_account = setup_account(cfg.main.chain_id)
+            if new_account is not None:
+                click.echo(f"{new_account.name} selected!")
+                return new_account
+            return None
         else:
-            click.echo("Missing an account to send disputes. Running alerts only!")
             return None
 
     accounts[0].unlock()
     return accounts[0]
 
 
 def get_logger(name: str) -> logging.Logger:
```

### Comparing `tellor_disputables-1.3.2/PKG-INFO` & `tellor_disputables-1.4.1/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tellor-disputables
-Version: 1.3.2
+Version: 1.4.1
 Summary: dashboard & text alerts for disputable values reported to Tellor oracles
 License: MIT
 Author: tallywiesenberg
 Author-email: info@tellor.io
 Requires-Python: >=3.9,<3.11
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

