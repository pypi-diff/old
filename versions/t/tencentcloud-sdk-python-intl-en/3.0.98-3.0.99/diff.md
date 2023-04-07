# Comparing `tmp/tencentcloud-sdk-python-intl-en-3.0.98.tar.gz` & `tmp/tencentcloud-sdk-python-intl-en-3.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-intl-en-3.0.98.tar", last modified: Tue Oct 13 00:49:56 2020, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-intl-en-3.0.99.tar", last modified: Wed Oct 14 00:51:41 2020, max compression
```

## Comparing `tencentcloud-sdk-python-intl-en-3.0.98.tar` & `tencentcloud-sdk-python-intl-en-3.0.99.tar`

### file list

```diff
@@ -1,341 +1,341 @@
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/
--rw-rw-rw-   0 root         (0) root         (0)       35 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/MANIFEST.in
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/v20191205/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/v20191205/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    71931 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/v20191205/models.py
--rw-rw-rw-   0 root         (0) root         (0)    18072 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/v20191205/ssl_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/v20180711/
--rw-rw-rw-   0 root         (0) root         (0)    13040 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/v20180711/gme_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/v20180711/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    27168 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/v20180711/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/v20180301/
--rw-rw-rw-   0 root         (0) root         (0)     2300 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/v20180301/faceid_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/v20180301/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3971 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/v20180301/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/v20200527/
--rw-rw-rw-   0 root         (0) root         (0)    12457 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/v20200527/mdp_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/v20200527/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    18094 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/v20200527/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    45540 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/v20170312/cbs_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    94693 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/v20170312/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/v20180328/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/v20180328/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   105003 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/v20180328/models.py
--rw-rw-rw-   0 root         (0) root         (0)    46237 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/v20180328/sqlserver_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/v20190819/
--rw-rw-rw-   0 root         (0) root         (0)    32869 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/v20190819/ckafka_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/v20190819/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   103824 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/v20190819/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/v20190304/
--rw-rw-rw-   0 root         (0) root         (0)    20978 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/v20190304/cmq_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/v20190304/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    57177 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/v20190304/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/v20180813/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    25119 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/v20180813/tag_client.py
--rw-rw-rw-   0 root         (0) root         (0)    46720 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/v20180813/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/v20190722/
--rw-rw-rw-   0 root         (0) root         (0)    21134 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/v20190722/trtc_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/v20190722/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    44046 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/v20190722/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/v20190719/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/v20190719/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    45253 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/v20190719/models.py
--rw-rw-rw-   0 root         (0) root         (0)    24943 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/v20190719/cfs_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    36505 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/v20180416/scf_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   107639 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/v20180416/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    39098 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/v20170312/batch_client.py
--rw-rw-rw-   0 root         (0) root         (0)   143184 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/v20170312/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/v20180529/
--rw-rw-rw-   0 root         (0) root         (0)   108727 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/v20180529/gaap_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/v20180529/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   223355 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/v20180529/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/v20180330/
--rw-rw-rw-   0 root         (0) root         (0)    41272 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/v20180330/dts_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/v20180330/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    82549 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/v20180330/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/v20191016/
--rw-rw-rw-   0 root         (0) root         (0)    10132 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/v20191016/dbbrain_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/v20191016/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    26535 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/v20191016/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/v20190103/
--rw-rw-rw-   0 root         (0) root         (0)    12979 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/v20190103/emr_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/v20190103/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    92421 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/v20190103/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/
--rw-rw-rw-   0 root         (0) root         (0)     1984 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/abstract_model.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/http/
--rw-rw-rw-   0 root         (0) root         (0)     4973 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/http/request.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/http/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1557 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/sign.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/exception/
--rw-rw-rw-   0 root         (0) root         (0)      760 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/exception/tencent_cloud_sdk_exception.py
--rw-rw-rw-   0 root         (0) root         (0)       25 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/exception/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11870 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/abstract_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/profile/
--rw-rw-rw-   0 root         (0) root         (0)     1405 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/profile/http_profile.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/profile/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1636 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/profile/client_profile.py
--rw-rw-rw-   0 root         (0) root         (0)     2036 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/credential.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/v20190725/
--rw-rw-rw-   0 root         (0) root         (0)    30578 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/v20190725/mongodb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/v20190725/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    69995 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/v20190725/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/v20190116/
--rw-rw-rw-   0 root         (0) root         (0)    72491 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/v20190116/cam_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/v20190116/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   106029 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/v20190116/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/v20191012/
--rw-rw-rw-   0 root         (0) root         (0)    19197 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/v20191012/ecdn_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/v20191012/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    61718 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/v20191012/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/v20200303/
--rw-rw-rw-   0 root         (0) root         (0)    50680 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/v20200303/iai_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/v20200303/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   152920 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/v20200303/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/v20180410/
--rw-rw-rw-   0 root         (0) root         (0)    14758 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/v20180410/dc_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/v20180410/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    45514 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/v20180410/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/v20180416/
--rw-rw-rw-   0 root         (0) root         (0)    13729 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/v20180416/es_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/v20180416/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    59679 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/v20180416/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)   267495 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/v20170312/vpc_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   457276 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/v20170312/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    34716 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/v20170312/postgres_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    68600 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/v20170312/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    37895 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/v20170312/mariadb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    83987 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/v20170312/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/v20180724/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/v20180724/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   119013 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/v20180724/models.py
--rw-rw-rw-   0 root         (0) root         (0)    23785 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/v20180724/monitor_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/v20170312/
--rw-rw-rw-   0 root         (0) root         (0)    94704 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/v20170312/cvm_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/v20170312/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   238121 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/v20170312/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/v20180813/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/v20180813/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4595 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/v20180813/sts_client.py
--rw-rw-rw-   0 root         (0) root         (0)     9001 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/v20180813/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/v20180419/
--rw-rw-rw-   0 root         (0) root         (0)    64872 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/v20180419/autoscaling_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/v20180419/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   186029 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/v20180419/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/v20180717/
--rw-rw-rw-   0 root         (0) root         (0)   135277 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/v20180717/vod_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/v20180717/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   720129 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/v20180717/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/v20180525/
--rw-rw-rw-   0 root         (0) root         (0)    37908 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/v20180525/tke_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/v20180525/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   111131 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/v20180525/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/v20180317/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/v20180317/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   196568 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/v20180317/models.py
--rw-rw-rw-   0 root         (0) root         (0)    86013 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/v20180317/clb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/v20180709/
--rw-rw-rw-   0 root         (0) root         (0)   126067 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/v20180709/dayu_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/v20180709/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   291827 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/v20180709/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/v20180709/
--rw-rw-rw-   0 root         (0) root         (0)     9651 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/v20180709/billing_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/v20180709/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    43454 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/v20180709/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/v20180808/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/v20180808/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   226259 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/v20180808/models.py
--rw-rw-rw-   0 root         (0) root         (0)    76418 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/v20180808/apigateway_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/v20190319/
--rw-rw-rw-   0 root         (0) root         (0)    15433 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/v20190319/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    28214 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/v20190319/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/v20191112/
--rw-rw-rw-   0 root         (0) root         (0)    15844 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/v20191112/gse_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/v20191112/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    44986 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/v20191112/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/v20181119/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/v20181119/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    27793 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/v20181119/models.py
--rw-rw-rw-   0 root         (0) root         (0)    12566 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/v20181119/ocr_client.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/v20181225/
--rw-rw-rw-   0 root         (0) root         (0)    25858 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/v20181225/organization_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/v20181225/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    25406 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/v20181225/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/v20190711/
--rw-rw-rw-   0 root         (0) root         (0)    23804 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/v20190711/sms_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/v20190711/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    52115 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/v20190711/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      628 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/v20190118/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/v20190118/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    59595 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/v20190118/kms_client.py
--rw-rw-rw-   0 root         (0) root         (0)    70942 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/v20190118/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/v20180801/
--rw-rw-rw-   0 root         (0) root         (0)   132027 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/v20180801/live_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/v20180801/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   252385 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/v20180801/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/v20200326/
--rw-rw-rw-   0 root         (0) root         (0)    27118 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/v20200326/mdl_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/v20200326/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    68208 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/v20200326/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/v20180606/
--rw-rw-rw-   0 root         (0) root         (0)    53983 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/v20180606/cdn_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/v20180606/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   262012 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/v20180606/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/v20170320/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/v20170320/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   115197 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/v20170320/cdb_client.py
--rw-rw-rw-   0 root         (0) root         (0)   255687 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/v20170320/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/v20180228/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/v20180228/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    87097 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/v20180228/yunjing_client.py
--rw-rw-rw-   0 root         (0) root         (0)   150161 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/v20180228/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/v20180412/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/v20180412/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    68159 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/v20180412/redis_client.py
--rw-rw-rw-   0 root         (0) root         (0)   144075 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/v20180412/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/v20180411/
--rw-rw-rw-   0 root         (0) root         (0)    31352 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/v20180411/dcdb_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/v20180411/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    69327 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/v20180411/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/v20190612/
--rw-rw-rw-   0 root         (0) root         (0)    83796 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/v20190612/mps_client.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/v20190612/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)   500241 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/v20190612/models.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/v20190919/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/v20190919/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    17253 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/v20190919/tiw_client.py
--rw-rw-rw-   0 root         (0) root         (0)    41947 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/v20190919/models.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/v20190823/
--rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/v20190823/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    41324 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/v20190823/tcaplusdb_client.py
--rw-rw-rw-   0 root         (0) root         (0)    98201 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/v20190823/models.py
--rw-rw-rw-   0 root         (0) root         (0)     1256 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/setup.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud_sdk_python_intl_en.egg-info/
--rw-rw-rw-   0 root         (0) root         (0)        1 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud_sdk_python_intl_en.egg-info/dependency_links.txt
--rw-rw-rw-   0 root         (0) root         (0)       13 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud_sdk_python_intl_en.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)     1798 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud_sdk_python_intl_en.egg-info/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     8785 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud_sdk_python_intl_en.egg-info/SOURCES.txt
--rw-rw-rw-   0 root         (0) root         (0)      685 2020-10-13 00:49:46.000000 tencentcloud-sdk-python-intl-en-3.0.98/README.rst
--rw-rw-rw-   0 root         (0) root         (0)     1798 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)       88 2020-10-13 00:49:56.000000 tencentcloud-sdk-python-intl-en-3.0.98/setup.cfg
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/
+-rw-rw-rw-   0 root         (0) root         (0)       35 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/MANIFEST.in
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/v20191205/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/v20191205/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    71931 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/v20191205/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    18072 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/v20191205/ssl_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/v20180711/
+-rw-rw-rw-   0 root         (0) root         (0)    13040 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/v20180711/gme_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/v20180711/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    27168 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/v20180711/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/v20180301/
+-rw-rw-rw-   0 root         (0) root         (0)     2300 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/v20180301/faceid_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/v20180301/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3971 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/v20180301/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/v20200527/
+-rw-rw-rw-   0 root         (0) root         (0)    12457 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/v20200527/mdp_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/v20200527/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    18094 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/v20200527/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    45540 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/v20170312/cbs_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    94693 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/v20170312/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/v20180328/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/v20180328/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   105003 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/v20180328/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    46237 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/v20180328/sqlserver_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/v20190819/
+-rw-rw-rw-   0 root         (0) root         (0)    32869 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/v20190819/ckafka_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/v20190819/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   103824 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/v20190819/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/v20190304/
+-rw-rw-rw-   0 root         (0) root         (0)    20978 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/v20190304/cmq_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/v20190304/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    57177 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/v20190304/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/v20180813/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    25119 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/v20180813/tag_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    46720 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/v20180813/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/v20190722/
+-rw-rw-rw-   0 root         (0) root         (0)    21134 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/v20190722/trtc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/v20190722/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    44046 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/v20190722/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/v20190719/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/v20190719/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    45253 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/v20190719/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    24943 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/v20190719/cfs_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    36505 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/v20180416/scf_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   107639 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/v20180416/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    39098 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/v20170312/batch_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   143184 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/v20170312/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/v20180529/
+-rw-rw-rw-   0 root         (0) root         (0)   108727 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/v20180529/gaap_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/v20180529/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   223355 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/v20180529/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/v20180330/
+-rw-rw-rw-   0 root         (0) root         (0)    41272 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/v20180330/dts_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/v20180330/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    82549 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/v20180330/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/v20191016/
+-rw-rw-rw-   0 root         (0) root         (0)    10132 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/v20191016/dbbrain_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/v20191016/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    26535 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/v20191016/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/v20190103/
+-rw-rw-rw-   0 root         (0) root         (0)    12979 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/v20190103/emr_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/v20190103/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    92421 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/v20190103/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/
+-rw-rw-rw-   0 root         (0) root         (0)     1984 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/abstract_model.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/http/
+-rw-rw-rw-   0 root         (0) root         (0)     4973 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/http/request.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/http/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1557 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/sign.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/exception/
+-rw-rw-rw-   0 root         (0) root         (0)      760 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/exception/tencent_cloud_sdk_exception.py
+-rw-rw-rw-   0 root         (0) root         (0)       25 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/exception/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11870 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/abstract_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/profile/
+-rw-rw-rw-   0 root         (0) root         (0)     1405 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/profile/http_profile.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/profile/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1636 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/profile/client_profile.py
+-rw-rw-rw-   0 root         (0) root         (0)     2036 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/credential.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/v20190725/
+-rw-rw-rw-   0 root         (0) root         (0)    30578 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/v20190725/mongodb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/v20190725/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    69995 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/v20190725/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/v20190116/
+-rw-rw-rw-   0 root         (0) root         (0)    72491 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/v20190116/cam_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/v20190116/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   106029 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/v20190116/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/v20191012/
+-rw-rw-rw-   0 root         (0) root         (0)    19197 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/v20191012/ecdn_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/v20191012/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    61718 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/v20191012/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/v20200303/
+-rw-rw-rw-   0 root         (0) root         (0)    50680 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/v20200303/iai_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/v20200303/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   152920 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/v20200303/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/v20180410/
+-rw-rw-rw-   0 root         (0) root         (0)    14758 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/v20180410/dc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/v20180410/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    45514 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/v20180410/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/v20180416/
+-rw-rw-rw-   0 root         (0) root         (0)    13729 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/v20180416/es_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/v20180416/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    59679 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/v20180416/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)   267495 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/v20170312/vpc_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   457276 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/v20170312/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    34716 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/v20170312/postgres_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    68600 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/v20170312/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    37895 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/v20170312/mariadb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    83987 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/v20170312/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/v20180724/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/v20180724/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   119013 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/v20180724/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    23785 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/v20180724/monitor_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/v20170312/
+-rw-rw-rw-   0 root         (0) root         (0)    94704 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/v20170312/cvm_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/v20170312/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   238121 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/v20170312/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/v20180813/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/v20180813/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4595 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/v20180813/sts_client.py
+-rw-rw-rw-   0 root         (0) root         (0)     9001 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/v20180813/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/v20180419/
+-rw-rw-rw-   0 root         (0) root         (0)    64872 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/v20180419/autoscaling_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/v20180419/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   186029 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/v20180419/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/v20180717/
+-rw-rw-rw-   0 root         (0) root         (0)   135277 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/v20180717/vod_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/v20180717/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   720129 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/v20180717/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/v20180525/
+-rw-rw-rw-   0 root         (0) root         (0)    37908 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/v20180525/tke_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/v20180525/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   111131 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/v20180525/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/v20180317/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/v20180317/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   196568 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/v20180317/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    86013 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/v20180317/clb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/v20180709/
+-rw-rw-rw-   0 root         (0) root         (0)   126067 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/v20180709/dayu_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/v20180709/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   291827 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/v20180709/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/v20180709/
+-rw-rw-rw-   0 root         (0) root         (0)     9651 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/v20180709/billing_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/v20180709/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    43454 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/v20180709/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/v20180808/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/v20180808/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   226259 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/v20180808/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    76418 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/v20180808/apigateway_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/v20190319/
+-rw-rw-rw-   0 root         (0) root         (0)    15433 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/v20190319/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    28214 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/v20190319/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/v20191112/
+-rw-rw-rw-   0 root         (0) root         (0)    15844 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/v20191112/gse_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/v20191112/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    44986 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/v20191112/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/v20181119/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/v20181119/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    27793 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/v20181119/models.py
+-rw-rw-rw-   0 root         (0) root         (0)    12566 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/v20181119/ocr_client.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/v20181225/
+-rw-rw-rw-   0 root         (0) root         (0)    25858 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/v20181225/organization_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/v20181225/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    25406 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/v20181225/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/v20190711/
+-rw-rw-rw-   0 root         (0) root         (0)    23804 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/v20190711/sms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/v20190711/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    52115 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/v20190711/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      628 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/v20190118/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/v20190118/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    59595 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/v20190118/kms_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    70942 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/v20190118/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/v20180801/
+-rw-rw-rw-   0 root         (0) root         (0)   132027 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/v20180801/live_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/v20180801/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   252385 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/v20180801/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/v20200326/
+-rw-rw-rw-   0 root         (0) root         (0)    27118 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/v20200326/mdl_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/v20200326/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    68208 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/v20200326/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/v20180606/
+-rw-rw-rw-   0 root         (0) root         (0)    53983 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/v20180606/cdn_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/v20180606/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   262012 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/v20180606/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/v20170320/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/v20170320/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   115197 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/v20170320/cdb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   255687 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/v20170320/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/v20180228/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/v20180228/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    87097 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/v20180228/yunjing_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   150161 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/v20180228/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/v20180412/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/v20180412/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    68159 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/v20180412/redis_client.py
+-rw-rw-rw-   0 root         (0) root         (0)   144075 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/v20180412/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/v20180411/
+-rw-rw-rw-   0 root         (0) root         (0)    31352 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/v20180411/dcdb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/v20180411/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    69327 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/v20180411/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/v20190612/
+-rw-rw-rw-   0 root         (0) root         (0)    83796 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/v20190612/mps_client.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/v20190612/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)   500241 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/v20190612/models.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/v20190919/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/v20190919/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    17253 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/v20190919/tiw_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    41947 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/v20190919/models.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/v20190823/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/v20190823/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    41324 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/v20190823/tcaplusdb_client.py
+-rw-rw-rw-   0 root         (0) root         (0)    98201 2020-10-14 00:51:30.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/v20190823/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     1256 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/setup.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud_sdk_python_intl_en.egg-info/
+-rw-rw-rw-   0 root         (0) root         (0)        1 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud_sdk_python_intl_en.egg-info/dependency_links.txt
+-rw-rw-rw-   0 root         (0) root         (0)       13 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud_sdk_python_intl_en.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)     1798 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud_sdk_python_intl_en.egg-info/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     8785 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud_sdk_python_intl_en.egg-info/SOURCES.txt
+-rw-rw-rw-   0 root         (0) root         (0)      685 2020-10-14 00:51:29.000000 tencentcloud-sdk-python-intl-en-3.0.99/README.rst
+-rw-rw-rw-   0 root         (0) root         (0)     1798 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)       88 2020-10-14 00:51:41.000000 tencentcloud-sdk-python-intl-en-3.0.99/setup.cfg
```

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/v20191205/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/v20191205/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ssl/v20191205/ssl_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ssl/v20191205/ssl_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/v20180711/gme_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/v20180711/gme_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gme/v20180711/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gme/v20180711/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/v20180301/faceid_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/v20180301/faceid_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/faceid/v20180301/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/faceid/v20180301/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/v20200527/mdp_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/v20200527/mdp_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdp/v20200527/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdp/v20200527/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/v20170312/cbs_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/v20170312/cbs_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cbs/v20170312/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cbs/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/v20180328/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/v20180328/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sqlserver/v20180328/sqlserver_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sqlserver/v20180328/sqlserver_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/v20190819/ckafka_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/v20190819/ckafka_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ckafka/v20190819/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ckafka/v20190819/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/v20190304/cmq_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/v20190304/cmq_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cmq/v20190304/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cmq/v20190304/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/v20180813/tag_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/v20180813/tag_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tag/v20180813/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tag/v20180813/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/v20190722/trtc_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/v20190722/trtc_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/trtc/v20190722/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/trtc/v20190722/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/v20190719/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/v20190719/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cfs/v20190719/cfs_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cfs/v20190719/cfs_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/v20180416/scf_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/v20180416/scf_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/scf/v20180416/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/scf/v20180416/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/v20170312/batch_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/v20170312/batch_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/batch/v20170312/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/batch/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/v20180529/gaap_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/v20180529/gaap_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gaap/v20180529/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gaap/v20180529/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/v20180330/dts_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/v20180330/dts_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dts/v20180330/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dts/v20180330/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/v20191016/dbbrain_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/v20191016/dbbrain_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dbbrain/v20191016/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dbbrain/v20191016/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/v20190103/emr_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/v20190103/emr_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/emr/v20190103/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/emr/v20190103/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/abstract_model.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/abstract_model.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/http/request.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/http/request.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/sign.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/sign.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/exception/tencent_cloud_sdk_exception.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/exception/tencent_cloud_sdk_exception.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/abstract_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/abstract_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/profile/http_profile.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/profile/http_profile.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/profile/client_profile.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/profile/client_profile.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/common/credential.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/common/credential.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/v20190725/mongodb_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/v20190725/mongodb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mongodb/v20190725/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mongodb/v20190725/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/v20190116/cam_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/v20190116/cam_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cam/v20190116/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cam/v20190116/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/v20191012/ecdn_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/v20191012/ecdn_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ecdn/v20191012/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ecdn/v20191012/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/v20200303/iai_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/v20200303/iai_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/iai/v20200303/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/iai/v20200303/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/v20180410/dc_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/v20180410/dc_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dc/v20180410/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dc/v20180410/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/v20180416/es_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/v20180416/es_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/es/v20180416/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/es/v20180416/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/v20170312/vpc_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/v20170312/vpc_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vpc/v20170312/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vpc/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/v20170312/postgres_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/v20170312/postgres_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/postgres/v20170312/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/postgres/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/v20170312/mariadb_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/v20170312/mariadb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mariadb/v20170312/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mariadb/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/v20180724/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/v20180724/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/monitor/v20180724/monitor_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/monitor/v20180724/monitor_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/v20170312/cvm_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/v20170312/cvm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cvm/v20170312/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cvm/v20170312/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/v20180813/sts_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/v20180813/sts_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sts/v20180813/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sts/v20180813/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/v20180419/autoscaling_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/v20180419/autoscaling_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/autoscaling/v20180419/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/autoscaling/v20180419/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/v20180717/vod_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/v20180717/vod_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/vod/v20180717/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/vod/v20180717/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/v20180525/tke_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/v20180525/tke_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tke/v20180525/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tke/v20180525/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/v20180317/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/v20180317/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/clb/v20180317/clb_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/clb/v20180317/clb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/v20180709/dayu_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/v20180709/dayu_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dayu/v20180709/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dayu/v20180709/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/v20180709/billing_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/v20180709/billing_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/billing/v20180709/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/billing/v20180709/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/v20180808/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/v20180808/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/apigateway/v20180808/apigateway_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/apigateway/v20180808/apigateway_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/v20190319/cloudaudit_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cloudaudit/v20190319/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cloudaudit/v20190319/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/v20191112/gse_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/v20191112/gse_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/gse/v20191112/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/gse/v20191112/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/v20181119/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/v20181119/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/ocr/v20181119/ocr_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/ocr/v20181119/ocr_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/v20181225/organization_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/v20181225/organization_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/organization/v20181225/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/organization/v20181225/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/v20190711/sms_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/v20190711/sms_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/sms/v20190711/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/sms/v20190711/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/__init__.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,8 +9,8 @@
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-__version__ = '3.0.98'
+__version__ = '3.0.99'
```

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/v20190118/kms_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/v20190118/kms_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/kms/v20190118/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/kms/v20190118/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/v20180801/live_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/v20180801/live_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/live/v20180801/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/live/v20180801/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/v20200326/mdl_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/v20200326/mdl_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mdl/v20200326/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mdl/v20200326/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/v20180606/cdn_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/v20180606/cdn_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdn/v20180606/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdn/v20180606/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/v20170320/cdb_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/v20170320/cdb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/cdb/v20170320/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/cdb/v20170320/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/v20180228/yunjing_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/v20180228/yunjing_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/yunjing/v20180228/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/yunjing/v20180228/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/v20180412/redis_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/v20180412/redis_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/redis/v20180412/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/redis/v20180412/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/v20180411/dcdb_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/v20180411/dcdb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/dcdb/v20180411/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/dcdb/v20180411/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/v20190612/mps_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/v20190612/mps_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/mps/v20190612/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/mps/v20190612/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/v20190919/tiw_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/v20190919/tiw_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tiw/v20190919/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tiw/v20190919/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/v20190823/tcaplusdb_client.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/v20190823/tcaplusdb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud/tcaplusdb/v20190823/models.py` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud/tcaplusdb/v20190823/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/setup.py` & `tencentcloud-sdk-python-intl-en-3.0.99/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud_sdk_python_intl_en.egg-info/PKG-INFO` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud_sdk_python_intl_en.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-intl-en
-Version: 3.0.98
+Version: 3.0.99
 Summary: Tencent Cloud SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python-intl-en
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/tencentcloud_sdk_python_intl_en.egg-info/SOURCES.txt` & `tencentcloud-sdk-python-intl-en-3.0.99/tencentcloud_sdk_python_intl_en.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/README.rst` & `tencentcloud-sdk-python-intl-en-3.0.99/README.rst`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-intl-en-3.0.98/PKG-INFO` & `tencentcloud-sdk-python-intl-en-3.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-intl-en
-Version: 3.0.98
+Version: 3.0.99
 Summary: Tencent Cloud SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python-intl-en
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

