# Comparing `tmp/trading_strategy-0.9.0.tar.gz` & `tmp/trading_strategy-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "trading_strategy-0.9.0.tar", max compression
+gzip compressed data, was "trading_strategy-0.9.1.tar", max compression
```

## Comparing `trading_strategy-0.9.0.tar` & `trading_strategy-0.9.1.tar`

### file list

```diff
@@ -1,359 +1,372 @@
--rw-r--r--   0        0        0      678 2022-09-17 18:31:15.771007 trading_strategy-0.9.0/LICENSE.txt
--rw-r--r--   0        0        0     3466 2022-11-27 21:12:23.603365 trading_strategy-0.9.0/README.md
--rw-r--r--   0        0        0     1709 2022-12-08 18:14:47.183408 trading_strategy-0.9.0/pyproject.toml
--rw-r--r--   0        0        0       22 2022-09-17 18:31:15.774650 trading_strategy-0.9.0/tradingstrategy/__init__.py
--rw-r--r--   0        0        0       48 2022-09-17 18:31:15.774796 trading_strategy-0.9.0/tradingstrategy/analysis/__init__.py
--rw-r--r--   0        0        0     9034 2022-09-17 18:31:15.774905 trading_strategy-0.9.0/tradingstrategy/analysis/portfolioanalyzer.py
--rw-r--r--   0        0        0     2660 2022-09-17 18:31:15.774982 trading_strategy-0.9.0/tradingstrategy/analysis/profitdistribution.py
--rw-r--r--   0        0        0    18671 2022-09-17 18:31:15.775103 trading_strategy-0.9.0/tradingstrategy/analysis/tradeanalyzer.py
--rw-r--r--   0        0        0      593 2022-09-17 18:31:15.775189 trading_strategy-0.9.0/tradingstrategy/analysis/tradehint.py
--rw-r--r--   0        0        0     1801 2022-09-19 08:44:04.949231 trading_strategy-0.9.0/tradingstrategy/caip.py
--rw-r--r--   0        0        0    18713 2022-12-08 18:11:18.366497 trading_strategy-0.9.0/tradingstrategy/candle.py
--rw-r--r--   0        0        0     7906 2022-09-17 18:31:15.775445 trading_strategy-0.9.0/tradingstrategy/chain.py
--rw-r--r--   0        0        0       82 2022-09-17 18:31:17.238364 trading_strategy-0.9.0/tradingstrategy/chains/.ci/kontinuum.json
--rw-r--r--   0        0        0       86 2022-09-17 18:31:17.190414 trading_strategy-0.9.0/tradingstrategy/chains/.git
--rw-r--r--   0        0        0      608 2022-09-17 18:31:17.238529 trading_strategy-0.9.0/tradingstrategy/chains/.github/ISSUE_TEMPLATE/add-new-chain---network-id.md
--rw-r--r--   0        0        0      122 2022-09-17 18:31:17.238589 trading_strategy-0.9.0/tradingstrategy/chains/.github/ISSUE_TEMPLATE/other.md
--rw-r--r--   0        0        0      139 2022-09-17 18:31:17.238646 trading_strategy-0.9.0/tradingstrategy/chains/.github/dependabot.yml
--rw-r--r--   0        0        0     1072 2022-09-17 18:31:17.238736 trading_strategy-0.9.0/tradingstrategy/chains/.github/workflows/build_and_deploy.yml
--rw-r--r--   0        0        0       62 2022-09-17 18:31:17.238786 trading_strategy-0.9.0/tradingstrategy/chains/.gitignore
--rw-r--r--   0        0        0     1057 2022-09-17 18:31:17.238847 trading_strategy-0.9.0/tradingstrategy/chains/LICENSE
--rw-r--r--   0        0        0     2539 2022-09-17 18:31:17.238924 trading_strategy-0.9.0/tradingstrategy/chains/README.md
--rw-r--r--   0        0        0      349 2022-09-17 18:31:17.239061 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/deprecated/eip155-218.json
--rw-r--r--   0        0        0      694 2022-09-17 18:31:17.239123 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1.json
--rw-r--r--   0        0        0      441 2022-09-17 18:31:17.239180 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-10.json
--rw-r--r--   0        0        0      784 2022-09-17 18:31:17.239240 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100.json
--rw-r--r--   0        0        0      483 2022-09-17 18:31:17.239295 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-10000.json
--rw-r--r--   0        0        0      369 2022-09-17 18:31:17.239359 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100000.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239417 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100001.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239470 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100002.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239522 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100003.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239570 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100004.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239623 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100005.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239675 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100006.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239722 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100007.json
--rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239771 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100008.json
--rw-r--r--   0        0        0      427 2022-09-17 18:31:17.239831 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-10001.json
--rw-r--r--   0        0        0      414 2022-09-17 18:31:17.239885 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1001.json
--rw-r--r--   0        0        0      350 2022-09-17 18:31:17.239943 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1007.json
--rw-r--r--   0        0        0      345 2022-09-17 18:31:17.239999 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-101.json
--rw-r--r--   0        0        0      339 2022-09-17 18:31:17.240052 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1010.json
--rw-r--r--   0        0        0      420 2022-09-17 18:31:17.240103 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-10101.json
--rw-r--r--   0        0        0      346 2022-09-17 18:31:17.240162 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1012.json
--rw-r--r--   0        0        0      363 2022-09-17 18:31:17.240212 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-102.json
--rw-r--r--   0        0        0      327 2022-09-17 18:31:17.240262 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1022.json
--rw-r--r--   0        0        0      337 2022-09-17 18:31:17.240316 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1023.json
--rw-r--r--   0        0        0      464 2022-09-17 18:31:17.240368 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1024.json
--rw-r--r--   0        0        0      485 2022-09-17 18:31:17.240429 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1028.json
--rw-r--r--   0        0        0      514 2022-09-17 18:31:17.240480 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-106.json
--rw-r--r--   0        0        0      415 2022-09-17 18:31:17.240533 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-108.json
--rw-r--r--   0        0        0      364 2022-09-17 18:31:17.240590 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-11.json
--rw-r--r--   0        0        0      375 2022-09-17 18:31:17.240646 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110.json
--rw-r--r--   0        0        0      368 2022-09-17 18:31:17.240692 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110000.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240747 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110001.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240799 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110002.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240851 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110003.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240899 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110004.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240947 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110005.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.241000 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110006.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.241057 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110007.json
--rw-r--r--   0        0        0      573 2022-09-17 18:31:17.241107 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110008.json
--rw-r--r--   0        0        0      395 2022-09-17 18:31:17.241158 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-111.json
--rw-r--r--   0        0        0      379 2022-09-17 18:31:17.241212 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1122334455.json
--rw-r--r--   0        0        0      300 2022-09-17 18:31:17.241269 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-11297108099.json
--rw-r--r--   0        0        0      299 2022-09-17 18:31:17.241324 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-11297108109.json
--rw-r--r--   0        0        0      431 2022-09-17 18:31:17.241378 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1139.json
--rw-r--r--   0        0        0      438 2022-09-17 18:31:17.241428 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1140.json
--rw-r--r--   0        0        0      343 2022-09-17 18:31:17.241482 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-12.json
--rw-r--r--   0        0        0      485 2022-09-17 18:31:17.241537 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1213.json
--rw-r--r--   0        0        0      313 2022-09-17 18:31:17.241591 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-122.json
--rw-r--r--   0        0        0      363 2022-09-17 18:31:17.241642 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-124.json
--rw-r--r--   0        0        0      373 2022-09-17 18:31:17.241696 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-127.json
--rw-r--r--   0        0        0      591 2022-09-17 18:31:17.241756 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-128.json
--rw-r--r--   0        0        0      313 2022-09-17 18:31:17.241809 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1284.json
--rw-r--r--   0        0        0      602 2022-09-17 18:31:17.241865 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1285.json
--rw-r--r--   0        0        0      266 2022-09-17 18:31:17.241925 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1286.json
--rw-r--r--   0        0        0      406 2022-09-17 18:31:17.241986 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1287.json
--rw-r--r--   0        0        0      361 2022-09-17 18:31:17.242065 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1288.json
--rw-r--r--   0        0        0      390 2022-09-17 18:31:17.242123 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-13.json
--rw-r--r--   0        0        0      531 2022-09-17 18:31:17.242176 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1313114.json
--rw-r--r--   0        0        0      341 2022-09-17 18:31:17.242237 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1313161554.json
--rw-r--r--   0        0        0      350 2022-09-17 18:31:17.242293 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1313161555.json
--rw-r--r--   0        0        0      350 2022-09-17 18:31:17.242340 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1313161556.json
--rw-r--r--   0        0        0      324 2022-09-17 18:31:17.242392 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1313500.json
--rw-r--r--   0        0        0      364 2022-09-17 18:31:17.242455 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-13371337.json
--rw-r--r--   0        0        0      778 2022-09-17 18:31:17.242527 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-137.json
--rw-r--r--   0        0        0      286 2022-09-17 18:31:17.242592 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-14.json
--rw-r--r--   0        0        0      313 2022-09-17 18:31:17.242658 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-142.json
--rw-r--r--   0        0        0      370 2022-09-17 18:31:17.242717 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-15.json
--rw-r--r--   0        0        0      355 2022-09-17 18:31:17.242772 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-16.json
--rw-r--r--   0        0        0      381 2022-09-17 18:31:17.242835 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-16000.json
--rw-r--r--   0        0        0      447 2022-09-17 18:31:17.242881 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-16001.json
--rw-r--r--   0        0        0      346 2022-09-17 18:31:17.242931 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1618.json
--rw-r--r--   0        0        0      436 2022-09-17 18:31:17.242986 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-162.json
--rw-r--r--   0        0        0      352 2022-09-17 18:31:17.243037 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1620.json
--rw-r--r--   0        0        0      362 2022-09-17 18:31:17.243098 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-163.json
--rw-r--r--   0        0        0      342 2022-09-17 18:31:17.243170 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1657.json
--rw-r--r--   0        0        0      540 2022-09-17 18:31:17.243349 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666600000.json
--rw-r--r--   0        0        0      359 2022-09-17 18:31:17.243437 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666600001.json
--rw-r--r--   0        0        0      359 2022-09-17 18:31:17.243497 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666600002.json
--rw-r--r--   0        0        0      359 2022-09-17 18:31:17.243549 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666600003.json
--rw-r--r--   0        0        0      527 2022-09-17 18:31:17.243603 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666700000.json
--rw-r--r--   0        0        0      397 2022-09-17 18:31:17.243664 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666700001.json
--rw-r--r--   0        0        0      397 2022-09-17 18:31:17.243713 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666700002.json
--rw-r--r--   0        0        0      397 2022-09-17 18:31:17.243765 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666700003.json
--rw-r--r--   0        0        0      332 2022-09-17 18:31:17.243828 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-17.json
--rw-r--r--   0        0        0      407 2022-09-17 18:31:17.243882 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-170.json
--rw-r--r--   0        0        0      475 2022-09-17 18:31:17.243935 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-172.json
--rw-r--r--   0        0        0      406 2022-09-17 18:31:17.243992 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-18.json
--rw-r--r--   0        0        0      324 2022-09-17 18:31:17.244049 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-18289463.json
--rw-r--r--   0        0        0      330 2022-09-17 18:31:17.244114 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1856.json
--rw-r--r--   0        0        0      523 2022-09-17 18:31:17.244177 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-19.json
--rw-r--r--   0        0        0      348 2022-09-17 18:31:17.244228 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1987.json
--rw-r--r--   0        0        0      470 2022-09-17 18:31:17.244272 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-199.json
--rw-r--r--   0        0        0      351 2022-09-17 18:31:17.244335 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-2.json
--rw-r--r--   0        0        0      341 2022-09-17 18:31:17.244392 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-20.json
--rw-r--r--   0        0        0      510 2022-09-17 18:31:17.244444 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-200.json
--rw-r--r--   0        0        0      344 2022-09-17 18:31:17.244510 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-200625.json
--rw-r--r--   0        0        0      628 2022-09-17 18:31:17.244571 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-201030.json
--rw-r--r--   0        0        0      453 2022-09-17 18:31:17.244628 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-20181205.json
--rw-r--r--   0        0        0      321 2022-09-17 18:31:17.244678 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-2020.json
--rw-r--r--   0        0        0      323 2022-09-17 18:31:17.244731 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-2021.json
--rw-r--r--   0        0        0      338 2022-09-17 18:31:17.244787 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-2022.json
--rw-r--r--   0        0        0      368 2022-09-17 18:31:17.244840 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-21.json
--rw-r--r--   0        0        0      458 2022-09-17 18:31:17.244900 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-2100.json
--rw-r--r--   0        0        0      477 2022-09-17 18:31:17.244945 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-2101.json
--rw-r--r--   0        0        0      638 2022-09-17 18:31:17.245001 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-210309.json
--rw-r--r--   0        0        0      450 2022-09-17 18:31:17.245056 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-211.json
--rw-r--r--   0        0        0      306 2022-09-17 18:31:17.245110 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-22.json
--rw-r--r--   0        0        0      357 2022-09-17 18:31:17.245164 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-222.json
--rw-r--r--   0        0        0      302 2022-09-17 18:31:17.245208 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-23.json
--rw-r--r--   0        0        0      355 2022-09-17 18:31:17.245260 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-24484.json
--rw-r--r--   0        0        0      411 2022-09-17 18:31:17.245317 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-245022926.json
--rw-r--r--   0        0        0      370 2022-09-17 18:31:17.245373 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-245022934.json
--rw-r--r--   0        0        0      370 2022-09-17 18:31:17.245422 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-245022940.json
--rw-r--r--   0        0        0      629 2022-09-17 18:31:17.245482 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-246.json
--rw-r--r--   0        0        0      365 2022-09-17 18:31:17.245537 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-246529.json
--rw-r--r--   0        0        0      353 2022-09-17 18:31:17.245592 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-246785.json
--rw-r--r--   0        0        0      348 2022-09-17 18:31:17.245646 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-24734.json
--rw-r--r--   0        0        0      539 2022-09-17 18:31:17.245701 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-250.json
--rw-r--r--   0        0        0      378 2022-09-17 18:31:17.245754 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-2559.json
--rw-r--r--   0        0        0      469 2022-09-17 18:31:17.245813 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-256.json
--rw-r--r--   0        0        0      483 2022-09-17 18:31:17.245867 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-262.json
--rw-r--r--   0        0        0      541 2022-09-17 18:31:17.245923 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-269.json
--rw-r--r--   0        0        0      604 2022-09-17 18:31:17.245977 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-28.json
--rw-r--r--   0        0        0      566 2022-09-17 18:31:17.246022 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-288.json
--rw-r--r--   0        0        0      374 2022-09-17 18:31:17.246077 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-28945486.json
--rw-r--r--   0        0        0      554 2022-09-17 18:31:17.246132 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-3.json
--rw-r--r--   0        0        0      545 2022-09-17 18:31:17.246192 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-30.json
--rw-r--r--   0        0        0      414 2022-09-17 18:31:17.246248 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-31.json
--rw-r--r--   0        0        0      373 2022-09-17 18:31:17.246305 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-31102.json
--rw-r--r--   0        0        0      539 2022-09-17 18:31:17.246370 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-311752642.json
--rw-r--r--   0        0        0      345 2022-09-17 18:31:17.246425 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-3125659152.json
--rw-r--r--   0        0        0      494 2022-09-17 18:31:17.246478 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-31337.json
--rw-r--r--   0        0        0      349 2022-09-17 18:31:17.246531 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-32.json
--rw-r--r--   0        0        0      484 2022-09-17 18:31:17.246588 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-321.json
--rw-r--r--   0        0        0      560 2022-09-17 18:31:17.246633 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-322.json
--rw-r--r--   0        0        0      365 2022-09-17 18:31:17.246688 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-32659.json
--rw-r--r--   0        0        0      346 2022-09-17 18:31:17.246741 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-33.json
--rw-r--r--   0        0        0      394 2022-09-17 18:31:17.246791 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-333888.json
--rw-r--r--   0        0        0      387 2022-09-17 18:31:17.246845 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-333999.json
--rw-r--r--   0        0        0      583 2022-09-17 18:31:17.246898 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-336.json
--rw-r--r--   0        0        0      583 2022-09-17 18:31:17.246947 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-338.json
--rw-r--r--   0        0        0      313 2022-09-17 18:31:17.247000 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-35.json
--rw-r--r--   0        0        0      340 2022-09-17 18:31:17.247052 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-35855456.json
--rw-r--r--   0        0        0      498 2022-09-17 18:31:17.247113 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-361.json
--rw-r--r--   0        0        0      561 2022-09-17 18:31:17.247162 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-363.json
--rw-r--r--   0        0        0      543 2022-09-17 18:31:17.247212 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-364.json
--rw-r--r--   0        0        0      514 2022-09-17 18:31:17.247260 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-365.json
--rw-r--r--   0        0        0      431 2022-09-17 18:31:17.247314 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-369.json
--rw-r--r--   0        0        0      336 2022-09-17 18:31:17.247369 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-38.json
--rw-r--r--   0        0        0      388 2022-09-17 18:31:17.247421 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-385.json
--rw-r--r--   0        0        0      357 2022-09-17 18:31:17.247473 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-39797.json
--rw-r--r--   0        0        0      661 2022-09-17 18:31:17.247526 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4.json
--rw-r--r--   0        0        0      336 2022-09-17 18:31:17.247577 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-40.json
--rw-r--r--   0        0        0      586 2022-09-17 18:31:17.247632 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4002.json
--rw-r--r--   0        0        0      391 2022-09-17 18:31:17.247681 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-41.json
--rw-r--r--   0        0        0      612 2022-09-17 18:31:17.247734 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-42.json
--rw-r--r--   0        0        0      343 2022-09-17 18:31:17.247788 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-420.json
--rw-r--r--   0        0        0      328 2022-09-17 18:31:17.247843 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-42069.json
--rw-r--r--   0        0        0      855 2022-09-17 18:31:17.247895 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-42161.json
--rw-r--r--   0        0        0      681 2022-09-17 18:31:17.247944 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-421611.json
--rw-r--r--   0        0        0      622 2022-09-17 18:31:17.247995 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4216137055.json
--rw-r--r--   0        0        0      515 2022-09-17 18:31:17.248054 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-42220.json
--rw-r--r--   0        0        0      326 2022-09-17 18:31:17.248104 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-43.json
--rw-r--r--   0        0        0      413 2022-09-17 18:31:17.248165 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-43110.json
--rw-r--r--   0        0        0      419 2022-09-17 18:31:17.248222 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-43113.json
--rw-r--r--   0        0        0      557 2022-09-17 18:31:17.248284 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-43114.json
--rw-r--r--   0        0        0      307 2022-09-17 18:31:17.248336 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-44.json
--rw-r--r--   0        0        0      513 2022-09-17 18:31:17.248387 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-44787.json
--rw-r--r--   0        0        0      466 2022-09-17 18:31:17.248439 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4689.json
--rw-r--r--   0        0        0      513 2022-09-17 18:31:17.248492 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4690.json
--rw-r--r--   0        0        0      363 2022-09-17 18:31:17.248538 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-49797.json
--rw-r--r--   0        0        0      299 2022-09-17 18:31:17.248586 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-499.json
--rw-r--r--   0        0        0      765 2022-09-17 18:31:17.248642 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5.json
--rw-r--r--   0        0        0      329 2022-09-17 18:31:17.248698 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-50.json
--rw-r--r--   0        0        0      337 2022-09-17 18:31:17.248747 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-51.json
--rw-r--r--   0        0        0      404 2022-09-17 18:31:17.248797 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5197.json
--rw-r--r--   0        0        0      360 2022-09-17 18:31:17.248849 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-52.json
--rw-r--r--   0        0        0      367 2022-09-17 18:31:17.248895 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-53.json
--rw-r--r--   0        0        0      592 2022-09-17 18:31:17.248945 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-55.json
--rw-r--r--   0        0        0      423 2022-09-17 18:31:17.248997 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-558.json
--rw-r--r--   0        0        0     1031 2022-09-17 18:31:17.249045 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-56.json
--rw-r--r--   0        0        0      556 2022-09-17 18:31:17.249104 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5700.json
--rw-r--r--   0        0        0      568 2022-09-17 18:31:17.249159 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-58.json
--rw-r--r--   0        0        0      607 2022-09-17 18:31:17.249215 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5851.json
--rw-r--r--   0        0        0      376 2022-09-17 18:31:17.249274 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5869.json
--rw-r--r--   0        0        0      449 2022-09-17 18:31:17.249328 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-59.json
--rw-r--r--   0        0        0      313 2022-09-17 18:31:17.249382 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-595.json
--rw-r--r--   0        0        0      329 2022-09-17 18:31:17.249436 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-6.json
--rw-r--r--   0        0        0      512 2022-09-17 18:31:17.249486 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-60.json
--rw-r--r--   0        0        0      554 2022-09-17 18:31:17.249534 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-61.json
--rw-r--r--   0        0        0      432 2022-09-17 18:31:17.249588 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-61717561.json
--rw-r--r--   0        0        0      335 2022-09-17 18:31:17.249639 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-62.json
--rw-r--r--   0        0        0      513 2022-09-17 18:31:17.249691 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-62320.json
--rw-r--r--   0        0        0      345 2022-09-17 18:31:17.249745 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-63.json
--rw-r--r--   0        0        0      343 2022-09-17 18:31:17.249801 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-64.json
--rw-r--r--   0        0        0      537 2022-09-17 18:31:17.249859 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-65.json
--rw-r--r--   0        0        0      545 2022-09-17 18:31:17.249910 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-66.json
--rw-r--r--   0        0        0      333 2022-09-17 18:31:17.249962 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-67.json
--rw-r--r--   0        0        0      347 2022-09-17 18:31:17.250010 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-68.json
--rw-r--r--   0        0        0      314 2022-09-17 18:31:17.250061 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-686.json
--rw-r--r--   0        0        0      337 2022-09-17 18:31:17.250105 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-69.json
--rw-r--r--   0        0        0      321 2022-09-17 18:31:17.250148 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-7.json
--rw-r--r--   0        0        0      466 2022-09-17 18:31:17.250202 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-71393.json
--rw-r--r--   0        0        0      374 2022-09-17 18:31:17.250255 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-721.json
--rw-r--r--   0        0        0      435 2022-09-17 18:31:17.250308 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-73799.json
--rw-r--r--   0        0        0      347 2022-09-17 18:31:17.250359 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-76.json
--rw-r--r--   0        0        0      568 2022-09-17 18:31:17.250416 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-77.json
--rw-r--r--   0        0        0      351 2022-09-17 18:31:17.250470 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-7762959.json
--rw-r--r--   0        0        0      326 2022-09-17 18:31:17.250519 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-777.json
--rw-r--r--   0        0        0      357 2022-09-17 18:31:17.250569 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-78.json
--rw-r--r--   0        0        0      361 2022-09-17 18:31:17.250624 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-78110.json
--rw-r--r--   0        0        0      311 2022-09-17 18:31:17.250673 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-787.json
--rw-r--r--   0        0        0      471 2022-09-17 18:31:17.250727 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8.json
--rw-r--r--   0        0        0      451 2022-09-17 18:31:17.250779 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-80.json
--rw-r--r--   0        0        0      770 2022-09-17 18:31:17.250835 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-80001.json
--rw-r--r--   0        0        0      325 2022-09-17 18:31:17.250893 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8029.json
--rw-r--r--   0        0        0      297 2022-09-17 18:31:17.250944 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-803.json
--rw-r--r--   0        0        0      560 2022-09-17 18:31:17.250991 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8080.json
--rw-r--r--   0        0        0      320 2022-09-17 18:31:17.251039 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-82.json
--rw-r--r--   0        0        0      364 2022-09-17 18:31:17.251093 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-820.json
--rw-r--r--   0        0        0      310 2022-09-17 18:31:17.251137 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-821.json
--rw-r--r--   0        0        0      374 2022-09-17 18:31:17.251191 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8217.json
--rw-r--r--   0        0        0      366 2022-09-17 18:31:17.251242 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8285.json
--rw-r--r--   0        0        0      577 2022-09-17 18:31:17.251296 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-85.json
--rw-r--r--   0        0        0      550 2022-09-17 18:31:17.251345 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-86.json
--rw-r--r--   0        0        0      473 2022-09-17 18:31:17.251398 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8723.json
--rw-r--r--   0        0        0      414 2022-09-17 18:31:17.251447 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8724.json
--rw-r--r--   0        0        0      345 2022-09-17 18:31:17.251501 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-88.json
--rw-r--r--   0        0        0      485 2022-09-17 18:31:17.251553 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-880.json
--rw-r--r--   0        0        0      353 2022-09-17 18:31:17.251609 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-888.json
--rw-r--r--   0        0        0      498 2022-09-17 18:31:17.251662 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8888.json
--rw-r--r--   0        0        0      365 2022-09-17 18:31:17.251716 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8995.json
--rw-r--r--   0        0        0      307 2022-09-17 18:31:17.251770 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-9.json
--rw-r--r--   0        0        0      642 2022-09-17 18:31:17.251823 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-9000.json
--rw-r--r--   0        0        0      439 2022-09-17 18:31:17.251873 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-940.json
--rw-r--r--   0        0        0      462 2022-09-17 18:31:17.251922 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-95.json
--rw-r--r--   0        0        0      981 2022-09-17 18:31:17.251975 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-955305.json
--rw-r--r--   0        0        0      828 2022-09-17 18:31:17.252029 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-97.json
--rw-r--r--   0        0        0      468 2022-09-17 18:31:17.252083 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-977.json
--rw-r--r--   0        0        0      581 2022-09-17 18:31:17.252136 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-99.json
--rw-r--r--   0        0        0      376 2022-09-17 18:31:17.252191 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-99415706.json
--rw-r--r--   0        0        0      747 2022-09-17 18:31:17.252241 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-998.json
--rw-r--r--   0        0        0      345 2022-09-17 18:31:17.252290 trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-999.json
--rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252374 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/SUR.json
--rw-r--r--   0        0        0      126 2022-09-17 18:31:17.252422 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/alaya.json
--rw-r--r--   0        0        0      137 2022-09-17 18:31:17.252475 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/eraswap.json
--rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252524 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/ethereum.json
--rw-r--r--   0        0        0      147 2022-09-17 18:31:17.252597 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/etherlite.json
--rw-r--r--   0        0        0      131 2022-09-17 18:31:17.252643 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/etho.json
--rw-r--r--   0        0        0      139 2022-09-17 18:31:17.252688 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/fantom.json
--rw-r--r--   0        0        0      135 2022-09-17 18:31:17.252738 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/ftmscan.json
--rw-r--r--   0        0        0      137 2022-09-17 18:31:17.252788 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/lucky.json
--rw-r--r--   0        0        0      136 2022-09-17 18:31:17.252838 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/oneledger.json
--rw-r--r--   0        0        0      124 2022-09-17 18:31:17.252887 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/platon.json
--rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252933 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/polis.json
--rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252980 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/polyjuice.json
--rw-r--r--   0        0        0      138 2022-09-17 18:31:17.253035 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/popcateum.json
--rw-r--r--   0        0        0      125 2022-09-17 18:31:17.253087 trading_strategy-0.9.0/tradingstrategy/chains/_data/icons/velas.json
--rw-r--r--   0        0        0     1305 2022-09-17 18:31:17.253152 trading_strategy-0.9.0/tradingstrategy/chains/build.gradle
--rw-r--r--   0        0        0    59536 2022-09-17 18:31:17.253638 trading_strategy-0.9.0/tradingstrategy/chains/gradle/wrapper/gradle-wrapper.jar
--rw-r--r--   0        0        0      200 2022-09-17 18:31:17.253704 trading_strategy-0.9.0/tradingstrategy/chains/gradle/wrapper/gradle-wrapper.properties
--rwxr-xr-x   0        0        0     8070 2022-09-17 18:31:17.253790 trading_strategy-0.9.0/tradingstrategy/chains/gradlew
--rw-r--r--   0        0        0     2674 2022-09-17 18:31:17.253854 trading_strategy-0.9.0/tradingstrategy/chains/gradlew.bat
--rw-r--r--   0        0        0      707 2022-09-17 18:31:17.254110 trading_strategy-0.9.0/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Env.kt
--rw-r--r--   0        0        0     9378 2022-09-17 18:31:17.254210 trading_strategy-0.9.0/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Main.kt
--rw-r--r--   0        0        0      324 2022-09-17 18:31:17.254293 trading_strategy-0.9.0/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/model/Chain.kt
--rw-r--r--   0        0        0     2060 2022-09-17 18:31:17.254358 trading_strategy-0.9.0/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/model/Exceptions.kt
--rw-r--r--   0        0        0     6318 2022-09-17 18:31:17.254589 trading_strategy-0.9.0/tradingstrategy/chains/src/test/kotlin/org/ethereum/lists/chains/TheChainChecker.kt
--rw-r--r--   0        0        0      325 2022-09-17 18:31:17.254733 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-1.json
--rw-r--r--   0        0        0      293 2022-09-17 18:31:17.254782 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-1.nojson
--rw-r--r--   0        0        0      474 2022-09-17 18:31:17.254834 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-100.json
--rw-r--r--   0        0        0      399 2022-09-17 18:31:17.254880 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-101.json
--rw-r--r--   0        0        0      396 2022-09-17 18:31:17.254929 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-102.json
--rw-r--r--   0        0        0      293 2022-09-17 18:31:17.254978 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-2.json
--rw-r--r--   0        0        0      293 2022-09-17 18:31:17.255026 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-3.json
--rw-r--r--   0        0        0      293 2022-09-17 18:31:17.255075 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-4.json
--rw-r--r--   0        0        0      462 2022-09-17 18:31:17.255129 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-99.json
--rw-r--r--   0        0        0      294 2022-09-17 18:31:17.255180 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-extracomma.json
--rw-r--r--   0        0        0      293 2022-09-17 18:31:17.255227 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-invalid_filename.json
--rw-r--r--   0        0        0      471 2022-09-17 18:31:17.255305 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorerinvalidurl/eip155-1.json
--rw-r--r--   0        0        0      450 2022-09-17 18:31:17.255382 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorermissingurl/eip155-1.json
--rw-r--r--   0        0        0      465 2022-09-17 18:31:17.255464 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorernoname/eip155-1.json
--rw-r--r--   0        0        0      410 2022-09-17 18:31:17.255555 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorersnotarray/eip155-1.json
--rw-r--r--   0        0        0      298 2022-09-17 18:31:17.255637 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/sameshortname/eip155-1.json
--rw-r--r--   0        0        0      595 2022-09-17 18:31:17.255692 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/sameshortname/eip155-5.json
--rw-r--r--   0        0        0      442 2022-09-17 18:31:17.255769 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentchaindoesnotexist/eip155-2.json
--rw-r--r--   0        0        0      468 2022-09-17 18:31:17.255851 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrabridgeelementnoobject/eip155-2.json
--rw-r--r--   0        0        0      478 2022-09-17 18:31:17.255933 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrabridgesfield/eip155-2.json
--rw-r--r--   0        0        0      466 2022-09-17 18:31:17.256014 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrabridgesnoarray/eip155-2.json
--rw-r--r--   0        0        0      464 2022-09-17 18:31:17.256093 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrafield/eip155-2.json
--rw-r--r--   0        0        0      444 2022-09-17 18:31:17.256174 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentinvalidtype/eip155-2.json
--rw-r--r--   0        0        0      401 2022-09-17 18:31:17.256253 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentnobject/eip155-2.json
--rw-r--r--   0        0        0      489 2022-09-17 18:31:17.256327 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/wrongexplorerstandard/eip155-1.json
--rw-r--r--   0        0        0      381 2022-09-17 18:31:17.256410 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/eip155-1.json
--rw-r--r--   0        0        0      590 2022-09-17 18:31:17.256470 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/eip155-5.json
--rw-r--r--   0        0        0      507 2022-09-17 18:31:17.256584 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/withexplorer/eip155-1.json
--rw-r--r--   0        0        0      499 2022-09-17 18:31:17.256641 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/withexplorer/eip155-2.json
--rw-r--r--   0        0        0      381 2022-09-17 18:31:17.256734 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/withparent/eip155-1.json
--rw-r--r--   0        0        0      442 2022-09-17 18:31:17.256785 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/withparent/eip155-2.json
--rw-r--r--   0        0        0      381 2022-09-17 18:31:17.256885 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/withparentbridge/eip155-1.json
--rw-r--r--   0        0        0      506 2022-09-17 18:31:17.256949 trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/withparentbridge/eip155-2.json
--rw-r--r--   0        0        0     3338 2022-12-08 18:11:50.494025 trading_strategy-0.9.0/tradingstrategy/charting/candle_chart.py
--rw-r--r--   0        0        0    15891 2022-12-05 14:53:42.263688 trading_strategy-0.9.0/tradingstrategy/client.py
--rw-r--r--   0        0        0     2400 2022-09-17 18:31:15.775681 trading_strategy-0.9.0/tradingstrategy/environment/base.py
--rw-r--r--   0        0        0      204 2022-09-17 18:31:15.775735 trading_strategy-0.9.0/tradingstrategy/environment/colab.py
--rw-r--r--   0        0        0      267 2022-09-17 18:31:15.775789 trading_strategy-0.9.0/tradingstrategy/environment/config.py
--rw-r--r--   0        0        0        2 2022-09-17 18:31:15.775836 trading_strategy-0.9.0/tradingstrategy/environment/console.py
--rw-r--r--   0        0        0        5 2022-09-17 18:31:15.775881 trading_strategy-0.9.0/tradingstrategy/environment/inpage.py
--rw-r--r--   0        0        0     3279 2022-09-28 17:08:08.709965 trading_strategy-0.9.0/tradingstrategy/environment/interactive_setup.py
--rw-r--r--   0        0        0     4840 2022-12-05 19:49:35.032041 trading_strategy-0.9.0/tradingstrategy/environment/jupyter.py
--rw-r--r--   0        0        0     2017 2022-09-19 08:44:04.949683 trading_strategy-0.9.0/tradingstrategy/environment/jupyterlite.py
--rw-r--r--   0        0        0        0 2022-09-17 18:31:15.776042 trading_strategy-0.9.0/tradingstrategy/environment/oracle.py
--rw-r--r--   0        0        0     7323 2022-09-27 21:11:58.028583 trading_strategy-0.9.0/tradingstrategy/exchange.py
--rw-r--r--   0        0        0     9077 2022-09-17 18:31:15.776244 trading_strategy-0.9.0/tradingstrategy/frameworks/backtrader.py
--rw-r--r--   0        0        0      768 2022-09-17 18:31:15.776310 trading_strategy-0.9.0/tradingstrategy/frameworks/matplotlib.py
--rw-r--r--   0        0        0    12252 2022-09-19 17:09:36.245411 trading_strategy-0.9.0/tradingstrategy/frameworks/qstrader.py
--rw-r--r--   0        0        0     8579 2022-09-17 18:31:15.776498 trading_strategy-0.9.0/tradingstrategy/liquidity.py
--rw-r--r--   0        0        0    40587 2022-11-26 12:17:28.842121 trading_strategy-0.9.0/tradingstrategy/pair.py
--rw-r--r--   0        0        0     8389 2022-09-17 18:31:15.776809 trading_strategy-0.9.0/tradingstrategy/priceimpact.py
--rw-r--r--   0        0        0     2024 2022-09-19 08:44:04.949935 trading_strategy-0.9.0/tradingstrategy/reader.py
--rw-r--r--   0        0        0     1318 2022-09-17 18:31:15.776944 trading_strategy-0.9.0/tradingstrategy/stablecoin.py
--rw-r--r--   0        0        0     3265 2022-09-17 18:31:15.777005 trading_strategy-0.9.0/tradingstrategy/timebucket.py
--rw-r--r--   0        0        0     1182 2022-09-17 18:31:15.777069 trading_strategy-0.9.0/tradingstrategy/token.py
--rw-r--r--   0        0        0     1046 2022-09-17 18:31:15.777154 trading_strategy-0.9.0/tradingstrategy/transport/base.py
--rw-r--r--   0        0        0    12031 2022-11-19 14:28:56.206120 trading_strategy-0.9.0/tradingstrategy/transport/cache.py
--rw-r--r--   0        0        0     7019 2022-12-05 19:49:18.944960 trading_strategy-0.9.0/tradingstrategy/transport/jsonl.py
--rw-r--r--   0        0        0      503 2022-09-19 08:44:04.950008 trading_strategy-0.9.0/tradingstrategy/transport/pyodide.py
--rw-r--r--   0        0        0     1767 2022-09-17 18:31:15.777399 trading_strategy-0.9.0/tradingstrategy/types.py
--rw-r--r--   0        0        0     2144 2022-09-17 18:31:15.777468 trading_strategy-0.9.0/tradingstrategy/universe.py
--rw-r--r--   0        0        0     1174 2022-09-17 18:31:15.777560 trading_strategy-0.9.0/tradingstrategy/utils/columnar.py
--rw-r--r--   0        0        0      946 2022-09-17 18:31:15.777619 trading_strategy-0.9.0/tradingstrategy/utils/format.py
--rw-r--r--   0        0        0    13678 2022-12-08 18:13:56.541607 trading_strategy-0.9.0/tradingstrategy/utils/groupeduniverse.py
--rw-r--r--   0        0        0     3256 2022-11-19 14:28:56.206660 trading_strategy-0.9.0/tradingstrategy/utils/jupyter.py
--rw-r--r--   0        0        0     3562 2022-09-17 18:31:15.777891 trading_strategy-0.9.0/tradingstrategy/utils/schema.py
--rw-r--r--   0        0        0     2481 2022-09-17 18:31:15.777957 trading_strategy-0.9.0/tradingstrategy/utils/summarydataframe.py
--rw-r--r--   0        0        0      901 2022-09-28 17:28:53.658400 trading_strategy-0.9.0/tradingstrategy/utils/time.py
--rw-r--r--   0        0        0     7085 1970-01-01 00:00:00.000000 trading_strategy-0.9.0/setup.py
--rw-r--r--   0        0        0     4791 1970-01-01 00:00:00.000000 trading_strategy-0.9.0/PKG-INFO
+-rw-r--r--   0        0        0      725 2022-12-15 16:47:52.647040 trading_strategy-0.9.1/LICENSE.txt
+-rw-r--r--   0        0        0     3496 2022-12-15 16:47:52.647294 trading_strategy-0.9.1/README.md
+-rw-r--r--   0        0        0     1892 2022-12-15 16:48:18.080989 trading_strategy-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0       22 2022-09-17 18:31:15.774650 trading_strategy-0.9.1/tradingstrategy/__init__.py
+-rw-r--r--   0        0        0       48 2022-09-17 18:31:15.774796 trading_strategy-0.9.1/tradingstrategy/analysis/__init__.py
+-rw-r--r--   0        0        0     9034 2022-09-17 18:31:15.774905 trading_strategy-0.9.1/tradingstrategy/analysis/portfolioanalyzer.py
+-rw-r--r--   0        0        0     2660 2022-09-17 18:31:15.774982 trading_strategy-0.9.1/tradingstrategy/analysis/profitdistribution.py
+-rw-r--r--   0        0        0    18671 2022-09-17 18:31:15.775103 trading_strategy-0.9.1/tradingstrategy/analysis/tradeanalyzer.py
+-rw-r--r--   0        0        0      593 2022-09-17 18:31:15.775189 trading_strategy-0.9.1/tradingstrategy/analysis/tradehint.py
+-rw-r--r--   0        0        0     1801 2022-09-19 08:44:04.949231 trading_strategy-0.9.1/tradingstrategy/caip.py
+-rw-r--r--   0        0        0    18713 2022-12-08 18:11:18.366497 trading_strategy-0.9.1/tradingstrategy/candle.py
+-rw-r--r--   0        0        0     7906 2022-09-17 18:31:15.775445 trading_strategy-0.9.1/tradingstrategy/chain.py
+-rw-r--r--   0        0        0       82 2022-09-17 18:31:17.238364 trading_strategy-0.9.1/tradingstrategy/chains/.ci/kontinuum.json
+-rw-r--r--   0        0        0       86 2022-09-17 18:31:17.190414 trading_strategy-0.9.1/tradingstrategy/chains/.git
+-rw-r--r--   0        0        0      608 2022-09-17 18:31:17.238529 trading_strategy-0.9.1/tradingstrategy/chains/.github/ISSUE_TEMPLATE/add-new-chain---network-id.md
+-rw-r--r--   0        0        0      122 2022-09-17 18:31:17.238589 trading_strategy-0.9.1/tradingstrategy/chains/.github/ISSUE_TEMPLATE/other.md
+-rw-r--r--   0        0        0      139 2022-09-17 18:31:17.238646 trading_strategy-0.9.1/tradingstrategy/chains/.github/dependabot.yml
+-rw-r--r--   0        0        0     1072 2022-09-17 18:31:17.238736 trading_strategy-0.9.1/tradingstrategy/chains/.github/workflows/build_and_deploy.yml
+-rw-r--r--   0        0        0       62 2022-09-17 18:31:17.238786 trading_strategy-0.9.1/tradingstrategy/chains/.gitignore
+-rw-r--r--   0        0        0     1057 2022-09-17 18:31:17.238847 trading_strategy-0.9.1/tradingstrategy/chains/LICENSE
+-rw-r--r--   0        0        0     2539 2022-09-17 18:31:17.238924 trading_strategy-0.9.1/tradingstrategy/chains/README.md
+-rw-r--r--   0        0        0      349 2022-09-17 18:31:17.239061 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/deprecated/eip155-218.json
+-rw-r--r--   0        0        0      694 2022-09-17 18:31:17.239123 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1.json
+-rw-r--r--   0        0        0      441 2022-09-17 18:31:17.239180 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-10.json
+-rw-r--r--   0        0        0      784 2022-09-17 18:31:17.239240 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100.json
+-rw-r--r--   0        0        0      483 2022-09-17 18:31:17.239295 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-10000.json
+-rw-r--r--   0        0        0      369 2022-09-17 18:31:17.239359 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100000.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239417 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100001.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239470 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100002.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239522 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100003.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239570 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100004.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239623 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100005.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239675 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100006.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239722 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100007.json
+-rw-r--r--   0        0        0      576 2022-09-17 18:31:17.239771 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100008.json
+-rw-r--r--   0        0        0      427 2022-09-17 18:31:17.239831 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-10001.json
+-rw-r--r--   0        0        0      414 2022-09-17 18:31:17.239885 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1001.json
+-rw-r--r--   0        0        0      350 2022-09-17 18:31:17.239943 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1007.json
+-rw-r--r--   0        0        0      345 2022-09-17 18:31:17.239999 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-101.json
+-rw-r--r--   0        0        0      339 2022-09-17 18:31:17.240052 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1010.json
+-rw-r--r--   0        0        0      420 2022-09-17 18:31:17.240103 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-10101.json
+-rw-r--r--   0        0        0      346 2022-09-17 18:31:17.240162 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1012.json
+-rw-r--r--   0        0        0      363 2022-09-17 18:31:17.240212 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-102.json
+-rw-r--r--   0        0        0      327 2022-09-17 18:31:17.240262 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1022.json
+-rw-r--r--   0        0        0      337 2022-09-17 18:31:17.240316 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1023.json
+-rw-r--r--   0        0        0      464 2022-09-17 18:31:17.240368 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1024.json
+-rw-r--r--   0        0        0      485 2022-09-17 18:31:17.240429 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1028.json
+-rw-r--r--   0        0        0      514 2022-09-17 18:31:17.240480 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-106.json
+-rw-r--r--   0        0        0      415 2022-09-17 18:31:17.240533 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-108.json
+-rw-r--r--   0        0        0      364 2022-09-17 18:31:17.240590 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-11.json
+-rw-r--r--   0        0        0      375 2022-09-17 18:31:17.240646 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110.json
+-rw-r--r--   0        0        0      368 2022-09-17 18:31:17.240692 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110000.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240747 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110001.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240799 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110002.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240851 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110003.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240899 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110004.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.240947 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110005.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.241000 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110006.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.241057 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110007.json
+-rw-r--r--   0        0        0      573 2022-09-17 18:31:17.241107 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110008.json
+-rw-r--r--   0        0        0      395 2022-09-17 18:31:17.241158 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-111.json
+-rw-r--r--   0        0        0      379 2022-09-17 18:31:17.241212 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1122334455.json
+-rw-r--r--   0        0        0      300 2022-09-17 18:31:17.241269 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-11297108099.json
+-rw-r--r--   0        0        0      299 2022-09-17 18:31:17.241324 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-11297108109.json
+-rw-r--r--   0        0        0      431 2022-09-17 18:31:17.241378 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1139.json
+-rw-r--r--   0        0        0      438 2022-09-17 18:31:17.241428 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1140.json
+-rw-r--r--   0        0        0      343 2022-09-17 18:31:17.241482 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-12.json
+-rw-r--r--   0        0        0      485 2022-09-17 18:31:17.241537 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1213.json
+-rw-r--r--   0        0        0      313 2022-09-17 18:31:17.241591 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-122.json
+-rw-r--r--   0        0        0      363 2022-09-17 18:31:17.241642 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-124.json
+-rw-r--r--   0        0        0      373 2022-09-17 18:31:17.241696 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-127.json
+-rw-r--r--   0        0        0      591 2022-09-17 18:31:17.241756 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-128.json
+-rw-r--r--   0        0        0      313 2022-09-17 18:31:17.241809 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1284.json
+-rw-r--r--   0        0        0      602 2022-09-17 18:31:17.241865 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1285.json
+-rw-r--r--   0        0        0      266 2022-09-17 18:31:17.241925 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1286.json
+-rw-r--r--   0        0        0      406 2022-09-17 18:31:17.241986 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1287.json
+-rw-r--r--   0        0        0      361 2022-09-17 18:31:17.242065 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1288.json
+-rw-r--r--   0        0        0      390 2022-09-17 18:31:17.242123 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-13.json
+-rw-r--r--   0        0        0      531 2022-09-17 18:31:17.242176 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1313114.json
+-rw-r--r--   0        0        0      341 2022-09-17 18:31:17.242237 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1313161554.json
+-rw-r--r--   0        0        0      350 2022-09-17 18:31:17.242293 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1313161555.json
+-rw-r--r--   0        0        0      350 2022-09-17 18:31:17.242340 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1313161556.json
+-rw-r--r--   0        0        0      324 2022-09-17 18:31:17.242392 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1313500.json
+-rw-r--r--   0        0        0      364 2022-09-17 18:31:17.242455 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-13371337.json
+-rw-r--r--   0        0        0      778 2022-09-17 18:31:17.242527 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-137.json
+-rw-r--r--   0        0        0      286 2022-09-17 18:31:17.242592 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-14.json
+-rw-r--r--   0        0        0      313 2022-09-17 18:31:17.242658 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-142.json
+-rw-r--r--   0        0        0      370 2022-09-17 18:31:17.242717 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-15.json
+-rw-r--r--   0        0        0      355 2022-09-17 18:31:17.242772 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-16.json
+-rw-r--r--   0        0        0      381 2022-09-17 18:31:17.242835 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-16000.json
+-rw-r--r--   0        0        0      447 2022-09-17 18:31:17.242881 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-16001.json
+-rw-r--r--   0        0        0      346 2022-09-17 18:31:17.242931 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1618.json
+-rw-r--r--   0        0        0      436 2022-09-17 18:31:17.242986 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-162.json
+-rw-r--r--   0        0        0      352 2022-09-17 18:31:17.243037 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1620.json
+-rw-r--r--   0        0        0      362 2022-09-17 18:31:17.243098 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-163.json
+-rw-r--r--   0        0        0      342 2022-09-17 18:31:17.243170 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1657.json
+-rw-r--r--   0        0        0      540 2022-09-17 18:31:17.243349 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666600000.json
+-rw-r--r--   0        0        0      359 2022-09-17 18:31:17.243437 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666600001.json
+-rw-r--r--   0        0        0      359 2022-09-17 18:31:17.243497 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666600002.json
+-rw-r--r--   0        0        0      359 2022-09-17 18:31:17.243549 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666600003.json
+-rw-r--r--   0        0        0      527 2022-09-17 18:31:17.243603 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666700000.json
+-rw-r--r--   0        0        0      397 2022-09-17 18:31:17.243664 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666700001.json
+-rw-r--r--   0        0        0      397 2022-09-17 18:31:17.243713 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666700002.json
+-rw-r--r--   0        0        0      397 2022-09-17 18:31:17.243765 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666700003.json
+-rw-r--r--   0        0        0      332 2022-09-17 18:31:17.243828 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-17.json
+-rw-r--r--   0        0        0      407 2022-09-17 18:31:17.243882 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-170.json
+-rw-r--r--   0        0        0      475 2022-09-17 18:31:17.243935 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-172.json
+-rw-r--r--   0        0        0      406 2022-09-17 18:31:17.243992 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-18.json
+-rw-r--r--   0        0        0      324 2022-09-17 18:31:17.244049 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-18289463.json
+-rw-r--r--   0        0        0      330 2022-09-17 18:31:17.244114 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1856.json
+-rw-r--r--   0        0        0      523 2022-09-17 18:31:17.244177 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-19.json
+-rw-r--r--   0        0        0      348 2022-09-17 18:31:17.244228 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1987.json
+-rw-r--r--   0        0        0      470 2022-09-17 18:31:17.244272 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-199.json
+-rw-r--r--   0        0        0      351 2022-09-17 18:31:17.244335 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-2.json
+-rw-r--r--   0        0        0      341 2022-09-17 18:31:17.244392 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-20.json
+-rw-r--r--   0        0        0      510 2022-09-17 18:31:17.244444 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-200.json
+-rw-r--r--   0        0        0      344 2022-09-17 18:31:17.244510 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-200625.json
+-rw-r--r--   0        0        0      628 2022-09-17 18:31:17.244571 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-201030.json
+-rw-r--r--   0        0        0      453 2022-09-17 18:31:17.244628 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-20181205.json
+-rw-r--r--   0        0        0      321 2022-09-17 18:31:17.244678 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-2020.json
+-rw-r--r--   0        0        0      323 2022-09-17 18:31:17.244731 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-2021.json
+-rw-r--r--   0        0        0      338 2022-09-17 18:31:17.244787 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-2022.json
+-rw-r--r--   0        0        0      368 2022-09-17 18:31:17.244840 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-21.json
+-rw-r--r--   0        0        0      458 2022-09-17 18:31:17.244900 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-2100.json
+-rw-r--r--   0        0        0      477 2022-09-17 18:31:17.244945 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-2101.json
+-rw-r--r--   0        0        0      638 2022-09-17 18:31:17.245001 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-210309.json
+-rw-r--r--   0        0        0      450 2022-09-17 18:31:17.245056 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-211.json
+-rw-r--r--   0        0        0      306 2022-09-17 18:31:17.245110 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-22.json
+-rw-r--r--   0        0        0      357 2022-09-17 18:31:17.245164 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-222.json
+-rw-r--r--   0        0        0      302 2022-09-17 18:31:17.245208 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-23.json
+-rw-r--r--   0        0        0      355 2022-09-17 18:31:17.245260 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-24484.json
+-rw-r--r--   0        0        0      411 2022-09-17 18:31:17.245317 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-245022926.json
+-rw-r--r--   0        0        0      370 2022-09-17 18:31:17.245373 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-245022934.json
+-rw-r--r--   0        0        0      370 2022-09-17 18:31:17.245422 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-245022940.json
+-rw-r--r--   0        0        0      629 2022-09-17 18:31:17.245482 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-246.json
+-rw-r--r--   0        0        0      365 2022-09-17 18:31:17.245537 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-246529.json
+-rw-r--r--   0        0        0      353 2022-09-17 18:31:17.245592 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-246785.json
+-rw-r--r--   0        0        0      348 2022-09-17 18:31:17.245646 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-24734.json
+-rw-r--r--   0        0        0      539 2022-09-17 18:31:17.245701 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-250.json
+-rw-r--r--   0        0        0      378 2022-09-17 18:31:17.245754 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-2559.json
+-rw-r--r--   0        0        0      469 2022-09-17 18:31:17.245813 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-256.json
+-rw-r--r--   0        0        0      483 2022-09-17 18:31:17.245867 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-262.json
+-rw-r--r--   0        0        0      541 2022-09-17 18:31:17.245923 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-269.json
+-rw-r--r--   0        0        0      604 2022-09-17 18:31:17.245977 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-28.json
+-rw-r--r--   0        0        0      566 2022-09-17 18:31:17.246022 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-288.json
+-rw-r--r--   0        0        0      374 2022-09-17 18:31:17.246077 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-28945486.json
+-rw-r--r--   0        0        0      554 2022-09-17 18:31:17.246132 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-3.json
+-rw-r--r--   0        0        0      545 2022-09-17 18:31:17.246192 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-30.json
+-rw-r--r--   0        0        0      414 2022-09-17 18:31:17.246248 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-31.json
+-rw-r--r--   0        0        0      373 2022-09-17 18:31:17.246305 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-31102.json
+-rw-r--r--   0        0        0      539 2022-09-17 18:31:17.246370 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-311752642.json
+-rw-r--r--   0        0        0      345 2022-09-17 18:31:17.246425 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-3125659152.json
+-rw-r--r--   0        0        0      494 2022-09-17 18:31:17.246478 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-31337.json
+-rw-r--r--   0        0        0      349 2022-09-17 18:31:17.246531 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-32.json
+-rw-r--r--   0        0        0      484 2022-09-17 18:31:17.246588 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-321.json
+-rw-r--r--   0        0        0      560 2022-09-17 18:31:17.246633 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-322.json
+-rw-r--r--   0        0        0      365 2022-09-17 18:31:17.246688 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-32659.json
+-rw-r--r--   0        0        0      346 2022-09-17 18:31:17.246741 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-33.json
+-rw-r--r--   0        0        0      394 2022-09-17 18:31:17.246791 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-333888.json
+-rw-r--r--   0        0        0      387 2022-09-17 18:31:17.246845 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-333999.json
+-rw-r--r--   0        0        0      583 2022-09-17 18:31:17.246898 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-336.json
+-rw-r--r--   0        0        0      583 2022-09-17 18:31:17.246947 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-338.json
+-rw-r--r--   0        0        0      313 2022-09-17 18:31:17.247000 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-35.json
+-rw-r--r--   0        0        0      340 2022-09-17 18:31:17.247052 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-35855456.json
+-rw-r--r--   0        0        0      498 2022-09-17 18:31:17.247113 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-361.json
+-rw-r--r--   0        0        0      561 2022-09-17 18:31:17.247162 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-363.json
+-rw-r--r--   0        0        0      543 2022-09-17 18:31:17.247212 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-364.json
+-rw-r--r--   0        0        0      514 2022-09-17 18:31:17.247260 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-365.json
+-rw-r--r--   0        0        0      431 2022-09-17 18:31:17.247314 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-369.json
+-rw-r--r--   0        0        0      336 2022-09-17 18:31:17.247369 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-38.json
+-rw-r--r--   0        0        0      388 2022-09-17 18:31:17.247421 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-385.json
+-rw-r--r--   0        0        0      357 2022-09-17 18:31:17.247473 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-39797.json
+-rw-r--r--   0        0        0      661 2022-09-17 18:31:17.247526 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4.json
+-rw-r--r--   0        0        0      336 2022-09-17 18:31:17.247577 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-40.json
+-rw-r--r--   0        0        0      586 2022-09-17 18:31:17.247632 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4002.json
+-rw-r--r--   0        0        0      391 2022-09-17 18:31:17.247681 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-41.json
+-rw-r--r--   0        0        0      612 2022-09-17 18:31:17.247734 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-42.json
+-rw-r--r--   0        0        0      343 2022-09-17 18:31:17.247788 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-420.json
+-rw-r--r--   0        0        0      328 2022-09-17 18:31:17.247843 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-42069.json
+-rw-r--r--   0        0        0      855 2022-09-17 18:31:17.247895 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-42161.json
+-rw-r--r--   0        0        0      681 2022-09-17 18:31:17.247944 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-421611.json
+-rw-r--r--   0        0        0      622 2022-09-17 18:31:17.247995 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4216137055.json
+-rw-r--r--   0        0        0      515 2022-09-17 18:31:17.248054 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-42220.json
+-rw-r--r--   0        0        0      326 2022-09-17 18:31:17.248104 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-43.json
+-rw-r--r--   0        0        0      413 2022-09-17 18:31:17.248165 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-43110.json
+-rw-r--r--   0        0        0      419 2022-09-17 18:31:17.248222 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-43113.json
+-rw-r--r--   0        0        0      557 2022-09-17 18:31:17.248284 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-43114.json
+-rw-r--r--   0        0        0      307 2022-09-17 18:31:17.248336 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-44.json
+-rw-r--r--   0        0        0      513 2022-09-17 18:31:17.248387 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-44787.json
+-rw-r--r--   0        0        0      466 2022-09-17 18:31:17.248439 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4689.json
+-rw-r--r--   0        0        0      513 2022-09-17 18:31:17.248492 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4690.json
+-rw-r--r--   0        0        0      363 2022-09-17 18:31:17.248538 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-49797.json
+-rw-r--r--   0        0        0      299 2022-09-17 18:31:17.248586 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-499.json
+-rw-r--r--   0        0        0      765 2022-09-17 18:31:17.248642 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5.json
+-rw-r--r--   0        0        0      329 2022-09-17 18:31:17.248698 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-50.json
+-rw-r--r--   0        0        0      337 2022-09-17 18:31:17.248747 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-51.json
+-rw-r--r--   0        0        0      404 2022-09-17 18:31:17.248797 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5197.json
+-rw-r--r--   0        0        0      360 2022-09-17 18:31:17.248849 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-52.json
+-rw-r--r--   0        0        0      367 2022-09-17 18:31:17.248895 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-53.json
+-rw-r--r--   0        0        0      592 2022-09-17 18:31:17.248945 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-55.json
+-rw-r--r--   0        0        0      423 2022-09-17 18:31:17.248997 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-558.json
+-rw-r--r--   0        0        0     1031 2022-09-17 18:31:17.249045 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-56.json
+-rw-r--r--   0        0        0      556 2022-09-17 18:31:17.249104 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5700.json
+-rw-r--r--   0        0        0      568 2022-09-17 18:31:17.249159 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-58.json
+-rw-r--r--   0        0        0      607 2022-09-17 18:31:17.249215 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5851.json
+-rw-r--r--   0        0        0      376 2022-09-17 18:31:17.249274 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5869.json
+-rw-r--r--   0        0        0      449 2022-09-17 18:31:17.249328 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-59.json
+-rw-r--r--   0        0        0      313 2022-09-17 18:31:17.249382 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-595.json
+-rw-r--r--   0        0        0      329 2022-09-17 18:31:17.249436 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-6.json
+-rw-r--r--   0        0        0      512 2022-09-17 18:31:17.249486 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-60.json
+-rw-r--r--   0        0        0      554 2022-09-17 18:31:17.249534 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-61.json
+-rw-r--r--   0        0        0      432 2022-09-17 18:31:17.249588 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-61717561.json
+-rw-r--r--   0        0        0      335 2022-09-17 18:31:17.249639 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-62.json
+-rw-r--r--   0        0        0      513 2022-09-17 18:31:17.249691 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-62320.json
+-rw-r--r--   0        0        0      345 2022-09-17 18:31:17.249745 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-63.json
+-rw-r--r--   0        0        0      343 2022-09-17 18:31:17.249801 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-64.json
+-rw-r--r--   0        0        0      537 2022-09-17 18:31:17.249859 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-65.json
+-rw-r--r--   0        0        0      545 2022-09-17 18:31:17.249910 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-66.json
+-rw-r--r--   0        0        0      333 2022-09-17 18:31:17.249962 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-67.json
+-rw-r--r--   0        0        0      347 2022-09-17 18:31:17.250010 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-68.json
+-rw-r--r--   0        0        0      314 2022-09-17 18:31:17.250061 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-686.json
+-rw-r--r--   0        0        0      337 2022-09-17 18:31:17.250105 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-69.json
+-rw-r--r--   0        0        0      321 2022-09-17 18:31:17.250148 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-7.json
+-rw-r--r--   0        0        0      466 2022-09-17 18:31:17.250202 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-71393.json
+-rw-r--r--   0        0        0      374 2022-09-17 18:31:17.250255 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-721.json
+-rw-r--r--   0        0        0      435 2022-09-17 18:31:17.250308 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-73799.json
+-rw-r--r--   0        0        0      347 2022-09-17 18:31:17.250359 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-76.json
+-rw-r--r--   0        0        0      568 2022-09-17 18:31:17.250416 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-77.json
+-rw-r--r--   0        0        0      351 2022-09-17 18:31:17.250470 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-7762959.json
+-rw-r--r--   0        0        0      326 2022-09-17 18:31:17.250519 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-777.json
+-rw-r--r--   0        0        0      357 2022-09-17 18:31:17.250569 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-78.json
+-rw-r--r--   0        0        0      361 2022-09-17 18:31:17.250624 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-78110.json
+-rw-r--r--   0        0        0      311 2022-09-17 18:31:17.250673 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-787.json
+-rw-r--r--   0        0        0      471 2022-09-17 18:31:17.250727 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8.json
+-rw-r--r--   0        0        0      451 2022-09-17 18:31:17.250779 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-80.json
+-rw-r--r--   0        0        0      770 2022-09-17 18:31:17.250835 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-80001.json
+-rw-r--r--   0        0        0      325 2022-09-17 18:31:17.250893 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8029.json
+-rw-r--r--   0        0        0      297 2022-09-17 18:31:17.250944 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-803.json
+-rw-r--r--   0        0        0      560 2022-09-17 18:31:17.250991 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8080.json
+-rw-r--r--   0        0        0      320 2022-09-17 18:31:17.251039 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-82.json
+-rw-r--r--   0        0        0      364 2022-09-17 18:31:17.251093 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-820.json
+-rw-r--r--   0        0        0      310 2022-09-17 18:31:17.251137 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-821.json
+-rw-r--r--   0        0        0      374 2022-09-17 18:31:17.251191 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8217.json
+-rw-r--r--   0        0        0      366 2022-09-17 18:31:17.251242 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8285.json
+-rw-r--r--   0        0        0      577 2022-09-17 18:31:17.251296 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-85.json
+-rw-r--r--   0        0        0      550 2022-09-17 18:31:17.251345 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-86.json
+-rw-r--r--   0        0        0      473 2022-09-17 18:31:17.251398 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8723.json
+-rw-r--r--   0        0        0      414 2022-09-17 18:31:17.251447 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8724.json
+-rw-r--r--   0        0        0      345 2022-09-17 18:31:17.251501 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-88.json
+-rw-r--r--   0        0        0      485 2022-09-17 18:31:17.251553 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-880.json
+-rw-r--r--   0        0        0      353 2022-09-17 18:31:17.251609 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-888.json
+-rw-r--r--   0        0        0      498 2022-09-17 18:31:17.251662 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8888.json
+-rw-r--r--   0        0        0      365 2022-09-17 18:31:17.251716 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8995.json
+-rw-r--r--   0        0        0      307 2022-09-17 18:31:17.251770 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-9.json
+-rw-r--r--   0        0        0      642 2022-09-17 18:31:17.251823 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-9000.json
+-rw-r--r--   0        0        0      439 2022-09-17 18:31:17.251873 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-940.json
+-rw-r--r--   0        0        0      462 2022-09-17 18:31:17.251922 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-95.json
+-rw-r--r--   0        0        0      981 2022-09-17 18:31:17.251975 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-955305.json
+-rw-r--r--   0        0        0      828 2022-09-17 18:31:17.252029 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-97.json
+-rw-r--r--   0        0        0      468 2022-09-17 18:31:17.252083 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-977.json
+-rw-r--r--   0        0        0      581 2022-09-17 18:31:17.252136 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-99.json
+-rw-r--r--   0        0        0      376 2022-09-17 18:31:17.252191 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-99415706.json
+-rw-r--r--   0        0        0      747 2022-09-17 18:31:17.252241 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-998.json
+-rw-r--r--   0        0        0      345 2022-09-17 18:31:17.252290 trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-999.json
+-rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252374 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/SUR.json
+-rw-r--r--   0        0        0      126 2022-09-17 18:31:17.252422 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/alaya.json
+-rw-r--r--   0        0        0      137 2022-09-17 18:31:17.252475 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/eraswap.json
+-rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252524 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/ethereum.json
+-rw-r--r--   0        0        0      147 2022-09-17 18:31:17.252597 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/etherlite.json
+-rw-r--r--   0        0        0      131 2022-09-17 18:31:17.252643 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/etho.json
+-rw-r--r--   0        0        0      139 2022-09-17 18:31:17.252688 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/fantom.json
+-rw-r--r--   0        0        0      135 2022-09-17 18:31:17.252738 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/ftmscan.json
+-rw-r--r--   0        0        0      137 2022-09-17 18:31:17.252788 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/lucky.json
+-rw-r--r--   0        0        0      136 2022-09-17 18:31:17.252838 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/oneledger.json
+-rw-r--r--   0        0        0      124 2022-09-17 18:31:17.252887 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/platon.json
+-rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252933 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/polis.json
+-rw-r--r--   0        0        0      127 2022-09-17 18:31:17.252980 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/polyjuice.json
+-rw-r--r--   0        0        0      138 2022-09-17 18:31:17.253035 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/popcateum.json
+-rw-r--r--   0        0        0      125 2022-09-17 18:31:17.253087 trading_strategy-0.9.1/tradingstrategy/chains/_data/icons/velas.json
+-rw-r--r--   0        0        0     1305 2022-09-17 18:31:17.253152 trading_strategy-0.9.1/tradingstrategy/chains/build.gradle
+-rw-r--r--   0        0        0    59536 2022-09-17 18:31:17.253638 trading_strategy-0.9.1/tradingstrategy/chains/gradle/wrapper/gradle-wrapper.jar
+-rw-r--r--   0        0        0      200 2022-09-17 18:31:17.253704 trading_strategy-0.9.1/tradingstrategy/chains/gradle/wrapper/gradle-wrapper.properties
+-rwxr-xr-x   0        0        0     8070 2022-09-17 18:31:17.253790 trading_strategy-0.9.1/tradingstrategy/chains/gradlew
+-rw-r--r--   0        0        0     2674 2022-09-17 18:31:17.253854 trading_strategy-0.9.1/tradingstrategy/chains/gradlew.bat
+-rw-r--r--   0        0        0      707 2022-09-17 18:31:17.254110 trading_strategy-0.9.1/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Env.kt
+-rw-r--r--   0        0        0     9378 2022-09-17 18:31:17.254210 trading_strategy-0.9.1/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Main.kt
+-rw-r--r--   0        0        0      324 2022-09-17 18:31:17.254293 trading_strategy-0.9.1/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/model/Chain.kt
+-rw-r--r--   0        0        0     2060 2022-09-17 18:31:17.254358 trading_strategy-0.9.1/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/model/Exceptions.kt
+-rw-r--r--   0        0        0     6318 2022-09-17 18:31:17.254589 trading_strategy-0.9.1/tradingstrategy/chains/src/test/kotlin/org/ethereum/lists/chains/TheChainChecker.kt
+-rw-r--r--   0        0        0      325 2022-09-17 18:31:17.254733 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-1.json
+-rw-r--r--   0        0        0      293 2022-09-17 18:31:17.254782 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-1.nojson
+-rw-r--r--   0        0        0      474 2022-09-17 18:31:17.254834 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-100.json
+-rw-r--r--   0        0        0      399 2022-09-17 18:31:17.254880 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-101.json
+-rw-r--r--   0        0        0      396 2022-09-17 18:31:17.254929 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-102.json
+-rw-r--r--   0        0        0      293 2022-09-17 18:31:17.254978 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-2.json
+-rw-r--r--   0        0        0      293 2022-09-17 18:31:17.255026 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-3.json
+-rw-r--r--   0        0        0      293 2022-09-17 18:31:17.255075 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-4.json
+-rw-r--r--   0        0        0      462 2022-09-17 18:31:17.255129 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-99.json
+-rw-r--r--   0        0        0      294 2022-09-17 18:31:17.255180 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-extracomma.json
+-rw-r--r--   0        0        0      293 2022-09-17 18:31:17.255227 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/eip155-invalid_filename.json
+-rw-r--r--   0        0        0      471 2022-09-17 18:31:17.255305 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorerinvalidurl/eip155-1.json
+-rw-r--r--   0        0        0      450 2022-09-17 18:31:17.255382 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorermissingurl/eip155-1.json
+-rw-r--r--   0        0        0      465 2022-09-17 18:31:17.255464 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorernoname/eip155-1.json
+-rw-r--r--   0        0        0      410 2022-09-17 18:31:17.255555 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/explorersnotarray/eip155-1.json
+-rw-r--r--   0        0        0      298 2022-09-17 18:31:17.255637 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/sameshortname/eip155-1.json
+-rw-r--r--   0        0        0      595 2022-09-17 18:31:17.255692 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/sameshortname/eip155-5.json
+-rw-r--r--   0        0        0      442 2022-09-17 18:31:17.255769 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentchaindoesnotexist/eip155-2.json
+-rw-r--r--   0        0        0      468 2022-09-17 18:31:17.255851 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrabridgeelementnoobject/eip155-2.json
+-rw-r--r--   0        0        0      478 2022-09-17 18:31:17.255933 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrabridgesfield/eip155-2.json
+-rw-r--r--   0        0        0      466 2022-09-17 18:31:17.256014 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrabridgesnoarray/eip155-2.json
+-rw-r--r--   0        0        0      464 2022-09-17 18:31:17.256093 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentextrafield/eip155-2.json
+-rw-r--r--   0        0        0      444 2022-09-17 18:31:17.256174 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentinvalidtype/eip155-2.json
+-rw-r--r--   0        0        0      401 2022-09-17 18:31:17.256253 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/withparentnobject/eip155-2.json
+-rw-r--r--   0        0        0      489 2022-09-17 18:31:17.256327 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/wrongexplorerstandard/eip155-1.json
+-rw-r--r--   0        0        0      381 2022-09-17 18:31:17.256410 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/eip155-1.json
+-rw-r--r--   0        0        0      590 2022-09-17 18:31:17.256470 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/eip155-5.json
+-rw-r--r--   0        0        0      507 2022-09-17 18:31:17.256584 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/withexplorer/eip155-1.json
+-rw-r--r--   0        0        0      499 2022-09-17 18:31:17.256641 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/withexplorer/eip155-2.json
+-rw-r--r--   0        0        0      381 2022-09-17 18:31:17.256734 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/withparent/eip155-1.json
+-rw-r--r--   0        0        0      442 2022-09-17 18:31:17.256785 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/withparent/eip155-2.json
+-rw-r--r--   0        0        0      381 2022-09-17 18:31:17.256885 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/withparentbridge/eip155-1.json
+-rw-r--r--   0        0        0      506 2022-09-17 18:31:17.256949 trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/withparentbridge/eip155-2.json
+-rw-r--r--   0        0        0     3732 2022-12-15 16:47:52.650816 trading_strategy-0.9.1/tradingstrategy/charting/candle_chart.py
+-rw-r--r--   0        0        0    15891 2022-12-05 14:53:42.263688 trading_strategy-0.9.1/tradingstrategy/client.py
+-rw-r--r--   0        0        0      206 2022-12-15 16:47:52.651033 trading_strategy-0.9.1/tradingstrategy/direct_feed/__init__.py
+-rw-r--r--   0        0        0     1691 2022-12-15 16:47:52.651188 trading_strategy-0.9.1/tradingstrategy/direct_feed/candle_feed.py
+-rw-r--r--   0        0        0     1575 2022-12-15 16:47:52.651356 trading_strategy-0.9.1/tradingstrategy/direct_feed/conversion.py
+-rw-r--r--   0        0        0      100 2022-12-15 16:47:52.651465 trading_strategy-0.9.1/tradingstrategy/direct_feed/dash.py
+-rw-r--r--   0        0        0      106 2022-12-15 16:47:52.651644 trading_strategy-0.9.1/tradingstrategy/direct_feed/direct_feed_pair.py
+-rw-r--r--   0        0        0     5533 2022-12-15 16:47:52.651794 trading_strategy-0.9.1/tradingstrategy/direct_feed/ohlcv_aggregate.py
+-rw-r--r--   0        0        0    10410 2022-12-15 16:47:52.652000 trading_strategy-0.9.1/tradingstrategy/direct_feed/reorg_mon.py
+-rw-r--r--   0        0        0     3953 2022-12-15 16:47:52.652135 trading_strategy-0.9.1/tradingstrategy/direct_feed/synthetic_feed.py
+-rw-r--r--   0        0        0     1041 2022-12-15 16:47:52.652313 trading_strategy-0.9.1/tradingstrategy/direct_feed/timeframe.py
+-rw-r--r--   0        0        0    13082 2022-12-15 16:47:52.652521 trading_strategy-0.9.1/tradingstrategy/direct_feed/trade_feed.py
+-rw-r--r--   0        0        0     1730 2022-12-15 16:47:52.652691 trading_strategy-0.9.1/tradingstrategy/direct_feed/trade_store.py
+-rw-r--r--   0        0        0    11381 2022-12-15 16:47:52.652898 trading_strategy-0.9.1/tradingstrategy/direct_feed/uniswap_v2.py
+-rw-r--r--   0        0        0      628 2022-12-15 16:47:52.653106 trading_strategy-0.9.1/tradingstrategy/direct_feed/warn.py
+-rw-r--r--   0        0        0     2400 2022-09-17 18:31:15.775681 trading_strategy-0.9.1/tradingstrategy/environment/base.py
+-rw-r--r--   0        0        0      204 2022-09-17 18:31:15.775735 trading_strategy-0.9.1/tradingstrategy/environment/colab.py
+-rw-r--r--   0        0        0      267 2022-09-17 18:31:15.775789 trading_strategy-0.9.1/tradingstrategy/environment/config.py
+-rw-r--r--   0        0        0        2 2022-09-17 18:31:15.775836 trading_strategy-0.9.1/tradingstrategy/environment/console.py
+-rw-r--r--   0        0        0        5 2022-09-17 18:31:15.775881 trading_strategy-0.9.1/tradingstrategy/environment/inpage.py
+-rw-r--r--   0        0        0     3279 2022-09-28 17:08:08.709965 trading_strategy-0.9.1/tradingstrategy/environment/interactive_setup.py
+-rw-r--r--   0        0        0     4840 2022-12-05 19:49:35.032041 trading_strategy-0.9.1/tradingstrategy/environment/jupyter.py
+-rw-r--r--   0        0        0     2017 2022-09-19 08:44:04.949683 trading_strategy-0.9.1/tradingstrategy/environment/jupyterlite.py
+-rw-r--r--   0        0        0        0 2022-09-17 18:31:15.776042 trading_strategy-0.9.1/tradingstrategy/environment/oracle.py
+-rw-r--r--   0        0        0     7474 2022-12-15 16:47:52.653693 trading_strategy-0.9.1/tradingstrategy/exchange.py
+-rw-r--r--   0        0        0     9077 2022-09-17 18:31:15.776244 trading_strategy-0.9.1/tradingstrategy/frameworks/backtrader.py
+-rw-r--r--   0        0        0      768 2022-09-17 18:31:15.776310 trading_strategy-0.9.1/tradingstrategy/frameworks/matplotlib.py
+-rw-r--r--   0        0        0    12252 2022-09-19 17:09:36.245411 trading_strategy-0.9.1/tradingstrategy/frameworks/qstrader.py
+-rw-r--r--   0        0        0     8579 2022-09-17 18:31:15.776498 trading_strategy-0.9.1/tradingstrategy/liquidity.py
+-rw-r--r--   0        0        0    40587 2022-11-26 12:17:28.842121 trading_strategy-0.9.1/tradingstrategy/pair.py
+-rw-r--r--   0        0        0     8389 2022-09-17 18:31:15.776809 trading_strategy-0.9.1/tradingstrategy/priceimpact.py
+-rw-r--r--   0        0        0     2024 2022-09-19 08:44:04.949935 trading_strategy-0.9.1/tradingstrategy/reader.py
+-rw-r--r--   0        0        0     1318 2022-09-17 18:31:15.776944 trading_strategy-0.9.1/tradingstrategy/stablecoin.py
+-rw-r--r--   0        0        0     3265 2022-09-17 18:31:15.777005 trading_strategy-0.9.1/tradingstrategy/timebucket.py
+-rw-r--r--   0        0        0     1182 2022-09-17 18:31:15.777069 trading_strategy-0.9.1/tradingstrategy/token.py
+-rw-r--r--   0        0        0     1046 2022-09-17 18:31:15.777154 trading_strategy-0.9.1/tradingstrategy/transport/base.py
+-rw-r--r--   0        0        0    12031 2022-11-19 14:28:56.206120 trading_strategy-0.9.1/tradingstrategy/transport/cache.py
+-rw-r--r--   0        0        0     7019 2022-12-05 19:49:18.944960 trading_strategy-0.9.1/tradingstrategy/transport/jsonl.py
+-rw-r--r--   0        0        0      503 2022-09-19 08:44:04.950008 trading_strategy-0.9.1/tradingstrategy/transport/pyodide.py
+-rw-r--r--   0        0        0     1767 2022-09-17 18:31:15.777399 trading_strategy-0.9.1/tradingstrategy/types.py
+-rw-r--r--   0        0        0     2144 2022-09-17 18:31:15.777468 trading_strategy-0.9.1/tradingstrategy/universe.py
+-rw-r--r--   0        0        0     1174 2022-09-17 18:31:15.777560 trading_strategy-0.9.1/tradingstrategy/utils/columnar.py
+-rw-r--r--   0        0        0      946 2022-09-17 18:31:15.777619 trading_strategy-0.9.1/tradingstrategy/utils/format.py
+-rw-r--r--   0        0        0    13678 2022-12-08 18:13:56.541607 trading_strategy-0.9.1/tradingstrategy/utils/groupeduniverse.py
+-rw-r--r--   0        0        0     3256 2022-11-19 14:28:56.206660 trading_strategy-0.9.1/tradingstrategy/utils/jupyter.py
+-rw-r--r--   0        0        0     3562 2022-09-17 18:31:15.777891 trading_strategy-0.9.1/tradingstrategy/utils/schema.py
+-rw-r--r--   0        0        0     2654 2022-12-15 16:47:52.654177 trading_strategy-0.9.1/tradingstrategy/utils/summarydataframe.py
+-rw-r--r--   0        0        0      901 2022-09-28 17:28:53.658400 trading_strategy-0.9.1/tradingstrategy/utils/time.py
+-rw-r--r--   0        0        0     7220 1970-01-01 00:00:00.000000 trading_strategy-0.9.1/setup.py
+-rw-r--r--   0        0        0     4931 1970-01-01 00:00:00.000000 trading_strategy-0.9.1/PKG-INFO
```

### Comparing `trading_strategy-0.9.0/LICENSE.txt` & `trading_strategy-0.9.1/LICENSE.txt`

 * *Files 9% similar despite different names*

```diff
@@ -1,8 +1,11 @@
-Capitalgram Python library
+Trading Strategy Python library
+
+Copyright (C) 2022 Market Software Ltd.
+
 Copyright (C) 2021 Mikko Ohtamaa
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 any later version.
```

### Comparing `trading_strategy-0.9.0/README.md` & `trading_strategy-0.9.1/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -47,21 +47,21 @@
 **Note**: Unless you are an experienced Python developer, [try the Binder cloud hosted Jupyter notebook examples first](https://tradingstrategy.ai/docs/programming/code-examples/index.html).
 
 You can install this package with 
 
 `poetry`:
 
 ```shell
-poetry add trading-strategy
+poetry add trading-strategy -E direct-feed
 ```
 
 `pip`:
 
 ```shell
-pip install trading-strategy 
+pip install "trading-strategy[direct-feed]" 
 ```
 
 # Documentation
 
 - [Read Trading Strategy documentation](https://tradingstrategy.ai/docs/).
 - [Documentation Github repository](https://github.com/tradingstrategy-ai/docs).
```

#### html2text {}

```diff
@@ -28,18 +28,19 @@
 decentralised exchange # Getting started See [the Getting Started tutorial]
 (https://tradingstrategy.ai/docs/programming/code-examples/getting-
 started.html) and the rest of the [Trading Strategy documentation](https://
 tradingstrategy.ai/docs/). # Prerequisites * Python 3.10 # Installing the
 package **Note**: Unless you are an experienced Python developer, [try the
 Binder cloud hosted Jupyter notebook examples first](https://
 tradingstrategy.ai/docs/programming/code-examples/index.html). You can install
-this package with `poetry`: ```shell poetry add trading-strategy ``` `pip`:
-```shell pip install trading-strategy ``` # Documentation - [Read Trading
-Strategy documentation](https://tradingstrategy.ai/docs/). - [Documentation
-Github repository](https://github.com/tradingstrategy-ai/docs). Community -----
----- * [Trading Strategy website](https://tradingstrategy.ai) * [Blog](https://
-tradingstrategy.ai/blog) * [Twitter](https://twitter.com/TradingProtocol) *
-[Discord](https://tradingstrategy.ai/community#discord) * [Telegram channel]
-(https://t.me/trading_protocol) * [Changelog and version history](https://
-github.com/tradingstrategy-ai/trading-strategy/blob/master/CHANGELOG.md) [Read
-more documentation how to develop this package](https://tradingstrategy.ai/
-docs/programming/development.html). # License GNU AGPL 3.0.
+this package with `poetry`: ```shell poetry add trading-strategy -E direct-feed
+``` `pip`: ```shell pip install "trading-strategy[direct-feed]" ``` #
+Documentation - [Read Trading Strategy documentation](https://
+tradingstrategy.ai/docs/). - [Documentation Github repository](https://
+github.com/tradingstrategy-ai/docs). Community --------- * [Trading Strategy
+website](https://tradingstrategy.ai) * [Blog](https://tradingstrategy.ai/blog)
+* [Twitter](https://twitter.com/TradingProtocol) * [Discord](https://
+tradingstrategy.ai/community#discord) * [Telegram channel](https://t.me/
+trading_protocol) * [Changelog and version history](https://github.com/
+tradingstrategy-ai/trading-strategy/blob/master/CHANGELOG.md) [Read more
+documentation how to develop this package](https://tradingstrategy.ai/docs/
+programming/development.html). # License GNU AGPL 3.0.
```

### Comparing `trading_strategy-0.9.0/pyproject.toml` & `trading_strategy-0.9.1/pyproject.toml`

 * *Files 23% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "trading-strategy"
-version = "0.9.0"
+version = "0.9.1"
 description = "DEX trading and blockchain quantitative finance data for Python"
 authors = ["Mikko Ohtamaa <mikko@tradingstrategy.ai>"]
 homepage = "https://tradingstrategy.ai"
 repository = "https://github.com/tradingstrategy-ai/trading-strategy"
 license = "AGPL"
 readme = "README.md"
 keywords = ["algorithmic trading", "ethereum", "cryptocurrency", "uniswap", "quantitative finance", "binance", "blockchain", "pancakeswap", "polygon", "web3"]
@@ -25,33 +25,42 @@
 requests = "^2.28.1"
 tqdm-loggable = "^0.1.2"
 
 # Legacy strategy and trading engines
 trading-strategy-qstrader = {version="^0.5.0", optional = true}
 scipy = {version="^1.6.1", optional = true}
 trading-strategy-backtrader = {version="^0.1",  optional = true}
+web3-ethereum-defi = {version = "0.11.3", extras = ["direct-feed"]}
 
 [tool.poetry.dev-dependencies]
 pytest = "7.1.3"
 ipdb = "^0.13.9"
 coloredlogs = "^15.0.1"
 
 memory-profiler = "^0.60.0"
 poetry-core = "^1.1.0"
 pytest-asyncio = "^0.19.0"
 
-# qstrader depends on Seaborn that depends on Scipy that is a problematic dependency
+
 [tool.poetry.extras]
+# Real-time OHLCV feeds over JSON-RPC
+direct-feed = ["web3-ethereum-defi"]
+
+# Legacy qstrader framework support
 qstrader = ["scipy", "trading-strategy-qstrader"]
+
+# Legacy backtrader framework support
 backtrader = ["trading-strategy-backtrader"]
 
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
-
 # https://docs.pytest.org/en/6.2.x/customize.html
 [tool.pytest.ini_options]
 testpaths = [
     "tests",
+]
+filterwarnings = [
+    "ignore::FutureWarning"
 ]
```

### Comparing `trading_strategy-0.9.0/tradingstrategy/analysis/portfolioanalyzer.py` & `trading_strategy-0.9.1/tradingstrategy/analysis/portfolioanalyzer.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/analysis/profitdistribution.py` & `trading_strategy-0.9.1/tradingstrategy/analysis/profitdistribution.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/analysis/tradeanalyzer.py` & `trading_strategy-0.9.1/tradingstrategy/analysis/tradeanalyzer.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/analysis/tradehint.py` & `trading_strategy-0.9.1/tradingstrategy/analysis/tradehint.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/caip.py` & `trading_strategy-0.9.1/tradingstrategy/caip.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/candle.py` & `trading_strategy-0.9.1/tradingstrategy/candle.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chain.py` & `trading_strategy-0.9.1/tradingstrategy/chain.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/.github/ISSUE_TEMPLATE/add-new-chain---network-id.md` & `trading_strategy-0.9.1/tradingstrategy/chains/.github/ISSUE_TEMPLATE/add-new-chain---network-id.md`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/.github/workflows/build_and_deploy.yml` & `trading_strategy-0.9.1/tradingstrategy/chains/.github/workflows/build_and_deploy.yml`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/LICENSE` & `trading_strategy-0.9.1/tradingstrategy/chains/LICENSE`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/README.md` & `trading_strategy-0.9.1/tradingstrategy/chains/README.md`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100001.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100001.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100002.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100002.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100003.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100003.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100004.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100004.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100005.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100005.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100006.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100006.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100007.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100007.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-100008.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-100008.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-106.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-106.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110001.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110001.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110002.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110002.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110003.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110003.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110004.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110004.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110005.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110005.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110006.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110006.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110007.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110007.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-110008.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-110008.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-128.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-128.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1285.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1285.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1313114.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1313114.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-137.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-137.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666600000.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666600000.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-1666700000.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-1666700000.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-19.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-19.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-201030.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-201030.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-210309.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-210309.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-246.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-246.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-250.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-250.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-269.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-269.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-28.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-28.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-288.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-288.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-3.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-3.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-30.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-30.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-311752642.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-311752642.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-322.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-322.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-336.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-336.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-338.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-338.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-363.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-363.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-364.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-364.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-365.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-365.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4002.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4002.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-42.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-42.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-42161.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-42161.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-421611.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-421611.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4216137055.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4216137055.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-42220.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-42220.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-43114.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-43114.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-44787.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-44787.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-4690.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-4690.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-55.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-55.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-56.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-56.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5700.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5700.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-58.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-58.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-5851.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-5851.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-60.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-60.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-61.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-61.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-62320.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-62320.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-65.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-65.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-66.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-66.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-77.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-77.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-80001.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-80001.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-8080.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-8080.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-85.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-85.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-86.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-86.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-9000.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-9000.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-955305.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-955305.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-97.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-97.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-99.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-99.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/_data/chains/eip155-998.json` & `trading_strategy-0.9.1/tradingstrategy/chains/_data/chains/eip155-998.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/build.gradle` & `trading_strategy-0.9.1/tradingstrategy/chains/build.gradle`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/gradle/wrapper/gradle-wrapper.jar` & `trading_strategy-0.9.1/tradingstrategy/chains/gradle/wrapper/gradle-wrapper.jar`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/gradlew` & `trading_strategy-0.9.1/tradingstrategy/chains/gradlew`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/gradlew.bat` & `trading_strategy-0.9.1/tradingstrategy/chains/gradlew.bat`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Env.kt` & `trading_strategy-0.9.1/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Env.kt`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Main.kt` & `trading_strategy-0.9.1/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/Main.kt`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/model/Exceptions.kt` & `trading_strategy-0.9.1/tradingstrategy/chains/src/main/kotlin/org/ethereum/lists/chains/model/Exceptions.kt`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/src/test/kotlin/org/ethereum/lists/chains/TheChainChecker.kt` & `trading_strategy-0.9.1/tradingstrategy/chains/src/test/kotlin/org/ethereum/lists/chains/TheChainChecker.kt`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/invalid/sameshortname/eip155-5.json` & `trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/invalid/sameshortname/eip155-5.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/chains/src/test/resources/test_chains/valid/eip155-5.json` & `trading_strategy-0.9.1/tradingstrategy/chains/src/test/resources/test_chains/valid/eip155-5.json`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/client.py` & `trading_strategy-0.9.1/tradingstrategy/client.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/environment/base.py` & `trading_strategy-0.9.1/tradingstrategy/environment/base.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/environment/interactive_setup.py` & `trading_strategy-0.9.1/tradingstrategy/environment/interactive_setup.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/environment/jupyter.py` & `trading_strategy-0.9.1/tradingstrategy/environment/jupyter.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/environment/jupyterlite.py` & `trading_strategy-0.9.1/tradingstrategy/environment/jupyterlite.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/exchange.py` & `trading_strategy-0.9.1/tradingstrategy/exchange.py`

 * *Files 5% similar despite different names*

```diff
@@ -25,14 +25,17 @@
     Note that each type can have multiple implementations.
     For example QuickSwap, Sushi and Pancake are all Uniswap v2 types.
     """
 
     #: Uniswap v2 style exchange
     uniswap_v2 = "uniswap_v2"
 
+    #: Uniswap v2 style exchange, but with incompatible implementation (e.g. Nomiswap Stable)
+    uniswap_v2_incompatible = "uniswap_v2_incompatible"
+
     #: Uniswap v3 style exchange
     uniswap_v3 = "uniswap_v3"
 
     # Uniswap v2 style exchange (same as above `uniswap_v2`)
     # NOTE: Do not use this member as it is deprecated and only kept for backward 
     # compatibility, it will be removed in the future
     _deprecated_uni_v2 = "uni_v2"
```

### Comparing `trading_strategy-0.9.0/tradingstrategy/frameworks/backtrader.py` & `trading_strategy-0.9.1/tradingstrategy/frameworks/backtrader.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/frameworks/matplotlib.py` & `trading_strategy-0.9.1/tradingstrategy/frameworks/matplotlib.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/frameworks/qstrader.py` & `trading_strategy-0.9.1/tradingstrategy/frameworks/qstrader.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/liquidity.py` & `trading_strategy-0.9.1/tradingstrategy/liquidity.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/pair.py` & `trading_strategy-0.9.1/tradingstrategy/pair.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/priceimpact.py` & `trading_strategy-0.9.1/tradingstrategy/priceimpact.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/reader.py` & `trading_strategy-0.9.1/tradingstrategy/reader.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/stablecoin.py` & `trading_strategy-0.9.1/tradingstrategy/stablecoin.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/timebucket.py` & `trading_strategy-0.9.1/tradingstrategy/timebucket.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/token.py` & `trading_strategy-0.9.1/tradingstrategy/token.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/transport/base.py` & `trading_strategy-0.9.1/tradingstrategy/transport/base.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/transport/cache.py` & `trading_strategy-0.9.1/tradingstrategy/transport/cache.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/transport/jsonl.py` & `trading_strategy-0.9.1/tradingstrategy/transport/jsonl.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/types.py` & `trading_strategy-0.9.1/tradingstrategy/types.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/universe.py` & `trading_strategy-0.9.1/tradingstrategy/universe.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/utils/columnar.py` & `trading_strategy-0.9.1/tradingstrategy/utils/columnar.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/utils/format.py` & `trading_strategy-0.9.1/tradingstrategy/utils/format.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/utils/groupeduniverse.py` & `trading_strategy-0.9.1/tradingstrategy/utils/groupeduniverse.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/utils/jupyter.py` & `trading_strategy-0.9.1/tradingstrategy/utils/jupyter.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/utils/schema.py` & `trading_strategy-0.9.1/tradingstrategy/utils/schema.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/tradingstrategy/utils/summarydataframe.py` & `trading_strategy-0.9.1/tradingstrategy/utils/summarydataframe.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,24 +11,27 @@
 
 class Format(enum.Enum):
     """Format different summary value cells."""
     integer = "int"
     percent = "percent"
     dollar = "dollar"
     duration = "duration"
+    num_bars = "num_bars"
 
     #: Value cannot be calculated, e.g division by zero
     missing = "missing"
 
 
+
 FORMATTERS = {
     Format.integer: "{v:.0f}",
     Format.percent: "{v:.2%}",
     Format.dollar: "${v:,.2f}",
     Format.duration: "{v.days} days",
+    Format.num_bars: "{v:.0f} bars",
     Format.missing: "-",
 }
 
 
 @dataclass
 class Value:
     v: object
@@ -50,20 +53,22 @@
     return Value(v, Format.percent)
 
 
 def as_duration(v: datetime.timedelta) -> Value:
     """Format value as a duration"""
     return Value(v, Format.duration)
 
+def as_bars(v: float) -> Value:
+    """Format value as number of bars"""
+    return Value(v, Format.num_bars)
 
 def as_missing() -> Value:
     """Format a missing value e.g. because of division by zero"""
     return Value(None, Format.missing)
 
-
 def format_value(v_instance: Value) -> str:
     assert isinstance(v_instance, Value), f"Expected Value instance, got {v_instance}"
     formatter = FORMATTERS[v_instance.format]
     if v_instance.v is not None:
         # TODO: Remove the hack
         if isinstance(v_instance.v, datetime.timedelta):
             return formatter.format(v=v_instance.v)
```

### Comparing `trading_strategy-0.9.0/tradingstrategy/utils/time.py` & `trading_strategy-0.9.1/tradingstrategy/utils/time.py`

 * *Files identical despite different names*

### Comparing `trading_strategy-0.9.0/setup.py` & `trading_strategy-0.9.1/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
 packages = \
 ['tradingstrategy',
  'tradingstrategy.analysis',
  'tradingstrategy.charting',
+ 'tradingstrategy.direct_feed',
  'tradingstrategy.environment',
  'tradingstrategy.frameworks',
  'tradingstrategy.transport',
  'tradingstrategy.utils']
 
 package_data = \
 {'': ['*'],
@@ -50,22 +51,23 @@
  'plotly>=5.1.0,<6.0.0',
  'pyarrow>=7.0.0,<8.0.0',
  'requests>=2.28.1,<3.0.0',
  'tqdm-loggable>=0.1.2,<0.2.0',
  'tqdm>=4.61.2,<5.0.0']
 
 extras_require = \
-{'backtrader': ['trading-strategy-backtrader>=0.1,<0.2'],
+{':extra == "direct-feed"': ['web3-ethereum-defi[direct-feed]==0.11.3'],
+ 'backtrader': ['trading-strategy-backtrader>=0.1,<0.2'],
  'qstrader': ['trading-strategy-qstrader>=0.5.0,<0.6.0', 'scipy>=1.6.1,<2.0.0']}
 
 setup_kwargs = {
     'name': 'trading-strategy',
-    'version': '0.9.0',
+    'version': '0.9.1',
     'description': 'DEX trading and blockchain quantitative finance data for Python',
-    'long_description': '[![CI Status](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-app.yml/badge.svg)](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-app.yml)\n\n[![pip installation works](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-install.yml/badge.svg)](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-install.yml)\n\n<a href="https://tradingstrategy.ai">\n  <img src="https://raw.githubusercontent.com/tradingstrategy-ai/trading-strategy/master/logo.svg" width="384">\n</a>\n\n# Trading Strategy framework for Python\n\nTrading Strategy framework is a Python framework for algorithmic trading on decentralised exchanges. \nIt is using [backtesting data](https://tradingstrategy.ai/trading-view/backtesting) and [real-time price feeds](https://tradingstrategy.ai/trading-view)\nfrom [Trading Strategy Protocol](https://tradingstrategy.ai/). \n\n# Use cases\n\n* Analyse cryptocurrency investment opportunities on [decentralised exchanges (DEXes)](https://tradingstrategy.ai/trading-view/exchanges)\n\n* Creating trading algorithms and trading bots that trade on DEXes\n\n* Deploy trading strategies as on-chain smart contracts where users can invest and withdraw with their wallets\n\n# Features\n\n* Supports multiple blockchains like [Ethereum mainnet](https://tradingstrategy.ai/trading-view/ethereum), \n  [Binance Smart Chain](https://tradingstrategy.ai/trading-view/binance) and \n  [Polygon](https://tradingstrategy.ai/trading-view/polygon)\n\n* Access trading data from on-chain decentralised exchanges like\n  [SushiSwap](https://tradingstrategy.ai/trading-view/ethereum/sushi), [QuickSwap](https://tradingstrategy.ai/trading-view/polygon/quickswap) and [PancakeSwap](https://tradingstrategy.ai/trading-view/binance/pancakeswap-v2)\n\n* Integration with Jupyter Notebook for easy manipulation of data.\n  See [example notebooks](https://tradingstrategy.ai/docs/programming/code-examples/index.html).\n\n* Write [algorithmic trading strategies](https://tradingstrategy.ai/docs/programming/strategy-examples/index.html) for  decentralised exchange \n\n# Getting started \n\nSee [the Getting Started tutorial](https://tradingstrategy.ai/docs/programming/code-examples/getting-started.html) and the rest of the [Trading Strategy documentation](https://tradingstrategy.ai/docs/).\n\n# Prerequisites\n\n* Python 3.10\n\n# Installing the package\n\n**Note**: Unless you are an experienced Python developer, [try the Binder cloud hosted Jupyter notebook examples first](https://tradingstrategy.ai/docs/programming/code-examples/index.html).\n\nYou can install this package with \n\n`poetry`:\n\n```shell\npoetry add trading-strategy\n```\n\n`pip`:\n\n```shell\npip install trading-strategy \n```\n\n# Documentation\n\n- [Read Trading Strategy documentation](https://tradingstrategy.ai/docs/).\n- [Documentation Github repository](https://github.com/tradingstrategy-ai/docs).\n\nCommunity\n---------\n\n* [Trading Strategy website](https://tradingstrategy.ai)\n\n* [Blog](https://tradingstrategy.ai/blog)\n\n* [Twitter](https://twitter.com/TradingProtocol)\n\n* [Discord](https://tradingstrategy.ai/community#discord) \n\n* [Telegram channel](https://t.me/trading_protocol)\n\n* [Changelog and version history](https://github.com/tradingstrategy-ai/trading-strategy/blob/master/CHANGELOG.md)\n\n[Read more documentation how to develop this package](https://tradingstrategy.ai/docs/programming/development.html).\n\n# License\n\nGNU AGPL 3.0. \n',
+    'long_description': '[![CI Status](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-app.yml/badge.svg)](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-app.yml)\n\n[![pip installation works](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-install.yml/badge.svg)](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-install.yml)\n\n<a href="https://tradingstrategy.ai">\n  <img src="https://raw.githubusercontent.com/tradingstrategy-ai/trading-strategy/master/logo.svg" width="384">\n</a>\n\n# Trading Strategy framework for Python\n\nTrading Strategy framework is a Python framework for algorithmic trading on decentralised exchanges. \nIt is using [backtesting data](https://tradingstrategy.ai/trading-view/backtesting) and [real-time price feeds](https://tradingstrategy.ai/trading-view)\nfrom [Trading Strategy Protocol](https://tradingstrategy.ai/). \n\n# Use cases\n\n* Analyse cryptocurrency investment opportunities on [decentralised exchanges (DEXes)](https://tradingstrategy.ai/trading-view/exchanges)\n\n* Creating trading algorithms and trading bots that trade on DEXes\n\n* Deploy trading strategies as on-chain smart contracts where users can invest and withdraw with their wallets\n\n# Features\n\n* Supports multiple blockchains like [Ethereum mainnet](https://tradingstrategy.ai/trading-view/ethereum), \n  [Binance Smart Chain](https://tradingstrategy.ai/trading-view/binance) and \n  [Polygon](https://tradingstrategy.ai/trading-view/polygon)\n\n* Access trading data from on-chain decentralised exchanges like\n  [SushiSwap](https://tradingstrategy.ai/trading-view/ethereum/sushi), [QuickSwap](https://tradingstrategy.ai/trading-view/polygon/quickswap) and [PancakeSwap](https://tradingstrategy.ai/trading-view/binance/pancakeswap-v2)\n\n* Integration with Jupyter Notebook for easy manipulation of data.\n  See [example notebooks](https://tradingstrategy.ai/docs/programming/code-examples/index.html).\n\n* Write [algorithmic trading strategies](https://tradingstrategy.ai/docs/programming/strategy-examples/index.html) for  decentralised exchange \n\n# Getting started \n\nSee [the Getting Started tutorial](https://tradingstrategy.ai/docs/programming/code-examples/getting-started.html) and the rest of the [Trading Strategy documentation](https://tradingstrategy.ai/docs/).\n\n# Prerequisites\n\n* Python 3.10\n\n# Installing the package\n\n**Note**: Unless you are an experienced Python developer, [try the Binder cloud hosted Jupyter notebook examples first](https://tradingstrategy.ai/docs/programming/code-examples/index.html).\n\nYou can install this package with \n\n`poetry`:\n\n```shell\npoetry add trading-strategy -E direct-feed\n```\n\n`pip`:\n\n```shell\npip install "trading-strategy[direct-feed]" \n```\n\n# Documentation\n\n- [Read Trading Strategy documentation](https://tradingstrategy.ai/docs/).\n- [Documentation Github repository](https://github.com/tradingstrategy-ai/docs).\n\nCommunity\n---------\n\n* [Trading Strategy website](https://tradingstrategy.ai)\n\n* [Blog](https://tradingstrategy.ai/blog)\n\n* [Twitter](https://twitter.com/TradingProtocol)\n\n* [Discord](https://tradingstrategy.ai/community#discord) \n\n* [Telegram channel](https://t.me/trading_protocol)\n\n* [Changelog and version history](https://github.com/tradingstrategy-ai/trading-strategy/blob/master/CHANGELOG.md)\n\n[Read more documentation how to develop this package](https://tradingstrategy.ai/docs/programming/development.html).\n\n# License\n\nGNU AGPL 3.0. \n',
     'author': 'Mikko Ohtamaa',
     'author_email': 'mikko@tradingstrategy.ai',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://tradingstrategy.ai',
     'packages': packages,
     'package_data': package_data,
```

#### html2text {}

```diff
@@ -1,78 +1,80 @@
 # -*- coding: utf-8 -*- from setuptools import setup packages = \
 ['tradingstrategy', 'tradingstrategy.analysis', 'tradingstrategy.charting',
-'tradingstrategy.environment', 'tradingstrategy.frameworks',
-'tradingstrategy.transport', 'tradingstrategy.utils'] package_data = \ {'':
-['*'], 'tradingstrategy': ['chains/*', 'chains/.ci/*', 'chains/.github/*',
-'chains/.github/ISSUE_TEMPLATE/*', 'chains/.github/workflows/*', 'chains/_data/
-chains/*', 'chains/_data/chains/deprecated/*', 'chains/_data/icons/*', 'chains/
-gradle/wrapper/*', 'chains/src/main/kotlin/org/ethereum/lists/chains/*',
-'chains/src/main/kotlin/org/ethereum/lists/chains/model/*', 'chains/src/test/
-kotlin/org/ethereum/lists/chains/*', 'chains/src/test/resources/test_chains/
-invalid/*', 'chains/src/test/resources/test_chains/invalid/explorerinvalidurl/
-*', 'chains/src/test/resources/test_chains/invalid/explorermissingurl/*',
-'chains/src/test/resources/test_chains/invalid/explorernoname/*', 'chains/src/
-test/resources/test_chains/invalid/explorersnotarray/*', 'chains/src/test/
-resources/test_chains/invalid/sameshortname/*', 'chains/src/test/resources/
-test_chains/invalid/withparentchaindoesnotexist/*', 'chains/src/test/resources/
-test_chains/invalid/withparentextrabridgeelementnoobject/*', 'chains/src/test/
-resources/test_chains/invalid/withparentextrabridgesfield/*', 'chains/src/test/
-resources/test_chains/invalid/withparentextrabridgesnoarray/*', 'chains/src/
-test/resources/test_chains/invalid/withparentextrafield/*', 'chains/src/test/
+'tradingstrategy.direct_feed', 'tradingstrategy.environment',
+'tradingstrategy.frameworks', 'tradingstrategy.transport',
+'tradingstrategy.utils'] package_data = \ {'': ['*'], 'tradingstrategy':
+['chains/*', 'chains/.ci/*', 'chains/.github/*', 'chains/.github/
+ISSUE_TEMPLATE/*', 'chains/.github/workflows/*', 'chains/_data/chains/*',
+'chains/_data/chains/deprecated/*', 'chains/_data/icons/*', 'chains/gradle/
+wrapper/*', 'chains/src/main/kotlin/org/ethereum/lists/chains/*', 'chains/src/
+main/kotlin/org/ethereum/lists/chains/model/*', 'chains/src/test/kotlin/org/
+ethereum/lists/chains/*', 'chains/src/test/resources/test_chains/invalid/*',
+'chains/src/test/resources/test_chains/invalid/explorerinvalidurl/*', 'chains/
+src/test/resources/test_chains/invalid/explorermissingurl/*', 'chains/src/test/
+resources/test_chains/invalid/explorernoname/*', 'chains/src/test/resources/
+test_chains/invalid/explorersnotarray/*', 'chains/src/test/resources/
+test_chains/invalid/sameshortname/*', 'chains/src/test/resources/test_chains/
+invalid/withparentchaindoesnotexist/*', 'chains/src/test/resources/test_chains/
+invalid/withparentextrabridgeelementnoobject/*', 'chains/src/test/resources/
+test_chains/invalid/withparentextrabridgesfield/*', 'chains/src/test/resources/
+test_chains/invalid/withparentextrabridgesnoarray/*', 'chains/src/test/
+resources/test_chains/invalid/withparentextrafield/*', 'chains/src/test/
 resources/test_chains/invalid/withparentinvalidtype/*', 'chains/src/test/
 resources/test_chains/invalid/withparentnobject/*', 'chains/src/test/resources/
 test_chains/invalid/wrongexplorerstandard/*', 'chains/src/test/resources/
 test_chains/valid/*', 'chains/src/test/resources/test_chains/valid/
 withexplorer/*', 'chains/src/test/resources/test_chains/valid/withparent/*',
 'chains/src/test/resources/test_chains/valid/withparentbridge/*']}
 install_requires = \ ['dataclasses-json>=0.5.4,<0.6.0',
 'jsonlines>=3.1.0,<4.0.0', 'pandas>=1.3.5,<2.0.0', 'plotly>=5.1.0,<6.0.0',
 'pyarrow>=7.0.0,<8.0.0', 'requests>=2.28.1,<3.0.0', 'tqdm-
-loggable>=0.1.2,<0.2.0', 'tqdm>=4.61.2,<5.0.0'] extras_require = \
-{'backtrader': ['trading-strategy-backtrader>=0.1,<0.2'], 'qstrader':
-['trading-strategy-qstrader>=0.5.0,<0.6.0', 'scipy>=1.6.1,<2.0.0']}
-setup_kwargs = { 'name': 'trading-strategy', 'version': '0.9.0', 'description':
-'DEX trading and blockchain quantitative finance data for Python',
-'long_description': '[![CI Status](https://github.com/tradingstrategy-ai/
-trading-strategy/actions/workflows/python-app.yml/badge.svg)](https://
-github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-
-app.yml)\n\n[![pip installation works](https://github.com/tradingstrategy-ai/
-trading-strategy/actions/workflows/pip-install.yml/badge.svg)](https://
-github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-
-install.yml)\n\n\n_[https://raw.githubusercontent.com/tradingstrategy-ai/
-trading-strategy/master/logo.svg]\n\n\n# Trading Strategy framework for
-Python\n\nTrading Strategy framework is a Python framework for algorithmic
-trading on decentralised exchanges. \nIt is using [backtesting data](https://
-tradingstrategy.ai/trading-view/backtesting) and [real-time price feeds](https:
-//tradingstrategy.ai/trading-view)\nfrom [Trading Strategy Protocol](https://
-tradingstrategy.ai/). \n\n# Use cases\n\n* Analyse cryptocurrency investment
-opportunities on [decentralised exchanges (DEXes)](https://tradingstrategy.ai/
-trading-view/exchanges)\n\n* Creating trading algorithms and trading bots that
-trade on DEXes\n\n* Deploy trading strategies as on-chain smart contracts where
-users can invest and withdraw with their wallets\n\n# Features\n\n* Supports
-multiple blockchains like [Ethereum mainnet](https://tradingstrategy.ai/
-trading-view/ethereum), \n [Binance Smart Chain](https://tradingstrategy.ai/
-trading-view/binance) and \n [Polygon](https://tradingstrategy.ai/trading-view/
-polygon)\n\n* Access trading data from on-chain decentralised exchanges like\n
-[SushiSwap](https://tradingstrategy.ai/trading-view/ethereum/sushi),
-[QuickSwap](https://tradingstrategy.ai/trading-view/polygon/quickswap) and
-[PancakeSwap](https://tradingstrategy.ai/trading-view/binance/pancakeswap-
-v2)\n\n* Integration with Jupyter Notebook for easy manipulation of data.\n See
-[example notebooks](https://tradingstrategy.ai/docs/programming/code-examples/
-index.html).\n\n* Write [algorithmic trading strategies](https://
-tradingstrategy.ai/docs/programming/strategy-examples/index.html) for
-decentralised exchange \n\n# Getting started \n\nSee [the Getting Started
-tutorial](https://tradingstrategy.ai/docs/programming/code-examples/getting-
-started.html) and the rest of the [Trading Strategy documentation](https://
-tradingstrategy.ai/docs/).\n\n# Prerequisites\n\n* Python 3.10\n\n# Installing
-the package\n\n**Note**: Unless you are an experienced Python developer, [try
-the Binder cloud hosted Jupyter notebook examples first](https://
-tradingstrategy.ai/docs/programming/code-examples/index.html).\n\nYou can
-install this package with \n\n`poetry`:\n\n```shell\npoetry add trading-
-strategy\n```\n\n`pip`:\n\n```shell\npip install trading-strategy \n```\n\n#
+loggable>=0.1.2,<0.2.0', 'tqdm>=4.61.2,<5.0.0'] extras_require = \ {':extra ==
+"direct-feed"': ['web3-ethereum-defi[direct-feed]==0.11.3'], 'backtrader':
+['trading-strategy-backtrader>=0.1,<0.2'], 'qstrader': ['trading-strategy-
+qstrader>=0.5.0,<0.6.0', 'scipy>=1.6.1,<2.0.0']} setup_kwargs = { 'name':
+'trading-strategy', 'version': '0.9.1', 'description': 'DEX trading and
+blockchain quantitative finance data for Python', 'long_description': '[![CI
+Status](https://github.com/tradingstrategy-ai/trading-strategy/actions/
+workflows/python-app.yml/badge.svg)](https://github.com/tradingstrategy-ai/
+trading-strategy/actions/workflows/python-app.yml)\n\n[![pip installation
+works](https://github.com/tradingstrategy-ai/trading-strategy/actions/
+workflows/pip-install.yml/badge.svg)](https://github.com/tradingstrategy-ai/
+trading-strategy/actions/workflows/pip-install.yml)\n\n\n_[https://
+raw.githubusercontent.com/tradingstrategy-ai/trading-strategy/master/
+logo.svg]\n\n\n# Trading Strategy framework for Python\n\nTrading Strategy
+framework is a Python framework for algorithmic trading on decentralised
+exchanges. \nIt is using [backtesting data](https://tradingstrategy.ai/trading-
+view/backtesting) and [real-time price feeds](https://tradingstrategy.ai/
+trading-view)\nfrom [Trading Strategy Protocol](https://tradingstrategy.ai/).
+\n\n# Use cases\n\n* Analyse cryptocurrency investment opportunities on
+[decentralised exchanges (DEXes)](https://tradingstrategy.ai/trading-view/
+exchanges)\n\n* Creating trading algorithms and trading bots that trade on
+DEXes\n\n* Deploy trading strategies as on-chain smart contracts where users
+can invest and withdraw with their wallets\n\n# Features\n\n* Supports multiple
+blockchains like [Ethereum mainnet](https://tradingstrategy.ai/trading-view/
+ethereum), \n [Binance Smart Chain](https://tradingstrategy.ai/trading-view/
+binance) and \n [Polygon](https://tradingstrategy.ai/trading-view/polygon)\n\n*
+Access trading data from on-chain decentralised exchanges like\n [SushiSwap]
+(https://tradingstrategy.ai/trading-view/ethereum/sushi), [QuickSwap](https://
+tradingstrategy.ai/trading-view/polygon/quickswap) and [PancakeSwap](https://
+tradingstrategy.ai/trading-view/binance/pancakeswap-v2)\n\n* Integration with
+Jupyter Notebook for easy manipulation of data.\n See [example notebooks]
+(https://tradingstrategy.ai/docs/programming/code-examples/index.html).\n\n*
+Write [algorithmic trading strategies](https://tradingstrategy.ai/docs/
+programming/strategy-examples/index.html) for decentralised exchange \n\n#
+Getting started \n\nSee [the Getting Started tutorial](https://
+tradingstrategy.ai/docs/programming/code-examples/getting-started.html) and the
+rest of the [Trading Strategy documentation](https://tradingstrategy.ai/docs/
+).\n\n# Prerequisites\n\n* Python 3.10\n\n# Installing the package\n\n**Note**:
+Unless you are an experienced Python developer, [try the Binder cloud hosted
+Jupyter notebook examples first](https://tradingstrategy.ai/docs/programming/
+code-examples/index.html).\n\nYou can install this package with \n\n`poetry`:
+\n\n```shell\npoetry add trading-strategy -E direct-feed\n```\n\n`pip`:
+\n\n```shell\npip install "trading-strategy[direct-feed]" \n```\n\n#
 Documentation\n\n- [Read Trading Strategy documentation](https://
 tradingstrategy.ai/docs/).\n- [Documentation Github repository](https://
 github.com/tradingstrategy-ai/docs).\n\nCommunity\n---------\n\n* [Trading
 Strategy website](https://tradingstrategy.ai)\n\n* [Blog](https://
 tradingstrategy.ai/blog)\n\n* [Twitter](https://twitter.com/
 TradingProtocol)\n\n* [Discord](https://tradingstrategy.ai/community#discord)
 \n\n* [Telegram channel](https://t.me/trading_protocol)\n\n* [Changelog and
```

### Comparing `trading_strategy-0.9.0/PKG-INFO` & `trading_strategy-0.9.1/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,34 +1,36 @@
 Metadata-Version: 2.1
 Name: trading-strategy
-Version: 0.9.0
+Version: 0.9.1
 Summary: DEX trading and blockchain quantitative finance data for Python
 Home-page: https://tradingstrategy.ai
 License: AGPL
 Keywords: algorithmic trading,ethereum,cryptocurrency,uniswap,quantitative finance,binance,blockchain,pancakeswap,polygon,web3
 Author: Mikko Ohtamaa
 Author-email: mikko@tradingstrategy.ai
 Requires-Python: >=3.10,<4
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Provides-Extra: backtrader
+Provides-Extra: direct-feed
 Provides-Extra: qstrader
 Requires-Dist: dataclasses-json (>=0.5.4,<0.6.0)
 Requires-Dist: jsonlines (>=3.1.0,<4.0.0)
 Requires-Dist: pandas (>=1.3.5,<2.0.0)
 Requires-Dist: plotly (>=5.1.0,<6.0.0)
 Requires-Dist: pyarrow (>=7.0.0,<8.0.0)
 Requires-Dist: requests (>=2.28.1,<3.0.0)
 Requires-Dist: scipy (>=1.6.1,<2.0.0); extra == "qstrader"
 Requires-Dist: tqdm (>=4.61.2,<5.0.0)
 Requires-Dist: tqdm-loggable (>=0.1.2,<0.2.0)
 Requires-Dist: trading-strategy-backtrader (>=0.1,<0.2); extra == "backtrader"
 Requires-Dist: trading-strategy-qstrader (>=0.5.0,<0.6.0); extra == "qstrader"
+Requires-Dist: web3-ethereum-defi[direct-feed] (==0.11.3); extra == "direct-feed"
 Project-URL: Repository, https://github.com/tradingstrategy-ai/trading-strategy
 Description-Content-Type: text/markdown
 
 [![CI Status](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-app.yml/badge.svg)](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-app.yml)
 
 [![pip installation works](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-install.yml/badge.svg)](https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-install.yml)
 
@@ -77,21 +79,21 @@
 **Note**: Unless you are an experienced Python developer, [try the Binder cloud hosted Jupyter notebook examples first](https://tradingstrategy.ai/docs/programming/code-examples/index.html).
 
 You can install this package with 
 
 `poetry`:
 
 ```shell
-poetry add trading-strategy
+poetry add trading-strategy -E direct-feed
 ```
 
 `pip`:
 
 ```shell
-pip install trading-strategy 
+pip install "trading-strategy[direct-feed]" 
 ```
 
 # Documentation
 
 - [Read Trading Strategy documentation](https://tradingstrategy.ai/docs/).
 - [Documentation Github repository](https://github.com/tradingstrategy-ai/docs).
```

#### html2text {}

```diff
@@ -1,63 +1,65 @@
-Metadata-Version: 2.1 Name: trading-strategy Version: 0.9.0 Summary: DEX
+Metadata-Version: 2.1 Name: trading-strategy Version: 0.9.1 Summary: DEX
 trading and blockchain quantitative finance data for Python Home-page: https://
 tradingstrategy.ai License: AGPL Keywords: algorithmic
 trading,ethereum,cryptocurrency,uniswap,quantitative
 finance,binance,blockchain,pancakeswap,polygon,web3 Author: Mikko Ohtamaa
 Author-email: mikko@tradingstrategy.ai Requires-Python: >=3.10,<4 Classifier:
 License :: Other/Proprietary License Classifier: Programming Language :: Python
 :: 3 Classifier: Programming Language :: Python :: 3.10 Classifier: Programming
-Language :: Python :: 3.11 Provides-Extra: backtrader Provides-Extra: qstrader
-Requires-Dist: dataclasses-json (>=0.5.4,<0.6.0) Requires-Dist: jsonlines
-(>=3.1.0,<4.0.0) Requires-Dist: pandas (>=1.3.5,<2.0.0) Requires-Dist: plotly
-(>=5.1.0,<6.0.0) Requires-Dist: pyarrow (>=7.0.0,<8.0.0) Requires-Dist:
-requests (>=2.28.1,<3.0.0) Requires-Dist: scipy (>=1.6.1,<2.0.0); extra ==
-"qstrader" Requires-Dist: tqdm (>=4.61.2,<5.0.0) Requires-Dist: tqdm-loggable
-(>=0.1.2,<0.2.0) Requires-Dist: trading-strategy-backtrader (>=0.1,<0.2); extra
-== "backtrader" Requires-Dist: trading-strategy-qstrader (>=0.5.0,<0.6.0);
-extra == "qstrader" Project-URL: Repository, https://github.com/
-tradingstrategy-ai/trading-strategy Description-Content-Type: text/markdown [!
-[CI Status](https://github.com/tradingstrategy-ai/trading-strategy/actions/
-workflows/python-app.yml/badge.svg)](https://github.com/tradingstrategy-ai/
-trading-strategy/actions/workflows/python-app.yml) [![pip installation works]
-(https://github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-
-install.yml/badge.svg)](https://github.com/tradingstrategy-ai/trading-strategy/
-actions/workflows/pip-install.yml) [https://raw.githubusercontent.com/
-tradingstrategy-ai/trading-strategy/master/logo.svg] # Trading Strategy
-framework for Python Trading Strategy framework is a Python framework for
-algorithmic trading on decentralised exchanges. It is using [backtesting data]
-(https://tradingstrategy.ai/trading-view/backtesting) and [real-time price
-feeds](https://tradingstrategy.ai/trading-view) from [Trading Strategy
-Protocol](https://tradingstrategy.ai/). # Use cases * Analyse cryptocurrency
-investment opportunities on [decentralised exchanges (DEXes)](https://
-tradingstrategy.ai/trading-view/exchanges) * Creating trading algorithms and
-trading bots that trade on DEXes * Deploy trading strategies as on-chain smart
-contracts where users can invest and withdraw with their wallets # Features *
-Supports multiple blockchains like [Ethereum mainnet](https://
-tradingstrategy.ai/trading-view/ethereum), [Binance Smart Chain](https://
-tradingstrategy.ai/trading-view/binance) and [Polygon](https://
-tradingstrategy.ai/trading-view/polygon) * Access trading data from on-chain
-decentralised exchanges like [SushiSwap](https://tradingstrategy.ai/trading-
-view/ethereum/sushi), [QuickSwap](https://tradingstrategy.ai/trading-view/
-polygon/quickswap) and [PancakeSwap](https://tradingstrategy.ai/trading-view/
-binance/pancakeswap-v2) * Integration with Jupyter Notebook for easy
-manipulation of data. See [example notebooks](https://tradingstrategy.ai/docs/
-programming/code-examples/index.html). * Write [algorithmic trading strategies]
-(https://tradingstrategy.ai/docs/programming/strategy-examples/index.html) for
-decentralised exchange # Getting started See [the Getting Started tutorial]
-(https://tradingstrategy.ai/docs/programming/code-examples/getting-
-started.html) and the rest of the [Trading Strategy documentation](https://
-tradingstrategy.ai/docs/). # Prerequisites * Python 3.10 # Installing the
-package **Note**: Unless you are an experienced Python developer, [try the
-Binder cloud hosted Jupyter notebook examples first](https://
-tradingstrategy.ai/docs/programming/code-examples/index.html). You can install
-this package with `poetry`: ```shell poetry add trading-strategy ``` `pip`:
-```shell pip install trading-strategy ``` # Documentation - [Read Trading
-Strategy documentation](https://tradingstrategy.ai/docs/). - [Documentation
-Github repository](https://github.com/tradingstrategy-ai/docs). Community -----
----- * [Trading Strategy website](https://tradingstrategy.ai) * [Blog](https://
-tradingstrategy.ai/blog) * [Twitter](https://twitter.com/TradingProtocol) *
-[Discord](https://tradingstrategy.ai/community#discord) * [Telegram channel]
-(https://t.me/trading_protocol) * [Changelog and version history](https://
-github.com/tradingstrategy-ai/trading-strategy/blob/master/CHANGELOG.md) [Read
-more documentation how to develop this package](https://tradingstrategy.ai/
-docs/programming/development.html). # License GNU AGPL 3.0.
+Language :: Python :: 3.11 Provides-Extra: backtrader Provides-Extra: direct-
+feed Provides-Extra: qstrader Requires-Dist: dataclasses-json (>=0.5.4,<0.6.0)
+Requires-Dist: jsonlines (>=3.1.0,<4.0.0) Requires-Dist: pandas
+(>=1.3.5,<2.0.0) Requires-Dist: plotly (>=5.1.0,<6.0.0) Requires-Dist: pyarrow
+(>=7.0.0,<8.0.0) Requires-Dist: requests (>=2.28.1,<3.0.0) Requires-Dist: scipy
+(>=1.6.1,<2.0.0); extra == "qstrader" Requires-Dist: tqdm (>=4.61.2,<5.0.0)
+Requires-Dist: tqdm-loggable (>=0.1.2,<0.2.0) Requires-Dist: trading-strategy-
+backtrader (>=0.1,<0.2); extra == "backtrader" Requires-Dist: trading-strategy-
+qstrader (>=0.5.0,<0.6.0); extra == "qstrader" Requires-Dist: web3-ethereum-
+defi[direct-feed] (==0.11.3); extra == "direct-feed" Project-URL: Repository,
+https://github.com/tradingstrategy-ai/trading-strategy Description-Content-
+Type: text/markdown [![CI Status](https://github.com/tradingstrategy-ai/
+trading-strategy/actions/workflows/python-app.yml/badge.svg)](https://
+github.com/tradingstrategy-ai/trading-strategy/actions/workflows/python-
+app.yml) [![pip installation works](https://github.com/tradingstrategy-ai/
+trading-strategy/actions/workflows/pip-install.yml/badge.svg)](https://
+github.com/tradingstrategy-ai/trading-strategy/actions/workflows/pip-
+install.yml) [https://raw.githubusercontent.com/tradingstrategy-ai/trading-
+strategy/master/logo.svg] # Trading Strategy framework for Python Trading
+Strategy framework is a Python framework for algorithmic trading on
+decentralised exchanges. It is using [backtesting data](https://
+tradingstrategy.ai/trading-view/backtesting) and [real-time price feeds](https:
+//tradingstrategy.ai/trading-view) from [Trading Strategy Protocol](https://
+tradingstrategy.ai/). # Use cases * Analyse cryptocurrency investment
+opportunities on [decentralised exchanges (DEXes)](https://tradingstrategy.ai/
+trading-view/exchanges) * Creating trading algorithms and trading bots that
+trade on DEXes * Deploy trading strategies as on-chain smart contracts where
+users can invest and withdraw with their wallets # Features * Supports multiple
+blockchains like [Ethereum mainnet](https://tradingstrategy.ai/trading-view/
+ethereum), [Binance Smart Chain](https://tradingstrategy.ai/trading-view/
+binance) and [Polygon](https://tradingstrategy.ai/trading-view/polygon) *
+Access trading data from on-chain decentralised exchanges like [SushiSwap]
+(https://tradingstrategy.ai/trading-view/ethereum/sushi), [QuickSwap](https://
+tradingstrategy.ai/trading-view/polygon/quickswap) and [PancakeSwap](https://
+tradingstrategy.ai/trading-view/binance/pancakeswap-v2) * Integration with
+Jupyter Notebook for easy manipulation of data. See [example notebooks](https:/
+/tradingstrategy.ai/docs/programming/code-examples/index.html). * Write
+[algorithmic trading strategies](https://tradingstrategy.ai/docs/programming/
+strategy-examples/index.html) for decentralised exchange # Getting started See
+[the Getting Started tutorial](https://tradingstrategy.ai/docs/programming/
+code-examples/getting-started.html) and the rest of the [Trading Strategy
+documentation](https://tradingstrategy.ai/docs/). # Prerequisites * Python 3.10
+# Installing the package **Note**: Unless you are an experienced Python
+developer, [try the Binder cloud hosted Jupyter notebook examples first](https:
+//tradingstrategy.ai/docs/programming/code-examples/index.html). You can
+install this package with `poetry`: ```shell poetry add trading-strategy -
+E direct-feed ``` `pip`: ```shell pip install "trading-strategy[direct-feed]"
+``` # Documentation - [Read Trading Strategy documentation](https://
+tradingstrategy.ai/docs/). - [Documentation Github repository](https://
+github.com/tradingstrategy-ai/docs). Community --------- * [Trading Strategy
+website](https://tradingstrategy.ai) * [Blog](https://tradingstrategy.ai/blog)
+* [Twitter](https://twitter.com/TradingProtocol) * [Discord](https://
+tradingstrategy.ai/community#discord) * [Telegram channel](https://t.me/
+trading_protocol) * [Changelog and version history](https://github.com/
+tradingstrategy-ai/trading-strategy/blob/master/CHANGELOG.md) [Read more
+documentation how to develop this package](https://tradingstrategy.ai/docs/
+programming/development.html). # License GNU AGPL 3.0.
```

