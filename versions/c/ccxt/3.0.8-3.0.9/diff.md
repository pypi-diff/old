# Comparing `tmp/ccxt-3.0.8.tar.gz` & `tmp/ccxt-3.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/ccxt-3.0.8.tar", last modified: Tue Mar 14 19:04:21 2023, max compression
+gzip compressed data, was "dist/ccxt-3.0.9.tar", last modified: Wed Mar 15 08:55:18 2023, max compression
```

## Comparing `ccxt-3.0.8.tar` & `ccxt-3.0.9.tar`

### file list

```diff
@@ -1,351 +1,351 @@
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.394651 ccxt-3.0.8/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1068 2023-03-14 19:04:07.000000 ccxt-3.0.8/LICENSE.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      100 2023-03-14 18:36:46.000000 ccxt-3.0.8/MANIFEST.in
--rw-rw-r--   0 travis    (2000) travis    (2000)   114885 2023-03-14 19:04:21.398651 ccxt-3.0.8/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)   102253 2023-03-14 18:36:46.000000 ccxt-3.0.8/README.rst
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.342647 ccxt-3.0.8/ccxt/
--rw-rw-r--   0 travis    (2000) travis    (2000)    15912 2023-03-14 19:04:05.000000 ccxt-3.0.8/ccxt/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    40996 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/ace.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    32886 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/alpaca.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   125822 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/ascendex.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.374650 ccxt-3.0.8/ccxt/async_support/
--rw-rw-r--   0 travis    (2000) travis    (2000)    15745 2023-03-14 19:04:05.000000 ccxt-3.0.8/ccxt/async_support/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    41226 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/ace.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33032 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/alpaca.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   126436 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/ascendex.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.374650 ccxt-3.0.8/ccxt/async_support/base/
--rw-rw-r--   0 travis    (2000) travis    (2000)       67 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   116899 2023-03-14 19:04:05.000000 ccxt-3.0.8/ccxt/async_support/base/exchange.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1847 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/throttler.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.378650 ccxt-3.0.8/ccxt/async_support/base/ws/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1791 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4987 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/aiohttp_client.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6085 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/cache.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7283 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/client.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3258 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/fast_client.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1495 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/functions.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      249 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/future.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2894 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/order_book.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6079 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/base/ws/order_book_side.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1091 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bequant.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    62156 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bigone.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   358204 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/binance.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1609 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/binancecoinm.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2104 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/binanceus.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1809 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/binanceusdm.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    35451 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bit2c.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    38962 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitbank.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      404 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitbay.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    45921 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitbns.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      419 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitcoincom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    69438 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitfinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   111044 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitfinex2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    37660 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitflyer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    28175 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitforex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   199276 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitget.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    42484 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bithumb.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   130252 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitmart.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   118655 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitmex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    63222 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitopro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    87293 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitpanda.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    85319 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitrue.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    68591 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitso.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    82101 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitstamp.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    17785 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitstamp1.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    93314 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bittrex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    76743 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bitvavo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    74192 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bkex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16205 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bl3p.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    47060 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/blockchaincom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34945 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/btcalpha.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22357 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/btcbox.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   110681 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/btcex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    48372 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/btcmarkets.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    21807 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/btctradeua.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    35240 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/btcturk.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    45641 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/buda.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   386287 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/bybit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    64828 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/cex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   124164 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinbase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1168 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinbaseprime.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    73502 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinbasepro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34067 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coincheck.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   188253 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    38909 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinfalcon.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    39472 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinmate.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34411 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinone.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18715 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/coinspot.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   104660 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/cryptocom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    79365 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/currencycom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    83985 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/delta.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   118966 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/deribit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   152112 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/digifinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    88514 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/exmo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1183 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/flowbtc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1194 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/fmfwio.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   219500 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/gate.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      401 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/gateio.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    69072 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/gemini.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    61961 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/hitbtc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   116300 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/hitbtc3.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    69106 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/hollaex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   339480 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/huobi.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    86429 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/huobijp.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      526 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/huobipro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    66310 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/idex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    29761 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/independentreserve.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    42404 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/indodax.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34892 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/itbit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   101201 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/kraken.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    80975 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/krakenfutures.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   157202 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/kucoin.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    93235 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/kucoinfutures.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    37610 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/kuna.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    69988 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/latoken.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33651 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/lbank.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    97774 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/lbank2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    40247 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/luno.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    48382 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/lykke.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34552 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/mercado.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   141627 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/mexc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   206083 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/mexc3.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   106106 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/ndax.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    61328 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/novadax.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    37058 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/oceanex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   177804 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/okcoin.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      392 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/okex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      398 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/okex5.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   260714 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/okx.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22756 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/paymium.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   183442 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/phemex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    83770 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/poloniex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    70002 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/poloniexfutures.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    66876 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/probit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    47293 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/ripio.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   115373 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/stex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    42340 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/tidex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    65239 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/timex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   117585 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/tokocrypto.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    73310 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/upbit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   103472 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/wavesexchange.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34628 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/wazirx.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    91898 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/whitebit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    93318 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/woo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    50778 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/yobit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27865 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/zaif.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   183865 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/zb.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    72999 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/async_support/zonda.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.378650 ccxt-3.0.8/ccxt/base/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1320 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/base/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6531 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/base/decimal_to_precision.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3401 2023-03-14 18:49:31.000000 ccxt-3.0.8/ccxt/base/errors.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   164338 2023-03-14 19:04:05.000000 ccxt-3.0.8/ccxt/base/exchange.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8565 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/base/precise.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1077 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bequant.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    61776 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bigone.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   357078 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/binance.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1571 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/binancecoinm.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2090 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/binanceus.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1771 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/binanceusdm.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    35245 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bit2c.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    38702 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitbank.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      390 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitbay.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    45667 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitbns.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      405 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitcoincom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    68998 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitfinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   110574 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitfinex2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    37352 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitflyer.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27969 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitforex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   198468 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitget.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    42266 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bithumb.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   129614 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitmart.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   118191 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitmex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    62854 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitopro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    86841 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitpanda.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    84963 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitrue.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    68205 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitso.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    81679 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitstamp.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    17639 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitstamp1.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    92808 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bittrex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    76333 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bitvavo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    73762 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bkex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16095 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bl3p.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    46632 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/blockchaincom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34667 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/btcalpha.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22163 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/btcbox.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   110055 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/btcex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    48022 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/btcmarkets.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    21661 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/btctradeua.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    35022 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/btcturk.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    45273 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/buda.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   384417 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/bybit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    64502 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/cex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   123520 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinbase.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1154 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinbaseprime.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    72996 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinbasepro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33861 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coincheck.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   187373 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    38613 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinfalcon.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    39224 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinmate.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34187 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinone.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18581 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/coinspot.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   104152 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/cryptocom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    78973 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/currencycom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    83605 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/delta.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   118424 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/deribit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   151412 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/digifinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    87972 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/exmo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1169 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/flowbtc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1180 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/fmfwio.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   218674 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/gate.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      387 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/gateio.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    68624 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/gemini.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    61527 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/hitbtc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   115614 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/hitbtc3.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    68684 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/hollaex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   338378 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/huobi.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    85947 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/huobijp.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      512 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/huobipro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    65882 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/idex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    29525 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/independentreserve.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    42132 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/indodax.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34644 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/itbit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   100659 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/kraken.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    80673 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/krakenfutures.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   156588 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/kucoin.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    92771 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/kucoinfutures.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    37362 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/kuna.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    69596 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/latoken.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33415 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/lbank.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    97226 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/lbank2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    39939 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/luno.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    48080 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/lykke.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34310 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/mercado.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   140851 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/mexc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   205055 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/mexc3.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   105582 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/ndax.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    60960 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/novadax.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    36720 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/oceanex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   177340 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/okcoin.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      378 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/okex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      384 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/okex5.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   259714 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/okx.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22568 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/paymium.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   182906 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/phemex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    83270 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/poloniex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    69634 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/poloniexfutures.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.390651 ccxt-3.0.8/ccxt/pro/
--rw-rw-r--   0 travis    (2000) travis    (2000)     5871 2023-03-14 19:04:05.000000 ccxt-3.0.8/ccxt/pro/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    26372 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/alpaca.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34257 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/ascendex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1081 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bequant.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    76677 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/binance.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      724 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/binancecoinm.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2016 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/binanceus.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      721 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/binanceusdm.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      914 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitcoincom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24527 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitfinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    41514 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitfinex2.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    44288 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitget.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24228 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitmart.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    54876 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitmex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12408 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitopro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16064 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitrue.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    20571 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitstamp.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    36334 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bittrex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    25674 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bitvavo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    30828 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/btcex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    60327 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/bybit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    44454 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/cex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1121 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/coinbaseprime.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    28811 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/coinbasepro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    41088 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/coinex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22695 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/cryptocom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    21858 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/currencycom.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33685 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/deribit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24171 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/exmo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    41655 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/gate.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      391 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/gateio.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24893 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/gemini.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14957 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/hitbtc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    21497 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/hollaex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    85197 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/huobi.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22414 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/huobijp.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      400 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/huobipro.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27696 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/idex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10899 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/independentreserve.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    44017 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/kraken.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33880 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/kucoin.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27539 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/kucoinfutures.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    12026 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/luno.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    44669 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/mexc.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22450 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/ndax.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    29967 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/okcoin.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      382 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/okex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    35390 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/okx.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    41618 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/phemex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11937 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/ripio.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     9327 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/upbit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    29511 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/wazirx.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33983 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/whitebit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24508 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/woo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    21298 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/pro/zb.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    66526 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/probit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    47033 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/ripio.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.390651 ccxt-3.0.8/ccxt/static_dependencies/
--rw-rw-r--   0 travis    (2000) travis    (2000)       30 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/__init__.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.390651 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/
--rw-rw-r--   0 travis    (2000) travis    (2000)      594 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18461 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/_version.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1886 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/curves.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6942 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/der.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    11336 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/ecdsa.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5517 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/ellipticcurve.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    14201 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/keys.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13468 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/numbertheory.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2572 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/rfc6979.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    10037 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/ecdsa/util.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.390651 ccxt-3.0.8/ccxt/static_dependencies/keccak/
--rw-rw-r--   0 travis    (2000) travis    (2000)       45 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/keccak/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     6934 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/static_dependencies/keccak/keccak.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   114873 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/stex.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.394651 ccxt-3.0.8/ccxt/test/
--rw-rw-r--   0 travis    (2000) travis    (2000)      362 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/test/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      864 2023-03-14 18:49:42.000000 ccxt-3.0.8/ccxt/test/test_account.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24990 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/test/test_async.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1177 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/test/test_calculate_fee.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7625 2023-03-14 18:49:39.000000 ccxt-3.0.8/ccxt/test/test_crypto.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    20468 2023-03-14 18:49:36.000000 ccxt-3.0.8/ccxt/test/test_decimal_to_precision.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1402 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/test/test_deep_extend.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3592 2023-03-14 18:49:37.000000 ccxt-3.0.8/ccxt/test/test_exchange_datetime_functions.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1247 2023-03-14 18:49:41.000000 ccxt-3.0.8/ccxt/test/test_leverage_tier.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1271 2023-03-14 18:49:42.000000 ccxt-3.0.8/ccxt/test/test_margin_modification.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4049 2023-03-14 18:49:40.000000 ccxt-3.0.8/ccxt/test/test_market.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1468 2023-03-14 18:49:41.000000 ccxt-3.0.8/ccxt/test/test_ohlcv.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2216 2023-03-14 18:49:41.000000 ccxt-3.0.8/ccxt/test/test_order.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      821 2023-03-14 18:49:41.000000 ccxt-3.0.8/ccxt/test/test_position.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    22795 2023-03-14 18:49:42.000000 ccxt-3.0.8/ccxt/test/test_sync.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3123 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/test/test_throttle.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3237 2023-03-14 18:49:40.000000 ccxt-3.0.8/ccxt/test/test_trade.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     1434 2023-03-14 18:49:41.000000 ccxt-3.0.8/ccxt/test/test_transaction.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    42092 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/tidex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    64907 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/timex.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   117241 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/tokocrypto.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    72876 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/upbit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   102978 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/wavesexchange.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    34380 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/wazirx.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    91446 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/whitebit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    92734 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/woo.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    50494 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/yobit.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    27683 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/zaif.py
--rw-rw-r--   0 travis    (2000) travis    (2000)   183189 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/zb.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    72709 2023-03-14 18:36:46.000000 ccxt-3.0.8/ccxt/zonda.py
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-14 19:04:21.342647 ccxt-3.0.8/ccxt.egg-info/
--rw-rw-r--   0 travis    (2000) travis    (2000)   114885 2023-03-14 19:04:21.000000 ccxt-3.0.8/ccxt.egg-info/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)     8089 2023-03-14 19:04:21.000000 ccxt-3.0.8/ccxt.egg-info/SOURCES.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2023-03-14 19:04:21.000000 ccxt-3.0.8/ccxt.egg-info/dependency_links.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      265 2023-03-14 19:04:21.000000 ccxt-3.0.8/ccxt.egg-info/requires.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)        5 2023-03-14 19:04:21.000000 ccxt-3.0.8/ccxt.egg-info/top_level.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     8093 2023-03-14 19:04:06.000000 ccxt-3.0.8/package.json
--rw-rw-r--   0 travis    (2000) travis    (2000)      205 2023-03-14 19:04:21.398651 ccxt-3.0.8/setup.cfg
--rwxrwxr-x   0 travis    (2000) travis    (2000)     3130 2023-03-14 18:36:46.000000 ccxt-3.0.8/setup.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.872025 ccxt-3.0.9/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1068 2023-03-15 08:55:04.000000 ccxt-3.0.9/LICENSE.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      100 2023-03-15 08:33:15.000000 ccxt-3.0.9/MANIFEST.in
+-rw-rw-r--   0 travis    (2000) travis    (2000)   114885 2023-03-15 08:55:18.876025 ccxt-3.0.9/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)   102253 2023-03-15 08:33:15.000000 ccxt-3.0.9/README.rst
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.712008 ccxt-3.0.9/ccxt/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    15912 2023-03-15 08:55:02.000000 ccxt-3.0.9/ccxt/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    40996 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/ace.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    32886 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/alpaca.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   125822 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/ascendex.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.808018 ccxt-3.0.9/ccxt/async_support/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    15745 2023-03-15 08:55:02.000000 ccxt-3.0.9/ccxt/async_support/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41226 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/ace.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33032 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/alpaca.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   126436 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/ascendex.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.812018 ccxt-3.0.9/ccxt/async_support/base/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       67 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   116899 2023-03-15 08:55:02.000000 ccxt-3.0.9/ccxt/async_support/base/exchange.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1847 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/throttler.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.816019 ccxt-3.0.9/ccxt/async_support/base/ws/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1791 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4987 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/aiohttp_client.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6085 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/cache.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7283 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/client.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3258 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/fast_client.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1495 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/functions.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      249 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/future.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2894 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/order_book.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6079 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/base/ws/order_book_side.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1091 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bequant.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    62156 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bigone.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   358204 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/binance.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1609 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/binancecoinm.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2104 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/binanceus.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1809 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/binanceusdm.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35451 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bit2c.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    38962 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitbank.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      404 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitbay.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    45921 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitbns.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      419 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitcoincom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    69438 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitfinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   111044 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitfinex2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    37660 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitflyer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    28175 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitforex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   199276 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitget.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    42484 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bithumb.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   130252 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitmart.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   118655 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitmex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    63222 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitopro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    87293 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitpanda.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    85319 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitrue.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    68591 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitso.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    82101 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitstamp.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    17785 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitstamp1.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    93314 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bittrex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    76743 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bitvavo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    74192 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bkex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16205 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bl3p.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    47060 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/blockchaincom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34945 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/btcalpha.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22357 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/btcbox.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   110681 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/btcex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    48372 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/btcmarkets.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21807 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/btctradeua.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35240 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/btcturk.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    45641 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/buda.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   386287 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/bybit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    64828 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/cex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   124164 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinbase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1168 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinbaseprime.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    73502 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinbasepro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34067 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coincheck.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   188253 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    38909 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinfalcon.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    39472 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinmate.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34411 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinone.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18715 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/coinspot.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   104660 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/cryptocom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    79365 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/currencycom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    83985 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/delta.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   118966 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/deribit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   152112 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/digifinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    88514 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/exmo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1183 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/flowbtc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1194 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/fmfwio.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   219500 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/gate.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      401 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/gateio.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    69072 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/gemini.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    61961 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/hitbtc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   116300 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/hitbtc3.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    69106 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/hollaex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   339480 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/huobi.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    86429 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/huobijp.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      526 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/huobipro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    66310 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/idex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    29761 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/independentreserve.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    42404 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/indodax.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34892 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/itbit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   101201 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/kraken.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    80975 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/krakenfutures.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   157202 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/kucoin.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    93235 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/kucoinfutures.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    37610 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/kuna.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    69988 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/latoken.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33651 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/lbank.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    97774 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/lbank2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    40247 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/luno.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    48382 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/lykke.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34552 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/mercado.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   141627 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/mexc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   206083 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/mexc3.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   106106 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/ndax.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    61328 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/novadax.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    37058 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/oceanex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   177804 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/okcoin.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      392 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/okex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      398 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/okex5.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   260714 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/okx.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22756 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/paymium.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   183442 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/phemex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    83770 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/poloniex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    70002 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/poloniexfutures.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    66876 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/probit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    47293 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/ripio.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   115373 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/stex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    42340 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/tidex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    65239 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/timex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   117585 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/tokocrypto.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    73310 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/upbit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   103472 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/wavesexchange.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34628 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/wazirx.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    91898 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/whitebit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    93318 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/woo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    50778 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/yobit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27865 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/zaif.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   183865 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/zb.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    72999 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/async_support/zonda.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.820019 ccxt-3.0.9/ccxt/base/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1320 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/base/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6531 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/base/decimal_to_precision.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3401 2023-03-15 08:40:40.000000 ccxt-3.0.9/ccxt/base/errors.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   164338 2023-03-15 08:55:02.000000 ccxt-3.0.9/ccxt/base/exchange.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8565 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/base/precise.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1077 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bequant.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    61776 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bigone.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   357078 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/binance.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1571 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/binancecoinm.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2090 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/binanceus.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1771 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/binanceusdm.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35245 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bit2c.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    38702 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitbank.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      390 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitbay.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    45667 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitbns.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      405 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitcoincom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    68998 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitfinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   110574 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitfinex2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    37352 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitflyer.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27969 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitforex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   198468 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitget.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    42266 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bithumb.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   129614 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitmart.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   118191 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitmex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    62854 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitopro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    86841 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitpanda.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    84963 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitrue.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    68205 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitso.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    81679 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitstamp.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    17639 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitstamp1.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    92808 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bittrex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    76333 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bitvavo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    73762 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bkex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16095 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bl3p.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    46632 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/blockchaincom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34667 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/btcalpha.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22163 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/btcbox.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   110055 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/btcex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    48022 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/btcmarkets.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21661 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/btctradeua.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35022 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/btcturk.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    45273 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/buda.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   384417 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/bybit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    64502 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/cex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   123520 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinbase.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1154 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinbaseprime.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    72996 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinbasepro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33861 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coincheck.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   187373 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    38613 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinfalcon.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    39224 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinmate.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34187 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinone.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18581 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/coinspot.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   104152 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/cryptocom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    78973 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/currencycom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    83605 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/delta.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   118424 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/deribit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   151412 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/digifinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    87972 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/exmo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1169 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/flowbtc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1180 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/fmfwio.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   218674 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/gate.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      387 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/gateio.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    68624 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/gemini.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    61527 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/hitbtc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   115614 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/hitbtc3.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    68684 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/hollaex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   338378 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/huobi.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    85947 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/huobijp.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      512 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/huobipro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    65882 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/idex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    29525 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/independentreserve.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    42132 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/indodax.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34644 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/itbit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   100659 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/kraken.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    80673 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/krakenfutures.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   156588 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/kucoin.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    92771 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/kucoinfutures.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    37362 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/kuna.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    69596 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/latoken.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33415 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/lbank.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    97226 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/lbank2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    39939 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/luno.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    48080 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/lykke.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34310 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/mercado.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   140851 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/mexc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   205055 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/mexc3.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   105582 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/ndax.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    60960 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/novadax.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    36720 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/oceanex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   177340 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/okcoin.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      378 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/okex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      384 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/okex5.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   259714 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/okx.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22568 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/paymium.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   182906 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/phemex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    83270 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/poloniex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    69634 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/poloniexfutures.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.856023 ccxt-3.0.9/ccxt/pro/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5871 2023-03-15 08:55:02.000000 ccxt-3.0.9/ccxt/pro/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    26372 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/alpaca.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34257 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/ascendex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1081 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bequant.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    76677 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/binance.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      724 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/binancecoinm.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2016 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/binanceus.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      721 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/binanceusdm.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      914 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitcoincom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24527 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitfinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41514 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitfinex2.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    44288 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitget.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24228 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitmart.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    54876 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitmex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12408 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitopro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16064 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitrue.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20571 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitstamp.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    36334 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bittrex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    25674 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bitvavo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    30828 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/btcex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    60327 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/bybit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    44454 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/cex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1121 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/coinbaseprime.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    28811 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/coinbasepro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41088 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/coinex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22695 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/cryptocom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21858 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/currencycom.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33685 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/deribit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24171 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/exmo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41655 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/gate.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      391 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/gateio.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24893 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/gemini.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14957 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/hitbtc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21497 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/hollaex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    85197 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/huobi.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22414 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/huobijp.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      400 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/huobipro.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27696 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/idex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10899 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/independentreserve.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    44017 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/kraken.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33880 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/kucoin.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27539 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/kucoinfutures.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12026 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/luno.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    44669 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/mexc.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22450 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/ndax.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    29967 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/okcoin.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      382 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/okex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35390 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/okx.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41618 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/phemex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11937 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/ripio.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     9327 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/upbit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    29511 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/wazirx.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33983 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/whitebit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24508 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/woo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21298 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/pro/zb.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    66526 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/probit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    47033 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/ripio.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.856023 ccxt-3.0.9/ccxt/static_dependencies/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       30 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/__init__.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.860023 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      594 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18461 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/_version.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1886 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/curves.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6942 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/der.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    11336 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/ecdsa.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5517 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/ellipticcurve.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    14201 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/keys.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13468 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/numbertheory.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2572 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/rfc6979.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10037 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/ecdsa/util.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.864024 ccxt-3.0.9/ccxt/static_dependencies/keccak/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       45 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/keccak/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6934 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/static_dependencies/keccak/keccak.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   114873 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/stex.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.872025 ccxt-3.0.9/ccxt/test/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      362 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/test/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      864 2023-03-15 08:40:50.000000 ccxt-3.0.9/ccxt/test/test_account.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24990 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/test/test_async.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1177 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/test/test_calculate_fee.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7625 2023-03-15 08:40:48.000000 ccxt-3.0.9/ccxt/test/test_crypto.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20468 2023-03-15 08:40:45.000000 ccxt-3.0.9/ccxt/test/test_decimal_to_precision.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1402 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/test/test_deep_extend.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3592 2023-03-15 08:40:45.000000 ccxt-3.0.9/ccxt/test/test_exchange_datetime_functions.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1247 2023-03-15 08:40:50.000000 ccxt-3.0.9/ccxt/test/test_leverage_tier.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1271 2023-03-15 08:40:50.000000 ccxt-3.0.9/ccxt/test/test_margin_modification.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4049 2023-03-15 08:40:49.000000 ccxt-3.0.9/ccxt/test/test_market.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1468 2023-03-15 08:40:50.000000 ccxt-3.0.9/ccxt/test/test_ohlcv.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2216 2023-03-15 08:40:49.000000 ccxt-3.0.9/ccxt/test/test_order.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      821 2023-03-15 08:40:50.000000 ccxt-3.0.9/ccxt/test/test_position.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22795 2023-03-15 08:40:51.000000 ccxt-3.0.9/ccxt/test/test_sync.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3123 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/test/test_throttle.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3237 2023-03-15 08:40:49.000000 ccxt-3.0.9/ccxt/test/test_trade.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1434 2023-03-15 08:40:50.000000 ccxt-3.0.9/ccxt/test/test_transaction.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    42092 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/tidex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    64907 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/timex.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   117241 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/tokocrypto.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    72876 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/upbit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   102978 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/wavesexchange.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    34380 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/wazirx.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    91446 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/whitebit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    92734 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/woo.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    50494 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/yobit.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    27683 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/zaif.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)   183189 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/zb.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    72709 2023-03-15 08:33:15.000000 ccxt-3.0.9/ccxt/zonda.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2023-03-15 08:55:18.716009 ccxt-3.0.9/ccxt.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)   114885 2023-03-15 08:55:18.000000 ccxt-3.0.9/ccxt.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8089 2023-03-15 08:55:18.000000 ccxt-3.0.9/ccxt.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2023-03-15 08:55:18.000000 ccxt-3.0.9/ccxt.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      265 2023-03-15 08:55:18.000000 ccxt-3.0.9/ccxt.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        5 2023-03-15 08:55:18.000000 ccxt-3.0.9/ccxt.egg-info/top_level.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8050 2023-03-15 08:55:03.000000 ccxt-3.0.9/package.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)      205 2023-03-15 08:55:18.880025 ccxt-3.0.9/setup.cfg
+-rwxrwxr-x   0 travis    (2000) travis    (2000)     3130 2023-03-15 08:33:15.000000 ccxt-3.0.9/setup.py
```

### Comparing `ccxt-3.0.8/LICENSE.txt` & `ccxt-3.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/PKG-INFO` & `ccxt-3.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ccxt
-Version: 3.0.8
+Version: 3.0.9
 Summary: A JavaScript / Python / PHP cryptocurrency trading library with support for 130+ exchanges
 Home-page: https://ccxt.com
 Author: Igor Kroitor
 Author-email: igor.kroitor@gmail.com
 License: MIT
 Project-URL: Homepage, https://ccxt.com
 Project-URL: Documentation, https://docs.ccxt.com/en/latest/manual.html
@@ -223,21 +223,21 @@
         console.log(version, Object.keys(exchanges));
         ```
         
         ### JavaScript (for use with the `<script>` tag):
         
         All-in-one browser bundle (dependencies included), served from a CDN of your choice:
         
-        * jsDelivr: https://cdn.jsdelivr.net/npm/ccxt@3.0.8/dist/ccxt.browser.js
-        * unpkg: https://unpkg.com/ccxt@3.0.8/dist/ccxt.browser.js
+        * jsDelivr: https://cdn.jsdelivr.net/npm/ccxt@3.0.9/dist/ccxt.browser.js
+        * unpkg: https://unpkg.com/ccxt@3.0.9/dist/ccxt.browser.js
         
         CDNs are not updated in real-time and may have delays. Defaulting to the most recent version without specifying the version number is not recommended. Please, keep in mind that we are not responsible for the correct operation of those CDN servers.
         
         ```HTML
-        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/ccxt@3.0.8/dist/ccxt.browser.js"></script>
+        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/ccxt@3.0.9/dist/ccxt.browser.js"></script>
         ```
         
         Creates a global `ccxt` object:
         
         ```JavaScript
         console.log (ccxt.exchanges) // print all available exchanges
         ```
```

### Comparing `ccxt-3.0.8/README.rst` & `ccxt-3.0.9/README.rst`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/__init__.py` & `ccxt-3.0.9/ccxt/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 
 # ----------------------------------------------------------------------------
 
-__version__ = '3.0.8'
+__version__ = '3.0.9'
 
 # ----------------------------------------------------------------------------
 
 from ccxt.base.exchange import Exchange                     # noqa: F401
 from ccxt.base.precise import Precise                       # noqa: F401
 
 from ccxt.base.decimal_to_precision import decimal_to_precision  # noqa: F401
```

### Comparing `ccxt-3.0.8/ccxt/ace.py` & `ccxt-3.0.9/ccxt/ace.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/alpaca.py` & `ccxt-3.0.9/ccxt/alpaca.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/ascendex.py` & `ccxt-3.0.9/ccxt/ascendex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/__init__.py` & `ccxt-3.0.9/ccxt/async_support/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 
 """CCXT: CryptoCurrency eXchange Trading Library (Async)"""
 
 # -----------------------------------------------------------------------------
 
-__version__ = '3.0.8'
+__version__ = '3.0.9'
 
 # -----------------------------------------------------------------------------
 
 from ccxt.async_support.base.exchange import Exchange                   # noqa: F401
 
 from ccxt.base.decimal_to_precision import decimal_to_precision  # noqa: F401
 from ccxt.base.decimal_to_precision import TRUNCATE              # noqa: F401
```

### Comparing `ccxt-3.0.8/ccxt/async_support/ace.py` & `ccxt-3.0.9/ccxt/async_support/ace.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/alpaca.py` & `ccxt-3.0.9/ccxt/async_support/alpaca.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/ascendex.py` & `ccxt-3.0.9/ccxt/async_support/ascendex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/exchange.py` & `ccxt-3.0.9/ccxt/async_support/base/exchange.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # -*- coding: utf-8 -*-
 
 # -----------------------------------------------------------------------------
 
-__version__ = '3.0.8'
+__version__ = '3.0.9'
 
 # -----------------------------------------------------------------------------
 
 import asyncio
 import concurrent.futures
 import socket
 import certifi
```

### Comparing `ccxt-3.0.8/ccxt/async_support/base/throttler.py` & `ccxt-3.0.9/ccxt/async_support/base/throttler.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/__init__.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/__init__.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/aiohttp_client.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/aiohttp_client.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/cache.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/cache.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/client.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/client.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/fast_client.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/fast_client.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/functions.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/functions.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/order_book.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/order_book.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/base/ws/order_book_side.py` & `ccxt-3.0.9/ccxt/async_support/base/ws/order_book_side.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bequant.py` & `ccxt-3.0.9/ccxt/async_support/bequant.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bigone.py` & `ccxt-3.0.9/ccxt/async_support/bigone.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/binance.py` & `ccxt-3.0.9/ccxt/async_support/binance.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/binancecoinm.py` & `ccxt-3.0.9/ccxt/async_support/binancecoinm.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/binanceus.py` & `ccxt-3.0.9/ccxt/async_support/binanceus.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/binanceusdm.py` & `ccxt-3.0.9/ccxt/async_support/binanceusdm.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bit2c.py` & `ccxt-3.0.9/ccxt/async_support/bit2c.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitbank.py` & `ccxt-3.0.9/ccxt/async_support/bitbank.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitbns.py` & `ccxt-3.0.9/ccxt/async_support/bitbns.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitfinex.py` & `ccxt-3.0.9/ccxt/async_support/bitfinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitfinex2.py` & `ccxt-3.0.9/ccxt/async_support/bitfinex2.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitflyer.py` & `ccxt-3.0.9/ccxt/async_support/bitflyer.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitforex.py` & `ccxt-3.0.9/ccxt/async_support/bitforex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitget.py` & `ccxt-3.0.9/ccxt/async_support/bitget.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bithumb.py` & `ccxt-3.0.9/ccxt/async_support/bithumb.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitmart.py` & `ccxt-3.0.9/ccxt/async_support/bitmart.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitmex.py` & `ccxt-3.0.9/ccxt/async_support/bitmex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitopro.py` & `ccxt-3.0.9/ccxt/async_support/bitopro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitpanda.py` & `ccxt-3.0.9/ccxt/async_support/bitpanda.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitrue.py` & `ccxt-3.0.9/ccxt/async_support/bitrue.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitso.py` & `ccxt-3.0.9/ccxt/async_support/bitso.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitstamp.py` & `ccxt-3.0.9/ccxt/async_support/bitstamp.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitstamp1.py` & `ccxt-3.0.9/ccxt/async_support/bitstamp1.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bittrex.py` & `ccxt-3.0.9/ccxt/async_support/bittrex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bitvavo.py` & `ccxt-3.0.9/ccxt/async_support/bitvavo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bkex.py` & `ccxt-3.0.9/ccxt/async_support/bkex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bl3p.py` & `ccxt-3.0.9/ccxt/async_support/bl3p.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/blockchaincom.py` & `ccxt-3.0.9/ccxt/async_support/blockchaincom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/btcalpha.py` & `ccxt-3.0.9/ccxt/async_support/btcalpha.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/btcbox.py` & `ccxt-3.0.9/ccxt/async_support/btcbox.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/btcex.py` & `ccxt-3.0.9/ccxt/async_support/btcex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/btcmarkets.py` & `ccxt-3.0.9/ccxt/async_support/btcmarkets.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/btctradeua.py` & `ccxt-3.0.9/ccxt/async_support/btctradeua.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/btcturk.py` & `ccxt-3.0.9/ccxt/async_support/btcturk.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/buda.py` & `ccxt-3.0.9/ccxt/async_support/buda.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/bybit.py` & `ccxt-3.0.9/ccxt/async_support/bybit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/cex.py` & `ccxt-3.0.9/ccxt/async_support/cex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinbase.py` & `ccxt-3.0.9/ccxt/async_support/coinbase.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinbaseprime.py` & `ccxt-3.0.9/ccxt/async_support/coinbaseprime.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinbasepro.py` & `ccxt-3.0.9/ccxt/async_support/coinbasepro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coincheck.py` & `ccxt-3.0.9/ccxt/async_support/coincheck.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinex.py` & `ccxt-3.0.9/ccxt/async_support/coinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinfalcon.py` & `ccxt-3.0.9/ccxt/async_support/coinfalcon.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinmate.py` & `ccxt-3.0.9/ccxt/async_support/coinmate.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinone.py` & `ccxt-3.0.9/ccxt/async_support/coinone.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/coinspot.py` & `ccxt-3.0.9/ccxt/async_support/coinspot.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/cryptocom.py` & `ccxt-3.0.9/ccxt/async_support/cryptocom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/currencycom.py` & `ccxt-3.0.9/ccxt/async_support/currencycom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/delta.py` & `ccxt-3.0.9/ccxt/async_support/delta.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/deribit.py` & `ccxt-3.0.9/ccxt/async_support/deribit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/digifinex.py` & `ccxt-3.0.9/ccxt/async_support/digifinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/exmo.py` & `ccxt-3.0.9/ccxt/async_support/exmo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/flowbtc.py` & `ccxt-3.0.9/ccxt/async_support/flowbtc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/fmfwio.py` & `ccxt-3.0.9/ccxt/async_support/fmfwio.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/gate.py` & `ccxt-3.0.9/ccxt/async_support/gate.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/gemini.py` & `ccxt-3.0.9/ccxt/async_support/gemini.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/hitbtc.py` & `ccxt-3.0.9/ccxt/async_support/hitbtc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/hitbtc3.py` & `ccxt-3.0.9/ccxt/async_support/hitbtc3.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/hollaex.py` & `ccxt-3.0.9/ccxt/async_support/hollaex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/huobi.py` & `ccxt-3.0.9/ccxt/async_support/huobi.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/huobijp.py` & `ccxt-3.0.9/ccxt/async_support/huobijp.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/huobipro.py` & `ccxt-3.0.9/ccxt/async_support/huobipro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/idex.py` & `ccxt-3.0.9/ccxt/async_support/idex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/independentreserve.py` & `ccxt-3.0.9/ccxt/async_support/independentreserve.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/indodax.py` & `ccxt-3.0.9/ccxt/async_support/indodax.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/itbit.py` & `ccxt-3.0.9/ccxt/async_support/itbit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/kraken.py` & `ccxt-3.0.9/ccxt/async_support/kraken.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/krakenfutures.py` & `ccxt-3.0.9/ccxt/async_support/krakenfutures.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/kucoin.py` & `ccxt-3.0.9/ccxt/async_support/kucoin.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/kucoinfutures.py` & `ccxt-3.0.9/ccxt/async_support/kucoinfutures.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/kuna.py` & `ccxt-3.0.9/ccxt/async_support/kuna.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/latoken.py` & `ccxt-3.0.9/ccxt/async_support/latoken.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/lbank.py` & `ccxt-3.0.9/ccxt/async_support/lbank.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/lbank2.py` & `ccxt-3.0.9/ccxt/async_support/lbank2.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/luno.py` & `ccxt-3.0.9/ccxt/async_support/luno.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/lykke.py` & `ccxt-3.0.9/ccxt/async_support/lykke.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/mercado.py` & `ccxt-3.0.9/ccxt/async_support/mercado.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/mexc.py` & `ccxt-3.0.9/ccxt/async_support/mexc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/mexc3.py` & `ccxt-3.0.9/ccxt/async_support/mexc3.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/ndax.py` & `ccxt-3.0.9/ccxt/async_support/ndax.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/novadax.py` & `ccxt-3.0.9/ccxt/async_support/novadax.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/oceanex.py` & `ccxt-3.0.9/ccxt/async_support/oceanex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/okcoin.py` & `ccxt-3.0.9/ccxt/async_support/okcoin.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/okx.py` & `ccxt-3.0.9/ccxt/async_support/okx.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/paymium.py` & `ccxt-3.0.9/ccxt/async_support/paymium.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/phemex.py` & `ccxt-3.0.9/ccxt/async_support/phemex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/poloniex.py` & `ccxt-3.0.9/ccxt/async_support/poloniex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/poloniexfutures.py` & `ccxt-3.0.9/ccxt/async_support/poloniexfutures.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/probit.py` & `ccxt-3.0.9/ccxt/async_support/probit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/ripio.py` & `ccxt-3.0.9/ccxt/async_support/ripio.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/stex.py` & `ccxt-3.0.9/ccxt/async_support/stex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/tidex.py` & `ccxt-3.0.9/ccxt/async_support/tidex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/timex.py` & `ccxt-3.0.9/ccxt/async_support/timex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/tokocrypto.py` & `ccxt-3.0.9/ccxt/async_support/tokocrypto.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/upbit.py` & `ccxt-3.0.9/ccxt/async_support/upbit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/wavesexchange.py` & `ccxt-3.0.9/ccxt/async_support/wavesexchange.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/wazirx.py` & `ccxt-3.0.9/ccxt/async_support/wazirx.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/whitebit.py` & `ccxt-3.0.9/ccxt/async_support/whitebit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/woo.py` & `ccxt-3.0.9/ccxt/async_support/woo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/yobit.py` & `ccxt-3.0.9/ccxt/async_support/yobit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/zaif.py` & `ccxt-3.0.9/ccxt/async_support/zaif.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/zb.py` & `ccxt-3.0.9/ccxt/async_support/zb.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/async_support/zonda.py` & `ccxt-3.0.9/ccxt/async_support/zonda.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/base/__init__.py` & `ccxt-3.0.9/ccxt/base/__init__.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/base/decimal_to_precision.py` & `ccxt-3.0.9/ccxt/base/decimal_to_precision.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/base/errors.py` & `ccxt-3.0.9/ccxt/base/errors.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/base/exchange.py` & `ccxt-3.0.9/ccxt/base/exchange.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 
 """Base exchange class"""
 
 # -----------------------------------------------------------------------------
 
-__version__ = '3.0.8'
+__version__ = '3.0.9'
 
 # -----------------------------------------------------------------------------
 
 from ccxt.base.errors import ExchangeError
 from ccxt.base.errors import NetworkError
 from ccxt.base.errors import NotSupported
 from ccxt.base.errors import AuthenticationError
```

### Comparing `ccxt-3.0.8/ccxt/base/precise.py` & `ccxt-3.0.9/ccxt/base/precise.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bequant.py` & `ccxt-3.0.9/ccxt/bequant.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bigone.py` & `ccxt-3.0.9/ccxt/bigone.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/binance.py` & `ccxt-3.0.9/ccxt/binance.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/binancecoinm.py` & `ccxt-3.0.9/ccxt/binancecoinm.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/binanceus.py` & `ccxt-3.0.9/ccxt/binanceus.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/binanceusdm.py` & `ccxt-3.0.9/ccxt/binanceusdm.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bit2c.py` & `ccxt-3.0.9/ccxt/bit2c.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitbank.py` & `ccxt-3.0.9/ccxt/bitbank.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitbns.py` & `ccxt-3.0.9/ccxt/bitbns.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitfinex.py` & `ccxt-3.0.9/ccxt/bitfinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitfinex2.py` & `ccxt-3.0.9/ccxt/bitfinex2.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitflyer.py` & `ccxt-3.0.9/ccxt/bitflyer.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitforex.py` & `ccxt-3.0.9/ccxt/bitforex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitget.py` & `ccxt-3.0.9/ccxt/bitget.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bithumb.py` & `ccxt-3.0.9/ccxt/bithumb.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitmart.py` & `ccxt-3.0.9/ccxt/bitmart.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitmex.py` & `ccxt-3.0.9/ccxt/bitmex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitopro.py` & `ccxt-3.0.9/ccxt/bitopro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitpanda.py` & `ccxt-3.0.9/ccxt/bitpanda.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitrue.py` & `ccxt-3.0.9/ccxt/bitrue.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitso.py` & `ccxt-3.0.9/ccxt/bitso.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitstamp.py` & `ccxt-3.0.9/ccxt/bitstamp.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitstamp1.py` & `ccxt-3.0.9/ccxt/bitstamp1.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bittrex.py` & `ccxt-3.0.9/ccxt/bittrex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bitvavo.py` & `ccxt-3.0.9/ccxt/bitvavo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bkex.py` & `ccxt-3.0.9/ccxt/bkex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bl3p.py` & `ccxt-3.0.9/ccxt/bl3p.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/blockchaincom.py` & `ccxt-3.0.9/ccxt/blockchaincom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/btcalpha.py` & `ccxt-3.0.9/ccxt/btcalpha.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/btcbox.py` & `ccxt-3.0.9/ccxt/btcbox.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/btcex.py` & `ccxt-3.0.9/ccxt/btcex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/btcmarkets.py` & `ccxt-3.0.9/ccxt/btcmarkets.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/btctradeua.py` & `ccxt-3.0.9/ccxt/btctradeua.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/btcturk.py` & `ccxt-3.0.9/ccxt/btcturk.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/buda.py` & `ccxt-3.0.9/ccxt/buda.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/bybit.py` & `ccxt-3.0.9/ccxt/bybit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/cex.py` & `ccxt-3.0.9/ccxt/cex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinbase.py` & `ccxt-3.0.9/ccxt/coinbase.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinbaseprime.py` & `ccxt-3.0.9/ccxt/coinbaseprime.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinbasepro.py` & `ccxt-3.0.9/ccxt/coinbasepro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coincheck.py` & `ccxt-3.0.9/ccxt/coincheck.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinex.py` & `ccxt-3.0.9/ccxt/coinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinfalcon.py` & `ccxt-3.0.9/ccxt/coinfalcon.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinmate.py` & `ccxt-3.0.9/ccxt/coinmate.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinone.py` & `ccxt-3.0.9/ccxt/coinone.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/coinspot.py` & `ccxt-3.0.9/ccxt/coinspot.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/cryptocom.py` & `ccxt-3.0.9/ccxt/cryptocom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/currencycom.py` & `ccxt-3.0.9/ccxt/currencycom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/delta.py` & `ccxt-3.0.9/ccxt/delta.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/deribit.py` & `ccxt-3.0.9/ccxt/deribit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/digifinex.py` & `ccxt-3.0.9/ccxt/digifinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/exmo.py` & `ccxt-3.0.9/ccxt/exmo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/flowbtc.py` & `ccxt-3.0.9/ccxt/flowbtc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/fmfwio.py` & `ccxt-3.0.9/ccxt/fmfwio.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/gate.py` & `ccxt-3.0.9/ccxt/gate.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/gemini.py` & `ccxt-3.0.9/ccxt/gemini.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/hitbtc.py` & `ccxt-3.0.9/ccxt/hitbtc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/hitbtc3.py` & `ccxt-3.0.9/ccxt/hitbtc3.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/hollaex.py` & `ccxt-3.0.9/ccxt/hollaex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/huobi.py` & `ccxt-3.0.9/ccxt/huobi.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/huobijp.py` & `ccxt-3.0.9/ccxt/huobijp.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/huobipro.py` & `ccxt-3.0.9/ccxt/huobipro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/idex.py` & `ccxt-3.0.9/ccxt/idex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/independentreserve.py` & `ccxt-3.0.9/ccxt/independentreserve.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/indodax.py` & `ccxt-3.0.9/ccxt/indodax.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/itbit.py` & `ccxt-3.0.9/ccxt/itbit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/kraken.py` & `ccxt-3.0.9/ccxt/kraken.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/krakenfutures.py` & `ccxt-3.0.9/ccxt/krakenfutures.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/kucoin.py` & `ccxt-3.0.9/ccxt/kucoin.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/kucoinfutures.py` & `ccxt-3.0.9/ccxt/kucoinfutures.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/kuna.py` & `ccxt-3.0.9/ccxt/kuna.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/latoken.py` & `ccxt-3.0.9/ccxt/latoken.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/lbank.py` & `ccxt-3.0.9/ccxt/lbank.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/lbank2.py` & `ccxt-3.0.9/ccxt/lbank2.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/luno.py` & `ccxt-3.0.9/ccxt/luno.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/lykke.py` & `ccxt-3.0.9/ccxt/lykke.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/mercado.py` & `ccxt-3.0.9/ccxt/mercado.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/mexc.py` & `ccxt-3.0.9/ccxt/mexc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/mexc3.py` & `ccxt-3.0.9/ccxt/mexc3.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/ndax.py` & `ccxt-3.0.9/ccxt/ndax.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/novadax.py` & `ccxt-3.0.9/ccxt/novadax.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/oceanex.py` & `ccxt-3.0.9/ccxt/oceanex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/okcoin.py` & `ccxt-3.0.9/ccxt/okcoin.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/okx.py` & `ccxt-3.0.9/ccxt/okx.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/paymium.py` & `ccxt-3.0.9/ccxt/paymium.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/phemex.py` & `ccxt-3.0.9/ccxt/phemex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/poloniex.py` & `ccxt-3.0.9/ccxt/poloniex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/poloniexfutures.py` & `ccxt-3.0.9/ccxt/poloniexfutures.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/__init__.py` & `ccxt-3.0.9/ccxt/pro/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # -*- coding: utf-8 -*-
 
 """CCXT: CryptoCurrency eXchange Trading Library (Async)"""
 
 # ----------------------------------------------------------------------------
 
-__version__ = '3.0.8'
+__version__ = '3.0.9'
 
 # ----------------------------------------------------------------------------
 
 # CCXT Pro exchanges (now this is mainly used for importing exchanges in WS tests)
 
 from ccxt.pro.alpaca import alpaca                                        # noqa: F401
 from ccxt.pro.ascendex import ascendex                                    # noqa: F401
```

### Comparing `ccxt-3.0.8/ccxt/pro/alpaca.py` & `ccxt-3.0.9/ccxt/pro/alpaca.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/ascendex.py` & `ccxt-3.0.9/ccxt/pro/ascendex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bequant.py` & `ccxt-3.0.9/ccxt/pro/bequant.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/binance.py` & `ccxt-3.0.9/ccxt/pro/binance.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/binancecoinm.py` & `ccxt-3.0.9/ccxt/pro/binancecoinm.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/binanceus.py` & `ccxt-3.0.9/ccxt/pro/binanceus.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/binanceusdm.py` & `ccxt-3.0.9/ccxt/pro/binanceusdm.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitcoincom.py` & `ccxt-3.0.9/ccxt/pro/bitcoincom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitfinex.py` & `ccxt-3.0.9/ccxt/pro/bitfinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitfinex2.py` & `ccxt-3.0.9/ccxt/pro/bitfinex2.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitget.py` & `ccxt-3.0.9/ccxt/pro/bitget.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitmart.py` & `ccxt-3.0.9/ccxt/pro/bitmart.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitmex.py` & `ccxt-3.0.9/ccxt/pro/bitmex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitopro.py` & `ccxt-3.0.9/ccxt/pro/bitopro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitrue.py` & `ccxt-3.0.9/ccxt/pro/bitrue.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitstamp.py` & `ccxt-3.0.9/ccxt/pro/bitstamp.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bittrex.py` & `ccxt-3.0.9/ccxt/pro/bittrex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bitvavo.py` & `ccxt-3.0.9/ccxt/pro/bitvavo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/btcex.py` & `ccxt-3.0.9/ccxt/pro/btcex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/bybit.py` & `ccxt-3.0.9/ccxt/pro/bybit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/cex.py` & `ccxt-3.0.9/ccxt/pro/cex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/coinbaseprime.py` & `ccxt-3.0.9/ccxt/pro/coinbaseprime.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/coinbasepro.py` & `ccxt-3.0.9/ccxt/pro/coinbasepro.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/coinex.py` & `ccxt-3.0.9/ccxt/pro/coinex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/cryptocom.py` & `ccxt-3.0.9/ccxt/pro/cryptocom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/currencycom.py` & `ccxt-3.0.9/ccxt/pro/currencycom.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/deribit.py` & `ccxt-3.0.9/ccxt/pro/deribit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/exmo.py` & `ccxt-3.0.9/ccxt/pro/exmo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/gate.py` & `ccxt-3.0.9/ccxt/pro/gate.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/gemini.py` & `ccxt-3.0.9/ccxt/pro/gemini.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/hitbtc.py` & `ccxt-3.0.9/ccxt/pro/hitbtc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/hollaex.py` & `ccxt-3.0.9/ccxt/pro/hollaex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/huobi.py` & `ccxt-3.0.9/ccxt/pro/huobi.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/huobijp.py` & `ccxt-3.0.9/ccxt/pro/huobijp.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/idex.py` & `ccxt-3.0.9/ccxt/pro/idex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/independentreserve.py` & `ccxt-3.0.9/ccxt/pro/independentreserve.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/kraken.py` & `ccxt-3.0.9/ccxt/pro/kraken.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/kucoin.py` & `ccxt-3.0.9/ccxt/pro/kucoin.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/kucoinfutures.py` & `ccxt-3.0.9/ccxt/pro/kucoinfutures.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/luno.py` & `ccxt-3.0.9/ccxt/pro/luno.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/mexc.py` & `ccxt-3.0.9/ccxt/pro/mexc.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/ndax.py` & `ccxt-3.0.9/ccxt/pro/ndax.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/okcoin.py` & `ccxt-3.0.9/ccxt/pro/okcoin.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/okx.py` & `ccxt-3.0.9/ccxt/pro/okx.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/phemex.py` & `ccxt-3.0.9/ccxt/pro/phemex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/ripio.py` & `ccxt-3.0.9/ccxt/pro/ripio.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/upbit.py` & `ccxt-3.0.9/ccxt/pro/upbit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/wazirx.py` & `ccxt-3.0.9/ccxt/pro/wazirx.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/whitebit.py` & `ccxt-3.0.9/ccxt/pro/whitebit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/woo.py` & `ccxt-3.0.9/ccxt/pro/woo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/pro/zb.py` & `ccxt-3.0.9/ccxt/pro/zb.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/probit.py` & `ccxt-3.0.9/ccxt/probit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/ripio.py` & `ccxt-3.0.9/ccxt/ripio.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/__init__.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/__init__.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/_version.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/_version.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/curves.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/curves.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/der.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/der.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/ecdsa.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/ecdsa.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/ellipticcurve.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/ellipticcurve.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/keys.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/keys.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/numbertheory.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/numbertheory.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/rfc6979.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/rfc6979.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/ecdsa/util.py` & `ccxt-3.0.9/ccxt/static_dependencies/ecdsa/util.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/static_dependencies/keccak/keccak.py` & `ccxt-3.0.9/ccxt/static_dependencies/keccak/keccak.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/stex.py` & `ccxt-3.0.9/ccxt/stex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_account.py` & `ccxt-3.0.9/ccxt/test/test_account.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_async.py` & `ccxt-3.0.9/ccxt/test/test_async.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_calculate_fee.py` & `ccxt-3.0.9/ccxt/test/test_calculate_fee.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_crypto.py` & `ccxt-3.0.9/ccxt/test/test_crypto.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_decimal_to_precision.py` & `ccxt-3.0.9/ccxt/test/test_decimal_to_precision.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_deep_extend.py` & `ccxt-3.0.9/ccxt/test/test_deep_extend.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_exchange_datetime_functions.py` & `ccxt-3.0.9/ccxt/test/test_exchange_datetime_functions.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_leverage_tier.py` & `ccxt-3.0.9/ccxt/test/test_leverage_tier.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_margin_modification.py` & `ccxt-3.0.9/ccxt/test/test_margin_modification.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_market.py` & `ccxt-3.0.9/ccxt/test/test_market.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_ohlcv.py` & `ccxt-3.0.9/ccxt/test/test_ohlcv.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_order.py` & `ccxt-3.0.9/ccxt/test/test_order.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_position.py` & `ccxt-3.0.9/ccxt/test/test_position.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_sync.py` & `ccxt-3.0.9/ccxt/test/test_sync.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_throttle.py` & `ccxt-3.0.9/ccxt/test/test_throttle.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_trade.py` & `ccxt-3.0.9/ccxt/test/test_trade.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/test/test_transaction.py` & `ccxt-3.0.9/ccxt/test/test_transaction.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/tidex.py` & `ccxt-3.0.9/ccxt/tidex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/timex.py` & `ccxt-3.0.9/ccxt/timex.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/tokocrypto.py` & `ccxt-3.0.9/ccxt/tokocrypto.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/upbit.py` & `ccxt-3.0.9/ccxt/upbit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/wavesexchange.py` & `ccxt-3.0.9/ccxt/wavesexchange.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/wazirx.py` & `ccxt-3.0.9/ccxt/wazirx.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/whitebit.py` & `ccxt-3.0.9/ccxt/whitebit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/woo.py` & `ccxt-3.0.9/ccxt/woo.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/yobit.py` & `ccxt-3.0.9/ccxt/yobit.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/zaif.py` & `ccxt-3.0.9/ccxt/zaif.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/zb.py` & `ccxt-3.0.9/ccxt/zb.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt/zonda.py` & `ccxt-3.0.9/ccxt/zonda.py`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/ccxt.egg-info/PKG-INFO` & `ccxt-3.0.9/ccxt.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ccxt
-Version: 3.0.8
+Version: 3.0.9
 Summary: A JavaScript / Python / PHP cryptocurrency trading library with support for 130+ exchanges
 Home-page: https://ccxt.com
 Author: Igor Kroitor
 Author-email: igor.kroitor@gmail.com
 License: MIT
 Project-URL: Homepage, https://ccxt.com
 Project-URL: Documentation, https://docs.ccxt.com/en/latest/manual.html
@@ -223,21 +223,21 @@
         console.log(version, Object.keys(exchanges));
         ```
         
         ### JavaScript (for use with the `<script>` tag):
         
         All-in-one browser bundle (dependencies included), served from a CDN of your choice:
         
-        * jsDelivr: https://cdn.jsdelivr.net/npm/ccxt@3.0.8/dist/ccxt.browser.js
-        * unpkg: https://unpkg.com/ccxt@3.0.8/dist/ccxt.browser.js
+        * jsDelivr: https://cdn.jsdelivr.net/npm/ccxt@3.0.9/dist/ccxt.browser.js
+        * unpkg: https://unpkg.com/ccxt@3.0.9/dist/ccxt.browser.js
         
         CDNs are not updated in real-time and may have delays. Defaulting to the most recent version without specifying the version number is not recommended. Please, keep in mind that we are not responsible for the correct operation of those CDN servers.
         
         ```HTML
-        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/ccxt@3.0.8/dist/ccxt.browser.js"></script>
+        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/ccxt@3.0.9/dist/ccxt.browser.js"></script>
         ```
         
         Creates a global `ccxt` object:
         
         ```JavaScript
         console.log (ccxt.exchanges) // print all available exchanges
         ```
```

### Comparing `ccxt-3.0.8/ccxt.egg-info/SOURCES.txt` & `ccxt-3.0.9/ccxt.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ccxt-3.0.8/package.json` & `ccxt-3.0.9/package.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9760251322751323%*

 * *Differences: {"'scripts'": "{'emitTypes': 'node build/emitTypes.js'}", "'version'": "'3.0.9'"}*

```diff
@@ -157,15 +157,15 @@
         "copy-python-files": "npm run copy-python-package && npm run copy-python-license && npm run copy-python-keys && npm run copy-python-readme",
         "copy-python-keys": "node build/copy keys.json python/keys.json",
         "copy-python-license": "node build/copy LICENSE.txt python/LICENSE.txt",
         "copy-python-package": "node build/copy package.json python/package.json",
         "copy-python-readme": "node build/copy README.md python/README.md",
         "dev-force-transpile": "npm run fast-force-transpileRest && npm run fast-force-transpileWs",
         "docker": "docker-compose run --rm ccxt",
-        "emitTypes": "(tsc --emitDeclarationOnly --declaration > /dev/null 2>&1 || true)",
+        "emitTypes": "node build/emitTypes.js",
         "export-docs": "python3 build/export-docs.py",
         "export-exchanges": "tsc && node build/export-exchanges",
         "fast-force-transpileRest": "node build/transpile.js --multiprocess",
         "fast-force-transpileWs": "node build/transpileWS.js --multiprocess",
         "fast-test": "node run-tests --js",
         "fast-test-ws": "node run-tests-ws --js",
         "fixTSBug": "node build/fixTSBug",
@@ -211,9 +211,9 @@
         "update-badges": "node build/update-badges",
         "update-links": "node build/update-links",
         "vss": "node build/vss"
     },
     "type": "module",
     "types": "./js/ccxt.d.ts",
     "unpkg": "dist/ccxt.browser.js",
-    "version": "3.0.8"
+    "version": "3.0.9"
 }
```

### Comparing `ccxt-3.0.8/setup.py` & `ccxt-3.0.9/setup.py`

 * *Files identical despite different names*

