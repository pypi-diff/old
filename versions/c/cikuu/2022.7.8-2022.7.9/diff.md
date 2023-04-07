# Comparing `tmp/cikuu-2022.7.8.tar.gz` & `tmp/cikuu-2022.7.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cikuu-2022.7.8.tar", last modified: Sat Jan  7 10:59:59 2023, max compression
+gzip compressed data, was "cikuu-2022.7.9.tar", last modified: Fri Jan 13 08:46:52 2023, max compression
```

## Comparing `cikuu-2022.7.8.tar` & `cikuu-2022.7.9.tar`

### file list

```diff
@@ -1,361 +1,361 @@
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.522736 cikuu-2022.7.8/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       23 2022-03-07 08:36:18.000000 cikuu-2022.7.8/MANIFEST.in
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      249 2023-01-07 10:59:59.522736 cikuu-2022.7.8/PKG-INFO
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:58.938736 cikuu-2022.7.8/api/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      228 2023-01-07 02:36:27.000000 cikuu-2022.7.8/api/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2086 2023-01-07 02:36:14.000000 cikuu-2022.7.8/api/c4.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1236 2022-09-10 08:16:22.000000 cikuu-2022.7.8/api/chunk.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1399 2023-01-07 02:36:14.000000 cikuu-2022.7.8/api/common.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1069 2022-09-02 03:25:13.000000 cikuu-2022.7.8/api/dm.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    19134 2023-01-07 10:59:50.000000 cikuu-2022.7.8/api/es.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4595 2022-10-04 11:04:51.000000 cikuu-2022.7.8/api/feishu.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1480 2023-01-07 02:36:27.000000 cikuu-2022.7.8/api/mynac.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2900 2023-01-07 10:59:50.000000 cikuu-2022.7.8/api/sntjson-es.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      451 2023-01-07 02:36:14.000000 cikuu-2022.7.8/api/sqlite.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1333 2023-01-07 02:36:14.000000 cikuu-2022.7.8/api/wget.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:58.938736 cikuu-2022.7.8/app/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/__init__.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:58.938736 cikuu-2022.7.8/app/dmdsk/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2097 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2298 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/app_navbar.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:58.950736 cikuu-2022.7.8/app/dmdsk/func/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      495 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/dim-awl.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      328 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/dims.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      210 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/eidv.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      452 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/feedback.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      364 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/info.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      777 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/lemma.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      208 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/scores.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      490 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/sent.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      600 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/func/trp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      708 2022-03-07 08:36:18.000000 cikuu-2022.7.8/app/dmdsk/index.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:58.950736 cikuu-2022.7.8/cikuu.egg-info/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      249 2023-01-07 10:59:58.000000 cikuu-2022.7.8/cikuu.egg-info/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6132 2023-01-07 10:59:58.000000 cikuu-2022.7.8/cikuu.egg-info/SOURCES.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2023-01-07 10:59:58.000000 cikuu-2022.7.8/cikuu.egg-info/dependency_links.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       15 2023-01-07 10:59:58.000000 cikuu-2022.7.8/cikuu.egg-info/requires.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       49 2023-01-07 10:59:58.000000 cikuu-2022.7.8/cikuu.egg-info/top_level.txt
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.294736 cikuu-2022.7.8/dic/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6977 2022-07-22 02:11:49.000000 cikuu-2022.7.8/dic/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      272 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    72703 2022-12-20 06:18:13.000000 cikuu-2022.7.8/dic/adjlist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    15209 2022-12-20 06:18:13.000000 cikuu-2022.7.8/dic/advlist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2036435 2022-06-22 08:01:11.000000 cikuu-2022.7.8/dic/bnc_wordlist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   742662 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/confu_set.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1423371 2022-06-22 08:01:11.000000 cikuu-2022.7.8/dic/ecdic.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8101 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/errants.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   716825 2022-07-13 02:04:15.000000 cikuu-2022.7.8/dic/essays.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   479692 2022-08-23 13:50:08.000000 cikuu-2022.7.8/dic/frame.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1966581 2022-12-20 06:18:14.000000 cikuu-2022.7.8/dic/lemma_lex.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   446749 2022-09-10 08:16:22.000000 cikuu-2022.7.8/dic/lemma_mf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   182701 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/lemma_scale.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1724919 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/lex_lemma.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4088 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/mwe_disconj.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10043 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/mwe_pv.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   173703 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/n_is_sb.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   173515 2022-12-20 13:19:48.000000 cikuu-2022.7.8/dic/nounlist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  3696547 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/nyt_wc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      438 2022-08-27 09:29:39.000000 cikuu-2022.7.8/dic/oneself.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    41916 2022-08-09 12:43:18.000000 cikuu-2022.7.8/dic/orals.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      125 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/poslist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2786732 2022-08-26 03:27:30.000000 cikuu-2022.7.8/dic/propbank.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1350 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/stoplist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      686 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/to_redislite.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    90499 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/verbform.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9125 2022-12-20 06:18:13.000000 cikuu-2022.7.8/dic/verblist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   147209 2022-12-20 13:19:48.000000 cikuu-2022.7.8/dic/verbtag.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   357010 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/vocab.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    42948 2022-07-06 02:32:21.000000 cikuu-2022.7.8/dic/word_awl.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   825665 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/word_bits.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   518752 2022-03-31 02:25:44.000000 cikuu-2022.7.8/dic/word_grade.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    46473 2022-07-06 02:32:21.000000 cikuu-2022.7.8/dic/word_gsl1.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    42152 2022-07-06 02:32:21.000000 cikuu-2022.7.8/dic/word_gsl2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2765429 2022-07-06 02:32:21.000000 cikuu-2022.7.8/dic/word_idf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2717304 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/word_oov.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  3086978 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/word_pos.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   182843 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/word_scale.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  4370200 2022-07-13 02:04:15.000000 cikuu-2022.7.8/dic/wordattr.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   300932 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/wordcnt.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   353846 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/wordlist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   957421 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/wordlist_ed1.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   100665 2022-03-07 08:36:18.000000 cikuu-2022.7.8/dic/wordnet_verb.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1150605 2022-09-01 06:07:31.000000 cikuu-2022.7.8/dic/wordpos.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    53593 2023-01-07 02:36:14.000000 cikuu-2022.7.8/dic/words.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.330736 cikuu-2022.7.8/dsk/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7973 2022-06-05 09:00:34.000000 cikuu-2022.7.8/dsk/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4196 2022-06-03 13:28:31.000000 cikuu-2022.7.8/dsk/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    94356 2022-12-20 06:18:13.000000 cikuu-2022.7.8/dsk/common.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5471 2022-04-06 06:57:43.000000 cikuu-2022.7.8/dsk/dm.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      303 2022-08-23 13:50:08.000000 cikuu-2022.7.8/dsk/dsk-hello.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4928 2022-06-17 01:02:19.000000 cikuu-2022.7.8/dsk/dsk-to-dskmkf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3970 2022-03-15 09:37:05.000000 cikuu-2022.7.8/dsk/dskapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3816 2022-04-16 07:48:05.000000 cikuu-2022.7.8/dsk/dskes.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4444 2022-06-05 09:00:34.000000 cikuu-2022.7.8/dsk/dskmkf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6148 2022-07-13 08:16:31.000000 cikuu-2022.7.8/dsk/dskmkf_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5410 2022-07-04 05:52:45.000000 cikuu-2022.7.8/dsk/dskmkf_fastapi2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2465 2022-04-16 07:48:05.000000 cikuu-2022.7.8/dsk/dsktrain.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7228 2022-03-31 02:25:44.000000 cikuu-2022.7.8/dsk/essaydm.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      899 2022-05-29 08:25:02.000000 cikuu-2022.7.8/dsk/gears-xdsk.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4284 2022-04-07 03:53:53.000000 cikuu-2022.7.8/dsk/gecv1.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7911 2022-12-20 06:18:14.000000 cikuu-2022.7.8/dsk/index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6162 2022-11-21 12:23:43.000000 cikuu-2022.7.8/dsk/innersim.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6946 2022-06-28 13:01:07.000000 cikuu-2022.7.8/dsk/json-to-dskmkf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9243 2022-06-26 02:55:41.000000 cikuu-2022.7.8/dsk/kvrdsk.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1478 2022-06-17 01:02:19.000000 cikuu-2022.7.8/dsk/load.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8998 2022-12-20 06:18:14.000000 cikuu-2022.7.8/dsk/mkf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1498 2022-06-05 02:40:48.000000 cikuu-2022.7.8/dsk/mqconsume.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    83132 2022-03-24 03:57:57.000000 cikuu-2022.7.8/dsk/pingyu.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3416 2022-10-30 06:51:36.000000 cikuu-2022.7.8/dsk/score.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6150 2022-04-11 14:40:50.000000 cikuu-2022.7.8/dsk/sntsdims.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      936 2022-12-20 06:18:14.000000 cikuu-2022.7.8/dsk/test.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2220 2022-08-25 03:56:00.000000 cikuu-2022.7.8/dsk/tok-hello.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3629 2022-06-19 12:35:53.000000 cikuu-2022.7.8/dsk/uvidsk.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6616 2022-11-21 12:24:05.000000 cikuu-2022.7.8/dsk/wps-gec.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13784 2022-12-20 06:18:14.000000 cikuu-2022.7.8/dsk/wps-xgec.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9689 2022-10-23 06:39:16.000000 cikuu-2022.7.8/dsk/xessay.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10368 2022-11-21 12:23:43.000000 cikuu-2022.7.8/dsk/xgecv1-test.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8578 2022-11-21 12:24:05.000000 cikuu-2022.7.8/dsk/xgecv1.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4396 2022-04-10 09:34:49.000000 cikuu-2022.7.8/dsk/xmkf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2902 2022-11-26 02:05:30.000000 cikuu-2022.7.8/dsk/xsnt-gec.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2186 2022-11-26 02:05:30.000000 cikuu-2022.7.8/dsk/xsnt-spacy.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.390736 cikuu-2022.7.8/en/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    35729 2023-01-07 10:59:50.000000 cikuu-2022.7.8/en/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5503 2022-08-09 12:43:18.000000 cikuu-2022.7.8/en/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6169 2022-04-04 13:55:29.000000 cikuu-2022.7.8/en/annotate.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      701 2022-11-21 12:23:43.000000 cikuu-2022.7.8/en/c4-cl.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3675 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/c4-fts.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      999 2022-11-26 02:05:30.000000 cikuu-2022.7.8/en/c4-gram-upload.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      984 2022-11-21 12:24:05.000000 cikuu-2022.7.8/en/c4-gram.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      875 2022-11-26 02:05:30.000000 cikuu-2022.7.8/en/c4-grams.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      768 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/c4-np.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      482 2022-09-10 08:16:21.000000 cikuu-2022.7.8/en/c4-postag.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      589 2022-10-04 11:04:51.000000 cikuu-2022.7.8/en/c4-trp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2039 2022-10-30 06:51:37.000000 cikuu-2022.7.8/en/c4cl.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      491 2022-09-10 08:16:21.000000 cikuu-2022.7.8/en/c4down.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1884 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/c4gram-mysql.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2812 2022-12-20 06:18:13.000000 cikuu-2022.7.8/en/c4gram-upsert.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1731 2022-11-21 12:23:43.000000 cikuu-2022.7.8/en/c4gram.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1401 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/c4np.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3683 2022-09-02 03:25:13.000000 cikuu-2022.7.8/en/c4postag.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2243 2022-08-23 13:50:08.000000 cikuu-2022.7.8/en/c4skenp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1096 2023-01-07 02:36:14.000000 cikuu-2022.7.8/en/c4tree.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1235 2023-01-07 02:36:14.000000 cikuu-2022.7.8/en/c4trp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1023 2022-10-23 06:39:16.000000 cikuu-2022.7.8/en/c4vp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      811 2022-06-12 03:36:11.000000 cikuu-2022.7.8/en/clause.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6120 2022-05-28 13:45:17.000000 cikuu-2022.7.8/en/dims.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16963 2022-04-04 09:44:40.000000 cikuu-2022.7.8/en/docfts.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8115 2022-08-19 07:35:05.000000 cikuu-2022.7.8/en/docjson.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3124 2022-07-10 08:29:01.000000 cikuu-2022.7.8/en/esbulk.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3777 2022-07-04 07:06:48.000000 cikuu-2022.7.8/en/esfile.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6311 2022-09-10 08:16:21.000000 cikuu-2022.7.8/en/esjson.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3506 2022-06-04 12:54:20.000000 cikuu-2022.7.8/en/exchunk.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1159 2022-06-04 12:54:20.000000 cikuu-2022.7.8/en/exphrase.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1387 2022-06-04 12:54:20.000000 cikuu-2022.7.8/en/extrp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4656 2022-06-01 01:31:35.000000 cikuu-2022.7.8/en/havc.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      181 2022-03-24 15:21:17.000000 cikuu-2022.7.8/en/hello.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18434 2022-08-09 12:43:18.000000 cikuu-2022.7.8/en/kpsi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4234 2022-05-11 12:11:59.000000 cikuu-2022.7.8/en/lempostag.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1185 2022-03-07 08:36:18.000000 cikuu-2022.7.8/en/nlp-lit.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4581 2022-03-20 14:20:59.000000 cikuu-2022.7.8/en/nlp-lmdb.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1900 2022-03-07 08:36:18.000000 cikuu-2022.7.8/en/postag.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2142 2022-05-28 04:33:34.000000 cikuu-2022.7.8/en/shav.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4531 2022-07-06 02:32:21.000000 cikuu-2022.7.8/en/silite.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1506 2022-10-04 11:05:23.000000 cikuu-2022.7.8/en/snt-esjson.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3342 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/sntjson-fts.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1257 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/sntjson-innodb.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8237 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/sntjson-mysql.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6901 2022-11-21 12:24:05.000000 cikuu-2022.7.8/en/sntjson-naclite.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      963 2022-12-20 06:18:14.000000 cikuu-2022.7.8/en/sntjson-parse-snt.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      913 2023-01-07 02:36:27.000000 cikuu-2022.7.8/en/sntjson-tosnt.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3888 2023-01-07 02:36:14.000000 cikuu-2022.7.8/en/sntjson-trpx.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2001 2023-01-07 02:36:14.000000 cikuu-2022.7.8/en/sntjson-vp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2612 2022-08-21 09:41:41.000000 cikuu-2022.7.8/en/spacybs-esjson.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    30937 2022-07-09 01:53:45.000000 cikuu-2022.7.8/en/spacybs.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2733 2022-09-10 08:16:22.000000 cikuu-2022.7.8/en/spider-esjson.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    30005 2022-08-19 07:35:05.000000 cikuu-2022.7.8/en/terms.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9544 2022-08-19 07:35:05.000000 cikuu-2022.7.8/en/verbnet.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1874 2022-04-07 03:45:50.000000 cikuu-2022.7.8/en/xsnt.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1093 2022-10-30 06:51:37.000000 cikuu-2022.7.8/en/zset-load.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.402736 cikuu-2022.7.8/lit/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16540 2022-08-25 03:56:00.000000 cikuu-2022.7.8/lit/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1467 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/common.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.402736 cikuu-2022.7.8/lit/es/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5386 2022-08-26 12:42:31.000000 cikuu-2022.7.8/lit/es/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      575 2022-08-21 09:41:41.000000 cikuu-2022.7.8/lit/es/index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      908 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/essay.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      506 2022-06-12 03:36:11.000000 cikuu-2022.7.8/lit/filling.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1905 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/fillmul.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      778 2022-07-30 14:36:22.000000 cikuu-2022.7.8/lit/hello-pages.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      587 2022-05-28 04:33:35.000000 cikuu-2022.7.8/lit/index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      908 2022-06-12 03:35:50.000000 cikuu-2022.7.8/lit/mock-scoring.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.406736 cikuu-2022.7.8/lit/penly/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-08-18 01:17:18.000000 cikuu-2022.7.8/lit/penly/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      575 2022-08-18 01:17:18.000000 cikuu-2022.7.8/lit/penly/index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      716 2022-06-17 01:02:19.000000 cikuu-2022.7.8/lit/penly-resend.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1827 2022-06-17 01:02:19.000000 cikuu-2022.7.8/lit/redis-dump.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1564 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/reorder.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1689 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/restore.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1152 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/scoring.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1109 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/single.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1295 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/sntspolish.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1091 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/sntupgrade.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1000 2022-06-22 08:01:11.000000 cikuu-2022.7.8/lit/student-input.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1002 2022-06-22 10:06:19.000000 cikuu-2022.7.8/lit/teacher-admin.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.410736 cikuu-2022.7.8/lit/yulk/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      668 2022-08-18 01:17:20.000000 cikuu-2022.7.8/lit/yulk/YULK.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16942 2022-12-20 06:18:14.000000 cikuu-2022.7.8/lit/yulk/common.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.426736 cikuu-2022.7.8/lit/yulk/func/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-12-20 06:18:13.000000 cikuu-2022.7.8/lit/yulk/func/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1063 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/func/bipos.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      598 2022-12-20 06:18:14.000000 cikuu-2022.7.8/lit/yulk/func/cola.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16942 2022-12-20 06:18:14.000000 cikuu-2022.7.8/lit/yulk/func/common.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      666 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/func/corpuslist.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      549 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/func/es.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      501 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/func/eshyb.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      581 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/func/given-expect.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      908 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/func/gramx-single.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1256 2022-12-20 06:18:14.000000 cikuu-2022.7.8/lit/yulk/func/lemma.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1912 2022-07-27 09:55:08.000000 cikuu-2022.7.8/lit/yulk/func/lemvs.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1023 2022-08-18 01:17:18.000000 cikuu-2022.7.8/lit/yulk/func/pos.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      793 2022-08-09 12:43:18.000000 cikuu-2022.7.8/lit/yulk/func/posvs.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1925 2022-08-18 01:17:20.000000 cikuu-2022.7.8/lit/yulk/func/style-in-mul.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      313 2022-08-18 01:17:20.000000 cikuu-2022.7.8/lit/yulk/func/style.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      353 2022-08-18 01:17:20.000000 cikuu-2022.7.8/lit/yulk/func/wcloud.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1547 2022-07-27 09:55:08.000000 cikuu-2022.7.8/lit/yulk/func/wordrank.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      684 2022-12-20 06:18:14.000000 cikuu-2022.7.8/lit/yulk/index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1255 2022-12-20 06:18:14.000000 cikuu-2022.7.8/lit/yulk/lemma.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.430736 cikuu-2022.7.8/pipe/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4906 2022-06-05 02:40:48.000000 cikuu-2022.7.8/pipe/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2622 2022-06-05 02:40:48.000000 cikuu-2022.7.8/pipe/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4039 2022-06-14 01:58:07.000000 cikuu-2022.7.8/pipe/redisgec8180.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6514 2022-06-05 07:30:56.000000 cikuu-2022.7.8/pipe/xgecv1.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.434736 cikuu-2022.7.8/sbert/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      255 2022-03-26 03:03:21.000000 cikuu-2022.7.8/sbert/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1316 2022-03-07 08:36:18.000000 cikuu-2022.7.8/sbert/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      613 2022-03-07 08:36:18.000000 cikuu-2022.7.8/sbert/hello.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13086 2022-03-27 14:17:45.000000 cikuu-2022.7.8/sbert/sntvec.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2023-01-07 10:59:59.522736 cikuu-2022.7.8/setup.cfg
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      814 2023-01-07 10:59:50.000000 cikuu-2022.7.8/setup.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.442736 cikuu-2022.7.8/so/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    24493 2023-01-07 10:59:50.000000 cikuu-2022.7.8/so/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18745 2022-09-01 06:07:31.000000 cikuu-2022.7.8/so/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13741 2022-06-19 12:35:53.000000 cikuu-2022.7.8/so/corpusly.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9475 2023-01-07 02:36:14.000000 cikuu-2022.7.8/so/cos.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    17434 2022-03-25 06:34:20.000000 cikuu-2022.7.8/so/esapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2427 2022-07-04 07:06:48.000000 cikuu-2022.7.8/so/eslite.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1317 2022-10-04 11:04:51.000000 cikuu-2022.7.8/so/kps-si.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1559 2023-01-07 02:36:14.000000 cikuu-2022.7.8/so/load.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1404 2022-08-21 09:41:41.000000 cikuu-2022.7.8/so/loadc4.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1746 2022-09-01 06:07:31.000000 cikuu-2022.7.8/so/loades.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1294 2022-09-01 06:07:31.000000 cikuu-2022.7.8/so/sikps.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    21465 2022-03-25 14:36:25.000000 cikuu-2022.7.8/so/sntvec.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.442736 cikuu-2022.7.8/stream/
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.458736 cikuu-2022.7.8/stream/arc/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8233 2022-04-17 09:06:40.000000 cikuu-2022.7.8/stream/arc/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3215 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2850 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/__main__0414.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      332 2022-04-21 06:16:01.000000 cikuu-2022.7.8/stream/arc/consume-stream.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3374 2022-04-17 09:06:40.000000 cikuu-2022.7.8/stream/arc/essay-plusone.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4019 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/ftessay.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1755 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/ftitem.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1757 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/ftsnt-cola.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2795 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/ftsnt.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1629 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/gecsnts.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6579 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/gecv1.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3256 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/mkf.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7761 2022-04-11 14:40:50.000000 cikuu-2022.7.8/stream/arc/realtime.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4878 2022-04-21 06:16:01.000000 cikuu-2022.7.8/stream/arc/uvisse.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4172 2022-04-17 09:06:39.000000 cikuu-2022.7.8/stream/arc/xessay.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3455 2022-05-01 03:27:58.000000 cikuu-2022.7.8/stream/arc/xsnt-spacy.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2773 2022-04-16 15:04:40.000000 cikuu-2022.7.8/stream/arc/xsnts-dsk.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.458736 cikuu-2022.7.8/stream/lit/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-04-21 06:16:01.000000 cikuu-2022.7.8/stream/lit/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      596 2022-05-11 12:11:59.000000 cikuu-2022.7.8/stream/lit/index.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    22837 2022-06-19 12:35:53.000000 cikuu-2022.7.8/stream/uvirun.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.482736 cikuu-2022.7.8/util/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4453 2023-01-07 02:36:14.000000 cikuu-2022.7.8/util/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6002 2022-10-30 06:51:36.000000 cikuu-2022.7.8/util/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4407 2022-03-15 02:34:12.000000 cikuu-2022.7.8/util/annotate.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3455 2022-07-22 02:01:31.000000 cikuu-2022.7.8/util/bcp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2820 2022-03-07 08:36:18.000000 cikuu-2022.7.8/util/c4data.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1748 2022-04-01 12:54:54.000000 cikuu-2022.7.8/util/client-blpop.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8772 2022-04-04 09:44:40.000000 cikuu-2022.7.8/util/client-xwps.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3219 2022-04-10 09:34:49.000000 cikuu-2022.7.8/util/clientx.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9342 2022-04-16 07:48:05.000000 cikuu-2022.7.8/util/dsk-util.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      506 2022-04-10 09:34:49.000000 cikuu-2022.7.8/util/fire-test.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      357 2022-03-07 08:36:19.000000 cikuu-2022.7.8/util/frame.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4097 2022-03-13 12:56:09.000000 cikuu-2022.7.8/util/kvr.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1730 2022-03-24 03:57:57.000000 cikuu-2022.7.8/util/mq.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      713 2022-07-22 02:01:31.000000 cikuu-2022.7.8/util/nldp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      796 2022-10-04 11:04:51.000000 cikuu-2022.7.8/util/pubsub-sync.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1665 2022-10-04 11:04:51.000000 cikuu-2022.7.8/util/pubsub2api.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      505 2022-03-07 08:36:19.000000 cikuu-2022.7.8/util/sent-diff.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3123 2022-03-31 02:25:44.000000 cikuu-2022.7.8/util/spider.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      430 2022-03-21 14:12:43.000000 cikuu-2022.7.8/util/sqlite.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      928 2022-03-13 12:56:09.000000 cikuu-2022.7.8/util/sqlitedict-load.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4749 2022-04-01 12:54:54.000000 cikuu-2022.7.8/util/wps-blpop.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    36149 2022-04-01 12:54:54.000000 cikuu-2022.7.8/util/wps.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      485 2022-04-10 09:34:49.000000 cikuu-2022.7.8/util/xfile.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      345 2022-07-22 02:01:31.000000 cikuu-2022.7.8/util/xgec-blpop120.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      371 2022-04-16 07:48:04.000000 cikuu-2022.7.8/util/xrange.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2034 2022-04-02 04:02:08.000000 cikuu-2022.7.8/util/xsnt-spacy.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1521 2022-04-10 09:34:49.000000 cikuu-2022.7.8/util/xstream.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1323 2022-04-04 09:44:40.000000 cikuu-2022.7.8/util/xtest-params.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1404 2022-04-04 09:44:40.000000 cikuu-2022.7.8/util/xtest.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.514737 cikuu-2022.7.8/uvirun/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1083 2022-11-21 12:23:43.000000 cikuu-2022.7.8/uvirun/Jinja2-test.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2151 2022-12-20 06:18:14.000000 cikuu-2022.7.8/uvirun/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2964 2022-12-20 06:18:14.000000 cikuu-2022.7.8/uvirun/__main__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6573 2023-01-07 02:36:27.000000 cikuu-2022.7.8/uvirun/c4es.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4734 2022-07-04 07:06:48.000000 cikuu-2022.7.8/uvirun/cos_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      662 2022-07-22 02:01:31.000000 cikuu-2022.7.8/uvirun/demo_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    22269 2022-11-21 12:23:43.000000 cikuu-2022.7.8/uvirun/dsk_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5335 2022-07-26 01:45:37.000000 cikuu-2022.7.8/uvirun/echart_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4778 2022-12-20 06:18:14.000000 cikuu-2022.7.8/uvirun/elastic_fastapi.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.518736 cikuu-2022.7.8/uvirun/errant/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      813 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7269 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/alignment.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3788 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/annotator.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.522736 cikuu-2022.7.8/uvirun/errant/commands/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/commands/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16344 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/commands/compare_m2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7343 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/commands/m2_to_m2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3801 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/commands/parallel_to_m2.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2352 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/edit.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-07 10:59:59.522736 cikuu-2022.7.8/uvirun/errant/en/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/en/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16879 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/en/classifier.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    12340 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/en/lancaster.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5602 2022-09-01 06:07:30.000000 cikuu-2022.7.8/uvirun/errant/en/merger.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10943 2022-11-21 12:23:43.000000 cikuu-2022.7.8/uvirun/errant_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    14040 2022-08-25 03:56:00.000000 cikuu-2022.7.8/uvirun/es1_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    25623 2022-12-20 06:18:14.000000 cikuu-2022.7.8/uvirun/es_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4806 2022-09-10 08:16:21.000000 cikuu-2022.7.8/uvirun/essay_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18036 2022-12-20 06:18:14.000000 cikuu-2022.7.8/uvirun/exchunk_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18525 2022-11-21 12:24:05.000000 cikuu-2022.7.8/uvirun/feishu_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3561 2022-08-25 03:56:00.000000 cikuu-2022.7.8/uvirun/flair_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1089 2023-01-07 02:36:14.000000 cikuu-2022.7.8/uvirun/ftp.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1010 2022-09-01 06:07:31.000000 cikuu-2022.7.8/uvirun/fusion_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3717 2022-09-10 08:16:22.000000 cikuu-2022.7.8/uvirun/gec_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2850 2022-10-23 06:39:16.000000 cikuu-2022.7.8/uvirun/gec_fastapi_33000.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13116 2022-12-20 06:18:14.000000 cikuu-2022.7.8/uvirun/gensim_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6045 2022-12-20 06:18:14.000000 cikuu-2022.7.8/uvirun/gramx_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2305 2022-07-25 13:51:53.000000 cikuu-2022.7.8/uvirun/hnswlib_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3461 2022-08-09 12:43:20.000000 cikuu-2022.7.8/uvirun/kenlm_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6264 2022-08-09 12:43:18.000000 cikuu-2022.7.8/uvirun/kpsi_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13096 2023-01-07 02:36:14.000000 cikuu-2022.7.8/uvirun/kvr_dskdm.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13096 2023-01-07 02:36:15.000000 cikuu-2022.7.8/uvirun/kvr_dskdm1230.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    19126 2022-07-22 02:01:31.000000 cikuu-2022.7.8/uvirun/nldp_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4490 2023-01-07 02:36:27.000000 cikuu-2022.7.8/uvirun/nltk_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1501 2022-09-01 06:07:31.000000 cikuu-2022.7.8/uvirun/nsp_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4343 2022-10-23 06:39:17.000000 cikuu-2022.7.8/uvirun/sbert_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      400 2022-09-01 06:07:31.000000 cikuu-2022.7.8/uvirun/single_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    26665 2023-01-07 02:36:14.000000 cikuu-2022.7.8/uvirun/spacy_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4320 2023-01-07 02:36:15.000000 cikuu-2022.7.8/uvirun/textacy_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2089 2022-07-22 02:01:31.000000 cikuu-2022.7.8/uvirun/trans_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2667 2022-08-09 12:43:20.000000 cikuu-2022.7.8/uvirun/unmasker_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4558 2022-09-10 08:16:21.000000 cikuu-2022.7.8/uvirun/util_fastapi.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    45795 2022-10-04 11:04:51.000000 cikuu-2022.7.8/uvirun/uviredis.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    28272 2023-01-07 02:36:27.000000 cikuu-2022.7.8/uvirun/yulk-nac.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.105927 cikuu-2022.7.9/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       23 2022-03-07 08:36:18.000000 cikuu-2022.7.9/MANIFEST.in
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      249 2023-01-13 08:46:52.669944 cikuu-2022.7.9/PKG-INFO
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.033927 cikuu-2022.7.9/api/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      228 2023-01-07 02:36:27.000000 cikuu-2022.7.9/api/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2086 2023-01-07 02:36:14.000000 cikuu-2022.7.9/api/c4.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1236 2022-09-10 08:16:22.000000 cikuu-2022.7.9/api/chunk.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1399 2023-01-07 02:36:14.000000 cikuu-2022.7.9/api/common.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1069 2022-09-02 03:25:13.000000 cikuu-2022.7.9/api/dm.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    20194 2023-01-13 08:46:09.000000 cikuu-2022.7.9/api/es.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4595 2022-10-04 11:04:51.000000 cikuu-2022.7.9/api/feishu.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1480 2023-01-07 02:36:27.000000 cikuu-2022.7.9/api/mynac.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2904 2023-01-13 08:46:09.000000 cikuu-2022.7.9/api/sntjson-es.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      451 2023-01-07 02:36:14.000000 cikuu-2022.7.9/api/sqlite.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1333 2023-01-07 02:36:14.000000 cikuu-2022.7.9/api/wget.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.033927 cikuu-2022.7.9/app/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/__init__.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.033927 cikuu-2022.7.9/app/dmdsk/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2097 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2298 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/app_navbar.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.037927 cikuu-2022.7.9/app/dmdsk/func/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      495 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/dim-awl.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      328 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/dims.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      210 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/eidv.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      452 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/feedback.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      364 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/info.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      777 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/lemma.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      208 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/scores.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      490 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/sent.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      600 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/func/trp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      708 2022-03-07 08:36:18.000000 cikuu-2022.7.9/app/dmdsk/index.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:52.661944 cikuu-2022.7.9/cikuu.egg-info/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      249 2023-01-13 08:46:52.000000 cikuu-2022.7.9/cikuu.egg-info/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6132 2023-01-13 08:46:52.000000 cikuu-2022.7.9/cikuu.egg-info/SOURCES.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2023-01-13 08:46:52.000000 cikuu-2022.7.9/cikuu.egg-info/dependency_links.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       15 2023-01-13 08:46:52.000000 cikuu-2022.7.9/cikuu.egg-info/requires.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       49 2023-01-13 08:46:52.000000 cikuu-2022.7.9/cikuu.egg-info/top_level.txt
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.081927 cikuu-2022.7.9/dic/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6977 2022-07-22 02:11:49.000000 cikuu-2022.7.9/dic/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      272 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    72703 2022-12-20 06:18:13.000000 cikuu-2022.7.9/dic/adjlist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    15209 2022-12-20 06:18:13.000000 cikuu-2022.7.9/dic/advlist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2036435 2022-06-22 08:01:11.000000 cikuu-2022.7.9/dic/bnc_wordlist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   742662 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/confu_set.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1423371 2022-06-22 08:01:11.000000 cikuu-2022.7.9/dic/ecdic.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8101 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/errants.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   716825 2022-07-13 02:04:15.000000 cikuu-2022.7.9/dic/essays.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   479692 2022-08-23 13:50:08.000000 cikuu-2022.7.9/dic/frame.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1966581 2022-12-20 06:18:14.000000 cikuu-2022.7.9/dic/lemma_lex.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   446749 2022-09-10 08:16:22.000000 cikuu-2022.7.9/dic/lemma_mf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   182701 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/lemma_scale.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1724919 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/lex_lemma.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4088 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/mwe_disconj.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10043 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/mwe_pv.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   173703 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/n_is_sb.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   173515 2022-12-20 13:19:48.000000 cikuu-2022.7.9/dic/nounlist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  3696547 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/nyt_wc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      438 2022-08-27 09:29:39.000000 cikuu-2022.7.9/dic/oneself.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    41916 2022-08-09 12:43:18.000000 cikuu-2022.7.9/dic/orals.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      125 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/poslist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2786732 2022-08-26 03:27:30.000000 cikuu-2022.7.9/dic/propbank.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1350 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/stoplist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      686 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/to_redislite.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    90499 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/verbform.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9125 2022-12-20 06:18:13.000000 cikuu-2022.7.9/dic/verblist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   147209 2022-12-20 13:19:48.000000 cikuu-2022.7.9/dic/verbtag.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   357010 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/vocab.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    42948 2022-07-06 02:32:21.000000 cikuu-2022.7.9/dic/word_awl.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   825665 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/word_bits.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   518752 2022-03-31 02:25:44.000000 cikuu-2022.7.9/dic/word_grade.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    46473 2022-07-06 02:32:21.000000 cikuu-2022.7.9/dic/word_gsl1.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    42152 2022-07-06 02:32:21.000000 cikuu-2022.7.9/dic/word_gsl2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2765429 2022-07-06 02:32:21.000000 cikuu-2022.7.9/dic/word_idf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  2717304 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/word_oov.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  3086978 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/word_pos.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   182843 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/word_scale.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  4370200 2022-07-13 02:04:15.000000 cikuu-2022.7.9/dic/wordattr.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   300932 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/wordcnt.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   353846 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/wordlist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   957421 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/wordlist_ed1.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   100665 2022-03-07 08:36:18.000000 cikuu-2022.7.9/dic/wordnet_verb.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)  1150605 2022-09-01 06:07:31.000000 cikuu-2022.7.9/dic/wordpos.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    53593 2023-01-07 02:36:14.000000 cikuu-2022.7.9/dic/words.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.085927 cikuu-2022.7.9/dsk/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7973 2022-06-05 09:00:34.000000 cikuu-2022.7.9/dsk/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4196 2022-06-03 13:28:31.000000 cikuu-2022.7.9/dsk/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    94356 2022-12-20 06:18:13.000000 cikuu-2022.7.9/dsk/common.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5471 2022-04-06 06:57:43.000000 cikuu-2022.7.9/dsk/dm.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      303 2022-08-23 13:50:08.000000 cikuu-2022.7.9/dsk/dsk-hello.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4928 2022-06-17 01:02:19.000000 cikuu-2022.7.9/dsk/dsk-to-dskmkf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3970 2022-03-15 09:37:05.000000 cikuu-2022.7.9/dsk/dskapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3816 2022-04-16 07:48:05.000000 cikuu-2022.7.9/dsk/dskes.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4444 2022-06-05 09:00:34.000000 cikuu-2022.7.9/dsk/dskmkf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6148 2022-07-13 08:16:31.000000 cikuu-2022.7.9/dsk/dskmkf_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5410 2022-07-04 05:52:45.000000 cikuu-2022.7.9/dsk/dskmkf_fastapi2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2465 2022-04-16 07:48:05.000000 cikuu-2022.7.9/dsk/dsktrain.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7228 2022-03-31 02:25:44.000000 cikuu-2022.7.9/dsk/essaydm.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      899 2022-05-29 08:25:02.000000 cikuu-2022.7.9/dsk/gears-xdsk.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4284 2022-04-07 03:53:53.000000 cikuu-2022.7.9/dsk/gecv1.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7911 2022-12-20 06:18:14.000000 cikuu-2022.7.9/dsk/index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6162 2022-11-21 12:23:43.000000 cikuu-2022.7.9/dsk/innersim.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6946 2022-06-28 13:01:07.000000 cikuu-2022.7.9/dsk/json-to-dskmkf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9243 2022-06-26 02:55:41.000000 cikuu-2022.7.9/dsk/kvrdsk.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1478 2022-06-17 01:02:19.000000 cikuu-2022.7.9/dsk/load.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8998 2022-12-20 06:18:14.000000 cikuu-2022.7.9/dsk/mkf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1498 2022-06-05 02:40:48.000000 cikuu-2022.7.9/dsk/mqconsume.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    83132 2022-03-24 03:57:57.000000 cikuu-2022.7.9/dsk/pingyu.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3416 2022-10-30 06:51:36.000000 cikuu-2022.7.9/dsk/score.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6150 2022-04-11 14:40:50.000000 cikuu-2022.7.9/dsk/sntsdims.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      936 2022-12-20 06:18:14.000000 cikuu-2022.7.9/dsk/test.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2220 2022-08-25 03:56:00.000000 cikuu-2022.7.9/dsk/tok-hello.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3629 2022-06-19 12:35:53.000000 cikuu-2022.7.9/dsk/uvidsk.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6616 2022-11-21 12:24:05.000000 cikuu-2022.7.9/dsk/wps-gec.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13784 2022-12-20 06:18:14.000000 cikuu-2022.7.9/dsk/wps-xgec.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9689 2022-10-23 06:39:16.000000 cikuu-2022.7.9/dsk/xessay.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10368 2022-11-21 12:23:43.000000 cikuu-2022.7.9/dsk/xgecv1-test.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8578 2022-11-21 12:24:05.000000 cikuu-2022.7.9/dsk/xgecv1.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4396 2022-04-10 09:34:49.000000 cikuu-2022.7.9/dsk/xmkf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2902 2022-11-26 02:05:30.000000 cikuu-2022.7.9/dsk/xsnt-gec.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2186 2022-11-26 02:05:30.000000 cikuu-2022.7.9/dsk/xsnt-spacy.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.089927 cikuu-2022.7.9/en/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    36393 2023-01-13 08:46:09.000000 cikuu-2022.7.9/en/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5503 2022-08-09 12:43:18.000000 cikuu-2022.7.9/en/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6169 2022-04-04 13:55:29.000000 cikuu-2022.7.9/en/annotate.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      701 2022-11-21 12:23:43.000000 cikuu-2022.7.9/en/c4-cl.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3675 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/c4-fts.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      999 2022-11-26 02:05:30.000000 cikuu-2022.7.9/en/c4-gram-upload.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      984 2022-11-21 12:24:05.000000 cikuu-2022.7.9/en/c4-gram.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      875 2022-11-26 02:05:30.000000 cikuu-2022.7.9/en/c4-grams.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      768 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/c4-np.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      482 2022-09-10 08:16:21.000000 cikuu-2022.7.9/en/c4-postag.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      589 2022-10-04 11:04:51.000000 cikuu-2022.7.9/en/c4-trp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2039 2022-10-30 06:51:37.000000 cikuu-2022.7.9/en/c4cl.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      491 2022-09-10 08:16:21.000000 cikuu-2022.7.9/en/c4down.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1884 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/c4gram-mysql.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2812 2022-12-20 06:18:13.000000 cikuu-2022.7.9/en/c4gram-upsert.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1731 2022-11-21 12:23:43.000000 cikuu-2022.7.9/en/c4gram.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1401 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/c4np.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3683 2022-09-02 03:25:13.000000 cikuu-2022.7.9/en/c4postag.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2243 2022-08-23 13:50:08.000000 cikuu-2022.7.9/en/c4skenp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1096 2023-01-07 02:36:14.000000 cikuu-2022.7.9/en/c4tree.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1235 2023-01-07 02:36:14.000000 cikuu-2022.7.9/en/c4trp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1023 2022-10-23 06:39:16.000000 cikuu-2022.7.9/en/c4vp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      811 2022-06-12 03:36:11.000000 cikuu-2022.7.9/en/clause.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6120 2022-05-28 13:45:17.000000 cikuu-2022.7.9/en/dims.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16963 2022-04-04 09:44:40.000000 cikuu-2022.7.9/en/docfts.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8115 2022-08-19 07:35:05.000000 cikuu-2022.7.9/en/docjson.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3124 2022-07-10 08:29:01.000000 cikuu-2022.7.9/en/esbulk.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3777 2022-07-04 07:06:48.000000 cikuu-2022.7.9/en/esfile.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6311 2022-09-10 08:16:21.000000 cikuu-2022.7.9/en/esjson.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3506 2022-06-04 12:54:20.000000 cikuu-2022.7.9/en/exchunk.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1159 2022-06-04 12:54:20.000000 cikuu-2022.7.9/en/exphrase.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1387 2022-06-04 12:54:20.000000 cikuu-2022.7.9/en/extrp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4656 2022-06-01 01:31:35.000000 cikuu-2022.7.9/en/havc.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      181 2022-03-24 15:21:17.000000 cikuu-2022.7.9/en/hello.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18434 2022-08-09 12:43:18.000000 cikuu-2022.7.9/en/kpsi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4234 2022-05-11 12:11:59.000000 cikuu-2022.7.9/en/lempostag.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1185 2022-03-07 08:36:18.000000 cikuu-2022.7.9/en/nlp-lit.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4581 2022-03-20 14:20:59.000000 cikuu-2022.7.9/en/nlp-lmdb.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1900 2022-03-07 08:36:18.000000 cikuu-2022.7.9/en/postag.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2142 2022-05-28 04:33:34.000000 cikuu-2022.7.9/en/shav.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4531 2022-07-06 02:32:21.000000 cikuu-2022.7.9/en/silite.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1506 2022-10-04 11:05:23.000000 cikuu-2022.7.9/en/snt-esjson.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3342 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/sntjson-fts.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1257 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/sntjson-innodb.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8237 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/sntjson-mysql.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6901 2022-11-21 12:24:05.000000 cikuu-2022.7.9/en/sntjson-naclite.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      963 2022-12-20 06:18:14.000000 cikuu-2022.7.9/en/sntjson-parse-snt.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      913 2023-01-07 02:36:27.000000 cikuu-2022.7.9/en/sntjson-tosnt.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3888 2023-01-07 02:36:14.000000 cikuu-2022.7.9/en/sntjson-trpx.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2001 2023-01-07 02:36:14.000000 cikuu-2022.7.9/en/sntjson-vp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2612 2022-08-21 09:41:41.000000 cikuu-2022.7.9/en/spacybs-esjson.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    30937 2022-07-09 01:53:45.000000 cikuu-2022.7.9/en/spacybs.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2733 2022-09-10 08:16:22.000000 cikuu-2022.7.9/en/spider-esjson.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    30005 2022-08-19 07:35:05.000000 cikuu-2022.7.9/en/terms.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9544 2022-08-19 07:35:05.000000 cikuu-2022.7.9/en/verbnet.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1874 2022-04-07 03:45:50.000000 cikuu-2022.7.9/en/xsnt.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1093 2022-10-30 06:51:37.000000 cikuu-2022.7.9/en/zset-load.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.093927 cikuu-2022.7.9/lit/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16540 2022-08-25 03:56:00.000000 cikuu-2022.7.9/lit/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1467 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/common.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.093927 cikuu-2022.7.9/lit/es/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5386 2022-08-26 12:42:31.000000 cikuu-2022.7.9/lit/es/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      575 2022-08-21 09:41:41.000000 cikuu-2022.7.9/lit/es/index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      908 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/essay.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      506 2022-06-12 03:36:11.000000 cikuu-2022.7.9/lit/filling.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1905 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/fillmul.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      778 2022-07-30 14:36:22.000000 cikuu-2022.7.9/lit/hello-pages.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      587 2022-05-28 04:33:35.000000 cikuu-2022.7.9/lit/index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      908 2022-06-12 03:35:50.000000 cikuu-2022.7.9/lit/mock-scoring.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.093927 cikuu-2022.7.9/lit/penly/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-08-18 01:17:18.000000 cikuu-2022.7.9/lit/penly/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      575 2022-08-18 01:17:18.000000 cikuu-2022.7.9/lit/penly/index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      716 2022-06-17 01:02:19.000000 cikuu-2022.7.9/lit/penly-resend.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1827 2022-06-17 01:02:19.000000 cikuu-2022.7.9/lit/redis-dump.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1564 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/reorder.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1689 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/restore.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1152 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/scoring.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1109 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/single.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1295 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/sntspolish.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1091 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/sntupgrade.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1000 2022-06-22 08:01:11.000000 cikuu-2022.7.9/lit/student-input.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1002 2022-06-22 10:06:19.000000 cikuu-2022.7.9/lit/teacher-admin.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.093927 cikuu-2022.7.9/lit/yulk/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      668 2022-08-18 01:17:20.000000 cikuu-2022.7.9/lit/yulk/YULK.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16942 2022-12-20 06:18:14.000000 cikuu-2022.7.9/lit/yulk/common.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.093927 cikuu-2022.7.9/lit/yulk/func/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-12-20 06:18:13.000000 cikuu-2022.7.9/lit/yulk/func/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1063 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/func/bipos.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      598 2022-12-20 06:18:14.000000 cikuu-2022.7.9/lit/yulk/func/cola.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16942 2022-12-20 06:18:14.000000 cikuu-2022.7.9/lit/yulk/func/common.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      666 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/func/corpuslist.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      549 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/func/es.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      501 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/func/eshyb.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      581 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/func/given-expect.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      908 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/func/gramx-single.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1256 2022-12-20 06:18:14.000000 cikuu-2022.7.9/lit/yulk/func/lemma.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1912 2022-07-27 09:55:08.000000 cikuu-2022.7.9/lit/yulk/func/lemvs.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1023 2022-08-18 01:17:18.000000 cikuu-2022.7.9/lit/yulk/func/pos.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      793 2022-08-09 12:43:18.000000 cikuu-2022.7.9/lit/yulk/func/posvs.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1925 2022-08-18 01:17:20.000000 cikuu-2022.7.9/lit/yulk/func/style-in-mul.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      313 2022-08-18 01:17:20.000000 cikuu-2022.7.9/lit/yulk/func/style.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      353 2022-08-18 01:17:20.000000 cikuu-2022.7.9/lit/yulk/func/wcloud.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1547 2022-07-27 09:55:08.000000 cikuu-2022.7.9/lit/yulk/func/wordrank.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      684 2022-12-20 06:18:14.000000 cikuu-2022.7.9/lit/yulk/index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1255 2022-12-20 06:18:14.000000 cikuu-2022.7.9/lit/yulk/lemma.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.093927 cikuu-2022.7.9/pipe/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4906 2022-06-05 02:40:48.000000 cikuu-2022.7.9/pipe/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2622 2022-06-05 02:40:48.000000 cikuu-2022.7.9/pipe/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4039 2022-06-14 01:58:07.000000 cikuu-2022.7.9/pipe/redisgec8180.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6514 2022-06-05 07:30:56.000000 cikuu-2022.7.9/pipe/xgecv1.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.093927 cikuu-2022.7.9/sbert/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      255 2022-03-26 03:03:21.000000 cikuu-2022.7.9/sbert/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1316 2022-03-07 08:36:18.000000 cikuu-2022.7.9/sbert/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      613 2022-03-07 08:36:18.000000 cikuu-2022.7.9/sbert/hello.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13086 2022-03-27 14:17:45.000000 cikuu-2022.7.9/sbert/sntvec.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2023-01-13 08:46:52.669944 cikuu-2022.7.9/setup.cfg
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      814 2023-01-13 08:46:09.000000 cikuu-2022.7.9/setup.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.097927 cikuu-2022.7.9/so/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    24493 2023-01-07 10:59:50.000000 cikuu-2022.7.9/so/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18745 2022-09-01 06:07:31.000000 cikuu-2022.7.9/so/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13741 2022-06-19 12:35:53.000000 cikuu-2022.7.9/so/corpusly.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9475 2023-01-07 02:36:14.000000 cikuu-2022.7.9/so/cos.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    17434 2022-03-25 06:34:20.000000 cikuu-2022.7.9/so/esapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2427 2022-07-04 07:06:48.000000 cikuu-2022.7.9/so/eslite.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1317 2022-10-04 11:04:51.000000 cikuu-2022.7.9/so/kps-si.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1559 2023-01-07 02:36:14.000000 cikuu-2022.7.9/so/load.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1404 2022-08-21 09:41:41.000000 cikuu-2022.7.9/so/loadc4.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1746 2022-09-01 06:07:31.000000 cikuu-2022.7.9/so/loades.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1294 2022-09-01 06:07:31.000000 cikuu-2022.7.9/so/sikps.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    21465 2022-03-25 14:36:25.000000 cikuu-2022.7.9/so/sntvec.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.097927 cikuu-2022.7.9/stream/
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.097927 cikuu-2022.7.9/stream/arc/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8233 2022-04-17 09:06:40.000000 cikuu-2022.7.9/stream/arc/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3215 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2850 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/__main__0414.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      332 2022-04-21 06:16:01.000000 cikuu-2022.7.9/stream/arc/consume-stream.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3374 2022-04-17 09:06:40.000000 cikuu-2022.7.9/stream/arc/essay-plusone.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4019 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/ftessay.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1755 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/ftitem.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1757 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/ftsnt-cola.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2795 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/ftsnt.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1629 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/gecsnts.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6579 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/gecv1.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3256 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/mkf.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7761 2022-04-11 14:40:50.000000 cikuu-2022.7.9/stream/arc/realtime.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4878 2022-04-21 06:16:01.000000 cikuu-2022.7.9/stream/arc/uvisse.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4172 2022-04-17 09:06:39.000000 cikuu-2022.7.9/stream/arc/xessay.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3455 2022-05-01 03:27:58.000000 cikuu-2022.7.9/stream/arc/xsnt-spacy.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2773 2022-04-16 15:04:40.000000 cikuu-2022.7.9/stream/arc/xsnts-dsk.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.097927 cikuu-2022.7.9/stream/lit/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-04-21 06:16:01.000000 cikuu-2022.7.9/stream/lit/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      596 2022-05-11 12:11:59.000000 cikuu-2022.7.9/stream/lit/index.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    22837 2022-06-19 12:35:53.000000 cikuu-2022.7.9/stream/uvirun.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.101927 cikuu-2022.7.9/util/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4510 2023-01-13 08:46:09.000000 cikuu-2022.7.9/util/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6002 2022-10-30 06:51:36.000000 cikuu-2022.7.9/util/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4407 2022-03-15 02:34:12.000000 cikuu-2022.7.9/util/annotate.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3455 2022-07-22 02:01:31.000000 cikuu-2022.7.9/util/bcp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2820 2022-03-07 08:36:18.000000 cikuu-2022.7.9/util/c4data.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1748 2022-04-01 12:54:54.000000 cikuu-2022.7.9/util/client-blpop.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     8772 2022-04-04 09:44:40.000000 cikuu-2022.7.9/util/client-xwps.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3219 2022-04-10 09:34:49.000000 cikuu-2022.7.9/util/clientx.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     9342 2022-04-16 07:48:05.000000 cikuu-2022.7.9/util/dsk-util.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      506 2022-04-10 09:34:49.000000 cikuu-2022.7.9/util/fire-test.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      357 2022-03-07 08:36:19.000000 cikuu-2022.7.9/util/frame.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4097 2022-03-13 12:56:09.000000 cikuu-2022.7.9/util/kvr.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1730 2022-03-24 03:57:57.000000 cikuu-2022.7.9/util/mq.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      713 2022-07-22 02:01:31.000000 cikuu-2022.7.9/util/nldp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      796 2022-10-04 11:04:51.000000 cikuu-2022.7.9/util/pubsub-sync.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1665 2022-10-04 11:04:51.000000 cikuu-2022.7.9/util/pubsub2api.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      505 2022-03-07 08:36:19.000000 cikuu-2022.7.9/util/sent-diff.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3123 2022-03-31 02:25:44.000000 cikuu-2022.7.9/util/spider.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      430 2022-03-21 14:12:43.000000 cikuu-2022.7.9/util/sqlite.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      928 2022-03-13 12:56:09.000000 cikuu-2022.7.9/util/sqlitedict-load.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4749 2022-04-01 12:54:54.000000 cikuu-2022.7.9/util/wps-blpop.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    36149 2022-04-01 12:54:54.000000 cikuu-2022.7.9/util/wps.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      485 2022-04-10 09:34:49.000000 cikuu-2022.7.9/util/xfile.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      345 2022-07-22 02:01:31.000000 cikuu-2022.7.9/util/xgec-blpop120.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      371 2022-04-16 07:48:04.000000 cikuu-2022.7.9/util/xrange.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2034 2022-04-02 04:02:08.000000 cikuu-2022.7.9/util/xsnt-spacy.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1521 2022-04-10 09:34:49.000000 cikuu-2022.7.9/util/xstream.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1323 2022-04-04 09:44:40.000000 cikuu-2022.7.9/util/xtest-params.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1404 2022-04-04 09:44:40.000000 cikuu-2022.7.9/util/xtest.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.105927 cikuu-2022.7.9/uvirun/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1083 2022-11-21 12:23:43.000000 cikuu-2022.7.9/uvirun/Jinja2-test.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2151 2022-12-20 06:18:14.000000 cikuu-2022.7.9/uvirun/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2964 2022-12-20 06:18:14.000000 cikuu-2022.7.9/uvirun/__main__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6573 2023-01-07 02:36:27.000000 cikuu-2022.7.9/uvirun/c4es.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4734 2022-07-04 07:06:48.000000 cikuu-2022.7.9/uvirun/cos_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      662 2022-07-22 02:01:31.000000 cikuu-2022.7.9/uvirun/demo_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    22269 2022-11-21 12:23:43.000000 cikuu-2022.7.9/uvirun/dsk_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5335 2022-07-26 01:45:37.000000 cikuu-2022.7.9/uvirun/echart_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4778 2022-12-20 06:18:14.000000 cikuu-2022.7.9/uvirun/elastic_fastapi.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.105927 cikuu-2022.7.9/uvirun/errant/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      813 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7269 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/alignment.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3788 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/annotator.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.105927 cikuu-2022.7.9/uvirun/errant/commands/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/commands/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16344 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/commands/compare_m2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     7343 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/commands/m2_to_m2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3801 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/commands/parallel_to_m2.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2352 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/edit.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2023-01-13 08:46:34.105927 cikuu-2022.7.9/uvirun/errant/en/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        0 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/en/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    16879 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/en/classifier.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    12340 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/en/lancaster.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     5602 2022-09-01 06:07:30.000000 cikuu-2022.7.9/uvirun/errant/en/merger.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10943 2022-11-21 12:23:43.000000 cikuu-2022.7.9/uvirun/errant_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    14040 2022-08-25 03:56:00.000000 cikuu-2022.7.9/uvirun/es1_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    25623 2022-12-20 06:18:14.000000 cikuu-2022.7.9/uvirun/es_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4806 2022-09-10 08:16:21.000000 cikuu-2022.7.9/uvirun/essay_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18036 2022-12-20 06:18:14.000000 cikuu-2022.7.9/uvirun/exchunk_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    18525 2022-11-21 12:24:05.000000 cikuu-2022.7.9/uvirun/feishu_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3561 2022-08-25 03:56:00.000000 cikuu-2022.7.9/uvirun/flair_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1809 2023-01-13 08:46:09.000000 cikuu-2022.7.9/uvirun/ftp.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1010 2022-09-01 06:07:31.000000 cikuu-2022.7.9/uvirun/fusion_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3717 2022-09-10 08:16:22.000000 cikuu-2022.7.9/uvirun/gec_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2850 2022-10-23 06:39:16.000000 cikuu-2022.7.9/uvirun/gec_fastapi_33000.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13116 2022-12-20 06:18:14.000000 cikuu-2022.7.9/uvirun/gensim_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6045 2022-12-20 06:18:14.000000 cikuu-2022.7.9/uvirun/gramx_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2305 2022-07-25 13:51:53.000000 cikuu-2022.7.9/uvirun/hnswlib_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3461 2022-08-09 12:43:20.000000 cikuu-2022.7.9/uvirun/kenlm_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     6264 2022-08-09 12:43:18.000000 cikuu-2022.7.9/uvirun/kpsi_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13096 2023-01-07 02:36:14.000000 cikuu-2022.7.9/uvirun/kvr_dskdm.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    13096 2023-01-07 02:36:15.000000 cikuu-2022.7.9/uvirun/kvr_dskdm1230.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    19126 2022-07-22 02:01:31.000000 cikuu-2022.7.9/uvirun/nldp_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4490 2023-01-07 02:36:27.000000 cikuu-2022.7.9/uvirun/nltk_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1501 2022-09-01 06:07:31.000000 cikuu-2022.7.9/uvirun/nsp_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4343 2022-10-23 06:39:17.000000 cikuu-2022.7.9/uvirun/sbert_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      400 2022-09-01 06:07:31.000000 cikuu-2022.7.9/uvirun/single_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    26665 2023-01-07 02:36:14.000000 cikuu-2022.7.9/uvirun/spacy_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4320 2023-01-07 02:36:15.000000 cikuu-2022.7.9/uvirun/textacy_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     2089 2022-07-22 02:01:31.000000 cikuu-2022.7.9/uvirun/trans_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     3032 2023-01-13 08:46:09.000000 cikuu-2022.7.9/uvirun/unmasker_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4558 2022-09-10 08:16:21.000000 cikuu-2022.7.9/uvirun/util_fastapi.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    45795 2022-10-04 11:04:51.000000 cikuu-2022.7.9/uvirun/uviredis.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    36607 2023-01-13 08:46:09.000000 cikuu-2022.7.9/uvirun/yulk-nac.py
```

### Comparing `cikuu-2022.7.8/api/c4.py` & `cikuu-2022.7.9/api/c4.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/api/chunk.py` & `cikuu-2022.7.9/api/chunk.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/api/common.py` & `cikuu-2022.7.9/api/common.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/api/dm.py` & `cikuu-2022.7.9/api/dm.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/api/es.py` & `cikuu-2022.7.9/api/es.py`

 * *Files 4% similar despite different names*

```diff
@@ -293,16 +293,37 @@
 		print (cp,  rel, flush=True) 
 		arr = rel.strip().split('_') 
 		gov_deps(arr[0], arr[1], arr[2], cp)
 		dep_govs(arr[0], arr[1], arr[2], cp)
 
 	print ("finished:", cp ) 
 
+def dump_trps(cp):
+	''' cp=dic/gzjc, dump trps, one word, one file, => dic/overcome-VERB.json '''
+	ssi = defaultdict(Counter) 
+	words = defaultdict(set) 
+	rows = cursor_rows(f"select glem, gpos, dep, lem, pos, count(*) cnt from {cp} where type='tok' and pos not in ('NUM','PUNCT','PROPN') and lem rlike '[a-z]+' and glem rlike '[a-z]+' and gpos in ('ADJ','ADV','VERB','NOUN') and pos in ('ADJ','ADV','VERB','NOUN','ADP') and dep not in ('ROOT') group by glem, gpos, dep, lem, pos")
+	if not os.path.exists(cp): os.makedirs(cp)
+	print ("started:", cp , len(rows), flush=True) 
+
+	for glem, gpos, dep, lem, pos, cnt in rows: 
+		ssi[f"{glem}:{gpos}:{dep}:{pos}"].update ( { lem: cnt}) 
+		ssi[f"{lem}:{pos}:~{dep}:{gpos}"].update ( { glem: cnt}) 
+		words[f"{glem}:{gpos}"].add (f"{dep}:{pos}")
+		words[f"{lem}:{pos}"].add (f"~{dep}:{gpos}")
+
+	for w, rels in words.items(): 
+		dic = defaultdict(list) 
+		for rel in rels: 
+			dic[rel] = ssi[f"{w}:{rel}"].most_common() 
+		save(dic, f"{cp}/{w.replace(':','-')}.json")
+	print ("finished:", cp ) 
+
 if __name__ == '__main__': 
-	fire.Fire( {"dumpcp":dumpcp} )
+	fire.Fire( {"dumpcp":dumpcp, 'dump_trps':dump_trps} )
 
 '''
 
 GET /c4-*/_search
 {
   "query": {
     "bool": {
```

### Comparing `cikuu-2022.7.8/api/feishu.py` & `cikuu-2022.7.9/api/feishu.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/api/mynac.py` & `cikuu-2022.7.9/api/mynac.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/api/sntjson-es.py` & `cikuu-2022.7.9/api/sntjson-es.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # 2023.1.7, cp from esjson.py 
 import json, traceback,sys, time,  fileinput, os, en, so, fire
 from collections import Counter
 from elasticsearch import Elasticsearch,helpers
 
 def run(infile, index:str=None, batch=200000, refresh:bool=True, eshost='172.17.0.1',esport=9200): 
-	''' python3 sntjson-es.py gzjc.jsonlg.3.4.1.gz'''
+	''' python3 -m api.sntjson-es gzjc.jsonlg.3.4.1.gz'''
 	es	  = Elasticsearch([ f"http://{eshost}:{esport}" ])  
 	if index is None : index = infile.split('.')[0]
 	print(">>load started: " , infile, index, flush=True )
 	if refresh or not es.indices.exists(index=index): 
 		if es.indices.exists(index=index):es.indices.delete(index=index)
 		es.indices.create(index=index, body=so.config)
```

### Comparing `cikuu-2022.7.8/api/wget.py` & `cikuu-2022.7.9/api/wget.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/app/dmdsk/__init__.py` & `cikuu-2022.7.9/app/dmdsk/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/app/dmdsk/app_navbar.py` & `cikuu-2022.7.9/app/dmdsk/app_navbar.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/app/dmdsk/func/lemma.py` & `cikuu-2022.7.9/app/dmdsk/func/lemma.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/app/dmdsk/func/trp.py` & `cikuu-2022.7.9/app/dmdsk/func/trp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/app/dmdsk/index.py` & `cikuu-2022.7.9/app/dmdsk/index.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/cikuu.egg-info/SOURCES.txt` & `cikuu-2022.7.9/cikuu.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/__init__.py` & `cikuu-2022.7.9/dic/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/adjlist.py` & `cikuu-2022.7.9/dic/adjlist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/advlist.py` & `cikuu-2022.7.9/dic/advlist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/bnc_wordlist.py` & `cikuu-2022.7.9/dic/bnc_wordlist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/confu_set.py` & `cikuu-2022.7.9/dic/confu_set.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/ecdic.py` & `cikuu-2022.7.9/dic/ecdic.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/errants.py` & `cikuu-2022.7.9/dic/errants.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/essays.py` & `cikuu-2022.7.9/dic/essays.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/frame.py` & `cikuu-2022.7.9/dic/frame.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/lemma_lex.py` & `cikuu-2022.7.9/dic/lemma_lex.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/lemma_mf.py` & `cikuu-2022.7.9/dic/lemma_mf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/lemma_scale.py` & `cikuu-2022.7.9/dic/lemma_scale.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/lex_lemma.py` & `cikuu-2022.7.9/dic/lex_lemma.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/mwe_disconj.py` & `cikuu-2022.7.9/dic/mwe_disconj.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/mwe_pv.py` & `cikuu-2022.7.9/dic/mwe_pv.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/n_is_sb.py` & `cikuu-2022.7.9/dic/n_is_sb.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/nounlist.py` & `cikuu-2022.7.9/dic/nounlist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/nyt_wc.py` & `cikuu-2022.7.9/dic/nyt_wc.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/orals.py` & `cikuu-2022.7.9/dic/orals.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/propbank.py` & `cikuu-2022.7.9/dic/propbank.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/stoplist.py` & `cikuu-2022.7.9/dic/stoplist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/to_redislite.py` & `cikuu-2022.7.9/dic/to_redislite.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/verbform.py` & `cikuu-2022.7.9/dic/verbform.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/verblist.py` & `cikuu-2022.7.9/dic/verblist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/verbtag.py` & `cikuu-2022.7.9/dic/verbtag.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/vocab.py` & `cikuu-2022.7.9/dic/vocab.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_awl.py` & `cikuu-2022.7.9/dic/word_awl.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_bits.py` & `cikuu-2022.7.9/dic/word_bits.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_grade.py` & `cikuu-2022.7.9/dic/word_grade.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_gsl1.py` & `cikuu-2022.7.9/dic/word_gsl1.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_gsl2.py` & `cikuu-2022.7.9/dic/word_gsl2.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_idf.py` & `cikuu-2022.7.9/dic/word_idf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_oov.py` & `cikuu-2022.7.9/dic/word_oov.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_pos.py` & `cikuu-2022.7.9/dic/word_pos.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/word_scale.py` & `cikuu-2022.7.9/dic/word_scale.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/wordattr.py` & `cikuu-2022.7.9/dic/wordattr.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/wordcnt.py` & `cikuu-2022.7.9/dic/wordcnt.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/wordlist.py` & `cikuu-2022.7.9/dic/wordlist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/wordlist_ed1.py` & `cikuu-2022.7.9/dic/wordlist_ed1.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/wordnet_verb.py` & `cikuu-2022.7.9/dic/wordnet_verb.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/wordpos.py` & `cikuu-2022.7.9/dic/wordpos.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dic/words.py` & `cikuu-2022.7.9/dic/words.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/__init__.py` & `cikuu-2022.7.9/dsk/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/__main__.py` & `cikuu-2022.7.9/dsk/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/common.py` & `cikuu-2022.7.9/dsk/common.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dm.py` & `cikuu-2022.7.9/dsk/dm.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dsk-to-dskmkf.py` & `cikuu-2022.7.9/dsk/dsk-to-dskmkf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dskapi.py` & `cikuu-2022.7.9/dsk/dskapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dskes.py` & `cikuu-2022.7.9/dsk/dskes.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dskmkf.py` & `cikuu-2022.7.9/dsk/dskmkf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dskmkf_fastapi.py` & `cikuu-2022.7.9/dsk/dskmkf_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dskmkf_fastapi2.py` & `cikuu-2022.7.9/dsk/dskmkf_fastapi2.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/dsktrain.py` & `cikuu-2022.7.9/dsk/dsktrain.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/essaydm.py` & `cikuu-2022.7.9/dsk/essaydm.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/gears-xdsk.py` & `cikuu-2022.7.9/dsk/gears-xdsk.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/gecv1.py` & `cikuu-2022.7.9/dsk/gecv1.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/index.py` & `cikuu-2022.7.9/dsk/index.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/innersim.py` & `cikuu-2022.7.9/dsk/innersim.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/json-to-dskmkf.py` & `cikuu-2022.7.9/dsk/json-to-dskmkf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/kvrdsk.py` & `cikuu-2022.7.9/dsk/kvrdsk.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/load.py` & `cikuu-2022.7.9/dsk/load.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/mkf.py` & `cikuu-2022.7.9/dsk/mkf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/mqconsume.py` & `cikuu-2022.7.9/dsk/mqconsume.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/pingyu.py` & `cikuu-2022.7.9/dsk/pingyu.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/score.py` & `cikuu-2022.7.9/dsk/score.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/sntsdims.py` & `cikuu-2022.7.9/dsk/sntsdims.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/test.py` & `cikuu-2022.7.9/dsk/test.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/tok-hello.py` & `cikuu-2022.7.9/dsk/tok-hello.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/uvidsk.py` & `cikuu-2022.7.9/dsk/uvidsk.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/wps-gec.py` & `cikuu-2022.7.9/dsk/wps-gec.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/wps-xgec.py` & `cikuu-2022.7.9/dsk/wps-xgec.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/xessay.py` & `cikuu-2022.7.9/dsk/xessay.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/xgecv1-test.py` & `cikuu-2022.7.9/dsk/xgecv1-test.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/xgecv1.py` & `cikuu-2022.7.9/dsk/xgecv1.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/xmkf.py` & `cikuu-2022.7.9/dsk/xmkf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/xsnt-gec.py` & `cikuu-2022.7.9/dsk/xsnt-gec.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/dsk/xsnt-spacy.py` & `cikuu-2022.7.9/dsk/xsnt-spacy.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/__init__.py` & `cikuu-2022.7.9/en/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -697,14 +697,28 @@
 				_kps.append(f"verbnet:{doc[verbi].pos_}_{doc[verbi].lemma_}:{chunk}")
 
 	for name,ibeg,iend in post_np_matcher(doc): #added 2022.7.25
 		if name in ('v_n_vbn','v_n_adj'): 
 			_kps.append(f"{name}:{doc[ibeg].pos_}_{doc[ibeg].lemma_}:{doc[ibeg].lemma_} {doc[ibeg+1].lemma_} {doc[ibeg+2].text}")
 	return _kps
 
+def merge_prt(doc): 
+	'''I turn off the radio. => turn_off , added 2023.1.13'''
+	if not hasattr(merge_prt, 'matcher'):
+		merge_prt.matcher = Matcher(spacy.nlp.vocab)
+		merge_prt.matcher.add("prt", [[{"POS":"VERB"}, {"POS":"ADP", "DEP":"prt"}]], greedy ='LONGEST')
+	with doc.retokenize() as retokenizer:
+		for name, start, end in merge_prt.matcher(doc):
+			try:
+				attrs = {"pos": doc[start].pos, "tag": doc[start].tag, "dep": doc[start].dep, "lemma":doc[start].lemma_ + "_" + doc[start+1].lemma_, "ent_type": "vprt"}
+				retokenizer.merge(doc[start : end], attrs=attrs)
+			except Exception as e:
+				print ( "merge_prt ex:", e , start, end)
+	return doc
+
 def depmatch(): #from spacy.matcher import Matcher,DependencyMatcher
 	''' 2023.1.6 '''
 	if not hasattr(depmatch,'matcher'): 
 		depmatch.matcher = DependencyMatcher(spacy.nlp.vocab)
 		pattern = {
 			# be thrilled , worried, 
 			"advcl-acomp": [ {"RIGHT_ID": "v", "RIGHT_ATTRS": {"POS": "VERB"}},  { "LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "advcl", "RIGHT_ATTRS": {"DEP": "advcl"} }, { "LEFT_ID": "advcl", "REL_OP": ">","RIGHT_ID": "object", "RIGHT_ATTRS": {"DEP": "acomp"} }] , 
@@ -717,15 +731,15 @@
 			# turn off the light
 			"prt-dobj": [  {"RIGHT_ID": "v","RIGHT_ATTRS": {"POS": "VERB"}},  { "LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "subject", "RIGHT_ATTRS": {"DEP": "prt"} }, { "LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "object", "RIGHT_ATTRS": {"DEP": "dobj"} }],
 			# be happy with
 			"acomp-prep":[ {"RIGHT_ID": "v","RIGHT_ATTRS": {"POS": "VERB"}}, { "LEFT_ID": "v","REL_OP": ">","RIGHT_ID": "acomp","RIGHT_ATTRS": {"DEP": "acomp"}},{  "LEFT_ID": "acomp", "REL_OP": ">", "RIGHT_ID": "prep", "RIGHT_ATTRS": {"DEP": "prep"}}],
 			# be based on
 			"be-vbn-prep":[ {"RIGHT_ID": "v", "RIGHT_ATTRS": {"TAG": "VBN"}}, {"LEFT_ID": "v", "REL_OP": ">","RIGHT_ID": "be","RIGHT_ATTRS": {"LEMMA": "be"} }, { "LEFT_ID": "v", "REL_OP": ">", "RIGHT_ID": "prep", "RIGHT_ATTRS": {"DEP": "prep"}  }],
 			}
-		for name,pat in pattern.items(): matcher.add(name, [pat])
+		for name,pat in pattern.items(): depmatch.matcher.add(name, [pat])
 	return depmatch.matcher 
 	#doc = spacy.nlp("I turn off the light, and it is based on the table.")
 	#for name, ar in matcher(doc) : print(spacy.nlp.vocab[name].text, doc[ar[0]].lemma_, doc[ar[1]].lemma_, doc[ar[2]]) # worry be thrilled
 
 [setattr(builtins, k, v) for k, v in globals().items() if not k.startswith("_") and not '.' in k and not hasattr(builtins,k) ] #setattr(builtins, "spacy", spacy)
 if __name__	== '__main__': 
 	doc = spacy.nlp("It is on the brink, and I am very happy, and I leave these books opened.")
```

### Comparing `cikuu-2022.7.8/en/__main__.py` & `cikuu-2022.7.9/en/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/annotate.py` & `cikuu-2022.7.9/en/annotate.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4-cl.py` & `cikuu-2022.7.9/en/c4-cl.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4-fts.py` & `cikuu-2022.7.9/en/c4-fts.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4-gram-upload.py` & `cikuu-2022.7.9/en/c4-gram-upload.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4-gram.py` & `cikuu-2022.7.9/en/c4-gram.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4-grams.py` & `cikuu-2022.7.9/en/c4-grams.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4-np.py` & `cikuu-2022.7.9/en/c4-np.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4-trp.py` & `cikuu-2022.7.9/en/c4-trp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4cl.py` & `cikuu-2022.7.9/en/c4cl.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4gram-mysql.py` & `cikuu-2022.7.9/en/c4gram-mysql.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4gram-upsert.py` & `cikuu-2022.7.9/en/c4gram-upsert.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4gram.py` & `cikuu-2022.7.9/en/c4gram.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4np.py` & `cikuu-2022.7.9/en/c4np.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4postag.py` & `cikuu-2022.7.9/en/c4postag.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4skenp.py` & `cikuu-2022.7.9/en/c4skenp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4tree.py` & `cikuu-2022.7.9/en/c4tree.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4trp.py` & `cikuu-2022.7.9/en/c4trp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/c4vp.py` & `cikuu-2022.7.9/en/c4vp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/clause.py` & `cikuu-2022.7.9/en/clause.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/dims.py` & `cikuu-2022.7.9/en/dims.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/docfts.py` & `cikuu-2022.7.9/en/docfts.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/docjson.py` & `cikuu-2022.7.9/en/docjson.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/esbulk.py` & `cikuu-2022.7.9/en/esbulk.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/esfile.py` & `cikuu-2022.7.9/en/esfile.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/esjson.py` & `cikuu-2022.7.9/en/esjson.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/exchunk.py` & `cikuu-2022.7.9/en/exchunk.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/exphrase.py` & `cikuu-2022.7.9/en/exphrase.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/extrp.py` & `cikuu-2022.7.9/en/extrp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/havc.py` & `cikuu-2022.7.9/en/havc.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/kpsi.py` & `cikuu-2022.7.9/en/kpsi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/lempostag.py` & `cikuu-2022.7.9/en/lempostag.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/nlp-lit.py` & `cikuu-2022.7.9/en/nlp-lit.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/nlp-lmdb.py` & `cikuu-2022.7.9/en/nlp-lmdb.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/postag.py` & `cikuu-2022.7.9/en/postag.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/shav.py` & `cikuu-2022.7.9/en/shav.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/silite.py` & `cikuu-2022.7.9/en/silite.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/snt-esjson.py` & `cikuu-2022.7.9/en/snt-esjson.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-fts.py` & `cikuu-2022.7.9/en/sntjson-fts.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-innodb.py` & `cikuu-2022.7.9/en/sntjson-innodb.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-mysql.py` & `cikuu-2022.7.9/en/sntjson-mysql.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-naclite.py` & `cikuu-2022.7.9/en/sntjson-naclite.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-parse-snt.py` & `cikuu-2022.7.9/en/sntjson-parse-snt.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-tosnt.py` & `cikuu-2022.7.9/en/sntjson-tosnt.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-trpx.py` & `cikuu-2022.7.9/en/sntjson-trpx.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/sntjson-vp.py` & `cikuu-2022.7.9/en/sntjson-vp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/spacybs-esjson.py` & `cikuu-2022.7.9/en/spacybs-esjson.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/spacybs.py` & `cikuu-2022.7.9/en/spacybs.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/spider-esjson.py` & `cikuu-2022.7.9/en/spider-esjson.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/terms.py` & `cikuu-2022.7.9/en/terms.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/verbnet.py` & `cikuu-2022.7.9/en/verbnet.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/xsnt.py` & `cikuu-2022.7.9/en/xsnt.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/en/zset-load.py` & `cikuu-2022.7.9/en/zset-load.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/__init__.py` & `cikuu-2022.7.9/lit/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/common.py` & `cikuu-2022.7.9/lit/common.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/es/__init__.py` & `cikuu-2022.7.9/lit/es/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/es/index.py` & `cikuu-2022.7.9/lit/es/index.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/essay.py` & `cikuu-2022.7.9/lit/essay.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/fillmul.py` & `cikuu-2022.7.9/lit/fillmul.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/hello-pages.py` & `cikuu-2022.7.9/lit/hello-pages.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/index.py` & `cikuu-2022.7.9/lit/index.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/mock-scoring.py` & `cikuu-2022.7.9/lit/mock-scoring.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/penly/index.py` & `cikuu-2022.7.9/lit/penly/index.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/penly-resend.py` & `cikuu-2022.7.9/lit/penly-resend.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/redis-dump.py` & `cikuu-2022.7.9/lit/redis-dump.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/reorder.py` & `cikuu-2022.7.9/lit/reorder.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/restore.py` & `cikuu-2022.7.9/lit/restore.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/scoring.py` & `cikuu-2022.7.9/lit/scoring.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/single.py` & `cikuu-2022.7.9/lit/single.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/sntspolish.py` & `cikuu-2022.7.9/lit/sntspolish.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/sntupgrade.py` & `cikuu-2022.7.9/lit/sntupgrade.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/student-input.py` & `cikuu-2022.7.9/lit/student-input.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/teacher-admin.py` & `cikuu-2022.7.9/lit/teacher-admin.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/YULK.py` & `cikuu-2022.7.9/lit/yulk/YULK.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/common.py` & `cikuu-2022.7.9/lit/yulk/common.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/bipos.py` & `cikuu-2022.7.9/lit/yulk/func/bipos.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/cola.py` & `cikuu-2022.7.9/lit/yulk/func/cola.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/common.py` & `cikuu-2022.7.9/lit/yulk/func/common.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/corpuslist.py` & `cikuu-2022.7.9/lit/yulk/func/corpuslist.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/es.py` & `cikuu-2022.7.9/lit/yulk/func/es.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/given-expect.py` & `cikuu-2022.7.9/lit/yulk/func/given-expect.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/gramx-single.py` & `cikuu-2022.7.9/lit/yulk/func/gramx-single.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/lemma.py` & `cikuu-2022.7.9/lit/yulk/func/lemma.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/lemvs.py` & `cikuu-2022.7.9/lit/yulk/func/lemvs.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/pos.py` & `cikuu-2022.7.9/lit/yulk/func/pos.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/posvs.py` & `cikuu-2022.7.9/lit/yulk/func/posvs.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/style-in-mul.py` & `cikuu-2022.7.9/lit/yulk/func/style-in-mul.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/func/wordrank.py` & `cikuu-2022.7.9/lit/yulk/func/wordrank.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/index.py` & `cikuu-2022.7.9/lit/yulk/index.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/lit/yulk/lemma.py` & `cikuu-2022.7.9/lit/yulk/lemma.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/pipe/__init__.py` & `cikuu-2022.7.9/pipe/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/pipe/__main__.py` & `cikuu-2022.7.9/pipe/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/pipe/redisgec8180.py` & `cikuu-2022.7.9/pipe/redisgec8180.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/pipe/xgecv1.py` & `cikuu-2022.7.9/pipe/xgecv1.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/sbert/__main__.py` & `cikuu-2022.7.9/sbert/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/sbert/hello.py` & `cikuu-2022.7.9/sbert/hello.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/sbert/sntvec.py` & `cikuu-2022.7.9/sbert/sntvec.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/setup.py` & `cikuu-2022.7.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 # Created Time: 2022-2-13
 #############################################
  
 from setuptools import setup, find_packages
  
 setup(
   name = "cikuu",
-  version = "2022.7.8",
+  version = "2022.7.9",
   keywords = ("pip"),
   description = "cikuu tools",
   long_description = "cikuu tools, commonly used, spacy3.4.1",
   license = "MIT Licence",
  
   url = "http://www.cikuu.com",
   author = "cikuu",
```

### Comparing `cikuu-2022.7.8/so/__init__.py` & `cikuu-2022.7.9/so/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/__main__.py` & `cikuu-2022.7.9/so/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/corpusly.py` & `cikuu-2022.7.9/so/corpusly.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/cos.py` & `cikuu-2022.7.9/so/cos.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/esapi.py` & `cikuu-2022.7.9/so/esapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/eslite.py` & `cikuu-2022.7.9/so/eslite.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/kps-si.py` & `cikuu-2022.7.9/so/kps-si.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/load.py` & `cikuu-2022.7.9/so/load.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/loadc4.py` & `cikuu-2022.7.9/so/loadc4.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/loades.py` & `cikuu-2022.7.9/so/loades.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/sikps.py` & `cikuu-2022.7.9/so/sikps.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/so/sntvec.py` & `cikuu-2022.7.9/so/sntvec.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/__init__.py` & `cikuu-2022.7.9/stream/arc/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/__main__.py` & `cikuu-2022.7.9/stream/arc/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/__main__0414.py` & `cikuu-2022.7.9/stream/arc/__main__0414.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/essay-plusone.py` & `cikuu-2022.7.9/stream/arc/essay-plusone.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/ftessay.py` & `cikuu-2022.7.9/stream/arc/ftessay.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/ftitem.py` & `cikuu-2022.7.9/stream/arc/ftitem.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/ftsnt-cola.py` & `cikuu-2022.7.9/stream/arc/ftsnt-cola.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/ftsnt.py` & `cikuu-2022.7.9/stream/arc/ftsnt.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/gecsnts.py` & `cikuu-2022.7.9/stream/arc/gecsnts.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/gecv1.py` & `cikuu-2022.7.9/stream/arc/gecv1.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/mkf.py` & `cikuu-2022.7.9/stream/arc/mkf.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/realtime.py` & `cikuu-2022.7.9/stream/arc/realtime.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/uvisse.py` & `cikuu-2022.7.9/stream/arc/uvisse.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/xessay.py` & `cikuu-2022.7.9/stream/arc/xessay.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/xsnt-spacy.py` & `cikuu-2022.7.9/stream/arc/xsnt-spacy.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/arc/xsnts-dsk.py` & `cikuu-2022.7.9/stream/arc/xsnts-dsk.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/lit/index.py` & `cikuu-2022.7.9/stream/lit/index.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/stream/uvirun.py` & `cikuu-2022.7.9/stream/uvirun.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/__init__.py` & `cikuu-2022.7.9/util/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,14 +19,16 @@
 		G2 = round(2 * ((a * ln(a / E1)) + (b * ln(b / E2))), 2)
 		if minus or  (minus is None and a * d < b * c): G2 = 0 - G2 #if minus or  (minus is None and a/c < b/d): G2 = 0 - G2
 		return round(G2,1)
 	except Exception as e:
 		print ("likelihood ex:",e, a,b,c,d)
 		return 0
 
+has_zh = lambda s : any([c for c in s if ord(c) > 255])
+
 def logdice(xy, x, y): # https://www.fi.muni.cz/usr/sojka/download/raslan2008/13.pdf
 	return round(14  + ln ( 2 * xy/ (x+y), 2),1)
 #print (logdice( 1, 23, 56) )
 
 def lexlist( lemma='open', sepa="|"):
 	from dic import lemma_lex
 	return sepa.join(list(lemma_lex.lemma_lex.get(lemma, [lemma]))) #opens|openest|opened|opener|opening|open
```

### Comparing `cikuu-2022.7.8/util/__main__.py` & `cikuu-2022.7.9/util/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/annotate.py` & `cikuu-2022.7.9/util/annotate.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/bcp.py` & `cikuu-2022.7.9/util/bcp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/c4data.py` & `cikuu-2022.7.9/util/c4data.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/client-blpop.py` & `cikuu-2022.7.9/util/client-blpop.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/client-xwps.py` & `cikuu-2022.7.9/util/client-xwps.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/clientx.py` & `cikuu-2022.7.9/util/clientx.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/dsk-util.py` & `cikuu-2022.7.9/util/dsk-util.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/kvr.py` & `cikuu-2022.7.9/util/kvr.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/mq.py` & `cikuu-2022.7.9/util/mq.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/nldp.py` & `cikuu-2022.7.9/util/nldp.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/pubsub-sync.py` & `cikuu-2022.7.9/util/pubsub-sync.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/pubsub2api.py` & `cikuu-2022.7.9/util/pubsub2api.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/spider.py` & `cikuu-2022.7.9/util/spider.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/sqlitedict-load.py` & `cikuu-2022.7.9/util/sqlitedict-load.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/wps-blpop.py` & `cikuu-2022.7.9/util/wps-blpop.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/wps.py` & `cikuu-2022.7.9/util/wps.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/xsnt-spacy.py` & `cikuu-2022.7.9/util/xsnt-spacy.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/xstream.py` & `cikuu-2022.7.9/util/xstream.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/xtest-params.py` & `cikuu-2022.7.9/util/xtest-params.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/util/xtest.py` & `cikuu-2022.7.9/util/xtest.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/Jinja2-test.py` & `cikuu-2022.7.9/uvirun/Jinja2-test.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/__init__.py` & `cikuu-2022.7.9/uvirun/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/__main__.py` & `cikuu-2022.7.9/uvirun/__main__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/c4es.py` & `cikuu-2022.7.9/uvirun/c4es.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/cos_fastapi.py` & `cikuu-2022.7.9/uvirun/cos_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/demo_fastapi.py` & `cikuu-2022.7.9/uvirun/demo_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/dsk_fastapi.py` & `cikuu-2022.7.9/uvirun/dsk_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/echart_fastapi.py` & `cikuu-2022.7.9/uvirun/echart_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/elastic_fastapi.py` & `cikuu-2022.7.9/uvirun/elastic_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/__init__.py` & `cikuu-2022.7.9/uvirun/errant/__init__.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/alignment.py` & `cikuu-2022.7.9/uvirun/errant/alignment.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/annotator.py` & `cikuu-2022.7.9/uvirun/errant/annotator.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/commands/compare_m2.py` & `cikuu-2022.7.9/uvirun/errant/commands/compare_m2.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/commands/m2_to_m2.py` & `cikuu-2022.7.9/uvirun/errant/commands/m2_to_m2.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/commands/parallel_to_m2.py` & `cikuu-2022.7.9/uvirun/errant/commands/parallel_to_m2.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/edit.py` & `cikuu-2022.7.9/uvirun/errant/edit.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/en/classifier.py` & `cikuu-2022.7.9/uvirun/errant/en/classifier.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/en/lancaster.py` & `cikuu-2022.7.9/uvirun/errant/en/lancaster.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant/en/merger.py` & `cikuu-2022.7.9/uvirun/errant/en/merger.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/errant_fastapi.py` & `cikuu-2022.7.9/uvirun/errant_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/es1_fastapi.py` & `cikuu-2022.7.9/uvirun/es1_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/es_fastapi.py` & `cikuu-2022.7.9/uvirun/es_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/essay_fastapi.py` & `cikuu-2022.7.9/uvirun/essay_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/exchunk_fastapi.py` & `cikuu-2022.7.9/uvirun/exchunk_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/feishu_fastapi.py` & `cikuu-2022.7.9/uvirun/feishu_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/flair_fastapi.py` & `cikuu-2022.7.9/uvirun/flair_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/fusion_fastapi.py` & `cikuu-2022.7.9/uvirun/fusion_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/gec_fastapi.py` & `cikuu-2022.7.9/uvirun/gec_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/gec_fastapi_33000.py` & `cikuu-2022.7.9/uvirun/gec_fastapi_33000.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/gensim_fastapi.py` & `cikuu-2022.7.9/uvirun/gensim_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/gramx_fastapi.py` & `cikuu-2022.7.9/uvirun/gramx_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/hnswlib_fastapi.py` & `cikuu-2022.7.9/uvirun/hnswlib_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/kenlm_fastapi.py` & `cikuu-2022.7.9/uvirun/kenlm_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/kpsi_fastapi.py` & `cikuu-2022.7.9/uvirun/kpsi_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/kvr_dskdm.py` & `cikuu-2022.7.9/uvirun/kvr_dskdm.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/kvr_dskdm1230.py` & `cikuu-2022.7.9/uvirun/kvr_dskdm1230.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/nldp_fastapi.py` & `cikuu-2022.7.9/uvirun/nldp_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/nltk_fastapi.py` & `cikuu-2022.7.9/uvirun/nltk_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/nsp_fastapi.py` & `cikuu-2022.7.9/uvirun/nsp_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/sbert_fastapi.py` & `cikuu-2022.7.9/uvirun/sbert_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/spacy_fastapi.py` & `cikuu-2022.7.9/uvirun/spacy_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/textacy_fastapi.py` & `cikuu-2022.7.9/uvirun/textacy_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/trans_fastapi.py` & `cikuu-2022.7.9/uvirun/trans_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/unmasker_fastapi.py` & `cikuu-2022.7.9/uvirun/unmasker_fastapi.py`

 * *Files 4% similar despite different names*

```diff
@@ -6,14 +6,20 @@
 	''' model: native/nju/fengtai/sino/sci/gblog/twit	'''
 	from transformers import pipeline
 	if not hasattr(unmasker, model): 
 		setattr(unmasker, model, pipeline('fill-mask', model=f'/data/model/unmasker/distilbert-base-uncased-{model}') )
 	arr = getattr(unmasker, model)(q.replace('*','[MASK]'), top_k = topk) #result: [{'score': 0.03619174659252167, 'token': 8404, 'token_str': 'happiness', 'sequence': 'the goal of life is happiness.'}, {'score': 0.030553610995411873, 'token': 7691, 'token_str': 'survival', 'sequence': 'the goal of life is survival.'}, {'score': 0.016977205872535706, 'token': 12611, 'token_str': 'salvation', 'sequence': 'the goal of life is salvation.'}, {'score': 0.016698481515049934, 'token': 4071, 'token_str': 'freedom', 'sequence': 'the goal of life is freedom.'}, {'score': 0.015267301350831985, 'token': 8499, 'token_str': 'unity', 'sequence': 'the goal of life is unity.'}]
 	return [ dict( row, **{"name": model}) for row in arr ] if verbose else [ {"name": model, "word": row["token_str"], "score": round(row["score"], 4)} for row in arr ]
 
+@app.get('/cloze', tags=["unmasker"])
+def cloze(q:str="The goal of life is *.", model:str='native', topk:int=10): 
+	''' model: native/nju/fengtai/sino/sci/gblog/twit, 2023.1.13	'''
+	rows = unmasker(q, model, topk, True)
+	return {"body": q, "model":model, "topk":topk, "data": [ {"name": row["token_str"], "value": round(row["score"], 4)} for row in rows ] }
+
 @app.get('/unmasker/single', tags=["unmasker"])
 def unmasker_single(body:str="Parents * much importance to education.", options:str="attach,pay,link,apply", sepa:str=",", model:str='native', topk:int=1000): 
 	'''  2022.8.6 '''
 	rows = unmasker(body,  model=model, topk=topk)
 	arr  = options.strip().split(sepa) 
 	return {"rank": [ (row['word'], row['score'], i+1) for i, row in enumerate(rows) if row['word'] in arr ], "cands": rows}
```

### Comparing `cikuu-2022.7.8/uvirun/util_fastapi.py` & `cikuu-2022.7.9/uvirun/util_fastapi.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/uviredis.py` & `cikuu-2022.7.9/uvirun/uviredis.py`

 * *Files identical despite different names*

### Comparing `cikuu-2022.7.8/uvirun/yulk-nac.py` & `cikuu-2022.7.9/uvirun/yulk-nac.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 # 2022.11.25 rhost=172.17.0.1 uvicorn yulk-nac:app --host 0.0.0.0 --reload 
-import json,requests,hashlib,os,time,pymysql,fastapi, uvicorn , random,asyncio, platform, re 
+import json,requests,hashlib,os,time,pymysql,fastapi, uvicorn , random,asyncio, platform, re ,itertools
 from collections import defaultdict, Counter 
 from functools import lru_cache
 from dic import lemma_lex
 from util import likelihood
 from fastapi import Request
 from typing import Optional
 from fastapi import FastAPI, Header
 from fastapi.responses import HTMLResponse, StreamingResponse, PlainTextResponse,  RedirectResponse
 
 app		= globals().get('app', fastapi.FastAPI()) 
 from fastapi.middleware.cors import CORSMiddleware  #https://fastapi.tiangolo.com/zh/tutorial/cors/
 app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)
 
 from fastapi.staticfiles import StaticFiles
+app.mount("/static", StaticFiles(directory="static", html = True), name="static") 
 app.mount("/templates", StaticFiles(directory="templates"), name="templates")
 from fastapi.templating import Jinja2Templates
 templates = Jinja2Templates(directory="templates")
-
+ 
 myhost	= os.getenv("myhost", "172.17.0.1" if not "Windows" in platform.system() else "lab.jukuu.com")
 myport  = int(os.getenv("myport", 3309))
 mydb	= os.getenv("mydb", "nac")
 conn	= pymysql.connect(host=myhost,port=myport,user='root',password='cikuutest!',db=mydb)
 
 def get_cursor(ssdict:bool=False):
 	try:
@@ -357,18 +358,172 @@
 	#{"xAxis":["12a","7p","8p","9p","10p","11p"],"yAxis":[,"Sunday"],"seriesData":[[0,0,5],
 	return {"xAxis": [a for a in attrs.keys()], "yAxis":[v for v in verbs.keys()], "seriesData": rows}
 
 @app.get('/echo')
 def echo_data(data:str="http://minio.penly.cn/yulk/sosnt.html"): 
 	return {"data":data}
 
+@app.post('/es/query', tags=["es"])
+def es_query(q:dict={"query": {"match_all": {}}}, index:str="gzjc", host:str='wrask.com:9200'): 
+	''' 2022.1.10 '''
+	return requests.post(f"http://{host}/{index}/_search", json=q).json() 
+
+@app.post('/es/must_phrase', tags=["es"])
+def es_must_phrase(chunks:list=["too many years", "_idea", "children"], index:str="c4-*", field:str='postag', size:int=10000, host:str='wrask.com:9200'): 
+	''' 2022.1.10 '''
+	return es_query({"query": {
+    "bool": { 
+		"must": [ { "match_phrase": {field: chunk}} for chunk in chunks]
+    }
+  }, "size":size
+}, index=index, host=host)
+
+hit_word = lambda lempostag, terms: any([w for w in lempostag.split('_') if w in terms])
+@app.get('/es/wordmap', tags=["es"])
+def es_wordmap(hybs:str="too many years|_idea", index:str="c4-*", field:str='postag', size:int=10000,  host:str='wrask.com:9200', includes:str='NOUN,idea,time', dumpidx:int=1, topk:int=100): 
+	''' includes: OR term list  '''
+	res = es_must_phrase(hybs.split("|"), index, field, size,host) 
+	terms = set(includes.strip().split(','))
+	si= Counter() 
+	for ar in res['hits']['hits']: 
+		postag = ar['_source'][field]
+		for lempostag in postag.split(' '):
+			if hit_word(lempostag, terms):
+				words = lempostag.split('_')
+				if words[dumpidx].isalpha():  
+					si.update({words[dumpidx]:1})
+	data = [{ "name":s, "value": i} for s,i in si.most_common(topk) ]
+	return {"hybs": hybs, "topk":topk, "includes": includes,  "data": data, "term": [ {"name":term, "value": si.get(term,0) } for term in terms if not term.isupper()]}
+
+addpat	= lambda s : f"{s}_[^ ]*" if not s.startswith('_') else f"[^ ]*{s}[^ ]*"   # if the last one, add $ 
+rehyb   = lambda hyb: ' '.join([ addpat(s) for s in hyb.split()])  #'the_[^ ]* [^ ]*_NNS_[^ ]* of_[^ ]*'
+heads   = lambda chunk:  ' '.join([s.split('_')[0].lower() for s in chunk.split()])		#the_the_DT_DET adventures_adventure_NNS_NOUN of_of_IN_ADP
+@app.get('/es/hybchunk', tags=["es"])
+def hybchunk(hyb:str='the _NNS of', index:str='c4-1', size:int= 1000, topk:int=100, host:str='wrask.com:9200'):
+	''' the _NNS of -> {the books of: 13, the doors of: 7} , added 2021.10.13 '''
+	start = time.time()
+	sql= { "query": {  "match_phrase": { "postag": hyb  } },  "_source": ["postag"], "size":  size}
+	res = requests.post(f"http://{host}/{index}/_search/", json=sql).json()
+	si = Counter()
+	repat = rehyb(hyb)
+	for ar in res['hits']['hits']: 
+		postag =  ar["_source"]['postag']
+		m= re.search(repat,postag) #the_the_DT_DET adventures_adventure_NNS_NOUN of_of_IN_ADP
+		if m : si.update({ heads(m.group()):1})
+	data  = [{"name":s, "value":i} for s,i in si.most_common(topk)]
+	return {"total": res["hits"]["total"]["value"],  "timing": round(time.time() - start, 1), "hyb": hyb, "index":index, "topk":topk, "size":size, "data":data}
+
+poslist = lambda arr: [i for i, term in enumerate(arr) if term.startswith("_") and term[1] >= 'A' and term[1] <= 'Z' and term != '_NP' ]
+@app.get('/es/poscands', tags=["es"])
+def es_poscands(hyb:str='pay _JJ attention to', posidx:int=None, index:str='c4-1', size:int= 1000, topk:int=100, host:str='wrask.com:9200'):
+	''' '''
+	res = hybchunk(hyb, index, size, topk, host=host) 
+	arr = hyb.strip().split() 
+	if posidx is None: posidx = poslist(arr)[0]
+	si = Counter()
+	for s, i in res['data']:
+		try:
+			si.update({ s.split()[posidx]:i})
+		except Exception as ex:
+			print ("poscands, ex:", ex)		
+	res['data'] = [ {"name":s, "value": i} for s,i in si.most_common()]
+	return res 
+
+postag_snt = lambda postag='_^ the_the_DET_DT solution_solution_NOUN_NN is_be_AUX_VBZ':  ' '.join([  ar.split('_')[0] for ar in postag.strip().split()[1:] ])
+@app.get('/es/snts', tags=["es"])
+def es_snts(q="many years early", given:str=None, index='c4-1', size:int=10, postag:bool=False, host:str='wrask.com:9200'):
+	'''  given="the early years" '''
+	arr = [{ "match_phrase": {"postag": q}}]
+	if given is not None and given: arr.append({ "match_phrase": {"postag": given}})
+	res = requests.post(f"http://{host}/{index}/_search/", json={
+		  "query": {"bool": { "must": arr}	}, "size": size 
+		}).json()
+	return {"total": res['hits']['total']['value'],  "data": [ {"snt":postag_snt(snt)} if not postag else snt for snt in [ar['_source']['postag'] for ar in res['hits']['hits'] ] ] }
+
+@app.get('/es/vp/snts', tags=["es"])
+def es_vp_snts(q="_open the door", index='dic', size:int=10, host:str='hw13.jukuu.com:9200'):
+	'''  **open the door** /markdown '''
+	arr = [{ "match_phrase": {"postag": q}}]
+	res = requests.post(f"http://{host}/{index}/_search/", json={"query": {"bool": { "must": arr}	}, "size": size }).json()
+	return {"total": res['hits']['total']['value'],  "data": [ {"snt":postag_snt(snt)}  for snt in [ar['_source']['postag'] for ar in res['hits']['hits'] ] ] }
+
+def cands_product(q='one two/ three/'):
+	''' {'one three', 'one two', 'one two three'} '''
+	if not ' ' in q : return set(q.strip().split('/'))
+	arr = [a.strip().split('/') for a in q.split()]
+	res = [' '.join([a for a in ar if a]) for ar in itertools.product( * arr)]
+	return set( [a.strip() for a in res if ' ' in a]) 
+
+iphrase = lambda q="_be in force", cp='c4-*', field='postag',host='wrask.com:9200': requests.post(f"http://{host}/{cp}/_search", json={   "query": {  "match_phrase": { field: q  }   } } ).json()['hits']['total']['value']
+@app.get('/compare', tags=["es"])
+def compare(q="_discuss about/ the issue", given:str=None, index='c4-1', host:str='wrask.com:9200'):
+	'''  given:str="the early years" '''
+	cands = cands_product(q)
+	data = [ {"name":cand, "value":iphrase(cand, index, host=host)} for cand in cands] if given is None or not given else  [{"name": phrase, "given":given, "value": requests.post(f"http://{host}/{index}/_search/", json={
+  "query": {
+    "bool": {
+      "must": 
+        {"match_phrase": {
+          "postag": phrase
+        }}
+      ,
+      
+       "filter": {
+        "match_phrase": {
+          "postag": given
+        }
+      }
+      
+    }
+  } }).json()["hits"]["total"]["value"] }  for phrase in cands ]
+	return {"q": q, "index":index, "given": "" if given is None or not given else given, "data":data}
+
+@app.get('/phrase-keyness', tags=["es"])
+def phrase_keyness(q="_be in force|_come into force|_go into force|by force|_VERB with force|_be forced to _VERB", head:str='_force', src:str='c4-1', tgt:str='c4-2', host:str='wrask.com:9200'):
+	''' 2023.1.13 '''
+	sum_a = iphrase(head, src, host=host) 
+	sum_b = iphrase(head, tgt, host=host) 
+	hybs  = q.strip().split("|")
+	dic_a = { hyb: iphrase(hyb, src, host=host) for hyb in hybs}
+	dic_b = { hyb: iphrase(hyb, tgt, host=host) for hyb in hybs}
+	data  = [ { "hyb": hyb, src: dic_a.get(hyb,0), tgt: dic_b.get(hyb,0), "sum_a":sum_a, "sum_b":sum_b, "keyness": likelihood(dic_a.get(hyb,0), dic_b.get(hyb,0), sum_a + 0.1, sum_b+0.1) } for hyb in hybs ]
+	return { "q":q, "head":head, "src":src, "tgt": tgt, "host":host, "data":data }
+
+@app.get('/semdis', tags=["cloze"])
+def semdis(cands:str="orange,banana", given:str="apple", sepa:str=','): # add a batch model? 
+	''' http://hw6.jukuu.com:8002/gensim/distance/words?src={given} 2022.1.13 ''' 
+	# [{'word': 'orange', 'distance': 0.6793981790542603},  {'word': 'tree', 'distance': 0.7035310864448547}]
+	rows = requests.post(f'http://hw6.jukuu.com:8002/gensim/distance/words?src={given}', json=cands.strip().split(sepa)).json() 
+	return {"cands":cands, "given": given, "data": [{"name": row['word'], "value":round(row["distance"],4)} for row in rows] }
+
 if __name__ == '__main__':	 
+	print ( es_vp_snts()) 
 	uvicorn.run(app, host='0.0.0.0', port=80)
 
 '''
+GET /c4-*/_search
+{
+  "query": {
+    "bool": {
+      "must": [
+        { "match_phrase": {"postag": "_idea"}},
+        { "match_phrase": {"postag": "children"}},
+        { "match_phrase": {"postag": "the early years"}}
+      ] 
+    }
+  }
+}
+
+var arr = []; 
+for (var row of query1.data.data) {
+    arr.push( {'key' : row[0], 'val' : row[1] } ); 
+}
+return arr;
+
+
 print( yulk_dual("sound:LEX") )
 docker run -d --restart=always --name nac.jukuu.com -p 8000:8000 -e pip=pyecharts -v /data/cikuu/pypi/uvirun/yulk-nac.py:/main.py wrask/uvirun uvicorn main:app --host 0.0.0.0 --reload 
 
 root@172.17.0.1|nac>select * from sino where name in ('age','book');
 +------+------+-------+
 | name | attr | count |
 +------+------+-------+
@@ -423,8 +578,12 @@
 def yulk_subobj(verb:str='consider', cp:str='dic', topk:int=50,): 
 	page = Page(layout=Page.SimplePageLayout)
 	page.add(
         WordCloud().add("", fetchall(f"select attr, count from {cp} where name ='{verb}:VERB:nsubj:NOUN' order by count desc limit {topk}"), word_size_range=[20, 100], shape=SymbolType.DIAMOND).set_global_opts(title_opts=opts.TitleOpts(title=f"NOUNs + {verb}")), 
 		WordCloud().add("", fetchall(f"select attr, count from {cp} where name ='{verb}:VERB:dobj:NOUN' order by count desc limit {topk}"), word_size_range=[20, 100], shape=SymbolType.DIAMOND).set_global_opts(title_opts=opts.TitleOpts(title=f"{verb} + NOUNs")),
     )
 	return HTMLResponse(content=page.render_embed() )
+
+@app.get('/es/hyb', tags=["es"])
+def es_hyb(hyb:str="too many years", index:str="c4-1", field:str='postag', size:int=1000, host:str='wrask.com:9200'): 
+	return es_query({ "query": {"match_phrase": {field: hyb }},  "_source": [field], "size": size}, index=index, host=host)
 '''
```

