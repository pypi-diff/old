# Comparing `tmp/tinkoff-investments-0.2.0b8.tar.gz` & `tmp/tinkoff-investments-0.2.0b9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tinkoff-investments-0.2.0b8.tar", max compression
+gzip compressed data, was "tinkoff-investments-0.2.0b9.tar", max compression
```

## Comparing `tinkoff-investments-0.2.0b8.tar` & `tinkoff-investments-0.2.0b9.tar`

### file list

```diff
@@ -1,42 +1,46 @@
--rw-r--r--   0        0        0    11338 2022-01-28 20:03:26.566898 tinkoff-investments-0.2.0b8/LICENSE
--rw-r--r--   0        0        0      661 2022-01-28 20:03:26.566898 tinkoff-investments-0.2.0b8/README.md
--rw-r--r--   0        0        0     1488 2022-01-28 20:03:26.566898 tinkoff-investments-0.2.0b8/pyproject.toml
--rw-r--r--   0        0        0     6912 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/__init__.py
--rw-r--r--   0        0        0     3608 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/_errors.py
--rw-r--r--   0        0        0    10969 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/_grpc_helpers.py
--rw-r--r--   0        0        0    41533 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/async_services.py
--rw-r--r--   0        0        0      873 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/channels.py
--rw-r--r--   0        0        0      607 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/clients.py
--rw-r--r--   0        0        0      244 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/constants.py
--rw-r--r--   0        0        0     1443 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/data_loaders.py
--rw-r--r--   0        0        0      687 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/exceptions.py
--rw-r--r--   0        0        0        0 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/__init__.py
--rw-r--r--   0        0        0    12906 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/common_pb2.py
--rw-r--r--   0        0        0     8568 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/common_pb2.pyi
--rw-r--r--   0        0        0      159 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/common_pb2_grpc.py
--rw-r--r--   0        0        0   164733 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/instruments_pb2.py
--rw-r--r--   0        0        0    80941 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/instruments_pb2.pyi
--rw-r--r--   0        0        0    29977 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/instruments_pb2_grpc.py
--rw-r--r--   0        0        0   106537 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/marketdata_pb2.py
--rw-r--r--   0        0        0    51321 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/marketdata_pb2.pyi
--rw-r--r--   0        0        0    11756 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/marketdata_pb2_grpc.py
--rw-r--r--   0        0        0    87750 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/operations_pb2.py
--rw-r--r--   0        0        0    45257 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/operations_pb2.pyi
--rw-r--r--   0        0        0    11175 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/operations_pb2_grpc.py
--rw-r--r--   0        0        0    58678 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/orders_pb2.py
--rw-r--r--   0        0        0    28564 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/orders_pb2.pyi
--rw-r--r--   0        0        0    11641 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/orders_pb2_grpc.py
--rw-r--r--   0        0        0    17700 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/sandbox_pb2.py
--rw-r--r--   0        0        0     3922 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/sandbox_pb2.pyi
--rw-r--r--   0        0        0    22008 2022-01-28 20:03:26.570898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/sandbox_pb2_grpc.py
--rw-r--r--   0        0        0    30095 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/stoporders_pb2.py
--rw-r--r--   0        0        0    14488 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/stoporders_pb2.pyi
--rw-r--r--   0        0        0     7168 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/stoporders_pb2_grpc.py
--rw-r--r--   0        0        0    30298 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/users_pb2.py
--rw-r--r--   0        0        0    14827 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/users_pb2.pyi
--rw-r--r--   0        0        0     8750 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/users_pb2_grpc.py
--rw-r--r--   0        0        0     3160 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/logging.py
--rw-r--r--   0        0        0    48570 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/schemas.py
--rw-r--r--   0        0        0    38751 2022-01-28 20:03:26.574898 tinkoff-investments-0.2.0b8/tinkoff/invest/services.py
--rw-r--r--   0        0        0     1414 2022-01-28 20:04:14.352496 tinkoff-investments-0.2.0b8/setup.py
--rw-r--r--   0        0        0     1371 2022-01-28 20:04:14.352810 tinkoff-investments-0.2.0b8/PKG-INFO
+-rw-r--r--   0        0        0    11338 2021-12-22 12:38:39.268211 tinkoff-investments-0.2.0b9/LICENSE
+-rw-r--r--   0        0        0      661 2022-01-18 16:58:10.868465 tinkoff-investments-0.2.0b9/README.md
+-rw-r--r--   0        0        0     1515 2022-01-31 06:06:53.936482 tinkoff-investments-0.2.0b9/pyproject.toml
+-rw-r--r--   0        0        0     6985 2022-01-31 06:06:34.428362 tinkoff-investments-0.2.0b9/tinkoff/invest/__init__.py
+-rw-r--r--   0        0        0     3608 2022-01-18 16:36:59.273141 tinkoff-investments-0.2.0b9/tinkoff/invest/_errors.py
+-rw-r--r--   0        0        0    11002 2022-01-31 05:48:18.274591 tinkoff-investments-0.2.0b9/tinkoff/invest/_grpc_helpers.py
+-rw-r--r--   0        0        0     1031 2022-01-31 05:48:18.275156 tinkoff-investments-0.2.0b9/tinkoff/invest/async_orders_canceling.py
+-rw-r--r--   0        0        0    41533 2022-01-30 08:06:43.655778 tinkoff-investments-0.2.0b9/tinkoff/invest/async_services.py
+-rw-r--r--   0        0        0      873 2022-01-18 16:36:59.276496 tinkoff-investments-0.2.0b9/tinkoff/invest/channels.py
+-rw-r--r--   0        0        0      607 2022-01-18 16:36:59.277845 tinkoff-investments-0.2.0b9/tinkoff/invest/clients.py
+-rw-r--r--   0        0        0      264 2022-01-31 06:02:07.341152 tinkoff-investments-0.2.0b9/tinkoff/invest/constants.py
+-rw-r--r--   0        0        0     1443 2022-01-25 15:13:10.956923 tinkoff-investments-0.2.0b9/tinkoff/invest/data_loaders.py
+-rw-r--r--   0        0        0      687 2022-01-25 13:31:11.602374 tinkoff-investments-0.2.0b9/tinkoff/invest/exceptions.py
+-rw-r--r--   0        0        0        0 2022-01-28 21:17:30.261306 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/__init__.py
+-rw-r--r--   0        0        0    12906 2022-01-30 08:06:43.657161 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/common_pb2.py
+-rw-r--r--   0        0        0     8568 2022-01-30 08:06:43.658613 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/common_pb2.pyi
+-rw-r--r--   0        0        0      159 2022-01-30 08:06:43.659810 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/common_pb2_grpc.py
+-rw-r--r--   0        0        0   164733 2022-01-30 08:06:43.662066 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/instruments_pb2.py
+-rw-r--r--   0        0        0    80941 2022-01-30 08:06:43.663760 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/instruments_pb2.pyi
+-rw-r--r--   0        0        0    29977 2022-01-30 08:06:43.665007 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/instruments_pb2_grpc.py
+-rw-r--r--   0        0        0   106537 2022-01-30 08:06:43.666564 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/marketdata_pb2.py
+-rw-r--r--   0        0        0    51321 2022-01-30 08:06:43.668280 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/marketdata_pb2.pyi
+-rw-r--r--   0        0        0    11756 2022-01-30 08:06:43.669512 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/marketdata_pb2_grpc.py
+-rw-r--r--   0        0        0    87750 2022-01-30 08:06:43.670779 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/operations_pb2.py
+-rw-r--r--   0        0        0    45257 2022-01-30 08:06:43.672100 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/operations_pb2.pyi
+-rw-r--r--   0        0        0    11175 2022-01-30 08:06:43.673183 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/operations_pb2_grpc.py
+-rw-r--r--   0        0        0    58678 2022-01-30 08:06:43.674229 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/orders_pb2.py
+-rw-r--r--   0        0        0    28564 2022-01-30 08:06:43.675355 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/orders_pb2.pyi
+-rw-r--r--   0        0        0    11641 2022-01-30 08:06:43.676414 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/orders_pb2_grpc.py
+-rw-r--r--   0        0        0    17700 2022-01-30 08:06:43.677376 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/sandbox_pb2.py
+-rw-r--r--   0        0        0     3922 2022-01-30 08:06:43.678287 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/sandbox_pb2.pyi
+-rw-r--r--   0        0        0    22008 2022-01-30 08:06:43.679391 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/sandbox_pb2_grpc.py
+-rw-r--r--   0        0        0    30095 2022-01-30 08:06:43.680854 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/stoporders_pb2.py
+-rw-r--r--   0        0        0    14488 2022-01-30 08:06:43.682092 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/stoporders_pb2.pyi
+-rw-r--r--   0        0        0     7168 2022-01-30 08:06:43.683291 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/stoporders_pb2_grpc.py
+-rw-r--r--   0        0        0    30298 2022-01-30 08:06:43.684459 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/users_pb2.py
+-rw-r--r--   0        0        0    14827 2022-01-30 08:06:43.685482 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/users_pb2.pyi
+-rw-r--r--   0        0        0     8750 2022-01-30 08:06:43.686540 tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/users_pb2_grpc.py
+-rw-r--r--   0        0        0     3485 2022-01-31 06:02:18.170685 tinkoff-investments-0.2.0b9/tinkoff/invest/logging.py
+-rw-r--r--   0        0        0      790 2022-01-31 05:48:18.275809 tinkoff-investments-0.2.0b9/tinkoff/invest/orders_canceling.py
+-rw-r--r--   0        0        0    48570 2022-01-30 08:06:43.688313 tinkoff-investments-0.2.0b9/tinkoff/invest/schemas.py
+-rw-r--r--   0        0        0    38751 2022-01-30 08:06:43.689678 tinkoff-investments-0.2.0b9/tinkoff/invest/services.py
+-rw-r--r--   0        0        0      194 2022-01-31 05:48:18.276415 tinkoff-investments-0.2.0b9/tinkoff/invest/token.py
+-rw-r--r--   0        0        0       66 2022-01-31 05:48:18.276996 tinkoff-investments-0.2.0b9/tinkoff/invest/typedefs.py
+-rw-r--r--   0        0        0     1451 2022-01-31 06:07:35.531262 tinkoff-investments-0.2.0b9/setup.py
+-rw-r--r--   0        0        0     1420 2022-01-31 06:07:35.531747 tinkoff-investments-0.2.0b9/PKG-INFO
```

### Comparing `tinkoff-investments-0.2.0b8/LICENSE` & `tinkoff-investments-0.2.0b9/LICENSE`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/README.md` & `tinkoff-investments-0.2.0b9/README.md`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/pyproject.toml` & `tinkoff-investments-0.2.0b9/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "tinkoff-investments"
-version = "0.2.0-beta8"
+version = "0.2.0-beta9"
 description = ""
 authors = ["Danil Akhtarov <d.akhtarov@tinkoff.ru>"]
 license = "Apache 2"
 readme = "README.md"
 repository = "https://github.com/Tinkoff/invest-python"
 homepage = "https://github.com/Tinkoff/invest-python"
 packages = [
@@ -17,14 +17,15 @@
 exclude = ["tinkoff/__init__.py"]
 
 [tool.poetry.dependencies]
 python = "^3.8"
 grpcio = "^1.39.0"
 protobuf = "^3.19.3"
 tinkoff = "^0.1.1"
+pytest-asyncio = "^0.17.2"
 
 [tool.poetry.dev-dependencies]
 autoflake = "^1.4"
 black = "^21.12b0"
 codecov = "^2.1.12"
 flake8 = "^4.0.1"
 flake8-annotations-complexity = "^0.0.6"
```

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/__init__.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 from .clients import AsyncClient, Client
 from .data_loaders import get_all_candles
 from .exceptions import AioRequestError, InvestError, RequestError
 from .logging import get_current_tracking_id
+from .orders_canceling import cancel_all_orders
 from .schemas import (
     Account,
     AccountStatus,
     AccountType,
     AccruedInterest,
     Bond,
     BondResponse,
@@ -283,8 +284,9 @@
     "StopOrder",
     "BrokerReportRequest",
     "BrokerReportResponse",
     "GenerateBrokerReportRequest",
     "GetBrokerReportRequest",
     "get_current_tracking_id",
     "get_all_candles",
+    "cancel_all_orders",
 )
```

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/_errors.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/_errors.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/_grpc_helpers.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/_grpc_helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import dataclasses
 import enum
 from abc import ABC
-from datetime import datetime, timezone
+from datetime import datetime, timedelta, timezone
 from decimal import Decimal
 from typing import (
     Any,
     Optional,
     Tuple,
     Type,
     TypeVar,
@@ -20,15 +20,15 @@
 _sym_db = symbol_database.Default()
 
 T = TypeVar("T")
 
 
 def ts_to_datetime(value: Timestamp) -> datetime:
     ts = value.seconds + (value.nanos / 1e9)
-    return datetime.fromtimestamp(ts, tz=timezone.utc)
+    return datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=ts)
 
 
 def datetime_to_ts(value: datetime) -> Tuple[int, int]:
     seconds = int(value.timestamp())
     nanos = int(value.microsecond * 1e3)
     return seconds, nanos
```

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/async_services.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/async_services.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/channels.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/channels.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/clients.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/clients.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/data_loaders.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/data_loaders.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/exceptions.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/exceptions.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/common_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/common_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/common_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/common_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/instruments_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/instruments_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/instruments_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/instruments_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/instruments_pb2_grpc.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/instruments_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/marketdata_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/marketdata_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/marketdata_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/marketdata_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/marketdata_pb2_grpc.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/marketdata_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/operations_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/operations_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/operations_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/operations_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/operations_pb2_grpc.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/operations_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/orders_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/orders_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/orders_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/orders_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/orders_pb2_grpc.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/orders_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/sandbox_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/sandbox_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/sandbox_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/sandbox_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/sandbox_pb2_grpc.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/sandbox_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/stoporders_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/stoporders_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/stoporders_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/stoporders_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/stoporders_pb2_grpc.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/stoporders_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/users_pb2.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/users_pb2.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/users_pb2.pyi` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/users_pb2.pyi`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/grpc/users_pb2_grpc.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/grpc/users_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/logging.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/logging.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 import logging
 from collections import namedtuple
 from contextvars import ContextVar
 from typing import Any, Optional
 
 from .constants import (
+    MESSAGE,
     X_RATELIMIT_LIMIT,
     X_RATELIMIT_REMAINING,
     X_RATELIMIT_RESET,
     X_TRACKING_ID,
 )
 
 __all__ = (
@@ -21,15 +22,21 @@
 )
 
 logger = logging.getLogger(__name__)
 
 _TRACKING_ID: ContextVar[Optional[str]] = ContextVar("tracking_id", default=None)
 Metadata = namedtuple(
     "Metadata",
-    ("tracking_id", "ratelimit_limit", "ratelimit_remaining", "ratelimit_reset"),
+    (
+        "tracking_id",
+        "ratelimit_limit",
+        "ratelimit_remaining",
+        "ratelimit_reset",
+        "message",
+    ),
 )
 
 
 def get_current_tracking_id() -> Optional[str]:
     return _TRACKING_ID.get() or None
 
 
@@ -61,39 +68,53 @@
 
 def get_metadata_from_call(call: Any) -> Optional[Metadata]:
     metadata = call.initial_metadata() or call.trailing_metadata()
     tracking_id = None
     ratelimit_limit = None
     ratelimit_remaining = None
     ratelimit_reset = None
+    message = None
     for item in metadata:
         if item.key == X_TRACKING_ID:
             tracking_id = item.value
         elif item.key == X_RATELIMIT_LIMIT:
             ratelimit_limit = item.value
         elif item.key == X_RATELIMIT_REMAINING:
             ratelimit_remaining = int(item.value)
         elif item.key == X_RATELIMIT_RESET:
             ratelimit_reset = int(item.value)
-    if not any((tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset)):
+        elif item.key == MESSAGE:
+            message = item.value
+    if not any(
+        (tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset, message)
+    ):
         return None
-    return Metadata(tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset)
+    return Metadata(
+        tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset, message
+    )
 
 
 def get_metadata_from_aio_error(err: Any) -> Optional[Metadata]:
     metadata = err.initial_metadata() or err.trailing_metadata()
     tracking_id = None
     ratelimit_limit = None
     ratelimit_remaining = None
     ratelimit_reset = None
+    message = None
     for key, value in metadata:
         if key == X_TRACKING_ID:
             tracking_id = value
         elif key == X_RATELIMIT_LIMIT:
             ratelimit_limit = value
         elif key == X_RATELIMIT_REMAINING:
             ratelimit_remaining = int(value)
         elif key == X_RATELIMIT_RESET:
             ratelimit_reset = int(value)
-    if not any((tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset)):
+        elif key == MESSAGE:
+            message = value
+    if not any(
+        (tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset, message)
+    ):
         return None
-    return Metadata(tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset)
+    return Metadata(
+        tracking_id, ratelimit_limit, ratelimit_remaining, ratelimit_reset, message
+    )
```

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/schemas.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/schemas.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/tinkoff/invest/services.py` & `tinkoff-investments-0.2.0b9/tinkoff/invest/services.py`

 * *Files identical despite different names*

### Comparing `tinkoff-investments-0.2.0b8/setup.py` & `tinkoff-investments-0.2.0b9/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -4,19 +4,22 @@
 packages = \
 ['tinkoff', 'tinkoff.invest', 'tinkoff.invest.grpc']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['grpcio>=1.39.0,<2.0.0', 'protobuf>=3.19.3,<4.0.0', 'tinkoff>=0.1.1,<0.2.0']
+['grpcio>=1.39.0,<2.0.0',
+ 'protobuf>=3.19.3,<4.0.0',
+ 'pytest-asyncio>=0.17.2,<0.18.0',
+ 'tinkoff>=0.1.1,<0.2.0']
 
 setup_kwargs = {
     'name': 'tinkoff-investments',
-    'version': '0.2.0b8',
+    'version': '0.2.0b9',
     'description': '',
     'long_description': '# Tinkoff Invest\n\n[![PyPI](https://img.shields.io/pypi/v/tinkoff-investments)](https://pypi.org/project/tinkoff-investments/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tinkoff-investments)](https://www.python.org/downloads/)\n\n## Начало работы\n\n```\npip install tinkoff-investments\n```\n\n## Примеры\n\nПримеры доступны [здесь](https://github.com/Tinkoff/invest-python/tree/main/examples).\n\n## Contribution\n\n- [CONTRIBUTING](https://github.com/Tinkoff/invest-python/blob/main/CONTRIBUTING.md)\n\n## License\n\nЛицензия [The Apache License](https://github.com/Tinkoff/invest-python/blob/main/LICENSE).\n',
     'author': 'Danil Akhtarov',
     'author_email': 'd.akhtarov@tinkoff.ru',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/Tinkoff/invest-python',
```

### Comparing `tinkoff-investments-0.2.0b8/PKG-INFO` & `tinkoff-investments-0.2.0b9/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,23 +1,24 @@
 Metadata-Version: 2.1
 Name: tinkoff-investments
-Version: 0.2.0b8
+Version: 0.2.0b9
 Summary: 
 Home-page: https://github.com/Tinkoff/invest-python
 License: Apache 2
 Author: Danil Akhtarov
 Author-email: d.akhtarov@tinkoff.ru
 Requires-Python: >=3.8,<4.0
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Dist: grpcio (>=1.39.0,<2.0.0)
 Requires-Dist: protobuf (>=3.19.3,<4.0.0)
+Requires-Dist: pytest-asyncio (>=0.17.2,<0.18.0)
 Requires-Dist: tinkoff (>=0.1.1,<0.2.0)
 Project-URL: Repository, https://github.com/Tinkoff/invest-python
 Description-Content-Type: text/markdown
 
 # Tinkoff Invest
 
 [![PyPI](https://img.shields.io/pypi/v/tinkoff-investments)](https://pypi.org/project/tinkoff-investments/)
```

