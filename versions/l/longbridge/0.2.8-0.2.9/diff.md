# Comparing `tmp/longbridge-0.2.8.tar.gz` & `tmp/longbridge-0.2.9.tar.gz`

## Comparing `longbridge-0.2.8.tar` & `longbridge-0.2.9.tar`

### file list

```diff
@@ -1,130 +1,132 @@
--rw-r--r--   0        0        0      243 1970-01-01 00:00:00.000000 longbridge-0.2.8/local_dependencies/longbridge-python-macros/Cargo.toml
--rw-r--r--   0      501       20      541 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-python-macros/src/error.rs
--rw-r--r--   0      501       20      692 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-python-macros/src/lib.rs
--rw-r--r--   0      501       20     2028 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-python-macros/src/pyenum.rs
--rw-r--r--   0      501       20     2795 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-python-macros/src/pyobject.rs
--rw-r--r--   0        0        0     1282 1970-01-01 00:00:00.000000 longbridge-0.2.8/local_dependencies/longbridge/Cargo.toml
--rw-r--r--   0      501       20      291 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/CHANGELOG.md
--rw-r--r--   0      501       20    46817 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/Cargo.lock
--rw-r--r--   0      501       20       78 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/Makefile.toml
--rw-r--r--   0      501       20     4176 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/README.md
--rw-r--r--   0      501       20      509 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/examples/pull_quotes.rs
--rw-r--r--   0      501       20      782 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/examples/submit_order.rs
--rw-r--r--   0      501       20      567 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/examples/subscribe_quote.rs
--rw-r--r--   0      501       20      147 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/blocking/error.rs
--rw-r--r--   0      501       20      184 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/blocking/mod.rs
--rw-r--r--   0      501       20    18569 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/blocking/quote.rs
--rw-r--r--   0      501       20     3534 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/blocking/runtime.rs
--rw-r--r--   0      501       20    10768 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/blocking/trade.rs
--rw-r--r--   0      501       20     3392 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/config.rs
--rw-r--r--   0      501       20      487 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/lib.rs
--rw-r--r--   0      501       20     1520 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/macros.rs
--rw-r--r--   0      501       20     1934 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/cache.rs
--rw-r--r--   0      501       20     1652 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/cmd_code.rs
--rw-r--r--   0      501       20    31103 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/context.rs
--rw-r--r--   0      501       20    13318 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/core.rs
--rw-r--r--   0      501       20      854 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/mod.rs
--rw-r--r--   0      501       20     5278 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/push_types.rs
--rw-r--r--   0      501       20     3739 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/store.rs
--rw-r--r--   0      501       20     1494 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/sub_flags.rs
--rw-r--r--   0      501       20    22670 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/types.rs
--rw-r--r--   0      501       20      345 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/quote/utils.rs
--rw-r--r--   0      501       20      284 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/cmd_code.rs
--rw-r--r--   0      501       20    15811 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/context.rs
--rw-r--r--   0      501       20     7212 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/core.rs
--rw-r--r--   0      501       20      836 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/mod.rs
--rw-r--r--   0      501       20     3174 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/push_types.rs
--rw-r--r--   0      501       20     1656 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_cash_flow.rs
--rw-r--r--   0      501       20      663 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_fund_positions.rs
--rw-r--r--   0      501       20     1374 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_history_executions.rs
--rw-r--r--   0      501       20     2270 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_history_orders.rs
--rw-r--r--   0      501       20      668 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_stock_positions.rs
--rw-r--r--   0      501       20      902 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_today_executions.rs
--rw-r--r--   0      501       20     1517 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_today_orders.rs
--rw-r--r--   0      501       20      663 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/mod.rs
--rw-r--r--   0      501       20     2469 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/replace_order.rs
--rw-r--r--   0      501       20     3615 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/submit_order.rs
--rw-r--r--   0      501       20     6411 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/serde_utils.rs
--rw-r--r--   0      501       20    27942 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/trade/types.rs
--rw-r--r--   0      501       20      378 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge/src/types.rs
--rw-r--r--   0        0        0      568 1970-01-01 00:00:00.000000 longbridge-0.2.8/local_dependencies/longbridge-wscli/Cargo.toml
--rw-r--r--   0      501       20    11037 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-wscli/src/client.rs
--rw-r--r--   0      501       20     6818 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-wscli/src/codec.rs
--rw-r--r--   0      501       20     1785 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-wscli/src/error.rs
--rw-r--r--   0      501       20      320 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-wscli/src/event.rs
--rw-r--r--   0      501       20      406 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-wscli/src/lib.rs
--rw-r--r--   0        0        0      678 1970-01-01 00:00:00.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/Cargo.toml
--rw-r--r--   0      501       20     1181 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/client.rs
--rw-r--r--   0      501       20     2064 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/config.rs
--rw-r--r--   0      501       20     1199 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/error.rs
--rw-r--r--   0      501       20      448 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/lib.rs
--rw-r--r--   0      501       20    27363 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/qs.rs
--rw-r--r--   0      501       20     4815 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/request.rs
--rw-r--r--   0      501       20     1967 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/signature.rs
--rw-r--r--   0      501       20      601 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/timestamp.rs
--rw-r--r--   0        0        0      215 1970-01-01 00:00:00.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/Cargo.toml
--rw-r--r--   0      501       20      491 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/build.rs
--rw-r--r--   0      501       20       96 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/error/error.proto
--rw-r--r--   0      501       20      282 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/.gitignore
--rw-r--r--   0      501       20       51 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/README.md
--rw-r--r--   0      501       20      259 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/buf.gen.yaml
--rw-r--r--   0      501       20      949 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/control/control.proto
--rw-r--r--   0      501       20      110 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/control/error.proto
--rw-r--r--   0      501       20    61777 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.cc
--rw-r--r--   0      501       20    57188 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.h
--rw-r--r--   0      501       20    12844 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.cc
--rw-r--r--   0      501       20    11444 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.h
--rw-r--r--   0      501       20   841977 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.cc
--rw-r--r--   0      501       20   880122 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.h
--rw-r--r--   0      501       20    66071 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.cc
--rw-r--r--   0      501       20    75407 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.h
--rw-r--r--   0      501       20    20623 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/control.pb.go
--rw-r--r--   0      501       20     5943 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/error.pb.go
--rw-r--r--   0      501       20   204823 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/quote/api.pb.go
--rw-r--r--   0      501       20    23270 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/trade/subscribe.pb.go
--rw-r--r--   0      501       20     5432 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/control_pb2.py
--rw-r--r--   0      501       20     1879 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/error_pb2.py
--rw-r--r--   0      501       20    45695 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/quote/api_pb2.py
--rw-r--r--   0      501       20     5940 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/trade/subscribe_pb2.py
--rw-r--r--   0      501       20      103 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/go.mod
--rw-r--r--   0      501       20      739 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/go.sum
--rw-r--r--   0      501       20    10422 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/quote/api.proto
--rw-r--r--   0      501       20     1186 2022-05-30 01:28:53.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/trade/subscribe.proto
--rw-r--r--   0      501       20      293 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/src/lib.rs
--rw-r--r--   0      501       20     1956 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/src/longbridgeapp.control.v1.rs
--rw-r--r--   0      501       20    24910 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/src/longbridgeapp.quote.v1.rs
--rw-r--r--   0      501       20     2691 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/src/longbridgeapp.trade.v1.rs
--rw-r--r--   0      501       20      191 2022-05-30 01:28:52.000000 longbridge-0.2.8/local_dependencies/longbridge-proto/src/qop.error.rs
--rw-r--r--   0        0        0      862 1970-01-01 00:00:00.000000 longbridge-0.2.8/Cargo.toml
--rw-r--r--   0      501       20      210 2022-05-30 01:28:52.000000 longbridge-0.2.8/.cargo/config.toml
--rw-r--r--   0      501       20        4 2022-05-30 01:28:52.000000 longbridge-0.2.8/.gitignore
--rw-r--r--   0      501       20      292 2022-05-30 01:28:52.000000 longbridge-0.2.8/CHANGELOG.md
--rw-r--r--   0      501       20      382 2022-05-30 01:28:52.000000 longbridge-0.2.8/Makefile.toml
--rw-r--r--   0      501       20     2529 2022-05-30 01:28:52.000000 longbridge-0.2.8/README.md
--rw-r--r--   0      501       20       71 2022-05-30 01:28:52.000000 longbridge-0.2.8/build.rs
--rw-r--r--   0      501       20       40 2022-05-30 01:28:52.000000 longbridge-0.2.8/docs/config.md
--rw-r--r--   0      501       20     2490 2022-05-30 01:28:52.000000 longbridge-0.2.8/docs/index.md
--rw-r--r--   0      501       20       52 2022-05-30 01:28:52.000000 longbridge-0.2.8/docs/quote_context.md
--rw-r--r--   0      501       20       41 2022-05-30 01:28:52.000000 longbridge-0.2.8/docs/reference_all.md
--rw-r--r--   0      501       20       91 2022-05-30 01:28:52.000000 longbridge-0.2.8/docs/requirements.txt
--rw-r--r--   0      501       20       52 2022-05-30 01:28:52.000000 longbridge-0.2.8/docs/trade_context.md
--rw-r--r--   0      501       20      731 2022-05-30 01:28:52.000000 longbridge-0.2.8/mkdocs.yml
--rw-r--r--   0      501       20      817 2022-05-30 01:28:52.000000 longbridge-0.2.8/pyproject.toml
--rw-r--r--   0      501       20       89 2022-05-30 01:28:52.000000 longbridge-0.2.8/pysrc/longbridge/__init__.py
--rw-r--r--   0      501       20        0 2022-05-30 01:28:52.000000 longbridge-0.2.8/pysrc/longbridge/openapi.py
--rw-r--r--   0      501       20    51903 2022-05-30 01:28:52.000000 longbridge-0.2.8/pysrc/longbridge/openapi.pyi
--rw-r--r--   0      501       20        0 2022-05-30 01:28:52.000000 longbridge-0.2.8/pysrc/longbridge/py.typed
--rw-r--r--   0      501       20      927 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/config.rs
--rw-r--r--   0      501       20     2206 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/decimal.rs
--rw-r--r--   0      501       20      422 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/lib.rs
--rw-r--r--   0      501       20     6271 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/quote/context.rs
--rw-r--r--   0      501       20     1616 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/quote/mod.rs
--rw-r--r--   0      501       20     1801 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/quote/push.rs
--rw-r--r--   0      501       20    15743 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/quote/types.rs
--rw-r--r--   0      501       20     3554 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/time.rs
--rw-r--r--   0      501       20     9753 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/trade/context.rs
--rw-r--r--   0      501       20      653 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/trade/mod.rs
--rw-r--r--   0      501       20      632 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/trade/push.rs
--rw-r--r--   0      501       20    11458 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/trade/types.rs
--rw-r--r--   0      501       20      326 2022-05-30 01:28:52.000000 longbridge-0.2.8/src/types.rs
--rw-r--r--   0        0        0     3356 1970-01-01 00:00:00.000000 longbridge-0.2.8/PKG-INFO
+-rw-r--r--   0        0        0      568 1970-01-01 00:00:00.000000 longbridge-0.2.9/local_dependencies/longbridge-wscli/Cargo.toml
+-rw-r--r--   0      501       20    11037 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-wscli/src/client.rs
+-rw-r--r--   0      501       20     6818 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-wscli/src/codec.rs
+-rw-r--r--   0      501       20     1785 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-wscli/src/error.rs
+-rw-r--r--   0      501       20      320 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-wscli/src/event.rs
+-rw-r--r--   0      501       20      406 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-wscli/src/lib.rs
+-rw-r--r--   0        0        0      215 1970-01-01 00:00:00.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/Cargo.toml
+-rw-r--r--   0      501       20      491 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/build.rs
+-rw-r--r--   0      501       20       96 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/error/error.proto
+-rw-r--r--   0      501       20      282 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/.gitignore
+-rw-r--r--   0      501       20       51 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/README.md
+-rw-r--r--   0      501       20      259 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/buf.gen.yaml
+-rw-r--r--   0      501       20      949 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/control/control.proto
+-rw-r--r--   0      501       20      110 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/control/error.proto
+-rw-r--r--   0      501       20    61777 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.cc
+-rw-r--r--   0      501       20    57188 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.h
+-rw-r--r--   0      501       20    12844 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.cc
+-rw-r--r--   0      501       20    11444 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.h
+-rw-r--r--   0      501       20   841977 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.cc
+-rw-r--r--   0      501       20   880122 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.h
+-rw-r--r--   0      501       20    66071 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.cc
+-rw-r--r--   0      501       20    75407 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.h
+-rw-r--r--   0      501       20    20623 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/control.pb.go
+-rw-r--r--   0      501       20     5943 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/error.pb.go
+-rw-r--r--   0      501       20   204823 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/quote/api.pb.go
+-rw-r--r--   0      501       20    23270 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/trade/subscribe.pb.go
+-rw-r--r--   0      501       20     5432 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/control_pb2.py
+-rw-r--r--   0      501       20     1879 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/error_pb2.py
+-rw-r--r--   0      501       20    45695 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/quote/api_pb2.py
+-rw-r--r--   0      501       20     5940 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/trade/subscribe_pb2.py
+-rw-r--r--   0      501       20      103 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/go.mod
+-rw-r--r--   0      501       20      739 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/go.sum
+-rw-r--r--   0      501       20    10422 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/quote/api.proto
+-rw-r--r--   0      501       20     1186 2022-06-03 01:44:18.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/trade/subscribe.proto
+-rw-r--r--   0      501       20      293 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/src/lib.rs
+-rw-r--r--   0      501       20     1956 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/src/longbridgeapp.control.v1.rs
+-rw-r--r--   0      501       20    24910 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/src/longbridgeapp.quote.v1.rs
+-rw-r--r--   0      501       20     2691 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/src/longbridgeapp.trade.v1.rs
+-rw-r--r--   0      501       20      191 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-proto/src/qop.error.rs
+-rw-r--r--   0        0        0      678 1970-01-01 00:00:00.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/Cargo.toml
+-rw-r--r--   0      501       20     1181 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/client.rs
+-rw-r--r--   0      501       20     2064 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/config.rs
+-rw-r--r--   0      501       20     1199 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/error.rs
+-rw-r--r--   0      501       20      448 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/lib.rs
+-rw-r--r--   0      501       20    27363 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/qs.rs
+-rw-r--r--   0      501       20     4852 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/request.rs
+-rw-r--r--   0      501       20     1967 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/signature.rs
+-rw-r--r--   0      501       20      601 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/timestamp.rs
+-rw-r--r--   0        0        0      243 1970-01-01 00:00:00.000000 longbridge-0.2.9/local_dependencies/longbridge-python-macros/Cargo.toml
+-rw-r--r--   0      501       20      541 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-python-macros/src/error.rs
+-rw-r--r--   0      501       20      692 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-python-macros/src/lib.rs
+-rw-r--r--   0      501       20     2561 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-python-macros/src/pyenum.rs
+-rw-r--r--   0      501       20     2831 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge-python-macros/src/pyobject.rs
+-rw-r--r--   0        0        0     1302 1970-01-01 00:00:00.000000 longbridge-0.2.9/local_dependencies/longbridge/Cargo.toml
+-rw-r--r--   0      501       20      251 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/CHANGELOG.md
+-rw-r--r--   0      501       20    46817 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/Cargo.lock
+-rw-r--r--   0      501       20       78 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/Makefile.toml
+-rw-r--r--   0      501       20     4188 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/README.md
+-rw-r--r--   0      501       20      497 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/examples/pull_quotes.rs
+-rw-r--r--   0      501       20      770 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/examples/submit_order.rs
+-rw-r--r--   0      501       20      555 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/examples/subscribe_quote.rs
+-rw-r--r--   0      501       20      147 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/blocking/error.rs
+-rw-r--r--   0      501       20      184 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/blocking/mod.rs
+-rw-r--r--   0      501       20    18977 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/blocking/quote.rs
+-rw-r--r--   0      501       20     3524 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/blocking/runtime.rs
+-rw-r--r--   0      501       20    10975 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/blocking/trade.rs
+-rw-r--r--   0      501       20     3399 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/config.rs
+-rw-r--r--   0      501       20     1347 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/error.rs
+-rw-r--r--   0      501       20      530 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/lib.rs
+-rw-r--r--   0      501       20     1520 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/macros.rs
+-rw-r--r--   0      501       20     1934 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/cache.rs
+-rw-r--r--   0      501       20     1652 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/cmd_code.rs
+-rw-r--r--   0      501       20    31715 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/context.rs
+-rw-r--r--   0      501       20    13306 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/core.rs
+-rw-r--r--   0      501       20      854 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/mod.rs
+-rw-r--r--   0      501       20     5190 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/push_types.rs
+-rw-r--r--   0      501       20     3739 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/store.rs
+-rw-r--r--   0      501       20     1494 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/sub_flags.rs
+-rw-r--r--   0      501       20    23404 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/types.rs
+-rw-r--r--   0      501       20      350 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/quote/utils.rs
+-rw-r--r--   0      501       20      284 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/cmd_code.rs
+-rw-r--r--   0      501       20    15942 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/context.rs
+-rw-r--r--   0      501       20     7233 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/core.rs
+-rw-r--r--   0      501       20      836 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/mod.rs
+-rw-r--r--   0      501       20     3095 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/push_types.rs
+-rw-r--r--   0      501       20     1663 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_cash_flow.rs
+-rw-r--r--   0      501       20      663 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_fund_positions.rs
+-rw-r--r--   0      501       20     1381 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_history_executions.rs
+-rw-r--r--   0      501       20     2277 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_history_orders.rs
+-rw-r--r--   0      501       20      668 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_stock_positions.rs
+-rw-r--r--   0      501       20      909 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_today_executions.rs
+-rw-r--r--   0      501       20     1524 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_today_orders.rs
+-rw-r--r--   0      501       20      663 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/mod.rs
+-rw-r--r--   0      501       20     2476 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/replace_order.rs
+-rw-r--r--   0      501       20     3622 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/submit_order.rs
+-rw-r--r--   0      501       20     6411 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/serde_utils.rs
+-rw-r--r--   0      501       20    27979 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/trade/types.rs
+-rw-r--r--   0      501       20      378 2022-06-03 01:44:16.000000 longbridge-0.2.9/local_dependencies/longbridge/src/types.rs
+-rw-r--r--   0        0        0      852 1970-01-01 00:00:00.000000 longbridge-0.2.9/Cargo.toml
+-rw-r--r--   0      501       20      210 2022-06-03 01:44:16.000000 longbridge-0.2.9/.cargo/config.toml
+-rw-r--r--   0      501       20        4 2022-06-03 01:44:16.000000 longbridge-0.2.9/.gitignore
+-rw-r--r--   0      501       20      252 2022-06-03 01:44:16.000000 longbridge-0.2.9/CHANGELOG.md
+-rw-r--r--   0      501       20      382 2022-06-03 01:44:16.000000 longbridge-0.2.9/Makefile.toml
+-rw-r--r--   0      501       20     2529 2022-06-03 01:44:16.000000 longbridge-0.2.9/README.md
+-rw-r--r--   0      501       20       71 2022-06-03 01:44:16.000000 longbridge-0.2.9/build.rs
+-rw-r--r--   0      501       20       40 2022-06-03 01:44:16.000000 longbridge-0.2.9/docs/config.md
+-rw-r--r--   0      501       20     2490 2022-06-03 01:44:16.000000 longbridge-0.2.9/docs/index.md
+-rw-r--r--   0      501       20       52 2022-06-03 01:44:16.000000 longbridge-0.2.9/docs/quote_context.md
+-rw-r--r--   0      501       20       41 2022-06-03 01:44:16.000000 longbridge-0.2.9/docs/reference_all.md
+-rw-r--r--   0      501       20       91 2022-06-03 01:44:16.000000 longbridge-0.2.9/docs/requirements.txt
+-rw-r--r--   0      501       20       52 2022-06-03 01:44:16.000000 longbridge-0.2.9/docs/trade_context.md
+-rw-r--r--   0      501       20      731 2022-06-03 01:44:16.000000 longbridge-0.2.9/mkdocs.yml
+-rw-r--r--   0      501       20      817 2022-06-03 01:44:16.000000 longbridge-0.2.9/pyproject.toml
+-rw-r--r--   0      501       20       89 2022-06-03 01:44:16.000000 longbridge-0.2.9/pysrc/longbridge/__init__.py
+-rw-r--r--   0      501       20        0 2022-06-03 01:44:16.000000 longbridge-0.2.9/pysrc/longbridge/openapi.py
+-rw-r--r--   0      501       20    51906 2022-06-03 01:44:16.000000 longbridge-0.2.9/pysrc/longbridge/openapi.pyi
+-rw-r--r--   0      501       20        0 2022-06-03 01:44:16.000000 longbridge-0.2.9/pysrc/longbridge/py.typed
+-rw-r--r--   0      501       20      982 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/config.rs
+-rw-r--r--   0      501       20     2206 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/decimal.rs
+-rw-r--r--   0      501       20      395 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/error.rs
+-rw-r--r--   0      501       20      584 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/lib.rs
+-rw-r--r--   0      501       20     7065 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/quote/context.rs
+-rw-r--r--   0      501       20     1616 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/quote/mod.rs
+-rw-r--r--   0      501       20     1801 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/quote/push.rs
+-rw-r--r--   0      501       20    15057 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/quote/types.rs
+-rw-r--r--   0      501       20     3554 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/time.rs
+-rw-r--r--   0      501       20    10210 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/trade/context.rs
+-rw-r--r--   0      501       20      653 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/trade/mod.rs
+-rw-r--r--   0      501       20      632 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/trade/push.rs
+-rw-r--r--   0      501       20    11528 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/trade/types.rs
+-rw-r--r--   0      501       20      328 2022-06-03 01:44:16.000000 longbridge-0.2.9/src/types.rs
+-rw-r--r--   0        0        0     3356 1970-01-01 00:00:00.000000 longbridge-0.2.9/PKG-INFO
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-python-macros/src/error.rs` & `longbridge-0.2.9/local_dependencies/longbridge-python-macros/src/error.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-python-macros/src/lib.rs` & `longbridge-0.2.9/local_dependencies/longbridge-python-macros/src/lib.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-python-macros/src/pyenum.rs` & `longbridge-0.2.9/local_dependencies/longbridge-python-macros/src/pyobject.rs`

 * *Files 22% similar despite different names*

```diff
@@ -1,81 +1,106 @@
-use darling::{
-    ast::{Data, Fields},
-    util::Ignored,
-    FromDeriveInput, FromVariant,
-};
+use darling::{ast::Data, util::Ignored, FromDeriveInput, FromField};
 use proc_macro2::TokenStream;
 use quote::quote;
-use syn::{DeriveInput, Error, Ident, TypePath};
+use syn::{DeriveInput, Error, Ident, Type, TypePath};
 
 use crate::error::GeneratorResult;
 
-#[derive(FromVariant)]
+#[derive(FromField)]
 #[darling(attributes(py), forward_attrs(doc))]
-struct EnumItem {
-    ident: Ident,
-    fields: Fields<Ignored>,
+struct ObjectField {
+    ident: Option<Ident>,
+    ty: Type,
 
     #[darling(default)]
-    from: Option<Ident>,
+    array: bool,
+    #[darling(default)]
+    opt: bool,
 }
 
 #[derive(FromDeriveInput)]
 #[darling(attributes(py), forward_attrs(doc))]
-struct EnumArgs {
+struct ObjectArgs {
     ident: Ident,
-    data: Data<EnumItem, Ignored>,
+    data: Data<Ignored, ObjectField>,
 
-    from: TypePath,
+    remote: TypePath,
 }
 
 pub(crate) fn generate(args: DeriveInput) -> GeneratorResult<TokenStream> {
-    let EnumArgs { ident, data, from } = EnumArgs::from_derive_input(&args)?;
-
-    let e = match data {
-        Data::Enum(e) => e,
-        _ => return Err(Error::new_spanned(ident, "Can only be applied to an enum.").into()),
+    let ObjectArgs {
+        ident,
+        data,
+        remote,
+    } = ObjectArgs::from_derive_input(&args)?;
+
+    let s = match data {
+        Data::Struct(s) => s,
+        _ => return Err(Error::new_spanned(ident, "can only be applied to an struct").into()),
     };
 
-    let mut from_remote = Vec::new();
-    let mut from_local = Vec::new();
+    let mut getters = Vec::new();
+    let mut from_fields = Vec::new();
 
-    for variant in e {
-        if !variant.fields.is_empty() {
-            return Err(Error::new_spanned(
-                &variant.ident,
-                format!("Invalid enum variant {}.", variant.ident),
-            )
-            .into());
-        }
-
-        let item_ident = &variant.ident;
-        let remote_ident = variant.from.as_ref().unwrap_or(&variant.ident);
-
-        from_remote.push(quote! {
-            #from::#remote_ident => #ident::#item_ident,
-        });
-        from_local.push(quote! {
-            #ident::#item_ident => #from::#remote_ident,
+    for field in &s.fields {
+        let field_ident = field.ident.as_ref().unwrap();
+        let field_type = &field.ty;
+
+        getters.push(quote! {
+            #[getter]
+            #[inline]
+            fn #field_ident(&self) -> #field_type {
+                self.#field_ident.clone()
+            }
         });
+
+        if field.array {
+            from_fields.push(quote! {
+                #field_ident: value.#field_ident
+                    .into_iter()
+                    .map(TryInto::try_into)
+                    .collect::<Result<::std::vec::Vec<_>, _>>()?,
+            });
+        } else if field.opt {
+            from_fields.push(quote! {
+                #field_ident: match value.#field_ident {
+                    ::std::option::Option::Some(value) => ::std::option::Option::Some(value.try_into()?),
+                    ::std::option::Option::None => ::std::option::Option::None,
+                },
+            });
+        } else {
+            from_fields.push(quote! {
+                #field_ident: value.#field_ident.try_into()?,
+            });
+        }
     }
 
     let expanded = quote! {
-        impl ::std::convert::From<#from> for #ident {
-            fn from(value: #from) -> #ident {
-                match value {
-                    #(#from_remote)*
-                }
+        #[::pyo3::pymethods]
+        impl #ident {
+            fn __repr__(&self) -> String {
+                ::std::format!("{:?}", self)
             }
+
+            fn __str__(&self) -> String {
+                ::std::format!("{:?}", self)
+            }
+
+            #(#getters)*
         }
 
-        impl ::std::convert::From<#ident> for #from {
-            fn from(value: #ident) -> #from {
-                match value {
-                    #(#from_local)*
-                }
+        impl ::std::convert::TryFrom<#remote> for #ident {
+            type Error = ::pyo3::PyErr;
+
+            fn try_from(value: #remote) -> ::std::result::Result<Self, Self::Error> {
+                use ::std::convert::TryInto;
+                use ::std::iter::Iterator;
+
+                Ok(Self {
+                    #(#from_fields)*
+                })
             }
         }
     };
 
     Ok(expanded)
 }
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/Cargo.toml` & `longbridge-0.2.9/local_dependencies/longbridge/Cargo.toml`

 * *Files 19% similar despite different names*

```diff
@@ -1,43 +1,42 @@
 [package]
 edition = "2021"
 name = "longbridge"
-version = "0.2.8"
+version = "0.2.9"
 description = "Longbridge OpenAPI SDK for Rust"
 homepage = "https://open.longbridgeapp.com/en/"
 readme = "README.md"
 repository = "https://github.com/longbridgeapp/openapi-sdk"
 license = "MIT OR Apache-2.0"
 keywords = ["longbridge", "openapi", "sdk"]
 categories = ["api-bindings"]
 
 [features]
-blocking = []
+blocking = ["flume"]
 
 [dependencies]
-longbridge-wscli = { path = "../longbridge-wscli", version = "0.2.8" }
-longbridge-httpcli = { path = "../longbridge-httpcli", version = "0.2.8" }
-longbridge-proto = { path = "../longbridge-proto", version = "0.2.8" }
+longbridge-wscli = { path = "../longbridge-wscli", version = "0.2.9" }
+longbridge-httpcli = { path = "../longbridge-httpcli", version = "0.2.9" }
+longbridge-proto = { path = "../longbridge-proto", version = "0.2.9" }
 
 tokio = { version = "1.18.2", features = [
     "time",
     "rt",
     "macros",
     "sync",
     "net",
 ] }
 rust_decimal = { version = "1.23.1", features = ["serde-with-str"] }
 num_enum = "0.5.7"
-anyhow = "1.0.57"
 prost = "0.10.3"
 tracing = "0.1.34"
 bitflags = "1.3.2"
 futures-util = "0.3.21"
 time = { version = "0.3.9", features = ["parsing", "macros", "formatting"] }
-flume = "0.10.12"
+flume = { version = "0.10.12", optional = true }
 thiserror = "1.0.31"
 strum = "0.24.0"
 strum_macros = "0.24.0"
 serde = "1.0.137"
 serde_json = "1.0.81"
 num-traits = "0.2.15"
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/Cargo.lock` & `longbridge-0.2.9/local_dependencies/longbridge/Cargo.lock`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/README.md` & `longbridge-0.2.9/local_dependencies/longbridge/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -46,24 +46,24 @@
 setx LONGBRIDGE_APP_SECRET "App Secret get from user center"
 setx LONGBRIDGE_ACCESS_TOKEN "Access Token get from user center"
 ```
 
 ## Quote API _(Get basic information of securities)_
 
 ```rust,no_run
-use std::{error::Error, sync::Arc};
+use std::sync::Arc;
 
 use longbridge::{
     decimal,
     trade::{OrderSide, OrderType, SubmitOrderOptions, TimeInForceType},
     Config, QuoteContext, TradeContext,
 };
 
 #[tokio::main]
-async fn main() -> Result<(), Box<dyn Error>> {
+async fn main() -> Result<(), Box<dyn std::error::Error>> {
     // Load configuration from environment variables
     let config = Arc::new(Config::from_env()?);
 
     // Create a context for quote APIs
     let (ctx, _) = QuoteContext::try_new(config.clone()).await?;
 
     // Get basic information of securities
@@ -77,19 +77,18 @@
 ```
 
 ## Quote API _(Subscribe quotes)_
 
 ```rust, no_run
 use std::sync::Arc;
 
-use anyhow::Result;
 use longbridge::{quote::SubFlags, Config, QuoteContext};
 
 #[tokio::main]
-async fn main() -> Result<()> {
+async fn main() -> Result<(), Box<dyn std::error::Error>> {
     // Load configuration from environment variables
     let config = Arc::new(Config::from_env()?);
 
     // Create a context for quote APIs
     let (ctx, mut receiver) = QuoteContext::try_new(config).await?;
 
     // Subscribe
@@ -105,23 +104,22 @@
 ```
 
 ## Trade API _(Submit order)_
 
 ```rust, no_run
 use std::sync::Arc;
 
-use anyhow::Result;
 use longbridge::{
     decimal,
     trade::{OrderSide, OrderType, SubmitOrderOptions, TimeInForceType},
     Config, TradeContext,
 };
 
 #[tokio::main]
-async fn main() -> Result<()> {
+async fn main() -> Result<(), Box<dyn std::error::Error>> {
     // Load configuration from environment variables
     let config = Arc::new(Config::from_env()?);
 
     // Create a context for trade APIs
     let (ctx, _) = TradeContext::try_new(config).await?;
 
     // Submit order
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/examples/subscribe_quote.rs` & `longbridge-0.2.9/local_dependencies/longbridge/examples/subscribe_quote.rs`

 * *Files 20% similar despite different names*

```diff
@@ -1,11 +1,10 @@
 use std::sync::Arc;
 
-use anyhow::Result;
-use longbridge::{quote::SubFlags, Config, QuoteContext};
+use longbridge::{quote::SubFlags, Config, QuoteContext, Result};
 
 #[tokio::main]
 async fn main() -> Result<()> {
     // Load configuration from environment variables
     let config = Arc::new(Config::from_env()?);
 
     // Create a context for quote APIs
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/blocking/quote.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/blocking/quote.rs`

 * *Files 17% similar despite different names*

```diff
@@ -1,21 +1,20 @@
 use std::sync::Arc;
 
-use anyhow::Result;
 use time::Date;
 
 use crate::{
     blocking::runtime::BlockingRuntime,
     quote::{
         AdjustType, Candlestick, IntradayLine, IssuerInfo, MarketTradingDays, MarketTradingSession,
         OptionQuote, ParticipantInfo, Period, PushEvent, RealtimeQuote, SecurityBrokers,
         SecurityDepth, SecurityQuote, SecurityStaticInfo, StrikePriceInfo, SubFlags, Trade,
         WarrantQuote,
     },
-    Config, Market, QuoteContext,
+    Config, Market, QuoteContext, Result,
 };
 
 /// Quote context
 pub struct QuoteContextSync {
     rt: BlockingRuntime<QuoteContext>,
 }
 
@@ -42,15 +41,15 @@
     ///     Config,
     /// };
     ///
     /// fn event_handler(event: PushEvent) {
     ///     println!("{:?}", event);
     /// }
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, event_handler)?;
     ///
     /// ctx.subscribe(["700.HK", "AAPL.US"], SubFlags::QUOTE, false)?;
     /// sleep(Duration::from_secs(30));
     /// # Ok(())
     /// # }
@@ -73,15 +72,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, quote::SubFlags, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.subscribe(["700.HK", "AAPL.US"], SubFlags::QUOTE, false)?;
     /// ctx.subscribe(["AAPL.US"], SubFlags::QUOTE, false)?;
     /// # Ok(())
     /// # }
@@ -102,15 +101,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.static_info(["700.HK", "AAPL.US", "TSLA.US", "NFLX.US"])?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -130,15 +129,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.quote(["700.HK", "AAPL.US", "TSLA.US", "NFLX.US"])?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -158,15 +157,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.option_quote(["AAPL230317P160000.US"])?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -186,15 +185,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.warrant_quote(["21125.HK"])?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -214,15 +213,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.depth("700.HK")?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -237,15 +236,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.brokers("700.HK")?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -260,15 +259,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.participants()?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -283,15 +282,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.trades("700.HK", 10)?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -310,15 +309,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.intraday("700.HK")?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -340,15 +339,15 @@
     ///
     /// use longbridge::{
     ///     blocking::QuoteContextSync,
     ///     quote::{AdjustType, Period},
     ///     Config,
     /// };
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.candlesticks("700.HK", Period::Day, 10, AdjustType::NoAdjust)?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -370,15 +369,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.option_chain_expiry_date_list("AAPL.US")?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -397,15 +396,15 @@
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     /// use time::macros::date;
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.option_chain_info_by_date("AAPL.US", date!(2023 - 01 - 20))?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -425,15 +424,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.warrant_issuers()?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -448,15 +447,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.trading_session()?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -475,15 +474,15 @@
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::QuoteContextSync, Config, Market};
     /// use time::macros::date;
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// let resp = ctx.trading_days(Market::HK, date!(2022 - 01 - 20), date!(2022 - 02 - 20))?;
     /// println!("{:?}", resp);
     /// # Ok(())
     /// # }
@@ -506,15 +505,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::{sync::Arc, thread::sleep, time::Duration};
     ///
     /// use longbridge::{blocking::QuoteContextSync, quote::SubFlags, Config, Market};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::QUOTE, true)?;
     /// sleep(Duration::from_secs(5));
     ///
     /// let resp = ctx.realtime_quote(["HK.700", "AAPL.US"])?;
@@ -540,15 +539,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::{sync::Arc, thread::sleep, time::Duration};
     ///
     /// use longbridge::{blocking::QuoteContextSync, quote::SubFlags, Config, Market};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::DEPTH, true)?;
     /// sleep(Duration::from_secs(5));
     ///
     /// let resp = ctx.realtime_depth("HK.700")?;
@@ -572,15 +571,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::{sync::Arc, thread::sleep, time::Duration};
     ///
     /// use longbridge::{blocking::QuoteContextSync, quote::SubFlags, Config, Market};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::TRADE, false)?;
     /// sleep(Duration::from_secs(5));
     ///
     /// let resp = ctx.realtime_trades("HK.700", 10)?;
@@ -605,15 +604,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::{sync::Arc, thread::sleep, time::Duration};
     ///
     /// use longbridge::{blocking::QuoteContextSync, quote::SubFlags, Config, Market};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = QuoteContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::BROKER, false)?;
     /// sleep(Duration::from_secs(5));
     ///
     /// let resp = ctx.realtime_brokers("HK.700")?;
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/blocking/runtime.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/blocking/runtime.rs`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 use std::{sync::Arc, thread};
 
-use anyhow::Result;
 use futures_util::{future::BoxFuture, Future};
 use tokio::sync::mpsc;
 
-use crate::blocking::BlockingError;
+use crate::{blocking::BlockingError, Result};
 
 const THREAD_NAME: &str = "longbridge-sync-runtime";
 
 type ExecFn<Ctx> = Box<dyn FnOnce(Arc<Ctx>) -> BoxFuture<'static, ()> + Send + 'static>;
 
 pub(crate) struct BlockingRuntime<Ctx> {
     task_tx: flume::Sender<ExecFn<Ctx>>,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/blocking/trade.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/blocking/trade.rs`

 * *Files 6% similar despite different names*

```diff
@@ -1,21 +1,19 @@
 use std::sync::Arc;
 
-use anyhow::Result;
-
 use crate::{
     blocking::runtime::BlockingRuntime,
     trade::{
         AccountBalance, CashFlow, Execution, FundPositionsResponse, GetCashFlowOptions,
         GetFundPositionsOptions, GetHistoryExecutionsOptions, GetHistoryOrdersOptions,
         GetStockPositionsOptions, GetTodayExecutionsOptions, GetTodayOrdersOptions, Order,
         PushEvent, ReplaceOrderOptions, StockPositionsResponse, SubmitOrderOptions,
         SubmitOrderResponse, TopicType, TradeContext,
     },
-    Config,
+    Config, Result,
 };
 
 /// Trade context
 pub struct TradeContextSync {
     rt: BlockingRuntime<TradeContext>,
 }
 
@@ -53,15 +51,15 @@
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, trade::GetHistoryExecutionsOptions, Config};
     /// use time::macros::datetime;
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// let opts = GetHistoryExecutionsOptions::new().symbol("700.HK")
     ///     .start_at(datetime!(2022-05-09 0:00 UTC))
     ///     .end_at(datetime!(2022-05-12 0:00 UTC));
     /// let resp = ctx.history_executions(opts)?;
@@ -83,15 +81,15 @@
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, trade::GetTodayExecutionsOptions, Config};
     /// use time::macros::datetime;
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// let opts = GetTodayExecutionsOptions::new().symbol("700.HK");
     /// let resp = ctx.today_executions(opts)?;
     /// println!("{:?}", resp);
     /// # Ok(())
@@ -115,15 +113,15 @@
     /// use longbridge::{
     ///     blocking::TradeContextSync,
     ///     trade::{GetHistoryOrdersOptions, OrderSide, OrderStatus},
     ///     Config, Market,
     /// };
     /// use time::macros::datetime;
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// let opts = GetHistoryOrdersOptions::new()
     ///     .symbol("700.HK")
     ///     .status([OrderStatus::Filled, OrderStatus::New])
     ///     .side(OrderSide::Buy)
@@ -152,15 +150,15 @@
     ///
     /// use longbridge::{
     ///     blocking::TradeContextSync,
     ///     trade::{GetTodayOrdersOptions, OrderSide, OrderStatus},
     ///     Config, Market,
     /// };
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// let opts = GetTodayOrdersOptions::new()
     ///     .symbol("700.HK")
     ///     .status([OrderStatus::Filled, OrderStatus::New])
     ///     .side(OrderSide::Buy)
@@ -183,15 +181,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, decimal, trade::ReplaceOrderOptions, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// let opts =
     ///     ReplaceOrderOptions::new("709043056541253632", decimal!(100i32)).price(decimal!(300i32));
     /// let resp = ctx.replace_order(opts)?;
     /// println!("{:?}", resp);
@@ -213,15 +211,15 @@
     /// use longbridge::{
     ///     blocking::TradeContextSync,
     ///     decimal,
     ///     trade::{OrderSide, OrderType, SubmitOrderOptions, TimeInForceType},
     ///     Config,
     /// };
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// let opts = SubmitOrderOptions::new(
     ///     "700.HK",
     ///     OrderType::LO,
     ///     OrderSide::Buy,
@@ -244,15 +242,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.withdraw_order("709043056541253632")?;
     /// # Ok(())
     /// # }
     /// ```
@@ -266,15 +264,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.account_balance()?;
     /// # Ok(())
     /// # }
     /// ```
@@ -289,15 +287,15 @@
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, trade::GetCashFlowOptions, Config};
     /// use time::macros::datetime;
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// let opts = GetCashFlowOptions::new(datetime!(2022-05-09 0:00 UTC), datetime!(2022-05-12 0:00 UTC));
     /// ctx.cash_flow(opts)?;
     /// # Ok(())
     /// # }
@@ -312,15 +310,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.fund_positions(None)?;
     /// # Ok(())
     /// # }
     /// ```
@@ -337,15 +335,15 @@
     /// # Examples
     ///
     /// ```no_run
     /// use std::sync::Arc;
     ///
     /// use longbridge::{blocking::TradeContextSync, Config};
     ///
-    /// # fn main() -> anyhow::Result<()> {
+    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
     /// let config = Arc::new(Config::from_env()?);
     /// let ctx = TradeContextSync::try_new(config, |_| ())?;
     ///
     /// ctx.stock_positions(None)?;
     /// # Ok(())
     /// # }
     /// ```
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/config.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/config.rs`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,11 @@
-use anyhow::Result;
 use longbridge_httpcli::{HttpClient, HttpClientConfig};
 
+use crate::error::Result;
+
 const QUOTE_WS_URL: &str = "wss://openapi-quote.longbridgeapp.com";
 const TRADE_WS_URL: &str = "wss://openapi-trade.longbridgeapp.com";
 
 /// Configuration options for Longbridge sdk
 #[derive(Debug, Clone)]
 pub struct Config {
     pub(crate) http_cli_config: HttpClientConfig,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/macros.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/macros.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/cache.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/cache.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/cmd_code.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/cmd_code.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/context.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/context.rs`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 use std::{sync::Arc, time::Duration};
 
-use anyhow::Result;
 use longbridge_proto::quote;
 use longbridge_wscli::WsClientError;
 use time::Date;
 use tokio::sync::{mpsc, oneshot};
 
 use crate::{
     quote::{
@@ -13,15 +12,15 @@
         core::{Command, Core},
         sub_flags::SubFlags,
         utils::{format_date, parse_date},
         AdjustType, Candlestick, IntradayLine, IssuerInfo, MarketTradingDays, MarketTradingSession,
         OptionQuote, ParticipantInfo, Period, PushEvent, RealtimeQuote, SecurityBrokers,
         SecurityDepth, SecurityQuote, SecurityStaticInfo, StrikePriceInfo, Trade, WarrantQuote,
     },
-    Config, Market,
+    Config, Error, Market, Result,
 };
 
 const PARTICIPANT_INFO_CACHE_TIMEOUT: Duration = Duration::from_secs(30 * 60);
 const ISSUER_INFO_CACHE_TIMEOUT: Duration = Duration::from_secs(30 * 60);
 const OPTION_CHAIN_EXPIRY_DATE_LIST_CACHE_TIMEOUT: Duration = Duration::from_secs(30 * 60);
 const OPTION_CHAIN_STRIKE_INFO_CACHE_TIMEOUT: Duration = Duration::from_secs(30 * 60);
 const TRADING_SESSION_CACHE_TIMEOUT: Duration = Duration::from_secs(60 * 60 * 2);
@@ -113,32 +112,32 @@
     /// let (ctx, mut receiver) = QuoteContext::try_new(config).await?;
     ///
     /// ctx.subscribe(["700.HK", "AAPL.US"], SubFlags::QUOTE, false)
     ///     .await?;
     /// while let Some(msg) = receiver.recv().await {
     ///     println!("{:?}", msg);
     /// }
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn subscribe<I, T>(
         &self,
         symbols: I,
-        sub_types: SubFlags,
+        sub_types: impl Into<SubFlags>,
         is_first_push: bool,
     ) -> Result<()>
     where
         I: IntoIterator<Item = T>,
         T: Into<String>,
     {
         let (reply_tx, reply_rx) = oneshot::channel();
         self.command_tx
             .send(Command::Subscribe {
                 symbols: symbols.into_iter().map(Into::into).collect(),
-                sub_types,
+                sub_types: sub_types.into(),
                 is_first_push,
                 reply_tx,
             })
             .map_err(|_| WsClientError::ClientClosed)?;
         reply_rx.await.map_err(|_| WsClientError::ClientClosed)?
     }
 
@@ -159,27 +158,27 @@
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// ctx.subscribe(["700.HK", "AAPL.US"], SubFlags::QUOTE, false)
     ///     .await?;
     /// ctx.unsubscribe(["AAPL.US"], SubFlags::QUOTE).await?;
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
-    pub async fn unsubscribe<I, T>(&self, symbols: I, sub_types: SubFlags) -> Result<()>
+    pub async fn unsubscribe<I, T>(&self, symbols: I, sub_types: impl Into<SubFlags>) -> Result<()>
     where
         I: IntoIterator<Item = T>,
         T: Into<String>,
     {
         let (reply_tx, reply_rx) = oneshot::channel();
         self.command_tx
             .send(Command::Unsubscribe {
                 symbols: symbols.into_iter().map(Into::into).collect(),
-                sub_types,
+                sub_types: sub_types.into(),
                 reply_tx,
             })
             .map_err(|_| WsClientError::ClientClosed)?;
         reply_rx.await.map_err(|_| WsClientError::ClientClosed)?
     }
 
     /// Get basic information of securities
@@ -197,15 +196,15 @@
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx
     ///     .static_info(["700.HK", "AAPL.US", "TSLA.US", "NFLX.US"])
     ///     .await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn static_info<I, T>(&self, symbols: I) -> Result<Vec<SecurityStaticInfo>>
     where
         I: IntoIterator<Item = T>,
         T: Into<String>,
     {
@@ -238,15 +237,15 @@
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx
     ///     .quote(["700.HK", "AAPL.US", "TSLA.US", "NFLX.US"])
     ///     .await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn quote<I, T>(&self, symbols: I) -> Result<Vec<SecurityQuote>>
     where
         I: IntoIterator<Item = T>,
         T: Into<String>,
     {
@@ -274,15 +273,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.option_quote(["AAPL230317P160000.US"]).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn option_quote<I, T>(&self, symbols: I) -> Result<Vec<OptionQuote>>
     where
         I: IntoIterator<Item = T>,
         T: Into<String>,
     {
@@ -310,15 +309,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.warrant_quote(["21125.HK"]).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn warrant_quote<I, T>(&self, symbols: I) -> Result<Vec<WarrantQuote>>
     where
         I: IntoIterator<Item = T>,
         T: Into<String>,
     {
@@ -346,15 +345,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.depth("700.HK").await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn depth(&self, symbol: impl Into<String>) -> Result<SecurityDepth> {
         let resp: quote::SecurityDepthResponse = self
             .request(
                 cmd_code::GET_SECURITY_DEPTH,
                 quote::SecurityRequest {
@@ -389,15 +388,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.brokers("700.HK").await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn brokers(&self, symbol: impl Into<String>) -> Result<SecurityBrokers> {
         let resp: quote::SecurityBrokersResponse = self
             .request(
                 cmd_code::GET_SECURITY_BROKERS,
                 quote::SecurityRequest {
@@ -424,15 +423,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.participants().await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn participants(&self) -> Result<Vec<ParticipantInfo>> {
         self.cache_participants
             .get_or_update(|| async {
                 let resp = self
                     .request_without_body::<quote::ParticipantBrokerIdsResponse>(
@@ -462,15 +461,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.trades("700.HK", 10).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn trades(&self, symbol: impl Into<String>, count: usize) -> Result<Vec<Trade>> {
         let resp: quote::SecurityTradeResponse = self
             .request(
                 cmd_code::GET_SECURITY_TRADES,
                 quote::SecurityTradeRequest {
@@ -500,15 +499,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.intraday("700.HK").await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn intraday(&self, symbol: impl Into<String>) -> Result<Vec<IntradayLine>> {
         let resp: quote::SecurityIntradayResponse = self
             .request(
                 cmd_code::GET_SECURITY_INTRADAY,
                 quote::SecurityIntradayRequest {
@@ -542,15 +541,15 @@
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx
     ///     .candlesticks("700.HK", Period::Day, 10, AdjustType::NoAdjust)
     ///     .await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn candlesticks(
         &self,
         symbol: impl Into<String>,
         period: Period,
         count: usize,
@@ -588,15 +587,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.option_chain_expiry_date_list("AAPL.US").await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn option_chain_expiry_date_list(
         &self,
         symbol: impl Into<String>,
     ) -> Result<Vec<Date>> {
         self.cache_option_chain_expiry_date_list
@@ -605,15 +604,17 @@
                     .request(
                         cmd_code::GET_OPTION_CHAIN_EXPIRY_DATE_LIST,
                         quote::SecurityRequest { symbol },
                     )
                     .await?;
                 resp.expiry_date
                     .iter()
-                    .map(|value| parse_date(value))
+                    .map(|value| {
+                        parse_date(value).map_err(|err| Error::parse_field_error("date", err))
+                    })
                     .collect::<Result<Vec<_>>>()
             })
             .await
     }
 
     /// Get option chain info by date
     ///
@@ -631,15 +632,15 @@
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx
     ///     .option_chain_info_by_date("AAPL.US", date!(2023 - 01 - 20))
     ///     .await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn option_chain_info_by_date(
         &self,
         symbol: impl Into<String>,
         expiry_date: Date,
     ) -> Result<Vec<StrikePriceInfo>> {
@@ -678,15 +679,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.warrant_issuers().await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn warrant_issuers(&self) -> Result<Vec<IssuerInfo>> {
         self.cache_issuers
             .get_or_update(|| async {
                 let resp = self
                     .request_without_body::<quote::IssuerInfoResponse>(
@@ -711,15 +712,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx.trading_session().await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn trading_session(&self) -> Result<Vec<MarketTradingSession>> {
         self.cache_trading_session
             .get_or_update(|| async {
                 let resp = self
                     .request_without_body::<quote::MarketTradePeriodResponse>(
@@ -753,15 +754,15 @@
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = QuoteContext::try_new(config).await?;
     ///
     /// let resp = ctx
     ///     .trading_days(Market::HK, date!(2022 - 01 - 20), date!(2022 - 02 - 20))
     ///     .await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn trading_days(
         &self,
         market: Market,
         begin: Date,
         end: Date,
@@ -775,20 +776,24 @@
                     end_day: format_date(end),
                 },
             )
             .await?;
         let trading_days = resp
             .trade_day
             .iter()
-            .map(|value| parse_date(value))
+            .map(|value| {
+                parse_date(value).map_err(|err| Error::parse_field_error("trade_day", err))
+            })
             .collect::<Result<Vec<_>>>()?;
         let half_trading_days = resp
             .half_trade_day
             .iter()
-            .map(|value| parse_date(value))
+            .map(|value| {
+                parse_date(value).map_err(|err| Error::parse_field_error("half_trade_day", err))
+            })
             .collect::<Result<Vec<_>>>()?;
         Ok(MarketTradingDays {
             trading_days,
             half_trading_days,
         })
     }
 
@@ -813,15 +818,15 @@
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::QUOTE, true)
     ///     .await?;
     /// tokio::time::sleep(Duration::from_secs(5)).await;
     ///
     /// let resp = ctx.realtime_quote(["HK.700", "AAPL.US"]).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn realtime_quote<I, T>(&self, symbols: I) -> Result<Vec<RealtimeQuote>>
     where
         I: IntoIterator<Item = T>,
         T: Into<String>,
     {
@@ -856,15 +861,15 @@
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::DEPTH, true)
     ///     .await?;
     /// tokio::time::sleep(Duration::from_secs(5)).await;
     ///
     /// let resp = ctx.realtime_depth("HK.700").await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn realtime_depth(&self, symbol: impl Into<String>) -> Result<SecurityDepth> {
         let (reply_tx, reply_rx) = oneshot::channel();
         self.command_tx
             .send(Command::GetRealtimeDepth {
                 symbol: symbol.into(),
@@ -895,15 +900,15 @@
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::TRADE, false)
     ///     .await?;
     /// tokio::time::sleep(Duration::from_secs(5)).await;
     ///
     /// let resp = ctx.realtime_trades("HK.700", 10).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn realtime_trades(
         &self,
         symbol: impl Into<String>,
         count: usize,
     ) -> Result<Vec<Trade>> {
@@ -940,15 +945,15 @@
     ///
     /// ctx.subscribe(["HK.700", "AAPL.US"], SubFlags::BROKER, true)
     ///     .await?;
     /// tokio::time::sleep(Duration::from_secs(5)).await;
     ///
     /// let resp = ctx.realtime_brokers("HK.700").await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn realtime_brokers(&self, symbol: impl Into<String>) -> Result<SecurityBrokers> {
         let (reply_tx, reply_rx) = oneshot::channel();
         self.command_tx
             .send(Command::GetRealtimeBrokers {
                 symbol: symbol.into(),
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/core.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/core.rs`

 * *Files 1% similar despite different names*

```diff
@@ -1,20 +1,19 @@
 use std::{collections::HashMap, sync::Arc, time::Duration};
 
-use anyhow::Result;
 use longbridge_proto::quote::{SubscribeRequest, SubscriptionResponse, UnsubscribeRequest};
 use longbridge_wscli::{CodecType, Platform, ProtocolVersion, WsClient, WsEvent, WsSession};
 use tokio::sync::{mpsc, oneshot};
 
 use crate::{
     quote::{
         cmd_code, store::Store, sub_flags::SubFlags, PushEvent, RealtimeQuote, SecurityBrokers,
         SecurityDepth, Trade,
     },
-    Config,
+    Config, Result,
 };
 
 const RECONNECT_DELAY: Duration = Duration::from_secs(2);
 
 pub(crate) enum Command {
     Request {
         command_code: u8,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/mod.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/mod.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/push_types.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/push_types.rs`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,16 @@
-use anyhow::{Context, Result};
 use longbridge_proto::quote::{self, TradeSession, TradeStatus};
 use prost::Message;
 use rust_decimal::Decimal;
 use time::OffsetDateTime;
 
-use crate::quote::{cmd_code, Brokers, Depth, Trade};
+use crate::{
+    quote::{cmd_code, Brokers, Depth, Trade},
+    Error, Result,
+};
 
 /// Quote message
 #[derive(Debug, Clone)]
 pub struct PushQuote {
     /// Latest price
     pub last_done: Decimal,
     /// Open
@@ -92,36 +94,35 @@
     /// Event detail
     pub detail: PushEventDetail,
 }
 
 impl PushEvent {
     pub(crate) fn parse(command_code: u8, data: &[u8]) -> Result<PushEvent> {
         match command_code {
-            cmd_code::PUSH_REALTIME_QUOTE => parse_push_quote(data).context("decode push quote"),
-            cmd_code::PUSH_REALTIME_DEPTH => parse_push_depth(data).context("decode push depth"),
-            cmd_code::PUSH_REALTIME_BROKERS => {
-                parse_push_brokers(data).context("decode push brokers")
-            }
-            cmd_code::PUSH_REALTIME_TRADES => parse_push_trade(data).context("decode push trades"),
-            _ => anyhow::bail!("unknown command: {}", command_code),
+            cmd_code::PUSH_REALTIME_QUOTE => parse_push_quote(data),
+            cmd_code::PUSH_REALTIME_DEPTH => parse_push_depth(data),
+            cmd_code::PUSH_REALTIME_BROKERS => parse_push_brokers(data),
+            cmd_code::PUSH_REALTIME_TRADES => parse_push_trade(data),
+            _ => Err(Error::UnknownCommand(command_code)),
         }
     }
 }
 
 fn parse_push_quote(data: &[u8]) -> Result<PushEvent> {
     let push_quote = quote::PushQuote::decode(data)?;
     Ok(PushEvent {
         symbol: push_quote.symbol,
         sequence: push_quote.sequence,
         detail: PushEventDetail::Quote(PushQuote {
             last_done: push_quote.last_done.parse().unwrap_or_default(),
             open: push_quote.open.parse().unwrap_or_default(),
             high: push_quote.high.parse().unwrap_or_default(),
             low: push_quote.low.parse().unwrap_or_default(),
-            timestamp: OffsetDateTime::from_unix_timestamp(push_quote.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(push_quote.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
             volume: push_quote.volume,
             turnover: push_quote.turnover.parse().unwrap_or_default(),
             trade_status: TradeStatus::from_i32(push_quote.trade_status).unwrap_or_default(),
             trade_session: TradeSession::from_i32(push_quote.trade_session).unwrap_or_default(),
         }),
     })
 }
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/store.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/store.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/sub_flags.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/sub_flags.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/quote/types.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/quote/types.rs`

 * *Files 15% similar despite different names*

```diff
@@ -1,15 +1,14 @@
-use anyhow::{Error, Result};
 use longbridge_proto::quote::{self, TradeSession, TradeStatus};
 use num_enum::{FromPrimitive, IntoPrimitive, TryFromPrimitive};
 use rust_decimal::Decimal;
 use strum_macros::EnumString;
 use time::{Date, OffsetDateTime, Time};
 
-use crate::{quote::utils::parse_date, Market};
+use crate::{quote::utils::parse_date, Error, Market, Result};
 
 /// Depth
 #[derive(Debug, Clone)]
 pub struct Depth {
     /// Position
     pub position: i32,
     /// Price
@@ -19,15 +18,15 @@
     /// Number of orders
     pub order_num: i64,
 }
 
 impl TryFrom<quote::Depth> for Depth {
     type Error = Error;
 
-    fn try_from(depth: quote::Depth) -> Result<Self, Self::Error> {
+    fn try_from(depth: quote::Depth) -> Result<Self> {
         Ok(Self {
             position: depth.position,
             price: depth.price.parse().unwrap_or_default(),
             volume: depth.volume,
             order_num: depth.order_num,
         })
     }
@@ -51,17 +50,17 @@
     }
 }
 
 /// Trade direction
 #[derive(Debug, FromPrimitive, Copy, Clone, Hash, Eq, PartialEq)]
 #[repr(i32)]
 pub enum TradeDirection {
-    /// Nature
+    /// Neutral
     #[num_enum(default)]
-    Nature = 0,
+    Neutral = 0,
     /// Down
     Down = 1,
     /// Up
     Up = 2,
 }
 
 /// Trade
@@ -111,19 +110,20 @@
     /// Trade session
     pub trade_session: TradeSession,
 }
 
 impl TryFrom<quote::Trade> for Trade {
     type Error = Error;
 
-    fn try_from(trade: quote::Trade) -> Result<Self, Self::Error> {
+    fn try_from(trade: quote::Trade) -> Result<Self> {
         Ok(Self {
             price: trade.price.parse().unwrap_or_default(),
             volume: trade.volume,
-            timestamp: OffsetDateTime::from_unix_timestamp(trade.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(trade.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
             trade_type: trade.trade_type,
             direction: trade.direction.into(),
             trade_session: TradeSession::from_i32(trade.trade_session).unwrap_or_default(),
         })
     }
 }
 
@@ -171,15 +171,15 @@
     /// Types of supported derivatives
     pub stock_derivatives: Vec<DerivativeType>,
 }
 
 impl TryFrom<quote::StaticInfo> for SecurityStaticInfo {
     type Error = Error;
 
-    fn try_from(resp: quote::StaticInfo) -> Result<Self, Self::Error> {
+    fn try_from(resp: quote::StaticInfo) -> Result<Self> {
         Ok(SecurityStaticInfo {
             symbol: resp.symbol,
             name_cn: resp.name_cn,
             name_en: resp.name_en,
             name_hk: resp.name_hk,
             exchange: resp.exchange,
             currency: resp.currency,
@@ -241,18 +241,19 @@
     /// Close of the last trade session
     pub prev_close: Decimal,
 }
 
 impl TryFrom<quote::PrePostQuote> for PrePostQuote {
     type Error = Error;
 
-    fn try_from(quote: quote::PrePostQuote) -> Result<Self, Self::Error> {
+    fn try_from(quote: quote::PrePostQuote) -> Result<Self> {
         Ok(Self {
             last_done: quote.last_done.parse().unwrap_or_default(),
-            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
             volume: quote.volume,
             turnover: quote.turnover.parse().unwrap_or_default(),
             high: quote.high.parse().unwrap_or_default(),
             low: quote.low.parse().unwrap_or_default(),
             prev_close: quote.prev_close.parse().unwrap_or_default(),
         })
     }
@@ -286,23 +287,24 @@
     /// Quote of US post market
     pub post_market_quote: Option<PrePostQuote>,
 }
 
 impl TryFrom<quote::SecurityQuote> for SecurityQuote {
     type Error = Error;
 
-    fn try_from(quote: quote::SecurityQuote) -> Result<Self, Self::Error> {
+    fn try_from(quote: quote::SecurityQuote) -> Result<Self> {
         Ok(Self {
             symbol: quote.symbol,
             last_done: quote.last_done.parse().unwrap_or_default(),
             prev_close: quote.prev_close.parse().unwrap_or_default(),
             open: quote.open.parse().unwrap_or_default(),
             high: quote.high.parse().unwrap_or_default(),
             low: quote.low.parse().unwrap_or_default(),
-            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
             volume: quote.volume,
             turnover: quote.turnover.parse().unwrap_or_default(),
             trade_status: TradeStatus::from_i32(quote.trade_status).unwrap_or_default(),
             pre_market_quote: quote.pre_market_quote.map(TryInto::try_into).transpose()?,
             post_market_quote: quote.post_market_quote.map(TryInto::try_into).transpose()?,
         })
     }
@@ -380,31 +382,33 @@
     /// Underlying security symbol of the option
     pub underlying_symbol: String,
 }
 
 impl TryFrom<quote::OptionQuote> for OptionQuote {
     type Error = Error;
 
-    fn try_from(quote: quote::OptionQuote) -> Result<Self, Self::Error> {
+    fn try_from(quote: quote::OptionQuote) -> Result<Self> {
         let option_extend = quote.option_extend.unwrap_or_default();
 
         Ok(Self {
             symbol: quote.symbol,
             last_done: quote.last_done.parse().unwrap_or_default(),
             prev_close: quote.prev_close.parse().unwrap_or_default(),
             open: quote.open.parse().unwrap_or_default(),
             high: quote.high.parse().unwrap_or_default(),
             low: quote.low.parse().unwrap_or_default(),
-            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
             volume: quote.volume,
             turnover: quote.turnover.parse().unwrap_or_default(),
             trade_status: TradeStatus::from_i32(quote.trade_status).unwrap_or_default(),
             implied_volatility: option_extend.implied_volatility.parse().unwrap_or_default(),
             open_interest: option_extend.open_interest,
-            expiry_date: parse_date(&option_extend.expiry_date)?,
+            expiry_date: parse_date(&option_extend.expiry_date)
+                .map_err(|err| Error::parse_field_error("expiry_date", err))?,
             strike_price: option_extend.strike_price.parse().unwrap_or_default(),
             contract_multiplier: option_extend
                 .contract_multiplier
                 .parse()
                 .unwrap_or_default(),
             contract_type: option_extend.contract_type.parse().unwrap_or_default(),
             contract_size: option_extend.contract_size.parse().unwrap_or_default(),
@@ -485,34 +489,37 @@
     /// Underlying security symbol of the warrant
     pub underlying_symbol: String,
 }
 
 impl TryFrom<quote::WarrantQuote> for WarrantQuote {
     type Error = Error;
 
-    fn try_from(quote: quote::WarrantQuote) -> Result<Self, Self::Error> {
+    fn try_from(quote: quote::WarrantQuote) -> Result<Self> {
         let warrant_extend = quote.warrant_extend.unwrap_or_default();
 
         Ok(Self {
             symbol: quote.symbol,
             last_done: quote.last_done.parse().unwrap_or_default(),
             prev_close: quote.prev_close.parse().unwrap_or_default(),
             open: quote.open.parse().unwrap_or_default(),
             high: quote.high.parse().unwrap_or_default(),
             low: quote.low.parse().unwrap_or_default(),
-            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(quote.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
             volume: quote.volume,
             turnover: quote.turnover.parse().unwrap_or_default(),
             trade_status: TradeStatus::from_i32(quote.trade_status).unwrap_or_default(),
             implied_volatility: warrant_extend
                 .implied_volatility
                 .parse()
                 .unwrap_or_default(),
-            expiry_date: parse_date(&warrant_extend.expiry_date)?,
-            last_trade_date: parse_date(&warrant_extend.last_trade_date)?,
+            expiry_date: parse_date(&warrant_extend.expiry_date)
+                .map_err(|err| Error::parse_field_error("expiry_date", err))?,
+            last_trade_date: parse_date(&warrant_extend.last_trade_date)
+                .map_err(|err| Error::parse_field_error("last_trade_date", err))?,
             outstanding_ratio: warrant_extend.outstanding_ratio.parse().unwrap_or_default(),
             outstanding_qty: warrant_extend.outstanding_qty,
             conversion_ratio: warrant_extend.conversion_ratio.parse().unwrap_or_default(),
             category: warrant_extend.category.parse().unwrap_or_default(),
             strike_price: warrant_extend.strike_price.parse().unwrap_or_default(),
             upper_strike_price: warrant_extend
                 .upper_strike_price
@@ -584,18 +591,19 @@
     /// Average price
     pub avg_price: Decimal,
 }
 
 impl TryFrom<quote::Line> for IntradayLine {
     type Error = Error;
 
-    fn try_from(value: quote::Line) -> Result<Self, Self::Error> {
+    fn try_from(value: quote::Line) -> Result<Self> {
         Ok(Self {
             price: value.price.parse().unwrap_or_default(),
-            timestamp: OffsetDateTime::from_unix_timestamp(value.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(value.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
             volume: value.volume,
             turnover: value.turnover.parse().unwrap_or_default(),
             avg_price: value.avg_price.parse().unwrap_or_default(),
         })
     }
 }
 
@@ -617,23 +625,24 @@
     /// Timestamp
     pub timestamp: OffsetDateTime,
 }
 
 impl TryFrom<quote::Candlestick> for Candlestick {
     type Error = Error;
 
-    fn try_from(value: quote::Candlestick) -> Result<Self, Self::Error> {
+    fn try_from(value: quote::Candlestick) -> Result<Self> {
         Ok(Self {
             close: value.close.parse().unwrap_or_default(),
             open: value.open.parse().unwrap_or_default(),
             low: value.low.parse().unwrap_or_default(),
             high: value.high.parse().unwrap_or_default(),
             volume: value.volume,
             turnover: value.turnover.parse().unwrap_or_default(),
-            timestamp: OffsetDateTime::from_unix_timestamp(value.timestamp)?,
+            timestamp: OffsetDateTime::from_unix_timestamp(value.timestamp)
+                .map_err(|err| Error::parse_field_error("timestamp", err))?,
         })
     }
 }
 
 /// Strike price info
 #[derive(Debug, Clone)]
 pub struct StrikePriceInfo {
@@ -646,15 +655,15 @@
     /// Is standard
     pub standard: bool,
 }
 
 impl TryFrom<quote::StrikePriceInfo> for StrikePriceInfo {
     type Error = Error;
 
-    fn try_from(value: quote::StrikePriceInfo) -> Result<Self, Self::Error> {
+    fn try_from(value: quote::StrikePriceInfo) -> Result<Self> {
         Ok(Self {
             price: value.price.parse().unwrap_or_default(),
             call_symbol: value.call_symbol,
             put_symbol: value.put_symbol,
             standard: value.standard,
         })
     }
@@ -744,26 +753,25 @@
     /// Trading session
     pub trade_session: TradeSession,
 }
 
 impl TryFrom<quote::TradePeriod> for TradingSessionInfo {
     type Error = Error;
 
-    fn try_from(value: quote::TradePeriod) -> Result<Self, Self::Error> {
-        fn parse_time(value: i32) -> Result<Time> {
-            Ok(Time::from_hms(
-                ((value / 100) % 100) as u8,
-                (value % 100) as u8,
-                0,
-            )?)
+    fn try_from(value: quote::TradePeriod) -> Result<Self> {
+        #[inline]
+        fn parse_time(value: i32) -> ::std::result::Result<Time, time::error::ComponentRange> {
+            Time::from_hms(((value / 100) % 100) as u8, (value % 100) as u8, 0)
         }
 
         Ok(Self {
-            begin_time: parse_time(value.beg_time)?,
-            end_time: parse_time(value.end_time)?,
+            begin_time: parse_time(value.beg_time)
+                .map_err(|err| Error::parse_field_error("beg_time", err))?,
+            end_time: parse_time(value.end_time)
+                .map_err(|err| Error::parse_field_error("end_time", err))?,
             trade_session: TradeSession::from_i32(value.trade_session).unwrap_or_default(),
         })
     }
 }
 
 /// Market trading session
 #[derive(Debug, Clone)]
@@ -773,15 +781,15 @@
     /// Trading session
     pub trade_session: Vec<TradingSessionInfo>,
 }
 
 impl TryFrom<quote::MarketTradePeriod> for MarketTradingSession {
     type Error = Error;
 
-    fn try_from(value: quote::MarketTradePeriod) -> Result<Self, Self::Error> {
+    fn try_from(value: quote::MarketTradePeriod) -> Result<Self> {
         Ok(Self {
             market: value.market.parse().unwrap_or_default(),
             trade_session: value
                 .trade_session
                 .into_iter()
                 .map(TryInto::try_into)
                 .collect::<Result<Vec<_>>>()?,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/context.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/context.rs`

 * *Files 8% similar despite different names*

```diff
@@ -1,24 +1,23 @@
 use std::sync::Arc;
 
-use anyhow::Result;
 use longbridge_httpcli::{HttpClient, Method};
 use longbridge_wscli::WsClientError;
 use serde::{Deserialize, Serialize};
 use tokio::sync::{mpsc, oneshot};
 
 use crate::{
     trade::{
         core::{Command, Core},
         AccountBalance, CashFlow, Execution, FundPositionsResponse, GetCashFlowOptions,
         GetFundPositionsOptions, GetHistoryExecutionsOptions, GetHistoryOrdersOptions,
         GetStockPositionsOptions, GetTodayExecutionsOptions, GetTodayOrdersOptions, Order,
         PushEvent, ReplaceOrderOptions, StockPositionsResponse, SubmitOrderOptions, TopicType,
     },
-    Config,
+    Config, Result,
 };
 
 /// Response for withdraw order request
 #[derive(Debug, Deserialize)]
 pub struct SubmitOrderResponse {
     /// Order id
     pub order_id: String,
@@ -104,15 +103,15 @@
     ///
     /// let opts = GetHistoryExecutionsOptions::new()
     ///     .symbol("700.HK")
     ///     .start_at(datetime!(2022-05-09 0:00 UTC))
     ///     .end_at(datetime!(2022-05-12 0:00 UTC));
     /// let resp = ctx.history_executions(opts).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn history_executions(
         &self,
         options: impl Into<Option<GetHistoryExecutionsOptions>>,
     ) -> Result<Vec<Execution>> {
         #[derive(Deserialize)]
@@ -147,15 +146,15 @@
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = TradeContext::try_new(config).await?;
     ///
     /// let opts = GetTodayExecutionsOptions::new().symbol("700.HK");
     /// let resp = ctx.today_executions(opts).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn today_executions(
         &self,
         options: impl Into<Option<GetTodayExecutionsOptions>>,
     ) -> Result<Vec<Execution>> {
         #[derive(Deserialize)]
@@ -197,15 +196,15 @@
     ///     .status([OrderStatus::Filled, OrderStatus::New])
     ///     .side(OrderSide::Buy)
     ///     .market(Market::HK)
     ///     .start_at(datetime!(2022-05-09 0:00 UTC))
     ///     .end_at(datetime!(2022-05-12 0:00 UTC));
     /// let resp = ctx.history_orders(opts).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn history_orders(
         &self,
         options: impl Into<Option<GetHistoryOrdersOptions>>,
     ) -> Result<Vec<Order>> {
         #[derive(Deserialize)]
@@ -244,15 +243,15 @@
     /// let opts = GetTodayOrdersOptions::new()
     ///     .symbol("700.HK")
     ///     .status([OrderStatus::Filled, OrderStatus::New])
     ///     .side(OrderSide::Buy)
     ///     .market(Market::HK);
     /// let resp = ctx.today_orders(opts).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn today_orders(
         &self,
         options: impl Into<Option<GetTodayOrdersOptions>>,
     ) -> Result<Vec<Order>> {
         #[derive(Deserialize)]
@@ -289,15 +288,15 @@
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = TradeContext::try_new(config).await?;
     ///
     /// let opts =
     ///     ReplaceOrderOptions::new("709043056541253632", decimal!(100i32)).price(decimal!(300i32));
     /// let resp = ctx.replace_order(opts).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn replace_order(&self, options: ReplaceOrderOptions) -> Result<()> {
         Ok(self
             .http_cli
             .request(Method::PUT, "/v1/trade/order")
             .body(options)
@@ -330,15 +329,15 @@
     ///     OrderSide::Buy,
     ///     decimal!(200i32),
     ///     TimeInForceType::Day,
     /// )
     /// .submitted_price(decimal!(50i32));
     /// let resp = ctx.submit_order(opts).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn submit_order(&self, options: SubmitOrderOptions) -> Result<SubmitOrderResponse> {
         Ok(self
             .http_cli
             .request(Method::POST, "/v1/trade/order")
             .body(options)
@@ -359,15 +358,15 @@
     /// use longbridge::{trade::TradeContext, Config};
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = TradeContext::try_new(config).await?;
     ///
     /// ctx.withdraw_order("709043056541253632").await?;
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn withdraw_order(&self, order_id: impl Into<String>) -> Result<()> {
         #[derive(Debug, Serialize)]
         struct Request {
             order_id: String,
         }
@@ -395,15 +394,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = TradeContext::try_new(config).await?;
     ///
     /// let resp = ctx.account_balance().await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn account_balance(&self) -> Result<Vec<AccountBalance>> {
         #[derive(Debug, Deserialize)]
         struct Response {
             list: Vec<AccountBalance>,
         }
@@ -435,15 +434,15 @@
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = TradeContext::try_new(config).await?;
     ///
     /// let opts = GetCashFlowOptions::new(datetime!(2022-05-09 0:00 UTC), datetime!(2022-05-12 0:00 UTC));
     /// let resp = ctx.cash_flow(opts).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn cash_flow(&self, options: GetCashFlowOptions) -> Result<Vec<CashFlow>> {
         #[derive(Debug, Deserialize)]
         struct Response {
             list: Vec<CashFlow>,
         }
@@ -471,15 +470,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = TradeContext::try_new(config).await?;
     ///
     /// let resp = ctx.fund_positions(None).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn fund_positions(
         &self,
         opts: impl Into<Option<GetFundPositionsOptions>>,
     ) -> Result<FundPositionsResponse> {
         Ok(self
@@ -504,15 +503,15 @@
     ///
     /// # tokio::runtime::Runtime::new().unwrap().block_on(async {
     /// let config = Arc::new(Config::from_env()?);
     /// let (ctx, _) = TradeContext::try_new(config).await?;
     ///
     /// let resp = ctx.stock_positions(None).await?;
     /// println!("{:?}", resp);
-    /// # Ok::<_, anyhow::Error>(())
+    /// # Ok::<_, Box<dyn std::error::Error>>(())
     /// # });
     /// ```
     pub async fn stock_positions(
         &self,
         opts: impl Into<Option<GetStockPositionsOptions>>,
     ) -> Result<StockPositionsResponse> {
         Ok(self
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/core.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/core.rs`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,16 @@
 use std::{collections::HashSet, sync::Arc, time::Duration};
 
-use anyhow::Result;
 use longbridge_proto::trade::{Sub, SubResponse, Unsub, UnsubResponse};
 use longbridge_wscli::{CodecType, Platform, ProtocolVersion, WsClient, WsEvent, WsSession};
 use tokio::sync::{mpsc, oneshot};
 
 use crate::{
     trade::{cmd_code, PushEvent, TopicType},
-    Config,
+    Config, Result,
 };
 
 const RECONNECT_DELAY: Duration = Duration::from_secs(2);
 
 pub(crate) enum Command {
     Subscribe {
         topics: Vec<TopicType>,
@@ -165,17 +164,18 @@
             WsEvent::Error(err) => Err(err.into()),
             WsEvent::Push { command_code, body } => self.handle_push(command_code, body).await,
         }
     }
 
     async fn handle_push(&mut self, command_code: u8, body: Vec<u8>) -> Result<()> {
         match PushEvent::parse(command_code, &body) {
-            Ok(event) => {
+            Ok(Some(event)) => {
                 let _ = self.push_tx.send(event);
             }
+            Ok(None) => {}
             Err(err) => {
                 tracing::error!(error = %err, "failed to parse push message");
             }
         }
         Ok(())
     }
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/mod.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/mod.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/push_types.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/push_types.rs`

 * *Files 12% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 use std::str::FromStr;
 
-use anyhow::{Context, Result};
 use longbridge_proto::trade::Notification;
 use prost::Message;
 use rust_decimal::Decimal;
 use serde::Deserialize;
 use strum_macros::{Display, EnumString};
 use time::OffsetDateTime;
 
-use crate::trade::{
-    cmd_code, serde_utils, OrderSide, OrderStatus, OrderTag, OrderType, TriggerStatus,
+use crate::{
+    trade::{cmd_code, serde_utils, OrderSide, OrderStatus, OrderTag, OrderType, TriggerStatus},
+    Error, Result,
 };
 
 /// Topic type
 #[derive(Debug, Copy, Clone, Hash, Eq, PartialEq, EnumString, Display)]
 pub enum TopicType {
     /// Private notification for trade
     #[strum(serialize = "private")]
@@ -83,21 +83,22 @@
 pub enum PushEvent {
     /// Order changed
     #[serde(rename = "order_changed_lb")]
     OrderChanged(PushOrderChanged),
 }
 
 impl PushEvent {
-    pub(crate) fn parse(command_code: u8, data: &[u8]) -> Result<PushEvent> {
+    pub(crate) fn parse(command_code: u8, data: &[u8]) -> Result<Option<PushEvent>> {
         if command_code == cmd_code::PUSH_NOTIFICATION {
-            let notification = Notification::decode(data).context("decode push notification")?;
-            match TopicType::from_str(&notification.topic) {
-                Ok(TopicType::Private) => {
-                    Ok(serde_json::from_slice::<PushEvent>(&notification.data)?)
-                }
-                Err(_) => anyhow::bail!("unknown topic: {}", notification.topic),
+            let notification = Notification::decode(data)?;
+            if let Ok(TopicType::Private) = TopicType::from_str(&notification.topic) {
+                Ok(Some(serde_json::from_slice::<PushEvent>(
+                    &notification.data,
+                )?))
+            } else {
+                Ok(None)
             }
         } else {
-            anyhow::bail!("unknown command: {}", command_code)
+            Err(Error::UnknownCommand(command_code))
         }
     }
 }
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_cash_flow.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_cash_flow.rs`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 use serde::Serialize;
 use time::OffsetDateTime;
 
 use crate::trade::{serde_utils, BalanceType};
 
 /// Options for submit order request
-#[derive(Debug, Serialize)]
+#[derive(Debug, Serialize, Clone)]
 pub struct GetCashFlowOptions {
     #[serde(rename = "start_time", with = "serde_utils::timestamp")]
     start_at: OffsetDateTime,
     #[serde(rename = "end_time", with = "serde_utils::timestamp")]
     end_at: OffsetDateTime,
     business_type: Option<BalanceType>,
     symbol: Option<String>,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_fund_positions.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_fund_positions.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_history_executions.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_history_executions.rs`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 use serde::Serialize;
 use time::OffsetDateTime;
 
 use crate::trade::serde_utils;
 
 /// Options for get histroy executions request
-#[derive(Debug, Serialize, Default)]
+#[derive(Debug, Serialize, Default, Clone)]
 pub struct GetHistoryExecutionsOptions {
     #[serde(skip_serializing_if = "Option::is_none")]
     symbol: Option<String>,
     #[serde(
         skip_serializing_if = "Option::is_none",
         with = "serde_utils::timestamp_opt"
     )]
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_history_orders.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_history_orders.rs`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 
 use crate::{
     trade::{serde_utils, OrderSide, OrderStatus},
     Market,
 };
 
 /// Options for get history orders request
-#[derive(Debug, Default, Serialize)]
+#[derive(Debug, Default, Serialize, Clone)]
 pub struct GetHistoryOrdersOptions {
     #[serde(skip_serializing_if = "Option::is_none")]
     symbol: Option<String>,
     #[serde(skip_serializing_if = "<[_]>::is_empty")]
     status: Vec<OrderStatus>,
     #[serde(skip_serializing_if = "Option::is_none")]
     side: Option<OrderSide>,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_stock_positions.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_stock_positions.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_today_executions.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_today_executions.rs`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 use serde::Serialize;
 
 /// Options for get today executions request
-#[derive(Debug, Default, Serialize)]
+#[derive(Debug, Default, Serialize, Clone)]
 pub struct GetTodayExecutionsOptions {
     #[serde(skip_serializing_if = "Option::is_none")]
     symbol: Option<String>,
     #[serde(skip_serializing_if = "Option::is_none")]
     order_id: Option<String>,
 }
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/get_today_orders.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/get_today_orders.rs`

 * *Files 7% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 use crate::{
     trade::{OrderSide, OrderStatus},
     Market,
 };
 
 /// Options for get today orders request
-#[derive(Debug, Default, Serialize)]
+#[derive(Debug, Default, Serialize, Clone)]
 pub struct GetTodayOrdersOptions {
     #[serde(skip_serializing_if = "Option::is_none")]
     symbol: Option<String>,
     #[serde(skip_serializing_if = "<[_]>::is_empty")]
     status: Vec<OrderStatus>,
     #[serde(skip_serializing_if = "Option::is_none")]
     side: Option<OrderSide>,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/mod.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/mod.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/replace_order.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/replace_order.rs`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 use rust_decimal::Decimal;
 use serde::Serialize;
 
 /// Options for replace order request
-#[derive(Debug, Serialize)]
+#[derive(Debug, Serialize, Clone)]
 pub struct ReplaceOrderOptions {
     order_id: String,
     quantity: Decimal,
     #[serde(skip_serializing_if = "Option::is_none")]
     price: Option<Decimal>,
     #[serde(skip_serializing_if = "Option::is_none")]
     trigger_price: Option<Decimal>,
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/requests/submit_order.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/requests/submit_order.rs`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 use rust_decimal::Decimal;
 use serde::Serialize;
 use time::Date;
 
 use crate::trade::{serde_utils, OrderSide, OrderType, OutsideRTH, TimeInForceType};
 
 /// Options for submit order request
-#[derive(Debug, Serialize)]
+#[derive(Debug, Serialize, Clone)]
 pub struct SubmitOrderOptions {
     symbol: String,
     order_type: OrderType,
     side: OrderSide,
     submitted_quantity: Decimal,
     time_in_force: TimeInForceType,
     #[serde(skip_serializing_if = "Option::is_none")]
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/serde_utils.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/serde_utils.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge/src/trade/types.rs` & `longbridge-0.2.9/local_dependencies/longbridge/src/trade/types.rs`

 * *Files 0% similar despite different names*

```diff
@@ -460,15 +460,16 @@
 #[derive(Debug, Clone, Deserialize)]
 pub struct StockPosition {
     /// Stock code
     pub symbol: String,
     /// Stock name
     pub symbol_name: String,
     /// The number of holdings
-    pub quality: Decimal,
+    #[serde(rename = "quality")]
+    pub quantity: Decimal,
     /// Available quantity
     pub available_quality: Decimal,
     /// Currency
     pub currency: String,
     /// Cost Price(According to the client's choice of average purchase or
     /// diluted cost)
     pub cost_price: Decimal,
@@ -574,31 +575,31 @@
         assert_eq!(channel.account_channel, "lb");
         assert_eq!(channel.positions.len(), 2);
 
         let position = &channel.positions[0];
         assert_eq!(position.symbol, "700.HK");
         assert_eq!(position.symbol_name, "腾讯控股");
         assert_eq!(position.currency, "HK");
-        assert_eq!(position.quality, decimal!(650i32));
+        assert_eq!(position.quantity, decimal!(650i32));
         assert_eq!(position.available_quality, decimal!(-450i32));
         assert_eq!(position.cost_price, decimal!(457.53f32));
 
         let position = &channel.positions[0];
         assert_eq!(position.symbol, "700.HK");
         assert_eq!(position.symbol_name, "腾讯控股");
         assert_eq!(position.currency, "HK");
-        assert_eq!(position.quality, decimal!(650i32));
+        assert_eq!(position.quantity, decimal!(650i32));
         assert_eq!(position.available_quality, decimal!(-450i32));
         assert_eq!(position.cost_price, decimal!(457.53f32));
 
         let position = &channel.positions[1];
         assert_eq!(position.symbol, "9991.HK");
         assert_eq!(position.symbol_name, "宝尊电商-SW");
         assert_eq!(position.currency, "HK");
-        assert_eq!(position.quality, decimal!(200i32));
+        assert_eq!(position.quantity, decimal!(200i32));
         assert_eq!(position.available_quality, decimal!(0i32));
         assert_eq!(position.cost_price, decimal!(32.25f32));
     }
 
     #[test]
     fn cash_flow() {
         let data = r#"
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-wscli/Cargo.toml` & `longbridge-0.2.9/local_dependencies/longbridge-wscli/Cargo.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 [package]
 name = "longbridge-wscli"
-version = "0.2.8"
+version = "0.2.9"
 edition = "2021"
 description = "Longbridge Websocket SDK for Rust"
 license = "MIT OR Apache-2.0"
 
 [dependencies]
-longbridge-proto = { path = "../longbridge-proto", version = "0.2.8" }
+longbridge-proto = { path = "../longbridge-proto", version = "0.2.9" }
 
 tokio = { version = "1.18.2", features = [
     "time",
     "rt",
     "macros",
     "sync",
     "net",
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-wscli/src/client.rs` & `longbridge-0.2.9/local_dependencies/longbridge-wscli/src/client.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-wscli/src/codec.rs` & `longbridge-0.2.9/local_dependencies/longbridge-wscli/src/codec.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-wscli/src/error.rs` & `longbridge-0.2.9/local_dependencies/longbridge-wscli/src/error.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/Cargo.toml` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/Cargo.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [package]
 edition = "2021"
 name = "longbridge-httpcli"
-version = "0.2.8"
+version = "0.2.9"
 description = "Longbridge HTTP SDK for Rust"
 license = "MIT OR Apache-2.0"
 
 [dependencies]
 futures-util = "0.3.21"
 hmac = "0.12.1"
 parking_lot = "0.12.0"
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/client.rs` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/client.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/config.rs` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/config.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/error.rs` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/error.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/qs.rs` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/qs.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/request.rs` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/request.rs`

 * *Files 1% similar despite different names*

```diff
@@ -139,14 +139,15 @@
         tracing::debug!(method = %request.method(), url = %request.url(), "http request");
 
         // send request
         let text = tokio::time::timeout(REQUEST_TIMEOUT, async move {
             http_cli
                 .execute(request)
                 .await?
+                .error_for_status()?
                 .text()
                 .await
                 .map_err(HttpClientError::from)
         })
         .await
         .map_err(|_| HttpClientError::RequestTimeout)??;
```

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/signature.rs` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/signature.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-httpcli/src/timestamp.rs` & `longbridge-0.2.9/local_dependencies/longbridge-httpcli/src/timestamp.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/control/control.proto` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/control/control.proto`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.cc` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.cc`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.h` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/control.pb.h`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.cc` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.cc`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.h` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/control/error.pb.h`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.cc` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.cc`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.h` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/quote/api.pb.h`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.cc` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.cc`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.h` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/cpp/trade/subscribe.pb.h`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/control.pb.go` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/control.pb.go`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/error.pb.go` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/control/error.pb.go`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/quote/api.pb.go` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/quote/api.pb.go`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/trade/subscribe.pb.go` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/go/trade/subscribe.pb.go`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/control_pb2.py` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/control_pb2.py`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/error_pb2.py` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/control/error_pb2.py`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/quote/api_pb2.py` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/quote/api_pb2.py`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/trade/subscribe_pb2.py` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/gen/python/trade/subscribe_pb2.py`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/go.sum` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/go.sum`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/quote/api.proto` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/quote/api.proto`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/openapi-protobufs/trade/subscribe.proto` & `longbridge-0.2.9/local_dependencies/longbridge-proto/openapi-protobufs/trade/subscribe.proto`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/src/longbridgeapp.control.v1.rs` & `longbridge-0.2.9/local_dependencies/longbridge-proto/src/longbridgeapp.control.v1.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/src/longbridgeapp.quote.v1.rs` & `longbridge-0.2.9/local_dependencies/longbridge-proto/src/longbridgeapp.quote.v1.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/local_dependencies/longbridge-proto/src/longbridgeapp.trade.v1.rs` & `longbridge-0.2.9/local_dependencies/longbridge-proto/src/longbridgeapp.trade.v1.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/Cargo.toml` & `longbridge-0.2.9/Cargo.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,29 +1,29 @@
 [package]
 edition = "2021"
 name = "longbridge-python"
-version = "0.2.8"
+version = "0.2.9"
 description = "Longbridge OpenAPI SDK for Python"
 homepage = "https://open.longbridgeapp.com/en/"
 readme = "README.md"
 repository = "https://github.com/longbridgeapp/openapi-sdk"
 license = "MIT OR Apache-2.0"
 keywords = ["longbridge", "openapi", "sdk"]
 categories = ["api-bindings"]
 
 [lib]
 name = "longbridge"
 crate-type = ["cdylib"]
 
 [dependencies]
-longbridge = { path = "local_dependencies/longbridge", version = "0.2.8", features = ["blocking"] }
-longbridge-python-macros = { path = "local_dependencies/longbridge-python-macros", version = "0.2.8" }
+longbridge = { path = "local_dependencies/longbridge", version = "0.2.9", features = ["blocking"] }
+longbridge-python-macros = { path = "local_dependencies/longbridge-python-macros", version = "0.2.9" }
 
 once_cell = "1.11.0"
-pyo3 = { version = "0.16.4", features = ["anyhow", "extension-module"] }
+pyo3 = { version = "0.16.4", features = ["extension-module"] }
 rust_decimal = "1.23.1"
 time = "0.3.9"
 
 [build-dependencies]
 pyo3-build-config = "0.16.4"
 
 [package.metadata.maturin]
```

### Comparing `longbridge-0.2.8/README.md` & `longbridge-0.2.9/README.md`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/docs/index.md` & `longbridge-0.2.9/docs/index.md`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/mkdocs.yml` & `longbridge-0.2.9/mkdocs.yml`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/pyproject.toml` & `longbridge-0.2.9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/pysrc/longbridge/openapi.pyi` & `longbridge-0.2.9/pysrc/longbridge/openapi.pyi`

 * *Files 0% similar despite different names*

```diff
@@ -870,17 +870,17 @@
 
 
 class TradeDirection:
     """
     Trade direction
     """
 
-    class Nature(TradeDirection):
+    class Neutral(TradeDirection):
         """
-        Nature
+        Neutral
         """
 
     class Down(TradeDirection):
         """
         Down
         """
 
@@ -2581,15 +2581,15 @@
     """
 
     symbol_name: str
     """
     Stock name
     """
 
-    quality: Decimal
+    quantity: Decimal
     """
     The number of holdings
     """
 
     available_quality: Decimal
     """
     Available quantity
```

### Comparing `longbridge-0.2.8/src/config.rs` & `longbridge-0.2.9/src/config.rs`

 * *Files 11% similar despite different names*

```diff
@@ -1,9 +1,11 @@
 use pyo3::{prelude::*, types::PyType};
 
+use crate::error::ErrorNewType;
+
 #[pyclass(name = "Config")]
 pub(crate) struct Config(pub(crate) longbridge::Config);
 
 #[pymethods]
 impl Config {
     #[new]
     #[args(
@@ -25,10 +27,10 @@
                 .quote_ws_url(quote_ws_url)
                 .trade_ws_url(trade_ws_url),
         )
     }
 
     #[classmethod]
     fn from_env(_cls: &PyType) -> PyResult<Self> {
-        Ok(Self(longbridge::Config::from_env()?))
+        Ok(Self(longbridge::Config::from_env().map_err(ErrorNewType)?))
     }
 }
```

### Comparing `longbridge-0.2.8/src/decimal.rs` & `longbridge-0.2.9/src/decimal.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/src/quote/context.rs` & `longbridge-0.2.9/src/quote/context.rs`

 * *Files 14% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 use std::sync::Arc;
 
 use longbridge::blocking::QuoteContextSync;
 use pyo3::prelude::*;
 
 use crate::{
     config::Config,
+    error::ErrorNewType,
     quote::{
         push::handle_push_event,
         types::{
             AdjustType, Candlestick, IntradayLine, IssuerInfo, MarketTradingDays,
             MarketTradingSession, OptionQuote, ParticipantInfo, Period, RealtimeQuote,
             SecurityBrokers, SecurityDepth, SecurityQuote, SecurityStaticInfo, StrikePriceInfo,
             SubType, SubTypes, Trade, WarrantQuote,
@@ -25,200 +26,225 @@
 impl QuoteContext {
     #[new]
     fn new(config: &Config, handler: Option<PyObject>) -> PyResult<Self> {
         let ctx = QuoteContextSync::try_new(Arc::new(config.0.clone()), move |event| {
             if let Some(handler) = &handler {
                 handle_push_event(handler, event);
             }
-        })?;
+        })
+        .map_err(ErrorNewType)?;
         Ok(Self(ctx))
     }
 
     /// Subscribe
     #[args(is_first_push = false)]
     fn subscribe(
         &self,
         symbols: Vec<String>,
         sub_types: Vec<SubType>,
         is_first_push: bool,
     ) -> PyResult<()> {
         self.0
-            .subscribe(symbols, SubTypes(sub_types), is_first_push)?;
+            .subscribe(symbols, SubTypes(sub_types), is_first_push)
+            .map_err(ErrorNewType)?;
         Ok(())
     }
 
     /// Unsubscribe
     fn unsubscribe(&self, symbols: Vec<String>, sub_types: Vec<SubType>) -> PyResult<()> {
-        self.0.unsubscribe(symbols, SubTypes(sub_types))?;
+        self.0
+            .unsubscribe(symbols, SubTypes(sub_types))
+            .map_err(ErrorNewType)?;
         Ok(())
     }
 
     /// Get basic information of securities
     fn static_info(&self, symbols: Vec<String>) -> PyResult<Vec<SecurityStaticInfo>> {
         self.0
-            .static_info(symbols)?
+            .static_info(symbols)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get quote of securities
     fn quote(&self, symbols: Vec<String>) -> PyResult<Vec<SecurityQuote>> {
         self.0
-            .quote(symbols)?
+            .quote(symbols)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get quote of option securities
     fn option_quote(&self, symbols: Vec<String>) -> PyResult<Vec<OptionQuote>> {
         self.0
-            .option_quote(symbols)?
+            .option_quote(symbols)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get quote of warrant securities
     fn warrant_quote(&self, symbols: Vec<String>) -> PyResult<Vec<WarrantQuote>> {
         self.0
-            .warrant_quote(symbols)?
+            .warrant_quote(symbols)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get security depth
     fn depth(&self, symbol: String) -> PyResult<SecurityDepth> {
-        self.0.depth(symbol)?.try_into()
+        self.0.depth(symbol).map_err(ErrorNewType)?.try_into()
     }
 
     /// Get security brokers
     fn brokers(&self, symbol: String) -> PyResult<SecurityBrokers> {
-        self.0.brokers(symbol)?.try_into()
+        self.0.brokers(symbol).map_err(ErrorNewType)?.try_into()
     }
 
     /// Get participants
-    pub fn participants(&self) -> PyResult<Vec<ParticipantInfo>> {
+    fn participants(&self) -> PyResult<Vec<ParticipantInfo>> {
         self.0
-            .participants()?
+            .participants()
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get security trades
-    pub fn trades(&self, symbol: String, count: usize) -> PyResult<Vec<Trade>> {
+    fn trades(&self, symbol: String, count: usize) -> PyResult<Vec<Trade>> {
         self.0
-            .trades(symbol, count)?
+            .trades(symbol, count)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get security intraday
-    pub fn intraday(&self, symbol: String) -> PyResult<Vec<IntradayLine>> {
+    fn intraday(&self, symbol: String) -> PyResult<Vec<IntradayLine>> {
         self.0
-            .intraday(symbol)?
+            .intraday(symbol)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get security candlesticks
-    pub fn candlesticks(
+    fn candlesticks(
         &self,
         symbol: String,
         period: Period,
         count: usize,
         adjust_type: AdjustType,
     ) -> PyResult<Vec<Candlestick>> {
         self.0
-            .candlesticks(symbol, period.into(), count, adjust_type.into())?
+            .candlesticks(symbol, period.into(), count, adjust_type.into())
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get option chain expiry date list
-    pub fn option_chain_expiry_date_list(&self, symbol: String) -> PyResult<Vec<PyDateWrapper>> {
+    fn option_chain_expiry_date_list(&self, symbol: String) -> PyResult<Vec<PyDateWrapper>> {
         Ok(self
             .0
-            .option_chain_expiry_date_list(symbol)?
+            .option_chain_expiry_date_list(symbol)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(Into::into)
             .collect())
     }
 
     /// Get option chain info by date
-    pub fn option_chain_info_by_date(
+    fn option_chain_info_by_date(
         &self,
         symbol: String,
         expiry_date: PyDateWrapper,
     ) -> PyResult<Vec<StrikePriceInfo>> {
         self.0
-            .option_chain_info_by_date(symbol, expiry_date.0)?
+            .option_chain_info_by_date(symbol, expiry_date.0)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get warrant issuers
-    pub fn warrant_issuers(&self) -> PyResult<Vec<IssuerInfo>> {
+    fn warrant_issuers(&self) -> PyResult<Vec<IssuerInfo>> {
         self.0
-            .warrant_issuers()?
+            .warrant_issuers()
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get trading session of the day
-    pub fn trading_session(&self) -> PyResult<Vec<MarketTradingSession>> {
+    fn trading_session(&self) -> PyResult<Vec<MarketTradingSession>> {
         self.0
-            .trading_session()?
+            .trading_session()
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get trading session of the day
-    pub fn trading_days(
+    fn trading_days(
         &self,
         market: Market,
         begin: PyDateWrapper,
         end: PyDateWrapper,
     ) -> PyResult<MarketTradingDays> {
         self.0
-            .trading_days(market.into(), begin.0, end.0)?
+            .trading_days(market.into(), begin.0, end.0)
+            .map_err(ErrorNewType)?
             .try_into()
     }
 
     /// Get real-time quote
     fn realtime_quote(&self, symbols: Vec<String>) -> PyResult<Vec<RealtimeQuote>> {
         self.0
-            .realtime_quote(symbols)?
+            .realtime_quote(symbols)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get real-time depth
     fn realtime_depth(&self, symbol: String) -> PyResult<SecurityDepth> {
-        self.0.realtime_depth(symbol)?.try_into()
+        self.0
+            .realtime_depth(symbol)
+            .map_err(ErrorNewType)?
+            .try_into()
     }
 
     /// Get real-time brokers
     fn realtime_brokers(&self, symbol: String) -> PyResult<SecurityBrokers> {
-        self.0.realtime_brokers(symbol)?.try_into()
+        self.0
+            .realtime_brokers(symbol)
+            .map_err(ErrorNewType)?
+            .try_into()
     }
 
     /// Get real-time trades
     #[args(count = 500)]
     fn realtime_trades(&self, symbol: String, count: usize) -> PyResult<Vec<Trade>> {
         self.0
-            .realtime_trades(symbol, count)?
+            .realtime_trades(symbol, count)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 }
```

### Comparing `longbridge-0.2.8/src/quote/mod.rs` & `longbridge-0.2.9/src/quote/mod.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/src/quote/push.rs` & `longbridge-0.2.9/src/quote/push.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/src/quote/types.rs` & `longbridge-0.2.9/src/quote/types.rs`

 * *Files 12% similar despite different names*

```diff
@@ -7,25 +7,25 @@
     time::{PyDateWrapper, PyOffsetDateTimeWrapper, PyTimeWrapper},
     types::Market,
 };
 
 /// Derivative type
 #[pyclass]
 #[derive(PyEnum, Debug, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::quote::DerivativeType")]
+#[py(remote = "longbridge::quote::DerivativeType")]
 pub(crate) enum DerivativeType {
     /// US stock options
     Option,
     /// HK warrants
     Warrant,
 }
 
 #[pyclass]
 #[derive(PyEnum, Debug, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::quote::TradeStatus")]
+#[py(remote = "longbridge::quote::TradeStatus")]
 pub(crate) enum TradeStatus {
     /// Normal
     Normal,
     /// Suspension
     Halted,
     /// Delisted
     Delisted,
@@ -40,31 +40,31 @@
     /// Split Stock Halts
     SplitStockHalts,
     /// Expired
     Expired,
     /// Warrant To BeListed
     WarrantPrepareList,
     /// Warrant To BeListed
-    #[py(from = "SuspendTrade")]
+    #[py(remote = "SuspendTrade")]
     Suspend,
 }
 
 /// Trade session
 #[pyclass]
 #[derive(PyEnum, Debug, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::quote::TradeSession")]
+#[py(remote = "longbridge::quote::TradeSession")]
 pub(crate) enum TradeSession {
     /// Trading
-    #[py(from = "NormalTrade")]
+    #[py(remote = "NormalTrade")]
     Normal,
     /// Pre-Trading
-    #[py(from = "PreTrade")]
+    #[py(remote = "PreTrade")]
     Pre,
     /// Post-Trading
-    #[py(from = "PostTrade")]
+    #[py(remote = "PostTrade")]
     Post,
 }
 
 /// Quote type of subscription
 #[pyclass]
 #[derive(Debug, Copy, Clone, Hash, Eq, PartialEq)]
 pub(crate) enum SubType {
@@ -97,54 +97,54 @@
             })
     }
 }
 
 /// Trade direction
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::quote::TradeDirection")]
+#[py(remote = "longbridge::quote::TradeDirection")]
 pub(crate) enum TradeDirection {
-    /// Nature
-    Nature,
+    /// Neutral
+    Neutral,
     /// Down
     Down,
     /// Up
     Up,
 }
 
 /// Option type
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::quote::OptionType")]
+#[py(remote = "longbridge::quote::OptionType")]
 pub(crate) enum OptionType {
     /// Unknown
     Unknown,
     /// American
     American,
     /// Europe
     Europe,
 }
 
 /// Option direction
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::quote::OptionDirection")]
+#[py(remote = "longbridge::quote::OptionDirection")]
 pub(crate) enum OptionDirection {
     /// Unknown
     Unknown,
     /// Put
     Put,
     /// Call
     Call,
 }
 
 /// Warrant type
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::quote::WarrantType")]
+#[py(remote = "longbridge::quote::WarrantType")]
 pub(crate) enum WarrantType {
     /// Unknown
     Unknown,
     /// Call
     Call,
     /// Put
     Put,
@@ -155,77 +155,57 @@
     /// Inline
     Inline,
 }
 
 /// Candlestick period
 #[pyclass]
 #[allow(non_camel_case_types)]
-#[derive(Debug, Copy, Clone, Hash, Eq, PartialEq)]
+#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
+#[py(remote = "longbridge::quote::Period", from = false)]
 pub(crate) enum Period {
     /// One Minute
+    #[py(remote = "OneMinute")]
     Min_1,
     /// Five Minutes
+    #[py(remote = "FiveMinute")]
     Min_5,
     /// Fifteen Minutes
+    #[py(remote = "FifteenMinute")]
     Min_15,
     /// Thirty Minutes
+    #[py(remote = "ThirtyMinute")]
     Min_30,
     /// Sixty Minutes
+    #[py(remote = "SixtyMinute")]
     Min_60,
     /// One Days
     Day,
     /// One Week
     Week,
     /// One Month
     Month,
     /// One Year
     Year,
 }
 
-impl From<Period> for longbridge::quote::Period {
-    #[inline]
-    fn from(period: Period) -> Self {
-        match period {
-            Period::Min_1 => longbridge::quote::Period::OneMinute,
-            Period::Min_5 => longbridge::quote::Period::FiveMinute,
-            Period::Min_15 => longbridge::quote::Period::FifteenMinute,
-            Period::Min_30 => longbridge::quote::Period::ThirtyMinute,
-            Period::Min_60 => longbridge::quote::Period::SixtyMinute,
-            Period::Day => longbridge::quote::Period::Day,
-            Period::Week => longbridge::quote::Period::Week,
-            Period::Month => longbridge::quote::Period::Month,
-            Period::Year => longbridge::quote::Period::Year,
-        }
-    }
-}
-
 /// Candlestick adjustment type
 #[pyclass]
-#[derive(Debug, Copy, Clone, Hash, Eq, PartialEq)]
+#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
+#[py(remote = "longbridge::quote::AdjustType")]
 pub(crate) enum AdjustType {
     /// Actual
     NoAdjust,
     /// Adjust forward
     ForwardAdjust,
 }
 
-impl From<AdjustType> for longbridge::quote::AdjustType {
-    #[inline]
-    fn from(ty: AdjustType) -> Self {
-        match ty {
-            AdjustType::NoAdjust => longbridge::quote::AdjustType::NoAdjust,
-            AdjustType::ForwardAdjust => longbridge::quote::AdjustType::ForwardAdjust,
-        }
-    }
-}
-
 /// The basic information of securities
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::SecurityStaticInfo")]
+#[py(remote = "longbridge::quote::SecurityStaticInfo")]
 pub(crate) struct SecurityStaticInfo {
     /// Security code
     symbol: String,
     /// Security name (zh-CN)
     name_cn: String,
     /// Security name (en)
     name_en: String,
@@ -255,15 +235,15 @@
     #[py(array)]
     stock_derivatives: Vec<DerivativeType>,
 }
 
 /// Quote of US pre/post market
 #[pyclass]
 #[derive(Debug, PyObject, Copy, Clone)]
-#[py(from = "longbridge::quote::PrePostQuote")]
+#[py(remote = "longbridge::quote::PrePostQuote")]
 pub(crate) struct PrePostQuote {
     /// Latest price
     last_done: PyDecimal,
     /// Time of latest price
     timestamp: PyOffsetDateTimeWrapper,
     /// Volume
     volume: i64,
@@ -276,15 +256,15 @@
     /// Close of the last trade session
     prev_close: PyDecimal,
 }
 
 /// Quote of securitity
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::SecurityQuote")]
+#[py(remote = "longbridge::quote::SecurityQuote")]
 pub(crate) struct SecurityQuote {
     /// Security code
     symbol: String,
     /// Latest price
     last_done: PyDecimal,
     /// Yesterday's close
     prev_close: PyDecimal,
@@ -309,15 +289,15 @@
     #[py(opt)]
     post_market_quote: Option<PrePostQuote>,
 }
 
 /// Quote of option
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::OptionQuote")]
+#[py(remote = "longbridge::quote::OptionQuote")]
 pub(crate) struct OptionQuote {
     /// Security code
     symbol: String,
     /// Latest price
     last_done: PyDecimal,
     /// Yesterday's close
     prev_close: PyDecimal,
@@ -356,15 +336,15 @@
     /// Underlying security symbol of the option
     underlying_symbol: String,
 }
 
 /// Quote of warrant
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::WarrantQuote")]
+#[py(remote = "longbridge::quote::WarrantQuote")]
 pub(crate) struct WarrantQuote {
     /// Security code
     symbol: String,
     /// Latest price
     last_done: PyDecimal,
     /// Yesterday's close
     prev_close: PyDecimal,
@@ -407,82 +387,82 @@
     /// Underlying security symbol of the warrant
     underlying_symbol: String,
 }
 
 /// Depth
 #[pyclass]
 #[derive(Debug, PyObject, Copy, Clone)]
-#[py(from = "longbridge::quote::Depth")]
+#[py(remote = "longbridge::quote::Depth")]
 pub(crate) struct Depth {
     /// Position
     position: i32,
     /// Price
     price: PyDecimal,
     /// Volume
     volume: i64,
     /// Number of orders
     order_num: i64,
 }
 
 /// Security depth
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::SecurityDepth")]
+#[py(remote = "longbridge::quote::SecurityDepth")]
 pub(crate) struct SecurityDepth {
     /// Ask depth
     #[py(array)]
     asks: Vec<Depth>,
     /// Bid depth
     #[py(array)]
     bids: Vec<Depth>,
 }
 
 /// Brokers
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::quote::Brokers")]
+#[py(remote = "longbridge::quote::Brokers")]
 pub(crate) struct Brokers {
     /// Position
     position: i32,
     /// Broker IDs
     broker_ids: Vec<i32>,
 }
 
 /// Security brokers
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::SecurityBrokers")]
+#[py(remote = "longbridge::quote::SecurityBrokers")]
 pub(crate) struct SecurityBrokers {
     /// Ask brokers
     #[py(array)]
     ask_brokers: Vec<Brokers>,
     /// Bid brokers
     #[py(array)]
     bid_brokers: Vec<Brokers>,
 }
 
 /// Participant info
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::ParticipantInfo")]
+#[py(remote = "longbridge::quote::ParticipantInfo")]
 pub(crate) struct ParticipantInfo {
     /// Broker IDs
     broker_ids: Vec<i32>,
     /// Participant name (zh-CN)
     name_cn: String,
     /// Participant name (en)
     name_en: String,
     /// Participant name (zh-HK)
     name_hk: String,
 }
 
 /// Trade
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::quote::Trade")]
+#[py(remote = "longbridge::quote::Trade")]
 pub(crate) struct Trade {
     /// Price
     price: PyDecimal,
     /// Volume
     volume: i64,
     /// Time of trading
     timestamp: PyOffsetDateTimeWrapper,
@@ -493,15 +473,15 @@
     /// Trade session
     trade_session: TradeSession,
 }
 
 /// Intraday line
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::IntradayLine")]
+#[py(remote = "longbridge::quote::IntradayLine")]
 pub(crate) struct IntradayLine {
     /// Close price of the minute
     price: PyDecimal,
     /// Start time of the minute
     timestamp: PyOffsetDateTimeWrapper,
     /// Volume
     volume: i64,
@@ -510,15 +490,15 @@
     /// Average price
     avg_price: PyDecimal,
 }
 
 /// Candlestick
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::Candlestick")]
+#[py(remote = "longbridge::quote::Candlestick")]
 pub(crate) struct Candlestick {
     /// Close price
     close: PyDecimal,
     /// Open price
     open: PyDecimal,
     /// Low price
     low: PyDecimal,
@@ -531,70 +511,70 @@
     /// Timestamp
     timestamp: PyOffsetDateTimeWrapper,
 }
 
 /// Strike price info
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::StrikePriceInfo")]
+#[py(remote = "longbridge::quote::StrikePriceInfo")]
 pub(crate) struct StrikePriceInfo {
     /// Strike price
     price: PyDecimal,
     /// Security code of call option
     call_symbol: String,
     /// Security code of put option
     put_symbol: String,
     /// Is standard
     standard: bool,
 }
 
 /// Issuer info
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::IssuerInfo")]
+#[py(remote = "longbridge::quote::IssuerInfo")]
 pub(crate) struct IssuerInfo {
     /// Issuer ID
     issuer_id: i32,
     /// Issuer name (zh-CN)
     name_cn: String,
     /// Issuer name (en)
     name_en: String,
     /// Issuer name (zh-HK)
     name_hk: String,
 }
 
 /// The information of trading session
 #[pyclass]
 #[derive(Debug, PyObject, Copy, Clone)]
-#[py(from = "longbridge::quote::TradingSessionInfo")]
+#[py(remote = "longbridge::quote::TradingSessionInfo")]
 pub(crate) struct TradingSessionInfo {
     /// Being trading time
     begin_time: PyTimeWrapper,
     /// End trading time
     end_time: PyTimeWrapper,
     /// Trading session
     trade_session: TradeSession,
 }
 
 /// Market trading session
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::MarketTradingSession")]
+#[py(remote = "longbridge::quote::MarketTradingSession")]
 pub(crate) struct MarketTradingSession {
     /// Market
     market: Market,
     /// Trading session
     #[py(array)]
     trade_session: Vec<TradingSessionInfo>,
 }
 
 /// Real-time quote
 #[pyclass]
 #[derive(PyObject, Debug, Clone)]
-#[py(from = "longbridge::quote::RealtimeQuote")]
+#[py(remote = "longbridge::quote::RealtimeQuote")]
 pub struct RealtimeQuote {
     /// Security code
     symbol: String,
     /// Latest price
     last_done: PyDecimal,
     /// Open
     open: PyDecimal,
@@ -611,15 +591,15 @@
     /// Security trading status
     trade_status: TradeStatus,
 }
 
 /// Push real-time quote
 #[pyclass]
 #[derive(PyObject)]
-#[py(from = "longbridge::quote::PushQuote")]
+#[py(remote = "longbridge::quote::PushQuote")]
 #[derive(Debug, Clone)]
 pub struct PushQuote {
     /// Latest price
     last_done: PyDecimal,
     /// Open
     open: PyDecimal,
     /// High
@@ -637,51 +617,51 @@
     /// Trade session,
     trade_session: TradeSession,
 }
 
 /// Push real-time depth
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::PushDepth")]
+#[py(remote = "longbridge::quote::PushDepth")]
 pub(crate) struct PushDepth {
     /// Ask depth
     #[py(array)]
     asks: Vec<Depth>,
     /// Bid depth
     #[py(array)]
     bids: Vec<Depth>,
 }
 
 /// Push real-time brokers
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::PushBrokers")]
+#[py(remote = "longbridge::quote::PushBrokers")]
 pub(crate) struct PushBrokers {
     /// Ask brokers
     #[py(array)]
     ask_brokers: Vec<Brokers>,
     /// Bid brokers
     #[py(array)]
     bid_brokers: Vec<Brokers>,
 }
 
 /// Push real-time trades
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::PushTrades")]
+#[py(remote = "longbridge::quote::PushTrades")]
 pub struct PushTrades {
     /// Trades data
     #[py(array)]
     trades: Vec<Trade>,
 }
 
 /// Market trading days
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::quote::MarketTradingDays")]
+#[py(remote = "longbridge::quote::MarketTradingDays")]
 pub struct MarketTradingDays {
     /// Trading days
     #[py(array)]
     trading_days: Vec<PyDateWrapper>,
     /// Half trading days
     #[py(array)]
     half_trading_days: Vec<PyDateWrapper>,
```

### Comparing `longbridge-0.2.8/src/time.rs` & `longbridge-0.2.9/src/time.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/src/trade/context.rs` & `longbridge-0.2.9/src/trade/context.rs`

 * *Files 8% similar despite different names*

```diff
@@ -9,14 +9,15 @@
     },
 };
 use pyo3::{pyclass, pymethods, PyObject, PyResult};
 
 use crate::{
     config::Config,
     decimal::PyDecimal,
+    error::ErrorNewType,
     time::{PyDateWrapper, PyOffsetDateTimeWrapper},
     trade::{
         push::handle_push_event,
         types::{
             AccountBalance, BalanceType, CashFlow, Execution, FundPositionsResponse, Order,
             OrderSide, OrderStatus, OrderType, OutsideRTH, StockPositionsResponse,
             SubmitOrderResponse, TimeInForceType, TopicType,
@@ -32,32 +33,37 @@
 impl TradeContext {
     #[new]
     fn new(config: &Config, handler: Option<PyObject>) -> PyResult<Self> {
         let ctx = TradeContextSync::try_new(Arc::new(config.0.clone()), move |event| {
             if let Some(handler) = &handler {
                 handle_push_event(handler, event);
             }
-        })?;
+        })
+        .map_err(ErrorNewType)?;
         Ok(Self(ctx))
     }
 
     /// Subscribe
     fn subscribe(&self, topics: Vec<TopicType>) -> PyResult<()> {
-        self.0.subscribe(topics.into_iter().map(Into::into))?;
+        self.0
+            .subscribe(topics.into_iter().map(Into::into))
+            .map_err(ErrorNewType)?;
         Ok(())
     }
 
     /// Unsubscribe
     fn unsubscribe(&self, topics: Vec<TopicType>) -> PyResult<()> {
-        self.0.unsubscribe(topics.into_iter().map(Into::into))?;
+        self.0
+            .unsubscribe(topics.into_iter().map(Into::into))
+            .map_err(ErrorNewType)?;
         Ok(())
     }
 
     /// Get history executions
-    pub fn history_executions(
+    fn history_executions(
         &self,
         symbol: Option<String>,
         start_at: Option<PyOffsetDateTimeWrapper>,
         end_at: Option<PyOffsetDateTimeWrapper>,
     ) -> PyResult<Vec<Execution>> {
         let mut opts = GetHistoryExecutionsOptions::new();
 
@@ -68,45 +74,47 @@
             opts = opts.start_at(start_at.0);
         }
         if let Some(end_at) = end_at {
             opts = opts.end_at(end_at.0);
         }
 
         self.0
-            .history_executions(Some(opts))?
+            .history_executions(Some(opts))
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get today executions
-    pub fn today_executions(
+    fn today_executions(
         &self,
         symbol: Option<String>,
         order_id: Option<String>,
     ) -> PyResult<Vec<Execution>> {
         let mut opts = GetTodayExecutionsOptions::new();
 
         if let Some(symbol) = symbol {
             opts = opts.symbol(symbol);
         }
         if let Some(order_id) = order_id {
             opts = opts.order_id(order_id);
         }
 
         self.0
-            .today_executions(Some(opts))?
+            .today_executions(Some(opts))
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get history orders
-    #[args(default = "[]")]
-    pub fn history_orders(
+    #[args(status = "vec![]")]
+    fn history_orders(
         &self,
         symbol: Option<String>,
         status: Vec<OrderStatus>,
         side: Option<OrderSide>,
         market: Option<Market>,
         start_at: Option<PyOffsetDateTimeWrapper>,
         end_at: Option<PyOffsetDateTimeWrapper>,
@@ -127,22 +135,23 @@
             opts = opts.start_at(start_at.0);
         }
         if let Some(end_at) = end_at {
             opts = opts.end_at(end_at.0);
         }
 
         self.0
-            .history_orders(Some(opts))?
+            .history_orders(Some(opts))
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Get today orders
-    pub fn today_orders(
+    fn today_orders(
         &self,
         symbol: Option<String>,
         status: Vec<OrderStatus>,
         side: Option<OrderSide>,
         market: Option<Market>,
     ) -> PyResult<Vec<Order>> {
         let mut opts = GetTodayOrdersOptions::new();
@@ -155,23 +164,24 @@
             opts = opts.side(side.into());
         }
         if let Some(market) = market {
             opts = opts.market(market.into());
         }
 
         self.0
-            .today_orders(Some(opts))?
+            .today_orders(Some(opts))
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect()
     }
 
     /// Replace order
     #[allow(clippy::too_many_arguments)]
-    pub fn replace_order(
+    fn replace_order(
         &self,
         order_id: String,
         quantity: PyDecimal,
         price: Option<PyDecimal>,
         trigger_price: Option<PyDecimal>,
         limit_offset: Option<PyDecimal>,
         trailing_amount: Option<PyDecimal>,
@@ -195,21 +205,21 @@
         if let Some(trailing_percent) = trailing_percent {
             opts = opts.trailing_percent(trailing_percent.into());
         }
         if let Some(remark) = remark {
             opts = opts.remark(remark);
         }
 
-        self.0.replace_order(opts)?;
+        self.0.replace_order(opts).map_err(ErrorNewType)?;
         Ok(())
     }
 
     /// Submit order
     #[allow(clippy::too_many_arguments)]
-    pub fn submit_order(
+    fn submit_order(
         &self,
         symbol: String,
         order_type: OrderType,
         side: OrderSide,
         submitted_quantity: PyDecimal,
         time_in_force: TimeInForceType,
         submitted_price: Option<PyDecimal>,
@@ -250,34 +260,35 @@
         if let Some(outside_rth) = outside_rth {
             opts = opts.outside_rth(outside_rth.into());
         }
         if let Some(remark) = remark {
             opts = opts.remark(remark);
         }
 
-        self.0.submit_order(opts)?.try_into()
+        self.0.submit_order(opts).map_err(ErrorNewType)?.try_into()
     }
 
     /// Withdraw order
-    pub fn withdraw_order(&self, order_id: String) -> PyResult<()> {
-        self.0.withdraw_order(order_id)?;
+    fn withdraw_order(&self, order_id: String) -> PyResult<()> {
+        self.0.withdraw_order(order_id).map_err(ErrorNewType)?;
         Ok(())
     }
 
     /// Get account balance
-    pub fn account_balance(&self) -> PyResult<Vec<AccountBalance>> {
+    fn account_balance(&self) -> PyResult<Vec<AccountBalance>> {
         self.0
-            .account_balance()?
+            .account_balance()
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect::<PyResult<Vec<_>>>()
     }
 
     /// Get cash flow
-    pub fn cash_flow(
+    fn cash_flow(
         &self,
         start_at: PyOffsetDateTimeWrapper,
         end_at: PyOffsetDateTimeWrapper,
         business_type: Option<BalanceType>,
         symbol: Option<String>,
         page: Option<usize>,
         size: Option<usize>,
@@ -294,29 +305,32 @@
             opts = opts.page(page);
         }
         if let Some(size) = size {
             opts = opts.size(size);
         }
 
         self.0
-            .cash_flow(opts)?
+            .cash_flow(opts)
+            .map_err(ErrorNewType)?
             .into_iter()
             .map(TryInto::try_into)
             .collect::<PyResult<Vec<_>>>()
     }
 
     /// Get fund positions
     #[args(symbols = "vec![]")]
-    pub fn fund_positions(&self, symbols: Vec<String>) -> PyResult<FundPositionsResponse> {
+    fn fund_positions(&self, symbols: Vec<String>) -> PyResult<FundPositionsResponse> {
         self.0
-            .fund_positions(GetFundPositionsOptions::new().symbols(symbols))?
+            .fund_positions(GetFundPositionsOptions::new().symbols(symbols))
+            .map_err(ErrorNewType)?
             .try_into()
     }
 
     /// Get stock positions
     #[args(symbols = "vec![]")]
-    pub fn stock_positions(&self, symbols: Vec<String>) -> PyResult<StockPositionsResponse> {
+    fn stock_positions(&self, symbols: Vec<String>) -> PyResult<StockPositionsResponse> {
         self.0
-            .stock_positions(GetStockPositionsOptions::new().symbols(symbols))?
+            .stock_positions(GetStockPositionsOptions::new().symbols(symbols))
+            .map_err(ErrorNewType)?
             .try_into()
     }
 }
```

### Comparing `longbridge-0.2.8/src/trade/mod.rs` & `longbridge-0.2.9/src/trade/mod.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/src/trade/push.rs` & `longbridge-0.2.9/src/trade/push.rs`

 * *Files identical despite different names*

### Comparing `longbridge-0.2.8/src/trade/types.rs` & `longbridge-0.2.9/src/trade/types.rs`

 * *Files 6% similar despite different names*

```diff
@@ -5,24 +5,24 @@
     decimal::PyDecimal,
     time::{PyDateWrapper, PyOffsetDateTimeWrapper},
 };
 
 /// Topic type
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::TopicType")]
-pub enum TopicType {
+#[py(remote = "longbridge::trade::TopicType")]
+pub(crate) enum TopicType {
     /// Private notification for trade
     Private,
 }
 
 /// Trade
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::trade::Execution")]
+#[py(remote = "longbridge::trade::Execution")]
 pub(crate) struct Execution {
     /// Order ID
     order_id: String,
     /// Execution ID
     trade_id: String,
     /// Security code
     symbol: String,
@@ -32,15 +32,15 @@
     quantity: PyDecimal,
     /// Executed price
     price: PyDecimal,
 }
 
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::OrderStatus")]
+#[py(remote = "longbridge::trade::OrderStatus")]
 pub(crate) enum OrderStatus {
     /// Unknown
     Unknown,
     /// Not reported
     NotReported,
     /// Not reported (Replaced Order)
     ReplacedNotReported,
@@ -74,27 +74,27 @@
     Expired,
     /// Partial Withdrawal
     PartialWithdrawal,
 }
 
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::OrderSide")]
+#[py(remote = "longbridge::trade::OrderSide")]
 pub(crate) enum OrderSide {
     /// Unknown
     Unknown,
     /// Buy
     Buy,
     /// Sell
     Sell,
 }
 
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::OrderType")]
+#[py(remote = "longbridge::trade::OrderType")]
 #[allow(clippy::upper_case_acronyms)]
 pub(crate) enum OrderType {
     /// Unknown
     Unknown,
     /// Limit Order
     LO,
     /// Enhanced Limit Order
@@ -120,73 +120,73 @@
     /// Trailing Market If Touched (Trailing Percent)
     TSMPCT,
 }
 
 /// Order tag
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::OrderTag")]
+#[py(remote = "longbridge::trade::OrderTag")]
 pub(crate) enum OrderTag {
     /// Unknown
     Unknown,
     /// Normal Order
     Normal,
     /// Long term Order
     LongTerm,
     /// Grey Order
     Grey,
 }
 
 /// Time in force type
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::TimeInForceType")]
+#[py(remote = "longbridge::trade::TimeInForceType")]
 pub(crate) enum TimeInForceType {
     /// Unknown
     Unknown,
     /// Day Order
     Day,
     /// Good Til Canceled Order
     GoodTilCanceled,
     /// Good Til Date Order
     GoodTilDate,
 }
 
 /// Trigger status
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::TriggerStatus")]
-pub enum TriggerStatus {
+#[py(remote = "longbridge::trade::TriggerStatus")]
+pub(crate) enum TriggerStatus {
     /// Unknown
     Unknown,
     /// Deactive
     Deactive,
     /// Active
     Active,
     /// Released
     Released,
 }
 
 /// Enable or disable outside regular trading hours
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::OutsideRTH")]
-pub enum OutsideRTH {
+#[py(remote = "longbridge::trade::OutsideRTH")]
+pub(crate) enum OutsideRTH {
     /// Unknown
     Unknown,
     /// Regular trading hour only
     RTHOnly,
     /// Any time
     AnyTime,
 }
 
 /// Order
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::trade::Order")]
+#[py(remote = "longbridge::trade::Order")]
 pub(crate) struct Order {
     /// Order ID
     order_id: String,
     /// Order status
     status: OrderStatus,
     /// Stock name
     stock_name: String,
@@ -248,15 +248,15 @@
     #[py(opt)]
     outside_rth: Option<OutsideRTH>,
 }
 
 /// Order changed message
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::trade::PushOrderChanged")]
+#[py(remote = "longbridge::trade::PushOrderChanged")]
 pub(crate) struct PushOrderChanged {
     /// Order side
     side: OrderSide,
     /// Stock name
     stock_name: String,
     /// Submitted quantity
     quantity: String,
@@ -305,24 +305,24 @@
     /// Account no
     account_no: String,
 }
 
 /// Response for withdraw order request
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::trade::SubmitOrderResponse")]
+#[py(remote = "longbridge::trade::SubmitOrderResponse")]
 pub(crate) struct SubmitOrderResponse {
     /// Order id
     order_id: String,
 }
 
 /// Account balance
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::trade::CashInfo")]
+#[py(remote = "longbridge::trade::CashInfo")]
 pub(crate) struct CashInfo {
     /// Withdraw cash
     withdraw_cash: PyDecimal,
     /// Available cash
     available_cash: PyDecimal,
     /// Frozen cash
     frozen_cash: PyDecimal,
@@ -331,15 +331,15 @@
     /// Currency
     currency: String,
 }
 
 /// Account balance
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::trade::AccountBalance")]
+#[py(remote = "longbridge::trade::AccountBalance")]
 pub(crate) struct AccountBalance {
     /// Total cash
     total_cash: PyDecimal,
     /// Maximum financing amount
     max_finance_amount: PyDecimal,
     /// Remaining financing amount
     remaining_finance_amount: PyDecimal,
@@ -352,42 +352,42 @@
     /// Cash details
     #[py(array)]
     cash_infos: Vec<CashInfo>,
 }
 
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::BalanceType")]
-pub enum BalanceType {
+#[py(remote = "longbridge::trade::BalanceType")]
+pub(crate) enum BalanceType {
     /// Unknown
     Unknown,
     /// Limit Order
     Cash,
     /// Stock
     Stock,
     /// Fund
     Fund,
 }
 
 #[pyclass]
 #[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
-#[py(from = "longbridge::trade::CashFlowDirection")]
-pub enum CashFlowDirection {
+#[py(remote = "longbridge::trade::CashFlowDirection")]
+pub(crate) enum CashFlowDirection {
     /// Unknown
     Unknown,
     /// Out
     Out,
     /// Stock
     In,
 }
 
 /// Account balance
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::trade::CashFlow")]
+#[py(remote = "longbridge::trade::CashFlow")]
 pub(crate) struct CashFlow {
     /// Cash flow name
     transaction_flow_name: String,
     /// Outflow direction
     direction: CashFlowDirection,
     /// Balance type
     business_type: BalanceType,
@@ -402,85 +402,85 @@
     /// Cash flow description
     description: String,
 }
 
 /// Fund positions response
 #[pyclass]
 #[derive(Debug, PyObject)]
-#[py(from = "longbridge::trade::FundPositionsResponse")]
+#[py(remote = "longbridge::trade::FundPositionsResponse")]
 pub(crate) struct FundPositionsResponse {
     #[py(array)]
-    pub channels: Vec<FundPositionChannel>,
+    channels: Vec<FundPositionChannel>,
 }
 
 /// Fund position channel
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::trade::FundPositionChannel")]
+#[py(remote = "longbridge::trade::FundPositionChannel")]
 pub(crate) struct FundPositionChannel {
     /// Account type
     account_channel: String,
     /// Fund positions
     #[py(array)]
     positions: Vec<FundPosition>,
 }
 
 /// Fund position
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::trade::FundPosition")]
+#[py(remote = "longbridge::trade::FundPosition")]
 pub(crate) struct FundPosition {
     /// Fund ISIN code
     symbol: String,
     /// Current equity
     current_net_asset_value: PyDecimal,
     /// Current equity time
     net_asset_value_day: PyOffsetDateTimeWrapper,
     /// Fund name
     symbol_name: String,
     /// Currency
     currency: String,
     /// Net cost
     cost_net_asset_value: PyDecimal,
     /// Holding units
-    pub holding_units: PyDecimal,
+    holding_units: PyDecimal,
 }
 
 /// Stock positions response
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::trade::StockPositionsResponse")]
+#[py(remote = "longbridge::trade::StockPositionsResponse")]
 pub(crate) struct StockPositionsResponse {
     #[py(array)]
-    pub channels: Vec<StockPositionChannel>,
+    channels: Vec<StockPositionChannel>,
 }
 
 /// Stock position channel
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::trade::StockPositionChannel")]
+#[py(remote = "longbridge::trade::StockPositionChannel")]
 pub(crate) struct StockPositionChannel {
     /// Account type
     account_channel: String,
     /// Fund details
     #[py(array)]
     positions: Vec<StockPosition>,
 }
 
 /// Stock position
 #[pyclass]
 #[derive(Debug, PyObject, Clone)]
-#[py(from = "longbridge::trade::StockPosition")]
+#[py(remote = "longbridge::trade::StockPosition")]
 pub(crate) struct StockPosition {
     /// Stock code
     symbol: String,
     /// Stock name
     symbol_name: String,
     /// The number of holdings
-    quality: PyDecimal,
+    quantity: PyDecimal,
     /// Available quantity
     available_quality: PyDecimal,
     /// Currency
     currency: String,
     /// Cost Price(According to the client's choice of average purchase or
     /// diluted cost)
     cost_price: PyDecimal,
```

### Comparing `longbridge-0.2.8/PKG-INFO` & `longbridge-0.2.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: longbridge
-Version: 0.2.8
+Version: 0.2.9
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Office/Business :: Financial
 Classifier: Programming Language :: Rust
 Classifier: Programming Language :: Python :: Implementation :: CPython
 Summary: A Python library for Longbridge Open API
 Keywords: longbridge,openapi,sdk
 Home-Page: https://open.longbridgeapp.com/en/
 License: MIT OR Apache-2.0
 Description-Content-Type: text/markdown; charset=UTF-8; variant=GFM
-Project-URL: documentation, https://open.longbridgeapp.com/en/docs
-Project-URL: homepage, https://open.longbridgeapp.com/en/
 Project-URL: repository, https://github.com/longbridgeapp/openapi-sdk
+Project-URL: documentation, https://open.longbridgeapp.com/en/docs
 Project-URL: changelog, https://github.com/longbridgeapp/openapi-sdk/blob/master/python/CHANGELOG.md
+Project-URL: homepage, https://open.longbridgeapp.com/en/
 
 # Longbridge OpenAPI SDK for Python
 
 `longbridge` provides an easy-to-use interface for invokes [`Longbridge OpenAPI`](https://open.longbridgeapp.com/en/).
 
 ## Quickstart
```

