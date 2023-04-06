# Comparing `tmp/kmax-4.5rc5.tar.gz` & `tmp/kmax-4.5rc6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kmax-4.5rc5.tar", last modified: Thu Feb  2 17:28:12 2023, max compression
+gzip compressed data, was "kmax-4.5rc6.tar", last modified: Tue Feb 28 13:32:50 2023, max compression
```

## Comparing `kmax-4.5rc5.tar` & `kmax-4.5rc6.tar`

### file list

```diff
@@ -1,151 +1,151 @@
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.723913 kmax-4.5rc5/
--rw-rw-r--   0 paul      (1000) paul      (1000)     1291 2022-07-24 16:10:49.000000 kmax-4.5rc5/MANIFEST.in
--rw-rw-r--   0 paul      (1000) paul      (1000)     8847 2023-02-02 17:28:12.723913 kmax-4.5rc5/PKG-INFO
--rw-rw-r--   0 paul      (1000) paul      (1000)     7321 2023-02-01 04:16:45.000000 kmax-4.5rc5/README.md
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.707913 kmax-4.5rc5/kextractors/
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.707913 kmax-4.5rc5/kextractors/kextractor-3.19/
--rw-rw-r--   0 paul      (1000) paul      (1000)    67230 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/bconf.lex.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    62099 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/bconf.tab.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    26063 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/confdata.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    27155 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/expr.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     7522 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/expr.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    59960 2023-01-19 20:19:52.000000 kmax-4.5rc5/kextractors/kextractor-3.19/kextractor.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3116 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/kextractor_extension.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3710 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/list.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     5022 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/lkc.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     2538 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/lkc_proto.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    17232 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/menu.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    29829 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/symbol.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3156 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/util.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    12255 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/zconf.hash.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    58266 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/zconf.lex.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    75191 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-3.19/zconf.tab.c
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.711913 kmax-4.5rc5/kextractors/kextractor-4.12.8/
--rw-rw-r--   0 paul      (1000) paul      (1000)    67230 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/bconf.lex.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    62099 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/bconf.tab.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    26265 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/confdata.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    27589 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/expr.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     7272 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/expr.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    60498 2023-01-19 20:19:52.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/kextractor.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3144 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/kextractor_extension.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3710 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/list.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     4554 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/lkc.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     2154 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/lkc_proto.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    17924 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/menu.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    31091 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/symbol.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     2979 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/util.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    12656 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/zconf.hash.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    59560 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/zconf.lex.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    76725 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-4.12.8/zconf.tab.c
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.715913 kmax-4.5rc5/kextractors/kextractor-4.18/
--rw-rw-r--   0 paul      (1000) paul      (1000)    25782 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/confdata.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    30843 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/expr.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     9898 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/expr.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     1854 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/kconf_id.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    37461 2023-01-19 20:19:52.000000 kmax-4.5rc5/kextractors/kextractor-4.18/kextractor.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3116 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/kextractor_extension.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3749 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/list.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     4157 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/lkc.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     2520 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/lkc_proto.h
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.715913 kmax-4.5rc5/kextractors/kextractor-4.18/lxdialog/
--rw-rw-r--   0 paul      (1000) paul      (1000)     7525 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/lxdialog/dialog.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    21978 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/menu.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     1875 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/nconf.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    11278 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/preprocess.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     7544 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/qconf.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    29198 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/symbol.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     2897 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/util.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    66732 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/zconf.lex.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    78087 2022-07-24 15:46:54.000000 kmax-4.5rc5/kextractors/kextractor-4.18/zconf.tab.c
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.715913 kmax-4.5rc5/kextractors/kextractor-next-20200430/
--rw-rw-r--   0 paul      (1000) paul      (1000)    27837 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/confdata.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    30726 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/expr.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     9873 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/expr.h
--rw-rw-r--   0 paul      (1000) paul      (1000)      752 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/images.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    37461 2023-01-19 20:19:52.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/kextractor.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3242 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/kextractor_extension.c
--rw-rw-r--   0 paul      (1000) paul      (1000)   126738 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/lexer.lex.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3749 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/list.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     3880 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/lkc.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     2479 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/lkc_proto.h
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.715913 kmax-4.5rc5/kextractors/kextractor-next-20200430/lxdialog/
--rw-rw-r--   0 paul      (1000) paul      (1000)     6854 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/lxdialog/dialog.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    22738 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/menu.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     1862 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/nconf.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    74727 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/parser.tab.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3441 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/parser.tab.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    11247 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/preprocess.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     7626 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/qconf.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    29264 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/symbol.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     2210 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20200430/util.c
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.719913 kmax-4.5rc5/kextractors/kextractor-next-20210426/
--rw-rw-r--   0 paul      (1000) paul      (1000)    24884 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/confdata.c
--rw-rw-r--   0 paul      (1000) paul      (1000)    30726 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/expr.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     9699 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/expr.h
--rw-rw-r--   0 paul      (1000) paul      (1000)      857 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/images.h
--rw-rw-r--   0 paul      (1000) paul      (1000)      172 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/internal.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    33157 2023-01-19 20:19:52.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/kextractor.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3242 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/kextractor_extension.c
--rw-rw-r--   0 paul      (1000) paul      (1000)   115311 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/lexer.lex.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3749 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/list.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     4017 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/lkc.h
--rw-rw-r--   0 paul      (1000) paul      (1000)     1962 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/lkc_proto.h
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.719913 kmax-4.5rc5/kextractors/kextractor-next-20210426/lxdialog/
--rw-rw-r--   0 paul      (1000) paul      (1000)     6854 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/lxdialog/dialog.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    22175 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/menu.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     2050 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/nconf.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    74500 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/parser.tab.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     3366 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/parser.tab.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    11254 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/preprocess.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     6552 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/qconf.h
--rw-rw-r--   0 paul      (1000) paul      (1000)    29284 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/symbol.c
--rw-rw-r--   0 paul      (1000) paul      (1000)     2210 2022-03-09 17:06:47.000000 kmax-4.5rc5/kextractors/kextractor-next-20210426/util.c
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.723913 kmax-4.5rc5/kmax/
--rw-rw-r--   0 paul      (1000) paul      (1000)        0 2022-03-09 17:06:47.000000 kmax-4.5rc5/kmax/__init__.py
--rw-rw-r--   0 paul      (1000) paul      (1000)       43 2023-02-02 17:27:26.000000 kmax-4.5rc5/kmax/about.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    65677 2022-07-24 15:46:54.000000 kmax-4.5rc5/kmax/alg.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    56365 2022-10-26 18:56:17.000000 kmax-4.5rc5/kmax/arch.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     4399 2022-07-24 15:46:54.000000 kmax-4.5rc5/kmax/common.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     9252 2022-07-24 15:46:54.000000 kmax-4.5rc5/kmax/datastructures.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     8945 2022-07-24 15:46:54.000000 kmax-4.5rc5/kmax/expression_converter.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     5357 2022-07-24 15:46:54.000000 kmax-4.5rc5/kmax/find_selectable.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    55265 2022-03-09 17:06:47.000000 kmax-4.5rc5/kmax/kclause
--rw-rw-r--   0 paul      (1000) paul      (1000)     1265 2022-03-09 17:06:47.000000 kmax-4.5rc5/kmax/kextract
--rw-rw-r--   0 paul      (1000) paul      (1000)     1626 2022-07-24 15:46:54.000000 kmax-4.5rc5/kmax/kextractcommon.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     2916 2022-07-24 16:10:49.000000 kmax-4.5rc5/kmax/kextractlinux
--rw-rw-r--   0 paul      (1000) paul      (1000)    54767 2022-10-06 23:25:38.000000 kmax-4.5rc5/kmax/kismet
--rw-rw-r--   0 paul      (1000) paul      (1000)    82064 2023-01-30 05:44:05.000000 kmax-4.5rc5/kmax/klocalizer
--rw-rw-r--   0 paul      (1000) paul      (1000)    65131 2022-11-20 19:35:30.000000 kmax-4.5rc5/kmax/klocalizer.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     4182 2022-03-09 17:06:47.000000 kmax-4.5rc5/kmax/kmax
--rw-rw-r--   0 paul      (1000) paul      (1000)    10619 2022-03-09 17:06:47.000000 kmax-4.5rc5/kmax/kmaxall
--rw-rw-r--   0 paul      (1000) paul      (1000)    51280 2023-01-30 05:44:05.000000 kmax-4.5rc5/kmax/koverage
--rw-rw-r--   0 paul      (1000) paul      (1000)     3637 2022-03-09 17:06:47.000000 kmax-4.5rc5/kmax/kreader
--rw-rw-r--   0 paul      (1000) paul      (1000)     8723 2022-07-24 15:46:54.000000 kmax-4.5rc5/kmax/patch.py
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.723913 kmax-4.5rc5/kmax/resources/
--rw-rw-r--   0 paul      (1000) paul      (1000)     2774 2022-07-24 16:10:49.000000 kmax-4.5rc5/kmax/resources/kismet_udd_printer_extension.h
--rw-rw-r--   0 paul      (1000) paul      (1000)      404 2022-07-24 16:10:49.000000 kmax-4.5rc5/kmax/resources/kismet_verification_patch.diff
--rw-rw-r--   0 paul      (1000) paul      (1000)      178 2022-03-09 17:06:47.000000 kmax-4.5rc5/kmax/settings.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    33203 2022-11-15 04:08:55.000000 kmax-4.5rc5/kmax/superc.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     4534 2022-07-24 16:10:49.000000 kmax-4.5rc5/kmax/udd_warning_parser.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    10220 2022-11-15 04:08:55.000000 kmax-4.5rc5/kmax/vcommon.py
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.723913 kmax-4.5rc5/kmax.egg-info/
--rw-rw-r--   0 paul      (1000) paul      (1000)     8847 2023-02-02 17:28:12.000000 kmax-4.5rc5/kmax.egg-info/PKG-INFO
--rw-rw-r--   0 paul      (1000) paul      (1000)     4713 2023-02-02 17:28:12.000000 kmax-4.5rc5/kmax.egg-info/SOURCES.txt
--rw-rw-r--   0 paul      (1000) paul      (1000)        1 2023-02-02 17:28:12.000000 kmax-4.5rc5/kmax.egg-info/dependency_links.txt
--rw-rw-r--   0 paul      (1000) paul      (1000)       72 2023-02-02 17:28:12.000000 kmax-4.5rc5/kmax.egg-info/requires.txt
--rw-rw-r--   0 paul      (1000) paul      (1000)      112 2023-02-02 17:28:12.000000 kmax-4.5rc5/kmax.egg-info/top_level.txt
-drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-02 17:28:12.723913 kmax-4.5rc5/pymake/
--rw-rw-r--   0 paul      (1000) paul      (1000)        0 2021-02-07 21:59:59.000000 kmax-4.5rc5/pymake/__init__.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     3495 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/builtins.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     9685 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/command.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    62509 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/data.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    26993 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/functions.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     1622 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/globrelative.py
--rw-rw-r--   0 paul      (1000) paul      (1000)      385 2021-02-07 22:00:30.000000 kmax-4.5rc5/pymake/implicit.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    30939 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/parser.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    33347 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/parserdata.py
--rw-rw-r--   0 paul      (1000) paul      (1000)    19784 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/process.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     3917 2022-07-24 15:46:54.000000 kmax-4.5rc5/pymake/util.py
--rw-rw-r--   0 paul      (1000) paul      (1000)     1013 2021-02-07 22:00:30.000000 kmax-4.5rc5/pymake/win32process.py
--rw-rw-r--   0 paul      (1000) paul      (1000)       38 2023-02-02 17:28:12.723913 kmax-4.5rc5/setup.cfg
--rw-rw-r--   0 paul      (1000) paul      (1000)     3714 2023-01-19 19:46:23.000000 kmax-4.5rc5/setup.py
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.721570 kmax-4.5rc6/
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1291 2022-07-24 16:10:49.000000 kmax-4.5rc6/MANIFEST.in
+-rw-rw-r--   0 paul      (1000) paul      (1000)     8847 2023-02-28 13:32:50.721570 kmax-4.5rc6/PKG-INFO
+-rw-rw-r--   0 paul      (1000) paul      (1000)     7321 2023-02-01 04:16:45.000000 kmax-4.5rc6/README.md
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.713569 kmax-4.5rc6/kextractors/
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.713569 kmax-4.5rc6/kextractors/kextractor-3.19/
+-rw-rw-r--   0 paul      (1000) paul      (1000)    67230 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/bconf.lex.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    62099 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/bconf.tab.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    26063 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/confdata.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    27155 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/expr.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     7522 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/expr.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    59960 2023-01-19 20:19:52.000000 kmax-4.5rc6/kextractors/kextractor-3.19/kextractor.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3116 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/kextractor_extension.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3710 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/list.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     5022 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/lkc.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2538 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/lkc_proto.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    17232 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/menu.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    29829 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/symbol.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3156 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/util.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    12255 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/zconf.hash.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    58266 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/zconf.lex.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    75191 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-3.19/zconf.tab.c
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.713569 kmax-4.5rc6/kextractors/kextractor-4.12.8/
+-rw-rw-r--   0 paul      (1000) paul      (1000)    67230 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/bconf.lex.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    62099 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/bconf.tab.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    26265 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/confdata.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    27589 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/expr.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     7272 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/expr.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    60498 2023-01-19 20:19:52.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/kextractor.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3144 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/kextractor_extension.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3710 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/list.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     4554 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/lkc.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2154 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/lkc_proto.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    17924 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/menu.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    31091 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/symbol.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2979 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/util.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    12656 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/zconf.hash.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    59560 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/zconf.lex.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    76725 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-4.12.8/zconf.tab.c
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.717569 kmax-4.5rc6/kextractors/kextractor-4.18/
+-rw-rw-r--   0 paul      (1000) paul      (1000)    25782 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/confdata.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    30843 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/expr.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     9898 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/expr.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1854 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/kconf_id.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    37461 2023-01-19 20:19:52.000000 kmax-4.5rc6/kextractors/kextractor-4.18/kextractor.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3116 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/kextractor_extension.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3749 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/list.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     4157 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/lkc.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2520 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/lkc_proto.h
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.717569 kmax-4.5rc6/kextractors/kextractor-4.18/lxdialog/
+-rw-rw-r--   0 paul      (1000) paul      (1000)     7525 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/lxdialog/dialog.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    21978 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/menu.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1875 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/nconf.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    11278 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/preprocess.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     7544 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/qconf.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    29198 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/symbol.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2897 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/util.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    66732 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/zconf.lex.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    78087 2022-07-24 15:46:54.000000 kmax-4.5rc6/kextractors/kextractor-4.18/zconf.tab.c
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.717569 kmax-4.5rc6/kextractors/kextractor-next-20200430/
+-rw-rw-r--   0 paul      (1000) paul      (1000)    27837 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/confdata.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    30726 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/expr.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     9873 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/expr.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)      752 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/images.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    37461 2023-01-19 20:19:52.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/kextractor.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3242 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/kextractor_extension.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)   126738 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/lexer.lex.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3749 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/list.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3880 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/lkc.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2479 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/lkc_proto.h
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.717569 kmax-4.5rc6/kextractors/kextractor-next-20200430/lxdialog/
+-rw-rw-r--   0 paul      (1000) paul      (1000)     6854 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/lxdialog/dialog.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    22738 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/menu.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1862 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/nconf.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    74727 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/parser.tab.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3441 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/parser.tab.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    11247 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/preprocess.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     7626 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/qconf.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    29264 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/symbol.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2210 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20200430/util.c
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.717569 kmax-4.5rc6/kextractors/kextractor-next-20210426/
+-rw-rw-r--   0 paul      (1000) paul      (1000)    24884 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/confdata.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)    30726 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/expr.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     9699 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/expr.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)      857 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/images.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)      172 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/internal.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    33157 2023-01-19 20:19:52.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/kextractor.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3242 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/kextractor_extension.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)   115311 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/lexer.lex.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3749 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/list.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     4017 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/lkc.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1962 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/lkc_proto.h
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.717569 kmax-4.5rc6/kextractors/kextractor-next-20210426/lxdialog/
+-rw-rw-r--   0 paul      (1000) paul      (1000)     6854 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/lxdialog/dialog.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    22175 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/menu.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2050 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/nconf.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    74500 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/parser.tab.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3366 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/parser.tab.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    11254 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/preprocess.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     6552 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/qconf.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)    29284 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/symbol.c
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2210 2022-03-09 17:06:47.000000 kmax-4.5rc6/kextractors/kextractor-next-20210426/util.c
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.721570 kmax-4.5rc6/kmax/
+-rw-rw-r--   0 paul      (1000) paul      (1000)        0 2022-03-09 17:06:47.000000 kmax-4.5rc6/kmax/__init__.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)       43 2023-02-28 13:29:23.000000 kmax-4.5rc6/kmax/about.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    65677 2022-07-24 15:46:54.000000 kmax-4.5rc6/kmax/alg.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    56365 2022-10-26 18:56:17.000000 kmax-4.5rc6/kmax/arch.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     4399 2022-07-24 15:46:54.000000 kmax-4.5rc6/kmax/common.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     9252 2022-07-24 15:46:54.000000 kmax-4.5rc6/kmax/datastructures.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     8945 2022-07-24 15:46:54.000000 kmax-4.5rc6/kmax/expression_converter.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     5357 2022-07-24 15:46:54.000000 kmax-4.5rc6/kmax/find_selectable.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    55265 2022-03-09 17:06:47.000000 kmax-4.5rc6/kmax/kclause
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1265 2022-03-09 17:06:47.000000 kmax-4.5rc6/kmax/kextract
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1626 2022-07-24 15:46:54.000000 kmax-4.5rc6/kmax/kextractcommon.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2916 2022-07-24 16:10:49.000000 kmax-4.5rc6/kmax/kextractlinux
+-rw-rw-r--   0 paul      (1000) paul      (1000)    54767 2022-10-06 23:25:38.000000 kmax-4.5rc6/kmax/kismet
+-rw-rw-r--   0 paul      (1000) paul      (1000)    83081 2023-02-28 13:28:45.000000 kmax-4.5rc6/kmax/klocalizer
+-rw-rw-r--   0 paul      (1000) paul      (1000)    65131 2022-11-20 19:35:30.000000 kmax-4.5rc6/kmax/klocalizer.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     4182 2022-03-09 17:06:47.000000 kmax-4.5rc6/kmax/kmax
+-rw-rw-r--   0 paul      (1000) paul      (1000)    10619 2022-03-09 17:06:47.000000 kmax-4.5rc6/kmax/kmaxall
+-rw-rw-r--   0 paul      (1000) paul      (1000)    51280 2023-01-30 05:44:05.000000 kmax-4.5rc6/kmax/koverage
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3637 2022-03-09 17:06:47.000000 kmax-4.5rc6/kmax/kreader
+-rw-rw-r--   0 paul      (1000) paul      (1000)     8723 2022-07-24 15:46:54.000000 kmax-4.5rc6/kmax/patch.py
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.721570 kmax-4.5rc6/kmax/resources/
+-rw-rw-r--   0 paul      (1000) paul      (1000)     2774 2022-07-24 16:10:49.000000 kmax-4.5rc6/kmax/resources/kismet_udd_printer_extension.h
+-rw-rw-r--   0 paul      (1000) paul      (1000)      404 2022-07-24 16:10:49.000000 kmax-4.5rc6/kmax/resources/kismet_verification_patch.diff
+-rw-rw-r--   0 paul      (1000) paul      (1000)      178 2022-03-09 17:06:47.000000 kmax-4.5rc6/kmax/settings.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    33203 2022-11-15 04:08:55.000000 kmax-4.5rc6/kmax/superc.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     4534 2022-07-24 16:10:49.000000 kmax-4.5rc6/kmax/udd_warning_parser.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    10220 2022-11-15 04:08:55.000000 kmax-4.5rc6/kmax/vcommon.py
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.721570 kmax-4.5rc6/kmax.egg-info/
+-rw-rw-r--   0 paul      (1000) paul      (1000)     8847 2023-02-28 13:32:50.000000 kmax-4.5rc6/kmax.egg-info/PKG-INFO
+-rw-rw-r--   0 paul      (1000) paul      (1000)     4713 2023-02-28 13:32:50.000000 kmax-4.5rc6/kmax.egg-info/SOURCES.txt
+-rw-rw-r--   0 paul      (1000) paul      (1000)        1 2023-02-28 13:32:50.000000 kmax-4.5rc6/kmax.egg-info/dependency_links.txt
+-rw-rw-r--   0 paul      (1000) paul      (1000)       72 2023-02-28 13:32:50.000000 kmax-4.5rc6/kmax.egg-info/requires.txt
+-rw-rw-r--   0 paul      (1000) paul      (1000)      112 2023-02-28 13:32:50.000000 kmax-4.5rc6/kmax.egg-info/top_level.txt
+drwxrwxr-x   0 paul      (1000) paul      (1000)        0 2023-02-28 13:32:50.721570 kmax-4.5rc6/pymake/
+-rw-rw-r--   0 paul      (1000) paul      (1000)        0 2021-02-07 21:59:59.000000 kmax-4.5rc6/pymake/__init__.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3495 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/builtins.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     9685 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/command.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    62509 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/data.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    26993 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/functions.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1622 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/globrelative.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)      385 2021-02-07 22:00:30.000000 kmax-4.5rc6/pymake/implicit.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    30939 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/parser.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    33347 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/parserdata.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)    19784 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/process.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3917 2022-07-24 15:46:54.000000 kmax-4.5rc6/pymake/util.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)     1013 2021-02-07 22:00:30.000000 kmax-4.5rc6/pymake/win32process.py
+-rw-rw-r--   0 paul      (1000) paul      (1000)       38 2023-02-28 13:32:50.721570 kmax-4.5rc6/setup.cfg
+-rw-rw-r--   0 paul      (1000) paul      (1000)     3714 2023-01-19 19:46:23.000000 kmax-4.5rc6/setup.py
```

### Comparing `kmax-4.5rc5/MANIFEST.in` & `kmax-4.5rc6/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/PKG-INFO` & `kmax-4.5rc6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kmax
-Version: 4.5rc5
+Version: 4.5rc6
 Summary: Tools for working with symbolic  constraints from Kbuild Makefile.
 Home-page: https://github.com/paulgazz/kmax
 Author: Paul Gazzillo
 Author-email: paul@pgazz.com
 License: GPLv2+
 Description: <!-- START doctoc generated TOC please keep comment here to allow auto update -->
         <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
```

### Comparing `kmax-4.5rc5/README.md` & `kmax-4.5rc6/README.md`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/bconf.lex.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/bconf.lex.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/bconf.tab.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/bconf.tab.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/confdata.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/confdata.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/expr.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/expr.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/expr.h` & `kmax-4.5rc6/kextractors/kextractor-3.19/expr.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/kextractor.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/kextractor.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/kextractor_extension.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/kextractor_extension.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/list.h` & `kmax-4.5rc6/kextractors/kextractor-3.19/list.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/lkc.h` & `kmax-4.5rc6/kextractors/kextractor-3.19/lkc.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/lkc_proto.h` & `kmax-4.5rc6/kextractors/kextractor-3.19/lkc_proto.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/menu.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/menu.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/symbol.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/symbol.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/util.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/util.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/zconf.hash.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/zconf.hash.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/zconf.lex.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/zconf.lex.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-3.19/zconf.tab.c` & `kmax-4.5rc6/kextractors/kextractor-3.19/zconf.tab.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/bconf.lex.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/bconf.lex.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/bconf.tab.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/bconf.tab.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/confdata.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/confdata.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/expr.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/expr.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/expr.h` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/expr.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/kextractor.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/kextractor.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/kextractor_extension.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/kextractor_extension.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/list.h` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/list.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/lkc.h` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/lkc.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/lkc_proto.h` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/lkc_proto.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/menu.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/menu.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/symbol.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/symbol.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/util.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/util.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/zconf.hash.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/zconf.hash.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/zconf.lex.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/zconf.lex.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.12.8/zconf.tab.c` & `kmax-4.5rc6/kextractors/kextractor-4.12.8/zconf.tab.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/confdata.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/confdata.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/expr.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/expr.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/expr.h` & `kmax-4.5rc6/kextractors/kextractor-4.18/expr.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/kconf_id.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/kconf_id.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/kextractor.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/kextractor.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/kextractor_extension.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/kextractor_extension.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/list.h` & `kmax-4.5rc6/kextractors/kextractor-4.18/list.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/lkc.h` & `kmax-4.5rc6/kextractors/kextractor-4.18/lkc.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/lkc_proto.h` & `kmax-4.5rc6/kextractors/kextractor-4.18/lkc_proto.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/lxdialog/dialog.h` & `kmax-4.5rc6/kextractors/kextractor-4.18/lxdialog/dialog.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/menu.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/menu.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/nconf.h` & `kmax-4.5rc6/kextractors/kextractor-4.18/nconf.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/preprocess.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/preprocess.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/qconf.h` & `kmax-4.5rc6/kextractors/kextractor-4.18/qconf.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/symbol.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/symbol.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/util.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/util.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/zconf.lex.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/zconf.lex.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-4.18/zconf.tab.c` & `kmax-4.5rc6/kextractors/kextractor-4.18/zconf.tab.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/confdata.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/confdata.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/expr.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/expr.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/expr.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/expr.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/images.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/images.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/kextractor.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/kextractor.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/kextractor_extension.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/kextractor_extension.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/lexer.lex.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/lexer.lex.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/list.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/list.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/lkc.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/lkc.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/lkc_proto.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/lkc_proto.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/lxdialog/dialog.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/lxdialog/dialog.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/menu.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/menu.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/nconf.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/nconf.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/parser.tab.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/parser.tab.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/parser.tab.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/parser.tab.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/preprocess.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/preprocess.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/qconf.h` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/qconf.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/symbol.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/symbol.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20200430/util.c` & `kmax-4.5rc6/kextractors/kextractor-next-20200430/util.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/confdata.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/confdata.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/expr.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/expr.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/expr.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/expr.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/images.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/images.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/kextractor.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/kextractor.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/kextractor_extension.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/kextractor_extension.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/lexer.lex.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/lexer.lex.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/list.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/list.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/lkc.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/lkc.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/lkc_proto.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/lkc_proto.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/lxdialog/dialog.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/lxdialog/dialog.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/menu.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/menu.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/nconf.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/nconf.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/parser.tab.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/parser.tab.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/parser.tab.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/parser.tab.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/preprocess.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/preprocess.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/qconf.h` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/qconf.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/symbol.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/symbol.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kextractors/kextractor-next-20210426/util.c` & `kmax-4.5rc6/kextractors/kextractor-next-20210426/util.c`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/alg.py` & `kmax-4.5rc6/kmax/alg.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/arch.py` & `kmax-4.5rc6/kmax/arch.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/common.py` & `kmax-4.5rc6/kmax/common.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/datastructures.py` & `kmax-4.5rc6/kmax/datastructures.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/expression_converter.py` & `kmax-4.5rc6/kmax/expression_converter.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/find_selectable.py` & `kmax-4.5rc6/kmax/find_selectable.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kclause` & `kmax-4.5rc6/kmax/kclause`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kextract` & `kmax-4.5rc6/kmax/kextract`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kextractcommon.py` & `kmax-4.5rc6/kmax/kextractcommon.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kextractlinux` & `kmax-4.5rc6/kmax/kextractlinux`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kismet` & `kmax-4.5rc6/kmax/kismet`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/klocalizer` & `kmax-4.5rc6/kmax/klocalizer`

 * *Files 0% similar despite different names*

```diff
@@ -151,14 +151,17 @@
   argparser.add_argument('-u',
                          '--show-unsat-core',
                          action="store_true",
                          help="""Show the unsatisfiable core if the formula is unsatisfiable.""")
   argparser.add_argument('--view-kbuild',
                          action="store_true",
                          help="""Just show the Kbuild constraints for the given compilation unit.  All other arguments are ignored.""")
+  argparser.add_argument("--save-smt",
+                         type=str,
+                         help="""Save the resulting formula in SMTLIB format to the given file.  This option will not create a .config file.""")
   argparser.add_argument("--save-dimacs",
                          type=str,
                          help="""Save the resulting formula in DIMACS format to the given file.  This option will not create a .config file.""")
   argparser.add_argument("--force-unmet-free",
                          action="store_true",
                          help="""Force unmet direct dependency free configuration.  This requires kclause direct depedency formulas file to exist in KMAX_FORMULAS/kclause/ARCH/kclause.normal_dep, which is a pickled dictionary from configuration options to direct dependency formulas.""")
   argparser.add_argument("--allow-unmet-for",
@@ -305,14 +308,15 @@
   disable_config_broken = not args.allow_config_broken
   allow_non_visibles = args.allow_non_visibles
   view_kbuild = args.view_kbuild
   sample = args.sample
   sample_count = sample if sample is not None else 1
   sample_prefix = args.sample_prefix
   random_seed = args.random_seed
+  save_smt = args.save_smt
   save_dimacs = args.save_dimacs
   force_unmet_free = args.force_unmet_free
   allow_unmet_for = args.allow_unmet_for
   no_nonbool_preservation = args.no_nonbool_preservation
   superc_linux_script = args.superc_linux_script
   cross_compiler = args.cross_compiler
   no_builtin_build_targets = args.no_builtin_build_targets
@@ -652,27 +656,39 @@
       exit(12)
     if show_unsat_core:
       logger.error("%s is incompatible with --show-unsat-core.\n" % mutual_exclusion_str)
       exit(12)
     if view_kbuild:
       logger.error("%s is incompatible with --view-kbuild.\n" % mutual_exclusion_str)
       exit(12)
+    if save_smt:
+      logger.error("%s is incompatible with --save-smt.\n" % mutual_exclusion_str)
+      exit(12)
     if save_dimacs:
       logger.error("%s is incompatible with --save-dimacs.\n" % mutual_exclusion_str)
       exit(12)
     
   if save_dimacs:
     if os.path.exists(save_dimacs):
       logger.warning("Overwriting existing file with the DIMACS output: %s\n" % (save_dimacs))
     if reportallarchs or sample:
       logger.error("--save-dimacs is incompatible with --report-all\n")
       exit(12)
     # current behavior is to not sample with z3 when outputting constraints in the DIMACS format
     sample_count = 0
 
+  if save_smt:
+    if os.path.exists(save_smt):
+      logger.warning("Overwriting existing file with the SMT output: %s\n" % (save_smt))
+    if reportallarchs or sample:
+      logger.error("--save-smt is incompatible with --report-all\n")
+      exit(12)
+    # current behavior is to not sample with z3 when outputting constraints in the SMT format
+    sample_count = 0
+
   if sample is not None:
     if sample_prefix is None:
       sample_prefix="config"
     if approximate:
       argparser.print_help()
       logger.error("--approximate and --sample cannot currently be used together\n")
       exit(12)
@@ -1645,14 +1661,22 @@
         dimacs_file_name = save_dimacs
         logger.info("Writing constraints in DIMACS format to \"%s\".\n" % dimacs_file_name)
         solver = z3.Solver()
         solver.add(constraints)
         with open(dimacs_file_name, 'w') as dimacsf:
           dimacsf.write(solver.dimacs())
 
+      if save_smt:
+        smt_file_name = save_smt
+        logger.info("Writing constraints in SMT format to \"%s\".\n" % smt_file_name)
+        solver = z3.Solver()
+        solver.add(constraints)
+        with open(smt_file_name, 'w') as smtf:
+          smtf.write(solver.to_smt2())
+
       #
       # Sample configs
       #
       if not reportallarchs and sample_count > 0:
 
         # Prepare the configs by sampling models
         configs = [Klocalizer.get_config_from_model(model, arch, set_tristate_m=modules_arg, allow_non_visibles=allow_non_visibles, approximate_config=approximate_config)]
```

### Comparing `kmax-4.5rc5/kmax/klocalizer.py` & `kmax-4.5rc6/kmax/klocalizer.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kmax` & `kmax-4.5rc6/kmax/kmax`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kmaxall` & `kmax-4.5rc6/kmax/kmaxall`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/koverage` & `kmax-4.5rc6/kmax/koverage`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/kreader` & `kmax-4.5rc6/kmax/kreader`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/patch.py` & `kmax-4.5rc6/kmax/patch.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/resources/kismet_udd_printer_extension.h` & `kmax-4.5rc6/kmax/resources/kismet_udd_printer_extension.h`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/superc.py` & `kmax-4.5rc6/kmax/superc.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/udd_warning_parser.py` & `kmax-4.5rc6/kmax/udd_warning_parser.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax/vcommon.py` & `kmax-4.5rc6/kmax/vcommon.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/kmax.egg-info/PKG-INFO` & `kmax-4.5rc6/kmax.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kmax
-Version: 4.5rc5
+Version: 4.5rc6
 Summary: Tools for working with symbolic  constraints from Kbuild Makefile.
 Home-page: https://github.com/paulgazz/kmax
 Author: Paul Gazzillo
 Author-email: paul@pgazz.com
 License: GPLv2+
 Description: <!-- START doctoc generated TOC please keep comment here to allow auto update -->
         <!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
```

### Comparing `kmax-4.5rc5/kmax.egg-info/SOURCES.txt` & `kmax-4.5rc6/kmax.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/builtins.py` & `kmax-4.5rc6/pymake/builtins.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/command.py` & `kmax-4.5rc6/pymake/command.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/data.py` & `kmax-4.5rc6/pymake/data.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/functions.py` & `kmax-4.5rc6/pymake/functions.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/globrelative.py` & `kmax-4.5rc6/pymake/globrelative.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/parser.py` & `kmax-4.5rc6/pymake/parser.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/parserdata.py` & `kmax-4.5rc6/pymake/parserdata.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/process.py` & `kmax-4.5rc6/pymake/process.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/util.py` & `kmax-4.5rc6/pymake/util.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/pymake/win32process.py` & `kmax-4.5rc6/pymake/win32process.py`

 * *Files identical despite different names*

### Comparing `kmax-4.5rc5/setup.py` & `kmax-4.5rc6/setup.py`

 * *Files identical despite different names*

