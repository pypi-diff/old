# Comparing `tmp/kedixa-0.0.1-py3-none-any.whl.zip` & `tmp/kedixa-0.0.2-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,10 +1,39 @@
-Zip file size: 3170 bytes, number of entries: 8
--rw-rw-r--  2.0 unx        0 b- defN 23-Jan-13 09:46 kedixa/__init__.py
--rw-rw-r--  2.0 unx      877 b- defN 23-Feb-16 11:16 kedixa/file_loader.py
--rw-rw-r--  2.0 unx     3828 b- defN 23-Feb-16 11:22 kedixa/mprocess.py
--rw-rw-r--  2.0 unx      145 b- defN 23-Jan-13 09:47 kedixa/version.py
--rw-rw-r--  2.0 unx      196 b- defN 23-Feb-16 12:01 kedixa-0.0.1.dist-info/METADATA
--rw-rw-r--  2.0 unx       92 b- defN 23-Feb-16 12:01 kedixa-0.0.1.dist-info/WHEEL
--rw-rw-r--  2.0 unx        7 b- defN 23-Feb-16 12:01 kedixa-0.0.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      589 b- defN 23-Feb-16 12:01 kedixa-0.0.1.dist-info/RECORD
-8 files, 5734 bytes uncompressed, 2144 bytes compressed:  62.6%
+Zip file size: 31877 bytes, number of entries: 37
+-rw-r--r--  2.0 unx        0 b- defN 23-Feb-28 08:01 kedixa/__init__.py
+-rw-r--r--  2.0 unx       46 b- defN 23-Mar-12 13:18 kedixa/compat.py
+-rw-r--r--  2.0 unx      877 b- defN 23-Feb-28 08:01 kedixa/file_loader.py
+-rw-r--r--  2.0 unx     3828 b- defN 23-Feb-28 08:01 kedixa/mprocess.py
+-rw-r--r--  2.0 unx      145 b- defN 23-Apr-07 13:12 kedixa/version.py
+-rw-r--r--  2.0 unx      286 b- defN 23-Apr-07 13:09 kedixa/comm/__init__.py
+-rw-r--r--  2.0 unx     1623 b- defN 23-Mar-25 08:13 kedixa/comm/address.py
+-rw-r--r--  2.0 unx     6678 b- defN 23-Apr-07 10:56 kedixa/comm/basic.py
+-rw-r--r--  2.0 unx     1525 b- defN 23-Apr-07 10:56 kedixa/comm/bridge.py
+-rw-r--r--  2.0 unx     2043 b- defN 23-Apr-07 10:57 kedixa/comm/connection.py
+-rw-r--r--  2.0 unx     1082 b- defN 23-Mar-18 17:04 kedixa/comm/debug_filter.py
+-rw-r--r--  2.0 unx     1107 b- defN 23-Apr-07 10:57 kedixa/comm/debug_transformer.py
+-rw-r--r--  2.0 unx      771 b- defN 23-Apr-07 10:58 kedixa/comm/exception.py
+-rw-r--r--  2.0 unx     1162 b- defN 23-Mar-12 13:18 kedixa/comm/file_adaptor.py
+-rw-r--r--  2.0 unx     1929 b- defN 23-Mar-12 13:18 kedixa/comm/read_until_filter.py
+-rw-r--r--  2.0 unx     1969 b- defN 23-Apr-07 10:58 kedixa/comm/read_until_transformer.py
+-rw-r--r--  2.0 unx     3439 b- defN 23-Mar-25 08:01 kedixa/comm/socket_adaptor.py
+-rw-r--r--  2.0 unx     5294 b- defN 23-Feb-26 14:05 kedixa/comm/socks5_filter.py
+-rw-r--r--  2.0 unx     5310 b- defN 23-Apr-07 11:12 kedixa/comm/socks5_updater.py
+-rw-r--r--  2.0 unx     3487 b- defN 23-Mar-26 14:20 kedixa/comm/speed_limit_filter.py
+-rw-r--r--  2.0 unx     3507 b- defN 23-Apr-07 10:58 kedixa/comm/speed_limit_transformer.py
+-rw-r--r--  2.0 unx     2151 b- defN 23-Mar-12 13:18 kedixa/comm/ssl_filter.py
+-rw-r--r--  2.0 unx     2171 b- defN 23-Apr-07 10:58 kedixa/comm/ssl_transformer.py
+-rw-r--r--  2.0 unx      129 b- defN 23-Apr-07 13:09 kedixa/comm/http/__init__.py
+-rw-r--r--  2.0 unx     1996 b- defN 23-Apr-01 02:16 kedixa/comm/http/http_chunk_filter.py
+-rw-r--r--  2.0 unx     2046 b- defN 23-Apr-07 10:59 kedixa/comm/http/http_chunk_transformer.py
+-rw-r--r--  2.0 unx     2011 b- defN 23-Mar-18 06:37 kedixa/comm/http/http_code_map.py
+-rw-r--r--  2.0 unx    12688 b- defN 23-Apr-07 11:00 kedixa/comm/http/http_message.py
+-rw-r--r--  2.0 unx     2356 b- defN 23-Apr-01 02:17 kedixa/comm/http/http_proxy_filter.py
+-rw-r--r--  2.0 unx     2435 b- defN 23-Apr-07 11:10 kedixa/comm/http/http_proxy_updater.py
+-rw-r--r--  2.0 unx       65 b- defN 23-Apr-06 10:25 kedixa/comm/websocket/__init__.py
+-rw-r--r--  2.0 unx     6842 b- defN 23-Apr-06 10:37 kedixa/comm/websocket/websocket_client.py
+-rw-r--r--  2.0 unx     3860 b- defN 23-Apr-01 03:14 kedixa/comm/websocket/websocket_message.py
+-rw-r--r--  2.0 unx      227 b- defN 23-Apr-07 13:12 kedixa-0.0.2.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-07 13:12 kedixa-0.0.2.dist-info/WHEEL
+-rw-r--r--  2.0 unx        7 b- defN 23-Apr-07 13:12 kedixa-0.0.2.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     3117 b- defN 23-Apr-07 13:12 kedixa-0.0.2.dist-info/RECORD
+37 files, 88301 bytes uncompressed, 26885 bytes compressed:  69.6%
```

## zipnote {}

```diff
@@ -1,25 +1,112 @@
 Filename: kedixa/__init__.py
 Comment: 
 
+Filename: kedixa/compat.py
+Comment: 
+
 Filename: kedixa/file_loader.py
 Comment: 
 
 Filename: kedixa/mprocess.py
 Comment: 
 
 Filename: kedixa/version.py
 Comment: 
 
-Filename: kedixa-0.0.1.dist-info/METADATA
+Filename: kedixa/comm/__init__.py
+Comment: 
+
+Filename: kedixa/comm/address.py
+Comment: 
+
+Filename: kedixa/comm/basic.py
+Comment: 
+
+Filename: kedixa/comm/bridge.py
+Comment: 
+
+Filename: kedixa/comm/connection.py
+Comment: 
+
+Filename: kedixa/comm/debug_filter.py
+Comment: 
+
+Filename: kedixa/comm/debug_transformer.py
+Comment: 
+
+Filename: kedixa/comm/exception.py
+Comment: 
+
+Filename: kedixa/comm/file_adaptor.py
+Comment: 
+
+Filename: kedixa/comm/read_until_filter.py
+Comment: 
+
+Filename: kedixa/comm/read_until_transformer.py
+Comment: 
+
+Filename: kedixa/comm/socket_adaptor.py
+Comment: 
+
+Filename: kedixa/comm/socks5_filter.py
+Comment: 
+
+Filename: kedixa/comm/socks5_updater.py
+Comment: 
+
+Filename: kedixa/comm/speed_limit_filter.py
+Comment: 
+
+Filename: kedixa/comm/speed_limit_transformer.py
+Comment: 
+
+Filename: kedixa/comm/ssl_filter.py
+Comment: 
+
+Filename: kedixa/comm/ssl_transformer.py
+Comment: 
+
+Filename: kedixa/comm/http/__init__.py
+Comment: 
+
+Filename: kedixa/comm/http/http_chunk_filter.py
+Comment: 
+
+Filename: kedixa/comm/http/http_chunk_transformer.py
+Comment: 
+
+Filename: kedixa/comm/http/http_code_map.py
+Comment: 
+
+Filename: kedixa/comm/http/http_message.py
+Comment: 
+
+Filename: kedixa/comm/http/http_proxy_filter.py
+Comment: 
+
+Filename: kedixa/comm/http/http_proxy_updater.py
+Comment: 
+
+Filename: kedixa/comm/websocket/__init__.py
+Comment: 
+
+Filename: kedixa/comm/websocket/websocket_client.py
+Comment: 
+
+Filename: kedixa/comm/websocket/websocket_message.py
+Comment: 
+
+Filename: kedixa-0.0.2.dist-info/METADATA
 Comment: 
 
-Filename: kedixa-0.0.1.dist-info/WHEEL
+Filename: kedixa-0.0.2.dist-info/WHEEL
 Comment: 
 
-Filename: kedixa-0.0.1.dist-info/top_level.txt
+Filename: kedixa-0.0.2.dist-info/top_level.txt
 Comment: 
 
-Filename: kedixa-0.0.1.dist-info/RECORD
+Filename: kedixa-0.0.2.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## kedixa/version.py

```diff
@@ -1,4 +1,4 @@
 __major_version__ = 0
 __minor_version__ = 0
-__bugfix_version__ = 1
+__bugfix_version__ = 2
 __version__ = f'{__major_version__}.{__minor_version__}.{__bugfix_version__}'
```

