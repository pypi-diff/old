# Comparing `tmp/tccli-intl-en-3.0.98.1.tar.gz` & `tmp/tccli-intl-en-3.0.99.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tccli-intl-en-3.0.98.1.tar", last modified: Tue Oct 13 00:44:00 2020, max compression
+gzip compressed data, was "dist/tccli-intl-en-3.0.99.1.tar", last modified: Wed Oct 14 00:46:16 2020, max compression
```

## Comparing `tccli-intl-en-3.0.98.1.tar` & `tccli-intl-en-3.0.99.1.tar`

### file list

```diff
@@ -1,413 +1,413 @@
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/
--rw-rw-rw-   0 root         (0) root         (0)     2485 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/MANIFEST.in
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/
--rw-rw-rw-   0 root         (0) root         (0)        1 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/dependency_links.txt
--rw-rw-rw-   0 root         (0) root         (0)       58 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/requires.txt
--rw-rw-rw-   0 root         (0) root         (0)       86 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/entry_points.txt
--rw-rw-rw-   0 root         (0) root         (0)        6 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)     2987 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)    10846 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/SOURCES.txt
--rw-rw-rw-   0 root         (0) root         (0)     2655 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/setup.py
--rw-rw-rw-   0 root         (0) root         (0)     1791 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/README.rst
--rw-rw-rw-   0 root         (0) root         (0)     2987 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/PKG-INFO
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/
--rw-rw-rw-   0 root         (0) root         (0)     2589 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/help_command.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ssl/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ssl/v20191205/
--rw-rw-rw-   0 root         (0) root         (0)    83259 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ssl/v20191205/api.json
--rw-rw-rw-   0 root         (0) root         (0)     9522 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ssl/v20191205/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ssl/v20191205/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ssl/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    28877 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ssl/ssl_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/gme/
--rw-rw-rw-   0 root         (0) root         (0)    14177 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gme/gme_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gme/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/gme/v20180711/
--rw-rw-rw-   0 root         (0) root         (0)    36434 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gme/v20180711/api.json
--rw-rw-rw-   0 root         (0) root         (0)     9774 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gme/v20180711/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gme/v20180711/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/faceid/
--rw-rw-rw-   0 root         (0) root         (0)     8126 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/faceid/faceid_client.py
--rw-rw-rw-   0 root         (0) root         (0)      221 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/faceid/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/faceid/v20180301/
--rw-rw-rw-   0 root         (0) root         (0)     4136 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/faceid/v20180301/api.json
--rw-rw-rw-   0 root         (0) root         (0)     1432 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/faceid/v20180301/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/faceid/v20180301/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mdp/
--rw-rw-rw-   0 root         (0) root         (0)    19740 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdp/mdp_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mdp/v20200527/
--rw-rw-rw-   0 root         (0) root         (0)    20425 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdp/v20200527/api.json
--rw-rw-rw-   0 root         (0) root         (0)     3330 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdp/v20200527/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdp/v20200527/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cbs/
--rw-rw-rw-   0 root         (0) root         (0)    48993 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cbs/cbs_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cbs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cbs/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   118118 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cbs/v20170312/api.json
--rw-rw-rw-   0 root         (0) root         (0)    40528 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cbs/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cbs/v20170312/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/sqlserver/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/sqlserver/v20180328/
--rw-rw-rw-   0 root         (0) root         (0)   127333 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sqlserver/v20180328/api.json
--rw-rw-rw-   0 root         (0) root         (0)    24281 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sqlserver/v20180328/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sqlserver/v20180328/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      239 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sqlserver/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    63373 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sqlserver/sqlserver_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ckafka/
--rw-rw-rw-   0 root         (0) root         (0)    47876 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ckafka/ckafka_client.py
--rw-rw-rw-   0 root         (0) root         (0)      221 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ckafka/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ckafka/v20190819/
--rw-rw-rw-   0 root         (0) root         (0)   118380 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ckafka/v20190819/api.json
--rw-rw-rw-   0 root         (0) root         (0)    20150 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ckafka/v20190819/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ckafka/v20190819/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cmq/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cmq/v20190304/
--rw-rw-rw-   0 root         (0) root         (0)    65142 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cmq/v20190304/api.json
--rw-rw-rw-   0 root         (0) root         (0)    21159 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cmq/v20190304/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cmq/v20190304/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    33323 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cmq/cmq_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cmq/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tag/
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tag/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tag/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)    55470 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tag/v20180813/api.json
--rw-rw-rw-   0 root         (0) root         (0)    14460 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tag/v20180813/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tag/v20180813/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    38106 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tag/tag_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/trtc/
--rw-rw-rw-   0 root         (0) root         (0)    26613 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/trtc/trtc_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/trtc/v20190722/
--rw-rw-rw-   0 root         (0) root         (0)    55785 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/trtc/v20190722/api.json
--rw-rw-rw-   0 root         (0) root         (0)    14902 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/trtc/v20190722/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/trtc/v20190722/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/trtc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cfs/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cfs/v20190719/
--rw-rw-rw-   0 root         (0) root         (0)    55592 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cfs/v20190719/api.json
--rw-rw-rw-   0 root         (0) root         (0)     8935 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cfs/v20190719/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cfs/v20190719/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cfs/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    34727 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cfs/cfs_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/scf/
--rw-rw-rw-   0 root         (0) root         (0)    52079 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/scf/scf_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/scf/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)   126899 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/scf/v20180416/api.json
--rw-rw-rw-   0 root         (0) root         (0)    27883 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/scf/v20180416/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/scf/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/scf/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/batch/
--rw-rw-rw-   0 root         (0) root         (0)      215 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/batch/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/batch/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   157804 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/batch/v20170312/api.json
--rw-rw-rw-   0 root         (0) root         (0)    15396 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/batch/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/batch/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    48151 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/batch/batch_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/gaap/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/gaap/v20180529/
--rw-rw-rw-   0 root         (0) root         (0)   262863 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gaap/v20180529/api.json
--rw-rw-rw-   0 root         (0) root         (0)    63189 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gaap/v20180529/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gaap/v20180529/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   133461 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gaap/gaap_client.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gaap/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dts/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dts/v20180330/
--rw-rw-rw-   0 root         (0) root         (0)   103892 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dts/v20180330/api.json
--rw-rw-rw-   0 root         (0) root         (0)    21430 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dts/v20180330/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dts/v20180330/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    50118 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dts/dts_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dbbrain/
--rw-rw-rw-   0 root         (0) root         (0)    17140 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dbbrain/dbbrain_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dbbrain/v20191016/
--rw-rw-rw-   0 root         (0) root         (0)    33024 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dbbrain/v20191016/api.json
--rw-rw-rw-   0 root         (0) root         (0)     4370 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dbbrain/v20191016/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dbbrain/v20191016/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dbbrain/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/emr/
--rw-rw-rw-   0 root         (0) root         (0)    25126 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/emr/emr_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/emr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/emr/v20190103/
--rw-rw-rw-   0 root         (0) root         (0)   107930 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/emr/v20190103/api.json
--rw-rw-rw-   0 root         (0) root         (0)    18152 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/emr/v20190103/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/emr/v20190103/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mongodb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mongodb/v20190725/
--rw-rw-rw-   0 root         (0) root         (0)    85931 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mongodb/v20190725/api.json
--rw-rw-rw-   0 root         (0) root         (0)    22426 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mongodb/v20190725/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mongodb/v20190725/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    42517 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mongodb/mongodb_client.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mongodb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cam/
--rw-rw-rw-   0 root         (0) root         (0)    91440 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cam/cam_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cam/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cam/v20190116/
--rw-rw-rw-   0 root         (0) root         (0)   130650 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cam/v20190116/api.json
--rw-rw-rw-   0 root         (0) root         (0)    25113 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cam/v20190116/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cam/v20190116/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ecdn/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ecdn/v20191012/
--rw-rw-rw-   0 root         (0) root         (0)    71262 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ecdn/v20191012/api.json
--rw-rw-rw-   0 root         (0) root         (0)    11675 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ecdn/v20191012/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ecdn/v20191012/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    27896 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ecdn/ecdn_client.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ecdn/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/iai/
--rw-rw-rw-   0 root         (0) root         (0)    51189 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/iai/iai_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/iai/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/iai/v20200303/
--rw-rw-rw-   0 root         (0) root         (0)   177749 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/iai/v20200303/api.json
--rw-rw-rw-   0 root         (0) root         (0)    70130 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/iai/v20200303/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/iai/v20200303/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dc/
--rw-rw-rw-   0 root         (0) root         (0)    25300 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dc/dc_client.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dc/v20180410/
--rw-rw-rw-   0 root         (0) root         (0)    52443 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dc/v20180410/api.json
--rw-rw-rw-   0 root         (0) root         (0)    10803 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dc/v20180410/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dc/v20180410/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/es/
--rw-rw-rw-   0 root         (0) root         (0)    24437 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/es/es_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/es/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    70156 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/es/v20180416/api.json
--rw-rw-rw-   0 root         (0) root         (0)    16392 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/es/v20180416/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/es/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      197 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/es/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/vpc/
--rw-rw-rw-   0 root         (0) root         (0)   292875 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vpc/vpc_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vpc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/vpc/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   547572 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vpc/v20170312/api.json
--rw-rw-rw-   0 root         (0) root         (0)   158022 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vpc/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vpc/v20170312/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/postgres/
--rw-rw-rw-   0 root         (0) root         (0)    48663 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/postgres/postgres_client.py
--rw-rw-rw-   0 root         (0) root         (0)      233 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/postgres/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/postgres/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    85027 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/postgres/v20170312/api.json
--rw-rw-rw-   0 root         (0) root         (0)    16016 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/postgres/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/postgres/v20170312/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mariadb/
--rw-rw-rw-   0 root         (0) root         (0)    50094 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mariadb/mariadb_client.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mariadb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mariadb/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    99206 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mariadb/v20170312/api.json
--rw-rw-rw-   0 root         (0) root         (0)    22280 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mariadb/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mariadb/v20170312/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/monitor/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/monitor/v20180724/
--rw-rw-rw-   0 root         (0) root         (0)   139884 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/monitor/v20180724/api.json
--rw-rw-rw-   0 root         (0) root         (0)    18766 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/monitor/v20180724/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/monitor/v20180724/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/monitor/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    36636 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/monitor/monitor_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cvm/
--rw-rw-rw-   0 root         (0) root         (0)    99460 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cvm/cvm_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cvm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cvm/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   280622 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cvm/v20170312/api.json
--rw-rw-rw-   0 root         (0) root         (0)   104088 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cvm/v20170312/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cvm/v20170312/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/sts/
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/sts/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)     9757 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sts/v20180813/api.json
--rw-rw-rw-   0 root         (0) root         (0)     2962 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sts/v20180813/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sts/v20180813/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11035 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sts/sts_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/autoscaling/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/autoscaling/v20180419/
--rw-rw-rw-   0 root         (0) root         (0)   206517 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/autoscaling/v20180419/api.json
--rw-rw-rw-   0 root         (0) root         (0)    71988 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/autoscaling/v20180419/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/autoscaling/v20180419/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    81418 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/autoscaling/autoscaling_client.py
--rw-rw-rw-   0 root         (0) root         (0)      251 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/autoscaling/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/vod/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/vod/v20180717/
--rw-rw-rw-   0 root         (0) root         (0)   800782 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vod/v20180717/api.json
--rw-rw-rw-   0 root         (0) root         (0)   152505 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vod/v20180717/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vod/v20180717/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   160104 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vod/vod_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/vod/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tke/
--rw-rw-rw-   0 root         (0) root         (0)    51422 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tke/tke_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tke/v20180525/
--rw-rw-rw-   0 root         (0) root         (0)   122495 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tke/v20180525/api.json
--rw-rw-rw-   0 root         (0) root         (0)    17379 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tke/v20180525/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tke/v20180525/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tke/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/clb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/clb/v20180317/
--rw-rw-rw-   0 root         (0) root         (0)   239125 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/clb/v20180317/api.json
--rw-rw-rw-   0 root         (0) root         (0)    51224 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/clb/v20180317/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/clb/v20180317/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/clb/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    99420 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/clb/clb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dayu/
--rw-rw-rw-   0 root         (0) root         (0)   162489 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dayu/dayu_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dayu/v20180709/
--rw-rw-rw-   0 root         (0) root         (0)   351384 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dayu/v20180709/api.json
--rw-rw-rw-   0 root         (0) root         (0)    88479 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dayu/v20180709/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dayu/v20180709/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dayu/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/billing/
--rw-rw-rw-   0 root         (0) root         (0)    17592 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/billing/billing_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/billing/v20180709/
--rw-rw-rw-   0 root         (0) root         (0)    53558 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/billing/v20180709/api.json
--rw-rw-rw-   0 root         (0) root         (0)     6684 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/billing/v20180709/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/billing/v20180709/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/billing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/apigateway/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/apigateway/v20180808/
--rw-rw-rw-   0 root         (0) root         (0)   257506 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/apigateway/v20180808/api.json
--rw-rw-rw-   0 root         (0) root         (0)    48532 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/apigateway/v20180808/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/apigateway/v20180808/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      245 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/apigateway/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    99496 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/apigateway/apigateway_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/
--rw-rw-rw-   0 root         (0) root         (0)    23828 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/cloudaudit_client.py
--rw-rw-rw-   0 root         (0) root         (0)      245 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/v20190319/
--rw-rw-rw-   0 root         (0) root         (0)    31736 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/v20190319/api.json
--rw-rw-rw-   0 root         (0) root         (0)     7542 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/v20190319/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/v20190319/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/gse/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/gse/v20191112/
--rw-rw-rw-   0 root         (0) root         (0)    49423 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gse/v20191112/api.json
--rw-rw-rw-   0 root         (0) root         (0)     8130 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gse/v20191112/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gse/v20191112/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    25788 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gse/gse_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/gse/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ocr/
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ocr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/ocr/v20181119/
--rw-rw-rw-   0 root         (0) root         (0)    35342 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ocr/v20181119/api.json
--rw-rw-rw-   0 root         (0) root         (0)    11578 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ocr/v20181119/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ocr/v20181119/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    16488 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/ocr/ocr_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/organization/
--rw-rw-rw-   0 root         (0) root         (0)    35067 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/organization/organization_client.py
--rw-rw-rw-   0 root         (0) root         (0)      257 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/organization/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/organization/v20181225/
--rw-rw-rw-   0 root         (0) root         (0)    32971 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/organization/v20181225/api.json
--rw-rw-rw-   0 root         (0) root         (0)     5233 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/organization/v20181225/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/organization/v20181225/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/sms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/sms/v20190711/
--rw-rw-rw-   0 root         (0) root         (0)    62459 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sms/v20190711/api.json
--rw-rw-rw-   0 root         (0) root         (0)    18490 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sms/v20190711/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sms/v20190711/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    31347 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sms/sms_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/sms/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      299 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/kms/
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/kms/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    71532 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/kms/kms_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/kms/v20190118/
--rw-rw-rw-   0 root         (0) root         (0)    88628 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/kms/v20190118/api.json
--rw-rw-rw-   0 root         (0) root         (0)    22561 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/kms/v20190118/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/kms/v20190118/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/live/
--rw-rw-rw-   0 root         (0) root         (0)   157564 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/live/live_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/live/v20180801/
--rw-rw-rw-   0 root         (0) root         (0)   315153 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/live/v20180801/api.json
--rw-rw-rw-   0 root         (0) root         (0)    84845 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/live/v20180801/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/live/v20180801/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/live/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mdl/
--rw-rw-rw-   0 root         (0) root         (0)    37030 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdl/mdl_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdl/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mdl/v20200326/
--rw-rw-rw-   0 root         (0) root         (0)    74966 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdl/v20200326/api.json
--rw-rw-rw-   0 root         (0) root         (0)     8566 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdl/v20200326/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mdl/v20200326/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cdn/
--rw-rw-rw-   0 root         (0) root         (0)    67386 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdn/cdn_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdn/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cdn/v20180606/
--rw-rw-rw-   0 root         (0) root         (0)   286275 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdn/v20180606/api.json
--rw-rw-rw-   0 root         (0) root         (0)    50656 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdn/v20180606/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdn/v20180606/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cdb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/cdb/v20170320/
--rw-rw-rw-   0 root         (0) root         (0)   311322 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdb/v20170320/api.json
--rw-rw-rw-   0 root         (0) root         (0)    71596 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdb/v20170320/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdb/v20170320/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdb/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   137869 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/cdb/cdb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/yunjing/
--rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/yunjing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/yunjing/v20180228/
--rw-rw-rw-   0 root         (0) root         (0)   182613 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/yunjing/v20180228/api.json
--rw-rw-rw-   0 root         (0) root         (0)    26783 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/yunjing/v20180228/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/yunjing/v20180228/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   107113 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/yunjing/yunjing_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/redis/
--rw-rw-rw-   0 root         (0) root         (0)      215 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/redis/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    87871 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/redis/redis_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/redis/v20180412/
--rw-rw-rw-   0 root         (0) root         (0)   180171 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/redis/v20180412/api.json
--rw-rw-rw-   0 root         (0) root         (0)    32280 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/redis/v20180412/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/redis/v20180412/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dcdb/
--rw-rw-rw-   0 root         (0) root         (0)    42221 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dcdb/dcdb_client.py
--rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dcdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/dcdb/v20180411/
--rw-rw-rw-   0 root         (0) root         (0)    88409 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dcdb/v20180411/api.json
--rw-rw-rw-   0 root         (0) root         (0)    18042 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dcdb/v20180411/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/dcdb/v20180411/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mps/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/mps/v20190612/
--rw-rw-rw-   0 root         (0) root         (0)   543204 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mps/v20190612/api.json
--rw-rw-rw-   0 root         (0) root         (0)    68840 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mps/v20190612/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mps/v20190612/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   107990 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mps/mps_client.py
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/mps/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tiw/
--rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tiw/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    25611 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tiw/tiw_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tiw/v20190919/
--rw-rw-rw-   0 root         (0) root         (0)    48776 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tiw/v20190919/api.json
--rw-rw-rw-   0 root         (0) root         (0)     9319 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tiw/v20190919/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tiw/v20190919/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/
--rw-rw-rw-   0 root         (0) root         (0)      239 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    55178 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/tcaplusdb_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/v20190823/
--rw-rw-rw-   0 root         (0) root         (0)   108209 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/v20190823/api.json
--rw-rw-rw-   0 root         (0) root         (0)    16768 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/v20190823/help.py
--rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/v20190823/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2720 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/generatecliskeleton.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/advance/
--rw-rw-rw-   0 root         (0) root         (0)    11514 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/advance/userProfileHandler.py
--rw-rw-rw-   0 root         (0) root         (0)       23 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/advance/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2873 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/advance/userConfigHandler.py
--rw-rw-rw-   0 root         (0) root         (0)      333 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/error_msg.py
--rw-rw-rw-   0 root         (0) root         (0)    16466 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/configure.py
--rw-rw-rw-   0 root         (0) root         (0)     2094 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/style.py
--rw-rw-rw-   0 root         (0) root         (0)    14791 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/table.py
--rw-rw-rw-   0 root         (0) root         (0)     2492 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/main.py
--rw-rw-rw-   0 root         (0) root         (0)     9476 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/document_handler.py
--rw-rw-rw-   0 root         (0) root         (0)     3353 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/cli_input_json.py
--rw-rw-rw-   0 root         (0) root         (0)     2861 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/base_command.py
--rw-rw-rw-   0 root         (0) root         (0)     8004 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/argument.py
--rw-rw-rw-   0 root         (0) root         (0)    11594 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/loaders.py
--rw-rw-rw-   0 root         (0) root         (0)      477 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/exceptions.py
--rw-rw-rw-   0 root         (0) root         (0)    10852 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/command.py
--rw-rw-rw-   0 root         (0) root         (0)       26 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2485 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/utils.py
--rw-rw-rw-   0 root         (0) root         (0)     4222 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/text.py
--rw-rw-rw-   0 root         (0) root         (0)      639 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/options_define.py
--rw-rw-rw-   0 root         (0) root         (0)     6372 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/format_output.py
--rw-rw-rw-   0 root         (0) root         (0)     2466 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/completer.py
--rw-rw-rw-   0 root         (0) root         (0)    26829 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/six.py
--rw-rw-rw-   0 root         (0) root         (0)     5136 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/argparser.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/tccli/colorama/
--rw-rw-rw-   0 root         (0) root         (0)     5267 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/colorama/win32.py
--rw-rw-rw-   0 root         (0) root         (0)     9490 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/colorama/ansitowin32.py
--rw-rw-rw-   0 root         (0) root         (0)     1663 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/colorama/initialise.py
--rw-rw-rw-   0 root         (0) root         (0)      232 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/colorama/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2403 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/colorama/ansi.py
--rw-rw-rw-   0 root         (0) root         (0)     5883 2020-10-13 00:43:49.000000 tccli-intl-en-3.0.98.1/tccli/colorama/winterm.py
--rw-rw-rw-   0 root         (0) root         (0)       88 2020-10-13 00:44:00.000000 tccli-intl-en-3.0.98.1/setup.cfg
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/
+-rw-rw-rw-   0 root         (0) root         (0)     2485 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/MANIFEST.in
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/
+-rw-rw-rw-   0 root         (0) root         (0)        1 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/dependency_links.txt
+-rw-rw-rw-   0 root         (0) root         (0)       58 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/requires.txt
+-rw-rw-rw-   0 root         (0) root         (0)       86 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/entry_points.txt
+-rw-rw-rw-   0 root         (0) root         (0)        6 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)     2987 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)    10846 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/SOURCES.txt
+-rw-rw-rw-   0 root         (0) root         (0)     2655 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/setup.py
+-rw-rw-rw-   0 root         (0) root         (0)     1791 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/README.rst
+-rw-rw-rw-   0 root         (0) root         (0)     2987 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/PKG-INFO
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/
+-rw-rw-rw-   0 root         (0) root         (0)     2589 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/help_command.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ssl/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ssl/v20191205/
+-rw-rw-rw-   0 root         (0) root         (0)    83259 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ssl/v20191205/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     9522 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ssl/v20191205/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ssl/v20191205/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ssl/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    28877 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ssl/ssl_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/gme/
+-rw-rw-rw-   0 root         (0) root         (0)    14177 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gme/gme_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gme/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/gme/v20180711/
+-rw-rw-rw-   0 root         (0) root         (0)    36434 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gme/v20180711/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     9774 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gme/v20180711/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gme/v20180711/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/faceid/
+-rw-rw-rw-   0 root         (0) root         (0)     8126 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/faceid/faceid_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      221 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/faceid/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/faceid/v20180301/
+-rw-rw-rw-   0 root         (0) root         (0)     4136 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/faceid/v20180301/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     1432 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/faceid/v20180301/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/faceid/v20180301/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mdp/
+-rw-rw-rw-   0 root         (0) root         (0)    19740 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdp/mdp_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mdp/v20200527/
+-rw-rw-rw-   0 root         (0) root         (0)    20425 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdp/v20200527/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     3330 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdp/v20200527/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdp/v20200527/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cbs/
+-rw-rw-rw-   0 root         (0) root         (0)    48993 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cbs/cbs_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cbs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cbs/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   118118 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cbs/v20170312/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    40528 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cbs/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cbs/v20170312/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/sqlserver/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/sqlserver/v20180328/
+-rw-rw-rw-   0 root         (0) root         (0)   127333 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sqlserver/v20180328/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    24281 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sqlserver/v20180328/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sqlserver/v20180328/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      239 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sqlserver/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    63373 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sqlserver/sqlserver_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ckafka/
+-rw-rw-rw-   0 root         (0) root         (0)    47876 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ckafka/ckafka_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      221 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ckafka/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ckafka/v20190819/
+-rw-rw-rw-   0 root         (0) root         (0)   118380 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ckafka/v20190819/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    20150 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ckafka/v20190819/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ckafka/v20190819/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cmq/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cmq/v20190304/
+-rw-rw-rw-   0 root         (0) root         (0)    65142 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cmq/v20190304/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    21159 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cmq/v20190304/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cmq/v20190304/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    33323 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cmq/cmq_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cmq/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tag/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tag/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tag/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)    55470 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tag/v20180813/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    14460 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tag/v20180813/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tag/v20180813/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    38106 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tag/tag_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/trtc/
+-rw-rw-rw-   0 root         (0) root         (0)    26613 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/trtc/trtc_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/trtc/v20190722/
+-rw-rw-rw-   0 root         (0) root         (0)    55785 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/trtc/v20190722/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    14902 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/trtc/v20190722/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/trtc/v20190722/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/trtc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cfs/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cfs/v20190719/
+-rw-rw-rw-   0 root         (0) root         (0)    55592 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cfs/v20190719/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     8935 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cfs/v20190719/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cfs/v20190719/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cfs/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    34727 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cfs/cfs_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/scf/
+-rw-rw-rw-   0 root         (0) root         (0)    52079 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/scf/scf_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/scf/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)   126899 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/scf/v20180416/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    27883 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/scf/v20180416/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/scf/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/scf/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/batch/
+-rw-rw-rw-   0 root         (0) root         (0)      215 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/batch/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/batch/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   157804 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/batch/v20170312/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    15396 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/batch/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/batch/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    48151 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/batch/batch_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/gaap/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/gaap/v20180529/
+-rw-rw-rw-   0 root         (0) root         (0)   262863 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gaap/v20180529/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    63189 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gaap/v20180529/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gaap/v20180529/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   133461 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gaap/gaap_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gaap/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dts/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dts/v20180330/
+-rw-rw-rw-   0 root         (0) root         (0)   103892 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dts/v20180330/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    21430 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dts/v20180330/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dts/v20180330/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    50118 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dts/dts_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dbbrain/
+-rw-rw-rw-   0 root         (0) root         (0)    17140 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dbbrain/dbbrain_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dbbrain/v20191016/
+-rw-rw-rw-   0 root         (0) root         (0)    33024 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dbbrain/v20191016/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     4370 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dbbrain/v20191016/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dbbrain/v20191016/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dbbrain/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/emr/
+-rw-rw-rw-   0 root         (0) root         (0)    25126 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/emr/emr_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/emr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/emr/v20190103/
+-rw-rw-rw-   0 root         (0) root         (0)   107930 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/emr/v20190103/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    18152 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/emr/v20190103/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/emr/v20190103/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mongodb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mongodb/v20190725/
+-rw-rw-rw-   0 root         (0) root         (0)    85931 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mongodb/v20190725/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    22426 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mongodb/v20190725/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mongodb/v20190725/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    42517 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mongodb/mongodb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mongodb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cam/
+-rw-rw-rw-   0 root         (0) root         (0)    91440 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cam/cam_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cam/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cam/v20190116/
+-rw-rw-rw-   0 root         (0) root         (0)   130650 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cam/v20190116/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    25113 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cam/v20190116/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cam/v20190116/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ecdn/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ecdn/v20191012/
+-rw-rw-rw-   0 root         (0) root         (0)    71262 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ecdn/v20191012/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    11675 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ecdn/v20191012/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ecdn/v20191012/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    27896 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ecdn/ecdn_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ecdn/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/iai/
+-rw-rw-rw-   0 root         (0) root         (0)    51189 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/iai/iai_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/iai/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/iai/v20200303/
+-rw-rw-rw-   0 root         (0) root         (0)   177749 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/iai/v20200303/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    70130 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/iai/v20200303/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/iai/v20200303/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dc/
+-rw-rw-rw-   0 root         (0) root         (0)    25300 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dc/dc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dc/v20180410/
+-rw-rw-rw-   0 root         (0) root         (0)    52443 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dc/v20180410/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    10803 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dc/v20180410/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dc/v20180410/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/es/
+-rw-rw-rw-   0 root         (0) root         (0)    24437 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/es/es_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/es/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    70156 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/es/v20180416/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    16392 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/es/v20180416/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/es/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      197 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/es/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/vpc/
+-rw-rw-rw-   0 root         (0) root         (0)   292875 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vpc/vpc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vpc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/vpc/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   547572 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vpc/v20170312/api.json
+-rw-rw-rw-   0 root         (0) root         (0)   158022 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vpc/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vpc/v20170312/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/postgres/
+-rw-rw-rw-   0 root         (0) root         (0)    48663 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/postgres/postgres_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      233 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/postgres/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/postgres/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    85027 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/postgres/v20170312/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    16016 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/postgres/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/postgres/v20170312/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mariadb/
+-rw-rw-rw-   0 root         (0) root         (0)    50094 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mariadb/mariadb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mariadb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mariadb/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    99206 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mariadb/v20170312/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    22280 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mariadb/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mariadb/v20170312/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/monitor/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/monitor/v20180724/
+-rw-rw-rw-   0 root         (0) root         (0)   139884 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/monitor/v20180724/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    18766 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/monitor/v20180724/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/monitor/v20180724/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/monitor/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    36636 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/monitor/monitor_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cvm/
+-rw-rw-rw-   0 root         (0) root         (0)    99460 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cvm/cvm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cvm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cvm/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   280622 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cvm/v20170312/api.json
+-rw-rw-rw-   0 root         (0) root         (0)   104088 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cvm/v20170312/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cvm/v20170312/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/sts/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/sts/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)     9757 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sts/v20180813/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     2962 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sts/v20180813/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sts/v20180813/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11035 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sts/sts_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/autoscaling/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/autoscaling/v20180419/
+-rw-rw-rw-   0 root         (0) root         (0)   206517 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/autoscaling/v20180419/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    71988 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/autoscaling/v20180419/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/autoscaling/v20180419/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    81418 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/autoscaling/autoscaling_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      251 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/autoscaling/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/vod/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/vod/v20180717/
+-rw-rw-rw-   0 root         (0) root         (0)   800782 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vod/v20180717/api.json
+-rw-rw-rw-   0 root         (0) root         (0)   152505 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vod/v20180717/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vod/v20180717/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   160104 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vod/vod_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/vod/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tke/
+-rw-rw-rw-   0 root         (0) root         (0)    51422 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tke/tke_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tke/v20180525/
+-rw-rw-rw-   0 root         (0) root         (0)   122495 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tke/v20180525/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    17379 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tke/v20180525/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tke/v20180525/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tke/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/clb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/clb/v20180317/
+-rw-rw-rw-   0 root         (0) root         (0)   239125 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/clb/v20180317/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    51224 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/clb/v20180317/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/clb/v20180317/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/clb/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    99420 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/clb/clb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dayu/
+-rw-rw-rw-   0 root         (0) root         (0)   162489 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dayu/dayu_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dayu/v20180709/
+-rw-rw-rw-   0 root         (0) root         (0)   351384 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dayu/v20180709/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    88479 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dayu/v20180709/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dayu/v20180709/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dayu/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/billing/
+-rw-rw-rw-   0 root         (0) root         (0)    17592 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/billing/billing_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/billing/v20180709/
+-rw-rw-rw-   0 root         (0) root         (0)    53558 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/billing/v20180709/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     6684 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/billing/v20180709/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/billing/v20180709/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/billing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/apigateway/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/apigateway/v20180808/
+-rw-rw-rw-   0 root         (0) root         (0)   257506 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/apigateway/v20180808/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    48532 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/apigateway/v20180808/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/apigateway/v20180808/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      245 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/apigateway/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    99496 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/apigateway/apigateway_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/
+-rw-rw-rw-   0 root         (0) root         (0)    23828 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/cloudaudit_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      245 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/v20190319/
+-rw-rw-rw-   0 root         (0) root         (0)    31736 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/v20190319/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     7542 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/v20190319/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/v20190319/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/gse/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/gse/v20191112/
+-rw-rw-rw-   0 root         (0) root         (0)    49423 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gse/v20191112/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     8130 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gse/v20191112/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gse/v20191112/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    25788 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gse/gse_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/gse/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ocr/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ocr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/ocr/v20181119/
+-rw-rw-rw-   0 root         (0) root         (0)    35342 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ocr/v20181119/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    11578 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ocr/v20181119/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ocr/v20181119/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    16488 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/ocr/ocr_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/organization/
+-rw-rw-rw-   0 root         (0) root         (0)    35067 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/organization/organization_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      257 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/organization/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/organization/v20181225/
+-rw-rw-rw-   0 root         (0) root         (0)    32971 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/organization/v20181225/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     5233 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/organization/v20181225/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/organization/v20181225/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/sms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/sms/v20190711/
+-rw-rw-rw-   0 root         (0) root         (0)    62459 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sms/v20190711/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    18490 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sms/v20190711/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sms/v20190711/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    31347 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sms/sms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/sms/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      299 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/kms/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/kms/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    71532 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/kms/kms_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/kms/v20190118/
+-rw-rw-rw-   0 root         (0) root         (0)    88628 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/kms/v20190118/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    22561 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/kms/v20190118/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/kms/v20190118/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/live/
+-rw-rw-rw-   0 root         (0) root         (0)   157564 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/live/live_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/live/v20180801/
+-rw-rw-rw-   0 root         (0) root         (0)   315153 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/live/v20180801/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    84845 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/live/v20180801/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/live/v20180801/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/live/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mdl/
+-rw-rw-rw-   0 root         (0) root         (0)    37030 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdl/mdl_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdl/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mdl/v20200326/
+-rw-rw-rw-   0 root         (0) root         (0)    74966 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdl/v20200326/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     8566 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdl/v20200326/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mdl/v20200326/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cdn/
+-rw-rw-rw-   0 root         (0) root         (0)    67386 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdn/cdn_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdn/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cdn/v20180606/
+-rw-rw-rw-   0 root         (0) root         (0)   286275 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdn/v20180606/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    50656 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdn/v20180606/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdn/v20180606/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cdb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/cdb/v20170320/
+-rw-rw-rw-   0 root         (0) root         (0)   311322 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdb/v20170320/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    71596 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdb/v20170320/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdb/v20170320/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdb/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   137869 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/cdb/cdb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/yunjing/
+-rw-rw-rw-   0 root         (0) root         (0)      227 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/yunjing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/yunjing/v20180228/
+-rw-rw-rw-   0 root         (0) root         (0)   182613 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/yunjing/v20180228/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    26783 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/yunjing/v20180228/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/yunjing/v20180228/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   107113 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/yunjing/yunjing_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/redis/
+-rw-rw-rw-   0 root         (0) root         (0)      215 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/redis/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    87871 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/redis/redis_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/redis/v20180412/
+-rw-rw-rw-   0 root         (0) root         (0)   180171 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/redis/v20180412/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    32280 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/redis/v20180412/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/redis/v20180412/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dcdb/
+-rw-rw-rw-   0 root         (0) root         (0)    42221 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dcdb/dcdb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      209 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dcdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/dcdb/v20180411/
+-rw-rw-rw-   0 root         (0) root         (0)    88409 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dcdb/v20180411/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    18042 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dcdb/v20180411/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/dcdb/v20180411/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mps/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/mps/v20190612/
+-rw-rw-rw-   0 root         (0) root         (0)   543204 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mps/v20190612/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    68840 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mps/v20190612/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mps/v20190612/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   107990 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mps/mps_client.py
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/mps/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tiw/
+-rw-rw-rw-   0 root         (0) root         (0)      203 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tiw/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    25611 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tiw/tiw_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tiw/v20190919/
+-rw-rw-rw-   0 root         (0) root         (0)    48776 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tiw/v20190919/api.json
+-rw-rw-rw-   0 root         (0) root         (0)     9319 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tiw/v20190919/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tiw/v20190919/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/
+-rw-rw-rw-   0 root         (0) root         (0)      239 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    55178 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/tcaplusdb_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/v20190823/
+-rw-rw-rw-   0 root         (0) root         (0)   108209 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/v20190823/api.json
+-rw-rw-rw-   0 root         (0) root         (0)    16768 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/v20190823/help.py
+-rw-rw-rw-   0 root         (0) root         (0)       22 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/v20190823/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2720 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/generatecliskeleton.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/advance/
+-rw-rw-rw-   0 root         (0) root         (0)    11514 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/advance/userProfileHandler.py
+-rw-rw-rw-   0 root         (0) root         (0)       23 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/advance/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2873 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/advance/userConfigHandler.py
+-rw-rw-rw-   0 root         (0) root         (0)      333 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/error_msg.py
+-rw-rw-rw-   0 root         (0) root         (0)    16466 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/configure.py
+-rw-rw-rw-   0 root         (0) root         (0)     2094 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/style.py
+-rw-rw-rw-   0 root         (0) root         (0)    14791 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/table.py
+-rw-rw-rw-   0 root         (0) root         (0)     2492 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/main.py
+-rw-rw-rw-   0 root         (0) root         (0)     9476 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/document_handler.py
+-rw-rw-rw-   0 root         (0) root         (0)     3353 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/cli_input_json.py
+-rw-rw-rw-   0 root         (0) root         (0)     2861 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/base_command.py
+-rw-rw-rw-   0 root         (0) root         (0)     8004 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/argument.py
+-rw-rw-rw-   0 root         (0) root         (0)    11594 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/loaders.py
+-rw-rw-rw-   0 root         (0) root         (0)      477 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/exceptions.py
+-rw-rw-rw-   0 root         (0) root         (0)    10852 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/command.py
+-rw-rw-rw-   0 root         (0) root         (0)       26 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2485 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     4222 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/text.py
+-rw-rw-rw-   0 root         (0) root         (0)      639 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/options_define.py
+-rw-rw-rw-   0 root         (0) root         (0)     6372 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/format_output.py
+-rw-rw-rw-   0 root         (0) root         (0)     2466 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/completer.py
+-rw-rw-rw-   0 root         (0) root         (0)    26829 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/six.py
+-rw-rw-rw-   0 root         (0) root         (0)     5136 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/argparser.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/tccli/colorama/
+-rw-rw-rw-   0 root         (0) root         (0)     5267 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/colorama/win32.py
+-rw-rw-rw-   0 root         (0) root         (0)     9490 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/colorama/ansitowin32.py
+-rw-rw-rw-   0 root         (0) root         (0)     1663 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/colorama/initialise.py
+-rw-rw-rw-   0 root         (0) root         (0)      232 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/colorama/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2403 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/colorama/ansi.py
+-rw-rw-rw-   0 root         (0) root         (0)     5883 2020-10-14 00:46:04.000000 tccli-intl-en-3.0.99.1/tccli/colorama/winterm.py
+-rw-rw-rw-   0 root         (0) root         (0)       88 2020-10-14 00:46:16.000000 tccli-intl-en-3.0.99.1/setup.cfg
```

### Comparing `tccli-intl-en-3.0.98.1/MANIFEST.in` & `tccli-intl-en-3.0.99.1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/PKG-INFO` & `tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tccli-intl-en
-Version: 3.0.98.1
+Version: 3.0.99.1
 Summary: Universal Command Line Environment for Tencent Cloud
 Home-page: https://github.com/TencentCloud/tencentcloud-cli-intl-en.git
 Author: Tencent Cloud
 Author-email: TencentCloudApi@tencent.com
 License: UNKNOWN
 Description: Install
         =======
```

### Comparing `tccli-intl-en-3.0.98.1/tccli_intl_en.egg-info/SOURCES.txt` & `tccli-intl-en-3.0.99.1/tccli_intl_en.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/setup.py` & `tccli-intl-en-3.0.99.1/setup.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/README.rst` & `tccli-intl-en-3.0.99.1/README.rst`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/PKG-INFO` & `tccli-intl-en-3.0.99.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tccli-intl-en
-Version: 3.0.98.1
+Version: 3.0.99.1
 Summary: Universal Command Line Environment for Tencent Cloud
 Home-page: https://github.com/TencentCloud/tencentcloud-cli-intl-en.git
 Author: Tencent Cloud
 Author-email: TencentCloudApi@tencent.com
 License: UNKNOWN
 Description: Install
         =======
```

### Comparing `tccli-intl-en-3.0.98.1/tccli/help_command.py` & `tccli-intl-en-3.0.99.1/tccli/help_command.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ssl/v20191205/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/ssl/v20191205/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ssl/v20191205/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/ssl/v20191205/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ssl/ssl_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/ssl/ssl_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gme/gme_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/gme/gme_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gme/v20180711/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/gme/v20180711/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gme/v20180711/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/gme/v20180711/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/faceid/faceid_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/faceid/faceid_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/faceid/v20180301/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/faceid/v20180301/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/faceid/v20180301/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/faceid/v20180301/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mdp/mdp_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/mdp/mdp_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mdp/v20200527/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/mdp/v20200527/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mdp/v20200527/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/mdp/v20200527/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cbs/cbs_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cbs/cbs_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cbs/v20170312/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cbs/v20170312/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cbs/v20170312/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cbs/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sqlserver/v20180328/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/sqlserver/v20180328/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sqlserver/v20180328/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/sqlserver/v20180328/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sqlserver/sqlserver_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/sqlserver/sqlserver_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ckafka/ckafka_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/ckafka/ckafka_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ckafka/v20190819/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/ckafka/v20190819/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ckafka/v20190819/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/ckafka/v20190819/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cmq/v20190304/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cmq/v20190304/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cmq/v20190304/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cmq/v20190304/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cmq/cmq_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cmq/cmq_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tag/v20180813/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/tag/v20180813/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tag/v20180813/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/tag/v20180813/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tag/tag_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/tag/tag_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/trtc/trtc_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/trtc/trtc_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/trtc/v20190722/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/trtc/v20190722/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/trtc/v20190722/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/trtc/v20190722/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cfs/v20190719/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cfs/v20190719/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cfs/v20190719/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cfs/v20190719/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cfs/cfs_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cfs/cfs_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/scf/scf_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/scf/scf_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/scf/v20180416/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/scf/v20180416/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/scf/v20180416/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/scf/v20180416/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/batch/v20170312/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/batch/v20170312/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/batch/v20170312/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/batch/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/batch/batch_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/batch/batch_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gaap/v20180529/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/gaap/v20180529/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gaap/v20180529/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/gaap/v20180529/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gaap/gaap_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/gaap/gaap_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dts/v20180330/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/dts/v20180330/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dts/v20180330/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/dts/v20180330/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dts/dts_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/dts/dts_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dbbrain/dbbrain_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/dbbrain/dbbrain_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dbbrain/v20191016/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/dbbrain/v20191016/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dbbrain/v20191016/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/dbbrain/v20191016/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/emr/emr_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/emr/emr_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/emr/v20190103/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/emr/v20190103/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/emr/v20190103/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/emr/v20190103/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mongodb/v20190725/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/mongodb/v20190725/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mongodb/v20190725/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/mongodb/v20190725/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mongodb/mongodb_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/mongodb/mongodb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cam/cam_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cam/cam_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cam/v20190116/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cam/v20190116/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cam/v20190116/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cam/v20190116/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ecdn/v20191012/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/ecdn/v20191012/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ecdn/v20191012/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/ecdn/v20191012/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ecdn/ecdn_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/ecdn/ecdn_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/iai/iai_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/iai/iai_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/iai/v20200303/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/iai/v20200303/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/iai/v20200303/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/iai/v20200303/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dc/dc_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/dc/dc_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dc/v20180410/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/dc/v20180410/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dc/v20180410/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/dc/v20180410/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/es/es_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/es/es_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/es/v20180416/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/es/v20180416/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/es/v20180416/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/es/v20180416/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/vpc/vpc_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/vpc/vpc_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/vpc/v20170312/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/vpc/v20170312/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/vpc/v20170312/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/vpc/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/postgres/postgres_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/postgres/postgres_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/postgres/v20170312/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/postgres/v20170312/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/postgres/v20170312/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/postgres/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mariadb/mariadb_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/mariadb/mariadb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mariadb/v20170312/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/mariadb/v20170312/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mariadb/v20170312/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/mariadb/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/monitor/v20180724/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/monitor/v20180724/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/monitor/v20180724/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/monitor/v20180724/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/monitor/monitor_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/monitor/monitor_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cvm/cvm_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cvm/cvm_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cvm/v20170312/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cvm/v20170312/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cvm/v20170312/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cvm/v20170312/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sts/v20180813/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/sts/v20180813/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sts/v20180813/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/sts/v20180813/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sts/sts_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/sts/sts_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/autoscaling/v20180419/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/autoscaling/v20180419/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/autoscaling/v20180419/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/autoscaling/v20180419/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/autoscaling/autoscaling_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/autoscaling/autoscaling_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/vod/v20180717/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/vod/v20180717/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/vod/v20180717/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/vod/v20180717/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/vod/vod_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/vod/vod_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tke/tke_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/tke/tke_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tke/v20180525/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/tke/v20180525/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tke/v20180525/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/tke/v20180525/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/clb/v20180317/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/clb/v20180317/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/clb/v20180317/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/clb/v20180317/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/clb/clb_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/clb/clb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dayu/dayu_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/dayu/dayu_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dayu/v20180709/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/dayu/v20180709/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dayu/v20180709/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/dayu/v20180709/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/billing/billing_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/billing/billing_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/billing/v20180709/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/billing/v20180709/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/billing/v20180709/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/billing/v20180709/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/apigateway/v20180808/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/apigateway/v20180808/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/apigateway/v20180808/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/apigateway/v20180808/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/apigateway/apigateway_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/apigateway/apigateway_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/cloudaudit_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/cloudaudit_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/v20190319/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/v20190319/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cloudaudit/v20190319/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cloudaudit/v20190319/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gse/v20191112/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/gse/v20191112/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gse/v20191112/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/gse/v20191112/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/gse/gse_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/gse/gse_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ocr/v20181119/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/ocr/v20181119/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ocr/v20181119/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/ocr/v20181119/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/ocr/ocr_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/ocr/ocr_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/organization/organization_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/organization/organization_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/organization/v20181225/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/organization/v20181225/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/organization/v20181225/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/organization/v20181225/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sms/v20190711/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/sms/v20190711/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sms/v20190711/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/sms/v20190711/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/sms/sms_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/sms/sms_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/kms/kms_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/kms/kms_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/kms/v20190118/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/kms/v20190118/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/kms/v20190118/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/kms/v20190118/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/live/live_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/live/live_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/live/v20180801/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/live/v20180801/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/live/v20180801/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/live/v20180801/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mdl/mdl_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/mdl/mdl_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mdl/v20200326/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/mdl/v20200326/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mdl/v20200326/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/mdl/v20200326/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cdn/cdn_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cdn/cdn_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cdn/v20180606/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cdn/v20180606/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cdn/v20180606/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cdn/v20180606/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cdb/v20170320/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/cdb/v20170320/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cdb/v20170320/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/cdb/v20170320/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/cdb/cdb_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/cdb/cdb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/yunjing/v20180228/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/yunjing/v20180228/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/yunjing/v20180228/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/yunjing/v20180228/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/yunjing/yunjing_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/yunjing/yunjing_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/redis/redis_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/redis/redis_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/redis/v20180412/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/redis/v20180412/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/redis/v20180412/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/redis/v20180412/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dcdb/dcdb_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/dcdb/dcdb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dcdb/v20180411/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/dcdb/v20180411/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/dcdb/v20180411/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/dcdb/v20180411/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mps/v20190612/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/mps/v20190612/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mps/v20190612/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/mps/v20190612/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/mps/mps_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/mps/mps_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tiw/tiw_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/tiw/tiw_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tiw/v20190919/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/tiw/v20190919/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tiw/v20190919/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/tiw/v20190919/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/tcaplusdb_client.py` & `tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/tcaplusdb_client.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/v20190823/api.json` & `tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/v20190823/api.json`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/services/tcaplusdb/v20190823/help.py` & `tccli-intl-en-3.0.99.1/tccli/services/tcaplusdb/v20190823/help.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/generatecliskeleton.py` & `tccli-intl-en-3.0.99.1/tccli/generatecliskeleton.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/advance/userProfileHandler.py` & `tccli-intl-en-3.0.99.1/tccli/advance/userProfileHandler.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/advance/userConfigHandler.py` & `tccli-intl-en-3.0.99.1/tccli/advance/userConfigHandler.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/configure.py` & `tccli-intl-en-3.0.99.1/tccli/configure.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/style.py` & `tccli-intl-en-3.0.99.1/tccli/style.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/table.py` & `tccli-intl-en-3.0.99.1/tccli/table.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/main.py` & `tccli-intl-en-3.0.99.1/tccli/main.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/document_handler.py` & `tccli-intl-en-3.0.99.1/tccli/document_handler.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/cli_input_json.py` & `tccli-intl-en-3.0.99.1/tccli/cli_input_json.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/base_command.py` & `tccli-intl-en-3.0.99.1/tccli/base_command.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/argument.py` & `tccli-intl-en-3.0.99.1/tccli/argument.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/loaders.py` & `tccli-intl-en-3.0.99.1/tccli/loaders.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/command.py` & `tccli-intl-en-3.0.99.1/tccli/command.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/utils.py` & `tccli-intl-en-3.0.99.1/tccli/utils.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/text.py` & `tccli-intl-en-3.0.99.1/tccli/text.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/options_define.py` & `tccli-intl-en-3.0.99.1/tccli/options_define.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/format_output.py` & `tccli-intl-en-3.0.99.1/tccli/format_output.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/completer.py` & `tccli-intl-en-3.0.99.1/tccli/completer.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/six.py` & `tccli-intl-en-3.0.99.1/tccli/six.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/argparser.py` & `tccli-intl-en-3.0.99.1/tccli/argparser.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/colorama/win32.py` & `tccli-intl-en-3.0.99.1/tccli/colorama/win32.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/colorama/ansitowin32.py` & `tccli-intl-en-3.0.99.1/tccli/colorama/ansitowin32.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/colorama/initialise.py` & `tccli-intl-en-3.0.99.1/tccli/colorama/initialise.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/colorama/ansi.py` & `tccli-intl-en-3.0.99.1/tccli/colorama/ansi.py`

 * *Files identical despite different names*

### Comparing `tccli-intl-en-3.0.98.1/tccli/colorama/winterm.py` & `tccli-intl-en-3.0.99.1/tccli/colorama/winterm.py`

 * *Files identical despite different names*

